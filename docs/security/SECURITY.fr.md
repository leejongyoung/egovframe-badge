# Politique de sécurité

[![English](../../badges/lang/en/outline.svg)](SECURITY.en.md)
[![한국어](../../badges/lang/ko/outline.svg)](SECURITY.ko.md)
[![Español](../../badges/lang/es/outline.svg)](SECURITY.es.md)
[![Tiếng Việt](../../badges/lang/vi/outline.svg)](SECURITY.vi.md)
[![العربية](../../badges/lang/ar/outline.svg)](SECURITY.ar.md)
[![Français](../../badges/lang/fr/flat.svg)](SECURITY.fr.md)

## Signalement d'une vulnérabilité

**Veuillez ne pas ouvrir d'issue public pour un problème de sécurité.**

Utilisez le signalement privé de vulnérabilités de GitHub :

➡ <https://github.com/leejongyoung/egovframe-badge/security/advisories/new>

Si le signalement privé de vulnérabilités n'est pas activé sur le dépôt, contactez le mainteneur en privé via les moyens de contact du profil GitHub du propriétaire du dépôt au lieu d'ouvrir un issue public.

Veuillez inclure :

- ce qui est affecté (version du badge, script de génération ou workflow)
- comment le reproduire et l'impact attendu
- tout ce que vous avez déjà fait pour le vérifier (hashes, URLs, logs)

Les signalements sont traités en privé jusqu'à ce qu'un correctif soit disponible ; le crédit est accordé sur demande.

## Périmètre

Dans le périmètre :

- SVGs des badges dans [`badges/`](../../badges/) : contenu généré, logo embarqué, métadonnées de version
- Automatisation : [`.github/workflows/`](../../.github/workflows/) et [`scripts/`](../../scripts/). Les nouveaux badges sont générés par le workflow `generate-badges` ; un moyen de faire en sorte que cette étape produise une sortie incorrecte, divulgue le token ou exécute une entrée non fiable compte comme une vulnérabilité.

Hors périmètre, signalez au propriétaire :

- Le framework eGovFrame et son serveur de téléchargement → le projet eGovFrame, <https://www.egovframe.go.kr/> et [eGovFramework](https://github.com/eGovFramework).
- GitHub lui-même → <https://github.com/github/github/security/policy>.
- shields.io → <https://github.com/badges/shields/security/policy>.

## Versions supportées

Seulement ce qui est dans `badges/` sur la branche par défaut est maintenu : toutes les versions listées dans `versions.json`. Les badges supprimés quand un patch plus récent de la même série arrive ne le sont pas.

## Vérifier un badge vous-même

Chaque badge est un SVG autonome avec logo embarqué. Pour vérifier que chaque badge commité correspond à la sortie du générateur :

```bash
python3 scripts/generate.py --check
```