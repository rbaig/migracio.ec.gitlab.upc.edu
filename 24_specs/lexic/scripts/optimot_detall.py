"""Per a cada terme d'optimot.json, baixa la fitxa (detall) de cada resultat del TERMCAT de l'àrea TIC
(i de les fonts que no són del TERMCAT) i n'extreu l'àrea i les denominacions ca/en. Escriu optimot_detall.json."""
import json, os, re, html, sys, urllib.parse, time
sys.path.insert(0, '/home/roger/.claude-vocdoni/jobs/f97379a0/tmp')
from optimot import get
U = ('https://aplicacions.llengua.gencat.cat/llc/AppJava/index.html?action=Principal&method=detall&input_cercar=%s'
     '&numPagina=1&database=%s&idFont=%s&idHit=%s&tipusFont=%s&numeroResultat=1&clickLink=detall&tipusCerca=cerca.queSignifica')
TIC = 'Tecnologies de la informació i la comunicació'
def parse(t, idf):
    # el bloc TransformLaTeX que segueix l'enllaç detall_completa d'aquesta fitxa
    i = t.find('method=detall_completa')
    m = re.search(r'TransformLaTeX\("(.*?)",\d+\);', t[i:], re.S) if i >= 0 else None
    if not m: return None
    s = m.group(1).replace('\\"', '"')
    area = re.search(r'Àrea tem(?:à|&agrave;)tica</b><br/>(.*?)<br/>', html.unescape(s))
    terms = []
    for mm in re.finditer(r'<span style="font-style: italic">(\w\w)<span style="font-style: normal"> - </span><span style="font-style: normal">(.*?)</span><span style="font-style: normal">&nbsp;</span>(.*?)<br/>', s):
        terms.append((mm.group(1), html.unescape(re.sub('<[^>]+>', '', mm.group(2))).strip(), html.unescape(re.sub('<[^>]+>', ' ', mm.group(3))).strip()))
    defi = re.search(r'Definici(?:ó|&oacute;)</b><br/>(.*?)</span>', s, re.S)
    return dict(area=html.unescape(area.group(1)) if area else '', termes=terms,
                definicio=html.unescape(re.sub('<[^>]+>', '', defi.group(1)))[:200] if defi else '',
                raw=html.unescape(re.sub('<[^>]+>', ' ', s))[:600])
op = json.load(open('optimot.json'))
out = json.load(open('optimot_detall.json')) if os.path.exists('optimot_detall.json') else {}
cache = {}
for v in out.values():
    for d in v: cache[d['id']] = d
for terme, v in op.items():
    if terme in out: continue
    det = []; vistos = set()
    for r in v.get('res', []):
        if r['db'] == 'TERMCAT' and r['area'] != TIC: continue
        if r['id'] in vistos: continue
        vistos.add(r['id'])
        if r['id'] in cache:
            det.append(cache[r['id']]); continue
        try:
            t = get(U % (urllib.parse.quote('"%s"' % terme), r['db'], r['id'], r['id'], urllib.parse.quote_plus(r['font'])))
            d = parse(t, r['id']) or dict(area='?', termes=[], definicio='', raw='')
        except Exception as e:
            d = dict(area='ERROR', termes=[], definicio=str(e)[:100], raw='')
        d.update(id=r['id'], db=r['db'], font=r['font'], titol=r['titol'])
        cache[r['id']] = d; det.append(d)
        time.sleep(0.3)
    out[terme] = det
    json.dump(out, open('optimot_detall.json', 'w'), ensure_ascii=False, indent=1)
    print(terme, len(det), flush=True)
