"""Tests for scripts/detect_version.py. Fixtures are excerpts of real eGovFramework project files."""

import contextlib
import importlib.util
import io
import json
import re
import tempfile
import unittest
import xml.etree.ElementTree as ET
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
        self.assertEqual(lines, {"found": "true", "version": "5.0.1", "badge_version": "5.0.1", "source": "pom.xml",
                                 "java": "", "spring_boot": "", "gradle": "", "changed": "true"})


# Excerpts of real files: egovframe-template-simple-backend (main, 4.0.x) and egovframe-msa-edu (main).
MAVEN_JAVA_17 = "<project><properties><java.version>17</java.version></properties>" + BOOT_PARENT.split("<version>1.0.0</version>")[1].replace("</project>", "") + "</project>"
MAVEN_SPRING_BOOT_PARENT = """<project><parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.4.5</version>
</parent></project>"""
MSA_BUILD_GRADLE = """plugins {
    id 'org.springframework.boot' version '3.5.6'
}
sourceCompatibility = '17'
targetCompatibility = '17'
ext {
    set('egovframeBootParentVersion', '5.0.0')
}"""
MSA_TOOLCHAIN = "java { toolchain { languageVersion = JavaLanguageVersion.of(17) } }"
GRADLE_WRAPPER_PROPERTIES = """distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\\://services.gradle.org/distributions/gradle-8.5-bin.zip
"""


def development(files):
    with make_project(files) as directory:
        return {component: sorted({c["version"] for c in found}) for component, found in dv.detect_development(directory).items()}


class DevelopmentEnvironmentTests(unittest.TestCase):
    def test_declarations_found_in_real_projects(self):
        cases = {
            "maven java.version": ({"pom.xml": MAVEN_JAVA_17}, {"Java": ["17"], "Spring Boot": [], "Gradle": []}),
            "maven spring boot parent": ({"pom.xml": MAVEN_SPRING_BOOT_PARENT}, {"Java": [], "Spring Boot": ["2.4.5"], "Gradle": []}),
            "gradle plugin and source compatibility": ({"build.gradle": MSA_BUILD_GRADLE}, {"Java": ["17"], "Spring Boot": ["3.5.6"], "Gradle": []}),
            "gradle java toolchain": ({"build.gradle": MSA_TOOLCHAIN}, {"Java": ["17"], "Spring Boot": [], "Gradle": []}),
            "gradle wrapper": ({"gradle/wrapper/gradle-wrapper.properties": GRADLE_WRAPPER_PROPERTIES}, {"Java": [], "Spring Boot": [], "Gradle": ["8.5"]}),
            "kotlin plugin syntax": ({"build.gradle.kts": 'plugins { id("org.springframework.boot") version "3.2.0" }'}, {"Java": [], "Spring Boot": ["3.2.0"], "Gradle": []}),
            "legacy java 1.8 and enum notation": ({"pom.xml": "<project><properties><maven.compiler.source>1.8</maven.compiler.source></properties></project>",
                                                   "build.gradle": "sourceCompatibility = JavaVersion.VERSION_1_8"}, {"Java": ["1.8"], "Spring Boot": [], "Gradle": []}),
        }
        for name, (files, expected) in cases.items():
            with self.subTest(name):
                self.assertEqual(development(files), expected)

    def test_only_what_the_project_declares_itself_is_reported(self):
        # eGovFrame 4.x/5.x parents bring Spring Boot and Java with them; the build file does not state them.
        self.assertEqual(development({"pom.xml": BOOT_PARENT}), {"Java": [], "Spring Boot": [], "Gradle": []})
        self.assertEqual(development({"pom.xml": PROPERTY_4X}), {"Java": [], "Spring Boot": [], "Gradle": []})

    def test_commented_out_and_unrelated_declarations_are_ignored(self):
        files = {"build.gradle": "// sourceCompatibility = '8'\n/* id 'org.springframework.boot' version '1.5.0' */\nsourceCompatibility = '17'\n",
                 "pom.xml": "<project><properties><!-- <java.version>8</java.version> --></properties></project>"}
        self.assertEqual(development(files), {"Java": ["17"], "Spring Boot": [], "Gradle": []})

    def test_the_highest_version_is_chosen_and_legacy_numbers_compare_as_their_minor_part(self):
        rows = dv.environment_rows(None, {"Java": [{"version": "1.8", "source": "a"}, {"version": "11", "source": "b"}, {"version": "9", "source": "c"}],
                                          "Spring Boot": [], "Gradle": []})
        self.assertEqual([(r["component"], r["version"], r["source"]) for r in rows], [("Java", "11", "b")])
        rows = dv.environment_rows(None, {"Java": [{"version": "1.8", "source": "a"}, {"version": "7", "source": "b"}], "Spring Boot": [], "Gradle": []})
        self.assertEqual(rows[0]["version"], "1.8")


ENVIRONMENT_README = """# Project

<!-- egovframe-badge:start -->
old badge
<!-- egovframe-badge:end -->

<!-- egovframe-environment:start -->
old table
<!-- egovframe-environment:end -->
"""


