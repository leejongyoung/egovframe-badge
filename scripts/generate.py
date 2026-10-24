#!/usr/bin/env python3
"""Generate self-contained eGovFrame version badges and language-selector badge buttons."""

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSIONS = ROOT / "versions.json"
LOGO = ROOT / "assets" / "egovframe-mark.svg"
OUTPUT = ROOT / "badges"
STYLES = ("flat", "flat-square", "plastic", "for-the-badge", "outline")
LANGUAGES = ("en", "ko", "es", "vi", "ar", "fr")
VERSION_PATTERN = re.compile(r"[0-9]+(?:\.[0-9]+){1,3}(?:-[A-Za-z0-9.]+)?\Z")
SVG_NS = "{http://www.w3.org/2000/svg}"

# Version-badge label metadata per language: (normal_label, prominent_label, normal_width, prominent_width, font_family)
VERSION_LABELS = {
    "en": (
        "eGovFrame",
        "EGOVFRAME",
        111,
        124,
        "Arial, Helvetica, sans-serif",
    ),
    "ko": (
        "전자정부표준프레임워크",
        "전자정부표준프레임워크",
        162,
        168,
        "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans KR', 'Malgun Gothic', Arial, sans-serif",
    ),
    "es": (
        "Marco Estándar eGovFrame",
        "MARCO ESTÁNDAR EGOVFRAME",
        178,
        196,
        "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Arial, sans-serif",
    ),
    "vi": (
        "Khung chuẩn eGovFrame",
        "KHUNG CHUẨN EGOVFRAME",
        166,
        182,
        "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Arial, sans-serif",
    ),
    "ar": (
        "إطار eGovFrame القياسي",
        "إطار EGOVFRAME القياسي",
        162,
        174,
        "'Noto Sans Arabic', -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif",
    ),
    "fr": (
        "Cadre standard eGovFrame",
        "CADRE STANDARD EGOVFRAME",
        178,
        196,
        "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Arial, sans-serif",
    ),
}

# Standalone language-selector badge buttons: code -> (code_label, native_name, name_width, prominent_name_width, font_family)
LANGUAGE_BUTTONS = {
    "en": ("EN", "English", 58, 68, "Arial, Helvetica, sans-serif"),
    "ko": ("KO", "한국어", 52, 60, "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans KR', 'Malgun Gothic', Arial, sans-serif"),
    "es": ("ES", "Español", 60, 70, "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Arial, sans-serif"),
    "vi": ("VI", "Tiếng Việt", 72, 82, "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Arial, sans-serif"),
    "ar": ("AR", "العربية", 56, 64, "'Noto Sans Arabic', -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"),
    "fr": ("FR", "Français", 64, 74, "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Arial, sans-serif"),
    "mn": ("MN", "Монгол", 62, 72, "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Arial, sans-serif"),
    "bg": ("BG", "Български", 76, 86, "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Arial, sans-serif"),
    "ne": ("NE", "नेपाली", 54, 62, "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans Devanagari', Arial, sans-serif"),
}


def load_versions():
    versions = json.loads(VERSIONS.read_text(encoding="utf-8"))
    if not isinstance(versions, list) or not versions or len(versions) != len(set(versions)):
        raise ValueError("versions.json must contain a nonempty list of unique versions")
    for version in versions:
        if not isinstance(version, str) or not VERSION_PATTERN.fullmatch(version):
            raise ValueError(f"invalid version: {version!r}")
    return versions


def logo_paths():
    root = ET.parse(LOGO).getroot()
    paths = root.findall(f"{SVG_NS}path")
    if root.get("viewBox") != "0 0 173.282 173.282" or len(paths) != 3:
        raise ValueError("unexpected eGovFrame logo structure")
    return "".join(
        f'<path fill="{escape(path.attrib["fill"], quote=True)}" '
        f'd="{escape(path.attrib["d"], quote=True)}"/>'
        for path in paths
    )


