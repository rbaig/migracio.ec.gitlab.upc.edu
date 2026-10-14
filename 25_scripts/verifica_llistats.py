#!/usr/bin/env python3
"""verifica_llistats.py — Els llistats `#lst-` i les remissions als blocs de codi
(13_contrib.qmd §Referències creuades, D-117 i D-121).

A un bloc de codi s'hi remet amb `@lst-…`, no per la posició, i només es numeren els llistats
`#lst-`: un div `::: {#lst-…}` amb el bloc a dins i el peu a l'última línia. L'script en
comprova el font, sobre els `.qmd` del llibre (tret de 13_contrib.qmd, que documenta la regla):

  L1  Un `#lst-` o un `lst-cap` a les claus d'un bloc de codi: la forma d'atribut, que dins
      d'un callout dona dos números al PDF. Cal la forma de div.                       (atura)
  L2  Un div `#lst-` sense bloc de codi, o sense peu.                                  (atura)
  L3  Un peu que no acaba en punt.                                                     (avisa)
  L4  Un `#lst-` dins d'un bloc `.content-visible when-format`: un format en tindria un
      més, i la numeració dels dos divergiria.                                         (atura)
  L5  Un `#lst-` sense cap remissió `@lst-`: només es numeren els blocs referenciats.  (atura)
  L6  Una remissió `@lst-` a un llistat que no existeix.                               (atura)
  L7  Una remissió per posició a un bloc de codi, al paràgraf de davant o al de darrere
      («el codi següent», «la funció C anterior», «aquest programa»).                  (avisa)

L7 és un avís perquè la decisió és de qui escriu: «la instrucció següent» pot ser prosa sobre
l'execució, i una presentació amb dos punts («es declara així:») no és una remissió. Una sèrie
d'apartats amb lletra (a), b)…) tampoc no porta `#lst-`.

Amb --sortida, després de `make render-complet`, compara la numeració dels llistats als dos
formats: cada `#lst-` del font ha de ser a l'HTML i al PDF, amb la mateixa posició dins del
capítol (el número de capítol de P, S i L és un altre al PDF: TODO.md), i el PDF no ha de
numerar cap bloc més.

Ús:
    python3 25_scripts/verifica_llistats.py              # el font; surt amb 1 si alguna troballa atura
    python3 25_scripts/verifica_llistats.py fitxer.qmd   # L1–L4 i L7 només d'aquests fitxers
    python3 25_scripts/verifica_llistats.py --sortida    # la numeració a _book/ i al PDF

El crida comprova.py (les comprovacions «Llistats» i «Llistats a la sortida»), i en vigilen el
comportament les autoproves (la bateria `llistats` de 25_scripts/autoproves.py).
"""

import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ARREL = Path(__file__).resolve().parent.parent
EXCLOSOS = {'13_contrib.qmd'}                       # documenta la regla, amb exemples
ATUREN = {'L1', 'L2', 'L4', 'L5', 'L6'}

CODI = re.compile(r'^\s*(?:(?:[-*+]|\d+[.)])\s+)?(`{3,}|~{3,})(.*)$')   # també «- ```», en una llista
DIV = re.compile(r'^(:{3,})\s*(.*)$')
LST_DIV = re.compile(r'^\{#(lst-[\w-]+)\}\s*$')
REMISSIO = re.compile(r'@(lst-[\w-]+)')

# L7: un nom que designa el bloc, uns quants mots que el modifiquen i la posició; un demostratiu;
# o «el següent:», «la següent:». Al paràgraf de davant del bloc compten totes les formes; al de
# darrere, només les que miren enrere: un «següent» de darrere apunta al que ve després (una llista,
# un altre bloc, que ja el compta el seu paràgraf de davant), no al bloc.
NOM = (r'(?:codi|programa|programes|fragments?|blocs?|funci(?:ó|ons)|subrutin(?:a|es)|sentènci(?:a|es)|'
       r'declaraci(?:ó|ons)|instrucci(?:ó|ons)|traducci(?:ó|ons)|versió|bucles?|patró|opció|vista|avís|'
       r'vectors?|matri(?:u|us)|variables)')
NOM = rf"(?:\b{NOM}|(?:(?<=\bel )|(?<=\bla ))`[^`\s]+`)"     # també un mot de codi: «el `for` anterior»
MODIFICADORS = r"(?:\s+[\w`'’()-]+){0,5}?"
ENRERE = re.compile(
    rf"{NOM}{MODIFICADORS}\s+anteriors?\b"
    r"|\baquest(?:a|s|es)?\s+(?:codi|programa|fragment|bloc|bucle|traducció|versió)\b", re.I)
POSICIO = re.compile(
    rf"{NOM}{MODIFICADORS}\s+següents?\b|{ENRERE.pattern}"
    r"|\b(?:al|el|la|els|les)\s+següents?\s*:", re.I)
# Una presentació adverbial no és una remissió (D-117): «es declaren de la manera següent:».
PRESENTACIO = re.compile(r"\b(?:manera|forma)\s+següents?\b", re.I)


