# 전자정부표준프레임워크 배지 기여 안내

[![한국어](../../badges/lang/ko/flat.svg)](CONTRIBUTING.ko.md)
[![English](../../badges/lang/en/outline.svg)](CONTRIBUTING.en.md)
[![Español](../../badges/lang/es/outline.svg)](CONTRIBUTING.es.md)
[![Tiếng Việt](../../badges/lang/vi/outline.svg)](CONTRIBUTING.vi.md)
[![العربية](../../badges/lang/ar/outline.svg)](CONTRIBUTING.ar.md)
[![Français](../../badges/lang/fr/outline.svg)](CONTRIBUTING.fr.md)

## 풀 리퀘스트 열기 전

```bash
python3 -m pip install PyYAML==6.0.3
python3 -m unittest discover -s tests -v   # 스크립트 테스트
```

CI가 테스트와 배지 생성 일관성을 실행합니다.

- 커밋 메시지는 기존 스타일을 따릅니다: `feat(badges): add 5.1.0 badges`, `fix(generate): ...`, `docs(readme): ...`, `ci: ...`.
- 생성된 SVG 파일을 직접 수정하지 마세요. 새 버전은 `scripts/generate.py`(워크플로 `generate-badges`)에서 나오며, 기존 배지를 다시 검사하려면 `python3 scripts/generate.py --check`을 실행하세요.
- 버전당 배지 세트 하나: `5.1.0` 추가 시 5가지 스타일 × 6개 언어가 생성됩니다.
- 문서 진입점은 자동 생성됩니다. `docs/`의 원본을 수정한 뒤 `python3 scripts/sync_readme.py`를 실행해 `README.md`와 `.github/` 진입점을 갱신하세요. 언어 버튼은 영어를 포함해 `docs/`의 언어별 원본을 가리켜야 합니다.

## GitHub Actions와 과금

- **공개 저장소에서 무료:** GitHub 과금 정책에 따라 표준 GitHub 호스팅 러너(`ubuntu-latest`)는 **공개 저장소에서 무료이고 시간 제한이 없습니다**. 배지는 `generate-badges.yml`에서 생성되어 커밋되며, Actions 아티팩트나 Release 스토리지를 소비하지 않습니다.

## 보안

이슈에 취약점을 신고하지 마세요; [SECURITY.ko.md](../security/SECURITY.ko.md)의 절차를 따르세요.