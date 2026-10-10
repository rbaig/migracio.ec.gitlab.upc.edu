#!/usr/bin/env python3
"""Gramàtica de la prosa dels .qmd amb LanguageTool (català), sense el soroll del llibre.

Passa la prosa per LanguageTool 6.6 (`-l ca-ES`), una sola vegada per a tots
els fitxers, i en filtra el que al llibre no és error, segons
`24_specs/gramatica.toml`: les regles desactivades (`--disable`), les formes
correctes d'una regla que es manté activa (les excepcions) i les coincidències
que només toquen el marcador. L'ortografia no és aquí: la fa `ortografia.py`
amb hunspell i el diccionari del projecte.

La prosa és la de `lint_prosa.prose_lines`, l'única neteja del projecte: sense
la capçalera YAML, els blocs de codi, les matemàtiques, les taules, el codi en
línia, les imatges, les citacions, les notes al peu, les referències @ ni les
URL, i dels enllaços, només el text. Aquí s'hi afegeix el que és de
LanguageTool: el que no és català, substituït pel mateix marcador, «X» (les
cursives, que són els termes anglesos, i les sigles). Un paràgraf del font és
un paràgraf del text, perquè LanguageTool en vegi les frases senceres.

LanguageTool no es versiona, com RARS (D-62). Es busca, per ordre, a --lt, a
la variable d'entorn LANGUAGETOOL_DIR (una còpia que ja és al sistema) i al
directori `.cache/` del clon, que git ignora (`eines_externes.py`); si no hi
és, s'hi baixa el zip de languagetool.org (uns 250 MB, uns 400 un cop
descomprimit), se'n comprova el sha256 i es descomprimeix. Demana Java 17 o
posterior.

Ús:
    python3 25_scripts/gramatica.py                # els paràgrafs amb línies afegides respecte d'HEAD,
                                                   # i els .qmd nous encara no versionats
    python3 25_scripts/gramatica.py FITXER.qmd…    # fitxers sencers
    python3 25_scripts/gramatica.py --tot          # el corpus sencer, sense els fitxers que documenten
                                                   # casos (la guia), com make comprova-tot (make gramatica)
    python3 25_scripts/gramatica.py --resum …      # només el compte per regla
    python3 25_scripts/gramatica.py --instal·la    # només la baixada

Surt amb 1 si troba res, amb 0 si no, i amb 3 si no es pot fer (sense Java 17,
o sense LanguageTool i sense poder-lo baixar). Només fa servir la biblioteca
estàndard (Python ≥ 3.11).
"""

import argparse
import bisect
import collections
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
import urllib.request
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import eines_externes                                                # noqa: E402
import lint_prosa                                                    # noqa: E402

ARREL = Path(__file__).resolve().parent.parent
CONFIG = ARREL / '24_specs' / 'gramatica.toml'
VERSIO = '6.6'
LT_URL = f'https://languagetool.org/download/LanguageTool-{VERSIO}.zip'
# El de la baixada del 2026-10-10: languagetool.org no en publica cap.
LT_SHA256 = '53600506b399bb5ffe1e4c8dec794fd378212f14aaf38ccef9b6f89314d11631'
CACHE = eines_externes.directori()
JAR = 'languagetool-commandline.jar'
OMESA = 3

M = 'X'                                                              # el marcador, el mateix de lint_prosa
NEGRETA_CURSIVA = re.compile(r'\*\*\*(.+?)\*\*\*')
CURSIVA = re.compile(r'(?<![*\w])\*(?![*\s])(.+?)(?<![*\s])\*(?![*\w])')
CURSIVA_ = re.compile(r'(?<![\w_])_(?![_\s])(.+?)(?<![_\s])_(?![\w_])')
NEGRETA = re.compile(r'\*\*(.+?)\*\*')
MOT = re.compile(r'[A-Za-z0-9ÀÁÈÉÍÏÒÓÚÜÇàáèéíïòóúüç][\wÀ-ÿ-]*')
CAPCALERA = re.compile(r'^#{1,6}\s+')
ENTITATS = {'&nbsp;': ' ', '&lt;': '<', '&gt;': '>', '&amp;': '&', '&thinsp;': ' '}


# ---------------------------------------------------------------------------
# La prosa
# ---------------------------------------------------------------------------
def sigla(mot):
    """Dues majúscules o més (MC, KiB, RISC-V), o majúscula i xifra (RV32I, Ca2)."""
    majuscules = sum(c.isupper() for c in mot)
    return majuscules >= 2 or (majuscules >= 1 and any(c.isdigit() for c in mot))


def despres(t):
    """La prosa de lint_prosa, amb el que no és català substituït pel marcador."""
    t = CAPCALERA.sub('', t)
    t = re.sub(r'^:\s+', '', t)                                      # peu de taula
    t = re.sub(r'^>\s*', '', t)
    for entitat, text in ENTITATS.items():
        t = t.replace(entitat, text)
    t = NEGRETA_CURSIVA.sub(M, t)
    t = CURSIVA.sub(M, t)
    t = CURSIVA_.sub(M, t)
    t = NEGRETA.sub(r'\1', t).replace('**', '')
    t = re.sub(r'\\([*_$#\[\]`\\|<>~^-])', r'\1', t)
    t = MOT.sub(lambda m: M if sigla(m.group(0)) else m.group(0), t)
    return re.sub(r'\\$', '', t).strip()


