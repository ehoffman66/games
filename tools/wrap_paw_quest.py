#!/usr/bin/env python3
"""Build paw-quest/index.html from the game source (the Claude artifact's paw-quest.html, which has no <html>/<head> wrapper).
Usage: python3 tools/wrap_paw_quest.py <paw-quest.html>"""
import sys, pathlib
src = pathlib.Path(sys.argv[1]).read_text()
head = '''<!doctype html>
<html lang="en">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="icon" type="image/png" href="icon-192.png">
<link rel="manifest" href="manifest.webmanifest">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Paw Quest">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="theme-color" content="#4fb0f2">
'''
out = pathlib.Path(__file__).resolve().parent.parent / 'paw-quest' / 'index.html'
out.write_text(head + src + '\n</html>\n')
print('wrote', out)
