"""Regression tests for the localized documentation and its generated entrypoints."""

import importlib.util
import re
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("sync_readme", ROOT / "scripts" / "sync_readme.py")
sr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sr)

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
                buttons = BUTTON.findall(head)  # repository-relative images only: they render on any branch or fork
                with self.subTest(file=path.relative_to(ROOT).as_posix()):
                    self.assertEqual([code for code, _, _ in buttons], list(LANGS))
                    self.assertEqual(
                        [target for _, _, target in buttons],
                        [Path(pattern.format(lang=other)).name for other in LANGS],
                    )
                    self.assertEqual(
                        [code for code, style, _ in buttons if style == "flat"], [lang]
                    )

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
            self.assertTrue(readme.startswith("# eGovFrame 배지"))
            self.assertIn("![flat](badges/5.0.1/flat.svg)", readme)
            self.assertIn("](docs/README.en.md)", readme)
            policy = (root / ".github/SECURITY.md").read_text(encoding="utf-8")
            self.assertTrue(policy.startswith("# 보안 정책"))
            self.assertIn("](/docs/security/SECURITY.en.md)", policy)


if __name__ == "__main__":
    unittest.main()
