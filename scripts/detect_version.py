#!/usr/bin/env python3
"""Detect the eGovFrame version a project declares and keep a README badge in sync with it.

The project's build files (Maven pom.xml, Gradle build scripts, gradle.properties, version catalogs) are
scanned for the eGovFrame version they declare. The badge between

    <!-- egovframe-badge:start -->  and  <!-- egovframe-badge:end -->

in a README is then rewritten: a project that declares an eGovFrame version gets the version badge, and a
project that declares none gets the name-only badge (no version area).

Exit status: 0 = ok, 1 = --check found an outdated README, 2 = configuration or usage error.
Standard library only, so a project can run it without installing anything.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_BASE = "https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges"
PORTAL = "https://www.egovframe.go.kr/"
STYLES = ("flat", "flat-square", "plastic", "for-the-badge", "outline")
UNVERSIONED = "unversioned"
# Kept equal to scripts/generate.py VERSION_LABELS by tests/test_detect_version.py.
LABELS = {
    "en": "eGovFrame",
    "ko": "전자정부표준프레임워크",
    "es": "Marco Estándar de Gobierno Electrónico",
    "vi": "Khung chuẩn Chính phủ điện tử",
    "ar": "الإطار القياسي للحكومة الإلكترونية",
    "fr": "Cadre standard de l'administration électronique",
}
START, END = "<!-- egovframe-badge:start -->", "<!-- egovframe-badge:end -->"

BUILD_FILES = {
    "pom.xml", "build.gradle", "build.gradle.kts", "settings.gradle", "settings.gradle.kts",
    "gradle.properties", "libs.versions.toml",
}
SKIP_DIRS = {".git", ".idea", ".mvn", ".gradle", "node_modules", "target", "build", "out", "dist", "vendor"}
MAX_BYTES = 2_000_000

NUMBER = r"\d+(?:\.\d+){1,3}"  # a suffix such as -SNAPSHOT, -Final or .RELEASE is ignored
# Groups published by the eGovFrame project. The project's own groupId ("egovframework", "org.egovframe.template")
# and the msa module group ("org.egovframe.cloud") are deliberately excluded: they are not framework versions.
FRAMEWORK_GROUP = r"(?:org\.egovframe\.(?:rte|boot|web)(?:\.[\w\-]+)*|egovframework\.rte(?:\.[\w\-]+)*)"

# Maven
MAVEN_COMMENT = re.compile(r"<!--.*?-->", re.S)
MAVEN_PROPERTIES = re.compile(r"<properties>(.*?)</properties>", re.S)
MAVEN_PROPERTY = re.compile(r"<([\w.\-]+)>\s*([^<]*?)\s*</\1>")
MAVEN_BLOCK = re.compile(r"<(parent|dependency|plugin)>(.*?)</\1>", re.S)
MAVEN_GROUP = re.compile(r"<groupId>\s*([^<\s]+)\s*</groupId>")
MAVEN_VERSION = re.compile(r"<version>\s*([^<\s]+)\s*</version>")
EGOVFRAME_VERSION_PROPERTY = re.compile(r"^(?:org\.)?egovframe(?:work)?[\w.\-]*version$", re.I)
PLACEHOLDER = re.compile(r"\$\{([^}]+)\}")

# Gradle, gradle.properties and version catalogs
GRADLE_BLOCK_COMMENT = re.compile(r"/\*.*?\*/", re.S)
GRADLE_LINE_COMMENT = re.compile(r"(?m)(?<![:\w\"'])//.*$")
GRADLE_VARIABLE = re.compile(
    r"(?i)\b(?:egovframe|egovframework)[\w.\-]*version\b['\"]?\s*[,=:(]\s*['\"]?(" + NUMBER + ")"
)
GRADLE_COORDINATE = re.compile(r"['\"]" + FRAMEWORK_GROUP + r":[\w.\-]+:(" + NUMBER + r")[^'\"]*['\"]")
GRADLE_MAP_NOTATION = re.compile(
    r"group\s*[:=]\s*['\"]" + FRAMEWORK_GROUP + r"['\"][^)\n]*?version\s*[:=]\s*['\"](" + NUMBER + ")"
)
CATALOG_ENTRY = re.compile(r"(?mi)^\s*(?:egovframe|egovframework)[\w\-]*\s*=\s*\"(" + NUMBER + ")\"")


class ConfigError(Exception):
    pass


def number(value):
    match = re.match(NUMBER, value or "")
    return match.group(0) if match else None


def version_key(version):
    return tuple(int(part) for part in version.split("."))


def resolve(value, properties, depth=0):
    """Resolve ${placeholders} through the collected Maven properties."""
    match = PLACEHOLDER.fullmatch(value or "")
    if not match:
        return value
    target = properties.get(match.group(1))
    return resolve(target, properties, depth + 1) if target and depth < 5 else None


def build_files(project):
    for directory, subdirectories, names in os.walk(project):
        subdirectories[:] = sorted(d for d in subdirectories if d not in SKIP_DIRS)
        for name in sorted(names):
            path = Path(directory) / name
            if name in BUILD_FILES and path.stat().st_size <= MAX_BYTES:
                yield path


def maven_candidates(text, properties):
    for name, value in properties.items():
        if EGOVFRAME_VERSION_PROPERTY.match(name) and number(value):
            yield number(value), f"property <{name}>"
    for kind, block in MAVEN_BLOCK.findall(text):
        group, version = MAVEN_GROUP.search(block), MAVEN_VERSION.search(block)
        if group and version and re.fullmatch(FRAMEWORK_GROUP, group.group(1)):
            resolved = number(resolve(version.group(1), properties))
            if resolved:
                yield resolved, f"<{kind}> {group.group(1)}"


def gradle_candidates(name, text):
    for pattern, rule in ((GRADLE_VARIABLE, "version variable"), (GRADLE_COORDINATE, "dependency coordinate"),
                          (GRADLE_MAP_NOTATION, "dependency map")):
        for match in pattern.finditer(text):
            yield match.group(1), rule
    if name == "libs.versions.toml":
        for match in CATALOG_ENTRY.finditer(text):
            yield match.group(1), "version catalog"


def detect(project):
    """Return every eGovFrame version declared under `project`, one dict per declaration."""
    project = Path(project)
    files = [(path, path.read_text(encoding="utf-8", errors="replace")) for path in build_files(project)]
    maven = {path: MAVEN_COMMENT.sub("", text) for path, text in files if path.name == "pom.xml"}
    properties = {}
    for text in maven.values():
        for block in MAVEN_PROPERTIES.findall(text):
            properties.update({name: value for name, value in MAVEN_PROPERTY.findall(block)})

    found = []
    for path, text in files:
        relative = path.relative_to(project).as_posix()
        if path in maven:
            pairs = maven_candidates(maven[path], properties)
        else:
            stripped = GRADLE_LINE_COMMENT.sub("", GRADLE_BLOCK_COMMENT.sub("", text))
            pairs = gradle_candidates(path.name, stripped)
        for version, rule in pairs:
            entry = {"version": number(version), "source": relative, "rule": rule}
            if entry not in found:
                found.append(entry)
    return found


def select(candidates):
    """The highest declared version wins when a multi-module project declares several."""
    return max(candidates, key=lambda c: version_key(c["version"])) if candidates else None


def badge_version(version, supported):
    """(version for the badge URL or None, warning). Unpublished versions fall back to the name-only badge."""
    if version is None:
        return None, None
    if version in supported:
        return version, None
    return None, (
        f"eGovFrame {version} has no published badge, so the name-only badge is used. "
        "Add the version to versions.json and regenerate the badges to get a version badge."
    )


def badge_markdown(version, language, style, base_url):
    suffix = "" if language == "en" else f"-{language}"
    label = LABELS[language] + (f" {version}" if version else "")
    return f"[![{label}]({base_url}/{version or UNVERSIONED}/{style}{suffix}.svg)]({PORTAL})"


def update_readme(text, markdown):
    block = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not block.search(text):
        raise ConfigError(f"README has no badge markers; add the two lines {START} and {END} where the badge belongs")
    return block.sub(lambda _: f"{START}\n{markdown}\n{END}", text, count=1)


def load_supported(path):
    try:
        versions = json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ConfigError(f"versions file not found: {path} (pass --versions)") from None
    return set(versions)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--project", type=Path, default=Path("."), help="project directory to scan (default: .)")
    parser.add_argument("--readme", type=Path, help="README whose badge block is rewritten")
    parser.add_argument("--language", choices=sorted(LABELS), default="en")
    parser.add_argument("--style", choices=STYLES, default="flat")
    parser.add_argument("--versions", type=Path, default=ROOT / "versions.json", help="supported badge versions")
    parser.add_argument("--base-url", default=RAW_BASE, help="where the badges are served from")
    parser.add_argument("--write", action="store_true", help="write the README when the badge changed")
    parser.add_argument("--check", action="store_true", help="exit 1 when the README badge is outdated")
    parser.add_argument("--github-output", type=Path, nargs="?", const=os.environ.get("GITHUB_OUTPUT"),
                        default=None, help="append results for GitHub Actions (default file: $GITHUB_OUTPUT)")
    args = parser.parse_args(argv)

    try:
        supported = load_supported(args.versions)
        candidates = detect(args.project)
        selected = select(candidates)
        version, warning = badge_version(selected["version"] if selected else None, supported)
        result = {
            "found": selected is not None,
            "version": selected["version"] if selected else None,
            "badge_version": version,
            "source": selected["source"] if selected else None,
            "candidates": candidates,
            "warning": warning,
        }
        changed = False
        if args.readme:
            markdown = badge_markdown(version, args.language, args.style, args.base_url.rstrip("/"))
            current = args.readme.read_text(encoding="utf-8")
            updated = update_readme(current, markdown)
            changed = updated != current
            if changed and args.write:
                args.readme.write_text(updated, encoding="utf-8")
            result["badge"] = markdown
            result["readme"] = {"path": args.readme.as_posix(), "changed": changed, "written": changed and args.write}
    except (ConfigError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2

    print(json.dumps(result, ensure_ascii=False, indent=2))
    if warning:
        print(f"Warning: {warning}", file=sys.stderr)
    if args.github_output:
        with open(args.github_output, "a", encoding="utf-8") as output:
            for key, value in (("found", str(result["found"]).lower()), ("version", result["version"] or ""),
                               ("badge_version", version or ""), ("source", result["source"] or ""),
                               ("changed", str(changed and args.write).lower())):
                output.write(f"{key}={value}\n")
    return 1 if (args.check and changed) else 0


if __name__ == "__main__":
    sys.exit(main())