def tanca_codi_partit(linies):
    """El codi en línia que comença en una línia i acaba en la següent (lint_prosa mira línia a
    línia i el deixa passar): del backtick desaparellat al final de la línia, i del principi de la
    següent fins al seu, és marcador."""
    obert = False
    resultat = []
    for n, t in linies:
        if obert and '`' in t:
            t = M + t.split('`', 1)[1]
            obert = False
        elif obert:
            t = M
        if t.count('`') % 2:
            t = t.rsplit('`', 1)[0] + M
            obert = True
        resultat.append((n, t))
    return resultat


def paragrafs(path):
    """[[(línia, text)]]: els paràgrafs de prosa d'un .qmd, una llista de línies cadascun."""
    crues = (ARREL / path).read_text(encoding='utf-8').split('\n')
    prosa = lint_prosa.prose_lines('\n'.join(crues))
    resultat, actual, anterior = [], [], None
    for n in sorted(prosa):
        cru = re.sub(r'^(?:>\s*)*', '', crues[n - 1].lstrip())
        nou = (anterior is None or n != anterior + 1 or CAPCALERA.match(cru)
               or lint_prosa.LIST_MARKER_RE.match(cru) or cru.startswith(': ')
               or CAPCALERA.match(crues[anterior - 1].lstrip()))
        anterior = n
        if nou and actual:
            resultat.append(actual)
            actual = []
        actual.append((n, prosa[n]))
    if actual:
        resultat.append(actual)
    return [[(n, despres(t)) for n, t in tanca_codi_partit(p)] for p in resultat]


def text_i_mapa(objectius):
    """El text de tots els objectius, un paràgraf per bloc, i el mapa [(inici, fitxer, línia)]."""
    trossos, mapa, pos = [], [], 0
    for path, only in sorted(objectius.items()):
        for p in paragrafs(path):
            if only is not None and not any(n in only for n, _ in p):
                continue
            p = [(n, t) for n, t in p if t and t != M]
            if not p:
                continue
            if trossos:
                trossos.append('\n\n')
                pos += 2
            for i, (n, t) in enumerate(p):
                if i:
                    trossos.append(' ')
                    pos += 1
                mapa.append((pos, path, n))
                trossos.append(t)
                pos += len(t)
    return ''.join(trossos) + '\n', mapa


# ---------------------------------------------------------------------------
# LanguageTool
# ---------------------------------------------------------------------------
def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for tros in iter(lambda: f.read(1 << 20), b''):
            h.update(tros)
    return h.hexdigest()


def comprova_java():
    """None si hi ha Java 17 o posterior; si no, el motiu."""
    if not shutil.which('java'):
        return 'falta Java (LanguageTool 6.6 demana Java 17 o posterior)'
    versio = subprocess.run(['java', '-version'], capture_output=True, text=True).stderr
    m = re.search(r'version "(?:1\.)?(\d+)', versio)
    if m and int(m.group(1)) < 17:
        return f'Java {m.group(1)} és anterior a la 17, que demana LanguageTool 6.6'
    return None


def installa():
    """El directori de LanguageTool al .cache/ del clon; si no hi és, el baixa i el descomprimeix."""
    desti = CACHE / f'LanguageTool-{VERSIO}'
    if (desti / JAR).is_file():
        return desti
    CACHE.mkdir(parents=True, exist_ok=True)
    zip_ = CACHE / f'LanguageTool-{VERSIO}.zip'                     # una baixada anterior, si n'hi ha
    if not (zip_.is_file() and sha256(zip_) == LT_SHA256):
        zip_ = CACHE / f'LanguageTool-{VERSIO}.zip.baixant'
        print(f'Baixant LanguageTool {VERSIO} a {CACHE} (uns 250 MB)…', file=sys.stderr)
        try:
            with urllib.request.urlopen(LT_URL, timeout=60) as resposta, open(zip_, 'wb') as f:
                shutil.copyfileobj(resposta, f)
        except OSError as e:
            zip_.unlink(missing_ok=True)
            raise SystemExit(f'[gramatica] omesa: no s\'ha pogut baixar LanguageTool ({e})') from None
        if sha256(zip_) != LT_SHA256:
            zip_.unlink()
            sys.exit(f'ERROR: el sha256 del LanguageTool baixat no és {LT_SHA256}')
    provisional = Path(tempfile.mkdtemp(prefix='.LanguageTool-', dir=CACHE))
    with zipfile.ZipFile(zip_) as z:                                 # extract() no surt del directori
        z.extractall(provisional)
    if desti.exists():                                              # una instal·lació a mitges, sense el .jar
        shutil.rmtree(desti)
    (provisional / f'LanguageTool-{VERSIO}').replace(desti)
    provisional.rmdir()
    if zip_.suffix == '.baixant':
        zip_.unlink()
    return desti