@dataclass
class Troballa:
    fitxer: str
    linia: int
    regla: str
    text: str

    def __str__(self):
        return f'{self.fitxer}:{self.linia}: {self.regla} {self.text}'


def fitxers_llibre(arrel):
    """Els .qmd del llibre, sense els generats (`_book/`, `auto_*`), els ocults ni els exclosos."""
    return sorted(str(p.relative_to(arrel)) for p in arrel.rglob('*.qmd')
                  if not any(part.startswith(('_', '.', 'auto_')) for part in p.relative_to(arrel).parts[:-1])
                  and str(p.relative_to(arrel)) not in EXCLOSOS)


def analitza(text):
    """Els blocs de codi, els divs #lst- i les línies de fora del codi d'un .qmd.
    blocs: [{obre, tanca, claus, div}], amb `div` el div #lst- que el conté, si n'hi ha; llistats:
    [(id, obertura, tancament, dins de when-format, blocs de dins, peu)]; prosa: {línia: text} fora
    del codi."""
    linies = text.split('\n')
    blocs, llistats, prosa, pila = [], [], {}, []
    i = 0
    while i < len(linies):
        l = linies[i]
        m = CODI.match(l)
        if m:
            t = m.group(1)
            j = i + 1
            while j < len(linies) and not (linies[j].strip() and set(linies[j].strip()) == {t[0]}
                                           and len(linies[j].strip()) >= len(t)):
                j += 1
            div = pila[-1] if pila and LST_DIV.match(pila[-1]['claus']) else None
            blocs.append({'obre': i + 1, 'tanca': j + 1, 'claus': m.group(2).strip(), 'div': div})
            for d in pila:
                d['blocs'] += 1
            if pila:
                pila[-1]['ultima'] = None                       # el peu ha de ser l'últim element del div
            i = j + 1
            continue
        prosa[i + 1] = l
        d = DIV.match(l)
        if d and d.group(2).strip():                            # obertura: «::: {…}» o «::: classe»
            claus = d.group(2).strip()
            pila.append({'claus': claus, 'obre': i + 1, 'blocs': 0, 'ultima': None})
        elif d and pila:                                        # tancament
            div = pila.pop()
            div['tanca'] = i + 1
            if pila:
                pila[-1]['ultima'] = None
            m_lst = LST_DIV.match(div['claus'])
            if m_lst:
                when = any('when-format' in p['claus'] for p in pila)
                llistats.append((m_lst.group(1), div['obre'], i + 1, when, div['blocs'], div['ultima']))
        elif l.strip() and pila:
            pila[-1]['ultima'] = (i + 1, l.strip())
        i += 1
    return linies, blocs, llistats, prosa


def paragraf(linies, i, pas):
    """El paràgraf contigu a la línia i (base 0), enrere (pas=-1) o endavant (+1): [(línia, text)]."""
    j = i + pas
    while 0 <= j < len(linies) and not linies[j].strip():
        j += pas
    out = []
    while 0 <= j < len(linies) and linies[j].strip() and not CODI.match(linies[j]) and not DIV.match(linies[j]):
        out.append((j + 1, linies[j]))
        j += pas
    return out


def revisa_fitxer(arrel, rel):
    """L1–L4 i L7 d'un fitxer, i els ids i les remissions que hi ha (per a L5 i L6)."""
    linies, blocs, llistats, prosa = analitza((arrel / rel).read_text(encoding='utf-8'))
    t = []
    for b in blocs:
        if '#lst-' in b['claus'] or 'lst-cap' in b['claus']:
            t.append(Troballa(rel, b['obre'], 'L1', 'forma d\'atribut (#lst- o lst-cap a les claus del bloc): cal el div ::: {#lst-…}'))
        # D'un bloc dins d'un llistat, els paràgrafs de davant i de darrere del div.
        obre, tanca = (b['div']['obre'], b['div'].get('tanca', b['tanca'])) if b['div'] else (b['obre'], b['tanca'])
        candidates = ([(POSICIO, n, x) for n, x in paragraf(linies, obre - 1, -1)]
                      + [(ENRERE, n, x) for n, x in paragraf(linies, tanca - 1, +1)])
        vistes = set()
        for patro, n, x in candidates:
            m = patro.search(x)
            if (m and n not in vistes and not PRESENTACIO.search(m.group(0))
                    and not REMISSIO.search(x[max(0, m.start() - 40):m.end() + 40])):
                vistes.add(n)
                t.append(Troballa(rel, n, 'L7', f'remissió per posició a un bloc de codi, «{m.group(0)}»: cal @lst-'))
    for ident, obre, tanca, when, nblocs, ultima in llistats:
        if not nblocs:
            t.append(Troballa(rel, obre, 'L2', f'#{ident} sense bloc de codi'))
        if ultima is None:
            t.append(Troballa(rel, obre, 'L2', f'#{ident} sense peu: va a l\'última línia del div'))
        elif not ultima[1].endswith('.'):
            t.append(Troballa(rel, ultima[0], 'L3', f'el peu de #{ident} no acaba en punt'))
        if when:
            t.append(Troballa(rel, obre, 'L4', f'#{ident} dins d\'un bloc when-format: la numeració dels dos formats divergiria'))
    ids = {ident: (rel, obre) for ident, obre, *_ in llistats}
    remissions = {}
    for n, x in prosa.items():
        for m in REMISSIO.finditer(x):
            remissions.setdefault(m.group(1).rstrip('.'), (rel, n))
    return t, ids, remissions


