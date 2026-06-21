#!/usr/bin/env python3
"""
Patch index.html: make "The short version" eyebrow a clickable link to about.html.
Run from the repo root: python3 patch_about_link.py
"""

import sys

INDEX = "index.html"

OLD = '<span class="eyebrow rise">The short version</span>'
NEW = '<a class="eyebrow rise" href="about.html" style="text-decoration:none;cursor:pointer">The short version &rarr;</a>'

with open(INDEX, "r", encoding="utf-8") as f:
    src = f.read()

if OLD not in src:
    print("ERROR: target string not found — check index.html hasn't changed.")
    sys.exit(1)

patched = src.replace(OLD, NEW, 1)

with open(INDEX, "w", encoding="utf-8") as f:
    f.write(patched)

print("Done — 'The short version' eyebrow is now a link to about.html.")
