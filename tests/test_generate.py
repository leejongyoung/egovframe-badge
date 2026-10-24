import importlib.util
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("generate", ROOT / "scripts" / "generate.py")
generate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generate)


class BadgeGenerationTests(unittest.TestCase):
    def test_all_published_badges_are_complete_accessible_svg(self):
        paths = generate.logo_paths()
        for version in generate.load_versions():
            for style in generate.STYLES:
                for lang in generate.LANGUAGES:
                    with self.subTest(version=version, style=style, lang=lang):
                        svg = generate.render(version, style, paths, lang=lang)
                        root = ET.fromstring(svg)
                        self.assertEqual(root.attrib["role"], "img")
                        self.assertEqual(
                            root.attrib["aria-label"], f"{generate.VERSION_LABELS[lang][0]} {version}"
                        )
                        # Scope to the icon group specifically (it's the only <g> with a
                        # transform attribute) - the badge background shape also contains
                        # a <path> inside its own <g>, which a bare ".//g/path" would also
                        # match and inflate the count to 4.
                        icon_paths = root.findall(
                            ".//{http://www.w3.org/2000/svg}g[@transform]/{http://www.w3.org/2000/svg}path"
                        )
                        self.assertEqual(len(icon_paths), 3)
                        self.assertNotIn("http://", svg.replace('xmlns="http://www.w3.org/2000/svg"', ""))
                        self.assertNotIn("<script", svg)

        for lang, (code_label, native_name, *_rest) in generate.LANGUAGE_BUTTONS.items():
            for style in generate.STYLES:
                with self.subTest(lang_button=lang, style=style):
                    svg = generate.render_language_button(lang, style)
                    root = ET.fromstring(svg)
                    self.assertEqual(root.attrib["role"], "img")
                    self.assertIn(native_name, root.attrib["aria-label"])
                    self.assertIn(code_label, root.attrib["aria-label"])
                    self.assertNotIn("<script", svg)

    def test_framework_name_is_localized_and_korean_name_stays_in_korean(self):
        paths = generate.logo_paths()
        for lang in generate.LANGUAGES:
            for style in generate.STYLES:
                svg = generate.render("5.0.6", style, paths, lang=lang)
                with self.subTest(lang=lang, style=style):
                    self.assertEqual("egovframe" in svg.lower(), lang == "en")
                    self.assertEqual("전자정부표준프레임워크" in svg, lang == "ko")

    def test_unversioned_badges_show_only_the_name_without_a_version_area(self):
        paths = generate.logo_paths()
        for lang in generate.LANGUAGES:
            label, prominent_label, label_width, prominent_width, _font = generate.VERSION_LABELS[lang]
            for style in generate.STYLES:
                svg = generate.render(None, style, paths, lang=lang)
                root = ET.fromstring(svg)
                prominent = style == "for-the-badge"
                with self.subTest(lang=lang, style=style):
                    self.assertEqual(root.attrib["aria-label"], label)
                    self.assertEqual(int(root.attrib["width"]), prominent_width if prominent else label_width)
                    self.assertEqual(len(root.findall(".//{http://www.w3.org/2000/svg}text")), 1)
                    self.assertEqual(len(root.findall(".//{http://www.w3.org/2000/svg}g[@clip-path]/{http://www.w3.org/2000/svg}path")), 0)
                    self.assertNotRegex(root.attrib["aria-label"], r"\d")
                    self.assertEqual(root.find("{http://www.w3.org/2000/svg}title").text, f"{label} ({style})")

    def test_fitted_languages_pin_label_text_to_the_label_area_so_no_font_can_overflow(self):
        paths = generate.logo_paths()
        for lang in generate.LANGUAGES:
            _label, _prominent_label, normal_width, prominent_width, _font = generate.VERSION_LABELS[lang]
            for style in generate.STYLES:
                for version in ("5.0.7", None):
                    svg = generate.render(version, style, paths, lang=lang)
                    prominent = style == "for-the-badge"
                    expected = (prominent_width - 33 - 14) if prominent else (normal_width - 29 - 12)
                    with self.subTest(lang=lang, style=style, version=version):
                        if lang in generate.FITTED_LANGUAGES:
                            self.assertIn(f'textLength="{expected}" lengthAdjust="spacingAndGlyphs"', svg)
                        else:
                            self.assertNotIn("textLength", svg)

    def test_rejects_invalid_paths_and_styles(self):
        for version in ("../5.0", "5/0", "<script>"):
            with self.assertRaises(ValueError):
                generate.render(version, "flat", "")
        with self.assertRaises(ValueError):
            generate.render("5.0.1", "unknown", "")
        with self.assertRaises(ValueError):
            generate.render("5.0.1", "flat", "", lang="invalid")
        with self.assertRaises(ValueError):
            generate.render_language_button("invalid", "flat")
        with self.assertRaises(ValueError):
            generate.render_language_button("en", "unknown")

    def test_supports_runtime_versions_from_1_to_5(self):
        versions = set(generate.load_versions())
        expected_milestones = (
            "1.0", "1.0.0",
            "2.0", "2.0.0", "2.5", "2.6", "2.7",
            "3.0", "3.0.0", "3.1", "3.5", "3.5.1", "3.6", "3.7", "3.8", "3.9", "3.10",
            "4.0", "4.0.0", "4.1", "4.2", "4.3",
            "5.0", "5.0.0", "5.0.1", "5.0.7",
        )
        for v in expected_milestones:
            with self.subTest(version=v):
                self.assertIn(v, versions)


if __name__ == "__main__":
    unittest.main()
