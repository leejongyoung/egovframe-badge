# eGovFrame badge

전자정부 표준프레임워크(eGovFrame)를 사용하는 **모든 프로젝트**가 README에 가져다 쓸 수 있는 SVG 배지입니다. 저장소마다 로고를 각자 하드코딩하는 대신, 한 곳에서 관리하는 배지를 raw URL 한 줄로 참조합니다. 정적 SVG라서 JavaScript, 별도 배포 서버, 긴 Base64 URL이 필요하지 않습니다.

## 한 줄로 사용

버전과 스타일, 언어(영문/한문)를 URL 경로에서 선택합니다. 아래 예시는 공식 포털로 연결됩니다.

**영문 (`eGovFrame`)**
```md
[![eGovFrame 5.0.1](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/5.0.1/flat.svg)](https://www.egovframe.go.kr)
```

**한문 (`전자정부표준프레임워크`)**
```md
[![전자정부표준프레임워크 5.0.1](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/5.0.1/flat-ko.svg)](https://www.egovframe.go.kr)
```
*(한문 배지는 `badges/5.0.1/flat-ko.svg` 및 `badges/5.0.1/ko/flat.svg` 경로를 모두 지원합니다.)*

전자정부 표준프레임워크 [실행환경 가이드](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:실행환경가이드)에 등재된 1.0부터 5.x까지의 모든 주요 실행환경 버전(`1.0`, `2.0`, `2.5`, `2.6`, `2.7`, `3.0`, `3.1`, `3.5`, `3.6`, `3.7`, `3.8`, `3.9`, `3.10`, `4.0`, `4.1`, `4.2`, `4.3`, `5.0`) 및 세부 릴리스 패치 버전을 제공합니다. 영문(`eGovFrame`)과 한문(`전자정부표준프레임워크`) 각각 아래 5가지 스타일을 선택할 수 있습니다 — [shields.io](https://shields.io)의 대표 스타일(`flat`, `flat-square`, `plastic`, `for-the-badge`)을 그대로 지원하고, 자체 `outline` 스타일을 더했습니다. (shields.io의 `social` 스타일은 마우스 호버 효과에 기대는 구조라 정적 `<img>` 임베드에서는 의미가 없어 제외했습니다.)

| 스타일 | 예시(영문) | 예시(한문) |
| --- | --- | --- |
| flat | ![flat](badges/5.0.1/flat.svg) | ![flat (한문)](badges/5.0.1/flat-ko.svg) |
| flat-square | ![flat-square](badges/5.0.1/flat-square.svg) | ![flat-square (한문)](badges/5.0.1/flat-square-ko.svg) |
| plastic | ![plastic](badges/5.0.1/plastic.svg) | ![plastic (한문)](badges/5.0.1/plastic-ko.svg) |
| for-the-badge | ![for-the-badge](badges/5.0.1/for-the-badge.svg) | ![for-the-badge (한문)](badges/5.0.1/for-the-badge-ko.svg) |
| outline | ![outline](badges/5.0.1/outline.svg) | ![outline (한문)](badges/5.0.1/outline-ko.svg) |

## 지원 버전

전자정부 표준프레임워크 [실행환경 가이드](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:실행환경가이드)에 등재된 1.0부터 5.x까지 총 52개 버전(주요 실행환경 및 패치 릴리스)을 지원합니다.

- **5.x**: `5.0`, `5.0.0`, `5.0.1`, `5.0.2`, `5.0.3`, `5.0.4`, `5.0.5`, `5.0.6`
- **4.x**: `4.3`, `4.3.0`, `4.3.1`, `4.3.2`, `4.2`, `4.2.0`, `4.2.1`, `4.2.2`, `4.1`, `4.1.0`, `4.1.1`, `4.1.2`, `4.0`, `4.0.0`, `4.0.1`
- **3.x**: `3.10`, `3.10.0`, `3.10.1`, `3.10.2`, `3.9`, `3.9.0`, `3.8`, `3.8.0`, `3.7`, `3.7.0`, `3.6`, `3.6.0`, `3.5`, `3.5.0`, `3.5.1`, `3.1`, `3.1.0`, `3.0`, `3.0.0`
- **2.x**: `2.7`, `2.7.0`, `2.6`, `2.6.0`, `2.5`, `2.5.0`, `2.0`, `2.0.0`
- **1.x**: `1.0`, `1.0.0`

## 버전 추가 및 배지 생성

버전은 실제 사용하는 프레임워크 버전에 맞춰 고릅니다. 이 배지는 프로젝트의 버전을 자동 감지하지 않습니다. 새 버전이 필요하면 `versions.json`에 추가하고 생성 스크립트를 실행해 SVG를 생성하고 커밋합니다.

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

로고는 [eGovFramework 저장소](https://github.com/eGovFramework)의 기존 README 배지에 포함된 SVG를 동일하게 추출했습니다. 로고와 eGovFrame 명칭의 권리는 해당 권리자에게 있습니다.

## 라이선스

이 저장소의 코드(생성 스크립트, 테스트, 워크플로)는 [MIT License](LICENSE)로 배포합니다. 로고 자산(`assets/egovframe-mark.svg`) 및 그로부터 생성된 배지에 포함된 로고 이미지는 이 라이선스의 적용을 받지 않으며, 위에서 설명한 대로 원 권리자에게 귀속됩니다.