def troba_lt(explicit=None):
    """El directori de LanguageTool: --lt, LANGUAGETOOL_DIR o el .cache/ del clon (on el baixa)."""
    for candidat in (explicit, os.environ.get('LANGUAGETOOL_DIR')):
        if candidat:
            if (Path(candidat) / JAR).is_file():
                return Path(candidat)
            sys.exit(f'ERROR: no hi ha {JAR} a {candidat}')
    return installa()


def disponible():
    """None si es pot passar LanguageTool (Java 17 i LanguageTool, o la possibilitat de baixar-lo);
    si no, el motiu. No baixa res."""
    return comprova_java()


def configuracio():
    return tomllib.loads(CONFIG.read_text(encoding='utf-8'))


def languagetool(text, lt, desactivades):
    """Les coincidències de LanguageTool per al text sencer (una sola execució de Java)."""
    with tempfile.TemporaryDirectory() as tmp:
        fitxer = Path(tmp) / 'prosa.txt'
        fitxer.write_text(text, encoding='utf-8')
        ordre = ['java', '-Xmx2g', '-jar', str(lt / JAR), '-l', 'ca-ES', '--json', '-c', 'utf-8']
        if desactivades:
            ordre += ['--disable', ','.join(desactivades)]
        p = subprocess.run(ordre + [str(fitxer)], capture_output=True, text=True)
    inici = p.stdout.find('{')
    if p.returncode or inici < 0:
        sys.exit(f'ERROR: LanguageTool ha fallat ({p.returncode}):\n{p.stderr[-2000:]}')
    return json.loads(p.stdout[inici:])['matches']


def excepcio(cfg, regla, fitxer, frag, context):
    for e in cfg.get('excepcio', []):
        if e['regla'] != regla or (e.get('fitxer') and e['fitxer'] != fitxer):
            continue
        if e.get('textos') and frag not in e['textos']:
            continue
        contextos = e.get('context', [])
        if isinstance(contextos, str):
            contextos = [contextos]
        if contextos and not any(c in context for c in contextos):
            continue
        return True
    return False


def revisa(objectius, lt):
    """[(fitxer, línia, regla, missatge, text, suggeriments)] de LanguageTool, ja filtrades."""
    cfg = configuracio()
    desactivades = sorted(d['id'] for d in cfg.get('desactivada', []))
    descarta = re.compile(cfg['marcador']['descarta'])
    text, mapa = text_i_mapa(objectius)
    if not mapa:
        return []
    inicis = [m[0] for m in mapa]
    trobades = []
    for m in languagetool(text, lt, desactivades):
        regla = m['rule']['id']
        o, n = m['offset'], m['length']
        frag = text[o:o + n]
        if regla in desactivades or descarta.fullmatch(frag):
            continue
        _, fitxer, linia = mapa[bisect.bisect_right(inicis, o) - 1]
        context = text[max(0, o - 80):o + n + 80]
        if excepcio(cfg, regla, fitxer, frag, context):
            continue
        only = objectius.get(fitxer)
        if only is not None and linia not in only:
            continue
        trobades.append((fitxer, linia, regla, m['message'], frag,
                         [r['value'] for r in m.get('replacements', [])[:3]]))
    return trobades


def corpus():
    """Els .qmd versionats, sense els que documenten casos (la guia), com comprova.py --tot."""
    import comprova
    return {f: None for f in comprova.versionats()
            if f.endswith('.qmd') and 'documenta' not in comprova.classifica(f)[1]}


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.split('\n', 1)[0])
    ap.add_argument('fitxers', nargs='*')
    ap.add_argument('--tot', action='store_true')
    ap.add_argument('--resum', action='store_true')
    ap.add_argument('--instal·la', dest='installa', action='store_true')
    ap.add_argument('--lt', help='el directori de LanguageTool (per defecte, LANGUAGETOOL_DIR o el .cache/ del clon)')
    args = ap.parse_args(argv)
    motiu = comprova_java()
    if motiu:
        print(f'[gramatica] omesa: {motiu}', file=sys.stderr)
        return OMESA
    try:
        lt = troba_lt(args.lt)
    except SystemExit as e:
        if str(e).startswith('[gramatica] omesa'):
            print(e, file=sys.stderr)
            return OMESA
        raise
    if args.installa:
        print(lt)
        return 0
    if args.tot:
        objectius = corpus()
    elif args.fitxers:
        objectius = {os.path.relpath(Path(p).resolve(), ARREL): None for p in args.fitxers}
    else:
        os.chdir(ARREL)
        objectius = {f: ls for f, ls in lint_prosa.added_lines().items() if ls is None or ls}
    trobades = revisa(objectius, lt)
    if args.resum:
        for regla, n in collections.Counter(t[2] for t in trobades).most_common():
            print(f'{n:5d} {regla}')
    else:
        for fitxer, linia, regla, missatge, frag, sugg in trobades:
            print(f'{fitxer}:{linia}: {regla}: {missatge} «{frag}»' + (f' → {", ".join(sugg)}' if sugg else ''))
    return 1 if trobades else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
