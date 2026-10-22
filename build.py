#!/usr/bin/env python3
"""Assemble index.html from src/app.html + src/data.js + src/fonts.css. Run after editing anything in src/."""
import pathlib
root = pathlib.Path(__file__).parent
app = (root/'src/app.html').read_text()
html = app.replace('/*FONTS*/', (root/'src/fonts.css').read_text()).replace('/*DATA*/', (root/'src/data.js').read_text())
(root/'index.html').write_text(html)
print('built index.html', len(html), 'bytes')
# vault copy (her rule: every page lives in the vault next to its subject, wrapped by a companion .md)
vault = pathlib.Path.home()/'Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian Vault/16 My Content Library/Singapore on Foot.html'
if vault.parent.exists():
    vault.write_text(html); print('copied to vault:', vault.name)
