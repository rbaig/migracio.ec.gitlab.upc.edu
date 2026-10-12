"""Consulta Softcatalà i l'Optimot per a cada terme de termes.txt; escriu softcatala.json i optimot.json."""
import json, os, sys, time, re
sys.path.insert(0, '/home/roger/.claude-vocdoni/jobs/f97379a0/tmp')
import softcatala, optimot
termes = [l.strip() for l in open('termes.txt', encoding='utf-8') if l.strip()]
sc = json.load(open('softcatala.json')) if os.path.exists('softcatala.json') else {}
op = json.load(open('optimot.json')) if os.path.exists('optimot.json') else {}
for t in termes:
    if t not in sc:
        try:
            st, r = softcatala.cerca(t)
            d = dict(status=st, text=r)
            if st == 404 and ' ' in t.replace('-', ' '):
                cap = re.split(r'[ -]', t)[0]
                st2, r2 = softcatala.cerca(cap)
                hits = []
                if r2:
                    for m in re.finditer(re.escape(t), r2, re.I):
                        hits.append(r2[max(0, m.start()-10): m.end()+160])
                d.update(cap=cap, cap_status=st2, cap_hits=hits)
            sc[t] = d
        except Exception as e:
            sc[t] = dict(status='error', text=str(e)[:200])
        json.dump(sc, open('softcatala.json', 'w'), ensure_ascii=False, indent=1)
    if t not in op:
        try:
            tot, r = optimot.cerca(t, pagines=6)
            op[t] = dict(total=tot, res=r)
        except Exception as e:
            op[t] = dict(error=str(e)[:200])
        json.dump(op, open('optimot.json', 'w'), ensure_ascii=False, indent=1)
    print(t, sc[t].get('status'), op[t].get('total'), flush=True)
    time.sleep(0.5)
