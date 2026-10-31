# 전자정부표준프레임워크 배지

<!-- latest-badge:start -->
[![전자정부표준프레임워크](../badges/unversioned/flat-ko.svg)](https://www.egovframe.go.kr/)
[![CI](https://github.com/leejongyoung/egovframe-badge/actions/workflows/verify.yml/badge.svg)](https://github.com/leejongyoung/egovframe-badge/actions/workflows/verify.yml)
[![Generate badges](https://github.com/leejongyoung/egovframe-badge/actions/workflows/generate-badges.yml/badge.svg)](https://github.com/leejongyoung/egovframe-badge/actions/workflows/generate-badges.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](../LICENSE)
<!-- latest-badge:end -->

[![English](../badges/lang/en/outline.svg)](README.en.md)
[![한국어](../badges/lang/ko/flat.svg)](README.ko.md)
[![Español](../badges/lang/es/outline.svg)](README.es.md)
[![Tiếng Việt](../badges/lang/vi/outline.svg)](README.vi.md)
[![العربية](../badges/lang/ar/outline.svg)](README.ar.md)
[![Français](../badges/lang/fr/outline.svg)](README.fr.md)

전자정부표준프레임워크를 사용하는 **모든 프로젝트**가 README에 가져다 쓸 수 있는 SVG 배지입니다. 저장소마다 로고를 각자 하드코딩하는 대신, 한 곳에서 관리하는 배지를 raw URL 한 줄로 참조합니다. 정적 SVG라서 JavaScript, 별도 배포 서버, 긴 Base64 URL이 필요하지 않습니다.

## 한 줄로 사용

버전과 스타일, 언어(`en`, `ko`, `es`, `vi`, `ar`, `fr`)를 URL 경로에서 선택합니다. 아래 예시는 공식 포털로 연결됩니다.

**영문**
```md
[![eGovFrame 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat.svg)](https://www.egovframe.go.kr)
```

**한국어**
```md
[![전자정부표준프레임워크 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-ko.svg)](https://www.egovframe.go.kr)
```

**다국어 버전 배지 (`es` 스페인어 · `vi` 베트남어 · `ar` 아랍어 · `fr` 프랑스어)**
```md
[![Marco Estándar de Gobierno Electrónico 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-es.svg)](https://www.egovframe.go.kr)
[![Khung chuẩn Chính phủ điện tử 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-vi.svg)](https://www.egovframe.go.kr)
[![الإطار القياسي للحكومة الإلكترونية 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-ar.svg)](https://www.egovframe.go.kr)
[![Cadre standard de l'administration électronique 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-fr.svg)](https://www.egovframe.go.kr)
```
*(모든 다국어 배지는 `badges/5.0.2/flat-<lang>.svg` 및 `badges/5.0.2/<lang>/flat.svg` 경로를 모두 지원합니다.)*

## 자동 버전 감지

README에 프로젝트 빌드 파일이 선언한 버전을 보여 줄 수 있습니다. `scripts/detect_version.py`가 버전을 찾아 표식이 있는 README 블록을 다시 쓰고, 워크플로가 푸시할 때마다 이를 실행할 수 있습니다.

### 버전을 찾는 위치

| 환경 | 구성 요소 | 선언 위치 |
| --- | --- | --- |
| 실행환경 | 전자정부표준프레임워크 | `pom.xml`: `org.egovframe.rte.version`, `egovframework.rte.version`, `<parent>` · `<dependency>`: `org.egovframe.boot`, `org.egovframe.web`, `org.egovframe.rte`<br>`build.gradle(.kts)`: `egovframeBootParentVersion`, `org.egovframe.*:artifact:version`<br>`settings.gradle(.kts)`, `gradle.properties`, `libs.versions.toml` |
| 개발환경 | Java | `pom.xml`: `java.version`, `maven.compiler.release`, `maven.compiler.source`, `maven.compiler.target`<br>`build.gradle(.kts)`: `sourceCompatibility`, `JavaLanguageVersion.of(17)` |
| 개발환경 | Spring Boot | `pom.xml`: `<parent>` `spring-boot-starter-parent`<br>`build.gradle(.kts)`: `id 'org.springframework.boot' version '3.5.6'` |
| 개발환경 | Gradle | `gradle/wrapper/gradle-wrapper.properties`: `distributionUrl` (`gradle-8.5-bin.zip`) |

- 여러 모듈이 선언하면 가장 높은 버전을 씁니다.
- Maven 속성과 `${...}` 참조는 이를 선언한 `pom.xml` 안에서만 해석하며 모듈 사이에 합치지 않습니다. 해결되지 않은 부모·외부 속성은 추측하지 않습니다.
- 주석은 무시하고, 빌드 산출물·의존성 폴더(`target`, `build`, `node_modules` 등)는 건너뜁니다.
- 프로젝트가 직접 선언한 값만 표시합니다. 4.x/5.x 부모는 자체 Spring Boot와 Java를 가져오므로, 빌드 파일에 적혀 있지 않으면 표에 나오지 않습니다.
- 버전을 선언하지 않은 프로젝트는 이름만 있는 배지를, 선언했지만 배지가 없는 버전(`versions.json`에 없음)은 경고와 함께 이름만 있는 배지를 씁니다.

### README 표식

내용이 들어갈 자리에 표식을 둡니다. 두 블록 모두 선택 사항이지만 최소 하나는 있어야 합니다. 첫 번째는 배지(버전을 선언했으면 버전 배지, 선언하지 않았으면 이름만 있는 배지)가 되고, 두 번째는 감지한 버전과 이를 선언한 파일을 담은 표가 됩니다.

```md
<!-- egovframe-badge:start -->
[![전자정부표준프레임워크](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/unversioned/flat-ko.svg)](https://www.egovframe.go.kr/)
<!-- egovframe-badge:end -->

<!-- egovframe-environment:start -->
<!-- egovframe-environment:end -->
```

`examples/sample-gradle-project`의 결과:

| 구분 | 구성 요소 | 버전 | 출처 |
| --- | --- | --- | --- |
| 실행환경 | 전자정부표준프레임워크 | 5.0.0 | `build.gradle` |
| 개발환경 | Java | 17 | `build.gradle` |
| 개발환경 | Spring Boot | 3.5.6 | `build.gradle` |
| 개발환경 | Gradle | 8.5 | `gradle/wrapper/gradle-wrapper.properties` |

### 실행

로컬에서 실행합니다(파일을 쓰지 않고 실패만 시키려면 `--check`를 추가하세요. 검증만 하는 CI에 적합합니다):

```bash
python3 scripts/detect_version.py --project . --readme README.md --language ko --style flat --write
```

### CI에서 실행

[`.github/workflows/example-egovframe-badge.yml`](../.github/workflows/example-egovframe-badge.yml)은 동작하는 예시입니다. 프로젝트를 건드리는 푸시마다 스크립트를 실행하고 다시 쓴 README를 브랜치에 커밋합니다. `examples/sample-project`(Maven), `examples/sample-gradle-project`(Gradle: Java, Spring Boot, Gradle), `examples/sample-project-unversioned`(선언 없음)에서 실행됩니다. `scripts/detect_version.py`, 루트의 `versions.json`, 워크플로를 자신의 저장소의 같은 경로에 복사하세요. 버전 선언이 없는 프로젝트도 `versions.json`이 저장소 루트에 필요하며, 다른 위치에 두면 `--versions path/to/versions.json`을 전달하세요. `PROJECT_DIRS`를 `.`로 바꾸고 README에 표식을 추가하세요. 직접 단계를 만들 때는 `--github-output`이 `version`, `badge_version`, `source`, `java`, `spring_boot`, `gradle`, `changed`를 `$GITHUB_OUTPUT`에 기록합니다.

## 다국어 문서 전환 배지 버튼 (`badges/lang/`)

다국어 `README` 상단에서 언어를 선택·전환할 때 공통으로 쓸 수 있는 독립 배지 버튼입니다 (`en`, `ko`, `es`, `vi`, `ar`, `fr`, `mn`, `bg`, `ne`). 현재 보고 있는 언어는 `flat.svg`, 다른 언어는 `outline.svg`(또는 전체 `flat.svg`)로 조합할 수 있습니다.

```md
[![English](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/en/flat.svg)](README.md)
[![한국어](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ko/outline.svg)](README.ko.md)
[![Español](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/es/outline.svg)](docs/README.es.md)
[![Tiếng Việt](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/vi/outline.svg)](docs/README.vi.md)
[![العربية](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ar/outline.svg)](docs/README.ar.md)
[![Français](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/fr/outline.svg)](docs/README.fr.md)
```

전자정부표준프레임워크 [실행환경 가이드](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:실행환경가이드)에 등재된 1.0부터 5.x까지의 모든 주요 실행환경 버전(`1.0`, `2.0`, `2.5`, `2.6`, `2.7`, `3.0`, `3.1`, `3.5`, `3.6`, `3.7`, `3.8`, `3.9`, `3.10`, `4.0`, `4.1`, `4.2`, `4.3`, `5.0`) 및 세부 릴리스 패치 버전을 제공합니다. 영문(`eGovFrame`)과 국문(`전자정부표준프레임워크`) 각각 아래 5가지 스타일을 선택할 수 있습니다 — [shields.io](https://shields.io)의 대표 스타일(`flat`, `flat-square`, `plastic`, `for-the-badge`)을 그대로 지원하고, 자체 `outline` 스타일을 더했습니다. (shields.io의 `social` 스타일은 마우스 호버 효과에 기대는 구조라 정적 `<img>` 임베드에서는 의미가 없어 제외했습니다.)

| 스타일 | 예시(영문) | 예시(한국어) | 언어 버튼 |
| --- | --- | --- | --- |
| flat | ![flat](../badges/5.0.1/flat.svg) | ![flat (한국어)](../badges/5.0.1/flat-ko.svg) | ![한국어](../badges/lang/ko/flat.svg) |
| flat-square | ![flat-square](../badges/5.0.1/flat-square.svg) | ![flat-square (한국어)](../badges/5.0.1/flat-square-ko.svg) | ![한국어](../badges/lang/ko/flat-square.svg) |
| plastic | ![plastic](../badges/5.0.1/plastic.svg) | ![plastic (한국어)](../badges/5.0.1/plastic-ko.svg) | ![한국어](../badges/lang/ko/plastic.svg) |
| for-the-badge | ![for-the-badge](../badges/5.0.1/for-the-badge.svg) | ![for-the-badge (한국어)](../badges/5.0.1/for-the-badge-ko.svg) | ![한국어](../badges/lang/ko/for-the-badge.svg) |
| outline | ![outline](../badges/5.0.1/outline.svg) | ![outline (한국어)](../badges/5.0.1/outline-ko.svg) | ![한국어](../badges/lang/ko/outline.svg) |

## 지원 버전

전자정부표준프레임워크 [실행환경 가이드](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:실행환경가이드)에 등재된 1.0부터 5.x까지 총 55개 버전(주요 실행환경 및 패치 릴리스)을 지원합니다.

- **5.x**: `5.0`, `5.0.0`, `5.0.1`, `5.0.2`, `5.0.3`, `5.0.4`, `5.0.5`, `5.0.6`, `5.0.7`
- **4.x**: `4.3`, `4.3.0`, `4.3.1`, `4.3.2`, `4.2`, `4.2.0`, `4.2.1`, `4.2.2`, `4.2.4`, `4.1`, `4.1.0`, `4.1.1`, `4.1.2`, `4.1.3`, `4.0`, `4.0.0`, `4.0.1`
- **3.x**: `3.10`, `3.10.0`, `3.10.1`, `3.10.2`, `3.9`, `3.9.0`, `3.8`, `3.8.0`, `3.7`, `3.7.0`, `3.6`, `3.6.0`, `3.5`, `3.5.0`, `3.5.1`, `3.1`, `3.1.0`, `3.0`, `3.0.0`
- **2.x**: `2.7`, `2.7.0`, `2.6`, `2.6.0`, `2.5`, `2.5.0`, `2.0`, `2.0.0`
- **1.x**: `1.0`, `1.0.0`

## 버전 추가 및 배지 생성

새 버전이 필요하면 `versions.json`에 추가하고 생성 스크립트를 실행해 SVG를 생성하고 커밋합니다. 프로젝트 자신의 버전은 위에서 설명한 스크립트가 감지합니다.

```sh
python3 scripts/generate.py
python3 -m unittest discover -s tests -v
python3 scripts/generate.py --check
```

## 설계

- SVG는 저장소에 커밋하고 GitHub raw URL로 제공합니다. README 렌더러가 이미지로 직접 읽을 수 있으며 별도 배포 서버가 필요하지 않습니다.
- 로고 경로는 `assets/egovframe-mark.svg` 한 곳에 보관합니다. 생성된 모든 배지는 로고를 내부에 포함하므로 외부 이미지 의존성이 없습니다.
- 버전과 스타일을 파일 경로로 고정해, 기존 README 배지가 새로운 릴리스 때문에 뜻밖에 바뀌지 않도록 합니다.
- `scripts/generate.py --check`와 CI로 생성물과 원본의 일치를 검사합니다. 스타일 변경 시 모든 버전에 일관되게 적용됩니다.
- `plastic` 스타일의 광택 그라데이션은 [shields.io](https://shields.io)가 쓰는 것과 동일한 그라데이션 스톱 값을 사용합니다. `for-the-badge`는 shields.io와 동일하게 모서리를 각지게(`shape-rendering`이 아닌 `rx="0"`으로) 그립니다.

로고는 [eGovFramework 저장소](https://github.com/eGovFramework)의 기존 README 배지에 포함된 SVG를 동일하게 추출했습니다. 로고와 전자정부표준프레임워크 명칭의 권리는 해당 권리자에게 있습니다.

## 라이선스

이 저장소의 코드(생성 스크립트, 테스트, 워크플로)는 [MIT License](../LICENSE)로 배포합니다. 로고 자산(`assets/egovframe-mark.svg`) 및 그로부터 생성된 배지에 포함된 로고 이미지는 이 라이선스의 적용을 받지 않으며, 위에서 설명한 대로 원 권리자에게 귀속됩니다.