# eGovFrame badge

eGovFrame 저장소 README에서 공통으로 사용할 수 있는 SVG 배지입니다. 기존 README 5곳에 반복된 동일 로고를 한 저장소에서 관리합니다. 정적 SVG라서 JavaScript, 별도 서비스, 긴 Base64 URL이 필요하지 않습니다.

## 한 줄로 사용

버전과 스타일을 URL 경로에서 선택합니다. 아래 예시는 공식 포털로 연결됩니다.

```md
[![eGovFrame 5.0.1](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.1/flat.svg)](https://www.egovframe.go.kr)
```

`5.0`, `5.0.0`, `5.0.1` 버전을 제공합니다. 각 버전에서 `flat`, `flat-square`, `for-the-badge`, `outline` 스타일을 선택할 수 있습니다.

| 스타일 | 예시 |
| --- | --- |
| flat | ![flat](badges/5.0.1/flat.svg) |
| flat-square | ![flat-square](badges/5.0.1/flat-square.svg) |
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

로고는 [eGovFramework 저장소](https://github.com/eGovFramework)의 기존 README 배지에 포함된 SVG를 동일하게 추출했습니다. 로고와 eGovFrame 명칭의 권리는 해당 권리자에게 있습니다. 이 저장소는 공식 프로젝트를 대표하지 않습니다.
