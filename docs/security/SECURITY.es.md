# Política de seguridad

[![English](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/en/outline.svg)](../../README.md)
[![한국어](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ko/outline.svg)](../README.ko.md)
[![Español](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/es/flat.svg)](../README.es.md)
[![Tiếng Việt](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/vi/outline.svg)](../README.vi.md)
[![العربية](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/ar/outline.svg)](../README.ar.md)
[![Français](https://raw.githubusercontent.com/leejongyoung/egovframe-badge/main/badges/lang/fr/outline.svg)](../README.fr.md)

## Notificación de vulnerabilidades

**Por favor, no abra un issue público para un problema de seguridad.**

Utilice la notificación privada de vulnerabilidades de GitHub:

➡ <https://github.com/leejongyoung/egovframe-badge/security/advisories/new>

Si la notificación privada de vulnerabilidades no está habilitada en el repositorio, notifique por correo electrónico en lugar de abrir un issue público.

Incluya:

- qué está afectado (versión del badge, script de generación o workflow)
- cómo reproducirlo y el impacto esperado
- cualquier cosa que ya haya hecho para verificarlo (hashes, URLs, logs)

Los informes se manejan en privado hasta que hay una solución disponible; se da crédito si se solicita.

## Alcance

En alcance:

- SVGs de badges en [`badges/`](../badges/): contenido generado, logo incrustado, metadatos de versión
- Automatización: [`.github/workflows/`](../.github/workflows/) y [`scripts/`](../scripts/). Los nuevos badges se generan con el workflow `generate-badges`; una forma de hacer que ese paso produzca salida incorrecta, filtre el token, o ejecute entrada no confiable cuenta como vulnerabilidad.

Fuera de alcance, notifique al propietario:

- El framework eGovFrame y su servidor de descarga → el proyecto eGovFrame, <https://www.egovframe.go.kr/> y [eGovFramework](https://github.com/eGovFramework).
- GitHub mismo → <https://github.com/github/github/security/policy>.
- shields.io → <https://github.com/badges/shields/security/policy>.

## Versiones soportadas

Solo lo que está en `badges/` en la rama por defecto se mantiene: todas las versiones listadas en `versions.json`. Badges eliminados cuando llegó un parche más nuevo de la misma serie no se mantienen.

## Verificar un badge usted mismo

Cada badge es un SVG autónomo con logo incrustado. Para regenerar y verificar una versión contra la fuente desde CI:

```bash
gh workflow run generate-badges.yml -R leejongyoung/egovframe-badge -f version=5.0.2
```