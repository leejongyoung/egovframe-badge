"""Regression tests for the localized documentation and its generated entrypoints."""

import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


sr = load("sync_readme")
dv = load("detect_version")
generate = load("generate")

LANGS = ("en", "ko", "es", "vi", "ar", "fr")
SOURCES = {
    "languages": "docs/README.{lang}.md",
    "contributing": "docs/contributing/CONTRIBUTING.{lang}.md",
    "security": "docs/security/SECURITY.{lang}.md",
}
FENCE = re.compile(r"^\s*(```|~~~)")
CODE_SPAN = re.compile(r"`[^`\n]*`")
DESTINATION = re.compile(r"\]\(\s*<?([^\s)<>]+)")
BUTTON = re.compile(
    r"\[!\[[^\]]*\]\((?!https?:)[^)\s]*badges/lang/(\w+)/(flat|outline)\.svg\)\]\(([^)]+)\)"
)
BADGE_BLOCK = re.compile(r"<!-- latest-badge:start -->\n(.*?)\n<!-- latest-badge:end -->", re.S)


def local_targets(text):
    """Yield repository-local link and image destinations outside code."""
    in_fence = False
    for line in text.split("\n"):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for target in DESTINATION.findall(CODE_SPAN.sub("", line)):
            if target.startswith(("#", "//")) or re.match(r"[A-Za-z][A-Za-z0-9+.-]*:", target):
                continue
            yield target


def prose(text):
    """Text outside code fences and inline code, where the framework name is written for readers."""
    lines, in_fence = [], False
    for line in text.split("\n"):
        if FENCE.match(line):
            in_fence = not in_fence
        elif not in_fence:
            lines.append(CODE_SPAN.sub("", line))
    return "\n".join(lines)


def source_files():
    return [ROOT / pattern.format(lang=lang) for pattern in SOURCES.values() for lang in LANGS]


class RebaseTests(unittest.TestCase):
    def test_assets_one_level_up_become_root_relative(self):
        self.assertEqual(sr.rebase_target("../badges/5.0.1/flat.svg", "docs"), "badges/5.0.1/flat.svg")
        self.assertEqual(sr.rebase_target("../LICENSE", "docs"), "LICENSE")
        self.assertEqual(sr.rebase_target("README.en.md", "docs"), "docs/README.en.md")

    def test_github_directory_entrypoints_use_repository_root_paths(self):
        self.assertEqual(
            sr.rebase_target("SECURITY.ko.md", "docs/security", "/"), "/docs/security/SECURITY.ko.md"
        )
        self.assertEqual(sr.rebase_target("../../LICENSE", "docs/security", "/"), "/LICENSE")


