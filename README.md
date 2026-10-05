# eGovFrame badge

전자정부 표준프레임워크(eGovFrame)를 사용하는 **모든 프로젝트**가 README에 가져다 쓸 수 있는 SVG 배지입니다. 저장소마다 로고를 각자 하드코딩하는 대신, 한 곳에서 관리하는 배지를 raw URL 한 줄로 참조합니다. 정적 SVG라서 JavaScript, 별도 배포 서버, 긴 Base64 URL이 필요하지 않습니다.

## 한 줄로 사용

버전과 스타일을 URL 경로에서 선택합니다. 아래 예시는 공식 포털로 연결됩니다.

```md
[![eGovFrame 5.0.1](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.1/flat.svg)](https://www.egovframe.go.kr)
```

`5.0`, `5.0.0`, `5.0.1` 버전을 제공합니다. 각 버전에서 아래 5가지 스타일을 선택할 수 있습니다 — [shields.io](https://shields.io)의 대표 스타일(`flat`, `flat-square`, `plastic`, `for-the-badge`)을 그대로 지원하고, 자체 `outline` 스타일을 더했습니다. (shields.io의 `social` 스타일은 마우스 호버 효과에 기대는 구조라 정적 `<img>` 임베드에서는 의미가 없어 제외했습니다.)

| 스타일 | 예시 |
| --- | --- |
| flat | ![flat](badges/5.0.1/flat.svg) |
| flat-square | ![flat-square](badges/5.0.1/flat-square.svg) |
| plastic | ![plastic](badges/5.0.1/plastic.svg) |
| for-the-badge | ![for-the-badge](badges/5.0.1/for-the-badge.svg) |
| outline | ![outline](badges/5.0.1/outline.svg) |

버전은 실제 사용하는 프레임워크 버전에 맞춰 고릅니다. 이 배지는 프로젝트의 버전을 자동 감지하지 않습니다. 새 버전이 필요하면 `versions.json`에 추가하고 생성 스크립트를 실행해 SVG를 커밋합니다.

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
