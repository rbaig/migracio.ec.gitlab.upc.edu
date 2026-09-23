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
4. `TODO/TODO.md` — tasques pendents i decisions obertes.

Per a tasques que impliquin figures SVG, llegeix també:

- `24_specs/svg.md` — paleta de colors, mapes de fonts i taula de substitució dark.
- `24_specs/registres.toml` — definicions dels registres de bits (font de veritat).

Repartiment de responsabilitats entre fitxers:

- `13_contrib.qmd` és **el fitxer de referència** del projecte i ha d'estar sempre actualitzat. Hi va qualsevol decisió de format, estil, terminologia o convenció.
- `CLAUDE.md` (aquest fitxer) recull **només** l'operació a claude.ai. Qualsevol altre aspecte va a `13_contrib.qmd`.
- `README.md` és el fitxer de presentació del repositori (documentació habitual d'un projecte Quarto tipus *book*).
- `TODO/TODO.md` només conté contingut transitori; al final ha de quedar buit.

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

Fase actual del projecte. El contingut de teoria (T1–T9), laboratori (L1–L6) i solucionari (S2–S8) ja està generat; ara es fa la **revisió** (tècnica i lingüística), només per l'usuari. La fase següent serà la **revisió externa**, amb altres professors de l'assignatura.

### Prioritats de la revisió

- Prioritats màximes: **coherència pedagògica** i **rigor tècnic** en tot el contingut.
- Revisió tècnica profunda i revisió lingüística en **català normatiu**.
- Solucionaris: detall **pas a pas**, excepte els passos trivials.
- **Harmonització abans de la revisió externa**: «Preparat per a revisió externa» no vol dir tancat a canvis profunds, especialment els d'harmonització (terminologia, estil, convencions transversals). Tot el que es pugui detectar i corregir abans que comenci la revisió externa s'ha de fer ara, encara que impliqui tocar fitxers ja marcats com a preparats: un cop entrin altres professors en la revisió, qualsevol canvi transversal té un cost de coordinació molt més alt. Si detectes una inconsistència que afecta múltiples fitxers (per exemple, terminologia o notació aplicada de manera desigual), proposa'n la correcció sistemàtica encara que surti de l'abast estricte del xat en curs.

### Estat dels materials

*Actualitzat el 2026-09-23. Secció única: hi és fusionada l'antiga §Seqüència de revisió pendent, que duplicava aquesta amb un marcador de progrés per tema.*

El fitxer en curs (WiP) l'indica l'usuari a l'inici de cada xat.

**Com es llegeixen les taules.** Una cel·la pot tenir **tres formes**, i cap d'elles és un veredicte derivat:

1. **Remet a un commit** — certa per sempre, perquè descriu el que aquell commit va declarar.
2. **Remet a l'estat declarat en un fitxer** (els registres de revisió, avui esborrats), amb el punter que el recupera. Sovint és **més precís que l'assumpte del commit**, que ha de cabre en una línia.

   ⚠️ **No citeu cap resum d'un registre: citeu la secció pròpia de l'ítem i comproveu-la al corpus.** Un registre pot portar **diversos resums escrits en moments diferents**, i cap marca no diu quin és vigent —ni el titular, ni l'ordre al fitxer—. El cas (2026-09-23): a `T4_P_tasques.md`, el titular diu «✅ FASE C COMPLETADA + DECISIONS FINALS RESOLTES», la taula «Decisions que resten obertes per a tu» (`:24`) llista els ítems 3, 4.2 i 8 com a pendents, i el resum final (`:312`) diu «no queda cap decisió pendent tret de l'ítem 8». **El vigent és el segon resum**, i el corpus ho confirma: `#wrn-mul-modul-2n` és a `A4.qmd:323` i el punter T4→T7 a `13_contrib.qmd:706`. Citar la taula de dalt hauria registrat com a pendents dues coses fetes des de juliol.
3. **És una declaració de l'usuari** — va a la columna «declaració de tancament», i només ell la pot omplir.

«Fase C executada» **no** vol dir «revisió interna acabada». Entre les dues hi ha les *passades finals* (vegeu `TODO.md §Tasques transversals → Passades finals pendents`), i el tancament es declara per separat per a les tres revisions —**pedagògica, tècnica i lingüística**—, tal com les pregunta `26_prompts/Lx__revisio_interna__plantilla.md`.

⚠️ **Una declaració de l'usuari no es verifica: es registra.** Demanar-li el commit que la sosté és un error de categoria —equival a demanar el commit que demostra una decisió— i esborrar-la per «no verificable» destrueix l'única còpia del que algú va declarar. Val tant per al punt 3 del protocol de sanejament (§Flux de treball) com per a qualsevol fusió de seccions: **abans de treure una secció, se'n registren els pendents i també les declaracions**.

Els commits transversals (auditories i harmonitzacions de setembre: `c2a9171`, `4accc6c`, `b3072a6`, `d017ee2`, `45f6cc2`, `257d37f`…) toquen molts fitxers alhora i **no són passades de revisió d'un tema**: no compten a la columna «passades posteriors».

#### Teoria (T1–T9)

Marc: **preparats per a revisió externa** (`A1.qmd`–`A9.qmd`). Segons §Prioritats de la revisió, això **no** vol dir tancat a canvis, especialment els d'harmonització.

✅ **La revisió interna de teoria és tancada: T1–T9, tots nou, el 2026-09-23** (declaracions de l'usuari, una per tema, al llarg del Bloc 4d). La taula d'estat per tema ja no cal, perquè no hi resta cap tema obert.

El tancament de cada tema —amb l'estat que tenia, el commit que el declarava i què en sobreviu— és a `TODO.md §Entrades retirades`. Quatre casos hi van necessitar una decisió o una execució abans de tancar-se, i el registre en diu el resultat: **T5** (revisió declarada «parcial»: auditats els 29 ítems del seu registre, executats els tres que restaven), **T6** (S6 harmonitzada sencera a $V_{CC}$), **T7** (C3, l'enunciat truncat d'`exr-p7-assoc-multinivell`, reparat contra el PDF original) i **T9** (contradicció entre l'assumpte del commit i el registre, resolta per decisió a favor del registre).

⚠️ **Tancar la revisió d'un tema no tanca el que hi queda registrat.** Els marcadors del corpus, les figures pendents i les decisions obertes **sobreviuen** al tancament i es resolen des de les seves entrades del `TODO.md`, sense reobrir cap tema: els set marcadors d'`A2.qmd`, les figures de T7 i T8, les decisions R4-TYPE i R5-TYPE d'A5, `#cau-boolea-c` d'A3, l'ítem 8 de T4 i la resta.

#### Enunciats (`Ex.qmd`) i Solucionaris (`Sx.qmd`)

- **`E3.qmd` i `S3.qmd`** — revisió interna completada. Encaix T2↔T3 en terminologia caller-saved/callee-saved (vegeu `TODO.md §T3`).
- **La resta de fitxers** (`E1.qmd`–`E2.qmd`, `E4.qmd`–`E9.qmd` i `S1.qmd`–`S2.qmd`, `S4.qmd`–`S9.qmd`) estan pendents d'un **pas combinat**: adaptació als `Ax.qmd` resultants de la revisió interna + revisió interna pròpia. Es fa en un sol xat per fitxer, en ordre temàtic. Tasques vives pendents: vegeu `TODO.md`.
- Tasca prèvia opcional (Claude Code): substitució global de terminologia revisada als fitxers PE/PS abans de la revisió web.

#### Laboratori (`L1`–`L6`)

✅ **La revisió interna de laboratori és tancada: `L1.qmd`–`L6.qmd`, tots sis, el 2026-09-23** (declaracions de l'usuari, una per fitxer). El tancament de cadascun, amb l'estat que tenia i què en sobreviu, és a `TODO.md §Entrades retirades`.

Dos avisos que el tancament no esborra, perquè descriuen l'historial i seguiran despistant qui el llegeixi:

- ⚠️ **`ca6c01a` es diu «L6 Fase B» però conté la Fase C sencera**: toca els quatre fitxers que el registre de L6 llistava com a modificats (`L6.qmd`, `A7.qmd`, `13_contrib.qmd` i el registre mateix), i s'hi verifiquen els ítems de Fase C (literals als `.space`, «farciment», l'exercici nou `s6_4_5`, la correcció d'`A7.qmd`). L'assumpte del commit enganya; el contingut, no.
- ⚠️ **`3cae913` és l'únic commit de revisió que ha tocat mai `L4.qmd`**, i el seu assumpte diu que és *previ* a les passades finals. L'usuari les va donar per cobertes en tancar L4.

Detalls transversals i decisions obertes: vegeu `TODO.md`.

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