def revisa(arrel=None, fitxers=None):
    """Totes les troballes del font. L5 i L6 són de tot el llibre; amb `fitxers`, L1–L4 i L7 només
    d'aquests."""
    arrel = arrel or ARREL
    tots = fitxers_llibre(arrel)
    troballes, ids, remissions = [], {}, {}
    for rel in tots:
        t, i, r = revisa_fitxer(arrel, rel)
        if fitxers is None or rel in fitxers:
            troballes += t
        ids.update(i)
        for k, v in r.items():
            remissions.setdefault(k, v)
    for ident, (rel, n) in sorted(ids.items()):
        if ident not in remissions:
            troballes.append(Troballa(rel, n, 'L5', f'#{ident} sense cap remissió @{ident}: només es numeren els blocs referenciats'))
    for ident, (rel, n) in sorted(remissions.items()):
        if ident not in ids:
            troballes.append(Troballa(rel, n, 'L6', f'@{ident}: no hi ha cap llistat #{ident}'))
    return troballes


# ---------------------------------------------------------------------------
# --sortida: la numeració a l'HTML i al PDF
# ---------------------------------------------------------------------------
def numeros_html(arrel):
    """{id: número} dels llistats de l'HTML."""
    out = {}
    for p in (arrel / '_book').rglob('*.html'):
        s = p.read_text(encoding='utf-8', errors='replace')
        for m in re.finditer(r'id="(lst-[\w-]+)"[^>]*>\s*<figure[^>]*>\s*<figcaption[^>]*>\s*Codi&nbsp;(\d+\.\d+)', s):
            out[m.group(1)] = m.group(2)
    return out


def numeros_pdf(tex, text_pdf):
    """{id: número} dels llistats del PDF: l'ordre dels \\label{lst-…} del .tex, que és el del
    comptador, aparellat amb els peus «Codi N.M:» del text del PDF. També els peus de més."""
    ordre = re.findall(r'\\label\{(lst-[\w-]+)\}', tex)
    peus = re.findall(r'^\s*Codi (\d+\.\d+):', text_pdf, re.M)
    return dict(zip(ordre, peus)), len(peus) - len(ordre)


def sortida(arrel=None, text_pdf=None):
    """Les diferències de numeració entre el font, l'HTML i el PDF. `text_pdf`: el text del PDF
    (pdftotext -layout); si no s'hi dona, es llegeix de _book/."""
    arrel = arrel or ARREL
    ids = set()
    for rel in fitxers_llibre(arrel):
        ids |= set(revisa_fitxer(arrel, rel)[1])
    tex = arrel / 'Estructura-de-computadors.tex'
    if text_pdf is None:
        pdf = arrel / '_book' / 'Estructura-de-computadors.pdf'
        if not pdf.exists() or not tex.exists() or shutil.which('pdftotext') is None:
            raise FileNotFoundError('cal _book/Estructura-de-computadors.pdf, Estructura-de-computadors.tex '
                                    '(make render-complet) i pdftotext')
        text_pdf = subprocess.run(['pdftotext', '-layout', str(pdf), '-'], capture_output=True, text=True).stdout
    html = numeros_html(arrel)
    pdf_n, sobrers = numeros_pdf(tex.read_text(encoding='utf-8', errors='replace'), text_pdf)
    r = []
    for ident in sorted(ids):
        h, p = html.get(ident), pdf_n.get(ident)
        if h is None or p is None:
            r.append(f'#{ident}: {"no és a l" + chr(39) + "HTML" if h is None else ""}'
                     f'{" i " if h is None and p is None else ""}{"no és al PDF" if p is None else ""}')
        elif h.split('.')[1] != p.split('.')[1]:
            r.append(f'#{ident}: «Codi {h}» a l\'HTML i «Codi {p}» al PDF: la posició dins del capítol no coincideix')
    if sobrers > 0:
        r.append(f'el PDF numera {sobrers} blocs més que els llistats #lst- (un bloc sense #lst- numerat, '
                 'o un llistat amb dos números: preamble.tex, 25_scripts/llistats.lua)')
    return r


def main(args):
    if '--sortida' in args:
        try:
            r = sortida()
        except FileNotFoundError as e:
            print(f'[llistats] omesa: {e}')
            return 0
        for x in r:
            print(f'[llistats] {x}')
        print(f'[llistats] sortida: {len(r)} diferències (13_contrib.qmd §Referències creuades, D-117)')
        return 1 if r else 0
    fitxers = [a for a in args if a.endswith('.qmd')] or None
    t = revisa(ARREL, fitxers)
    for x in t:
        print(f'[llistats] {x}')
    atura = [x for x in t if x.regla in ATUREN]
    print(f'[llistats] {len(t)} troballes, {len(atura)} que aturen (13_contrib.qmd §Referències creuades, D-117)')
    return 1 if atura else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
