"""Segona passada: Optimot (frase exacta + fitxes TIC) i Softcatalà per a variants angleses i formes catalanes."""
import json, os, re, sys, time, urllib.parse
sys.path.insert(0, '/home/roger/.claude-vocdoni/jobs/f97379a0/tmp')
import optimot, softcatala
from optimot_detall import U, parse, TIC
from optimot import get
from pass2_termes import EN_VAR, CA
od = json.load(open('optimot_detall.json'))
cache = {d['id']: d for v in od.values() for d in v}
out = json.load(open('pass2.json')) if os.path.exists('pass2.json') else {}
SC_CAT = 'https://www.softcatala.org/diccionari-angles-catala/cat/paraula/%s/'
def sc(q, lang):
    if lang == 'en': return softcatala.cerca(q)
    st, t = softcatala.get(SC_CAT % urllib.parse.quote(q))
    if st != 200: return st, None
    s = softcatala.text(t)
    m = re.search(r'català → anglès \((\d+) resultats?\)(.*?)(Exemples d’ús|Ajudeu-nos|$)', s)
    return st, (m.group(2).strip()[:500] if m else '')
for lang, llista in (('en', EN_VAR), ('ca', CA)):
    for q in llista:
        key = lang + ':' + q
        if key in out: continue
        r = {}
        try:
            tot, res = optimot.cerca(q, pagines=6)
            det = []
            seen = set()
            for x in res:
                if x['db'] == 'TERMCAT' and x['area'] != TIC: continue
                if x['id'] in seen: continue
                seen.add(x['id'])
                if x['id'] in cache: det.append(cache[x['id']]); continue
                try:
                    t = get(U % (urllib.parse.quote('"%s"' % q), x['db'], x['id'], x['id'], urllib.parse.quote_plus(x['font'])))
                    d = parse(t, x['id']) or dict(area='?', termes=[], definicio='', raw='')
                except Exception as e:
                    d = dict(area='ERROR', termes=[], definicio=str(e)[:100], raw='')
                d.update(id=x['id'], db=x['db'], font=x['font'], titol=x['titol'])
                cache[x['id']] = d; det.append(d); time.sleep(0.2)
            r['optimot_total'] = tot; r['optimot'] = det
        except Exception as e:
            r['optimot_error'] = str(e)[:200]
        try:
            st, txt = sc(q, lang); r['sc_status'] = st; r['sc'] = txt
        except Exception as e:
            r['sc_error'] = str(e)[:200]
        out[key] = r
        json.dump(out, open('pass2.json', 'w'), ensure_ascii=False, indent=1)
        print(key, r.get('optimot_total'), len(r.get('optimot', [])), r.get('sc_status'), flush=True)
