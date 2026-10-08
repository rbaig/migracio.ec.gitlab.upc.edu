# Regles de les escombrades

Aquestes regles eren a `13_contrib.qmd §Escombrades i verificació del corpus`
fins al 2026-10-07; en partir la guia (fase 7e de `CLAUDE.md §Pla de treball`)
van passar a aquesta skill, perquè només les fan servir les sessions de Claude
Code. Cada regla porta el cas que la va originar.


Una **escombrada** és tota cerca que pretén mesurar el corpus sencer: comptar
ocurrències d'una forma, localitzar tots els casos d'una convenció o sostenir
una afirmació sobre el conjunt. Aquestes regles surten totes d'una escombrada
que va fallar; cadascuna en porta el cas. `25_scripts/escombrada.sh` aplica les
que no demanen judici i escriu el compte, el repartiment per fitxer i l'ordre i
el commit que ho reprodueixen (`--help` diu quines regles cobreix).

**1. `git grep`, mai `grep -r`.** `git grep` només veu fitxers versionats: cobreix
l'arrel i `21_riscv/`, i exclou `auto_riscv/` (generat) i `_book/` sense haver-hi
de pensar. `grep -r` obliga a enumerar exclusions a mà, que és com es perden
ocurrències: l'escombrada de l'slug `desplacament-arithmetic` es va limitar a
`01_apunts/` i `04_laboratori/` i va deixar la quarta ocurrència a
`11_riscv.qmd`, que és contingut inclòs amb `{{< include >}}` i que cau fora de
les carpetes numerades (`953edca`). Afegiu el pathspec `':!TODO.md'` a tota
escombrada, o la mesura s'inclou a si mateixa: el compte d'`int main`/`void main` sense el
pathspec comptava els registres i l'informe que parlava de totes dues formes.
I **`git grep -c` compta línies, no ocurrències**: per a comptatges,
`git grep -o … | wc -l`.

L'exclusió era `':!TODO/'` mentre el fitxer vivia al directori `TODO/`; el
trasllat a l'arrel (2026-09-23) la va deixar sense excloure res, i amb ella
totes les xifres que el fitxer publica de si mateix. **Una exclusió per ruta
caduca amb la ruta**: quan un fitxer es mou, les mesures que l'excloïen són
part del que s'ha de migrar, no un detall del trasllat.

**2. Mesureu per forma, no per nom.** Un patró que busca noms concrets no mesura
el que la regla defineix. El que RARS rebutja no és cap nom sinó **l'expressió
aritmètica a l'operand**; el patró que buscava `NC*4`, `NC*2` i `.space` va
donar 20 línies a `A4.qmd` i 5 a `S4.qmd` (`c2a9171`), i les xifres per forma
eren 11 i 27 (`45f6cc2`) — a A4 inflava amb comentaris i repeticions, i a S4 se
li escapaven `N*4`, `(N+1)*4`, `3*(N-1)*4` i les directives `.set`, o sigui una
secció sencera, que la nota afegida amb la xifra dolenta deixava fora.

**3. Cap afirmació «és l'únic» o «no n'hi ha cap» sense l'ordre exacta que la
sosté**, i sense haver llegit el fitxer o el bloc sencer. Val igual per a les
afirmacions que arriben ja mesurades des d'un encàrrec o d'un registre: una
mesura pot no mesurar el que afirma, i verificar-la costa una ordre.

**4. El patró ha de cobrir totes les formes i tots els tipus de fitxer.**
Majúscules incloses (`-i`), i no només els `.qmd`. L'escombrada de «simple
precisió» ho va fallar per les dues bandes alhora: un patró en minúscules
deixava sis capçaleres de columna i de paràgraf a `A5.qmd` i `S5.qmd`, i un
patró restringit als `.qmd` deixava nou ocurrències més que viuen als SVG de
`22_figs_originals/` i al `24_specs/registres.toml`, que és la font de veritat
de les figures de registres.

**5. Per afirmar res sobre l'historial, pregunteu a l'historial**
(`git log -S'<fragment>' -- <fitxer>`, `git log --all -- <ruta>`), no a l'arbre
de treball. Un text absent del repositori pot ser feina no integrada o feina
**retirada a posta**, i des de l'arbre les dues coses són idèntiques. El cas:
dos extrets de juliol duien una línia sobre `fcvt.w.s` que semblava una millora
tècnica; `git log -S` va mostrar que el commit `92345e4` l'havia corregida
perquè era **incorrecta**. Reintroduir-la hauria posat un error tècnic en
aquest mateix fitxer.

