import subprocess, collections, re, sys
rows=[l.rstrip('\n').split('\t') for l in open('italiques.tsv',encoding='utf-8')]
spans=collections.Counter(r[2] for r in rows)
words=set()
for s in spans:
    words.update(re.findall(r"[A-Za-zÀ-ÿ·'’-]+",s))
def unknown(d):
    out=subprocess.run(['hunspell','-l','-i','utf-8','-d',d],input='\n'.join(words),capture_output=True,text=True).stdout.split()
    return set(out)
unk_ca=unknown('ca_ES'); unk_en=unknown('en_US')
for s,c in spans.most_common():
    ws=re.findall(r"[A-Za-zÀ-ÿ·'’-]+",s)
    nca=[w for w in ws if w in unk_ca]
    nen=[w for w in ws if w in unk_en]
    tag = 'EN' if nca and len(nen)<len(ws) else ('CA' if not nca and nen else ('BOTH' if not nca else '??'))
    print(f'{tag}\t{c}\t{s}')
