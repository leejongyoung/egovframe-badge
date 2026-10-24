# Contribuer à eGovFrame Badge

[![English](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/en/outline.svg)](../../README.md)
[![한국어](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ko/outline.svg)](../README.ko.md)
[![Español](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/es/outline.svg)](../README.es.md)
[![Tiếng Việt](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/vi/outline.svg)](../README.vi.md)
[![العربية](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ar/outline.svg)](../README.ar.md)
[![Français](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/fr/flat.svg)](../README.fr.md)

## Avant d'ouvrir une pull request

```bash
python3 -m pip install -r requirements.txt
python3 -m unittest discover -s tests -v   # tests des scripts
```

Le CI exécute les tests et vérifie la cohérence de la génération des badges.

- Les messages de commit suivent le style existant : `feat(badges): add 5.1.0 badges`, `fix(generate): ...`, `docs(readme): ...`, `ci: ...`.
- Ne modifiez pas les fichiers SVG générés directement. Les nouvelles versions proviennent de `scripts/generate.py` (le workflow `generate-badges`) ; pour revérifier les badges existants, exécutez `python3 scripts/generate.py --check`.
- Un ensemble de badges par version : l'ajout de `5.1.0` génère les 5 styles × 6 langues.

## GitHub Actions et facturation

- **Gratuit sur les dépôts publics :** selon la politique de facturation de GitHub, les runners standard hébergés par GitHub (`ubuntu-latest`) sont **gratuits et illimités en minutes sur les dépôts publics**. Les badges sont générés pendant `generate-badges.yml` et commités ; aucun artefact Actions ni stockage Release n'est consommé.

## Sécurité

Ne signalez pas de vulnérabilités dans les issues ; suivez la procédure dans [SECURITY.md](../security/SECURITY.md).