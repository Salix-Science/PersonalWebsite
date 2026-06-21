#!/usr/bin/env python3
"""
Patch index.html: add a 'Full bio →' button after the sticky note in the about section.
Run from the repo root: python3 patch_bio_button.py
"""
import sys

INDEX = "index.html"

OLD = """          <aside class="sticky-note rise">
            <span class="lbl">For the record</span>
            These projects <i>will</i> get done. The problem is that I want to learn anything and everything. My professor worries I'll be a master of none, but I bet I can be a master of some if I keep the way I'm going.
          </aside>
        </div>
      </div>"""

NEW = """          <aside class="sticky-note rise">
            <span class="lbl">For the record</span>
            These projects <i>will</i> get done. The problem is that I want to learn anything and everything. My professor worries I'll be a master of none, but I bet I can be a master of some if I keep the way I'm going.
          </aside>
          <div class="rise">
            <a class="btn" href="about.html">Full bio &rarr;</a>
          </div>
        </div>
      </div>"""

with open(INDEX, "r", encoding="utf-8") as f:
    src = f.read()

if OLD not in src:
    print("ERROR: target string not found — check index.html hasn't changed.")
    sys.exit(1)

patched = src.replace(OLD, NEW, 1)

with open(INDEX, "w", encoding="utf-8") as f:
    f.write(patched)

print("Done — 'Full bio →' button added to the about section.")
