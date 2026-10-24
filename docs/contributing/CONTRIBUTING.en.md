# Contributing to eGovFrame Badge

[![English](../../badges/lang/en/flat.svg)](CONTRIBUTING.en.md)
[![한국어](../../badges/lang/ko/outline.svg)](CONTRIBUTING.ko.md)
[![Español](../../badges/lang/es/outline.svg)](CONTRIBUTING.es.md)
[![Tiếng Việt](../../badges/lang/vi/outline.svg)](CONTRIBUTING.vi.md)
[![العربية](../../badges/lang/ar/outline.svg)](CONTRIBUTING.ar.md)
[![Français](../../badges/lang/fr/outline.svg)](CONTRIBUTING.fr.md)

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

Do not report vulnerabilities in issues; follow the process in [SECURITY.en.md](../security/SECURITY.en.md).
