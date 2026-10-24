# Contribuer à eGovFrame Badge

[![English](../../badges/lang/en/outline.svg)](CONTRIBUTING.en.md)
[![한국어](../../badges/lang/ko/outline.svg)](CONTRIBUTING.ko.md)
[![Español](../../badges/lang/es/outline.svg)](CONTRIBUTING.es.md)
[![Tiếng Việt](../../badges/lang/vi/outline.svg)](CONTRIBUTING.vi.md)
[![العربية](../../badges/lang/ar/outline.svg)](CONTRIBUTING.ar.md)
[![Français](../../badges/lang/fr/flat.svg)](CONTRIBUTING.fr.md)

## Avant d'ouvrir une pull request

```bash
python3 -m pip install PyYAML==6.0.3
python3 -m unittest discover -s tests -v   # tests des scripts
```

Le CI exécute les tests et vérifie la cohérence de la génération des badges.

- Les messages de commit suivent le style existant : `feat(badges): add 5.1.0 badges`, `fix(generate): ...`, `docs(readme): ...`, `ci: ...`.
- Ne modifiez pas les fichiers SVG générés directement. Les nouvelles versions proviennent de `scripts/generate.py` (le workflow `generate-badges`) ; pour revérifier les badges existants, exécutez `python3 scripts/generate.py --check`.
- Un ensemble de badges par version : l'ajout de `5.1.0` génère les 5 styles × 6 langues.
- Les points d'entrée de la documentation sont générés : modifiez les sources de `docs/`, puis exécutez `python3 scripts/sync_readme.py` pour actualiser `README.md` et les points d'entrée de `.github/`. Les boutons de langue doivent pointer vers les sources localisées dans `docs/`, anglais compris.

## GitHub Actions et facturation

- **Gratuit sur les dépôts publics :** selon la politique de facturation de GitHub, les runners standard hébergés par GitHub (`ubuntu-latest`) sont **gratuits et illimités en minutes sur les dépôts publics**. Les badges sont générés pendant `generate-badges.yml` et commités ; aucun artefact Actions ni stockage Release n'est consommé.

## Sécurité

Ne signalez pas de vulnérabilités dans les issues ; suivez la procédure dans [SECURITY.fr.md](../security/SECURITY.fr.md).