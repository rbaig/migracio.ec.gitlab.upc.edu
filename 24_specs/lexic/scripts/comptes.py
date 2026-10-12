"""Compta les ocurrències (prosa, fora de codi i matemàtiques) de cada terme anglès (en cursiva i en pla)
i de la forma catalana dels termes del glossari. Escriu comptes.json."""
import re, json, sys, collections
sys.path.insert(0, '/home/roger/.claude-vocdoni/jobs/f97379a0/tmp')
from termes_c import C
rows = [l.rstrip('\n').split('\t', 2) for l in open('prosa.tsv', encoding='utf-8')]
def fitxer(f): return f.split('/')[-1].replace('.qmd', '')
def ital_spans(t):
    t = t.replace('***', '*').replace('**', '')
    return [(m.start(), m.end()) for m in re.finditer(r'(?<![\w*\\])\*(?![\s*])[^*\n]+?(?<![\s\\])\*(?![\w*])', t)], t
def pat_en(term):
    parts = re.split(r'([ /+-])', term)
    out = ''
    for p in parts:
        if p in (' ', '-'): out += r'[ -]'
        elif p in ('/', '+'): out += r'\s*' + re.escape(p) + r'\s*'
        else: out += re.escape(p)
    return r'(?<![\w-])' + out + r'(?:s|es)?(?![\w-])'
def pat_ca(term):
    ws = term.split()
    o = []
    for w in ws:
        w = w.strip('«»')
        if len(w) <= 2 or w in ('de', 'del', 'la', 'el', 'per', 'al', 'a'): o.append(re.escape(w)); continue
        if w.endswith('a'): o.append(re.escape(w[:-1]) + '(?:a|es)')
        elif w.endswith('ó'): o.append(re.escape(w[:-1]) + '(?:ó|ons)')
        elif w.endswith('ble'): o.append(re.escape(w) + 's?')
        else: o.append(re.escape(w) + '(?:s|os|es)?')
    return r'(?<![\w])' + r'\s+'.join(o).replace("d'", "d['’]") + r'(?![\w])'
def compta(pat):
    rx = re.compile(pat, re.I)
    it = collections.Counter(); pl = collections.Counter()
    for f, n, t in rows:
        spans, t2 = ital_spans(t)
        for m in rx.finditer(t2):
            if any(a <= m.start() < b for a, b in spans): it[fitxer(f)] += 1
            else: pl[fitxer(f)] += 1
    return dict(ital=dict(it), pla=dict(pl))
g = json.load(open('glossari.json'))
res = {}
for r in g['principal']:
    en = r['en']; ca = r['ca']
    res[en.lower()] = dict(en=compta(pat_en(en)), ca=compta(pat_ca(ca)), ca_forma=ca)
for t in ['pipeline', 'heap', 'target', 'caller', 'callee', 'caller-saved', 'callee-saved', 'sticky']:
    res[t] = dict(en=compta(pat_en(t)))
for en, forma, _ in C:
    res.setdefault(en, dict(en=compta(pat_en(en))))
extra = {'tiling': 'tiling', 'walker': 'walker', 'handler': 'handler', 'fetch': 'fetch'}
for k, v in extra.items(): res['_' + k] = dict(en=compta(pat_en(v)))
json.dump(res, open('comptes.json', 'w'), ensure_ascii=False, indent=1)
def s(d): 
    tot = sum(d.values()); return f"{tot} (" + ', '.join(f'{k} {v}' for k, v in sorted(d.items(), key=lambda x: -x[1])) + ")" if tot else '0'
for k, v in res.items():
    print(k, '| EN ital', s(v['en']['ital']), '| EN pla', s(v['en']['pla']), ('| CA ' + s({**v['ca']['ital'], **v['ca']['pla']}) if 'ca' in v else ''))
