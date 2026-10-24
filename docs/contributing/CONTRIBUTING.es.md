# Guía de contribución a eGovFrame Badge

[![English](../../badges/lang/en/outline.svg)](CONTRIBUTING.en.md)
[![한국어](../../badges/lang/ko/outline.svg)](CONTRIBUTING.ko.md)
[![Español](../../badges/lang/es/flat.svg)](CONTRIBUTING.es.md)
[![Tiếng Việt](../../badges/lang/vi/outline.svg)](CONTRIBUTING.vi.md)
[![العربية](../../badges/lang/ar/outline.svg)](CONTRIBUTING.ar.md)
[![Français](../../badges/lang/fr/outline.svg)](CONTRIBUTING.fr.md)

## Antes de abrir un pull request

```bash
python3 -m pip install PyYAML==6.0.3
python3 -m unittest discover -s tests -v   # pruebas de los scripts
```

El CI ejecuta las pruebas y verifica la consistencia de la generación de badges.

- Los mensajes de commit siguen el estilo existente: `feat(badges): add 5.1.0 badges`, `fix(generate): ...`, `docs(readme): ...`, `ci: ...`.
- No edites los archivos SVG generados directamente. Las nuevas versiones provienen de `scripts/generate.py` (el workflow `generate-badges`); para volver a comprobar badges existentes ejecuta `python3 scripts/generate.py --check`.
- Un conjunto de badges por versión: al agregar `5.1.0` se generan los 5 estilos × 6 idiomas.
- Los puntos de entrada de la documentación se generan: edita las fuentes de `docs/` y ejecuta `python3 scripts/sync_readme.py` para actualizar `README.md` y los puntos de entrada de `.github/`. Los botones de idioma deben apuntar a las fuentes localizadas en `docs/`, incluido el inglés.

## GitHub Actions y facturación

- **Gratis en repositorios públicos:** según la política de facturación de GitHub, los runners estándar alojados por GitHub (`ubuntu-latest`) son **gratuitos y sin límite de minutos en repositorios públicos**. Los badges se generan durante `generate-badges.yml` y se confirman; no se consumen artefactos de Actions ni almacenamiento de Release.

## Seguridad

No notifiques vulnerabilidades en issues; sigue el proceso en [SECURITY.es.md](../security/SECURITY.es.md).