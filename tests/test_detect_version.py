"""Tests for scripts/detect_version.py. Fixtures are excerpts of real eGovFramework project files."""

import contextlib
import importlib.util
import io
import json
import re
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


dv = load("detect_version")
generate = load("generate")

BOOT_PARENT = """<project><groupId>egovframework</groupId><artifactId>egovframe-boot-simple-backend</artifactId>
<version>1.0.0</version>
<parent>
    <groupId>org.egovframe.boot</groupId>
    <artifactId>egovframe-boot-starter-parent</artifactId>
    <version>5.0.1</version>
</parent></project>"""
WEB_PARENT = """<project><parent>
    <groupId>org.egovframe.web</groupId>
    <artifactId>egovframe-web-config-parent</artifactId>
    <version>5.0.2</version>
</parent></project>"""
PROPERTY_4X = """<project><properties>
    <spring.maven.artifact.version>5.3.37</spring.maven.artifact.version>
    <org.egovframe.rte.version>4.3.0</org.egovframe.rte.version>
</properties></project>"""
PROPERTY_3X = """<project><properties><egovframework.rte.version>3.10.0</egovframework.rte.version></properties></project>"""
GRADLE_SET = """ext {
    set('egovframeBootParentVersion', '5.0.0')
    set('springCloudVersion', '2025.0.0')
}"""
GRADLE_ASSIGN = """ext {
    egovframeBootParentVersion = '5.0.0'
}"""
GRADLE_KTS = 'val egovframeVersion = "5.0.0"\n'
GRADLE_PROPERTIES = "springBootVersion=3.2.0\negovframeVersion=4.2.1\n"
GRADLE_COORDINATE = 'dependencies { implementation("org.egovframe.rte:org.egovframe.rte.ptl.mvc:4.3.0") }'
GRADLE_MAP = "dependencies { implementation group: 'org.egovframe.rte', name: 'egovframe-rte-ptl-mvc', version: '5.0.0' }"
CATALOG = '[versions]\negovframe = "5.0.0"\nspring = "6.1.0"\n'
MAVEN_LITERAL = """<project><dependencies><dependency>
    <groupId>org.egovframe.rte</groupId><artifactId>egovframe-rte-ptl-mvc</artifactId><version>4.1.0</version>
</dependency></dependencies></project>"""
MAVEN_INDIRECT = """<project><properties><rte.release>4.2.0</rte.release></properties>
<dependencies><dependency><groupId>egovframework.rte</groupId><artifactId>x</artifactId><version>${rte.release}</version></dependency></dependencies></project>"""

README = "# Project\n\n<!-- egovframe-badge:start -->\nold\n<!-- egovframe-badge:end -->\n\nText.\n"


def make_project(files):
    directory = tempfile.TemporaryDirectory()
    for name, content in files.items():
        path = Path(directory.name) / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return directory


def run(*args):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        status = dv.main([str(arg) for arg in args])
    return status, out.getvalue(), err.getvalue()


def detected(files):
    with make_project(files) as directory:
        return dv.detect(directory)


