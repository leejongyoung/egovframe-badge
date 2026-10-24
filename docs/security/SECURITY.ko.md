# 보안 정책

[![English](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/en/outline.svg)](../../README.md)
[![한국어](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ko/flat.svg)](../README.ko.md)
[![Español](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/es/outline.svg)](../README.es.md)
[![Tiếng Việt](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/vi/outline.svg)](../README.vi.md)
[![العربية](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ar/outline.svg)](../README.ar.md)
[![Français](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/fr/outline.svg)](../README.fr.md)

## 취약점 신고

**보안 문제를 퍼블릭 이슈로 열지 마세요.**

GitHub의 비공개 취약점 신고를 사용하세요:

➡ <https://github.com/leejongyoung/egovframe-badge/security/advisories/new>

저장소에서 비공개 취약점 신고가 활성화되어 있지 않으면, 퍼블릭 이슈 대신 이메일로 신고해 주세요.

다음을 포함해 주세요:

- 무엇이 영향받는지 (배지 버전, 생성 스크립트, 워크플로)
- 재현 방법과 예상되는 영향
- 이미 확인한 내용 (해시, URL, 로그)

수정이 나올 때까지 비공개로 처리되며, 요청 시 크레딧을 드립니다.

## 범위

범위 내:

- [`badges/`](../badges/)의 배지 SVG: 생성된 콘텐츠, 임베디드 로고, 버전 메타데이터
- 자동화: [`.github/workflows/`](../.github/workflows/)와 [`scripts/`](../scripts/). 새 배지는 `generate-badges` 워크플로에서 생성되며, 이 단계가 잘못된 출력을 내거나 토큰을 유출하거나 신뢰할 수 없는 입력을 실행하게 만드는 것은 취약점으로 간주합니다.

범위 밖, 소유자에게 신고:

- eGovFrame 프레임워크와 다운로드 서버 → eGovFrame 프로젝트, <https://www.egovframe.go.kr/> 및 [eGovFramework](https://github.com/eGovFramework).
- GitHub 자체 → <https://github.com/github/github/security/policy>.
- shields.io → <https://github.com/badges/shields/security/policy>.

## 지원 버전

기본 브랜치의 `badges/`에 있는 것만 유지 관리됩니다: `versions.json`에 나열된 모든 버전. 같은 시리즈의 새 패치가 나오면 제거된 배지는 지원하지 않습니다.

## 배지 직접 검증

모든 배지는 임베디드 로고를 포함한 독립형 SVG입니다. CI에서 소스와 대조해 재생성 및 검증하려면:

```bash
gh workflow run generate-badges.yml -R leejongyoung/egovframe-badge -f version=5.0.2
```