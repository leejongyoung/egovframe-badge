# Badge du Cadre standard de l'administration électronique

<!-- latest-badge:start -->
[![Cadre standard de l'administration électronique](../badges/unversioned/flat-fr.svg)](https://www.egovframe.go.kr/)
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

Un **seul badge SVG** pour chaque projet utilisant le Cadre standard de l'administration électronique. Au lieu d'incruster les logos dans chaque dépôt, référencez un badge maintenu centralement via une URL raw. SVG statique — pas de JavaScript, pas de serveur de déploiement, pas d'URLs Base64 longues.

## Utilisation en une ligne

Choisissez la version, le style et la langue (`en`, `ko`, `es`, `vi`, `ar`, `fr`) depuis le chemin de l'URL. Les exemples ci-dessous renvoient au portail officiel.

**Anglais**
```md
[![eGovFrame 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat.svg)](https://www.egovframe.go.kr)
```

**Français**
```md
[![Cadre standard de l'administration électronique 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-fr.svg)](https://www.egovframe.go.kr)
```

**Badges de version multilingues (`es` espagnol · `vi` vietnamien · `ar` arabe)**
```md
[![Marco Estándar de Gobierno Electrónico 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-es.svg)](https://www.egovframe.go.kr)
[![Khung chuẩn Chính phủ điện tử 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-vi.svg)](https://www.egovframe.go.kr)
[![الإطار القياسي للحكومة الإلكترونية 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-ar.svg)](https://www.egovframe.go.kr)
```
*(Tous les badges multilingues supportent à la fois les chemins `badges/5.0.2/flat-<lang>.svg` et `badges/5.0.2/<lang>/flat.svg`.)*

## Détection automatique des versions

Un README peut afficher les versions que déclarent les fichiers de build de son projet. `scripts/detect_version.py` les trouve et réécrit les blocs balisés du README, et un workflow peut l'exécuter à chaque push.

### Où les versions sont trouvées

| Environnement | Composant | Déclaré dans |
| --- | --- | --- |
| Environnement d'exécution | Cadre standard de l'administration électronique | `pom.xml`: `org.egovframe.rte.version`, `egovframework.rte.version`, `<parent>` · `<dependency>`: `org.egovframe.boot`, `org.egovframe.web`, `org.egovframe.rte`<br>`build.gradle(.kts)`: `egovframeBootParentVersion`, `org.egovframe.*:artifact:version`<br>`settings.gradle(.kts)`, `gradle.properties`, `libs.versions.toml` |
| Environnement de développement | Java | `pom.xml`: `java.version`, `maven.compiler.release`, `maven.compiler.source`, `maven.compiler.target`<br>`build.gradle(.kts)`: `sourceCompatibility`, `JavaLanguageVersion.of(17)` |
| Environnement de développement | Spring Boot | `pom.xml`: `<parent>` `spring-boot-starter-parent`<br>`build.gradle(.kts)`: `id 'org.springframework.boot' version '3.5.6'` |
| Environnement de développement | Gradle | `gradle/wrapper/gradle-wrapper.properties`: `distributionUrl` (`gradle-8.5-bin.zip`) |

- Si plusieurs modules déclarent une version, la plus élevée l'emporte.
- Les propriétés Maven et les références `${...}` sont résolues dans le `pom.xml` qui les déclare, sans fusion entre modules. Les propriétés parentes ou externes non résolues ne sont pas devinées.
- Les commentaires sont ignorés, et les dossiers de sortie de build et de dépendances (`target`, `build`, `node_modules`, ...) sont ignorés.
- Seul ce que le projet déclare lui-même est affiché : les parents des versions 4.x/5.x apportent leur propre Spring Boot et Java, qui n'apparaissent pas si le fichier de build ne les indique pas.
- Un projet qui ne déclare aucune version reçoit le badge du nom seul ; une version déclarée sans badge publié (absente de `versions.json`) reçoit le badge du nom seul et un avertissement.

### Balises du README

Placez les balises là où le contenu doit apparaître. Chaque bloc est facultatif, mais il en faut au moins un : le premier devient le badge (le badge de version, ou le badge du nom seul quand aucune version n'est déclarée), le second un tableau des versions détectées avec le fichier qui déclare chacune.

```md
<!-- egovframe-badge:start -->
[![Cadre standard de l'administration électronique](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/unversioned/flat-fr.svg)](https://www.egovframe.go.kr/)
<!-- egovframe-badge:end -->

<!-- egovframe-environment:start -->
<!-- egovframe-environment:end -->
```

Résultat pour `examples/sample-gradle-project` :

| Catégorie | Composant | Version | Source |
| --- | --- | --- | --- |
| Environnement d'exécution | Cadre standard de l'administration électronique | 5.0.0 | `build.gradle` |
| Environnement de développement | Java | 17 | `build.gradle` |
| Environnement de développement | Spring Boot | 3.5.6 | `build.gradle` |
| Environnement de développement | Gradle | 8.5 | `gradle/wrapper/gradle-wrapper.properties` |

### L'exécuter

Exécutez-le en local (ajoutez `--check` pour échouer au lieu d'écrire, utile pour une CI qui ne fait que vérifier) :

```bash
python3 scripts/detect_version.py --project . --readme README.md --language fr --style flat --write
```

### L'exécuter en CI

[`.github/workflows/example-egovframe-badge.yml`](../.github/workflows/example-egovframe-badge.yml) est un exemple fonctionnel : à chaque push qui touche les projets, il exécute le script et commite les README réécrits sur la branche. Il tourne sur `examples/sample-project` (Maven), `examples/sample-gradle-project` (Gradle : Java, Spring Boot, Gradle) et `examples/sample-project-unversioned` (sans déclaration). Copiez `scripts/detect_version.py`, le fichier racine `versions.json` et le workflow aux mêmes chemins dans votre dépôt. Gardez `versions.json` à la racine, même pour les projets sans déclaration de version ; pour un autre emplacement, passez `--versions path/to/versions.json`. Mettez `PROJECT_DIRS` à `.` et ajoutez les balises au README. Pour des étapes personnalisées, `--github-output` écrit `version`, `badge_version`, `source`, `java`, `spring_boot`, `gradle` et `changed` dans `$GITHUB_OUTPUT`.

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

Toutes les versions principales du [Guide de l'environnement d'exécution du Cadre standard de l'administration électronique](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:실행환경가이드) — de 1.0 à 5.x (53 versions au total) — avec cinq styles chacun : `flat`, `flat-square`, `plastic`, `for-the-badge` et le style personnalisé `outline` (le style `social` de shields.io est exclu car il dépend des effets hover).

| Style | Exemple (Anglais) | Exemple (Français) | Bouton de langue |
| --- | --- | --- | --- |
| flat | ![flat](../badges/5.0.1/flat.svg) | ![flat (Français)](../badges/5.0.1/flat-fr.svg) | ![Français](../badges/lang/fr/flat.svg) |
| flat-square | ![flat-square](../badges/5.0.1/flat-square.svg) | ![flat-square (Français)](../badges/5.0.1/flat-square-fr.svg) | ![Français](../badges/lang/fr/flat-square.svg) |
| plastic | ![plastic](../badges/5.0.1/plastic.svg) | ![plastic (Français)](../badges/5.0.1/plastic-fr.svg) | ![Français](../badges/lang/fr/plastic.svg) |
| for-the-badge | ![for-the-badge](../badges/5.0.1/for-the-badge.svg) | ![for-the-badge (Français)](../badges/5.0.1/for-the-badge-fr.svg) | ![Français](../badges/lang/fr/for-the-badge.svg) |
| outline | ![outline](../badges/5.0.1/outline.svg) | ![outline (Français)](../badges/5.0.1/outline-fr.svg) | ![Français](../badges/lang/fr/outline.svg) |

## Versions supportées

Toutes les 53 versions du guide de l'environnement d'exécution du Cadre standard de l'administration électronique :

- **5.x** : `5.0`, `5.0.0`, `5.0.1`, `5.0.2`, `5.0.3`, `5.0.4`, `5.0.5`, `5.0.6`, `5.0.7`
- **4.x** : `4.3`, `4.3.0`, `4.3.1`, `4.3.2`, `4.2`, `4.2.0`, `4.2.1`, `4.2.2`, `4.1`, `4.1.0`, `4.1.1`, `4.1.2`, `4.0`, `4.0.0`, `4.0.1`
- **3.x** : `3.10`, `3.10.0`, `3.10.1`, `3.10.2`, `3.9`, `3.9.0`, `3.8`, `3.8.0`, `3.7`, `3.7.0`, `3.6`, `3.6.0`, `3.5`, `3.5.0`, `3.5.1`, `3.1`, `3.1.0`, `3.0`, `3.0.0`
- **2.x** : `2.7`, `2.7.0`, `2.6`, `2.6.0`, `2.5`, `2.5.0`, `2.0`, `2.0.0`
- **1.x** : `1.0`, `1.0.0`

## Ajout de versions et génération de badges

Pour ajouter une nouvelle version, modifiez `versions.json` et lancez le générateur (la version du projet lui-même est détectée par le script décrit ci-dessus) :

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

Logo extrait du badge README existant d'eGovFramework. Les droits du logo et du nom du Cadre standard de l'administration électronique appartiennent à leurs propriétaires respectifs.

## Licence

Le code (script de génération, tests, workflows) est sous [licence MIT](../LICENSE). La ressource logo (`assets/egovframe-mark.svg`) et les logos embarqués dans les badges générés **ne sont pas** couverts par cette licence et appartiennent à leurs propriétaires originaux comme indiqué ci-dessus.