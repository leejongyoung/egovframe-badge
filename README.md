# eGovFrame badge

<!-- latest-badge:start -->
[![eGovFrame](badges/unversioned/flat.svg)](https://www.egovframe.go.kr/)
[![CI](https://github.com/leejongyoung/egovframe-badge/actions/workflows/verify.yml/badge.svg)](https://github.com/leejongyoung/egovframe-badge/actions/workflows/verify.yml)
[![Generate badges](https://github.com/leejongyoung/egovframe-badge/actions/workflows/generate-badges.yml/badge.svg)](https://github.com/leejongyoung/egovframe-badge/actions/workflows/generate-badges.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
<!-- latest-badge:end -->

[![English](badges/lang/en/flat.svg)](docs/README.en.md)
[![한국어](badges/lang/ko/outline.svg)](docs/README.ko.md)
[![Español](badges/lang/es/outline.svg)](docs/README.es.md)
[![Tiếng Việt](badges/lang/vi/outline.svg)](docs/README.vi.md)
[![العربية](badges/lang/ar/outline.svg)](docs/README.ar.md)
[![Français](badges/lang/fr/outline.svg)](docs/README.fr.md)

A **single SVG badge** for every project using the eGovFrame (electronic Government Framework). Instead of hard-coding logos in each repository, reference one centrally-maintained badge with a raw URL. Static SVG — no JavaScript, no deployment server, no long Base64 URLs.

## One-line usage

Pick the version, style, and language (`en`, `ko`, `es`, `vi`, `ar`, `fr`) from the URL path. The examples below link to the official portal.

**English (`eGovFrame`)**
```md
[![eGovFrame 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat.svg)](https://www.egovframe.go.kr)
```

**Multilingual version badges (`es` Spanish · `vi` Vietnamese · `ar` Arabic · `fr` French)**
```md
[![Marco Estándar de Gobierno Electrónico 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-es.svg)](https://www.egovframe.go.kr)
[![Khung chuẩn Chính phủ điện tử 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-vi.svg)](https://www.egovframe.go.kr)
[![الإطار القياسي للحكومة الإلكترونية 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-ar.svg)](https://www.egovframe.go.kr)
[![Cadre standard de l'administration électronique 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-fr.svg)](https://www.egovframe.go.kr)
```
*(All multilingual badges support both `badges/5.0.2/flat-<lang>.svg` and `badges/5.0.2/<lang>/flat.svg` paths.)*

## Automatic version detection

A README can show the versions its project's build files declare. `scripts/detect_version.py` finds them and rewrites the marked README blocks, and a workflow can run it on every push.

### Where the versions are found

| Environment | Component | Declared in |
| --- | --- | --- |
| Runtime environment | eGovFrame | `pom.xml`: `org.egovframe.rte.version`, `egovframework.rte.version`, `<parent>` · `<dependency>`: `org.egovframe.boot`, `org.egovframe.web`, `org.egovframe.rte`<br>`build.gradle(.kts)`: `egovframeBootParentVersion`, `org.egovframe.*:artifact:version`<br>`settings.gradle(.kts)`, `gradle.properties`, `libs.versions.toml` |
| Development environment | Java | `pom.xml`: `java.version`, `maven.compiler.release`, `maven.compiler.source`, `maven.compiler.target`<br>`build.gradle(.kts)`: `sourceCompatibility`, `JavaLanguageVersion.of(17)` |
| Development environment | Spring Boot | `pom.xml`: `<parent>` `spring-boot-starter-parent`<br>`build.gradle(.kts)`: `id 'org.springframework.boot' version '3.5.6'` |
| Development environment | Gradle | `gradle/wrapper/gradle-wrapper.properties`: `distributionUrl` (`gradle-8.5-bin.zip`) |

- The highest version wins when several modules declare one.
- Comments are ignored, and build output and dependency folders (`target`, `build`, `node_modules`, ...) are skipped.
- Only what the project declares itself is shown: eGovFrame 4.x/5.x parents bring their own Spring Boot and Java, which are not listed unless the build file states them.
- A project that declares no eGovFrame version gets the name-only badge; a declared version without a published badge (not in `versions.json`) gets the name-only badge and a warning.

### README markers

Put the markers where the content belongs. Each block is optional, but at least one is required: the first becomes the badge (the version badge, or the name-only badge when no version is declared), the second becomes a table of the detected versions with the file that declares each one.

```md
<!-- egovframe-badge:start -->
[![eGovFrame](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/unversioned/flat.svg)](https://www.egovframe.go.kr/)
<!-- egovframe-badge:end -->

<!-- egovframe-environment:start -->
<!-- egovframe-environment:end -->
```

Result for `examples/sample-gradle-project`:

| Category | Component | Version | Source |
| --- | --- | --- | --- |
| Runtime environment | eGovFrame | 5.0.0 | `build.gradle` |
| Development environment | Java | 17 | `build.gradle` |
| Development environment | Spring Boot | 3.5.6 | `build.gradle` |
| Development environment | Gradle | 8.5 | `gradle/wrapper/gradle-wrapper.properties` |

### Run it

Run it locally (add `--check` to fail instead of writing, for a CI that only verifies):

```bash
python3 scripts/detect_version.py --project . --readme README.md --language en --style flat --write
```

### Run it in CI

[`.github/workflows/example-egovframe-badge.yml`](.github/workflows/example-egovframe-badge.yml) is a working example: on every push that touches the projects it runs the script and commits the rewritten READMEs back to the branch. It runs on `examples/sample-project` (Maven), `examples/sample-gradle-project` (Gradle: Java, Spring Boot, Gradle) and `examples/sample-project-unversioned` (no declaration). Copy `scripts/detect_version.py` and the workflow into your own project, set `PROJECT_DIRS` to `.` and add the markers. For custom steps, `--github-output` writes `version`, `badge_version`, `source`, `java`, `spring_boot`, `gradle` and `changed` to `$GITHUB_OUTPUT`.

## Language selector badge buttons (`badges/lang/`)

Standalone badge buttons for multilingual `README` language switching (`en`, `ko`, `es`, `vi`, `ar`, `fr`, `mn`, `bg`, `ne`). The current language uses `flat.svg`; other languages use `outline.svg` (or all `flat.svg`).

```md
[![English](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/en/flat.svg)](README.md)
[![한국어](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ko/outline.svg)](README.ko.md)
[![Español](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/es/outline.svg)](docs/README.es.md)
[![Tiếng Việt](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/vi/outline.svg)](docs/README.vi.md)
[![العربية](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ar/outline.svg)](docs/README.ar.md)
[![Français](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/fr/outline.svg)](docs/README.fr.md)
```

All major runtime versions from the [eGovFrame Runtime Guide](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:실행환경가이드) — 1.0 through 5.x (53 versions total) — with five styles each: `flat`, `flat-square`, `plastic`, `for-the-badge`, and the custom `outline` style (shields.io `social` style excluded as it relies on hover effects).

| Style | Example | Language button |
| --- | --- | --- |
| flat | ![flat](badges/5.0.1/flat.svg) | ![English](badges/lang/en/flat.svg) |
| flat-square | ![flat-square](badges/5.0.1/flat-square.svg) | ![English](badges/lang/en/flat-square.svg) |
| plastic | ![plastic](badges/5.0.1/plastic.svg) | ![English](badges/lang/en/plastic.svg) |
| for-the-badge | ![for-the-badge](badges/5.0.1/for-the-badge.svg) | ![English](badges/lang/en/for-the-badge.svg) |
| outline | ![outline](badges/5.0.1/outline.svg) | ![English](badges/lang/en/outline.svg) |

## Supported versions

All 53 versions from the eGovFrame Runtime Guide:

- **5.x**: `5.0`, `5.0.0`, `5.0.1`, `5.0.2`, `5.0.3`, `5.0.4`, `5.0.5`, `5.0.6`, `5.0.7`
- **4.x**: `4.3`, `4.3.0`, `4.3.1`, `4.3.2`, `4.2`, `4.2.0`, `4.2.1`, `4.2.2`, `4.1`, `4.1.0`, `4.1.1`, `4.1.2`, `4.0`, `4.0.0`, `4.0.1`
- **3.x**: `3.10`, `3.10.0`, `3.10.1`, `3.10.2`, `3.9`, `3.9.0`, `3.8`, `3.8.0`, `3.7`, `3.7.0`, `3.6`, `3.6.0`, `3.5`, `3.5.0`, `3.5.1`, `3.1`, `3.1.0`, `3.0`, `3.0.0`
- **2.x**: `2.7`, `2.7.0`, `2.6`, `2.6.0`, `2.5`, `2.5.0`, `2.0`, `2.0.0`
- **1.x**: `1.0`, `1.0.0`

## Adding versions and generating badges

To add a new version, edit `versions.json` and run the generator (a project's own version is detected by the script described above):

```sh
python3 scripts/generate.py
python3 -m unittest discover -s tests -v
python3 scripts/generate.py --check
```

## Design
- SVGs are committed and served via GitHub raw URLs. README renderers load them directly; no deployment server required.
- Single logo source at `assets/egovframe-mark.svg`. All generated badges embed the logo — no external image dependencies.
- Version and style are fixed in the file path so existing README badges don't change unexpectedly when new releases arrive.
- `scripts/generate.py --check` and CI verify generated output matches source. Style changes apply consistently across all versions.
- `plastic` style uses the same gloss gradient stops as shields.io. `for-the-badge` uses sharp corners (`rx="0"`) like shields.io.

Logo extracted from the existing eGovFramework README badge. Logo and eGovFrame name rights belong to their respective owners.

## License

Code (generation script, tests, workflows) is [MIT licensed](LICENSE). Logo asset (`assets/egovframe-mark.svg`) and logos embedded in generated badges are **not** covered by this license and belong to their original owners as noted above.

