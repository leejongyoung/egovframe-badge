# Insignia eGovFrame

<!-- latest-badge:start -->
[![Marco Estándar eGovFrame 5.0.6](../badges/5.0.6/flat-es.svg)](https://www.egovframe.go.kr/)
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

Una **insignia SVG única** para cada proyecto que utiliza eGovFrame (marco electrónico de gobierno). En lugar de incrustar logotipos en cada repositorio, referencia una insignia mantenida centralmente con una URL raw. SVG estático — sin JavaScript, sin servidor de despliegue, sin URLs Base64 largas.

## Uso en una línea

Elige la versión, el estilo y el idioma (`en`, `ko`, `es`, `vi`, `ar`, `fr`) desde la ruta de la URL. Los ejemplos a continuación enlazan al portal oficial.

**Inglés (`eGovFrame`)**
```md
[![eGovFrame 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat.svg)](https://www.egovframe.go.kr)
```

**Coreano (`전자정부표준프레임워크`)**
```md
[![전자정부표준프레임워크 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-ko.svg)](https://www.egovframe.go.kr)
```

**Insignias de versión multilingües (`es` Español · `vi` Vietnamita · `ar` Árabe · `fr` Francés)**
```md
[![Marco Estándar eGovFrame 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-es.svg)](https://www.egovframe.go.kr)
[![Khung chuẩn eGovFrame 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-vi.svg)](https://www.egovframe.go.kr)
[![إطار eGovFrame القياسي 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-ar.svg)](https://www.egovframe.go.kr)
[![Cadre standard eGovFrame 5.0.2](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/5.0.2/flat-fr.svg)](https://www.egovframe.go.kr)
```
*(Todas las insignias multilingües soportan tanto las rutas `badges/5.0.2/flat-<lang>.svg` como `badges/5.0.2/<lang>/flat.svg`.)*

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

Todas las versiones principales del [eGovFrame Runtime Guide](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:실행환경가이드) — de 1.0 a 5.x (52 versiones en total) — con cinco estilos cada una: `flat`, `flat-square`, `plastic`, `for-the-badge` y el estilo personalizado `outline` (el estilo `social` de shields.io se excluye porque depende de efectos hover).

| Estilo | Ejemplo (Inglés) | Ejemplo (Coreano) |
| --- | --- | --- |
| flat | ![flat](../badges/5.0.1/flat.svg) | ![flat (Coreano)](../badges/5.0.1/flat-ko.svg) |
| flat-square | ![flat-square](../badges/5.0.1/flat-square.svg) | ![flat-square (Coreano)](../badges/5.0.1/flat-square-ko.svg) |
| plastic | ![plastic](../badges/5.0.1/plastic.svg) | ![plastic (Coreano)](../badges/5.0.1/plastic-ko.svg) |
| for-the-badge | ![for-the-badge](../badges/5.0.1/for-the-badge.svg) | ![for-the-badge (Coreano)](../badges/5.0.1/for-the-badge-ko.svg) |
| outline | ![outline](../badges/5.0.1/outline.svg) | ![outline (Coreano)](../badges/5.0.1/outline-ko.svg) |

## Versiones soportadas

Todas las 52 versiones de la Guía de Tiempo de Ejecución eGovFrame:

- **5.x**: `5.0`, `5.0.0`, `5.0.1`, `5.0.2`, `5.0.3`, `5.0.4`, `5.0.5`, `5.0.6`
- **4.x**: `4.3`, `4.3.0`, `4.3.1`, `4.3.2`, `4.2`, `4.2.0`, `4.2.1`, `4.2.2`, `4.1`, `4.1.0`, `4.1.1`, `4.1.2`, `4.0`, `4.0.0`, `4.0.1`
- **3.x**: `3.10`, `3.10.0`, `3.10.1`, `3.10.2`, `3.9`, `3.9.0`, `3.8`, `3.8.0`, `3.7`, `3.7.0`, `3.6`, `3.6.0`, `3.5`, `3.5.0`, `3.5.1`, `3.1`, `3.1.0`, `3.0`, `3.0.0`
- **2.x**: `2.7`, `2.7.0`, `2.6`, `2.6.0`, `2.5`, `2.5.0`, `2.0`, `2.0.0`
- **1.x**: `1.0`, `1.0.0`

## Agregar versiones y generar insignias

Elige la versión que coincida con tu marco. Esta insignia **no** detecta automáticamente la versión de tu proyecto. Para agregar una nueva versión, edita `versions.json` y ejecuta el generador:

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

Logotipo extraído de la insignia README existente de eGovFramework. Los derechos del logotipo y el nombre eGovFrame pertenecen a sus respectivos propietarios.

## Licencia

El código (script de generación, tests, workflows) tiene [licencia MIT](../LICENSE). El recurso del logotipo (`assets/egovframe-mark.svg`) y los logotipos incrustados en las insignias generadas **no** están cubiertos por esta licencia y pertenecen a sus propietarios originales como se indica arriba.