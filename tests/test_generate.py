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
                        self.assertIn(version, root.attrib["aria-label"])
                        if lang == "ko":
                            self.assertIn("전자정부표준프레임워크", root.attrib["aria-label"])
                        else:
                            self.assertIn("eGovFrame", root.attrib["aria-label"])
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

    def test_rejects_invalid_paths_and_styles(self):
        for version in ("../5.0", "5/0", "<script>"):
            with self.assertRaises(ValueError):
                generate.render(version, "flat", "")
        with self.assertRaises(ValueError):
            generate.render("5.0.1", "unknown", "")
        with self.assertRaises(ValueError):
            generate.render("5.0.1", "flat", "", lang="invalid")

    def test_supports_runtime_versions_from_1_to_5(self):
        versions = set(generate.load_versions())
        expected_milestones = (
            "1.0", "1.0.0",
            "2.0", "2.0.0", "2.5", "2.6", "2.7",
            "3.0", "3.0.0", "3.1", "3.5", "3.5.1", "3.6", "3.7", "3.8", "3.9", "3.10",
            "4.0", "4.0.0", "4.1", "4.2", "4.3",
            "5.0", "5.0.0", "5.0.1",
        )
        for v in expected_milestones:
            with self.subTest(version=v):
                self.assertIn(v, versions)


if __name__ == "__main__":
    unittest.main()
