#!/usr/bin/env python3
"""Extreu els fragments en cursiva de la prosa dels .qmd del llibre (fora de codi i matemàtiques).

Ús: python3 italiques.py ARREL > italiques.tsv   (fitxer \t línia \t fragment)
"""
import re
import sys
from pathlib import Path

ARREL = Path(sys.argv[1] if len(sys.argv)>1 and not sys.argv[1].startswith("-") else "/home/roger/gitlab/migracio")
FITXERS = (sorted((ARREL / '01_apunts').glob('*.qmd')) + sorted((ARREL / '02_problemes').glob('*.qmd'))
           + sorted((ARREL / '03_solucions').glob('*.qmd')) + sorted((ARREL / '04_laboratori').glob('*.qmd'))
           + [ARREL / 'index.qmd', ARREL / '11_riscv.qmd'] + sorted((ARREL / '21_riscv').glob('*.qmd')))
FENCE = re.compile(r'^\s*(`{3,}|~{3,})')
INLINE_CODE = re.compile(r'`[^`\n]*`')
MATH = re.compile(r'\$[^$\n]+\$')
LINK_URL = re.compile(r'\]\([^)]*\)')
ATTR = re.compile(r'\{[#.][^}]*\}')
ITAL = re.compile(r'(?<![\w*\\])\*(?![\s*])([^*\n]+?)(?<![\s\\])\*(?![\w*])')


def linies(path):
    text = path.read_text(encoding='utf-8').split('\n')
    start = 0
    if text and text[0].strip() == '---':
        for i in range(1, len(text)):
            if text[i].strip() in ('---', '...'):
                start = i + 1
                break
    fence = None
    in_math = in_comment = False
    for idx in range(start, len(text)):
        raw = text[idx]
        s = raw.strip()
        if fence:
            m = FENCE.match(raw)
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= fence[1] and not raw[m.end():].strip():
                fence = None
            continue
        m = FENCE.match(raw)
        if m:
            fence = (m.group(1)[0], len(m.group(1)))
            continue
        if in_comment:
            if '-->' in raw:
                in_comment = False
            continue
        if in_math:
            if '$$' in s:
                in_math = False
            continue
        if s.startswith('$$'):
            if s.count('$$') == 1:
                in_math = True
            continue
        line = re.sub(r'<!--.*?-->', '', raw)
        if '<!--' in line:
            in_comment = True
            line = line.split('<!--', 1)[0]
        yield idx + 1, line


def main():
  for f in FITXERS:
    for n, line in linies(f):
        l = INLINE_CODE.sub('X', line)
        l = MATH.sub('X', l)
        l = LINK_URL.sub(']', l)
        l = ATTR.sub('', l)
        l = l.replace('***', '*').replace('**', '')
        for m in ITAL.finditer(l):
            print(f'{f.relative_to(ARREL)}\t{n}\t{m.group(1).strip()}')


if __name__ == '__main__':
    main()