`git log --all -- <ruta>` respon una pregunta diferent —si una cosa **hi va ser
mai**— i és igual d'invisible des de l'arbre. El cas és de la capa de revisió,
no de qui executava: de `04_laboratori/rars1_6.jar`, absent del repositori i
sense cap regla de `.gitignore` per als `.jar`, se'n va concloure que no hi
havia estat mai, i hi va ser des del commit inicial fins a `fbf7c3d`, que el va
eliminar deliberadament i ho diu al cos del missatge. `git ls-files` i el
`.gitignore` descriuen l'arbre d'avui; la pregunta era sobre l'historial.

Una tercera pregunta a l'historial: `git show <commit>~1:<fitxer>` respon
«aquesta còpia antiga, és l'estat previ a tal commit?». Si coincideix byte a
byte, totes les diferències són aquell commit i no cal classificar-ne cap una
a una. Serveix per a qualsevol còpia antiga —un `.orig`, una branca
abandonada, un fitxer que algú us passi—, no només per a la feina que la va
originar.

Una quarta, sobre els registres de revisió d'abans del 2026-09-22 (esborrats,
i recuperables amb `git show a211bbf:<ruta>`): **no en citeu cap resum, citeu
la secció pròpia de l'ítem i comproveu-la al corpus.** Un registre pot portar
diversos resums escrits en moments diferents, i cap marca no diu quin és
vigent —ni el titular, ni l'ordre al fitxer—. El cas (2026-09-23): a
`T4_P_tasques.md`, el titular diu «✅ FASE C COMPLETADA + DECISIONS FINALS
RESOLTES», la taula «Decisions que resten obertes per a tu» (`:24`) llista els
ítems 3, 4.2 i 8 com a pendents, i el resum final (`:329`) diu «no queda cap
decisió pendent tret de l'ítem 8». **El vigent és el segon resum**, i el
corpus ho confirma: `#wrn-mul-modul-2n` és a `A4.qmd:323` i el punter T4→T7, a
`13_contrib.qmd §Referències creuades`. Citar la taula de dalt hauria
registrat com a pendents dues coses fetes des de juliol. Fins al 2026-10-07
aquesta lliçó era a `CLAUDE.md §Estat dels materials`, que en citava el resum
final com a `:312`, una línia que no reprodueix a `a211bbf`.

**6. Quan trobeu un cas d'una forma, escombreu la forma**: ni el nom sol, ni la
línia sola. En excloure el mecanisme `startup.s`, l'escombrada pel nom va donar
setze ocurrències i un panorama tranquil; la traça que de debò contradeia la
decisió al llibre publicat era un bloc amb `.globl main` / `main:` / `ret` que
**no conté la paraula «startup»**, i era al callout de bones pràctiques, tres
línies abans de l'esquelet bo. Es va trobar escombrant les formes sintàctiques
del mecanisme, no el seu nom, i el bloc diu ara `suma:` (`c2a9171`).

**7. Abans d'afirmar que una línia arriba a l'alumne, comproveu `_quarto.yml`.**
Un fitxer comentat als `chapters:` segueix sent del projecte (vegeu
`CLAUDE.md §Abast del projecte`) i el seu contingut sortirà imprès quan es descomenti:
l'únic «TODO» escrit com a text de llibre era a `S_criteris_seleccio.qmd`, que
llavors no es renderitzava (el fitxer es va retirar el 2026-10-08, a la fase 7g), i per això cap escombrada del `_book/` no el veia. A
l'inrevés, `13_contrib.qmd` és **HTML-only** (`.content-visible when-format="html"`
obert a l'inici i tancat al final): res del que s'hi escriu no arriba al PDF.
L'escombrada es fa sempre **sobre el font**, no sobre la sortida.

**8. Un marcador dins del corpus és una còpia.** Abans de fer-lo desaparèixer
—o de retirar una entrada del `TODO.md`— comproveu **on en queda còpia** i
digueu-ho. Dos casos amb desenllaç oposat: el comentari `fig-lru-roger` es va
poder eliminar perquè el `TODO.md` ja en tenia l'entrada (i ara n'és l'única
còpia, cosa que consta a l'entrada); en canvi el bloc comentat d'`A2.qmd`
contenia un bolcat de RARS que no existia enlloc més
(`git grep -c "00c000ef" -- . ':!TODO.md' ':!13_contrib.qmd'` → cap, el
2026-09-23; l'exclusió de `13_contrib.qmd`, on llavors vivia aquesta regla,
n'amagava l'única ocurrència que hi quedava, **aquesta línia mateixa**),
i es va copiar al `TODO.md`
**abans** de la supressió, no després: totes dues coses, al mateix commit
`cef40b1`. L'inventari del que conté un bloc va a
l'informe abans d'eliminar-lo.