class DocumentationTests(unittest.TestCase):
    def test_every_family_has_every_language_source(self):
        config = sr.load_config(ROOT)
        for group, pattern in SOURCES.items():
            for lang in LANGS:
                with self.subTest(group=group, lang=lang):
                    self.assertEqual(config[group][lang], pattern.format(lang=lang))
                    self.assertTrue((ROOT / config[group][lang]).is_file())

    def test_generated_entrypoints_are_current(self):
        config = sr.load_config(ROOT)
        for group, entry in sr.ENTRIES.items():
            with self.subTest(entry=entry):
                self.assertEqual(
                    (ROOT / entry).read_text(encoding="utf-8"), sr.render_entry(ROOT, config, group)
                )

    def test_local_links_and_images_resolve(self):
        for path in source_files() + [ROOT / entry for entry in sr.ENTRIES.values()]:
            for target in local_targets(path.read_text(encoding="utf-8")):
                clean = target.split("#")[0].split("?")[0]
                resolved = ROOT / clean.lstrip("/") if clean.startswith("/") else path.parent / clean
                with self.subTest(file=path.relative_to(ROOT).as_posix(), target=target):
                    self.assertTrue(resolved.exists())

    def test_language_buttons_switch_within_the_same_document_family(self):
        for pattern in SOURCES.values():
            for lang in LANGS:
                path = ROOT / pattern.format(lang=lang)
                head = path.read_text(encoding="utf-8").split("\n## ", 1)[0]
                # Repository-relative images only: they render on any branch or fork.
                buttons = BUTTON.findall(head)
                with self.subTest(file=path.relative_to(ROOT).as_posix()):
                    # The page's own language comes first so the order stays sensible
                    # no matter which language is the default.
                    expected = [lang] + [other for other in LANGS if other != lang]
                    self.assertEqual([code for code, _, _ in buttons], expected)
                    self.assertEqual(
                        [target for _, _, target in buttons],
                        [Path(pattern.format(lang=other)).name for other in expected],
                    )
                    self.assertEqual(
                        [code for code, style, _ in buttons if style == "flat"], [lang]
                    )

    def test_readme_header_has_the_name_only_badge_ci_and_license(self):
        # This repository declares no eGovFrame version, so its header shows the name-only badge.
        for lang in LANGS:
            path = ROOT / f"docs/README.{lang}.md"
            block = BADGE_BLOCK.search(path.read_text(encoding="utf-8")).group(1)
            with self.subTest(file=path.name):
                name_badge, ci, generation, license_badge = block.split("\n")
                suffix = "" if lang == "en" else f"-{lang}"
                label = generate.VERSION_LABELS[lang][0]
                self.assertEqual(
                    name_badge,
                    f"[![{label}](../badges/{generate.UNVERSIONED}/flat{suffix}.svg)](https://www.egovframe.go.kr/)",
                )
                for badge in (ci, generation):
                    workflow = re.search(r"/workflows/([\w.-]+)/badge\.svg", badge).group(1)
                    self.assertTrue((ROOT / ".github/workflows" / workflow).is_file(), workflow)
                self.assertEqual(
                    license_badge,
                    "[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](../LICENSE)",
                )
        self.assertTrue((ROOT / "LICENSE").read_text(encoding="utf-8").startswith("MIT License"))

    def test_framework_name_is_localized_and_korean_name_stays_in_korean_documents(self):
        for path in source_files():
            lang = path.name.split(".")[-2]
            text = path.read_text(encoding="utf-8")
            with self.subTest(file=path.relative_to(ROOT).as_posix()):
                # "eGovFramework" is the GitHub organization, not the framework name.
                self.assertEqual("eGovFrame" in prose(text).replace("eGovFramework", ""), lang == "en")
                self.assertEqual("전자정부표준프레임워크" in text, lang == "ko")

    def test_style_table_shows_one_language_button_matching_the_document_language(self):
        for lang in LANGS:
            lines = (ROOT / f"docs/README.{lang}.md").read_text(encoding="utf-8").split("\n")
            rows = [line for line in lines if line.startswith("| ") and "badges/5.0.1/" in line]
            with self.subTest(lang=lang):
                self.assertEqual([row.split("|")[1].strip() for row in rows], list(generate.STYLES))
                for row in rows:
                    style = row.split("|")[1].strip()
                    buttons = re.findall(r"!\[([^\]]*)\]\(\.\./badges/lang/(\w+)/([\w-]+)\.svg\)", row)
                    self.assertEqual(buttons, [(generate.LANGUAGE_BUTTONS[lang][1], lang, style)], style)

    def test_every_language_documents_version_detection_with_the_same_structure(self):
        shapes = {}
        for lang in LANGS:
            text = (ROOT / f"docs/README.{lang}.md").read_text(encoding="utf-8")
            headings = [line[:3] for line in text.split("\n") if line.startswith(("## ", "### "))]
            with self.subTest(lang=lang):
                self.assertEqual(text.count(dv.START), 1, "exactly one example badge marker pair")
                self.assertEqual(text.count(dv.ENV_START), 1, "exactly one example environment marker pair")
                self.assertEqual(sum(h == "## " for h in headings), 7, "one detection section, no duplicates")
            shapes[lang] = headings
        self.assertEqual(len({tuple(shape) for shape in shapes.values()}), 1, "every language has the same headings")

    def test_detection_table_source_column_is_identifiers_only_so_no_language_leaks(self):
        for lang in LANGS:
            text = (ROOT / f"docs/README.{lang}.md").read_text(encoding="utf-8")
            rows = [line for line in text.split("\n") if line.startswith("| ") and ("<br>" in line or "distributionUrl" in line)]
            with self.subTest(lang=lang):
                self.assertEqual(len(rows), 4)  # runtime, Java, Spring Boot, Gradle
                for row in rows:
                    source_column = row.split("|")[3]
                    leftovers = re.findall(r"[A-Za-z]{2,}", CODE_SPAN.sub("", source_column.replace("<br>", " ")))
                    self.assertEqual(leftovers, [], "prose in a column that is shared by every language")

    def test_documentation_names_every_file_and_key_the_detector_reads(self):
        needed = {name.removesuffix(".kts") for name in dv.BUILD_FILES}
        needed |= set(dv.MAVEN_JAVA_PROPERTIES) | {dv.SPRING_BOOT_PARENT[1], "org.springframework.boot", "sourceCompatibility",
                                                  "JavaLanguageVersion.of", "distributionUrl", ".github/workflows/example-egovframe-badge.yml",
                                                  "--check", "--write", "--github-output", "PROJECT_DIRS"}
        needed |= {marker for pair in ((dv.START, dv.END), (dv.ENV_START, dv.ENV_END)) for marker in pair}
        for lang in LANGS:
            text = (ROOT / f"docs/README.{lang}.md").read_text(encoding="utf-8")
            with self.subTest(lang=lang):
                self.assertEqual({item for item in needed if item not in text}, set())

    def test_documented_environment_table_is_what_the_detector_produces(self):
        project = ROOT / "examples" / "sample-gradle-project"
        run = subprocess.run([sys.executable, str(ROOT / "scripts/detect_version.py"), "--project", str(project)],
                             capture_output=True, text=True, check=True)
        rows = json.loads(run.stdout)["environment"]
        for lang in LANGS:
            text = (ROOT / f"docs/README.{lang}.md").read_text(encoding="utf-8")
            with self.subTest(lang=lang):
                self.assertIn(dv.environment_markdown(rows, lang), text)

    def test_no_english_leftovers_or_stale_counts_in_translations(self):
        total = len(generate.load_versions())
        for lang in LANGS:
            text = (ROOT / f"docs/README.{lang}.md").read_text(encoding="utf-8")
            with self.subTest(lang=lang):
                if lang != "en":
                    self.assertNotIn("versions total", text)
                self.assertIn(str(total), text)
                self.assertNotIn(f"{total - 1} ", text.replace("5.0.1", ""))
                self.assertIn("`5.0.7`", next(line for line in text.split("\n") if "**5.x**" in line))

    def test_default_language_selects_every_entrypoint(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / "docs", root / "docs")
            config = root / "docs/config.yml"
            config.write_text(
                config.read_text(encoding="utf-8").replace("default_language: en", "default_language: ko"),
                encoding="utf-8",
            )
            self.assertEqual(sorted(sr.sync(root)), sorted(sr.ENTRIES.values()))
            self.assertEqual(sr.sync(root), [])
            readme = (root / "README.md").read_text(encoding="utf-8")
            self.assertTrue(readme.startswith("# 전자정부표준프레임워크 배지"))
            self.assertIn("![flat](badges/5.0.1/flat.svg)", readme)
            self.assertIn("](docs/README.en.md)", readme)
            self.assertIn(f"](badges/{generate.UNVERSIONED}/flat-ko.svg)", readme)
            policy = (root / ".github/SECURITY.md").read_text(encoding="utf-8")
            self.assertTrue(policy.startswith("# 보안 정책"))
            self.assertIn("](/docs/security/SECURITY.en.md)", policy)


if __name__ == "__main__":
    unittest.main()
