# eGovFrame badge

[![English](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/en/flat.svg)](README.en.md)
[![한국어](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/ko/outline.svg)](README.ko.md)
[![Español](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/es/outline.svg)](README.es.md)
[![Tiếng Việt](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/vi/outline.svg)](README.vi.md)
[![العربية](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/ar/outline.svg)](README.ar.md)
[![Français](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/fr/outline.svg)](README.fr.md)

A **single SVG badge** for every project using the eGovFrame (electronic Government Framework). Instead of hard-coding logos in each repository, reference one centrally-maintained badge with a raw URL. Static SVG — no JavaScript, no deployment server, no long Base64 URLs.

## One-line usage

Pick the version, style, and language (`en`, `ko`, `es`, `vi`, `ar`, `fr`) from the URL path. The examples below link to the official portal.

**English (`eGovFrame`)**
```md
[![eGovFrame 5.0.2](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/5.0.2/flat.svg)](https://www.egovframe.go.kr)
```

**Korean (`전자정부표준프레임워크`)**
```md
[![전자정부표준프레임워크 5.0.2](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/5.0.2/flat-ko.svg)](https://www.egovframe.go.kr)
```

**Multilingual version badges (`es` Spanish · `vi` Vietnamese · `ar` Arabic · `fr` French)**
```md
[![Marco Estándar eGovFrame 5.0.2](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/5.0.2/flat-es.svg)](https://www.egovframe.go.kr)
[![Khung chuẩn eGovFrame 5.0.2](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/5.0.2/flat-vi.svg)](https://www.egovframe.go.kr)
[![إطار eGovFrame القياسي 5.0.2](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/5.0.2/flat-ar.svg)](https://www.egovframe.go.kr)
[![Cadre standard eGovFrame 5.0.2](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/5.0.2/flat-fr.svg)](https://www.egovframe.go.kr)
```
*(All multilingual badges support both `badges/5.0.2/flat-<lang>.svg` and `badges/5.0.2/<lang>/flat.svg` paths.)*

## Language selector badge buttons (`badges/lang/`)

Standalone badge buttons for multilingual `README` language switching (`en`, `ko`, `es`, `vi`, `ar`, `fr`, `mn`, `bg`, `ne`). The current language uses `flat.svg`; other languages use `outline.svg` (or all `flat.svg`).

```md
[![English](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/en/flat.svg)](README.md)
[![한국어](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/ko/outline.svg)](README.ko.md)
[![Español](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/es/outline.svg)](docs/README.es.md)
[![Tiếng Việt](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/vi/outline.svg)](docs/README.vi.md)
[![العربية](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/ar/outline.svg)](docs/README.ar.md)
[![Français](https://raw.githubusercontent.com/egovframework/egovframe-badge/main/badges/lang/fr/outline.svg)](docs/README.fr.md)
```

All major runtime versions from the [eGovFrame Runtime Guide](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:실행환경가이드) — 1.0 through 5.x (52 versions total) — with five styles each: `flat`, `flat-square`, `plastic`, `for-the-badge`, and the custom `outline` style (shields.io `social` style excluded as it relies on hover effects).

| Style | Example (English) | Example (Korean) |
| --- | --- | --- |
| flat | ![flat](../badges/5.0.1/flat.svg) | ![flat (Korean)](../badges/5.0.1/flat-ko.svg) |
| flat-square | ![flat-square](../badges/5.0.1/flat-square.svg) | ![flat-square (Korean)](../badges/5.0.1/flat-square-ko.svg) |
| plastic | ![plastic](../badges/5.0.1/plastic.svg) | ![plastic (Korean)](../badges/5.0.1/plastic-ko.svg) |
| for-the-badge | ![for-the-badge](../badges/5.0.1/for-the-badge.svg) | ![for-the-badge (Korean)](../badges/5.0.1/for-the-badge-ko.svg) |
| outline | ![outline](../badges/5.0.1/outline.svg) | ![outline (Korean)](../badges/5.0.1/outline-ko.svg) |

## Supported versions

All 52 versions from the eGovFrame Runtime Guide:

- **5.x**: `5.0`, `5.0.0`, `5.0.1`, `5.0.2`, `5.0.3`, `5.0.4`, `5.0.5`, `5.0.6`
- **4.x**: `4.3`, `4.3.0`, `4.3.1`, `4.3.2`, `4.2`, `4.2.0`, `4.2.1`, `4.2.2`, `4.1`, `4.1.0`, `4.1.1`, `4.1.2`, `4.0`, `4.0.0`, `4.0.1`
- **3.x**: `3.10`, `3.10.0`, `3.10.1`, `3.10.2`, `3.9`, `3.9.0`, `3.8`, `3.8.0`, `3.7`, `3.7.0`, `3.6`, `3.6.0`, `3.5`, `3.5.0`, `3.5.1`, `3.1`, `3.1.0`, `3.0`, `3.0.0`
- **2.x**: `2.7`, `2.7.0`, `2.6`, `2.6.0`, `2.5`, `2.5.0`, `2.0`, `2.0.0`
- **1.x**: `1.0`, `1.0.0`

## Adding versions and generating badges

Choose the version matching your framework. This badge does **not** auto-detect your project version. To add a new version, edit `versions.json` and run the generator:

```sh
python3 scripts/generate.py
python3 -m unittest discover -s tests -v
python3 scripts/generate.py --check
```

## Design

- SVGs are committed and served via GitHub raw URLs. README renderers load them directly; no deployment server required.
- Single logo source at `assets/egovframe-mark.svg`. All generated badges embed the logo — no external image dependencies.
- Version and style are fixed in the file path so existing README badges don't change unexpectedly when new releases arrive.
- `scripts/generate.py --check` and CI verify generated output matches source. Style changes apply consistently across all versions.
- `plastic` style uses the same gloss gradient stops as shields.io. `for-the-badge` uses sharp corners (`rx="0"`) like shields.io.

Logo extracted from the existing eGovFramework README badge. Logo and eGovFrame name rights belong to their respective owners.

## License

Code (generation script, tests, workflows) is [MIT licensed](../LICENSE). Logo asset (`assets/egovframe-mark.svg`) and logos embedded in generated badges are **not** covered by this license and belong to their original owners as noted above.

