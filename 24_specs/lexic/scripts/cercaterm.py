"""Consulta el Cercaterm del TERMCAT (cerca avançada: denominació igual a, llengua anglès, àrea TIC o totes)
amb Playwright (la web té un repte Anubis). Escriu JSON per terme a cercaterm.json.
Ús: python3 cercaterm.py termes.txt   (un terme anglès per línia)"""
import re, html, sys, json, time, urllib.parse, os
from playwright.sync_api import sync_playwright
TIC = 'Tecnologies de la informació i la comunicació'
URL = 'https://www.termcat.cat/ca/cercaterm/%s?type=advanced&condition=match&language=' + (sys.argv[3] if len(sys.argv) > 3 else 'en') + '%s'
def net(s): return html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s))).strip()
def parse(t):
    fitxes = []
    parts = t.split('<div class="service-item__title"')[1:]
    for p in parts:
        nom = re.search(r'<span class="service-item__name">(.*?)</span>', p, re.S)
        area = re.search(r'service-item__tag--main">(.*?)</p>', p, re.S)
        terms = []
        for li in re.finditer(r'<li class="service-item__term">(.*?)</li>', p, re.S):
            lang = re.search(r'<span title="([^"]*)"><i>([^<]*)</i>', li.group(1))
            b = re.search(r'<b>(.*?)</b>', li.group(1), re.S)
            hier = [net(h) or net(tt) for tt, h in re.findall(r'service-item__term-hierarchy" title="([^"]*)">(.*?)</span>', li.group(1), re.S)]
            hier = [h for h in hier if h]
            if lang and b:
                terms.append((lang.group(2), net(b.group(1)).rstrip(','), ' '.join(hier)))
        tag = re.search(r'<p class="service-item__tag">(.*?)</p>', p, re.S)
        notes = net(' '.join(re.findall(r'service-item__notes-text">(.*?)</li>', p, re.S)))
        font = 'Neoloteca' if 'Neoloteca' in p else ''
        m = re.search(r"procedeix de (?:l'obra següent|la Neoloteca)[^:]*:\s*(.{0,140})", notes)
        fitxes.append(dict(nom=net(nom.group(1)) if nom else '', area=net(area.group(1)) if area else '',
                           tag=net(tag.group(1)) if tag else '', termes=terms, font=font,
                           obra=(m.group(1) if m else notes[:140])))
    return fitxes
def consulta(pg, terme, area):
    u = URL % (urllib.parse.quote(terme, safe=''), ('&thematic_area=' + urllib.parse.quote(TIC)) if area else '')
    pg.goto(u, wait_until='networkidle', timeout=90000)
    try: t = pg.content()
    except Exception: t = ''
    for _ in range(60):
        if 'Resultats per a la cerca' in t or 'No s\'han trobat' in t or 'no ha retornat' in t: break
        pg.wait_for_timeout(1000)
        try:
            pg.wait_for_load_state('networkidle', timeout=30000); t = pg.content()
        except Exception:
            t = ''
    ok = 'Resultats per a la cerca' in t
    pag = re.findall(r'href="\?[^"]*page=(\d+)', t)
    if pag: ok = ok and 'PAGINAT:%s' % max(pag)
    return ok, parse(t), u
if __name__ == '__main__':
    termes = [l.strip() for l in open(sys.argv[1], encoding='utf-8') if l.strip()]
    out = sys.argv[2] if len(sys.argv) > 2 else 'cercaterm.json'
    res = json.load(open(out)) if os.path.exists(out) else {}
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome', headless=True)
        pg = b.new_page()
        for t in termes:
            if t in res and res[t].get('ok'): continue
            try:
                ok, f, u = consulta(pg, t, True)
                ok2, f2, u2 = consulta(pg, t, False)
                r = dict(ok=ok, ok_totes=ok2, tic=f, url=u, totes=f2, url_totes=u2)
            except Exception as e:
                r = dict(ok=False, error=str(e)[:200])
            res[t] = r
            json.dump(res, open(out, 'w'), ensure_ascii=False, indent=1)
            print(t, r.get('ok'), len(r.get('tic', [])), len(r.get('totes', [])), flush=True)
        b.close()
