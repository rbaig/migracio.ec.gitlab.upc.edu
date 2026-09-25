#!/usr/bin/env python3
"""Revisió de la prosa dels .qmd: dobles espais i cometes rectes.

Aplica la regla de 13_contrib.qmd §Commits: «abans de fer commit, apliqueu
linting a la prosa dels fitxers .qmd modificats: elimineu dobles espais
(excepte als blocs de codi, fórmules LaTeX i cel·les de taula), i verifiqueu
que no hi ha cometes rectes "..." que haurien de ser guillemets «...»».

Salta el que no és prosa: la capçalera YAML, els blocs de codi, les
matemàtiques, les taules, les línies de div (`:::`), els comentaris HTML i,
dins de cada línia, el codi en línia, els atributs {…}, els shortcodes
{{< … >}}, les etiquetes HTML i les URL dels enllaços. Els dos espais a final
de línia (salt de línia forçat de Markdown) no compten.

Ús:
    python3 25_scripts/lint_prosa.py               # només les línies afegides respecte d'HEAD,
                                                   # més els .qmd nous encara no versionats
    python3 25_scripts/lint_prosa.py FITXER.qmd…   # fitxers sencers

Surt amb 1 si troba res i amb 0 si no. És el que crida el hook
`.claude/hooks/abans-commit.sh`, però es pot fer servir a mà.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

# Una tanca de codi pot obrir dins d'un element de llista (`- ```{.c}`).
FENCE_RE = re.compile(r'^\s*(?:(?:[-*+]|\d+[.)])\s+)?(`{3,}|~{3,})')
HUNK_RE = re.compile(r'^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@')

# Spans de dins d'una línia que no són prosa. L'ordre importa: primer el
# codi en línia, que pot contenir qualsevol dels altres.
SPANS = [
    re.compile(r'(`+).+?\1'),                      # codi en línia
    re.compile(r'(?<!\\)\$[^$]+?(?<!\\)\$'),       # matemàtiques en línia
    re.compile(r'\{\{<.*?>\}\}'),                  # shortcodes
    re.compile(r'\{[^{}]*\}'),                     # atributs {#id .classe clau="valor"}
    re.compile(r'<!--.*?-->'),                     # comentari HTML d'una línia
    re.compile(r'<[^<>]*>'),                       # etiquetes HTML
    re.compile(r'\]\([^)]*\)'),                    # URL d'enllaç
]
LIST_MARKER_RE = re.compile(r'^(?:>\s*)*(?:[-*+]|\d+[.)]|\(?[a-z]\))\s+')
DOUBLE_SPACE_RE = re.compile(r'\S {2,}(?=\S)')


def prose_lines(text):
    """Retorna {número de línia: text de prosa net} per a les línies de prosa."""
    lines = text.split('\n')
    result = {}
    fence = None          # (caràcter, llargada) del bloc de codi obert
    in_math = False
    in_comment = False
    start = 0
    if lines and lines[0].strip() == '---':
        for i in range(1, len(lines)):
            if lines[i].strip() in ('---', '...'):
                start = i + 1
                break
    for idx in range(start, len(lines)):
        raw = lines[idx]
        stripped = raw.strip()
        if fence:
            m = FENCE_RE.match(raw)
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= fence[1] \
                    and not raw[m.end():].strip():
                fence = None
            continue
        m = FENCE_RE.match(raw)
        if m:
            fence = (m.group(1)[0], len(m.group(1)))
            continue
        if in_comment:
            if '-->' in raw:
                in_comment = False
            continue
        if in_math:
            if '$$' in stripped:
                in_math = False
            continue
        if stripped.startswith('$$'):
            if stripped.count('$$') == 1:
                in_math = True
            continue
        if not stripped or stripped.startswith(('|', '+-', '+=', ':::')):
            continue
        line = re.sub(r'<!--.*?-->', '', raw)
        if '<!--' in line:
            in_comment = True
            line = line.split('<!--', 1)[0]
        line = line.rstrip()
        line = LIST_MARKER_RE.sub('', line.lstrip())
        for span in SPANS:
            line = span.sub('X', line)
        result[idx + 1] = line
    return result


def check(path, only_lines=None):
    text = Path(path).read_text(encoding='utf-8')
    findings = []
    for n, line in sorted(prose_lines(text).items()):
        if only_lines is not None and n not in only_lines:
            continue
        if DOUBLE_SPACE_RE.search(line):
            findings.append((path, n, 'doble espai'))
        if '"' in line:
            findings.append((path, n, 'cometa recta (cal «…»?)'))
    return findings


def git(*args):
    return subprocess.run(['git', *args], capture_output=True, text=True,
                          check=True).stdout


def added_lines():
    """{fitxer: línies afegides} respecte d'HEAD, més els .qmd no versionats."""
    targets = {}
    current = None
    for row in git('diff', 'HEAD', '-U0', '--no-color', '--diff-filter=AM',
                   '--', '*.qmd').splitlines():
        if row.startswith('+++ '):
            current = row[6:] if row.startswith('+++ b/') else None
            if current:
                targets.setdefault(current, set())
            continue
        m = HUNK_RE.match(row)
        if m and current:
            first, count = int(m.group(1)), int(m.group(2) or 1)
            targets[current].update(range(first, first + count))
    for path in git('ls-files', '--others', '--exclude-standard',
                    '--', '*.qmd').splitlines():
        targets[path] = None     # fitxer nou: totes les línies
    return targets


def main(argv):
    root = git('rev-parse', '--show-toplevel').strip()
    if argv:
        targets = {p: None for p in argv}
    else:
        os.chdir(root)
        targets = added_lines()
    findings = []
    for path, only in sorted(targets.items()):
        if only is not None and not only:
            continue
        findings.extend(check(path, only))
    for path, n, kind in findings:
        print(f'{path}:{n}: {kind}')
    return 1 if findings else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
