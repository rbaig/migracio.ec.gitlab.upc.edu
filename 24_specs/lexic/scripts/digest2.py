import json, re, os, collections
p2 = json.load(open('pass2.json'))
c2 = {}
for fn, lang in (('cercaterm2_en.json', 'en'), ('cercaterm2_ca.json', 'ca')):
    if os.path.exists(fn):
        for k, v in json.load(open(fn)).items(): c2[lang + ':' + k] = v
def norm(x): return re.sub(r'[\s-]+', ' ', x.lower().replace(', to', '').strip())
def short(a): return a.replace('Tecnologies de la informació i la comunicació', 'TIC').replace('<', '').replace('>', '')
for key, r in p2.items():
    lang, q = key.split(':', 1)
    other = 'en' if lang == 'ca' else 'ca'
    ex = collections.OrderedDict(); co = []
    for d in r.get('optimot', []):
        if d.get('db') != 'TERMCAT': continue
        mine = [a for l, a, h in d['termes'] if l == lang]
        oth = ', '.join(a for l, a, h in d['termes'] if l == other)
        cas = '; '.join(a + (' [' + h + ']' if ('sin' in h or 'desest' in h) else '') for l, a, h in d['termes'] if l == 'ca')
        if any(norm(a) == norm(q) for a in mine):
            ex.setdefault(cas + ' {en: ' + ', '.join(a for l, a, h in d['termes'] if l == 'en')[:80] + '}', set()).add(d['area'])
    ct = c2.get(key, {})
    tic = collections.OrderedDict()
    for x in ct.get('tic', []):
        cas = '; '.join(a + (' [' + h + ']' if ('sin' in h or 'desest' in h) else '') for l, a, h in x['termes'] if l == 'ca')
        ens = ', '.join(a for l, a, h in x['termes'] if l == 'en')
        tic.setdefault(cas + ' {en: ' + ens[:80] + '}', set()).add(short(x['area']) + (' NEOLOTECA' if x['font'] else ''))
    totes = sorted(set(short(x['area']).split(' > ')[0] for x in ct.get('totes', [])))[:5] if not tic else []
    sc = r.get('sc') or '—'
    altres = sorted(set(d['font'].replace('<i>','').replace('</i>','').replace('<I>','').replace('</I>','')[:32] + ':' + d['titol'].strip() for d in r.get('optimot', []) if d.get('db') != 'TERMCAT' and norm(d['titol'].strip().rstrip('0123456789 ')) == norm(q)))
    print(f"### {key} | OPTIMOT total {r.get('optimot_total')} exacte TIC: " + (' || '.join(f'{k} <{"/".join(sorted(v))[:80]}>' for k, v in ex.items()) or '—'))
    print(f"    CERCATERM TIC: " + (' || '.join(f'{k} <{"/".join(sorted(v))[:80]}>' for k, v in tic.items()) or ('—' + (f' (totes: {totes})' if totes else '') + ('' if ct else ' [no consultat encara]'))))
    print(f"    SC({r.get('sc_status')}): {sc[:260]}" + (f"\n    ALTRES FONTS OPTIMOT: {altres}" if altres else ''))