class EnvironmentTableTests(unittest.TestCase):
    def sync(self, files, language="en", readme=ENVIRONMENT_README, *flags):
        with make_project({**files, "README.md": readme}) as directory:
            target = Path(directory) / "README.md"
            status, out, _ = run("--project", directory, "--readme", target, "--language", language, "--write", *flags)
            return status, json.loads(out), target.read_text(encoding="utf-8")

    def test_table_lists_runtime_then_development_with_the_declaring_file(self):
        files = {"build.gradle": MSA_BUILD_GRADLE, "gradle/wrapper/gradle-wrapper.properties": GRADLE_WRAPPER_PROPERTIES}
        status, result, text = self.sync(files)
        self.assertEqual(status, 0)
        self.assertIn(
            "<!-- egovframe-environment:start -->\n"
            "| Category | Component | Version | Source |\n| --- | --- | --- | --- |\n"
            "| Runtime environment | eGovFrame | 5.0.0 | `build.gradle` |\n"
            "| Development environment | Java | 17 | `build.gradle` |\n"
            "| Development environment | Spring Boot | 3.5.6 | `build.gradle` |\n"
            "| Development environment | Gradle | 8.5 | `gradle/wrapper/gradle-wrapper.properties` |\n"
            "<!-- egovframe-environment:end -->", text)
        self.assertEqual(result["readme"]["blocks"], [dv.START, dv.ENV_START])
        self.assertIn("/5.0.0/flat.svg", text)

    def test_rows_without_a_declaration_are_left_out_and_a_project_with_none_says_so(self):
        _, _, text = self.sync({"pom.xml": BOOT_PARENT})
        self.assertIn("| Runtime environment | eGovFrame | 5.0.1 | `pom.xml` |", text)
        self.assertNotIn("Development environment", text)
        _, result, text = self.sync({"package.json": "{}"})
        self.assertEqual(result["environment"], [])
        self.assertIn("<!-- egovframe-environment:start -->\nNo build file declares a eGovFrame version.\n<!-- egovframe-environment:end -->", text)

    def test_table_is_localized_and_the_korean_name_appears_only_in_korean(self):
        for language in dv.LABELS:
            _, _, text = self.sync({"build.gradle": MSA_BUILD_GRADLE}, language)
            table = text.split(dv.ENV_START)[1].split(dv.ENV_END)[0]
            with self.subTest(language):
                self.assertIn(dv.TABLE_TEXT[language]["runtime"], table)
                self.assertIn(dv.TABLE_TEXT[language]["development"], table)
                self.assertIn(f"| {dv.LABELS[language]} | 5.0.0 |", table)
                self.assertEqual("전자정부표준프레임워크" in table, language == "ko")
                self.assertEqual("eGovFrame" in table, language == "en")

    def test_every_language_has_every_table_word(self):
        for language, text in dv.TABLE_TEXT.items():
            self.assertEqual(set(text), set(dv.TABLE_TEXT["en"]), language)
            self.assertIn("{name}", text["none"])

    def test_either_marker_pair_alone_is_enough_and_untouched_blocks_stay(self):
        only_table = "# P\n\n<!-- egovframe-environment:start -->\nx\n<!-- egovframe-environment:end -->\nkeep\n"
        _, result, text = self.sync({"pom.xml": BOOT_PARENT}, readme=only_table)
        self.assertEqual(result["readme"]["blocks"], [dv.ENV_START])
        self.assertTrue(text.startswith("# P\n") and text.endswith("-->\nkeep\n"))
        only_badge = "# P\n\n<!-- egovframe-badge:start -->\nx\n<!-- egovframe-badge:end -->\n"
        _, result, text = self.sync({"pom.xml": BOOT_PARENT}, readme=only_badge)
        self.assertEqual(result["readme"]["blocks"], [dv.START])
        self.assertNotIn("Runtime environment", text)

    def test_second_run_changes_nothing(self):
        with make_project({"pom.xml": BOOT_PARENT, "README.md": ENVIRONMENT_README}) as directory:
            args = ("--project", directory, "--readme", Path(directory) / "README.md", "--write")
            self.assertTrue(json.loads(run(*args)[1])["readme"]["changed"])
            self.assertFalse(json.loads(run(*args)[1])["readme"]["changed"])


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

    def test_example_projects_are_valid_and_their_readmes_match_the_detection(self):
        expected = {
            "sample-project": ("5.0.2", ["Java"]),
            "sample-gradle-project": ("5.0.0", ["Java", "Spring Boot", "Gradle"]),
            "sample-project-unversioned": (None, ["Java", "Spring Boot"]),
        }
        for name, (version, development_components) in expected.items():
            project = ROOT / "examples" / name
            with self.subTest(project=name):
                if (project / "pom.xml").exists():
                    ET.parse(project / "pom.xml")  # real Maven rejects malformed XML; the regex scanner would not
                status, out, _ = run("--project", project, "--readme", project / "README.md", "--check")
                result = json.loads(out)
                self.assertEqual(result["version"], version)
                self.assertEqual([r["component"] for r in result["environment"] if r["category"] == "development"], development_components)
                self.assertEqual((status, result["readme"]["changed"]), (0, False), "README is stale")
                self.assertEqual(result["readme"]["blocks"], [dv.START, dv.ENV_START])

    def test_example_workflow_commits_the_rewritten_readmes_for_every_example(self):
        workflow = (ROOT / ".github/workflows/example-egovframe-badge.yml").read_text(encoding="utf-8")
        self.assertNotIn("github.output", workflow)  # not a GitHub Actions context
        self.assertIn("--write", workflow)
        self.assertRegex(workflow, r"git commit")
        self.assertRegex(workflow, r'git push origin "HEAD:\$\{GITHUB_REF_NAME\}"')
        for sample in ("sample-project", "sample-gradle-project", "sample-project-unversioned"):
            self.assertIn(f"examples/{sample}", workflow)
            self.assertTrue((ROOT / "examples" / sample / "README.md").is_file(), sample)
    def test_no_scratch_files_are_committed(self):
        tracked = {path.name for path in ROOT.iterdir() if path.is_file()}
        self.assertEqual({name for name in tracked if name.startswith(("fix_", "tmp"))}, set())


if __name__ == "__main__":
    unittest.main()
