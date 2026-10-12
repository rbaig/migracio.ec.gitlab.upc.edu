import json
d='/home/roger/.claude-vocdoni/jobs/f97379a0/tmp/'
t=json.load(open(d+'taules.json'))
cap=open(d+'cap.md').read(); cua=open(d+'cua.md').read()
txt=cap + t['C'] + '\n\n## Taula 2. Dubtoses (decisió de l\'editor)\n\n' + t['D'] + \
 '\n\n## Taula 3. Glossari: es mantenen\n\nInclou, com a fila de referència, els termes del glossari que també surten a la taula 1 per un ús concret o per l\'observació (*Polling*, *Syscall*, *Store*, *Page-table walker*, *Jump table*, *Half-adder*, *Full-adder*, *Multicore*): la forma del glossari es manté.\n\n' + t['M_G'] + \
 '\n\n## Taula 4. Es mantenen en anglès\n\nLes cinc primeres són a la segona taula del glossari; la resta en són candidates (decisió 2). *Heap* és a la taula 1 (motiu).\n\n' + t['A'] + \
 '\n\n## Taula 5. Anglicismes fora del glossari amb la glossa catalana al text: es mantenen\n\n' + t['M_N'] + '\n' + cua
open(d+'lexic.md','w').write(txt)
print(len(txt))