**9. Verifiqueu contra la llista de canvis aprovats i sobre l'arbre de
treball**, mai contra el fitxer d'on heu copiat. Si durant la revisió s'ha
acordat qualsevol afegit que no és a la font, la igualtat amb la font és una
**alarma, no una confirmació**. El cas: la comprovació final d'un fitxer es va
fer contra una còpia antiga i va donar OK; el que feia era confirmar la pèrdua
d'un paràgraf aprovat aquell mateix dia. `f136762` el va afegir, `7f0703c` el
va esborrar en aplicar l'extret a tota la regió, i `8b9f82d` el va restaurar
(el missatge d'aquest commit és l'exemple de `13_contrib.qmd §Format del missatge`).

**10. Una escombrada amb la sortida truncada no sosté cap negació.** Un
`| head -N`, un `-m N` o qualsevol altre límit donen una **mostra**: permeten
dir «n'hi ha almenys N», mai «no n'hi ha cap» ni «és l'únic» ni «enlloc». Per a
una negació, l'ordre s'executa **sencera** i se'n compta el resultat
(`… | wc -l`). El cas (2026-09-23):
`git grep -niE "\bmul\b" -- 01_apunts/A4.qmd | head -5` va fer concloure que el
callout `#wrn-mul-modul-2n` no existia i que el matís del `mul` mòdul $2^n$ era
un pendent obert; el callout és a `A4.qmd:323` i el `head -5` tallava a `:281`.
El límit no va acotar la lectura: va decidir la resposta. És la mateixa família
que la regla 3 —cap afirmació «és l'únic» o «no n'hi ha cap» sense l'ordre
exacta que la sosté—, i aquí la trampa és que l'ordre **hi era** i semblava
completa.

**11. Una xifra només és certa respecte del commit on es va mesurar.** Quan
dues lectures d'un mateix compte discrepen, la primera pregunta és **quan**,
no **com**: el corpus creix entremig. El cas (2026-09-23): una lectura del
`TODO.md` deia 19 pathspecs i 11 punters històrics, i la relectura en va
trobar 26 i 10 — cap de les dues no comptava malament, sinó que el Bloc 4d
n'havia escrit set de nous i n'havia consolidat un. Es comprova amb
`git show <commit>:<ruta>`, que retorna el fitxer tal com era:

```bash
git show 75987cb:TODO/TODO.md | grep -o "':!TODO/'" | wc -l   # 19
grep -o "':!TODO.md'" TODO.md | wc -l                         # 26
```

És la regla d'ancoratge de `CLAUDE.md §Flux de treball` —treballar per
àncora de contingut, no per número de línia— aplicada als **comptes**: una
xifra publicada sense dir de quan és no es pot verificar, només reproduir, i
si no reprodueix no se sap si ha caducat o si mai no va ser certa. **Dateu
les que publiqueu**, com fan les entrades del `TODO.md` i del registre de
decisions, amb la data entre parèntesis.

**12. Una afirmació d'absència ha d'excloure els fitxers que documenten el
cas.** Quan una entrada diu «X ja no és al corpus», la comprovació ha
d'excloure els fitxers que el documenten: el `TODO.md`, perquè hi registra la
tasca; `13_contrib.qmd` i `24_specs/registre_de_decisions.md`, perquè hi
escriuen la regla i el seu perquè; i `.claude/`, perquè les skills hi escriuen
la lliçó. Totes aquestes còpies són **cites, no ocurrències**. Si no s'exclouen, documentar una correcció la fa aparèixer com a
no feta:

```bash
git grep -c "00c000ef" -- . ':!TODO.md' ':!13_contrib.qmd' ':!24_specs/registre_de_decisions.md' ':!.claude/'
```

Fins al 2026-10-07 aquestes regles eren a `13_contrib.qmd`, i l'exclusió era
`':!TODO.md' ':!13_contrib.qmd'`. En partir la guia (fase 7e de
`CLAUDE.md §Pla de treball`), les lliçons van passar a aquesta skill i els
perquès al registre, i les ordres que els excloïen es van migrar amb ells
(regla 1: una exclusió per ruta caduca amb la ruta).

Els tres casos (2026-09-23): `fig-lru-roger`, `04_laboratori/rars1_6` i
`00c000ef`, els tres citats per aquestes regles mateixes. El d'`00c000ef` és el
cas pur —l'ordre escrita a la regla 8 era l'única ocurrència que quedava, de
manera que **es comptava a si mateixa**—; els altres dos els contamina prosa
veïna que en cita el cas. És la cara complementària de la regla 1: allà
l'exclusió evita que la **mesura** s'inclogui a si mateixa; aquí evita que
s'hi inclogui la **lliçó que n'explica el resultat**.

