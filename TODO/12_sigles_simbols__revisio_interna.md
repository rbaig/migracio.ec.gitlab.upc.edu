Nom d'aquest xat: `12_sigles_simbols — Revisió creuada de Símbols i Notació`

Objectiu d'aquest xat: revisar i completar sistemàticament les taules `## Símbols`
i `## Notació` de `12_sigles_simbols.qmd` contra el contingut real de **tots**
els temes (T1–T9), corregint qualsevol discrepància trobada.

## Origen i motiu d'aquest xat

Durant un xat anterior (revisió interna de T8, i posteriorment una tasca puntual
de completar `## Símbols`/`## Notació` amb el contingut de T8), en verificar els
símbols compartits amb T7 es van trobar **diverses discrepàncies greus i
sistemàtiques** entre el que deia la taula i l'ús real del símbol a `A7.qmd`:

| Símbol | La taula deia | Ús real verificat a `A7.qmd` |
| :---: | :--- | :--- |
| $A$ | Grau d'associativitat | Adreça (de la dada a la memòria principal) |
| $D$ | Nombre de conjunts (*directori*) de la memòria cau | Bit de modificació (*dirty bit*) |
| $N$ | Nombre de conjunts | Grau d'associativitat (nombre de vies) |
| $N_C$, $N_L$ | Fusionats en una sola entrada («nombre de conjunts / de línies») | Conceptes diferents: $N_C$ = nombre de conjunts, $N_L$ = nombre de línies totals |
| $w$ | Nombre de bits de l'etiqueta (*tag*) | Nombre de bits d'una adreça (l'etiqueta és $w - n_c - b$, sense símbol propi) |
| $b$ | «T7, T8» (compartit) | Només T7 (mida de bloc). A T8 el desplaçament de pàgina és $t$, no $b$ |

Totes verificades amb `grep` directe contra el text de `A7.qmd` i corregides
**només per als símbols que es van creuar amb T8**. **Cap altre tema (T1–T6,
T9) s'ha verificat encara.** És molt probable que hi hagi discrepàncies
similars en símbols d'altres temes que ningú ha contrastat sistemàticament
contra el text real des que es va crear la taula.

**Hipòtesi de treball per a aquest xat**: la taula `## Símbols` es va omplir en
algun moment (probablement per extracció ràpida o de memòria) sense verificar
cada entrada contra el text font de cada `Ax.qmd`. Cal fer-ho ara,
sistemàticament, tema per tema.

## Com obtenir els fitxers

El repositori és públic a `raw.githubusercontent.com/rbaig/migracio.ec.gitlab.upc.edu/main/...`.
Vés-los a buscar tu mateix amb `bash_tool`/`curl` en el moment que et calguin,
no els demanis com a adjunt ni els llegeixis tots per endavant.

**Nomenclatura actual del repositori** (verificada 2026-07-13; pot haver canviat,
comprova-ho primer si trobes 404):
- Teoria: `01_apunts/A1.qmd`–`A9.qmd`
- Enunciats: `02_exercicis/E1.qmd`–`E9.qmd`
- Solucions: `03_solucions/S1.qmd`–`S9.qmd` (S1 no existeix), `S_criteris_seleccio.qmd`
- Operacionals: `CLAUDE.md`, `13_contrib.qmd`, `TODO/TODO.md`
- Sigles/símbols/notació: `12_sigles_simbols.qmd`
- Especificacions SVG: `24_specs/svg.md`
- **Excepció coneguda**: si algun `curl` retorna 404 amb aquesta nomenclatura,
  el repositori pot haver-se reestructurat de nou (ja ha passat un cop en
  aquest projecte); si és així, llista l'arrel via
  `https://github.com/rbaig/migracio.ec.gitlab.upc.edu` (pàgina HTML, no
  `api.github.com`, que pateix rate-limit fàcilment sense autenticació) per
  trobar la nomenclatura vigent abans de continuar.

## Aspecte a revisar

Per a **cada tema T1–T9**, per a cada símbol/variable de fórmula que hi
aparegui:

1. Localitza totes les ocurrències del símbol al text real de `Ax.qmd`
   (i, si cal per desfer ambigüitats, també `Ex.qmd`/`Sx.qmd`).
2. Compara el significat real amb el que diu (o no diu) la taula `## Símbols`
   de `12_sigles_simbols.qmd`.
3. Si hi ha discrepància, error, fusió indeguda de dos símbols diferents, o
   una entrada absent: proposa la correcció.
4. Si un mateix símbol té significats diferents en temes diferents **o dins
   del mateix tema** (cas real trobat amb $n_c$ a T7: nombre de cicles en
   contextos de rendiment vs. nombre de bits d'índex de conjunt en contextos
   d'organització de la MC), documenta-ho a la columna «Observacions», no
   ho amaguis fusionant-ho.
5. Fes el mateix, de manera més lleugera, per a la taula `## Notació`
   (operadors i convencions transversals: `<<`, `>>`, `>>>`, `\lfloor \cdot \rfloor`,
   `\bmod`, etc. — comprova si en falta cap d'ús freqüent i inequívoc a tot
   el llibre).

**No cal tocar res més** dels fitxers `Ax.qmd`/`Ex.qmd`/`Sx.qmd` en aquest
xat: l'abast és exclusivament `12_sigles_simbols.qmd`, llevat que en el procés
de verificació trobis un error de contingut clar al tema mateix (com l'ordre
de magnitud d'A8 en un xat anterior); en aquest cas, anota-ho a part i
demana'm si el vols corregir aquí o en un xat dedicat a aquell tema.

## Criteri de contingut (extret de `13_contrib.qmd`, citat literalment)

> **`## Símbols`**: glossari de variables/paràmetres d'equacions (símbol →
> concepte que representa), **contextual per tema**. Un mateix símbol pot
> tenir significats diferents segons on s'usi (p. ex. $m$ és la mantissa a T5
> però la taxa de fallades a T7): en aquest cas s'indica a la columna
> «Observacions». Columnes: `Símbol | Significat | Tema | Observacions`.
> Ordenació: alfabètica pel símbol/nom de variable.
>
> **`## Notació`**: operadors i convencions de representació
> **transversals**, estables amb independència del tema (p. ex. $\oplus$,
> $>>>$, $\lfloor\cdot\rfloor$). Columnes: `Notació | Significat` (sense
> columna de tema). Ordenació: per categoria funcional (operadors
> lògics/bit a bit, desplaçaments, funcions...), no alfabètica.
>
> **Criteri de distinció**: si el signe es "llegeix" com una magnitud amb nom
> i valor contextual → Símbols. Si es "llegeix" com una operació o convenció
> de representació → Notació.
>
> **Sigles que també apareixen com a variable d'equació** (p. ex. CPI): doble
> entrada — definició completa a `## Sigles`, entrada curta amb remissió
> («Vegeu CPI a Sigles») a `## Símbols`. Criteri: si la sigla apareix dins
> d'una fórmula matemàtica (no només en prosa), guanya entrada també a
> Símbols.

**Ordre alfabètic**: el patró ja establert a la taula és: lletra minúscula
sola, després totes les seves variants amb subíndex (per ordre alfabètic del
subíndex), després la mateixa lletra en majúscula i les seves variants amb
subíndex, abans de passar a la lletra següent (p. ex. `n, n_A, n_c, n_l,
n_cicles, n_dat/n_ins, N, N_C, N_L` — comprovat i corregit en el xat anterior).

## Regla transversal sobre correccions

Si detectes una inconsistència que afecta múltiples fitxers o temes, proposa'n
la correcció sistemàtica encara que surti de l'abast estricte d'aquest xat
(criteri de `CLAUDE.md §Prioritats de la revisió`).

## Model i effortness

- **Fase d'exploració i verificació creuada (extracció dels símbols reals de
  cada `Ax.qmd`, contrast amb la taula, detecció de discrepàncies)**:
  **Fable 5 High amb Thinking**. Motiu: cal llegir i retenir amb precisió el
  significat exacte de desenes de símbols a través de 9 fitxers de teoria
  llargs, i el cost d'un error de lectura (com els trobats: $D$↔$N_C$,
  $N$↔$N_C$) és alt perquè es propaga silenciosament a un document de
  referència que tothom consultarà. Aquest tipus d'error és exactament el que
  Thinking ajuda a evitar (verificació pas a pas contra el text citat, no per
  record).