def _gloss_markup(width, height, radius, glossy):
    if not glossy:
        return ""
    return (
        f'<defs><linearGradient id="gloss" x2="0" y2="100%">'
        f'<stop offset="0" stop-color="#fff" stop-opacity=".7"/>'
        f'<stop offset=".1" stop-color="#aaa" stop-opacity=".1"/>'
        f'<stop offset=".9" stop-color="#000" stop-opacity=".3"/>'
        f'<stop offset="1" stop-color="#000" stop-opacity=".5"/>'
        f'</linearGradient></defs>\n'
        f'<rect width="{width}" height="{height}" rx="{radius}" fill="url(#gloss)"/>\n'
    )


def render(version, style, paths, lang="en"):
    if style not in STYLES or not VERSION_PATTERN.fullmatch(version):
        raise ValueError("unsupported badge style or version")
    if lang not in VERSION_LABELS:
        raise ValueError(f"unsupported language: {lang!r}")

    prominent = style == "for-the-badge"
    outlined = style == "outline"
    glossy = style == "plastic"
    squared = style in ("flat-square", "for-the-badge")

    normal_label, prominent_label, normal_w, prominent_w, font_family = VERSION_LABELS[lang]
    height = 28 if prominent else 22 if outlined else 20
    label_text = prominent_label if prominent else normal_label
    label_width = prominent_w if prominent else normal_w
    message_width = max(48, (9 if prominent else 8) * len(version) + 18)
    width = label_width + message_width
    radius = 0 if squared else 4
    label_color = "#003764" if prominent else "#ffffff"
    message_color = "#e4032e" if prominent else "#ffffff" if outlined else "#134f8c"
    text_color = "#ffffff" if prominent else "#003764"
    version_color = "#134f8c" if outlined else "#ffffff"
    icon_size = 20 if prominent else 16
    icon_x = 6
    icon_y = (height - icon_size) / 2
    icon_scale = icon_size / 173.282
    label_font_size = 11 if (prominent or lang != "en") else 12
    version_font_size = 11 if prominent else 12
    baseline = height / 2 + (3.7 if prominent else 4)

    aria_label = f"{escape(normal_label, quote=True)} {escape(version, quote=True)}"
    title_text = f"{escape(normal_label)} {escape(version)} ({style})"
    gloss = _gloss_markup(width, height, radius, glossy)
    stroke = "#134f8c" if outlined else "#d0d7de" if not prominent else "#003764"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{aria_label}">
