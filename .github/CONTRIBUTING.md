# Contributing to eGovFrame Badge

[![English](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/en/flat.svg)](/README.md)
[![한국어](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ko/outline.svg)](/docs/README.ko.md)
[![Español](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/es/outline.svg)](/docs/README.es.md)
[![Tiếng Việt](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/vi/outline.svg)](/docs/README.vi.md)
[![العربية](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ar/outline.svg)](/docs/README.ar.md)
[![Français](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/fr/outline.svg)](/docs/README.fr.md)

## Before opening a pull request

```bash
python3 -m pip install -r requirements.txt
python3 -m unittest discover -s tests -v   # script tests
```

The CI runs tests and checks badge generation consistency.

- Commit messages follow the existing style: `feat(badges): add 5.1.0 badges`, `fix(generate): ...`, `docs(readme): ...`, `ci: ...`.
- Do not edit generated SVG files directly. New versions come from `scripts/generate.py` (the `generate-badges` workflow); to re-check existing badges run `python3 scripts/generate.py --check`.
- One badge set per version: adding `5.1.0` generates all 5 styles × 6 languages.

## GitHub Actions and billing

- **Free on public repositories:** according to GitHub's billing policy, standard GitHub-hosted runners (`ubuntu-latest`) are **free and unlimited on public repositories**. Badges are generated during `generate-badges.yml` and committed; no Actions artifacts or Release storage is consumed.

## Security

Do not report vulnerabilities in issues; follow the process in [SECURITY.md](/docs/security/SECURITY.md).
