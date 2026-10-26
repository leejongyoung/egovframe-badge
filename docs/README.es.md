# Insignia del Marco Estándar de Gobierno Electrónico

<!-- latest-badge:start -->
[![Marco Estándar de Gobierno Electrónico](../badges/unversioned/flat-es.svg)](https://www.egovframe.go.kr/)
[![CI](https://github.com/leejongyoung/egovframe-badge/actions/workflows/verify.yml/badge.svg)](https://github.com/leejongyoung/egovframe-badge/actions/workflows/verify.yml)
[![Generate badges](https://github.com/leejongyoung/egovframe-badge/actions/workflows/generate-badges.yml/badge.svg)](https://github.com/leejongyoung/egovframe-badge/actions/workflows/generate-badges.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](../LICENSE)
<!-- latest-badge:end -->

[![English](../badges/lang/en/outline.svg)](README.en.md)
[![한국어](../badges/lang/ko/outline.svg)](README.ko.md)
[![Español](../badges/lang/es/flat.svg)](README.es.md)
[![Tiếng Việt](../badges/lang/vi/outline.svg)](README.vi.md)
[![العربية](../badges/lang/ar/outline.svg)](README.ar.md)
[![Français](../badges/lang/fr/outline.svg)](README.fr.md)

Una **insignia SVG única** para cada proyecto que utiliza el Marco Estándar de Gobierno Electrónico. En lugar de incrustar logotipos en cada repositorio, referencia una insignia mantenida centralmente con una URL raw. SVG estático — sin JavaScript, sin servidor de despliegue, sin URLs Base64 largas.

## Uso en una línea

Elige la versión, el estilo y el idioma (`en`, `ko`, `es`, `vi`, `ar`, `fr`) desde la ruta de la URL. Los ejemplos a continuación enlazan al portal oficial.

**Inglés**
```md
[![eGovFrame 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat.svg)](https://www.egovframe.go.kr)
```

**Español**
```md
[![Marco Estándar de Gobierno Electrónico 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-es.svg)](https://www.egovframe.go.kr)
```

**Insignias de versión multilingües (`vi` vietnamita · `ar` árabe · `fr` francés)**
```md
[![Khung chuẩn Chính phủ điện tử 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-vi.svg)](https://www.egovframe.go.kr)
[![الإطار القياسي للحكومة الإلكترونية 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-ar.svg)](https://www.egovframe.go.kr)
[![Cadre standard de l'administration électronique 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-fr.svg)](https://www.egovframe.go.kr)
```
*(Todas las insignias multilingües soportan tanto las rutas `badges/5.0.2/flat-<lang>.svg` como `badges/5.0.2/<lang>/flat.svg`.)*

## Detección automática de versiones

Un README puede mostrar las versiones que declaran los archivos de construcción de su proyecto. `scripts/detect_version.py` las encuentra y reescribe los bloques marcados del README, y un workflow puede ejecutarlo en cada push.

### Dónde se encuentran las versiones

| Entorno | Componente | Declarado en |
| --- | --- | --- |
| Entorno de ejecución | Marco Estándar de Gobierno Electrónico | `pom.xml`: `org.egovframe.rte.version`, `egovframework.rte.version`, `<parent>` · `<dependency>`: `org.egovframe.boot`, `org.egovframe.web`, `org.egovframe.rte`<br>`build.gradle(.kts)`: `egovframeBootParentVersion`, `org.egovframe.*:artifact:version`<br>`settings.gradle(.kts)`, `gradle.properties`, `libs.versions.toml` |
| Entorno de desarrollo | Java | `pom.xml`: `java.version`, `maven.compiler.release`, `maven.compiler.source`, `maven.compiler.target`<br>`build.gradle(.kts)`: `sourceCompatibility`, `JavaLanguageVersion.of(17)` |
| Entorno de desarrollo | Spring Boot | `pom.xml`: `<parent>` `spring-boot-starter-parent`<br>`build.gradle(.kts)`: `id 'org.springframework.boot' version '3.5.6'` |
| Entorno de desarrollo | Gradle | `gradle/wrapper/gradle-wrapper.properties`: `distributionUrl` (`gradle-8.5-bin.zip`) |

- Si varios módulos declaran una versión, gana la más alta.
- Las propiedades de Maven y las referencias `${...}` se resuelven en el `pom.xml` que las declara, sin mezclar módulos. No se adivinan propiedades del padre o externas que no se puedan resolver.
- Se ignoran los comentarios y se omiten las carpetas de compilación y dependencias (`target`, `build`, `node_modules`, ...).
- Solo se muestra lo que el proyecto declara por sí mismo: los parents de la versión 4.x/5.x traen su propio Spring Boot y Java, que no aparecen si el archivo de construcción no los indica.
- Un proyecto que no declara ninguna versión recibe la insignia solo con el nombre; una versión declarada sin insignia publicada (que no está en `versions.json`) recibe la insignia solo con el nombre y una advertencia.

### Marcadores del README

Coloca los marcadores donde debe ir el contenido. Cada bloque es opcional, pero se necesita al menos uno: el primero se convierte en la insignia (la de versión, o la insignia solo con el nombre cuando no se declara ninguna) y el segundo en una tabla con las versiones detectadas y el archivo que declara cada una.

```md
<!-- egovframe-badge:start -->
[![Marco Estándar de Gobierno Electrónico](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/unversioned/flat-es.svg)](https://www.egovframe.go.kr/)
<!-- egovframe-badge:end -->

<!-- egovframe-environment:start -->
<!-- egovframe-environment:end -->
```

Resultado para `examples/sample-gradle-project`:

| Categoría | Componente | Versión | Fuente |
| --- | --- | --- | --- |
| Entorno de ejecución | Marco Estándar de Gobierno Electrónico | 5.0.0 | `build.gradle` |
| Entorno de desarrollo | Java | 17 | `build.gradle` |
| Entorno de desarrollo | Spring Boot | 3.5.6 | `build.gradle` |
| Entorno de desarrollo | Gradle | 8.5 | `gradle/wrapper/gradle-wrapper.properties` |

### Ejecutarlo

Ejecútalo en local (añade `--check` para que falle en lugar de escribir, útil en un CI que solo verifica):

```bash
python3 scripts/detect_version.py --project . --readme README.md --language es --style flat --write
```

### Ejecutarlo en CI

[`.github/workflows/example-egovframe-badge.yml`](../.github/workflows/example-egovframe-badge.yml) es un ejemplo funcional: en cada push que toca los proyectos ejecuta el script y confirma de vuelta en la rama los README reescritos. Se ejecuta sobre `examples/sample-project` (Maven), `examples/sample-gradle-project` (Gradle: Java, Spring Boot, Gradle) y `examples/sample-project-unversioned` (sin declaración). Copia `scripts/detect_version.py` y el workflow a tu proyecto, establece `PROJECT_DIRS` en `.` y añade los marcadores. Para pasos propios, `--github-output` escribe `version`, `badge_version`, `source`, `java`, `spring_boot`, `gradle` y `changed` en `$GITHUB_OUTPUT`.

## Botones de insignia para selector de idioma (`badges/lang/`)

Botones de insignia independientes para cambiar de idioma en `README` multilingües (`en`, `ko`, `es`, `vi`, `ar`, `fr`, `mn`, `bg`, `ne`). El idioma actual usa `flat.svg`; los demás usan `outline.svg` (o todos `flat.svg`).

```md
[![English](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/en/flat.svg)](README.md)
[![한국어](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ko/outline.svg)](README.ko.md)
[![Español](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/es/outline.svg)](docs/README.es.md)
[![Tiếng Việt](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/vi/outline.svg)](docs/README.vi.md)
[![العربية](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ar/outline.svg)](docs/README.ar.md)
[![Français](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/fr/outline.svg)](docs/README.fr.md)
```

Todas las versiones principales del [Guía del entorno de ejecución del Marco Estándar de Gobierno Electrónico](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:실행환경가이드) — de 1.0 a 5.x (53 versiones en total) — con cinco estilos cada una: `flat`, `flat-square`, `plastic`, `for-the-badge` y el estilo personalizado `outline` (el estilo `social` de shields.io se excluye porque depende de efectos hover).

| Estilo | Ejemplo (Inglés) | Ejemplo (Español) | Botón de idioma |
| --- | --- | --- | --- |
| flat | ![flat](../badges/5.0.1/flat.svg) | ![flat (Español)](../badges/5.0.1/flat-es.svg) | ![Español](../badges/lang/es/flat.svg) |
| flat-square | ![flat-square](../badges/5.0.1/flat-square.svg) | ![flat-square (Español)](../badges/5.0.1/flat-square-es.svg) | ![Español](../badges/lang/es/flat-square.svg) |
| plastic | ![plastic](../badges/5.0.1/plastic.svg) | ![plastic (Español)](../badges/5.0.1/plastic-es.svg) | ![Español](../badges/lang/es/plastic.svg) |
| for-the-badge | ![for-the-badge](../badges/5.0.1/for-the-badge.svg) | ![for-the-badge (Español)](../badges/5.0.1/for-the-badge-es.svg) | ![Español](../badges/lang/es/for-the-badge.svg) |
| outline | ![outline](../badges/5.0.1/outline.svg) | ![outline (Español)](../badges/5.0.1/outline-es.svg) | ![Español](../badges/lang/es/outline.svg) |

## Versiones soportadas

Todas las 53 versiones de la Guía del entorno de ejecución del Marco Estándar de Gobierno Electrónico:

- **5.x**: `5.0`, `5.0.0`, `5.0.1`, `5.0.2`, `5.0.3`, `5.0.4`, `5.0.5`, `5.0.6`, `5.0.7`
- **4.x**: `4.3`, `4.3.0`, `4.3.1`, `4.3.2`, `4.2`, `4.2.0`, `4.2.1`, `4.2.2`, `4.1`, `4.1.0`, `4.1.1`, `4.1.2`, `4.0`, `4.0.0`, `4.0.1`
- **3.x**: `3.10`, `3.10.0`, `3.10.1`, `3.10.2`, `3.9`, `3.9.0`, `3.8`, `3.8.0`, `3.7`, `3.7.0`, `3.6`, `3.6.0`, `3.5`, `3.5.0`, `3.5.1`, `3.1`, `3.1.0`, `3.0`, `3.0.0`
- **2.x**: `2.7`, `2.7.0`, `2.6`, `2.6.0`, `2.5`, `2.5.0`, `2.0`, `2.0.0`
- **1.x**: `1.0`, `1.0.0`

## Agregar versiones y generar insignias

Para agregar una nueva versión, edita `versions.json` y ejecuta el generador (la versión del propio proyecto la detecta el script descrito arriba):

```sh
python3 scripts/generate.py
python3 -m unittest discover -s tests -v
python3 scripts/generate.py --check
```

## Diseño

- Los SVG se confirman y se sirven via URLs raw de GitHub. Los renderizadores de README los cargan directamente; no se requiere servidor de despliegue.
- Fuente única del logotipo en `assets/egovframe-mark.svg`. Todas las insignias generadas incrustan el logotipo — sin dependencias de imágenes externas.
- La versión y el estilo se fijan en la ruta del archivo para que las insignias README existentes no cambien inesperadamente cuando llegan nuevos lanzamientos.
- `scripts/generate.py --check` y CI verifican que la salida generada coincida con la fuente. Los cambios de estilo se aplican consistentemente en todas las versiones.
- El estilo `plastic` usa las mismas paradas de gradiente brilloso que shields.io. `for-the-badge` usa esquinas rectas (`rx="0"`) como shields.io.

Logotipo extraído de la insignia README existente de eGovFramework. Los derechos del logotipo y del nombre del Marco Estándar de Gobierno Electrónico pertenecen a sus respectivos propietarios.

## Licencia

El código (script de generación, tests, workflows) tiene [licencia MIT](../LICENSE). El recurso del logotipo (`assets/egovframe-mark.svg`) y los logotipos incrustados en las insignias generadas **no** están cubiertos por esta licencia y pertenecen a sus propietarios originales como se indica arriba.