<title>{title_text}</title>
<defs><clipPath id="badge-shape"><rect width="{width}" height="{height}" rx="{radius}"/></clipPath></defs>
<g clip-path="url(#badge-shape)">
<rect width="{width}" height="{height}" rx="{radius}" fill="{label_color}"/>
<path d="M{label_width} 0h{message_width}v{height}h-{message_width}z" fill="{message_color}"/>
{gloss}</g>
<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="{radius}" fill="none" stroke="{stroke}"/>
<g transform="translate({icon_x} {icon_y:g}) scale({icon_scale:.8f})">{paths}</g>
<text x="{icon_x + icon_size + 7}" y="{baseline:g}" fill="{text_color}" font-family="{font_family}" font-size="{label_font_size}" font-weight="600">{escape(label_text)}</text>
<text x="{label_width + message_width / 2:g}" y="{baseline:g}" fill="{version_color}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="{version_font_size}" font-weight="700">{escape(version)}</text>
</svg>
'''


def render_language_button(lang, style):
    if style not in STYLES:
        raise ValueError(f"unsupported badge style: {style!r}")
    if lang not in LANGUAGE_BUTTONS:
        raise ValueError(f"unsupported language button: {lang!r}")

    prominent = style == "for-the-badge"
    outlined = style == "outline"
    glossy = style == "plastic"
    squared = style in ("flat-square", "for-the-badge")

    code_label, native_name, normal_w, prominent_w, font_family = LANGUAGE_BUTTONS[lang]
    height = 28 if prominent else 22 if outlined else 20
    label_width = 46 if prominent else 40
    message_width = prominent_w if prominent else normal_w
    width = label_width + message_width
    radius = 0 if squared else 4
    label_color = "#003764" if prominent else "#ffffff"
    message_color = "#e4032e" if prominent else "#ffffff" if outlined else "#134f8c"
    text_color = "#ffffff" if prominent else "#003764"
    name_color = "#134f8c" if outlined else "#ffffff"
    stroke = "#134f8c" if outlined else "#d0d7de" if not prominent else "#003764"
    baseline = height / 2 + (3.7 if prominent else 4)
    code_font_size = 10 if prominent else 10
    name_font_size = 11 if prominent else 11
    gloss = _gloss_markup(width, height, radius, glossy)

    # Compact globe icon on the left side of the language selector badge
    r_globe = 6 if prominent else 5.5
    cx = 11 if prominent else 10
    cy = height / 2
    globe_svg = (
        f'<g fill="none" stroke="{text_color}" stroke-width="1.2">'
        f'<circle cx="{cx:g}" cy="{cy:g}" r="{r_globe:g}"/>'
        f'<ellipse cx="{cx:g}" cy="{cy:g}" rx="{r_globe * 0.48:.2f}" ry="{r_globe:g}"/>'
        f'<line x1="{cx - r_globe:g}" y1="{cy:g}" x2="{cx + r_globe:g}" y2="{cy:g}"/>'
        f'</g>'
    )
    aria_label = f"Language: {escape(native_name, quote=True)} ({code_label})"
    title_text = f"{escape(native_name)} ({code_label}, {style})"
    divider = f'<line x1="{label_width}" y1="1" x2="{label_width}" y2="{height - 1}" stroke="#134f8c" stroke-opacity="0.35"/>\n' if outlined else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{aria_label}">
<title>{title_text}</title>
<defs><clipPath id="badge-shape"><rect width="{width}" height="{height}" rx="{radius}"/></clipPath></defs>
<g clip-path="url(#badge-shape)">
<rect width="{width}" height="{height}" rx="{radius}" fill="{label_color}"/>
<path d="M{label_width} 0h{message_width}v{height}h-{message_width}z" fill="{message_color}"/>
{gloss}</g>
<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="{radius}" fill="none" stroke="{stroke}"/>
{divider}{globe_svg}
<text x="{cx + r_globe + 4:g}" y="{baseline:g}" fill="{text_color}" font-family="Arial, Helvetica, sans-serif" font-size="{code_font_size}" font-weight="700">{code_label}</text>
<text x="{label_width + message_width / 2:g}" y="{baseline:g}" fill="{name_color}" text-anchor="middle" font-family="{font_family}" font-size="{name_font_size}" font-weight="600">{escape(native_name)}</text>
</svg>
'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify committed badges match generated output")
    args = parser.parse_args()
    versions = load_versions()
    paths = logo_paths()

    expected = {}
    for version in versions:
        for style in STYLES:
            for lang in LANGUAGES:
                svg = render(version, style, paths, lang=lang)
                if lang == "en":
                    expected[OUTPUT / version / f"{style}.svg"] = svg
                else:
                    expected[OUTPUT / version / f"{style}-{lang}.svg"] = svg
                    expected[OUTPUT / version / lang / f"{style}.svg"] = svg

    for lang in LANGUAGE_BUTTONS:
        for style in STYLES:
            btn_svg = render_language_button(lang, style)
            expected[OUTPUT / "lang" / lang / f"{style}.svg"] = btn_svg
            expected[OUTPUT / "lang" / f"{style}-{lang}.svg"] = btn_svg

    existing = set(OUTPUT.glob("**/*.svg"))

    if args.check:
        mismatches = [p for p, content in expected.items() if not p.exists() or p.read_text(encoding="utf-8") != content]
        extras = existing - expected.keys()
        if mismatches or extras:
            for p in sorted([*mismatches, *extras]):
                print(f"out of date: {p.relative_to(ROOT)}", file=sys.stderr)
            return 1
        print(f"Verified {len(expected)} badges")
        return 0

    for path in existing - expected.keys():
        path.unlink()
        curr = path.parent
        while curr != OUTPUT and curr != ROOT:
            try:
                curr.rmdir()
            except OSError:
                break
            curr = curr.parent

    for path, content in expected.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"Generated {len(expected)} badges")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
