import json, re, sys, collections
sys.path.insert(0, '/home/roger/.claude-vocdoni/jobs/f97379a0/tmp')
from termes_c import C
c = json.load(open('cercaterm.json')); s = json.load(open('softcatala.json'))
od = json.load(open('optimot_detall.json')); op = json.load(open('optimot.json'))
cm = json.load(open('comptes.json')); g = json.load(open('glossari.json'))
forma = {r['en'].lower(): ('G', r['ca'], r['tema']) for r in g['principal']}
for t in ['pipeline', 'heap', 'target', 'caller', 'callee', 'caller-saved', 'callee-saved', 'sticky']:
    forma[t] = ('B', 'anglès', '')
for en, f, _ in C: forma.setdefault(en, ('C', f, ''))
def norm(x): return re.sub(r'[\s-]+', ' ', x.lower().replace(', to', '').strip())
def short(a): return a.replace('Tecnologies de la informació i la comunicació', 'TIC').replace('<', '').replace('>', '')
def sc_txt(v):
    if v['status'] != 200 or not v['text']: return '—' + ('' if v['status'] in (200, 404) else ' (%s)' % v['status'])
    t = v['text'].replace('\xa0', ' ')
    return re.sub(r'\s+', ' ', t)[:400]
def cnt(d):
    tot = sum(d.values()); return f"{tot}" + (" (" + ', '.join(f'{k} {v}' for k, v in sorted(d.items(), key=lambda x: -x[1])[:6]) + ")" if tot else '')
for t in [l.strip() for l in open('termes.txt') if l.strip()]:
    f = forma.get(t, ('?', '?', ''))
    print(f'### {t}  [{f[0]}] forma: {f[1]} {f[2]}')
    k = t if t in cm else None
    if k:
        e = cm[k]['en']; print(f"   corpus EN ital {cnt(e['ital'])} | pla {cnt(e['pla'])}" + (f" | CA {cnt({**cm[k]['ca']['ital'], **cm[k]['ca']['pla']})}" if 'ca' in cm[k] else ''))
    v = c.get(t, {})
    tic = collections.OrderedDict()
    for x in v.get('tic', []):
        cas = '; '.join(a + (' ['+h+']' if h and h not in ('n m','n f','n','adj','v tr','n m pl','n f pl','v intr','n m, f') else '') for l, a, h in x['termes'] if l == 'ca')
        ens = ', '.join(a for l, a, h in x['termes'] if l == 'en')
        tic.setdefault(cas, []).append(short(x['area']) + (' NEOLOTECA' if x['font'] else '') + ' {en: ' + ens + '}')
    print('   CERCATERM=TIC:', ' || '.join(f'{k2} <{" / ".join(sorted(set(v2)))[:200]}>' for k2, v2 in tic.items()) or '—', '' if v.get('ok') is True else f"(ok={v.get('ok')})")
    if not tic:
        ar = collections.Counter(short(x['area']).split(' > ')[0] for x in v.get('totes', []))
        noms = sorted(set(x['nom'] for x in v.get('totes', [])))[:6]
        print('   CERCATERM=totes:', dict(ar) or '—', noms)
    ex = collections.OrderedDict(); co = collections.OrderedDict(); alt = []
    for d in od.get(t, []):
        if d['db'] != 'TERMCAT': alt.append(d['font'][:40] + ':' + d['titol']); continue
        ens = [a for l, a, h in d['termes'] if l == 'en']
        cas = '; '.join(a + (' ['+h+']' if ('sin' in h or 'desest' in h or 'compl' in h) else '') for l, a, h in d['termes'] if l == 'ca')
        if any(norm(a) == norm(t) for a in ens): ex.setdefault(cas, set()).add(d['area'])
        elif any(re.search(r'(^| )' + re.escape(norm(t)) + r'( |$)', norm(a)) and len(norm(a).split()) <= len(norm(t).split()) + 2 for a in ens):
            co.setdefault(cas + ' {' + ', '.join(ens)[:60] + '}', set()).add(d['area'])
    print(f"   OPTIMOT (total {op.get(t, {}).get('total')}): exacte:", ' || '.join(f'{k2} <{"/".join(sorted(v2))[:120]}>' for k2, v2 in ex.items()) or '—')
    if co: print('      conté:', ' || '.join(f'{k2}' for k2 in list(co)[:6]))
    if alt: print('      altres fonts:', alt[:4])
    print('   SOFTCATALÀ:', sc_txt(s.get(t, {'status': '?', 'text': ''})))
