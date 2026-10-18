"""Rebuild killhouse/index.html from the game source (the Claude artifact body).

usage: python3 tools/wrap_killhouse.py /path/to/shooter/index.html
"""
import sys, pathlib

HEAD = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,viewport-fit=cover">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="icon" type="image/png" href="icon-192.png">
<link rel="manifest" href="manifest.webmanifest">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Killhouse">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="theme-color" content="#0c0b0a">
</head><body>
"""

src = pathlib.Path(sys.argv[1]).read_text()
out = pathlib.Path(__file__).resolve().parent.parent / 'killhouse' / 'index.html'
out.write_text(HEAD + src + '\n</body></html>\n')
print('wrote', out)
