#!/usr/bin/env python3
"""Generate self-contained eGovFrame SVG badges from the shared logo."""

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
STYLES = ("flat", "flat-square", "for-the-badge", "outline")
VERSION_PATTERN = re.compile(r"[0-9]+(?:\.[0-9]+){1,3}(?:-[A-Za-z0-9.]+)?\Z")
SVG_NS = "{http://www.w3.org/2000/svg}"


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


def render(version, style, paths):
    if style not in STYLES or not VERSION_PATTERN.fullmatch(version):
        raise ValueError("unsupported badge style or version")

    prominent = style == "for-the-badge"
    outlined = style == "outline"
    height = 28 if prominent else 22 if outlined else 20
    label_width = 124 if prominent else 111
    message_width = max(48, (9 if prominent else 8) * len(version) + 18)
    width = label_width + message_width
    radius = 0 if style == "flat-square" else 4
    label_color = "#003764" if prominent else "#ffffff"
    message_color = "#e4032e" if prominent else "#ffffff" if outlined else "#134f8c"
    text_color = "#ffffff" if prominent else "#003764"
    version_color = "#134f8c" if outlined else "#ffffff"
    icon_size = 20 if prominent else 16
    icon_x = 6
    icon_y = (height - icon_size) / 2
    icon_scale = icon_size / 173.282
    label_text = "EGOVFRAME" if prominent else "eGovFrame"
    font_size = 11 if prominent else 12
    baseline = height / 2 + (3.7 if prominent else 4)
    # Every badge contains the complete logo; README renderers need no data URI or script.
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="eGovFrame {escape(version, quote=True)}">
<title>eGovFrame {escape(version)} ({style})</title>
<defs><clipPath id="badge-shape"><rect width="{width}" height="{height}" rx="{radius}"/></clipPath></defs>
<g clip-path="url(#badge-shape)">
<rect width="{width}" height="{height}" rx="{radius}" fill="{label_color}"/>
<path d="M{label_width} 0h{message_width}v{height}h-{message_width}z" fill="{message_color}"/>
</g>
<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="{radius}" fill="none" stroke="{'#134f8c' if outlined else '#d0d7de' if not prominent else '#003764'}"/>
<g transform="translate({icon_x} {icon_y:g}) scale({icon_scale:.8f})">{paths}</g>
<text x="{icon_x + icon_size + 7}" y="{baseline:g}" fill="{text_color}" font-family="Arial, Helvetica, sans-serif" font-size="{font_size}" font-weight="600">{label_text}</text>
<text x="{label_width + message_width / 2:g}" y="{baseline:g}" fill="{version_color}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="{font_size}" font-weight="700">{escape(version)}</text>
</svg>
'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify committed badges match generated output")
    args = parser.parse_args()
    versions = load_versions()
    paths = logo_paths()
    expected = {
        OUTPUT / version / f"{style}.svg": render(version, style, paths)
        for version in versions for style in STYLES
    }
    existing = set(OUTPUT.glob("*/*.svg"))

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
    for path, content in expected.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"Generated {len(expected)} badges")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
