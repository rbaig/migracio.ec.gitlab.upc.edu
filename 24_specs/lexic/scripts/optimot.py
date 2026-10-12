"""Consulta l'Optimot (cerca de frase exacta, tipusCerca=cerca.queSignifica) i en retorna els resultats."""
import re,html,sys,json,urllib.parse,urllib.request,time
BASE='https://aplicacions.llengua.gencat.cat/llc/AppJava/index.html?action=Principal&method=cerca_generica&tipusCerca=%s&input_cercar=%s&numPagina=%d'
def get(url):
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=40) as r:
                return r.read().decode('utf-8','replace')
        except Exception as e:
            err=e; time.sleep(3)
    raise err
def cerca(terme,tipus='cerca.queSignifica',pagines=3):
    res=[]; total=None
    for p in range(1,pagines+1):
        t=get(BASE%(tipus,urllib.parse.quote(terme),p))
        m=re.search(r'Resultats de la cerca[^:]*:\s*(?:&nbsp;)?(\d+)',t)
        if m: total=int(m.group(1))
        for a in re.finditer(r'<a href="index\.html[^"]*?database=([^&]*)&amp;idFont=(\d+)[^"]*?tipusFont=([^&]*)[^"]*?titol=([^&]*)&amp;tematica=([^&"]*)[^"]*"',t):
            res.append(dict(db=a.group(1),id=a.group(2),font=urllib.parse.unquote_plus(html.unescape(a.group(3))),titol=urllib.parse.unquote_plus(html.unescape(a.group(4))),area=urllib.parse.unquote_plus(html.unescape(a.group(5)))))
        if total is None or len(res)>=total: break
    return total,res
if __name__=='__main__':
    for w in sys.argv[1:]:
        tot,r=cerca(w)
        print(w,tot)
        for x in r: print('   ',x['font'],'|',x['area'],'|',x['titol'])
