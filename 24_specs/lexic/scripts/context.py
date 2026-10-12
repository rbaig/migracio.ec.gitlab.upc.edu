import sys,re
R='/home/roger/gitlab/migracio/'
rows=[l.rstrip('\n').split('\t') for l in open('italiques.tsv',encoding='utf-8')]
skip=re.compile(r'^(Vegeu|Pas \d|Precisió|Float |CSR read|Multiply|Divide|Remainder|Machine |Supervisor |Tools|Settings|Run|File)')
for f,n,s in rows:
    if skip.match(s): continue
    line=open(R+f,encoding='utf-8').read().split('\n')[int(n)-1]
    i=line.find('*'+s) if ('*'+s) in line else line.find(s)
    a=max(0,i-90); b=i+len(s)+60
    print(f'{s} || {f}:{n} || {line[a:b]}')
