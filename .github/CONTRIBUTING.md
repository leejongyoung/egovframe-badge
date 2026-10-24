# Contributing to eGovFrame Badge

[![English](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/en/flat.svg)](/docs/contributing/CONTRIBUTING.en.md)
[![한국어](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ko/outline.svg)](/docs/contributing/CONTRIBUTING.ko.md)
[![Español](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/es/outline.svg)](/docs/contributing/CONTRIBUTING.es.md)
[![Tiếng Việt](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/vi/outline.svg)](/docs/contributing/CONTRIBUTING.vi.md)
[![العربية](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ar/outline.svg)](/docs/contributing/CONTRIBUTING.ar.md)
[![Français](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/fr/outline.svg)](/docs/contributing/CONTRIBUTING.fr.md)

## Before opening a pull request

```bash
python3 -m pip install PyYAML==6.0.3
python3 -m unittest discover -s tests -v   # script tests
```

The CI runs tests and checks badge generation consistency.

- Commit messages follow the existing style: `feat(badges): add 5.1.0 badges`, `fix(generate): ...`, `docs(readme): ...`, `ci: ...`.
- Do not edit generated SVG files directly. New versions come from `scripts/generate.py` (the `generate-badges` workflow); to re-check existing badges run `python3 scripts/generate.py --check`.
- One badge set per version: adding `5.1.0` generates all 5 styles × 6 languages.
- Documentation entrypoints are generated: edit the `docs/` sources, then run `python3 scripts/sync_readme.py` to refresh `README.md` and the `.github/` entrypoints. Language buttons must point to the localized sources in `docs/`, English included.

## GitHub Actions and billing

- **Free on public repositories:** according to GitHub's billing policy, standard GitHub-hosted runners (`ubuntu-latest`) are **free and unlimited on public repositories**. Badges are generated during `generate-badges.yml` and committed; no Actions artifacts or Release storage is consumed.

## Security

Do not report vulnerabilities in issues; follow the process in [SECURITY.en.md](/docs/security/SECURITY.en.md).
