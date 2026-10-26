#!/usr/bin/env python3
"""Detect the eGovFrame runtime and development environment versions a project declares and keep its README in sync.

The project's build files (Maven pom.xml, Gradle build scripts, gradle.properties, version catalogs and the Gradle
wrapper) are scanned for:

  * runtime environment     the eGovFrame version (RTE, Boot parent, Web parent, Gradle boot parent variable, ...)
  * development environment Java, Spring Boot and Gradle versions, when the project declares them itself

Two README blocks are rewritten, each only when its marker pair exists:

    <!-- egovframe-badge:start -->        <!-- egovframe-badge:end -->          badge of the eGovFrame version
    <!-- egovframe-environment:start -->  <!-- egovframe-environment:end -->    table of the detected versions

A project that declares an eGovFrame version gets the version badge; a project that declares none gets the
name-only badge (no version area). The table lists only what was found, with the file that declares it.

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
RAW_BASE = "https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges"
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
ENV_START, ENV_END = "<!-- egovframe-environment:start -->", "<!-- egovframe-environment:end -->"

# Table wording per language. The runtime row is named with LABELS[language].
TABLE_TEXT = {
    "en": {"category": "Category", "component": "Component", "version": "Version", "source": "Source",
           "runtime": "Runtime environment", "development": "Development environment",
           "none": "No build file declares a {name} version."},
    "ko": {"category": "구분", "component": "구성 요소", "version": "버전", "source": "출처",
           "runtime": "실행환경", "development": "개발환경",
           "none": "빌드 파일에 선언된 {name} 버전이 없습니다."},
    "es": {"category": "Categoría", "component": "Componente", "version": "Versión", "source": "Fuente",
           "runtime": "Entorno de ejecución", "development": "Entorno de desarrollo",
           "none": "Ningún archivo de construcción declara una versión de {name}."},
    "vi": {"category": "Phân loại", "component": "Thành phần", "version": "Phiên bản", "source": "Nguồn",
           "runtime": "Môi trường thực thi", "development": "Môi trường phát triển",
           "none": "Không có tệp xây dựng nào khai báo phiên bản {name}."},
    "ar": {"category": "الفئة", "component": "المكوّن", "version": "الإصدار", "source": "المصدر",
           "runtime": "بيئة التشغيل", "development": "بيئة التطوير",
           "none": "لا يوجد ملف بناء يعلن عن إصدار {name}."},
    "fr": {"category": "Catégorie", "component": "Composant", "version": "Version", "source": "Source",
           "runtime": "Environnement d'exécution", "development": "Environnement de développement",
           "none": "Aucun fichier de build ne déclare de version de {name}."},
}

BUILD_FILES = {
    "pom.xml", "build.gradle", "build.gradle.kts", "settings.gradle", "settings.gradle.kts",
    "gradle.properties", "libs.versions.toml", "gradle-wrapper.properties",
}
SKIP_DIRS = {".git", ".idea", ".mvn", ".gradle", "node_modules", "target", "build", "out", "dist", "vendor"}
MAX_BYTES = 2_000_000

NUMBER = r"\d+(?:\.\d+){1,3}"  # a suffix such as -SNAPSHOT, -Final or .RELEASE is ignored
JAVA_NUMBER = r"\d+(?:[._]\d+)?"  # 17, 1.8, 1_8 (JavaVersion.VERSION_1_8)
# Groups published by the eGovFrame project. The project's own groupId ("egovframework", "org.egovframe.template")
# and the msa module group ("org.egovframe.cloud") are deliberately excluded: they are not framework versions.
FRAMEWORK_GROUP = r"(?:org\.egovframe\.(?:rte|boot|web)(?:\.[\w\-]+)*|egovframework\.rte(?:\.[\w\-]+)*)"

# Maven
MAVEN_COMMENT = re.compile(r"<!--.*?-->", re.S)
MAVEN_PROPERTIES = re.compile(r"<properties>(.*?)</properties>", re.S)
MAVEN_PROPERTY = re.compile(r"<([\w.\-]+)>\s*([^<]*?)\s*</\1>")
MAVEN_BLOCK = re.compile(r"<(parent|dependency|plugin)>(.*?)</\1>", re.S)
MAVEN_GROUP = re.compile(r"<groupId>\s*([^<\s]+)\s*</groupId>")
MAVEN_ARTIFACT = re.compile(r"<artifactId>\s*([^<\s]+)\s*</artifactId>")
MAVEN_VERSION = re.compile(r"<version>\s*([^<\s]+)\s*</version>")
EGOVFRAME_VERSION_PROPERTY = re.compile(r"^(?:org\.)?egovframe(?:work)?[\w.\-]*version$", re.I)
MAVEN_JAVA_PROPERTIES = ("maven.compiler.release", "maven.compiler.source", "maven.compiler.target", "java.version")
SPRING_BOOT_PARENT = ("org.springframework.boot", "spring-boot-starter-parent")
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
GRADLE_JAVA_COMPATIBILITY = re.compile(
    r"\b(?:sourceCompatibility|targetCompatibility)\s*=\s*['\"]?(?:JavaVersion\.VERSION_)?(" + JAVA_NUMBER + r")['\"]?"
)
GRADLE_JAVA_TOOLCHAIN = re.compile(r"JavaLanguageVersion\.of\(\s*(\d+)\s*\)")
GRADLE_SPRING_BOOT_PLUGIN = re.compile(
    r"""id\s*\(?\s*['"]org\.springframework\.boot['"]\s*\)?\s+version\s+['"](""" + NUMBER + ")"
)
GRADLE_WRAPPER = re.compile(r"gradle-(\d+(?:\.\d+){1,2})-(?:bin|all)\.zip")

DEVELOPMENT_COMPONENTS = ("Java", "Spring Boot", "Gradle")


class ConfigError(Exception):
    pass


def number(value):
    match = re.match(NUMBER, value or "")
    return match.group(0) if match else None


def version_key(version):
    return tuple(int(part) for part in version.split("."))


def java_number(value):
    match = re.fullmatch(JAVA_NUMBER, value or "")
    return match.group(0).replace("_", ".") if match else None


def java_key(version):
    """1.8 is Java 8, so legacy 1.x numbers compare by their minor part."""
    parts = version.split(".")
    return (int(parts[1]),) if parts[0] == "1" and len(parts) > 1 else tuple(int(part) for part in parts)


def resolve(value, properties, depth=0):
    """Resolve ${placeholders} through properties declared in the same Maven file."""
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


def read_project(project):
    """Read build files once, retaining comment-free Maven text and properties per file."""
    files = [(path, path.read_text(encoding="utf-8", errors="replace")) for path in build_files(Path(project))]
    maven = {path: MAVEN_COMMENT.sub("", text) for path, text in files if path.name == "pom.xml"}
    properties = {}
    for path, text in maven.items():
        local = {}
        for block in MAVEN_PROPERTIES.findall(text):
            local.update({name: value for name, value in MAVEN_PROPERTY.findall(block)})
        properties[path] = local
    return files, maven, properties


def strip_gradle_comments(text):
    return GRADLE_LINE_COMMENT.sub("", GRADLE_BLOCK_COMMENT.sub("", text))


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


def development_candidates(project, files, maven, properties):
    """{component: [declaration, ...]} for Java, Spring Boot and Gradle, as each file declares them."""
    found = {component: [] for component in DEVELOPMENT_COMPONENTS}

    def add(component, version, source, rule):
        entry = {"version": version, "source": source, "rule": rule}
        if version and entry not in found[component]:
            found[component].append(entry)

    for path, text in files:
        relative = path.relative_to(project).as_posix()
        if path in maven:
            body = maven[path]
            local = properties[path]
            for name in MAVEN_JAVA_PROPERTIES:
                if name in local:
                    add("Java", java_number(resolve(local[name], local)), relative, f"property <{name}>")
            for kind, block in MAVEN_BLOCK.findall(body):
                group, artifact, version = MAVEN_GROUP.search(block), MAVEN_ARTIFACT.search(block), MAVEN_VERSION.search(block)
                if kind == "parent" and group and artifact and version and (group.group(1), artifact.group(1)) == SPRING_BOOT_PARENT:
                    add("Spring Boot", number(resolve(version.group(1), local)), relative, "<parent> spring-boot-starter-parent")
        elif path.name == "gradle-wrapper.properties":
            for line in text.splitlines():
                match = None if line.lstrip().startswith("#") else GRADLE_WRAPPER.search(line)
                if match:
                    add("Gradle", match.group(1), relative, "gradle wrapper")
        elif path.suffix in (".gradle", ".kts"):
            stripped = strip_gradle_comments(text)
            for match in GRADLE_JAVA_COMPATIBILITY.finditer(stripped):
                add("Java", java_number(match.group(1)), relative, "sourceCompatibility")
            for match in GRADLE_JAVA_TOOLCHAIN.finditer(stripped):
                add("Java", match.group(1), relative, "java toolchain")
            for match in GRADLE_SPRING_BOOT_PLUGIN.finditer(stripped):
                add("Spring Boot", match.group(1), relative, "spring boot plugin")
    return found


def detect(project):
    """Return every eGovFrame version declared under `project`, one dict per declaration."""
    project = Path(project)
    files, maven, properties = read_project(project)
    found = []
    for path, text in files:
        relative = path.relative_to(project).as_posix()
        if path in maven:
            pairs = maven_candidates(maven[path], properties[path])
        else:
            pairs = gradle_candidates(path.name, strip_gradle_comments(text))
        for version, rule in pairs:
            entry = {"version": number(version), "source": relative, "rule": rule}
            if entry not in found:
                found.append(entry)
    return found


def detect_development(project):
    """Return {component: [declaration, ...]} for the development environment under `project`."""
    project = Path(project)
    files, maven, properties = read_project(project)
    return development_candidates(project, files, maven, properties)


def select(candidates, key=None):
    """The highest declared version wins when a multi-module project declares several."""
    key = key or (lambda candidate: version_key(candidate["version"]))
    return max(candidates, key=key) if candidates else None


def environment_rows(runtime_selected, development):
    """Rows for the README table: the runtime environment first, then Java, Spring Boot and Gradle when found."""
    rows = []
    if runtime_selected:
        rows.append({"category": "runtime", "component": "eGovFrame", **{k: runtime_selected[k] for k in ("version", "source")}})
    for component in DEVELOPMENT_COMPONENTS:
        key = (lambda c: java_key(c["version"])) if component == "Java" else None
        chosen = select(development.get(component, []), key)
        if chosen:
            rows.append({"category": "development", "component": component,
                         "version": chosen["version"], "source": chosen["source"]})
    return rows


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


def environment_markdown(rows, language):
    text = TABLE_TEXT[language]
    if not rows:
        return text["none"].format(name=LABELS[language])
    lines = [f"| {text['category']} | {text['component']} | {text['version']} | {text['source']} |",
             "| --- | --- | --- | --- |"]
    for row in rows:
        component = LABELS[language] if row["component"] == "eGovFrame" else row["component"]
        lines.append(f"| {text[row['category']]} | {component} | {row['version']} | `{row['source']}` |")
    return "\n".join(lines)


def update_readme(text, blocks):
    """Rewrite each block whose marker pair is in the README. `blocks` maps (start, end) to its Markdown."""
    present = []
    for (start, end), markdown in blocks.items():
        pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
        if pattern.search(text):
            present.append(start)
            text = pattern.sub(lambda _: f"{start}\n{markdown}\n{end}", text, count=1)
    if not present:
        raise ConfigError(
            f"README has no markers; add the lines {START} and {END} for the badge, "
            f"and/or {ENV_START} and {ENV_END} for the environment table"
        )
    return text, present


def load_supported(path):
    try:
        versions = json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ConfigError(f"versions file not found: {path} (pass --versions)") from None
    return set(versions)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--project", type=Path, default=Path("."), help="project directory to scan (default: .)")
    parser.add_argument("--readme", type=Path, help="README whose badge and environment blocks are rewritten")
    parser.add_argument("--language", choices=sorted(LABELS), default="en")
    parser.add_argument("--style", choices=STYLES, default="flat")
    parser.add_argument("--versions", type=Path, default=ROOT / "versions.json", help="supported badge versions")
    parser.add_argument("--base-url", default=RAW_BASE, help="where the badges are served from")
    parser.add_argument("--write", action="store_true", help="write the README when a block changed")
    parser.add_argument("--check", action="store_true", help="exit 1 when the README is outdated")
    parser.add_argument("--github-output", type=Path, nargs="?", const=os.environ.get("GITHUB_OUTPUT"),
                        default=None, help="append results for GitHub Actions (default file: $GITHUB_OUTPUT)")
    args = parser.parse_args(argv)

    try:
        supported = load_supported(args.versions)
        files, maven, properties = read_project(args.project)
        project = Path(args.project)
        candidates = []
        for path, text in files:
            relative = path.relative_to(project).as_posix()
            pairs = (maven_candidates(maven[path], properties[path]) if path in maven
                     else gradle_candidates(path.name, strip_gradle_comments(text)))
            for found_version, rule in pairs:
                entry = {"version": number(found_version), "source": relative, "rule": rule}
                if entry not in candidates:
                    candidates.append(entry)
        selected = select(candidates)
        development = development_candidates(project, files, maven, properties)
        rows = environment_rows(selected, development)
        version, warning = badge_version(selected["version"] if selected else None, supported)
        result = {
            "found": selected is not None,
            "version": selected["version"] if selected else None,
            "badge_version": version,
            "source": selected["source"] if selected else None,
            "candidates": candidates,
            "environment": rows,
            "warning": warning,
        }
        changed = False
        if args.readme:
            badge = badge_markdown(version, args.language, args.style, args.base_url.rstrip("/"))
            current = args.readme.read_text(encoding="utf-8")
            updated, blocks = update_readme(current, {
                (START, END): badge,
                (ENV_START, ENV_END): environment_markdown(rows, args.language),
            })
            changed = updated != current
            if changed and args.write:
                args.readme.write_text(updated, encoding="utf-8")
            result["badge"] = badge
            result["readme"] = {"path": args.readme.as_posix(), "changed": changed,
                                "written": changed and args.write, "blocks": blocks}
    except (ConfigError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2

    print(json.dumps(result, ensure_ascii=False, indent=2))
    if warning:
        print(f"Warning: {warning}", file=sys.stderr)
    if args.github_output:
        by_component = {row["component"]: row["version"] for row in rows}
        with open(args.github_output, "a", encoding="utf-8") as output:
            for key, value in (("found", str(result["found"]).lower()), ("version", result["version"] or ""),
                               ("badge_version", version or ""), ("source", result["source"] or ""),
                               ("java", by_component.get("Java", "")),
                               ("spring_boot", by_component.get("Spring Boot", "")),
                               ("gradle", by_component.get("Gradle", "")),
                               ("changed", str(changed and args.write).lower())):
                output.write(f"{key}={value}\n")
    return 1 if (args.check and changed) else 0


if __name__ == "__main__":
    sys.exit(main())
