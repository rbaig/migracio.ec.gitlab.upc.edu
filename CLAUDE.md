# CLAUDE.md — Estructura de Computadors (EC)

## Projecte

Apunts de l'assignatura **Estructura de Computadors** (EC), Grau d'Enginyeria
Informàtica (GEI), FIB-UPC. Llibre Quarto (`_quarto.yml`), amb sortida HTML i PDF.
Llengua: **català** (tot el contingut generat ha de ser en català).

## Fitxers de referència obligatòria

Abans de qualsevol acció, llegeix:

1. `_quarto.yml` — configuració del projecte.
2. `index.qmd` — fitxers que componen el llibre.
3. `13_contrib.qmd` — convencions d'estil, callouts, terminologia, SVG, laboratori i decisions per tema.
4. `TODO.md` — tasques pendents i decisions obertes.

Per a tasques que impliquin figures SVG, llegeix també:

- `24_specs/svg.md` — paleta de colors, mapes de fonts i taula de substitució dark.
- `24_specs/registres.toml` — definicions dels registres de bits (font de veritat).

Repartiment de responsabilitats entre fitxers:

- `13_contrib.qmd` és **el fitxer de referència** del projecte i ha d'estar sempre actualitzat. Hi va qualsevol decisió de format, estil, terminologia o convenció.
- `CLAUDE.md` (aquest fitxer) recull **només** l'operació a claude.ai. Qualsevol altre aspecte va a `13_contrib.qmd`.
- `README.md` és el fitxer de presentació del repositori (documentació habitual d'un projecte Quarto tipus *book*).
- `TODO.md` només conté contingut transitori. El que ha de quedar buit al final
  és **el fitxer mateix** —és a dir, no hi ha de restar cap entrada viva—, no
  cap directori: el fitxer viu a l'arrel des del 2026-09-23, i el `TODO/` que
  el contenia ja no existeix.

Altres fitxers transversals: `11_riscv.qmd` (compendi de referència RISC-V, inclòs via `{{< include >}}`) i `12_sigles_simbols.qmd` (glossari de sigles i símbols).

## Abast del projecte

### Estructura de fitxers `.qmd`

Convenció de noms (x = número de tema, 1–9; y = sessió de laboratori):

- `Ax.qmd`: teoria del tema x.
- `Ex.qmd`: enunciats dels problemes del tema x.
- `Sx.qmd`: solucions d'una selecció de problemes del tema x.
- `S_criteris_seleccio.qmd`: criteris de selecció dels problemes a solucionar.
- `Ly.qmd`: laboratori, sessió y.

### Volum

| Material | Fitxers `.qmd` |
| :--- | :--- |
| Teoria | `A1.qmd`–`A9.qmd` |
| Enunciats | `Ex.qmd` (x = 1–9) |
| Solucions | `Sx.qmd` (x = 2–9), `S_criteris_seleccio.qmd` |
| Laboratori | `L1.qmd`–`L6.qmd` |

Tots els fitxers `.qmd` de `index.qmd` formen part del projecte, encara que estiguin comentats (es comenten per escurçar el temps de renderització en proves).

Els PDFs originals (MIPS) són al directori `/PDF_originals`; consulta'ls en cas de dubte sobre els continguts.

## Revisió interna

El contingut de teoria (T1–T9), laboratori (L1–L6) i solucionari (S2–S8) ja està generat. ✅ **La revisió interna és tancada sencera**, per declaracions de l'usuari: teoria i laboratori el 2026-09-23, enunciats i solucionaris el 2026-10-01 (vegeu §Estat dels materials).

**El projecte és, doncs, a la fase de revisió externa**, que fan altres professors de l'assignatura. Ha començat per a **T3** (branca `contingut/t3-traduccio`, des del 6 de juliol del 2026) i per a **T4, T5 i T6** (branca `temes456`, des del 21 de juliol), però **el 2026-10-01 les dues MR (`!5` i `!7`) es van tancar sense fusionar**. La integra una sessió de Claude Code (§Pla de treball, fase 1): **totes dues ja són a `main` des del 2026-10-01** (T4–T6, `451c3ef`; T3, `ab48732`); el detall és al 📌 de §Estat dels materials → Teoria. Per a **T8** va començar el 2026-10-05 (branca `tema8`, MR `!8`, Adrià Armejach), i la MR es va fusionar a `main` el 2026-10-06 (`80f8946`), amb la revisió feta fins a §8.7 (exclosa). Per a la resta del material encara no ha començat. L'ordre de la feina que queda és a §Pla de treball.

**Abast de la revisió externa** (declaracions de l'usuari, 2026-10-06, literals): «de moment, la revisió externa només afecta A1--A8. A9 de moment n'ha quedat fora i també Ex, Sx i Ly»; «Inclou també T3--T6»; «Les branches de revisió les crearà cada equip de revisió». I, el mateix dia: ara mateix no hi ha cap revisor extern actiu. Conseqüència operativa: **abans de tocar A1–A8, `21_riscv/` o una figura que A1–A8 consumeixi, `git fetch` i `git ls-remote --heads origin`**; si un equip ja hi té una branca que toca el fitxer, no es toca: se'n registra el pendent i s'avisa l'usuari.

### Prioritats de la revisió

- Prioritats màximes: **coherència pedagògica** i **rigor tècnic** en tot el contingut.
- Revisió tècnica profunda i revisió lingüística en **català normatiu**.
- Solucionaris: detall **pas a pas**, excepte els passos trivials.
- **Harmonització abans de la revisió externa**: «Preparat per a revisió externa» no vol dir tancat a canvis profunds, especialment els d'harmonització (terminologia, estil, convencions transversals). Tot el que es pugui detectar i corregir abans que la revisió externa arribi a un fitxer s'ha de fer ara, encara que impliqui tocar fitxers ja marcats com a preparats: amb altres professors ja dins de la revisió, qualsevol canvi transversal té un cost de coordinació molt més alt. ⚠️ Per a **T3, T4, T5, T6 i T8 això ja ha passat**: la revisió externa hi és en curs (§Estat dels materials → Teoria), i des del 2026-10-06 l'abast declarat és A1–A8 sencer (§Revisió interna, «Abast de la revisió externa»), de manera que un canvi transversal que els toqui s'ha de coordinar amb els revisors, no aplicar-hi pel davant. Abans de tocar qualsevol fitxer que una branca de revisió també toqui —no només `A3.qmd`–`A6.qmd`—, feu-ne una fusió de prova (`TODO.md §Decisions obertes → Branques del remot`): `980434b` va afegir un conflicte a `.gitignore` per no haver-la feta. Si detectes una inconsistència que afecta múltiples fitxers (per exemple, terminologia o notació aplicada de manera desigual), proposa'n la correcció sistemàtica encara que surti de l'abast estricte del xat en curs.

### Estat dels materials

*Actualitzat el 2026-10-01. Secció única: hi és fusionada l'antiga §Seqüència de revisió pendent, que duplicava aquesta amb un marcador de progrés per tema. La seqüència de la feina que queda és a §Pla de treball.*

El fitxer en curs (WiP) l'indica l'usuari a l'inici de cada xat.

**Com es llegeixen les taules.** Una cel·la pot tenir **tres formes**, i cap d'elles és un veredicte derivat:

1. **Remet a un commit** — certa per sempre, perquè descriu el que aquell commit va declarar.
2. **Remet a l'estat declarat en un fitxer** (els registres de revisió, avui esborrats), amb el punter que el recupera. Sovint és **més precís que l'assumpte del commit**, que ha de cabre en una línia.

   ⚠️ **No citeu cap resum d'un registre: citeu la secció pròpia de l'ítem i comproveu-la al corpus.** Un registre pot portar **diversos resums escrits en moments diferents**, i cap marca no diu quin és vigent —ni el titular, ni l'ordre al fitxer—. El cas (2026-09-23): a `T4_P_tasques.md`, el titular diu «✅ FASE C COMPLETADA + DECISIONS FINALS RESOLTES», la taula «Decisions que resten obertes per a tu» (`:24`) llista els ítems 3, 4.2 i 8 com a pendents, i el resum final (`:312`) diu «no queda cap decisió pendent tret de l'ítem 8». **El vigent és el segon resum**, i el corpus ho confirma: `#wrn-mul-modul-2n` és a `A4.qmd:323` i el punter T4→T7 a `13_contrib.qmd:706`. Citar la taula de dalt hauria registrat com a pendents dues coses fetes des de juliol.
3. **És una declaració de l'usuari** — va a la columna «declaració de tancament», i només ell la pot omplir.

«Fase C executada» **no** volia dir «revisió interna acabada». Entre les dues hi havia les *passades finals*, i el tancament es declarava per separat per a les tres revisions —**pedagògica, tècnica i lingüística**—. Amb la revisió interna tancada, la distinció queda com a registre: com es va tancar cada ítem és a `TODO.md §Entrades retirades → Executades` («Passades finals pendents»), i la plantilla que feia les tres preguntes, a l'historial (`git show 980434b:26_prompts/Lx__revisio_interna__plantilla.md`). Val igual per a la revisió externa: que una MR es fusioni no vol dir que el revisor doni el tema per tancat.

⚠️ **Una declaració de l'usuari no es verifica: es registra.** Demanar-li el commit que la sosté és un error de categoria —equival a demanar el commit que demostra una decisió— i esborrar-la per «no verificable» destrueix l'única còpia del que algú va declarar. Val tant per al punt 3 del protocol de sanejament (§Flux de treball) com per a qualsevol fusió de seccions: **abans de treure una secció, se'n registren els pendents i també les declaracions**.

Els commits transversals (auditories i harmonitzacions de setembre: `c2a9171`, `4accc6c`, `b3072a6`, `d017ee2`, `45f6cc2`, `257d37f`…) toquen molts fitxers alhora i **no són passades de revisió d'un tema**: no compten a la columna «passades posteriors».

#### Teoria (T1–T9)

Marc: **preparats per a revisió externa** (`A1.qmd`–`A9.qmd`). Segons §Prioritats de la revisió, això **no** vol dir tancat a canvis, especialment els d'harmonització.

✅ **La revisió interna de teoria és tancada: T1–T9, tots nou, el 2026-09-23** (declaracions de l'usuari, una per tema, al llarg del Bloc 4d). La taula d'estat per tema ja no cal, perquè no hi resta cap tema obert.

El tancament de cada tema —amb l'estat que tenia, el commit que el declarava i què en sobreviu— és a `TODO.md §Entrades retirades`. Quatre casos hi van necessitar una decisió o una execució abans de tancar-se, i el registre en diu el resultat: **T5** (revisió declarada «parcial»: auditats els 29 ítems del seu registre, executats els tres que restaven), **T6** (S6 harmonitzada sencera a $V_{CC}$), **T7** (C3, l'enunciat truncat d'`exr-t7-assoc-multinivell`, reparat contra el PDF original) i **T9** (contradicció entre l'assumpte del commit i el registre, resolta per decisió a favor del registre).

⚠️ **Tancar la revisió d'un tema no tanca el que hi queda registrat.** Els marcadors del corpus, les figures pendents i les decisions obertes **sobreviuen** al tancament i es resolen des de les seves entrades del `TODO.md`, sense reobrir cap tema: els set marcadors d'`A2.qmd`, les figures de T7 i T8, les decisions R4-TYPE i R5-TYPE d'A5, `#cau-boolea-c` d'A3, l'ítem 8 de T4 i la resta.

📌 **T3, T4, T5, T6 i T8: la revisió externa ja és en curs.** És l'etapa que segueix la interna, i el tancament de la interna declarat més amunt n'és la **condició prèvia**: les dues coses són coherents.

- **T4, T5 i T6, a `temes456` (MR `!7`).** El grup de treball hi va revisar `A4.qmd`, `A5.qmd` i `A6.qmd` del 21 de juliol al 7 d'agost (11 commits). Una fusió de prova (2026-10-01) donava tres conflictes: `A4.qmd`, `A5.qmd` i `.gitignore`. **La MR es va tancar sense fusionar el 2026-10-01** (`pedro.martinez.ferrer`, 16:21; GitLab la marcava `cannot_be_merged`). Decisió de l'usuari (2026-10-01, al vespre, substituint la d'esperar el grup): **la fusió la fa una sessió de Claude Code**, amb l'aprovació de l'usuari de cada conflicte resolt abans del push (§Pla de treball, fase 1). ✅ **Fusionada el mateix dia: `451c3ef`** (commit de fusió, autoria dels 11 commits conservada), seguida de `40396e8` (errades que portava la branca) i `454a82e` (marca dels termes anglesos, de les sigles i d'«A **EC**», restaurada per decisió de l'usuari). `A4.qmd`–`A6.qmd` ja es poden tocar, i les 10 anotacions de la branca són marcadors a `main`. Que la branca s'hagi fusionat no vol dir que el grup doni la revisió per tancada.
- **T3, a `contingut/t3-traduccio` (MR `!5`, Pedro J. Martinez-Ferrer, 2026-07-06).** Un sol commit, amb rutes d'abans de la reorganització de directoris, que git no pot fusionar. **El port a les rutes actuals el fa l'autor de la MR** (decisió de l'usuari, 2026-10-01). **La MR es va tancar sense fusionar el 2026-10-01** (16:20, el mateix autor). Decisió de l'usuari (al vespre): **el port el fa una sessió de Claude Code**, hunk a hunk i amb `Co-authored-by` de l'autor (§Pla de treball, fase 1). ✅ **Portada el mateix dia: `ab48732`.** `A3.qmd` ja es pot tocar, i els vuit comentaris del revisor són marcadors a `main` (`TODO.md §Entrades retirades → Executades`, «Anotacions de la revisió externa de T3»). ✅ Set s'han valorat i resolt el 2026-10-02 (fase 3b del pla); el vuitè, la «↔» d'`A3.qmd:322`, és de la fase 4, i s'ha resolt el mateix dia (`0d7bd5c`).
- **T8, a `tema8` (MR `!8`, Adrià Armejach, 2026-10-05 i 06).** 32 commits sobre `A8.qmd`, `A9.qmd`, `E8.qmd`, `S8.qmd`, `13_contrib.qmd §T8` i les figures de T8 (`gen_T8.py`): el TLB passa al model de RISC-V. ✅ **Fusionada a `main` el 2026-10-06 per l'usuari, des del GitLab, sense conflictes: `80f8946`**, amb commit de fusió i sense *squash*. **La revisió és parcial**: la descripció de la MR diu «Canvis fets fins a la secció 8.7 (exclosa)», de manera que §Integració del TLB i la memòria cau encara no s'ha revisat. La branca es conserva, perquè el revisor hi pugui continuar.
- **La resta d'A1–A8 (T1, T2, T7 i el que queda de T8), i una segona volta de T3–T6.** Declaracions de l'usuari (2026-10-06): la revisió externa afecta, de moment, **A1–A8**, «també T3--T6»; **A9, Ex, Sx i Ly en queden fora** de moment, i **les branques les crea cada equip**. El mateix dia no hi havia cap revisor extern actiu ni cap branca d'equip a `origin` (`git ls-remote --heads origin`: `main`, `tema8`, ja dins de `main`, `temes456` i `contingut/t3-traduccio`). Text literal a §Revisió interna, «Abast de la revisió externa».

Estat de les branques, autors i el que cada fusió haurà de resoldre fitxer per fitxer: `TODO.md §Decisions obertes → Branques del remot`.

#### Enunciats (`Ex.qmd`) i Solucionaris (`Sx.qmd`)

✅ **La revisió interna d'enunciats i solucionaris és tancada: `E1.qmd`–`E9.qmd` i `S1.qmd`–`S9.qmd`, el 2026-10-01.** Declaració de l'usuari, literal: «les revisions internes es poden donar per acabades». Amb ella queda tancada tota la revisió interna. (`E3.qmd` i `S3.qmd` ja hi constaven com a completats des del 2026-07-12, `614f576`.)

⚠️ **Fins al 2026-10-01, aquesta subsecció deia que els altres setze fitxers eren «pendents d'un pas combinat», i des del juliol no era cert.** La frase es va escriure el 2026-06-19 (`879f3e7`), quan els fitxers encara es deien `PE_Tx` i `PS_Tx`; `614f576` només en va canviar els noms. Les revisions de tema de juliol ja eren A-E-S conjuntes: els nou registres declaren E<x> i S<x> com a abast (`git show a211bbf:TODO/T<x>_P_tasques.md`, al títol o a «Fitxers objectiu»), i els de T6 i T7 diuen literalment «pas combinat E6+S6» i «E7+S7 (adaptació + revisió pròpia)». La declaració de l'usuari i l'historial coincideixen. La skill `/pas-combinat` (`980434b`), feta sobre aquella frase sense preguntar a l'historial, es va retirar amb ella.

Els pendents d'E/S que sobreviuen al tancament són al `TODO.md`: «Exercicis → Problemes», les expressions aritmètiques als operands d'`Ex`/`Sx`, la taula de T1 de `S_criteris_seleccio.qmd` i la terminologia anglesa a la prosa, que és l'antiga «tasca prèvia opcional» d'aquesta subsecció i que, mesurada, no està feta.

#### Laboratori (`L1`–`L6`)

✅ **La revisió interna de laboratori és tancada: `L1.qmd`–`L6.qmd`, tots sis, el 2026-09-23** (declaracions de l'usuari, una per fitxer). El tancament de cadascun, amb l'estat que tenia i què en sobreviu, és a `TODO.md §Entrades retirades`.

Dos avisos que el tancament no esborra, perquè descriuen l'historial i seguiran despistant qui el llegeixi:

- ⚠️ **`ca6c01a` es diu «L6 Fase B» però conté la Fase C sencera**: toca els quatre fitxers que el registre de L6 llistava com a modificats (`L6.qmd`, `A7.qmd`, `13_contrib.qmd` i el registre mateix), i s'hi verifiquen els ítems de Fase C (literals als `.space`, «farciment», l'exercici nou `s6_4_5`, la correcció d'`A7.qmd`). L'assumpte del commit enganya; el contingut, no.
- ⚠️ **`3cae913` és l'únic commit de revisió que ha tocat mai `L4.qmd`**, i el seu assumpte diu que és *previ* a les passades finals. L'usuari les va donar per cobertes en tancar L4.

Detalls transversals i decisions obertes: vegeu `TODO.md`.

### Pla de treball

*Refet el 2026-10-01, sobre l'inventari del grup de treball de T4–T6 (`TODO.md §Decisions obertes → Anotacions de la revisió externa de T4–T6`). Substitueix el pla del matí del mateix dia, en què la línia 1 era «esperar el grup de treball».* Cada fase remet a les entrades del `TODO.md`; el detall, les ordres i els ⛔ són allà. **Una sessió nova per fase o per grup de fases**, amb el model de la columna: aquesta taula és la que ho decideix, no el nom de la tasca.

| Fase | Què | Sessió | Model i effort |
| :---: | :--- | :--- | :--- |
| 1 | **Integració de la revisió externa** (decisions de l'usuari, 2026-10-01). Fusionar `temes456` amb un commit de fusió, sense *rebase*, per conservar l'autoria dels 11 commits, i resoldre els 3 conflictes (`A4.qmd`, `A5.qmd`, `.gitignore`) conservant alhora els canvis dels revisors i les harmonitzacions de `main`. Portar `!5` a `A3.qmd` i `21_riscv/` hunk a hunk, amb `Co-authored-by` de l'autor. **Abans del push, presentar a l'usuari la resolució de cada conflicte i els casos dubtosos del port.** Registrar al `TODO.md` les 10 anotacions [br] i fer `make render-complet`. ✅ **Feta el 2026-10-01**: `temes456` fusionada (`451c3ef`, `40396e8`, `454a82e`), `!5` portada (`ab48732`), anotacions de totes dues registrades i `make render-complet` net. | A | Opus, High |
| 2 | **Harmonitzacions pendents a A3–A6**: tornar a passar totes les escombrades del 2026-10-01 (la branca porta text d'abans): cometes (`A4.qmd:119`), «precisió simple» al material de T5, «l'X següent», amplada dels hexadecimals, tanques i quatre formats a A3. ~~Fixar la regla d'`AND`/`OR` (decisió de l'usuari) i aplicar-la~~ ✅ feta el 2026-10-01 (`13_contrib.qmd §Codi, matemàtiques i cursiva`). ~~Escriure la convenció de l'anotació #4 (algorismes, blocs «Pseudocodi»)~~ ✅ escrita i aplicada als títols el 2026-10-01; la cursiva dels algorismes, a la fase 4. ✅ **Fase feta el 2026-10-01** (`d50b0ba`, `2693ec3`, `f066a8e` i el format U a T2): les escombrades, la regla d'`AND`/`OR`, la convenció #4 i els quatre formats. | A, si hi cap | Opus, Medium–High |
| 3 | **Estructura pedagògica**: anotacions #12 (reordenar §Potència), #9 (temps i rendiment a §Definicions) i #3 (moure `#cau-sobreeiximent-extensio-m`). ✅ **Feta el 2026-10-01** (`4759902`, `457e9cd`, `666835c`): les tres resoltes i els cinc marcadors esborrats; l'ampliació de #12 queda a la fase 6. | B | Opus, High |
| 3b | **Revisió externa de T3** (afegida el 2026-10-02): valorar i resoldre els set comentaris de contingut de Pedro J. Martinez-Ferrer (`TODO.md §Entrades retirades → Executades`, «Anotacions de la revisió externa de T3»). ✅ **Feta el 2026-10-02** (decisions de l'usuari, a proposta de Claude Code; de `fec6d95` a `4a5cad5`): criteri de traduccions literals, «enter»/«natural» amb escombrada i regla a `13_contrib.qmd`, `slli` per a vectors i matrius, «NOT», fusió dels callouts *lazy*, bucles `while` → `do-while` → `for` i `.global` fora de T3. La «↔» (`A3.qmd:322`) queda a la fase 4. | B | Opus, High |
| 4 | **Una sola passada de render** (HTML clar i fosc, i PDF): anotacions #7, #8, #10 i #11, la cursiva dels algorismes al PDF (#4), la «↔» d'`A3.qmd:327` i la figura de `#nte-instruccions-tipus` d'A2, que mostra els set formats en lloc de R, I i S (`TODO.md §T2`). ✅ **Feta el 2026-10-02** (`0d7bd5c`, `e532380`, `70865b6`, `c450782`): #8 verificada sense canvi, #11 partida, cursiva fora (`preamble.tex`), «↔» → «LSb». #7, #10 i la figura d'A2 ja no eren de render: SVG retocats i una variant a `gen_regs.py` (`COMPENDIS`), fets amb Opus per decisió de l'usuari. | B, o una altra | Sonnet, Low–Medium |
| 5 | **Figures** #1 i #2 (*half-adder*, *full-adder*, cadena amb XOR), en SVG natiu segons `24_specs/svg.md`. ✅ **Feta el 2026-10-03** (`e49c014`, `184832c` i el commit de la #2): `#fig-semisumador-sumador-complet` i `#fig-sumador-propagacio-rossec`, generades per `25_scripts/gen_T4_sumador.py`, i la convenció de portes a `svg.md §16`. De pas, decisions de l'usuari: *carry* → «ròssec» a tot el corpus, i «semisumador» i «sumador complet», pendents de confirmar al Termcat. | B, o una altra | Opus, Medium |
| 6 | **Decisions per als revisors**: #5 R4-TYPE, #6 R5-TYPE i l'ampliació de #12. No bloquegen res. ✅ **Feta el 2026-10-02** (decisions de l'usuari, a proposta de Claude Code): #6, no (`1ca023a`); #5, sí, com a aprofundiment (`0fb688a`); ampliació de #12, sí, com a aprofundiment (`99be9b8`). En analitzar #5 es va trobar l'errada de la figura de `#nte-instruccions-tipus` d'A2, que va a la fase 4. | B | Opus, High |
| 7 | **Símbols i Notació** (`12_sigles_simbols.qmd`), després de les fases 1 i 2, perquè llegeix A3–A6. ✅ **Feta el 2026-10-03** (decisions de l'usuari, a proposta de Claude Code; de `a5340f3` a `d61a848`): CPI i la resta de sigles dins de fórmules amb `\text{}`; S6 i E6 amb la notació d'A6 (guany, Amdahl, potència); una sola notació per a la divisió de T4; el glossari verificat contra el corpus (Símbols 100 → 109 files, Notació 17 → 27), i les excepcions de subíndexs i de taules ISA escrites a `13_contrib.qmd`. Toca A3–A6 (notació, i una correcció a A5), cosa que el grup de revisió ha de saber. En van sortir dues entrades del `TODO.md`: «guany» per *speedup* a E6 i S6 (fase 7b), i VPN i PPN a Sigles (decidida el mateix dia, `8e19383`). | C | Opus, High |
| 7b | **Neteja prèvia a la revisió externa de la resta** (afegida el 2026-10-03): tancar els pendents dels fitxers que entraran a la fase 8, perquè cap revisor no hi trobi marcadors ni incoherències. A2: verificar la taula de restriccions d'alineació contra l'ABI `ilp32` (`TODO.md §T2`), unificar el format de les taules de pseudoinstruccions (§Decisions obertes, dos marcadors) i la taula de `#tip-codificacio-instruccions`, que surt del callout al PDF (§T2). E6, S6 i `S_criteris_seleccio.qmd`: «guany» per *speedup* (§Tasques transversals). L2: decidir l'alineació de `.dword` a RARS (§Tasques transversals, amb marcador a `L2.qmd`). Format del codi: aplicar el que decideixi la reunió del grup de treball del 2026-10-05 (consens i alineació dels operands, §Decisions obertes → «Criteris de codi C»). Ja fet el 2026-10-03, abans d'obrir-la: Load/Store/Branch → Lectura/Escriptura/Salt (`9a292eb`), VPN i PPN (`8e19383`) i el *checker* de format amb la indentació (`c27c68a`). ✅ **Feta el 2026-10-03, excepte el format del codi**, que esperava la reunió (decisions de l'usuari, a proposta de Claude Code; de `5684c8a` a `a7876b9`). ✅ **El format del codi, fet el 2026-10-06** (decisió de l'usuari, perquè la reunió no ho va tractar; `0e25c9f` i el commit següent): operands a la columna 16 (F5) al callout `#imp-codi-format-criteris`, el format no s'avalua per si mateix, i 849 línies reformatades a A1–A3, A5, A9, E2–E4, E8, S2, S4, S5 i L2–L6; amb això, **la fase 7b és feta del tot**: la taula d'alineació, correcta, amb l'alineació dels punters i el límit de la relaxació de `sp`; `.dword` a RARS, que només s'alinea a 4 (error d'A2), i L2 amb una sola solució i `.align 3`; `la` amb taula i al compendi; la taula de codificació, dins del callout; «guany» a E6, S6 i `S_criteris_seleccio.qmd`; i el literal de `.dword` d'E2 i S2, que RARS llegia amb signe. Toca A3 i A6 (una frase i una cursiva), cosa que el grup de revisió ha de saber. En surten quatre entrades del `TODO.md`: l'opció B de les pseudoinstruccions, les etiquetes dins dels `#nte-`, la distribució de columnes de totes les taules i `auipc` al compendi. | D | Opus, High |
| 7c | **Figures** (afegida el 2026-10-03): la revisió general de `TODO.md §Tasques transversals` («Revisió general de les figures i generació per script», detallada a `608a71f`: inventari, integració, model de generació, pilot de T7 i figures dinàmiques), amb les pendents de T7 i T8 (§T7, §T8), les taules de memòria de T2 (§Decisions obertes) i el gris del text de figura (§Tasques globals → SVG). ✅ **Feta del 2026-10-03 al 2026-10-06** (decisions de l'usuari 1–13, a proposta de Claude Code; de `1f5f006` a `e806916`, en dotze blocs): inventari de figures pel contingut (`make inventari`), 29 fitxers orfes retirats, generadors al pre-render (`__BA`, `__subrutina`, `__MC`, `__memoria`) i de model (a) amb `--comprova` (`gen_T4_sumador.py`, `gen_T7.py`, `gen_T8.py`), totes les figures de T7 i T8 en SVG natiu, figures dinàmiques a l'HTML, les taules de memòria de T2, text alternatiu des del `<desc>`, una mida comuna a l'HTML i una remissió a cada figura del cos del text. Toca A3–A6 (remissions i, a A3, figures), cosa que el grup de revisió ha de saber. Les entrades executades són a `TODO.md §Entrades retirades → Executades`; en queden dues de noves (les taules de MC de T7 i els avisos de l'inventari) i les que ja hi havia (canvas dels BA, retocs de T3). ✅ **Les dues noves, fetes el 2026-10-06** (decisions de l'usuari D1–D8, a proposta de Claude Code; `d59ae41`, `c7180d9`, `77e6bce` i `42ac228`): les tres taules de MC de T7, de `gen_MC.py` (estil `estat`), amb els originals retirats; els colors fora de la paleta, migrats, i `#e6f1fb` i `#dee2e6`, afegits a `svg.md §10`; les figures de T6, sense `textLength` i amb la notació d'A6; i la resta d'avisos de l'inventari, que ja només llista els originals conservats. Toca SVG de T3–T6 i A2, A7 i A9; declaració de l'usuari (2026-10-06): ara mateix no hi ha cap revisor extern actiu. En surten dues entrades del `TODO.md`: la revisió de la paleta per reduir-ne els colors i el ✓ que no surt al PDF. | E | Opus, High |
| 7d | **Tasques independents dels equips de revisió** (afegida el 2026-10-06, continuació de la 7c, amb les declaracions de l'usuari del mateix dia sobre l'abast A1–A8 i les branques per equip). ✅ **Feta del 2026-10-06 al 2026-10-07** (recomanacions de Claude Code acceptades per l'usuari, i les decisions puntuals que no cobrien; de `82e7c99` a `35be646` i el commit del bloc 5), en sis blocs, un commit cadascun: (0) registre de l'abast i neteja del `TODO.md`; (1) A1–A8, abans que els equips en parteixin: la freqüència de sostre d'A6, com la d'A7 i datada cap al 2003–2005, i `auipc` presentada a A2, amb fragment de `21_riscv/` i taula al compendi (de pas, una errada tècnica d'A3 sobre l'expansió de `la`); (2) render: ✓ i DejaVu Sans Mono al PDF, imatges centrades als callouts, fórmules en línia alineades a l'HTML, marcadors del PDF amb els títols curts i hash del commit a la data; (3) A9, Ex, Sx i Ly: «d'arrencada en fred» en lloc de *cold-start*, la taula de T1 de `S_criteris_seleccio.qmd` i el bloc no autònom deduït a `verifica_laboratoris.py`; (4) les 296 taules del PDF verificades amb una eina nova, `verifica_taules.py`, i 52 corregides; (5) `codi_erroni` a `13_contrib.qmd`, la taula de figures externes (la foto de T7 és CC0 1.0, no CC BY-SA 2.0: `.bib` corregit) i el glossari anglès–català generat (`gen_glossari.py`). Abans de cada bloc que tocava A1–A8, `git ls-remote --heads origin`: cap branca d'equip. Toca A1–A6, A9 i el compendi (taules, `auipc`, la freqüència de sostre), cosa que els equips han de saber. `TODO.md`: 33 → 23 entrades. ✅ **Seguiment del 2026-10-07** (decisions de l'usuari sobre els pendents; `9f8e746` i el commit següent): «lectura/escriptura» per *load/store* a tot el corpus (69 substitucions en 16 fitxers), els glifs que faltaven al PDF (`\newunicodechar`), les marques `codi_erroni` d'A2, una sintaxi pròpia de RISC-V i RARS per als blocs `.s` (`24_specs/riscv.xml`), i la llista de llocs i solucions de l'HTML al mòbil, per decidir. `TODO.md`: 23 → 21. Després, el mateix dia: «Solució» a les referències `@sol-` del PDF, les quatre correccions de l'amplada del mòbil (totes les pàgines a 375 px) i, al glossari, «farciment» i «multinucli» (`TODO.md`: 21 → 20). Queden per decidir *hosted* al glossari i el contingut que va treure la revisió de T4–T6 (amb la informació recollida, al `TODO.md`). | F | Opus, High |
| 8 | **Preparar el material per als equips de revisió d'A1–A8** (declaracions de l'usuari, 2026-10-06: la revisió externa afecta, de moment, A1–A8, «també T3--T6»; A9, Ex, Sx i Ly en queden fora; «Les branches de revisió les crearà cada equip de revisió»). La feina d'aquesta fase és el material, no les branques: una nota per als revisors i l'estat de cada fitxer d'A1–A8. Els equips i el calendari els decideix l'usuari; cada equip crea la seva branca, `revisio/<grup>-t<N>-t<M>` (`13_contrib.qmd §Convenció de noms de branques`). Fins al 2026-10-06 aquesta fila deia «Obrir la revisió externa de la resta: T1, T2 i T7–T9, els enunciats i solucionaris, i el laboratori, amb una branca per grup», amb l'ordre recomanat del 2026-10-03 (T1, T2, E/S i laboratori després de la 7b; T7–T9 després de la 7c). T8 ja és en revisió: `!8`, fusionada el 2026-10-06 fins a §8.7 exclosa. | — | — |

Sense fase pròpia, quan hi hagi ocasió i sense bloquejar res: `#cau-boolea-c` (pendent d'un col·lega) i les eines (protocol de gestió d'errades, taula de referències d'`index.qmd`; `verifica_laboratoris.py` i les figures centrades al PDF, fetes a la fase 7d). Ja fet el 2026-10-01, fora d'A3–A6: les harmonitzacions de la línia 2 de l'antic pla (`TODO.md §Entrades retirades`).

Les fases 1 i 2 van abans que les altres per §Prioritats de la revisió: mentre la revisió de T3–T6 no sigui a `main`, cada canvi que hi entri és un conflicte més. Les eines són a `13_contrib.qmd §IAs` (skill `escombrada`, subagents `auditor-xifres` i `revisor-linguistic`).

### Etiquetes `{#sec-}` a les capçaleres

Totes les capçaleres `##`, `###` i `####` dels fitxers `Ax.qmd` han de tenir un identificador `{#sec-nom}` per ser referenciables amb `@sec-nom`.

**Estat:**
- Tots els fitxers `A1.qmd`–`A9.qmd` tenen les capçaleres etiquetades: **complet**.

**Criteris de generació de l'slug**: vegeu `13_contrib.qmd §Etiquetes `{#sec-}` a les capçaleres`.

### Flux de treball

En començar un xat:

1. Explora el repositori. Si hi ha fitxers als quals no tens accés, demana'ls.
2. Llegeix els fitxers de referència obligatòria (vegeu §Fitxers de referència obligatòria) i la resta de fitxers necessaris per a la tasca.
3. Presenta'm la llista exhaustiva de tasques o problemes que proposes **abans de fer cap canvi**, i digues si cal que canviï el model o l'effortness.
4. Espera confirmació per procedir.
5. En cas de dubte, atura't, exposa el dubte i, si pots, proposa solucions. **Una parada sense el motiu escrit és tan dolenta com no aturar-se**: qui la llegeixi ha de poder decidir sense tornar a fer la feina.

Regles operatives:

- Pots fer canvis d'ordre i crear, reanomenar o eliminar seccions, figures, taules, llistes, etc.
- Interromp l'execució només si tens un dubte que hagi de resoldre l'usuari; mostra-li les opcions disponibles.
- **Un commit per bloc d'instruccions**, i push a cada un: el bloc és la unitat que l'usuari ha confirmat i ha de ser la unitat que es pugui revisar i revertir.
- **Numeració de seccions, figures, taules, equacions i callouts: fins a l'inici de les classes (febrer del 2027) no hi ha cap referència externa als números** (declaració de l'usuari, 2026-10-02). Afegir, moure o treure elements numerats és lliure: les referències `@` s'actualitzen soles i cap material de fora del llibre no en depèn. A partir de llavors, qualsevol canvi que renumeri s'ha d'avisar abans de fer-lo. Dins del repositori, un número escrit a mà sí que caduca (la «eq. 6.8» de l'anotació #12 era `#eq-potencia`): se cita l'etiqueta, no el número.
- **Treballa per àncora de contingut, no per número de línia.** Els números que et doni l'usuari són d'una lectura seva i poden haver-se mogut; si l'àncora no hi és o no coincideix amb el que esperaves, atura't en lloc d'aplicar el canvi a on sembli que toca.
- **Abans d'esborrar o fusionar una secció, registra'n els pendents *i les declaracions de l'usuari*.** Una declaració («tancat de facto», «quasi tancat», «ho dono per bo») **no es verifica: es registra**. No té commit que la sostingui per construcció —demanar-l'hi és com demanar el commit que demostra una decisió—, de manera que descartar-la per «no verificable» n'esborra l'única còpia. El cas: la fusió de les dues seccions d'estat (2026-09-23) va descartar tres declaracions del 2026-07-12 per aquest motiu, i es van haver de recuperar de `git show 397c2da:CLAUDE.md`. Un fet fals es corregeix; una declaració, només qui la va fer la pot retirar.
- Claude Code: pots fer commit i `push` a `origin`, però **només de canvis que l'usuari hagi confirmat explícitament**. Fix-forward sempre: no reescriguis l'historial. L'informe de la feina en curs es publica a cada aturada, perquè la revisió es fa llegint el repositori.
- El mirall de GitHub s'actualitza **automàticament** des de GitLab, amb un parell de minuts de retard. **No s'hi ha d'empènyer a mà** pel remot `mirror`: competiria amb la sincronització. Verificat el 2026-09-21.

### Model i effortness

| Tasca | Model | Effort |
| :--- | :--- | :--- |
| Revisió tècnica o lingüística de teoria | Sonnet | Normal |
| Solucionari (`Sx.qmd`) | Opus | High |
| Tasques operatives (reorganització, neteja de fitxers) | Sonnet | Low |
| Neteja de warnings del render | Sonnet | Low–Medium |
| Classificar diferències amb criteri (moltes decisions independents, cadascuna amb el seu veredicte) | Opus | High |
| Aplicar decisions ja preses i escrites (l'experiència de les passades A, B i C mostra que aplicar **no és mecànic**: l'especificació filtra i afloren judicis que ningú no havia previst) | Opus | High |
| Escombrades del corpus amb un discriminador (`git grep` + veredicte cas a cas, inclosos els contraexemples) | Opus | Medium–High |
| Substitucions mecàniques amb el compte ja verificat (l'abast i la xifra ja són comprovats **abans** de començar; només queda substituir) | Sonnet | Low |

- L'**effort** és la palanca del raonament estès: en aquesta versió de Claude Code **no hi ha cap interruptor de *Thinking* a part**.
- El model es tria per si el criteri ja és escrit **i verificat**, no pel nom de la tasca. I qualsevol configuració, en trobar una cosa que l'especificació no cobreix, **s'atura** en lloc de decidir-la.
- Si la tasca canvia, indica-ho explícitament.
- Si vols que et canviï la configuració, digues-m'ho.

### Figures SVG: política de generació

Política de generació SVG (prioritat, tipus de figures, fonts i colors): vegeu `13_contrib.qmd §Figures i material gràfic`.

Mirror públic del repositori: https://github.com/rbaig/migracio.ec.gitlab.upc.edu
Renderització HTML (pot estar desactualitzada): https://loi.ac.upc.edu/ec