class DetectionTests(unittest.TestCase):
    def test_every_real_world_declaration_style_is_found(self):
        cases = {
            "boot 5.0 parent": ({"pom.xml": BOOT_PARENT}, "5.0.1"),
            "web 5.0 parent": ({"pom.xml": WEB_PARENT}, "5.0.2"),
            "maven 4.x property": ({"pom.xml": PROPERTY_4X}, "4.3.0"),
            "maven 3.x property": ({"pom.xml": PROPERTY_3X}, "3.10.0"),
            "maven literal dependency": ({"pom.xml": MAVEN_LITERAL}, "4.1.0"),
            "maven placeholder through another property": ({"pom.xml": MAVEN_INDIRECT}, "4.2.0"),
            "gradle set()": ({"build.gradle": GRADLE_SET}, "5.0.0"),
            "gradle assignment": ({"build.gradle": GRADLE_ASSIGN}, "5.0.0"),
            "gradle kotlin": ({"build.gradle.kts": GRADLE_KTS}, "5.0.0"),
            "gradle.properties": ({"gradle.properties": GRADLE_PROPERTIES}, "4.2.1"),
            "gradle coordinate": ({"build.gradle.kts": GRADLE_COORDINATE}, "4.3.0"),
            "gradle map notation": ({"build.gradle": GRADLE_MAP}, "5.0.0"),
            "version catalog": ({"gradle/libs.versions.toml": CATALOG}, "5.0.0"),
        }
        for name, (files, expected) in cases.items():
            with self.subTest(name):
                self.assertEqual({c["version"] for c in detected(files)}, {expected})

    def test_projects_without_an_egovframe_version_declare_nothing(self):
        cases = {
            "javascript project": {"package.json": '{"name": "egovframe-template-simple-react", "version": "0.0.0"}'},
            "own groupId and spring parent only": {"pom.xml": """<project><groupId>egovframework</groupId>
                <artifactId>demo</artifactId><version>5.0.0</version>
                <parent><groupId>org.springframework.boot</groupId><artifactId>spring-boot-starter-parent</artifactId>
                <version>3.2.0</version></parent></project>"""},
            "template and cloud groups are not framework versions": {"pom.xml": """<project><dependencies>
                <dependency><groupId>org.egovframe.cloud</groupId><artifactId>m</artifactId><version>5.0.0</version></dependency>
                <dependency><groupId>org.egovframe.template</groupId><artifactId>t</artifactId><version>5.0.0</version></dependency>
                </dependencies></project>"""},
            "unrelated version variables": {"build.gradle": "ext { set('springCloudVersion', '2025.0.0') }"},
        }
        for name, files in cases.items():
            with self.subTest(name):
                self.assertEqual(detected(files), [])

    def test_comments_and_build_output_are_ignored(self):
        files = {
            "pom.xml": "<project><properties><!-- <org.egovframe.rte.version>3.9.0</org.egovframe.rte.version> -->"
                       "<org.egovframe.rte.version>4.3.0</org.egovframe.rte.version></properties></project>",
            "build.gradle": "// egovframeVersion = '3.9.0'\n/* egovframeBootParentVersion = '3.5.0' */\n"
                            "repositories { maven { url 'https://maven.egovframe.go.kr/maven/' } }\n"
                            "ext { egovframeVersion = '4.3.0' }\n",
            "node_modules/dep/pom.xml": PROPERTY_3X,
            "target/pom.xml": PROPERTY_3X,
            "build/build.gradle": GRADLE_SET,
        }
        self.assertEqual({c["version"] for c in detected(files)}, {"4.3.0"})

    def test_version_suffixes_are_ignored(self):
        for text, expected in (("5.0.0-SNAPSHOT", "5.0.0"), ("4.3.0.RELEASE", "4.3.0"), ("5.0.2-Final", "5.0.2")):
            with self.subTest(text):
                files = {"pom.xml": f"<project><properties><org.egovframe.rte.version>{text}</org.egovframe.rte.version></properties></project>"}
                self.assertEqual([c["version"] for c in detected(files)], [expected])

    def test_highest_declared_version_wins_in_multi_module_projects(self):
        files = {"a/pom.xml": PROPERTY_4X, "b/pom.xml": BOOT_PARENT, "c/build.gradle": GRADLE_SET}
        with make_project(files) as directory:
            status, out, _ = run("--project", directory)
        result = json.loads(out)
        self.assertEqual((status, result["version"], result["source"]), (0, "5.0.1", "b/pom.xml"))
        self.assertEqual({c["version"] for c in result["candidates"]}, {"4.3.0", "5.0.1", "5.0.0"})


