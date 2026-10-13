#!/usr/bin/env python3
"""Revisió de la prosa dels .qmd: dobles espais, cometes i formes que no s'han de fer servir.

Aplica dues regles de 13_contrib.qmd. La de §Commits: «elimineu dobles espais
(excepte als blocs de codi, fórmules LaTeX i cel·les de taula), i verifiqueu
que no hi ha cometes rectes "..." que haurien de ser guillemets «...»». I la
llista de formes que no s'han de fer servir, `[no_admeses]` de
24_specs/termes.toml (D-115), de la qual es genera la taula de §Anglicismes i
terminologia obligatòria → «Formes que no s'han de fer servir»: cada forma, també
en plural, en femení o conjugada, és una troballa. I els termes anglesos del
mateix fitxer fora de la cursiva (D-116): un de [termes], que s'escriu en
català, o un de [en_angles], que va sempre en cursiva; [angles_en_pla] en recull
les excepcions, amb el motiu (noms propis). comprova.py tracta les formes i els
termes anglesos com a error i la resta com a avís.

Salta el que no és prosa: la capçalera YAML, els blocs de codi, les
matemàtiques, les taules, les línies de div (`:::`), els comentaris HTML i,
dins de cada línia, el codi en línia, els atributs {…}, els shortcodes
{{< … >}}, les etiquetes HTML, les imatges, les citacions, les notes al peu,
les referències @ i les URL; dels enllaços i dels spans ([…]{…}) en deixa el
text. És l'única neteja de la prosa del projecte: prose_lines() la fan servir
també ortografia.py i gramatica.py, que només hi afegeixen el que és seu (D-105).
Els dos espais a final de línia (salt de línia forçat de Markdown) no compten.

Ús:
    python3 25_scripts/lint_prosa.py               # només les línies afegides respecte d'HEAD,
                                                   # més els .qmd nous encara no versionats
    python3 25_scripts/lint_prosa.py FITXER.qmd…   # fitxers sencers

Surt amb 1 si troba res i amb 0 si no. El fa servir 25_scripts/comprova.py
(13_contrib.qmd §Comprovacions per nivells), però es pot fer servir a mà.
"""

import os
import re
import subprocess
import sys
import tomllib
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
    re.compile(r'\]\([^)]*\)'),                    # el destí d'un enllaç que NETEJA no hagi llegit
]
LIST_MARKER_RE = re.compile(r'^(?:>\s*)*(?:[-*+]|\d+[.)]|\(?[a-z]\))\s+')
# El que s'ha de treure abans de SPANS, que en deixaria restes enganxades al text
# («[LaTeX](…)» → «[LaTeXX»). Els enllaços i els spans admeten un nivell de claudàtors o de
# parèntesis a dins.
IMG_RE = re.compile(r'!\[(?:[^\[\]]|\[[^\[\]]*\])*\]\((?:[^()]|\([^()]*\))*\)(?:\{[^{}]*\})?')
LINK_RE = re.compile(r'(?<!!)\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\((?:[^()]|\([^()]*\))*\)')
SPAN_RE = re.compile(r'\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\{[^{}]*\}')
CITA_RE = re.compile(r'\[-?@[^\[\]]*\]')
NOTA_RE = re.compile(r'\[\^[^\]]*\]:?')                # la crida i la definició d'una nota al peu
URL_RE = re.compile(r'https?://\S+')
REFERENCIA_RE = re.compile(r'(?<![\w.])-?@[A-Za-z][\w:.-]*\w')   # no una adreça de correu
DOUBLE_SPACE_RE = re.compile(r'\S {2,}(?=\S)')


def neteja(line):
    """Una línia sense el que no és prosa: les imatges, les citacions, les referències i les URL,
    canviades per X; les notes al peu, fora; i dels enllaços i els spans, només el text."""
    line = IMG_RE.sub('X', line)
    line = CITA_RE.sub('X', line)
    line = NOTA_RE.sub('', line)
    for _ in range(2):                                    # un enllaç dins d'un span
        line = SPAN_RE.sub(r'\1', line)
        line = LINK_RE.sub(r'\1', line)
    line = URL_RE.sub('X', line)
    return REFERENCIA_RE.sub('X', line)


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
        line = neteja(line)
        for span in SPANS:
            line = span.sub('X', line)
        result[idx + 1] = line
    return result


