# Guía de contribución a eGovFrame Badge

[![English](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/en/outline.svg)](../../README.md)
[![한국어](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ko/outline.svg)](../README.ko.md)
[![Español](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/es/flat.svg)](../README.es.md)
[![Tiếng Việt](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/vi/outline.svg)](../README.vi.md)
[![العربية](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ar/outline.svg)](../README.ar.md)
[![Français](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/fr/outline.svg)](../README.fr.md)

## Antes de abrir un pull request

```bash
python3 -m pip install -r requirements.txt
python3 -m unittest discover -s tests -v   # pruebas de los scripts
```

El CI ejecuta las pruebas y verifica la consistencia de la generación de badges.

- Los mensajes de commit siguen el estilo existente: `feat(badges): add 5.1.0 badges`, `fix(generate): ...`, `docs(readme): ...`, `ci: ...`.
- No edites los archivos SVG generados directamente. Las nuevas versiones provienen de `scripts/generate.py` (el workflow `generate-badges`); para volver a comprobar badges existentes ejecuta `python3 scripts/generate.py --check`.
- Un conjunto de badges por versión: al agregar `5.1.0` se generan los 5 estilos × 6 idiomas.

## GitHub Actions y facturación

- **Gratis en repositorios públicos:** según la política de facturación de GitHub, los runners estándar alojados por GitHub (`ubuntu-latest`) son **gratuitos y sin límite de minutos en repositorios públicos**. Los badges se generan durante `generate-badges.yml` y se confirman; no se consumen artefactos de Actions ni almacenamiento de Release.

## Seguridad

No notifiques vulnerabilidades en issues; sigue el proceso en [SECURITY.md](../security/SECURITY.md).