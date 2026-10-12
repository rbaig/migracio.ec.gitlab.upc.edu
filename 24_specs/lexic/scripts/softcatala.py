"""Consulta el diccionari anglès-català de Softcatalà i en retorna les entrades (lema, categoria, accepcions amb àrea)."""
import re,html,sys,urllib.parse,urllib.request,time
URL='https://www.softcatala.org/diccionari-angles-catala/eng/paraula/%s/'
def get(url):
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=40) as r:
                return r.status, r.read().decode('utf-8','replace')
        except urllib.error.HTTPError as e:
            return e.code, ''
        except Exception as e:
            err=e; time.sleep(3)
    raise err
def text(s):
    s=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)
    s=re.sub(r'<[^>]+>',' ',s); return html.unescape(re.sub(r'\s+',' ',s)).strip()
def cerca(terme):
    st,t=get(URL%urllib.parse.quote(terme))
    if st!=200: return st,None
    s=text(t)
    m=re.search(r'anglès → català \((\d+) resultats?\)(.*?)(Exemples d’ús|Altres paraules|Compartiu|$)',s)
    if not m:
        if 'No s’ha trobat' in s or 'no s\'ha trobat' in s.lower() or 'cap resultat' in s.lower(): return st,''
        i=s.find('Resultats de la cerca'); return st,'?? '+s[i:i+300]
    return st,m.group(2).strip()
if __name__=='__main__':
    for w in sys.argv[1:]:
        print(w,'=>',cerca(w))