⚠️ **L'exclusió s'explica, no s'amaga.** Cada entrada corregida diu quina
ocurrència exclou i per què: una exclusió muda és indistingible d'una que tapa
una ocurrència real. I abans d'afegir-la, comproveu que el que s'exclou és
efectivament una cita —si l'ordre segueix sense reproduir la xifra publicada,
hi ha una ocurrència que no s'havia vist, i llavors el que s'ha de corregir és
l'afirmació, no el pathspec.

**12 bis. Un desglossament s'ha de poder sumar al total que acompanya.** Quan
una entrada publica un repartiment —per fitxer, per secció o per forma— al
costat d'una xifra global, les parts **han de sumar el global** i han de portar
l'ordre que les reprodueix, com el porta el total. El cas (2026-09-23): el
repartiment de `_start` sumava **91** contra un titular de **104**, amb quatre
valors dolents, i el total sí que reproduïa.

⚠️ **L'ordre va ancorada a un commit, perquè el corpus que mesurava ja no
existeix.** El criteri del punt d'entrada sense etiqueta (`13_contrib.qmd
§Convencions globals del laboratori`) ha tret `_start` del codi, de manera que la forma sobre l'arbre
de treball ja no dona aquell repartiment. L'exemple es mesura a `b2c1a4f`,
l'últim commit on era cert, i **hi reprodueix exacte**
(96 = 27+19+16+14+8+8+2+1+1):

```bash
git grep -o "_start" b2c1a4f -- '*.qmd' ':!TODO.md' ':!13_contrib.qmd' \
  | awk -F: '{print $2}' | sed 's|.*/||' | sort | uniq -c | sort -rn
```

📌 **Ancorar no és dir «avui dona zero»**: sobre l'arbre d'avui l'ordre dona
**3**, i són el callout d'`A3.qmd` que explica la convenció de GNU/Linux i per
què a EC no s'aplica —prosa correcta que hi ha de ser—. És el patró del
contraexemple de `@nte-rars-noms-reservats`: **la correcció introdueix
ocurrències d'allò que elimina**. Allà es podien marcar amb `codi_erroni`;
aquí no, perquè són prosa, i **l'única defensa és que la xifra ho digui**. Una
escombrada futura ha de trobar la resposta abans de la pregunta, en lloc
d'aturar-se a decidir si són un residu. Per això tota afirmació d'absència
d'aquesta família diu **quantes en queden, on i per què** (regla 12).

📌 **Un commit al `git grep` desplaça els camps**: la sortida passa a ser
`<commit>:<ruta>:<coincidència>`, de manera que l'`awk` ha de llegir `$2` i no
`$1`. És l'aplicació de la regla 11 a aquestes regles mateixes —una xifra només
és certa respecte del commit on es va mesurar—, i el motiu pel qual s'ancora
en lloc d'actualitzar-se: l'exemple no és el compte de `_start`, és **l'avaria
del desglossament que no sumava**, i aquella només es pot veure al corpus que
la tenia.

📌 **Un total correcte no avala les parts**: és precisament el que fa que se'n
refiï qui les llegeix. Va de bracet amb la regla 11 —el repartiment de `_start`
no era desfasat sinó **fals en néixer**, i només mesurar-lo al seu propi commit
ho distingeix—, i la comprovació és barata: sumar.

**13. Una afirmació sobre branques ha de dir de quin remot parla, i mesurar-se
amb `git ls-remote`.** `git branch -r` ensenya la **vista guardada del clon**,
que pot estar desfasada en les dues direccions: branques que ja no hi són i
branques que hi són i no s'han baixat. El projecte té **dos remots amb
contingut diferent** —GitLab (`origin`), que és la font de veritat, i el mirall
de GitHub (`mirror`), on el CI escriu la branca `build`—, de manera que «no
existeix» sense dir **on** no vol dir res.

```bash
git ls-remote --heads origin    # el que hi ha de debò a GitLab, ara
git ls-remote --heads mirror    # i al mirall, que no és el mateix
```

El cas (2026-09-23): `build` declarada inexistent mirant només GitLab —hi és,
al mirall, generada pel bot—, i `T3-review-adria` i `to-trash` declarades
existents des de referències de seguiment obsoletes, que `git fetch --prune`
va treure. Les dues direccions de l'error, en una sola lectura. Quan una
branca resulti ser una referència obsoleta, el que cal és **podar**, no
registrar-la.