def patro_forma(terme):
    """L'expressió d'una forma de la taula, amb el plural, el femení o la conjugació."""
    mots = terme.split()
    if len(mots) > 1:                       # «ample de banda», «punt flotant»
        return r'\s+'.join(re.escape(m) + ('s?' if len(m) > 2 else '') for m in mots)
    m = mots[0]
    if m.endswith('ar'):                    # mapejar: mapeja, mapejos, mapejat…
        return re.escape(m[:-2]) + r'\w*'
    if m.endswith('at'):                    # aniuat: aniuats, aniuada, aniuades
        return re.escape(m[:-1]) + r'(?:t|ts|da|des)'
    return re.escape(m) + r'(?:s|os|es)?'


def formes_no_admeses(root):
    """[(expressió, forma, substitut)] de `[no_admeses]` de 24_specs/termes.toml."""
    dades = tomllib.loads((Path(root) / '24_specs' / 'termes.toml').read_text(encoding='utf-8'))
    formes = []
    for clau, entrada in dades.get('no_admeses', {}).items():
        for terme in re.split(r'\s*[,/]\s*', clau):
            if terme:
                rx = re.compile(r'(?<![\w·])(' + patro_forma(terme) + r')(?![\w·])', re.I)
                formes.append((rx, terme, entrada['si']))
    return formes


CURSIVA_RE = re.compile(r'(?<![\w*])(\*{1,3})(?!\s)[^*]+?(?<!\s)\1(?![\w*])|(?<!\w)_(?!\s)[^_]+?(?<!\s)_(?!\w)')


def termes_anglesos(root):
    """(expressió, {clau en minúscula: missatge}, [textos exclosos]) dels termes anglesos de
    24_specs/termes.toml (D-116): els de [termes] no es fan servir en pla, sinó en català, i els
    de [en_angles] van sempre en cursiva. [angles_en_pla] en recull les excepcions, amb el motiu."""
    dades = tomllib.loads((Path(root) / '24_specs' / 'termes.toml').read_text(encoding='utf-8'))
    missatges = {}
    for clau, e in dades.get('termes', {}).items():
        missatges[clau.lower()] = f'terme anglès en pla: s\'escriu «{e["ca"]}» (o *{clau}*, en cursiva, com a glossa)'
    for clau in dades.get('en_angles', {}):
        for part in clau.split(','):
            missatges[part.strip().lower()] = f'terme anglès sense cursiva: *{part.strip()}* (13_contrib.qmd §Anglicismes)'
    # Els més llargs primer: *working set* abans que *set*, *TLB hit* abans que *hit*.
    alternatives = '|'.join(re.escape(k) for k in sorted(missatges, key=len, reverse=True))
    # El plural anglès: -s, i -es només darrere de s, x, ch o sh («conflictes» és català).
    rx = re.compile(r'(?<![\w·-])(' + alternatives + r')(?:s|(?<=[sx])es|(?<=ch)es|(?<=sh)es)?(?![\w·-])', re.I)
    excepcions = list(dades.get('angles_en_pla', {}))
    return rx, missatges, excepcions


def check(path, only_lines=None, formes=None, angles=None):
    """Troballes d'un .qmd. formes, la llista de formes_no_admeses() (None: no les mira); angles,
    la de termes_anglesos() (None: no els mira)."""
    text = Path(path).read_text(encoding='utf-8')
    findings = []
    for n, line in sorted(prose_lines(text).items()):
        if only_lines is not None and n not in only_lines:
            continue
        for rx, terme, substitut in formes or []:
            for m in rx.finditer(line):
                findings.append((path, n, f'forma no admesa: «{m.group(1)}» (s\'escriu «{substitut}»)'))
        if angles:
            rx, missatges, excepcions = angles
            pla = CURSIVA_RE.sub(lambda m: 'X' * len(m.group(0)), line)
            for text_exclos in excepcions:
                pla = pla.replace(text_exclos, 'X' * len(text_exclos))
            for m in rx.finditer(pla):
                findings.append((path, n, f'«{m.group(0)}»: {missatges[m.group(1).lower()]}'))
        if DOUBLE_SPACE_RE.search(line):
            findings.append((path, n, 'doble espai'))
        if '"' in line:
            findings.append((path, n, 'cometa recta (cal «…»?)'))
        if '“' in line or '”' in line:
            findings.append((path, n, 'cometa tipogràfica (cal «…»?)'))
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
    formes = formes_no_admeses(root)
    angles = termes_anglesos(root)
    for path, only in sorted(targets.items()):
        if only is not None and not only:
            continue
        findings.extend(check(path, only, formes, angles))
    for path, n, kind in findings:
        print(f'{path}:{n}: {kind}')
    return 1 if findings else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
