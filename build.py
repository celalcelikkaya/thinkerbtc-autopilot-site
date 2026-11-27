"""Build index.html from src/index.src.html and the files in assets/.

The page is one self-contained HTML file: the logo and coin icons are inlined as data URIs,
so it opens anywhere (a browser, GitHub Pages) with no other files.

Placeholders in the source:
  {{LOGO}}        -> assets/logo.png
  {{COIN:BTC}}    -> assets/coins/BTC.svg (any coin file name)
  {{COINS}}       -> a JSON object of every coin in assets/coins
  {{IMG:path}}    -> any image under assets/, e.g. {{IMG:phones/plans.webp}}
  {{FONT:path}}   -> a font under assets/, e.g. {{FONT:fonts/Anton-Regular.woff2}}

Usage:  python build.py
"""
import base64
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "src" / "index.src.html"
OUT = ROOT / "index.html"


MIME = {".png": "image/png", ".svg": "image/svg+xml", ".webp": "image/webp", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".woff2": "font/woff2"}


def data_uri(path: pathlib.Path) -> str:
    mime = MIME.get(path.suffix.lower(), "application/octet-stream")
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def main() -> int:
    html = SRC.read_text(encoding="utf-8")
    coins = {p.stem: data_uri(p) for p in sorted((ROOT / "assets" / "coins").glob("*.svg"))}

    html = html.replace("{{LOGO}}", data_uri(ROOT / "assets" / "logo.png"))
    html = html.replace("{{COINS}}", json.dumps(coins))

    def coin(m: re.Match) -> str:
        name = m.group(1)
        if name not in coins:
            sys.exit(f"Unknown coin {name}: add assets/coins/{name}.svg")
        return coins[name]

    html = re.sub(r"\{\{COIN:(\w+)\}\}", coin, html)

    def image(m: re.Match) -> str:
        path = (ROOT / "assets" / m.group(1)).resolve()
        if not path.is_file() or (ROOT / "assets") not in path.parents:
            sys.exit(f"Unknown image {m.group(1)}: add it under assets/")
        return data_uri(path)

    html = re.sub(r"\{\{(?:IMG|FONT):([\w./-]+)\}\}", image, html)
    left = re.findall(r"\{\{[^}]+\}\}", html)
    if left:
        sys.exit(f"Unreplaced placeholders: {sorted(set(left))}")

    head = (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        "<style>:root{padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}"
        "body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style></head><body>"
    )
    OUT.write_text(head + html + "</body></html>", encoding="utf-8", newline="")
    print(f"Built {OUT.name} ({OUT.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
