import json, sys, collections
sys.path.insert(0, '/home/roger/.claude-vocdoni/jobs/f97379a0/tmp')
from files import R, G
cm = json.load(open('comptes.json')); g = json.load(open('glossari.json'))
def top(d, n=4):
    it = sorted(d.items(), key=lambda x: -x[1]); s = ', '.join(f'{k.replace("RV32I_", "21_riscv/RV32I_")[:60]} {v}' for k, v in it[:n])
    return s + (', …' if len(it) > n else '')
def us(key):
    v = cm.get(key)
    if not v: return '—'
    e = v['en']; ti = sum(e['ital'].values()); tp = sum(e['pla'].values())
    parts = []
    if ti: parts.append(f'ital {ti} ({top(e["ital"])})')
    if tp: parts.append(f'pla {tp} ({top(e["pla"])})')
    s = '; '.join(parts) or 'EN 0'
    if 'ca' in v:
        c = collections.Counter(v['ca']['ital']) + collections.Counter(v['ca']['pla'])
        s += f'; CA {sum(c.values())}' + (f' ({top(c, 3)})' if c else '')
    return s
def esc(x): return (x or '').replace('|', '\\|')
glos = {r['en'].lower() for r in g['principal']}
sec = {'C': [], 'D': [], 'M': [], 'A': []}
for key, en, forma, op, sc, u, cat, prop, mot in R:
    isg = en.startswith(G); en2 = en[1:] if isg else en
    if isg: forma = forma + ' (glossari)'
    en3 = en2.split(' (', 1); en3 = f'*{en3[0]}* (' + en3[1] if len(en3) == 2 else f'*{en2}*'
    row = f'| {esc(en3)} | {esc(forma)} | {esc(op)} | {esc(sc)} | {esc(u if u else us(key))} | {esc(prop)} | {esc(mot)} |'
    sec[cat].append((isg, row, key))
hdr = '| Anglès | Forma actual al llibre | Optimot/Termcat | Softcatalà | Ús al corpus | Proposta | Motiu |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- |'
out = {}
for c in sec:
    rows = sec[c]
    if c == 'M':
        gl = [r for r in rows if r[0]]; ng = [r for r in rows if not r[0]]
        out['M_G'] = hdr + '\n' + '\n'.join(r[1] for r in gl)
        out['M_N'] = hdr + '\n' + '\n'.join(r[1] for r in ng)
    else:
        out[c] = hdr + '\n' + '\n'.join(r[1] for r in rows)
json.dump(out, open('taules.json', 'w'), ensure_ascii=False)
# cobertura del glossari
keys_by_cat = collections.defaultdict(set)
for key, en, *_ in R:
    pass
cov = collections.defaultdict(set)
for key, en, forma, op, sc, u, cat, prop, mot in R:
    k = key.lstrip('_')
    if k in glos: cov[k].add(cat)
miss = sorted(glos - set(cov))
print('glossari sense fila:', miss)
st = {k: ('C' if 'C' in v else 'D' if 'D' in v else 'M') for k, v in cov.items()}
print('glossari per estat:', collections.Counter(st.values()))
print('C glossari:', sorted(k for k, v in st.items() if v == 'C'))
print('D glossari:', sorted(k for k, v in cov.items() if 'D' in v))
print('files per secció:', {c: len(v) for c, v in sec.items()})
nong = [r for c in sec for r in sec[c] if not r[0]]
print('files fora del glossari principal:', len(nong))
