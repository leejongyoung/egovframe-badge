# Badge eGovFrame

<!-- latest-badge:start -->
[![Cadre standard eGovFrame 5.0.6](../badges/5.0.6/flat-fr.svg)](https://www.egovframe.go.kr/)
[![CI](https://github.com/leejongyoung/egovframe-badge/actions/workflows/verify.yml/badge.svg)](https://github.com/leejongyoung/egovframe-badge/actions/workflows/verify.yml)
[![Generate badges](https://github.com/leejongyoung/egovframe-badge/actions/workflows/generate-badges.yml/badge.svg)](https://github.com/leejongyoung/egovframe-badge/actions/workflows/generate-badges.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](../LICENSE)
<!-- latest-badge:end -->

[![English](../badges/lang/en/outline.svg)](README.en.md)
[![한국어](../badges/lang/ko/outline.svg)](README.ko.md)
[![Español](../badges/lang/es/outline.svg)](README.es.md)
[![Tiếng Việt](../badges/lang/vi/outline.svg)](README.vi.md)
[![العربية](../badges/lang/ar/outline.svg)](README.ar.md)
[![Français](../badges/lang/fr/flat.svg)](README.fr.md)

Un **seul badge SVG** pour chaque projet utilisant eGovFrame (cadre électronique gouvernemental). Au lieu d'incrustation les logos dans chaque dépôt, référencez un badge maintenu centralement via une URL raw. SVG statique — pas de JavaScript, pas de serveur de déploiement, pas d'URLs Base64 longues.

## Utilisation en une ligne

Choisissez la version, le style et la langue (`en`, `ko`, `es`, `vi`, `ar`, `fr`) depuis le chemin de l'URL. Les exemples ci-dessous renvoient au portail officiel.

**Anglais (`eGovFrame`)**
```md
[![eGovFrame 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat.svg)](https://www.egovframe.go.kr)
```

**Coréen (`전자정부표준프레임워크`)**
```md
[![전자정부표준프레임워크 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-ko.svg)](https://www.egovframe.go.kr)
```

**Badges de version multilingues (`es` Espagnol · `vi` Vietnamien · `ar` Arabe · `fr` Français)**
```md
[![Marco Estándar eGovFrame 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-es.svg)](https://www.egovframe.go.kr)
[![Khung chuẩn eGovFrame 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-vi.svg)](https://www.egovframe.go.kr)
[![إطار eGovFrame القياسي 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-ar.svg)](https://www.egovframe.go.kr)
[![Cadre standard eGovFrame 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-fr.svg)](https://www.egovframe.go.kr)
```
*(Tous les badges multilingues supportent à la fois les chemins `badges/5.0.2/flat-<lang>.svg` et `badges/5.0.2/<lang>/flat.svg`.)*

## Boutons de badge pour sélecteur de langue (`badges/lang/`)

Boutons de badge autonomes pour le changement de langue dans les `README` multilingues (`en`, `ko`, `es`, `vi`, `ar`, `fr`, `mn`, `bg`, `ne`). La langue courante utilise `flat.svg` ; les autres utilisent `outline.svg` (ou tous `flat.svg`).

```md
[![English](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/en/flat.svg)](README.md)
[![한국어](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ko/outline.svg)](README.ko.md)
[![Español](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/es/outline.svg)](docs/README.es.md)
[![Tiếng Việt](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/vi/outline.svg)](docs/README.vi.md)
[![العربية](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ar/outline.svg)](docs/README.ar.md)
[![Français](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/fr/outline.svg)](docs/README.fr.md)
```

Toutes les versions principales du [eGovFrame Runtime Guide](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:실행환경가이드) — de 1.0 à 5.x (52 versions au total) — avec cinq styles chacun : `flat`, `flat-square`, `plastic`, `for-the-badge` et le style personnalisé `outline` (le style `social` de shields.io est exclu car il dépend des effets hover).

| Style | Exemple (Anglais) | Exemple (Coréen) |
| --- | --- | --- |
| flat | ![flat](../badges/5.0.1/flat.svg) | ![flat (Coréen)](../badges/5.0.1/flat-ko.svg) |
| flat-square | ![flat-square](../badges/5.0.1/flat-square.svg) | ![flat-square (Coréen)](../badges/5.0.1/flat-square-ko.svg) |
| plastic | ![plastic](../badges/5.0.1/plastic.svg) | ![plastic (Coréen)](../badges/5.0.1/plastic-ko.svg) |
| for-the-badge | ![for-the-badge](../badges/5.0.1/for-the-badge.svg) | ![for-the-badge (Coréen)](../badges/5.0.1/for-the-badge-ko.svg) |
| outline | ![outline](../badges/5.0.1/outline.svg) | ![outline (Coréen)](../badges/5.0.1/outline-ko.svg) |

## Versions supportées

Toutes les 52 versions du guide d'exécution eGovFrame :

- **5.x** : `5.0`, `5.0.0`, `5.0.1`, `5.0.2`, `5.0.3`, `5.0.4`, `5.0.5`, `5.0.6`
- **4.x** : `4.3`, `4.3.0`, `4.3.1`, `4.3.2`, `4.2`, `4.2.0`, `4.2.1`, `4.2.2`, `4.1`, `4.1.0`, `4.1.1`, `4.1.2`, `4.0`, `4.0.0`, `4.0.1`
- **3.x** : `3.10`, `3.10.0`, `3.10.1`, `3.10.2`, `3.9`, `3.9.0`, `3.8`, `3.8.0`, `3.7`, `3.7.0`, `3.6`, `3.6.0`, `3.5`, `3.5.0`, `3.5.1`, `3.1`, `3.1.0`, `3.0`, `3.0.0`
- **2.x** : `2.7`, `2.7.0`, `2.6`, `2.6.0`, `2.5`, `2.5.0`, `2.0`, `2.0.0`
- **1.x** : `1.0`, `1.0.0`

## Ajout de versions et génération de badges

Choisissez la version correspondant à votre framework. Ce badge ne détecte **pas** automatiquement la version de votre projet. Pour ajouter une nouvelle version, modifiez `versions.json` et lancez le générateur :

```sh
python3 scripts/generate.py
python3 -m unittest discover -s tests -v
python3 scripts/generate.py --check
```

## Conception

- Les SVG sont commités et servis via les URLs raw de GitHub. Les moteurs de rendu README les chargent directement ; pas de serveur de déploiement requis.
- Source unique du logo en `assets/egovframe-mark.svg`. Tous les badges générés embarquent le logo — pas de dépendances d'images externes.
- La version et le style sont fixés dans le chemin du fichier pour que les badges README existants ne changent pas inopinément avec les nouvelles versions.
- `scripts/generate.py --check` et CI vérifient que la sortie générée correspond à la source. Les changements de style s'appliquent de façon cohérente sur toutes les versions.
- Le style `plastic` utilise les mêmes arrêts de gradient glossy que shields.io. `for-the-badge` utilise des coins carrés (`rx="0"`) comme shields.io.

Logo extrait du badge README existant d'eGovFramework. Les droits du logo et du nom eGovFrame appartiennent à leurs propriétaires respectifs.

## Licence

Le code (script de génération, tests, workflows) est sous [licence MIT](../LICENSE). La ressource logo (`assets/egovframe-mark.svg`) et les logos embarqués dans les badges générés **ne sont pas** couverts par cette licence et appartiennent à leurs propriétaires originaux comme indiqué ci-dessus.