class ReadmeTests(unittest.TestCase):
    def sync(self, files, *flags, language="en", readme=README):
        with make_project({**files, "README.md": readme}) as directory:
            target = Path(directory) / "README.md"
            status, out, err = run("--project", directory, "--readme", target, "--language", language, *flags)
            return status, json.loads(out) if out else None, err, target.read_text(encoding="utf-8")

    def test_declared_version_gets_the_localized_version_badge(self):
        expected = {
            "en": "[![eGovFrame 5.0.1](" + dv.RAW_BASE + "/5.0.1/flat.svg)](https://www.egovframe.go.kr/)",
            "ko": "[![전자정부표준프레임워크 5.0.1](" + dv.RAW_BASE + "/5.0.1/flat-ko.svg)](https://www.egovframe.go.kr/)",
            "ar": "[![الإطار القياسي للحكومة الإلكترونية 5.0.1](" + dv.RAW_BASE + "/5.0.1/flat-ar.svg)](https://www.egovframe.go.kr/)",
        }
        for language, badge in expected.items():
            with self.subTest(language):
                status, result, _, text = self.sync({"pom.xml": BOOT_PARENT}, "--write", language=language)
                self.assertEqual((status, result["badge"]), (0, badge))
                self.assertIn(f"<!-- egovframe-badge:start -->\n{badge}\n<!-- egovframe-badge:end -->", text)
                self.assertTrue(text.startswith("# Project") and text.endswith("Text.\n"))

    def test_project_without_a_version_gets_the_name_only_badge(self):
        status, result, _, text = self.sync({"package.json": "{}"}, "--write", "--style", "outline", language="ko")
        self.assertEqual(status, 0)
        self.assertFalse(result["found"])
        self.assertIn("[![전자정부표준프레임워크](" + dv.RAW_BASE + "/unversioned/outline-ko.svg)]", text)
        self.assertNotRegex(result["badge"], r"\d+\.\d+")

    def test_unpublished_version_falls_back_to_the_name_only_badge_with_a_warning(self):
        files = {"pom.xml": PROPERTY_4X.replace("4.3.0", "9.9.9")}
        status, result, err, text = self.sync(files, "--write")
        self.assertEqual((status, result["version"], result["badge_version"]), (0, "9.9.9", None))
        self.assertIn("/unversioned/flat.svg", text)
        self.assertIn("9.9.9", err)

    def test_write_is_required_to_change_the_readme_and_a_second_run_changes_nothing(self):
        files = {"pom.xml": BOOT_PARENT}
        _, result, _, text = self.sync(files)
        self.assertEqual((result["readme"]["changed"], result["readme"]["written"], text), (True, False, README))
        with make_project({**files, "README.md": README}) as directory:
            target = Path(directory) / "README.md"
            args = ("--project", directory, "--readme", target)
            self.assertEqual(json.loads(run(*args, "--write")[1])["readme"]["written"], True)
            second = json.loads(run(*args, "--write")[1])
            self.assertEqual((second["readme"]["changed"], second["readme"]["written"]), (False, False))

    def test_check_fails_only_while_the_readme_is_outdated(self):
        with make_project({"pom.xml": BOOT_PARENT, "README.md": README}) as directory:
            target = Path(directory) / "README.md"
            args = ("--project", directory, "--readme", target)
            self.assertEqual(run(*args, "--check")[0], 1)
            self.assertEqual(run(*args, "--write")[0], 0)
            self.assertEqual(run(*args, "--check")[0], 0)

    def test_readme_without_markers_is_a_configuration_error(self):
        status, result, err, text = self.sync({"pom.xml": BOOT_PARENT}, "--write", readme="# No markers\n")
        self.assertEqual((status, result, text), (2, None, "# No markers\n"))
        self.assertIn("egovframe-badge:start", err)

    def test_github_output_reports_the_detection_for_later_steps(self):
        with make_project({"pom.xml": BOOT_PARENT, "README.md": README}) as directory:
            output = Path(directory) / "github-output"
            run("--project", directory, "--readme", Path(directory) / "README.md", "--write", "--github-output", output)
            lines = dict(line.split("=", 1) for line in output.read_text(encoding="utf-8").splitlines())
        self.assertEqual(lines, {"found": "true", "version": "5.0.1", "badge_version": "5.0.1", "source": "pom.xml", "changed": "true"})


class ContractWithGeneratorTests(unittest.TestCase):
    def test_labels_match_the_generator(self):
        self.assertEqual(dv.LABELS, {lang: generate.VERSION_LABELS[lang][0] for lang in generate.LANGUAGES})
        self.assertEqual(dv.STYLES, generate.STYLES)
        self.assertEqual(dv.UNVERSIONED, generate.UNVERSIONED)

    def test_every_badge_url_points_at_a_published_file(self):
        published = generate.load_versions()
        for version in (published[0], published[-1], None):
            for language in generate.LANGUAGES:
                for style in generate.STYLES:
                    markdown = dv.badge_markdown(version, language, style, dv.RAW_BASE)
                    path = re.search(re.escape(dv.RAW_BASE) + r"/([^)]+)\)", markdown).group(1)
                    with self.subTest(version=version, language=language, style=style):
                        self.assertTrue((ROOT / "badges" / path).is_file(), path)

    def test_the_example_project_declares_a_published_version(self):
        status, out, _ = run("--project", ROOT / "examples" / "sample-project")
        self.assertEqual(status, 0)
        self.assertTrue(json.loads(out)["badge_version"])


if __name__ == "__main__":
    unittest.main()