- **Fase d'execució (escriure les correccions finals a la taula, un cop
  identificades)**: es pot baixar a **Sonnet High, sense Thinking** — és
  edició mecànica de taules Markdown a partir d'un llistat de correccions ja
  decidides.
- Indica'm explícitament, en començar cada fase, quina configuració esperes
  que tingui activa, seguint la mateixa regla transversal dels altres xats
  d'aquest projecte: si detectes que la configuració activa no és l'adequada
  per a la feina següent, atura't i digues-m'ho abans de continuar.

## Estat de partida (contingut ja verificat i corregit; no cal repetir-ho)

La taula ja reflecteix correctament, verificat contra `A7.qmd` i `A8.qmd`:

- Tots els símbols creuats T7/T8: $a$, $A$, $b$, $B$, $C$, $D$, $n$, $n_c$,
  $n_l$, $N$, $N_C$, $N_L$, $p$, $t$, $T$, $V$, $w$.
- La taula `## Notació` té `<<`, `>>`, `>>>`, $\lfloor \cdot \rfloor$, $\bmod$.

**Pendent de verificar** (no tocat encara, cap garantia que sigui correcte):
tots els símbols exclusius de T1, T2, T3, T4, T5, T6 i T9 que no s'hagin
creuat casualment amb T7/T8 — és a dir, la major part de la taula actual.
Símbols especialment sospitosos per revisar amb prioritat (per la seva
similitud notacional amb els errors ja trobats, típica font de confusió
símbol↔concepte relacionat): $CPI$/$CPI_i$/$C_i$, $f_B$/$f_{clock}$,
$K$, $m$/$m_d$/$m_i$/$m_{L1}$/$m_{L2}$, $P$/$P_d$/$P_s$/$P_x$,
$s_{max}$/$s_x$, $V_{CC}$/$V_{in}$/$V_t$ (tots de T6, tema no verificat en
cap dels xats anteriors).

## Fitxer de referència

L'estat actual de `12_sigles_simbols.qmd` (amb els símbols T7/T8 ja corregits)
és a l'adjunt d'aquest xat.
