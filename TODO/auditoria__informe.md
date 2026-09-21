# Auditoria — informe de la sessió 1 (mesurar)

Fitxer **transitori**. S'esborra en tancar l'auditoria.

Sessió 2026-09-21. Model: Opus 5. Base: `5b7e396` (tancament del bloc 3 de la
passada C).

**Aquesta sessió no canvia res del corpus.** L'única escriptura és aquest
fitxer. Tot el que s'hi proposa va a la sessió 2.

## Regles aplicades

Heretades de `recuperacio_diff__informe.md §Regles vigents` i de
`decisions__informe.md §Regla d'escombrada` i `§Regla de protocol`:

1. Tota escombrada amb `git grep`, mai amb `grep -r`. `git grep` només veu
   fitxers versionats: cobreix els `.qmd` de l'arrel i `21_riscv/`, i exclou
   `auto_riscv/` (generat) i `_book/`.
2. `git grep -c` compta **línies**; per a ocurrències, `-o … | wc -l`.
3. Pathspec `':!TODO/'` a tota escombrada, o la mesura s'inclou a si mateixa.
4. Tota afirmació «és l'únic» / «no n'hi ha cap» va amb l'ordre que la sosté.
5. Abans de concloure sobre un bloc, llegir-lo sencer; abans de concloure que
   una línia és per a l'alumne, comprovar que no és dins d'un comentari HTML.

---

# 1a — Els comentaris: 38 casos en 10 fitxers

## Verificació del compte

```bash
git grep -n "TODO\|Cal decidir\|Reactivar" -- '*.qmd' ':!TODO/' | wc -l    # 38
git grep -o "TODO\|Cal decidir\|Reactivar" -- '*.qmd' ':!TODO/' | wc -l    # 46
git grep -c "TODO\|Cal decidir\|Reactivar" -- '*.qmd' ':!TODO/'
```

**38 línies confirmades**, 46 ocurrències (8 línies en duen més d'una).
Distribució: A1×1, A2×10, A3×2, A4×2, A5×2, A7×2,
`S_criteris_seleccio`×1, L2×2, `13_contrib`×9, `index.qmd`×7.

## Ampliació del patró — no aporta res

```bash
git grep -nI -e "FIXME" -e "XXX" -e "PENDENT" -e "REVISAR" -e "PROVISIONAL" \
  -e "Cal veure" -e "per decidir" -e "a decidir" -- '*.qmd' ':!TODO/'
```

**Cap `FIXME`, `XXX`, `PENDENT`, `REVISAR` ni `PROVISIONAL` a tot el corpus.**
Els 5 resultats de «per decidir» són prosa normal (A1:211, A3:1902, A3:2089,
A4:167, A9:760): descriuen què decideix el compilador o l'ABI, no pendents.
Igualment «provisional» (adreces provisionals de reubicació, A3 i S3) i
«pendent» (`13_contrib.qmd:166`, que **sí** compta i ja surt als 38).

**El patró original és complet.** No cal ampliar-lo.

## Un ajust de categoria abans de la taula

L'enunciat proposava tres categories. La lectura cas a cas n'exigeix una
quarta, perquè 10 dels 38 no són ni decisions ni notes de progrés:

- **(4) FALS POSITIU**: la paraula «TODO» hi surt com a **metavariable de la
  convenció** (`#nte-TODO`, `#tbl-TODO`) o com a **remissió al `TODO.md`**.
  No és cap pendent. Esborrar-los seria un error.

Comptar-los com a pendents inflava la xifra en un 26 %.

## Classificació dels 38

Llegenda: **(1)** decisió viva no registrada · **(2)** comentari obsolet que
contradiu una decisió presa · **(3)** nota de progrés caduca · **(4)** fals
positiu.

### `01_apunts/A1.qmd`

| Línia | Cat. | Contingut | Què n'ha de passar |
| :--- | :---: | :--- | :--- |
| 39 | **2** | `<!-- TODO reactivar si al final startup.s exception handler -->` + el paràgraf comentat de `:40` sobre l'emulació de `__start` | **Eliminar tots dos** (comentari i paràgraf). La decisió del 19/07 exclou el mecanisme; «reactivar-lo» contradiu la resolució. Vegeu §1b. |

### `01_apunts/A2.qmd` — 10 casos

| Línia | Cat. | Contingut | Què n'ha de passar |
| :--- | :---: | :--- | :--- |
| 578 | **3** | `<!-- TODO Roger unificar format taules pseudoinstruccions -->` (dins `#nte-pseudoinstruccio-la`) | 🔁 **DUPLICAT — instància canònica.** Nota de progrés adreçada a una persona. **Decisió de l'usuari**: o fer la unificació i esborrar-lo, o passar-lo al `TODO.md` com a tasca transversal. No pot quedar-se al corpus. |
| 603 | **3** | Íd., dins `#imp-ec-la-offset` | 🔁 **DUPLICAT de `:578`.** Mateix text literal. El `TODO.md` n'ha de tenir **una** entrada, amb les dues ubicacions com a llista. |
| 686 | **1** | `<!-- TODO hi ha consens? -->`, just abans de `#imp-codi-format-criteris` | **Decisió viva no registrada**: pregunta si els criteris de format de codi tenen consens entre professors. Candidata a `TODO.md §Decisions obertes`, i encaixa amb l'entrada oberta «Criteris de codi C: completar». |
| 687 | **1** | `<!-- TODO Miquel: podríem fer un checker -->` | **Proposta viva d'eina** (verificador de format de codi), adreçada a un professor. Va a `TODO.md`, no al corpus. Relacionada amb `25_scripts/verifica_laboratoris.py`, que ja existeix. |
| 744 | **2** | `<!-- TODO(startup.s) Reactivar si es manté l'esquelet específic d'EC amb startup.s. Si es manté, corregir abans: _start (no __start), li a7, 93 (no a7, 10). -->` | **Contradiu la decisió del 19/07.** Eliminar amb tot el bloc comentat `:745-810`. Vegeu §1b. |
| 810 | **2** | `--- TODO -->` — **tancament** del bloc comentat obert a `:745` | Desapareix amb el bloc. Nota: la grafia `--- TODO -->` és un tancament de comentari mal format (tres guions en lloc de dos), i el comptador el registra com a cas propi. |
| 988 | **3** | `<!-- TODO substituir la taula següent per un diagrama de memòria estàndard. -->` | 🔁 **DUPLICAT — instància canònica.** Pendent **de figura**, no de decisió. El `TODO.md` ja té secció de figures pendents (`§T7`, `§T8`); això n'és una de T2 que no hi consta. Migrar-lo. |
| 1026 | **3** | `<!-- TODO passar a figura de memòria estàndard -->` (dins `#tip-endianness`) | 🔁 **DUPLICAT de `:988`.** Mateixa tasca sobre una altra taula (`#fig-big-endian`/`#fig-little-endian`). Una entrada al `TODO.md` amb les dues ubicacions. |
| 1080 | **1** | `<!-- TODO: Verificar que la informació de la taula és correcta i coincideix amb l'ABI ilp32 i que no hi ha col·lisió amb l'ABI RV de Bloc d'Activació alineació a 16 -->` | **Verificació tècnica viva i no registrada**, sobre `#nte-restriccions-alineacio` — la taula que la Fase C de L2 va corregir. Afecta rigor tècnic: va al `TODO.md` amb prioritat, no s'esborra. |
| 1720 | **3** | `<!-- TODO afegir ref a secció concreta -->` (§Absència de control en l'accés a memòria, punt 2 de la llista) | Pendent menor de referència creuada. Es pot resoldre a la sessió 2 si es troba el destí; si no, al `TODO.md`. |

### `01_apunts/A3.qmd`

| Línia | Cat. | Contingut | Què n'ha de passar |
| :--- | :---: | :--- | :--- |
| 244 | **1** | `<!-- TODO Adrià: tu has proposat "unes expressions" (abans era "les expressions"); cal indicar com es poden identificar les que sí i les que no -->` | **Decisió de contingut viva**, no registrada enlloc. El text de `#cau-boolea-c` diu «unes expressions no nul·les s'interpreten com a certes» sense dir quines: el pendent és real i afecta el rigor. Va al `TODO.md §T3`. |
| 1541 | **2** | `<!-- TODO(startup.s) Reactivar … (vegeu imp-exception-handler a T2). -->` + bloc comentat `:1542-1549` (`#tip-rars-main-multinivell`) | **Bessó d'A2:744.** Eliminar comentari i bloc. Vegeu §1b. |

### `01_apunts/A4.qmd`

| Línia | Cat. | Contingut | Què n'ha de passar |
| :--- | :---: | :--- | :--- |
| 80 | **3** | `<!-- TODO: Afegir la figura d'un half-adder i la d'un full-adder -->` | Figura pendent de T4. **No consta al `TODO.md`**, que només té seccions de figures per a T7, T8 i T9. Migrar. |
| 81 | **1** | `<!-- TODO: Afegir la figura de la seqüència de full-adders amb la porta XOR per detectar el sobreeiximent en el darrer? -->` | El signe d'interrogació el fa **decisió**, no tasca: cal decidir si la figura s'ha de fer. Migrar com a decisió oberta de T4. |

### `01_apunts/A5.qmd`

| Línia | Cat. | Contingut | Què n'ha de passar |
| :--- | :---: | :--- | :--- |
| 5 | **1** | `<!-- TODO: cal introduir el R4-TYPE? (Harris) -->` | **Decisió d'abast de contingut** no registrada: si T5 ha d'introduir el format R4. Rellevant, perquè `24_specs/registres.toml` ja genera `T5_instruccio_tipus_R4` (citat a `TODO.md §T5 F1`). Va a `TODO.md §T5`. |
| 6 | **1** | `<!-- TODO: com a "aprofundiment" R5-TYPE (RISC-V compressed) per a la codificació de les instruccions? Al principi de T2? -->` | Íd. — decisió d'abast que **creua dos temes** (T5 i T2). Va a `TODO.md`, com a decisió oberta transversal. |

Nota: totes dues són **abans del `# {{< var tema5 >}}`**, a la capçalera del
fitxer, fora de cap secció. Fàcils de perdre de vista.

### `01_apunts/A7.qmd`

| Línia | Cat. | Contingut | Què n'ha de passar |
| :--- | :---: | :--- | :--- |
| 476 | **3** | `<!-- TODO fig-lru-roger: diagrama d'estats -->` | **Ja consta al `TODO.md §T7`** («`fig-lru-roger` · Màquina d'estats LRU · Ja inclosa dins `T7_lru_exemple.svg`; decidir si cal figura independent»). El comentari és **redundant** amb el registre: es pot eliminar del corpus sense perdre res. |
| 480 | **4** | «…i la còpia a la memòria principal divergeixen. **Cal decidir** com i quan sincronitzar-les.» | **Fals positiu**: prosa didàctica viva, renderitzada. «Cal decidir» hi és com a subjecte del disseny de la memòria cau, no com a marcador. **No tocar.** |

### `03_solucions/S_criteris_seleccio.qmd`

| Línia | Cat. | Contingut | Què n'ha de passar |
| :--- | :---: | :--- | :--- |
| 19 | **3** | `TODO (taula pendent de completar amb la resta de solucions de S1.qmd)` | ⚠️ **L'únic «TODO» del corpus que és text de contingut destinat a l'alumne** (no comentari HTML, no metavariable). Vegeu el matís de sota: ara mateix no arriba a l'HTML perquè el fitxer és comentat a `_quarto.yml`, però el `CLAUDE.md` diu que els fitxers comentats formen part del projecte. **Prioritat alta**: substituir-lo per una nota neutra o per res, i registrar la tasca al `TODO.md`. |

**Matís verificat, i canvia la urgència.** `S_criteris_seleccio.qmd` **no
es renderitza ara mateix**: és comentat a `_quarto.yml:94-95`
(`# - text: "Criteris de selecció"`). Ordres:

```bash
grep -n "S_criteris" index.qmd _quarto.yml     # només _quarto.yml:95, comentat
grep -rc "TODO" _book/03_solucions/*.html      # cap resultat
ls _book/03_solucions/                         # S1..S9, cap S_criteris
```

Per tant **el «TODO» no és avui al llibre publicat**. Però `CLAUDE.md §Volum`
diu que «tots els fitxers `.qmd` d'`index.qmd` formen part del projecte,
encara que estiguin comentats (es comenten per escurçar el temps de
renderització en proves)». Quan es descomenti, el «TODO» sortirà imprès. És
un pendent real, no una falsa alarma — i el fet que **el `_book/` no el
detecti és precisament per què l'escombrada s'ha de fer sobre el font**.

### `04_laboratori/L2.qmd` — el cas pur

| Línia | Cat. | Contingut | Què n'ha de passar |
| :--- | :---: | :--- | :--- |
| 156 | **1** | Obertura de `<!-- TODO Alineació de long long a RARS` (bloc `:156-166`) | Vegeu la fila següent: és el mateix cas. |
| 162 | **1** | «Cal decidir quina versió presentar als alumnes i si s'ha d'afegir una nota sobre aquest comportament. De moment es presenten les dues versions.» | **Decisió viva.** Estava amagada en un comentari fins que es va **registrar el 2026-09-20** a `TODO.md §Tasques transversals` («`L2.qmd:163` — TODO en comentari sobre l'alineació de `.dword` a RARS»). El pendent, doncs, **no és anotar-la sinó resoldre-la**. ⚠️ Vegeu l'avís de sota sobre `:164-166`. |

> ⚠️ **El bolcat comparatiu MARS/RARS de `L2.qmd:164-166` no existeix enlloc
> més.** Si la sessió 2 elimina aquell comentari, **aquelles dues línies de
> dades s'han de preservar** — al `TODO.md`, a l'entrada de la decisió.
> Ordre que ho sosté:
>
> ```bash
> git grep -n "fea800fb" -- . ':!TODO/auditoria__informe.md'
> ```
>
> És el tipus de pèrdua que portem tres dies reparant: dades mesurades
> empíricament que només viuen dins d'un comentari destinat a desaparèixer.
> No és prosa reconstruïble — és un bolcat de dos simuladors.

### `13_contrib.qmd` — 9 casos, **tots falsos positius**

| Línia | Cat. | Contingut | Què n'ha de passar |
| :--- | :---: | :--- | :--- |
| 17 | **4** | «Per a tasques pendents i decisions obertes, vegeu `TODO/TODO.md`.» | Remissió. **No tocar.** |
| 166 | **4** | «…**pendent** una decisió transversal sobre si convertir-les a «Lectura/Escriptura/Salt» (vegeu `TODO.md §T6`)» | Convenció vigent que **remet correctament** al registre. Consta a `TODO.md §T6`. **No tocar** (però la decisió de fons sí que és viva: vegeu la llista final). |
| 410 | **4** | «Noms d'etiquetes `#nte-TODO`, `@sec-callouts`» | Metavariable dins la convenció de format codi. **No tocar.** |
| 419 | **4** | «Tots han d'anar etiquetats (p. ex. `::: {#nte-TODO .callout-note}`). Cal substituir el `TODO` per una cadena única.» | **És la definició de la metavariable.** No tocar. |
| 561 | **4** | «…vegeu `TODO/TODO.md §Tasques transversals`. No l'«arregleu» canviant la taula.» | Remissió, i **verificada**: `§Tasques transversals` existeix al `TODO.md` (línia 15) i hi conté l'entrada de la figura Graphviz de T7. **No tocar.** |
| 629 | **4** | `: Caption opcional {#tbl-TODO …}` | Metavariable dins l'exemple de taula. **No tocar.** |
| 632 | **4** | «La referència és `@tbl-TODO`.» | Íd. **No tocar.** |
| 703 | **4** | «T5 → T9: `fcsr` → `@nte-zicsr` (vegeu `TODO.md §T5 P8`)» | Remissió, i **verificada**: `§T5` existeix (línia 63) i hi conté l'entrada «**P8** — `fcsr` té dependència cap endavant amb `@nte-zicsr` (T9)». **No tocar.** |
| 817 | **4** | «Abans de fer commit, assegureu-vos que no hi ha cap etiqueta `-TODO` ni cap `TODO` que pugueu solucionar…» | **És la regla que aquesta auditoria està executant.** No tocar. |

**Comprovació de remissions penjades** (via 5 de detecció del mode 2,
avançada aquí perquè aquest bloc la demanava): les tres remissions de
`13_contrib.qmd` a seccions del `TODO.md` (`§Tasques transversals`, `§T6`,
`§T5 P8`) **apunten totes a seccions existents**. Ordre:
`grep -n "^#\+ " TODO/TODO.md`. Cap remissió penjada. Vegeu §1d per a
l'escombrada completa.

### `index.qmd` — 7 casos

| Línia | Cat. | Contingut | Què n'ha de passar |
| :--- | :---: | :--- | :--- |
| 147 | **2** | `<!-- TODO(startup.s) Reactivar … -->` + bloc `:148-151` (descàrrega de `startup.s`) | Eliminar comentari i bloc. Vegeu §1b. |
| 160 | **2** | `<!-- TODO(startup.s) Reactivar secció sencera … -->` + bloc `:161-167` (*Settings → Exception Handler*) | Íd. Vegeu §1b. |
| 209 | **1** | `<!-- TODO Determinar versió la ISO de C? -->` | 🔁 **DUPLICAT — instància canònica del grup `:209-212`.** Decisió viva **ja registrada**: `TODO.md §index.qmd` diu «Pendent encara: versió ISO de C i versió GCC (marcades amb `<!-- TODO -->`…)». Ara la taula ja cita `[@iso9899_2024]`, de manera que el pendent és **verificar i tancar**, no decidir de zero. |
| 210 | **1** | `<!-- TODO La ISO de C és tancada? -->` | 🔁 **DUPLICAT de `:209`.** La mateixa decisió (quina norma ISO de C es pren com a referència), formulada com a pregunta diferent. |
| 211 | **1** | `<!-- TODO GCC cal especificar millor -->` | 🔁 **DUPLICAT de `:209`** en el seu abast: la mateixa taula, fila del compilador (`[@gcc16]`). Registrat conjuntament al `TODO.md`. |
| 212 | **1** | `<!-- TODO Consolidar noms, versions, etc. de tot -->` | 🔁 **DUPLICAT de `:209`** — n'és la formulació genèrica («tot» = les files de la taula). Al `TODO.md` hi ha d'anar **una** entrada per a les quatre. |
| 213 | **1** | `<!-- TODO Versió numèrica de CSR o de data a la resta -->` | ✅ **NO és duplicat: categoria 1 de debò.** **No consta al `TODO.md`** — l'entrada registrada només parla d'ISO de C i GCC. Aquest afecta la fila de RISC-V (`[@riscv_csrs]`) i demana una cosa diferent: si la referència s'identifica per número de versió o per data. |

## Recompte de 1a

| Categoria | Casos |
| :--- | ---: |
| (1) Decisió viva no registrada (o registrada a mitges) | 14 |
| (2) Comentari obsolet que contradiu una decisió presa | 6 |
| (3) Nota de progrés caduca | 8 |
| (4) Fals positiu — no tocar | 10 |
| **Total** | **38** |

Els 10 falsos positius són els **9 de `13_contrib.qmd`** (totes les seves
ocurrències: metavariables, remissions i la regla de commit) i
**`A7.qmd:480`** (prosa didàctica). `S_criteris_seleccio.qmd:19` **no** ho
és: és contingut de llibre mal posat, encara que el fitxer estigui
temporalment desactivat.

Recompte verificat comptant les files de les taules d'aquest apartat: 38
files, 14 + 6 + 8 + 10.

## Tres troballes de 1a que no eren a l'encàrrec

1. **`S_criteris_seleccio.qmd:19` és l'únic «TODO» escrit com a contingut**,
   no com a comentari ni com a metavariable. Els altres 37 són dins de
   comentaris HTML o són part de la convenció. No arriba a l'alumne avui
   només perquè el fitxer és comentat a `_quarto.yml` — cosa que el
   `CLAUDE.md` declara temporal.
2. **Quatre pendents d'`index.qmd` són el mateix pendent** escrit quatre
   vegades (`:209-212`, canònica `:209`), i un cinquè (`:213`, versions de
   CSR) **no consta enlloc** — aquest sí que és categoria 1 pura.
3. **A2 duplica dos pendents**: figura de memòria (`:988` canònica, `:1026`
   duplicat) i format de taules de pseudoinstruccions (`:578` canònica,
   `:603` duplicat).

**Conseqüència per a la sessió 3.** Els duplicats són marcats amb 🔁 a la
classificació, amb la instància canònica indicada. La reescriptura del
`TODO.md` els ha de **col·lapsar a una entrada cadascun**, amb les ubicacions
com a llista — no arrossegar-ne quatre.

**Recompte de pendents distints:**

| Pas | Casos |
| :--- | ---: |
| Línies trobades | 38 |
| − falsos positius (cat. 4) | −10 |
| = pendents | 28 |
| − línies duplicades (`:603`, `:1026`, `:210`, `:211`, `:212`) | −5 |
| **= pendents distints per al `TODO.md`** | **23** |

Més `A2.qmd:810`, que no és un pendent propi sinó el **tancament** del bloc
comentat de `:745`: desapareix amb ell. Els pendents distints reals són,
doncs, **22 entrades** més la neteja de `startup.s` de §1b.

---

# 1b — `startup.s`: inventari complet

**Decisió de referència** (`TODO/TODO.md:7` i `:115`, 2026-07-19, presa amb
tots els professors): s'exclou totalment el mecanisme `startup.s` / `main` com
a punt d'entrada; es manté `_start`, amb sortida via `li a7, 93` + `ecall`.
**Mai executada.**

## Escombrada base

```bash
git grep -n "startup" -- . ':!TODO/'      # 16 línies, 5 fitxers
git grep -c "startup" -- . ':!TODO/'      # A1:1 A2:6 A3:4 13_contrib:1 index:4
```

Sense filtre d'extensió i sense filtre de directori: cobreix `21_riscv/` i
qualsevol fitxer versionat. **Cap ocurrència fora d'aquests 5 fitxers.**

## Comentari HTML o contingut viu

Determinat programàticament (cerca de parelles `<!--` … `-->` i comprovació de
si l'offset de cada línia hi cau dins), no per inspecció visual:

| Fitxer:línia | Estat | Bloc comentat |
| :--- | :--- | :--- |
| `A1.qmd:39` | COMENTARI | `39-39` (el marcador mateix) |
| `A2.qmd:744` | COMENTARI | `744-744` (el marcador) |
| `A2.qmd:770` | COMENTARI | **`745-810`** |
| `A2.qmd:774` | COMENTARI | `745-810` |
| `A2.qmd:778` | COMENTARI | `745-810` |
| `A2.qmd:780` | COMENTARI | `745-810` |
| `A2.qmd:795` | COMENTARI | `745-810` |
| `A3.qmd:1541` | COMENTARI | `1541-1541` (el marcador) |
| `A3.qmd:1546` | COMENTARI | **`1542-1550`** |
| **`A3.qmd:2050`** | **VIU** | — |
| **`A3.qmd:2052`** | **VIU** | — |
| **`13_contrib.qmd:205`** | **VIU** | — |
| `index.qmd:147` | COMENTARI | `147-147` (el marcador) |
| `index.qmd:149` | COMENTARI | **`148-151`** |
| `index.qmd:160` | COMENTARI | **`160-167`** |
| `index.qmd:165` | COMENTARI | `160-167` |

**13 de 16 són dins de comentaris HTML. Només 3 són contingut viu**, i són
exactament els tres que l'encàrrec assenyalava: els dos a jutjar i el registre
de la decisió. **Cap traça viva inesperada per la via de la paraula
«startup».** (Per una traça viva que aquesta escombrada **no** veu, vegeu
§Troballa nova, més avall.)

## El fitxer `startup.s` de RARS vs. una altra cosa

| Ocurrència | Què anomena |
| :--- | :--- |
| `A1.qmd:39` | El fitxer de RARS (marcador) |
| `A2.qmd:744, 770, 774, 778, 780, 795` | El fitxer de RARS — `:780` n'és el **codi sencer** en un bloc `{.s filename="startup.s"}` |
| `A3.qmd:1541, 1546` | El fitxer de RARS |
| **`A3.qmd:2050, 2052`** | **Una altra cosa**: la rutina de *startup* d'un executable real de UNIX/Linux. En cursiva, no en codi, i sense `.s`. |
| `13_contrib.qmd:205` | El fitxer de RARS — **en negatiu**: «No es fa servir `startup.s`» |
| `index.qmd:147, 149, 160, 165` | El fitxer de RARS (descàrrega i configuració de l'*Exception Handler*) |

## Els quatre blocs a eliminar

| Fitxer | Línies | Què conté |
| :--- | :--- | :--- |
| `A1.qmd` | `39-40` | Marcador + paràgraf sobre l'emulació de `__start` |
| `A2.qmd` | `744-810` | Marcador + `#imp-programa-esquelet` + `#imp-exception-handler` + `#wrn-so-start` (66 línies, el gruix del mecanisme) |
| `A3.qmd` | `1541-1550` | Marcador + `#tip-rars-main-multinivell` |
| `index.qmd` | `147-151` i `160-167` | Descàrrega del fitxer + secció «Configuració inicial» |

Coincideix **exactament** amb l'enumeració del `TODO.md:7`, que ja preveia
aquests quatre llocs. **Res que el registre no previngués.**

⚠️ **Avís sobre `A2.qmd:744-810`.** Aquest bloc conté l'única exposició del
corpus del flux `_start` → `main` → `exit` → `_exit` i la taula de les tres
primeres instruccions amb el codi màquina (`:799-801`). Unicitat verificada:

```bash
git grep -n "_exit\|libc" -- '*.qmd' ':!TODO/'        # A2:806 i A3:2076 (libc.a, altre tema)
git grep -n "00c000ef\|0x00a00893" -- . ':!TODO/'     # només A2:799 i A2:800
```

Està **comentat**, de
manera que no és al llibre; però abans d'eliminar-lo cal decidir si alguna
part té valor pedagògic independent del mecanisme exclòs. El meu judici:
**no** — descriu el mecanisme `startup.s` de cap a peus, i `A3.qmd:2043-2052`
ja explica el mateix concepte (carregador → rutina de startup → `main` →
`exit`) de manera general i correcta. Però és una eliminació de 66 línies i
va amb confirmació explícita.

## Els dos casos a jutjar

### `A3.qmd:2050-2052` — la descripció del carregador real

Context llegit sencer (`§Càrrega en memòria`, `A3.qmd:2043-2052`): és la
llista dels cinc passos que fa el **carregador de UNIX/Linux** en posar un
executable en memòria. El pas 5 diu que salta a «una rutina de *startup* dins
l'executable, la qual copia els paràmetres `argc` i `argv` … i fa una crida a
`main`», i el paràgraf final que en tornar `main`, aquella rutina invoca
`exit`.

**Veredicte: es queda. No té relació amb el `startup.s` de RARS.**

- Diu «*startup*» en cursiva (terme genèric), no `startup.s` en codi.
- Parla d'`argc`/`argv`, que el `startup.s` de RARS no toca.
- Descriu un **sistema real amb SO**, que és justament el contrari del
  supòsit d'EC (`#imp-directe-sobre-processador`).
- La secció sencera és sobre UNIX/Linux: el paràgraf d'entrada ho diu
  explícitament («En el cas de UNIX/Linux segueix els passos següents»).

**Retoc proposat, però: sí, i n'hi ha prou amb una frase.** El risc real no és
que l'alumne confongui aquesta rutina amb el fitxer de RARS —que ja no
existirà al corpus—, sinó que **suposi que els seus programes d'EC arrenquen
així**, amb `main` i amb `argc`/`argv`. El text no ho desmenteix enlloc.

**Redacció proposada** (aprovada la forma per l'usuari; la redacció concreta,
a confirmar abans d'aplicar). Callout nou després de `A3.qmd:2052`:

```markdown
::: {#cau-carrega-ec .callout-caution}
El mecanisme descrit en aquesta secció és el d'un **sistema real amb SO**. A
**EC** no hi ha ni SO ni carregador (@imp-directe-sobre-processador): els
programes no reben `argc` ni `argv`, no s'inicien per una crida a `main` i no
tornen enlloc en acabar. El punt d'entrada és `_start` i la sortida es fa amb
`li a7, 93` + `ecall` (@nte-programa-esquelet).
:::
```

**Per què aquesta forma i no una frase solta.** És el patró de
`#cau-void-main` (`A2.qmd:2028`, afegit al bloc 3a): un `callout-caution` que
davant d'un contingut que **no val a EC** diu les dues meitats —què val en un
sistema normal i què val aquí— en lloc de només negar. La comparació:

| | `#cau-void-main` (A2) | `#cau-carrega-ec` (proposat) |
| :--- | :--- | :--- |
| Contingut que matisa | C amb `void main()` | Càrrega amb `main`/`argc`/`argv` |
| Raó a EC | no es compila, no hi ha SO que en reculli el retorn | no hi ha SO ni carregador |
| Referència a la convenció | `@imp-directe-sobre-processador` | íd. + `@nte-programa-esquelet` |
| Reconeix l'altra meitat | «En un programa de C normal … cal `int main`» | «El mecanisme … és el d'un sistema real amb SO» |

**Tres decisions de redacció, per si les vols canviar:**

1. **Enumera què no rep l'alumne** (`argc`, `argv`, crida a `main`, retorn) en
   lloc de dir-ho en general. És el que evita la suposició concreta que ens
   preocupa.
2. **No cita `startup.s`.** Quan això s'apliqui, el mot ja no existirà al
   corpus fora de `13_contrib.qmd:205`; anomenar-lo aquí el ressuscitaria.
3. **Va després del paràgraf de `:2052`**, no abans de la llista: la llista
   s'ha de poder llegir sencera com el que és, la descripció d'un sistema
   real. L'slug segueix el criteri de `13_contrib.qmd` (`cau-` + tema).

### `13_contrib.qmd:205` — el registre de la decisió

Text: «**Sortida del programa**: `li a7, 93` + `ecall` (syscall `exit2`). No
es fa servir `startup.s`.»

**Veredicte: es queda, intacte.** És a `§Convencions globals del laboratori`,
i la frase és **el perquè** de la convenció de sortida. Esborrar-la deixaria
`li a7, 93` sense motiu escrit, i el projecte ja ha pagat aquest preu: el
`fcvt.w.s` de la passada A mostra què passa quan una convenció perd la seva
justificació.

Un matís que la sessió 2 ha de tenir present: quan els quatre blocs
desapareguin, aquesta serà **l'única menció de `startup.s` a tot el corpus**, i
l'alumne que la llegeixi no tindrà cap context del que es nega. Dues sortides:
deixar-la com és (el destinatari de `13_contrib.qmd` és el professorat, no
l'alumne, i per a ell la frase és informativa) o reformular-la com a decisió
datada. **Recomanació: deixar-la com és** — `13_contrib.qmd` és el fitxer de
convencions i la seva funció és precisament registrar què no es fa.

## Troballa nova — una traça viva que l'escombrada de «startup» no veu

`A2.qmd:709-720`, dins `#tip-codi-bones-practiques` (**contingut viu**,
renderitzat), és aquest bloc:

```
.text
.globl  main
main:
        add t0, a0, a1
        ret
```

És **la forma exacta que la decisió exclou**: `main` com a punt d'entrada,
declarat `.globl`, amb sortida per `ret` en lloc d'`ecall`. I és al callout
que el corpus presenta com a **model de bones pràctiques de format**.

Com s'ha trobat: `git grep -n "\.globl" -- '*.qmd' ':!TODO/'`, que no conté la
paraula «startup». **L'escombrada per la paraula no bastava.**

### Escombrada sistemàtica de `main` com a punt d'entrada

```bash
git grep -n "^main:" -- '*.qmd' ':!TODO/'          # 7
git grep -n "\.globl" -- '*.qmd' ':!TODO/'         # 44 línies
```

Els 7 `main:` classificats un a un, llegint-ne el bloc sencer:

| Ocurrència | Veredicte |
| :--- | :--- |
| **`A2.qmd:718-719`** | ⚠️ **TRAÇA VIVA.** `.globl main` + `main:` + `ret` a `#tip-codi-bones-practiques`. Vegeu sota. |
| `A2.qmd:763-765` | Dins del bloc comentat `745-810`. Desapareix amb ell. |
| `A2.qmd:2052` | ✅ Traducció del `void main()` del C de sobre (`#tip-vector-acces-aleatori`). |
| `A2.qmd:2103` | ✅ Íd. (recorregut per punter). |
| `A3.qmd:1205` | ✅ Traducció del `void main()` de `:1196`. |
| `S3.qmd:501` | ✅ «Traducció de `main`» — l'exercici demana traduir un `main` de C. |
| `S4.qmd:388` | ✅ Íd. |

Els sis casos ✅ són **notació de C traduïda a mà**, exactament la meitat
esquerra de la regla del bloc 2b (`void main()` quan el C és notació). No són
el mecanisme d'entrada de RARS i **no s'han de tocar**.

**`.globl`**: de les 44 línies, 2 són `.globl main` (`A2:718` viu, `A2:763`
comentat), 40 són `.globl _start` o `.globl <subrutina>` als laboratoris i a
A2/A3, i 2 són prosa de `13_contrib.qmd:118` i `21_riscv/RARS_directives.qmd`.
**Tot el laboratori (L1–L6) és `_start`**: cap desviació.

### ⭐ La regla que se'n deriva — val per a tota l'auditoria

> **Quan s'exclou un MECANISME, no n'hi ha prou d'escombrar-ne el NOM; cal
> enumerar-ne les formes sintàctiques.**

`startup.s` no apareixia enlloc d'aquell bloc i la traça hi era sencera:
`.globl main` / `main:` / `ret`. L'escombrada per la paraula donava 16
ocurrències i un panorama tranquil; la traça que de debò contradiu la decisió
al llibre publicat no en tenia cap.

**I el context ho empitjora**: `#tip-codi-bones-practiques` acaba a `:723` i
`### Esquelet d'un programa {#sec-esquelet-programa}` comença a `:726`. El
llibre presenta com a **model de bones pràctiques** el mecanisme que exclou,
**tres línies abans d'ensenyar el bo** (`#nte-programa-esquelet`, `:730`).

Corol·lari per a la resta de l'auditoria: les escombrades de 1c i 1d no es
poden limitar als noms que els registres citen. Cada decisió executada s'ha
de comprovar per les **formes** que produeix al codi.

### Judici sobre `A2.qmd:718-719`

**No és eliminable sense més**, perquè el bloc no il·lustra el punt d'entrada:
il·lustra **la indentació** (directives a columna 0, instruccions tabulades).
La correcció mínima que el posa d'acord amb la convenció és substituir les
dues línies per `.globl _start` / `_start:` i acabar amb la sortida canònica
en lloc de `ret`.

**RESOLT (veredicte de l'usuari): convergir amb la forma canònica d'`A1`.**
No és invenció sinó harmonització: `A1.qmd:204-208` ja té exactament aquest
exemple, i és el primer codi d'assemblador del llibre.

```
# A1.qmd:205-208 — la forma canònica
suma:
    add a0, a0, a1    # Instrucció de l'ISA: a0 <- a0 + a1
    ret               # Pseudoinstrucció: retorna el control al cridant
```

Canvi a aplicar a `A2.qmd:717-721`, **tres línies, no dues**:

| Línia | Actual | Proposat |
| ---: | :--- | :--- |
| 718 | `.globl  main` | `.globl  suma` |
| 719 | `main:` | `suma:` |
| 720 | `        add t0, a0, a1` | `        add a0, a0, a1` |

**El tercer canvi no és cosmètic i sense ell el rename seria deshonest.** Una
subrutina que rep els arguments a `a0`/`a1` i deixa el resultat a `t0` **no
retorna res**: el `ret` la tornaria al cridant amb `a0` intacte. El bloc
passaria de mostrar un mecanisme dolent a mostrar una subrutina incorrecta —
canviaríem un error per un altre. Amb `add a0, a0, a1` el bloc és consistent
amb l'ABI, amb el `ret` que ja té i amb `A1.qmd:205-208`.

El bloc conserva el que il·lustra (la indentació: directives a columna 0,
instruccions tabulades) i deixa de prometre res sobre el punt d'entrada.

## `li a7, 10` — inventari

La mateixa decisió mana unificar a `li a7, 93`.

```bash
git grep -n "a7, *10\|a7,10" -- '*.qmd' ':!TODO/'      # 5 línies
git grep -o "a7, *10\b" -- '*.qmd' ':!TODO/' | wc -l   # 5
git grep -niI "syscall .*10\|servei 10\|número 10" -- '*.qmd' ':!TODO/'
```

**Confirmat l'enunciat, i n'hi ha més.** Els de codi són els 3 anunciats
(A9, E9, S9) més el del bloc comentat d'A2; però l'escombrada de prosa en
destapa 3 més que no són instruccions.

| Ocurrència | Estat | Veredicte |
| :--- | :--- | :--- |
| `A2.qmd:744` | Comentari (marcador) | Desapareix amb el marcador. |
| `A2.qmd:800` | Comentari (bloc `745-810`) | Desapareix amb el bloc. |
| **`A9.qmd:575`** | **VIU** — `li a7, 10 # codi de exit` | ⚠️ **A jutjar, no substituir.** Vegeu sota. |
| **`E9.qmd:72`** | **VIU** — «sortida amb `li a7, 10` + `ecall`» | ❌ **Error clar.** Diu «les convencions del curs» i cita la que **no** ho és. Substituir per `li a7, 93`. |
| **`S9.qmd:201`** | **VIU** — `li a7, 10 # codi: exit` | A jutjar amb A9: és la solució de l'exercici paral·lel. |

**Ocurrències en prosa i taules, que l'escombrada de `a7, 10` no veu:**

| Ocurrència | Contingut | Veredicte |
| :--- | :--- | :--- |
| `A2.qmd:804, 806` | «`a7 = 10` activa la syscall `exit` (número 10)» | Dins el bloc comentat. Desapareixen amb ell. |
| **`A9.qmd:527`** | «RARS … estableix dos codis de servei per a sortir del programa, `exit` (codi de servei 10) i `exit2` (codi de servei 93). La diferència és que `exit2` permet especificar el codi de sortida…» | ✅ **Es queda.** És **documentació de RARS**, no una convenció d'EC, i explica per què EC tria `exit2`. |
| **`21_riscv/RARS_syscall_codis.qmd:7`** | Fila `\| 10 \| exit \| — \| — \|` de la taula de codis de RARS | ✅ **Es queda.** És la taula de referència de les syscalls de RARS: si RARS en té 10, la taula l'ha de llistar. |

### El judici sobre `A9.qmd:575` i `S9.qmd:201`

Tots dos són **exemples del servei `exit`**, no esquelets de programa:

- `A9.qmd:575` és dins d'una llista d'exemples de `ecall` («Finalitzar el
  programa (codi 10)»), al costat de `print_string` (codi 4) i altres. És
  l'**exemplificació del servei 10** que `:527` acaba de presentar.
- `S9.qmd:201` és l'apartat **d)** de `sol-p9-syscall-serveis`, la solució de
  l'exercici que demana «d) Finalitzar el programa» — i el seu enunciat
  (`E9.qmd:62`) **no fixa cap codi**, a diferència de `:72`.

**RESOLT — veredicte de l'usuari, que separa els dos casos.** La meva
proposta els tractava igual; l'usuari hi discrepa en part i té raó, perquè el
paper dels dos blocs al fitxer és diferent.

| Cas | Veredicte | Raó |
| :--- | :--- | :--- |
| **`A9.qmd:575`** | **Es queda, amb una addició** | És una entrada d'un **catàleg de serveis** (codi 1, codi 5, codi 4, codi 10), no un esquelet. El servei 10 existeix i el catàleg l'ha de documentar. Però l'entrada **ha de dir que a EC la sortida es fa amb `li a7, 93`** (`exit2`): tal com està, l'alumne que llegeixi T9 n'aprèn a sortir amb 10, i **cap altre lloc del corpus no ho fa**. |
| **`S9.qmd:201`** | **→ `li a7, 93`** | Forma **parella enunciat/solució** amb `E9.qmd:72`. L'enunciat demana finalitzar el programa i la convenció del curs governa els programes que escriu l'alumne. Que l'enunciat no fixi codi **no el deixa fora: el deixa dins per defecte.** |
| **`E9.qmd:72`** | **→ `li a7, 93`** | Error clar: **afirma** una convenció («les convencions del curs») i en cita la que no ho és. |

El criteri que els separa: **catàleg de referència vs. programa que l'alumne
escriu**. `A9:575` documenta què ofereix RARS; `S9:201` és codi que l'alumne
prendrà com a model. Mateix criteri que deixa viure `A9:527` i
`21_riscv/RARS_syscall_codis.qmd:7`.

Nota d'execució per a la sessió 2: el pas a `li a7, 93` a `S9.qmd:201` demana
afegir-hi `li a0, 0` (el codi de sortida), perquè `exit2` el pren de `a0` —
vegeu `@nte-programa-esquelet`. Cal comprovar què fa l'`E9` corresponent.

Comprovació de l'altra banda:
`git grep -o "a7, *93" -- '*.qmd' ':!TODO/' | wc -l` → **32 ocurrències** en 9
fitxers (A2×3, A9×1, L1×5, L2×4, L3×5, L4×3, L5×3, L6×6, `13_contrib`×2). La
forma canònica és majoritària 32 a 3 al corpus viu.

## Resum de 1b

| Element | Compte |
| :--- | ---: |
| Mencions de `startup` | 16 |
| — dins de comentaris HTML | 13 |
| — contingut viu | 3 (els 2 a jutjar + el registre) |
| Blocs comentats a eliminar | 4 (en 4 fitxers) |
| Traces vives del mecanisme **sense** la paraula «startup» | **1** (`A2.qmd:718-719`) |
| `li a7, 10` en codi viu | 3 (A9, E9, S9) |
| — a substituir per `93` | **2** (`E9.qmd:72`, `S9.qmd:201`) |
| — es queda, amb addició sobre la convenció d'EC | 1 (`A9.qmd:575`) |
| Mencions del servei 10 en prosa/taules, legítimes | 2 (`A9:527`, `RARS_syscall_codis.qmd:7`) |

**La lliçó metodològica del bloc**: l'escombrada per la paraula clau
(`startup`) donava 16 ocurrències i un panorama tranquil —13 comentades, 3
vives i totes tres previstes. La traça que de debò contradiu la decisió al
llibre publicat (`A2.qmd:718-719`) **no conté la paraula**. S'ha trobat
escombrant el **mecanisme** (`.globl`, `^main:`), no el nom. És el mateix
error que la passada C va documentar a 1a amb `11_riscv.qmd`, en una altra
dimensió: allà s'escapava un **directori**, aquí s'escapa un **sinònim**.

---

# 1c — Els registres `Tx` contra el repositori

Registres comprovats: `T1_P`, `T2_P`, `T3_P`, `T4_P`, `T5_P`, `T6_P`, `T7_P`,
`T8_P`, `T9_P`, `L1`–`L6_tasques`, `L2`–`L6__revisio_interna`.

**Mètode**: per a cada tasca amb una afirmació **verificable amb una ordre**
(un text que hi ha de ser o no hi ha de ser, un identificador, un fitxer), s'ha
executat l'ordre. Les tasques de judici («reformulat», «millorat») no es poden
verificar així i queden fora. Es presenten **només les discrepàncies**, com
demana l'encàrrec.

Nota metodològica: els meus dos primers greps de T2.3 i T3/T01 van donar «cap
resultat» i **eren falsos negatius meus**: buscava `sll t6, %idx` i
`srai t0, t0, 2` amb espais, i el corpus indenta amb tabulacions. Les dues
tasques estaven aplicades. Ho anoto perquè és el mode de fallada típic
d'aquesta comprovació: **un grep massa literal fabrica discrepàncies que no
existeixen**, i en una auditoria això és tan dolent com no veure-les.

## Verificat correcte (mostra, no exhaustiu)

| Registre | Tasca | Comprovació | Resultat |
| :--- | :--- | :--- | :--- |
| T1 | Ref. `@wrn-codificacio-enters-ca1` → `@sec-enters-en-ca1` a A3:48 | `git grep -n "wrn-codificacio-enters-ca1"` | ✅ cap; A3:48 usa l'slug bo, definit a A1:582 |
| T2 | 1 — recompte RV32I 41→40 | `git grep -n "Nombre d'instruccions" -- 01_apunts/A2.qmd` | ✅ `:151` diu **40** |
| T2 | 2 — typo `imm12$` | `git grep -n 'imm12\$'` | ✅ cap |
| T2 | 3 — `sll`→`slli` a `zero_elem` | `sed -n '650p' 01_apunts/A2.qmd` | ✅ `slli t6, %idx, 2` |
| T2 | 4 — «load half/byte **unsigned**» | `grep -n "load half\|load byte" 21_riscv/RV32I_instruccions_lectura_escriptura.qmd` | ✅ `lhu`/`lbu` correctes |
| T2 | 6 — includes `mv`/`li` | `git grep -n "RV32I_pseudo_mv\|RV32I_pseudo_li"` | ✅ A2:543,559 + `13_contrib:85-86` actualitzat |
| T3 | T01 — `sra`→`srai` | `sed -n '105,108p' 01_apunts/A3.qmd` | ✅ `srai t0, t0, 2` |
| T3 | T02 — `andi … 0x800`→`-2048` | `sed -n '162,164p' 01_apunts/A3.qmd` | ✅ `andi t0, t1, -2048` |
| T3 | T03 — ordre de `jalr` | `cat 21_riscv/RV32I_instruccions_salt_incondicional_indirecte.qmd` | ✅ $PC \leftarrow …; rd \leftarrow PC_{ant}+4$ |
| T3 | T04 — «set **les** than» ×4 | `git grep -n "set les than" -- . ':!TODO/'` | ✅ cap |
| T3 | T11 — TODO de l'ABI al BA | `git grep -n "Verificar que ho diu l'ABI"` | ✅ cap; A3:1379 diu «Per conveni —i com a criteri seguit a EC—» |
| T4 | 5.1 — «No obstant,» | `git grep -n "No obstant,"` | ✅ cap |
| T4 | 5.2 — `***stride***` | `git grep -n "stride" -- 01_apunts/A4.qmd` | ✅ A4:678 en triple asterisc |
| T4 | 5.4 — «razonable» a `svg.md` | `git grep -n "razonable" -- . ':!TODO/'` | ✅ cap |
| T6 | A1 — «per unitat de temps» | `git grep -n "energia dissipada" -- 01_apunts/A6.qmd` | ✅ A6:262 |
| T6 | A6 — «Km/h», «Joules» | `git grep -n "Km/h\|Joules"` | ✅ cap |
| T6 | A11/A12 — «la única», «els ràtios» | `git grep -n "la única\|els ràtios\|dels ràtios"` | ✅ cap |
| T6 | A14/A23 — hardware→maquinari | `git grep -niI "hardware"` | ✅ cap en prosa tret d'`13_contrib:189` (vegeu D5) |
| T6 | A21 — «1.350» | `git grep -n "1\.350" -- 03_solucions/S6.qmd` | ✅ cap |

**Els registres són fiables.** A diferència del `startup.s`, el que donen per
fet hi és. Les discrepàncies que segueixen són **cinc**, i cap no és una tasca
declarada feta que no s'hagi fet: són **notes de registre que el repositori ha
deixat enrere**.

## D1 🔴 — Tres registres diuen que la regla de `_start` és «pendent d'aplicar a L3». Ja no ho és.

**Afirmació als registres** (tres llocs, dos d'ells de contingut):

| Lloc | Text |
| :--- | :--- |
| `13_contrib.qmd:204` | «Aplicat a L4, L5 i L6, verificat empíricament amb RARS 1.6; **pendent d'aplicar a L3**.» |
| `TODO/TODO.md:115` | «**Pendent**: L3 (`s3_4_2` amb `moda`; `s3_5_1` amb `codifica`/`g`) té subrutines abans de `_start` → mateixa fallada d'execució» |
| `TODO/L5_tasques.md:99` | «La regla encara no s'ha afegit a `13_contrib.qmd` … supeditada a completar també la revisió de L3.» |

**Estat real del repositori**: els **5 blocs de `L3.qmd` amb `_start` compleixen
la regla**. Verificat programàticament, no a ull: per a cada bloc de codi, es
localitza `.text` i es comprova quina és la primera etiqueta que el segueix.

```
L3 bloc  65-78 : primera etiqueta després de .text = _start:   OK
L3 bloc 116-168: _start:   OK
L3 bloc 207-233: _start:   OK
L3 bloc 358-445: _start:   OK        <- s3_4_2.s, el que els registres citen
L3 bloc 491-552: _start:   OK        <- s3_5_1.s, l'altre que citen
```

Els dos blocs que `TODO.md:115` anomena explícitament (`s3_4_2` i `s3_5_1`)
són precisament dos dels que compleixen. `L3:358-380` té `_start:` immediatament
després de `.text` i `moda:` a sota.

**Per què**: el commit `b6c8124` (2026-09-20) va reordenar `_start` al bloc
`#exr-depuracio`, i la resta ja ho complia. L'informe de recuperació ho
documenta (`§Verificació final`), però **les tres notes no es van actualitzar**.

**Conseqüència**: la regla de `_start` **ja es pot consolidar a
`13_contrib.qmd`**, que era l'acció que els tres registres deixaven supeditada
a L3. Ara mateix `13_contrib.qmd:204` conté la regla **i** la nota que diu que
encara no s'ha acabat d'aplicar — es contradiu a si mateixa.

⚠️ **Matís que la sessió 2 no pot passar per alt**: «complir la regla d'ordre»
**no** vol dir que `L3:357` (`s3_4_2.s`) estigui resolt. L'informe de
recuperació explica que aquell bloc segueix sent l'únic `ERROR E1` del
verificador, i que deixa de ser-ho *com a comprovació estàtica d'ordre* però
continua sent un bloc no autònom per disseny. Són dues coses diferents i les
notes les barregen. Vegeu D4.

## D2 🟠 — `TODO.md` dona per oberta la decisió de les plantilles Markdown. Ja està executada.

`TODO/TODO.md:11` (`§Decisions obertes`):

> **Plantilles Markdown** (`L2.qmd` i resta): posar-ne a tots excepte `L2.qmd`,
> o eliminar de `L2.qmd`?

**Resolta i executada** per la decisió D3 de `decisions__informe.md`
(commit `733b408`): es van eliminar els tres blocs `.markdown` de L2.

```bash
git grep -n '```{.markdown' -- '*.qmd' ':!TODO/'    # cap
```

L'entrada s'ha de retirar de `§Decisions obertes` a la sessió 3.

## D3 🟠 — `TODO.md §Laboratori` dona per pendent el forat de contingut de L2. Ja està omplert.

`TODO/TODO.md:105`:

> **L2 §«Pseudoinstrucció `la` i `li`»**: el cos de la secció és només «TODO»;
> redactar-ne el contingut o eliminar la secció.

**Resolt** per la Fase C de la recuperació (hunk L2-7, commit de la passada A):
`L2.qmd:350` i següents tenen la secció redactada, amb el callout
`#cau-rars-la-offset`. Ordre: `sed -n '350,356p' 04_laboratori/L2.qmd`.

## D4 🟠 — `TODO.md` descriu la tasca d'expressions als operands com si A4 fos l'únic pendent. L6 ja està net; A4 no s'ha tocat gens.

`TODO/TODO.md:114` diu: «**Pendent**: `A4.qmd` (…) i `L6.qmd` (≈8 ocurrències
de `.space N*4` i similars amb `.eqv`)».

| Fitxer | Estat real | Ordre |
| :--- | :--- | :--- |
| `L6.qmd` | ✅ **Net.** Cap `.space` amb expressió. L'única menció és `L6:525`, que dona el literal `.space 256` ja calculat. | `git grep -n "\.space .*\*" -- 04_laboratori/L6.qmd` |
| `A4.qmd` | ❌ **Intacte: 20 línies** amb `NF*NC*4`, `li tX, NC*4`, `NC*2`, `la t3, mat + 5*4`, `mat + 3*NC*4`… | `git grep -c "NC\*4\|NC\*2\|NF\*NC\|mat + [0-9]" -- 01_apunts/A4.qmd` → 20 |
| `S4.qmd` | ❌ **Afectat i no citat al registre**: `S4.qmd:258` té `li t2, NC*4`. | `git grep -ln "NC\*4\|NC\*2" -- '*.qmd' ':!TODO/'` → A2, A4, S4, L4 |

**I la mitigació mínima que el registre preveia tampoc no s'ha fet.** El
`TODO.md` deia: «si es mantenen simbòlics, com a mínim cal remetre a
`@nte-rars-operands-literals`».

```bash
git grep -n "nte-rars-operands-literals" -- '*.qmd' ':!TODO/'
```

→ **2 resultats**: la definició (`A2.qmd:451`) i **una sola remissió**
(`L4.qmd:94`). **Cap des d'A4 ni des de S4.** L'alumne que copiï el patró
d'A4 escriurà codi que RARS rebutja, i el corpus no l'avisa enlloc.

**Gravetat**: el `TODO.md` mateix classifica això com a **error real verificat
empíricament** («el material afectat no assembla o no s'executa»), no com a
millora. És la discrepància de més impacte de 1c.

## D5 🟡 — `13_contrib.qmd:189` infringeix la seva pròpia taula de substitució

`13_contrib.qmd:303` fixa «hardware / HW → **maquinari** (terme preferent)»; i
`13_contrib.qmd:189` (secció T9) diu:

> L'ajust (`mepc + 4`) és responsabilitat de la RSE, no **del hardware**.

Ordre que ho sosté i que en mostra l'abast:

```bash
git grep -niI "software\|el hardware\|del hardware" -- '*.qmd' ':!TODO/' \
  | grep -v "\*hardware\*\|\*software\*\|hardware page-table\|flux-hardware\|eq-sobre\|hardware / HW"
```

→ **2 resultats**, i l'altre (`A8.qmd:240`, «*software-managed TLB*») és un
**terme tècnic propi en cursiva**, correcte. `13_contrib.qmd:189` és l'única
infracció real del corpus. Correcció d'una paraula.

És menor, però simptomàtic: el fitxer que fixa la convenció és l'únic que la
incompleix, i cap escombrada de T6 el va tocar perquè T6 només mirava A6/E6/S6.

## Pendents heretats confirmats com a **encara oberts** (no són discrepàncies)

Verificats perquè els registres els deixaven explícitament oberts:

| Origen | Pendent | Estat verificat |
| :--- | :--- | :--- |
| `T4 §8` | Dos `<!-- TODO -->` de figures a `#wrn-sobreeiximent-maquinari` | ✅ Oberts — són `A4.qmd:80-81` de §1a |
| `T4 §8` | `22_figs_originals/T4_multiplicador_sequencial.png` al costat del `.svg` | ✅ **El `.png` hi és** (63 KB). Decisió d'eliminar-lo, pendent |
| `T4 §8` | Slug genèric `{#sec-casos-especials}` | ✅ Obert; ara **sí que es referencia** (`S4.qmd:228` fa `@sec-casos-especials`), o sigui que reanomenar-lo ja no és gratuït |
| `T3 T34` | TODO d'Adrià a `#cau-boolea-c` | ✅ Obert — és `A3.qmd:244` de §1a |
| `T6 C6` | Etiquetes Load/Store/Branch en anglès | ✅ Obert i correctament registrat a `TODO.md §T6` i `13_contrib.qmd:166` |
| `T6 D2` | $V^2$ (A7) vs. $V_{CC}^2$ (A6) a la potència dinàmica | ⚠️ **No verificat en aquesta sessió** — requereix llegir les dues fórmules senceres; va a la llista de la sessió 2 |

## Resum de 1c

| Discrepància | Gravetat | Naturalesa |
| :--- | :---: | :--- |
| **D1** — `_start` a L3 «pendent» quan ja està fet (3 llocs) | 🔴 | Nota desfasada; **bloqueja** la consolidació de la regla |
| **D2** — Plantilles Markdown «decisió oberta» quan està executada | 🟠 | Entrada caduca |
| **D3** — Forat de `la`/`li` a L2 «pendent» quan està omplert | 🟠 | Entrada caduca |
| **D4** — Expressions als operands: L6 net, **A4 i S4 intactes i sense remissió** | 🔴 | **Feina real no feta**, amb error tècnic verificat |
| **D5** — `13_contrib.qmd:189` infringeix la seva pròpia taula | 🟡 | Una paraula |

**Cap tasca declarada feta que no s'hagi fet.** El mode de fallada d'aquests
registres no és el del `startup.s` (una decisió presa i mai executada), sinó
el contrari: **el repositori ha avançat i les notes no ho han seguit**. Tres
de les cinc (D1, D2, D3) diuen «pendent» d'una cosa ja resolta, i això té un
cost real: D1 **bloqueja** una consolidació que ja es podria fer.

La quarta (D4) sí que és feina pendent de debò, i és la que el `TODO.md`
qualifica d'error verificat empíricament.

---

# 1d — El segon mode de fallada: cerca de més casos

**Resultat, primer**: s'han executat les sis vies sobre els **273 commits** de
l'historial sencer. **No s'ha trobat cap cas nou de mode 2.** El CAS 1
(`4f973d5`) segueix sent l'únic, i el CAS 2 (`7f0703c`) ja consta reparat.

Això no és una absència d'evidència: és evidència d'absència, i sota quines
ordres es va buscar, que és el que l'informe ha de deixar escrit.

## Abast

```bash
git log --oneline | wc -l          # 273 commits (1d57f8d, 27/04 → c295b8b, 21/09)
git log --format=%H c5d9416..HEAD | wc -l   # 90 posteriors al refactor de l'11/07
```

Les vies 1, 2 i 6 s'han executat **dues vegades**: sobre l'historial sencer i
restringides a l'època post-refactor (`c5d9416`, 2026-07-11), que és quan
comença la revisió interna i on una pèrdua encara tindria valor. Els commits
anteriors al refactor treballen amb noms de fitxer que ja no existeixen
(`01_T/T2.qmd`, `contrib.qmd`) i el seu contingut ha estat reescrit diverses
vegades.

## Via 1 — supressions grans en fitxers que el missatge no anomena

```bash
git log --format='@@@%H%n%s%n%b%n---NUMSTAT---' --numstat
```

Processat amb un script que, per a cada commit, compara els fitxers amb
supressions > 20 línies contra els noms citats al missatge (nom base, arrel
sense extensió i ruta).

| Filtre | Candidats |
| :--- | ---: |
| Cru (tot `.qmd`/`.md`, historial sencer) | 168 |
| Descartant renames, esborrats complets i fitxers de `TODO/` | 46 |
| **Restringit a `.qmd` de contingut post-refactor amb supr. > insercions** | **4** |

**El filtre cru és inútil**: 168 candidats són majoritàriament el refactor
`c5d9416` (que reanomena 40 fitxers), esborrats deliberats de registres i
reescriptures massives de juny. La senyal apareix quan s'exigeixen les tres
condicions del CAS 1 alhora: **fitxer de contingut, no anomenat al missatge, i
més supressions que insercions sense ser un esborrat complet**.

## Via 2 — relació insercions/supressions anòmala

Els **4 candidats** post-refactor, examinats un a un llegint-ne el diff:

| Commit | Fitxer | Δ | Veredicte |
| :--- | :--- | :--- | :--- |
| **`4f973d5`** | `13_contrib.qmd` | +38 / −58 | ⚠️ **CAS 1, ja conegut i reparat** per `614f576` |
| `edac921` | `index.qmd` | +2 / −62 | ✅ **Deliberat**: elimina la duplicació MathML/LaTeX de la fórmula de la nota final (blocs `.content-visible when-format="html"` amb `<math>` a mà). Simplificació, no pèrdua. |
| `fe53cfc` | `12_sigles_simbols.qmd` | +2 / −6 | ✅ **Deliberat**: passa `` `<<` ``/`` `>>` `` a `$<<$`/`$>>$` i suprimeix un callout que explicava la coexistència de les dues notacions. Canvi de criteri, visible al diff. |
| `b81e3fa` | `index.qmd` | +1 / −2 | ✅ **Deliberat**: elimina **la fila duplicada de Toolchain** i corregeix «Complemenetària». És exactament el que `TODO.md §index.qmd` dona per resolt. |

## Via 3 — commits que arrosseguen fitxers de treball

```bash
git log --format='@@@%h %ad %s' --date=short --name-only --diff-filter=A \
  | (filtre: noms acabats en _, .orig, .bak, .rej, ~, .tmp, còpies numerades)
```

**3 resultats a tot l'historial:**

| Commit | Data | Fitxer arrossegat | Δ als `.qmd` reals |
| :--- | :--- | :--- | :--- |
| **`4f973d5`** | 12/07 | `01_apunts/A3.qmd_` (2110 l.) | ⚠️ **CAS 1** |
| `b55e413` | 13/07 | `13_contrib.qmd_` (802 l.) + `A3.qmd` (2106 l.) | ✅ `13_contrib.qmd`: **+1/−0**. El fitxer víctima potencial no es toca. |
| `b81e3fa` | 13/07 | `index.qmd_` (268 l.) | ✅ `index.qmd`: **+1/−2**, i els dos canvis són deliberats (vegeu via 2). |

**`b55e413` i `b81e3fa` tenen el símptoma però no la malaltia.** Arrosseguen
còpies de treball —el mateix `git add` massa ampli que el CAS 1— però **no
reverteixen res**: el fitxer que podria ser víctima rep +1 línia. La via 3 és
un bon detector precisament perquè dispara abans que hi hagi dany.

**Tots tres fitxers de treball ja s'han netejat del repositori:**

```bash
git ls-files | grep -E "_$|\.orig$|\.bak$"      # cap
```

| Fitxer | Esborrat per |
| :--- | :--- |
| `13_contrib.qmd_` | `dd0524f` |
| `index.qmd_` | `edac921` |
| `01_apunts/A3.qmd_` | `ccae7dd` |
| `A3.qmd` (còpia a l'arrel) | `d4086cd` |
| `03_solucions/S_criteris.qmd` | `71e07ee` |

## Via 4 — correccions declarades als missatges, encara vives?

Extretes les correccions amb patró `X → Y` dels missatges de commit i
comprovat, per a cadascuna, que **`X` ha desaparegut i `Y` hi és**.

| Correcció declarada | `X` encara viu? | `Y` present? |
| :--- | :--- | :--- |
| «de menor pes» → «de menys pes» (`4accc6c`) | no ✅ | sí ✅ |
| slug `-arithmetic` → `-aritmetic` (`953edca`) | no ✅ | sí ✅ |
| `restricicons` → `restriccions` | no ✅ | sí ✅ |
| `zobacz` → `vegeu` (`0951e74`) | no ✅ | — |
| `bibliografia.qmd` → `15_bibliografia.bib` (`614f576`) | no ✅ | sí ✅ |
| `sigles.md` → `12_sigles_simbols.qmd` (`614f576`) | no ✅ | sí ✅ |
| `0x1001 0000` → `0x10010000` (L2) | no ✅ | sí ✅ |
| «menys de 5 instruccions» → «com a màxim 4» (L3) | no ✅ | sí ✅ |
| «l'esclat» → «escalat» (`614f576`) | no ✅ | sí ✅ |
| «escriviu un programa» → «fragment» ×5 (`bcc9d52`) | no ✅ | — |
| `char w1[16]` → `char w1[13]` | no ✅ | sí ✅ |
| «avaluació lazy» → «avaluació gandula» (L3) | **sí** ⚠️ | sí ✅ |
| «dígits numèrics» → «dígits decimals» (L3) | **sí** ⚠️ | sí ✅ |

**Els dos positius no són pèrdues**, i tots dos s'expliquen igual: la
correcció es va aplicar **al lloc concret** que el commit tocava, i la forma
antiga sobreviu en **altres fitxers que aquell commit no tocava**.

```bash
git grep -n "avaluació lazy\|avaluació gandula" -- '*.qmd' ':!TODO/'
git grep -n "dígits numèrics\|dígits decimals" -- '*.qmd' ':!TODO/'
```

- `L3.qmd:87` diu «avaluació gandula (*lazy*)» ✅ i `L3.qmd:184` «dígits
  decimals» ✅ — les correccions **hi són**.
- Però `A3.qmd:372`, `:376`, `:661` i `L3.qmd:110`, `:170` diuen «avaluació
  lazy», i `E3.qmd:329` diu «dígits numèrics».

### 🟠 Troballa de la via 4 — «avaluació lazy» no s'ha harmonitzat

No és mode 2 (res no s'ha perdut), però és una **inconsistència
terminològica viva** que cap registre no recull:

| Forma | Ocurrències | On |
| :--- | ---: | :--- |
| «avaluació gandula (*lazy*)» | 1 | `L3.qmd:87` |
| «avaluació lazy» | 5 | `A3.qmd:372,376,661` · `L3.qmd:110,170` |

El commit que va introduir «gandula» ho declarava com a correcció de
manlleu no marcat, i `13_contrib.qmd` té regla sobre manlleus en cursiva. La
forma corregida és **minoria 1 a 5** al propi corpus. Va a la llista de la
sessió 2 com a escombrada pendent, amb el mateix criteri de simetria que la
passada C va usar per a «de menys pes».

## Via 5 — remissions `§Secció` penjades

Script que extreu tot `[fitxer] §Nom de secció` de `CLAUDE.md` i
`13_contrib.qmd` i comprova que hi hagi una capçalera corresponent al fitxer
destí.

**4 candidats, els 4 falsos positius del meu comparador:**

| Remissió | Per què no és penjada |
| :--- | :--- |
| `svg.md §15` | `24_specs/svg.md:487` = `## 15. Figures extretes de PDFs existents`. El meu script resolia la ruta relativa malament. |
| `A7.qmd §El problema de la diferència entre processador i memòria` | `A7.qmd:27` és `### El problema de la diferència (*gap*) entre processador i memòria`. **El títol duu «(*gap*)» intercalat** i la comparació literal fallava. La remissió és correcta i porta, a més, l'slug `@sec-gap-memoria` al costat. |
| `_quarto.yml §language` | No és una secció Markdown sinó una **clau YAML**. Correcta. |
| `§Fitxer de referència tècnica i…` | `13_contrib.qmd:30` = `### Fitxer de referència tècnica (\`11_riscv.qmd\`) i directori \`21_riscv/\``. Parèntesi intercalat, mateix cas. |

**Cap remissió penjada.** Les tres remissions al `TODO.md` ja es van verificar
a §1a. Recordatori: aquesta via és la que va destapar el CAS 1
(`CLAUDE.md:93` apuntava a una secció inexistent), de manera que el seu
resultat net és significatiu.

## Via 6 — línies afegides que no són a l'arbre final

Aplicada a **tots els 59 commits post-refactor que toquen `.qmd`**, no només a
un lot. Per a cada línia afegida de ≥ 25 caràcters, es comprova si segueix a
l'arbre de treball; si no, es busca si en sobreviu un **fragment distintiu**
(supersessió per reedició) abans de comptar-la com a pèrdua.

| Mesura | Xifra |
| :--- | ---: |
| Commits examinats | 59 |
| Línies afegides absents de l'arbre final | 83 |
| — de les quals sense cap fragment supervivent | **55** |
| — **de les quals del CAS 1 (`4f973d5`)** | **36** |
| Restants a explicar | **19** |

Les 19 restants, revisades una a una:

| Commit | Cas | Explicació |
| :--- | :--- | :--- |
| `254509b` ×6 | Capçaleres `*Padding* [B]` i 4 callouts «Comprovació pràctica» de L2 | **Ja documentades**: supersessió per `12bac2c` (`Padding [B]`) i per la decisió **P1** de la passada A, que va partir els callouts i en va moure l'oracle a l'enunciat. `L2.qmd:427` conté l'oracle de `s0 = 0x0000000C`. |
| `614f576` ×4 | Taula Graphviz, «Criteris de generació de l'slug (aplicats a `A4.qmd`)», «referencias», «Pendent de definir» | Reedicions posteriors: `13_contrib.qmd:638` diu ara «**Criteris de generació de l'slug**» sense el parèntesi; «referencias» era un **castellanisme** corregit després (`git grep -n "referencias"` → cap). |
| `87015d2` ×2 | Fila de la taula de callouts; llista de destins amb `TODO/TODO.md` | Reeditades: `13_contrib.qmd:434` té la fila amb text nou; `:17` recull la remissió al `TODO.md`. |
| `4ab25cb` ×1 | ` ```{.s filename="s2_3_1.s"} ` | **Ja documentada**: supersessió aprovada per `608056f` (regla P3 → `RV32I`). |
| `1489c84` ×1 | «Assembleu la declaració a RARS…» | Mateixa partició P1. |
| `b55e413` ×1 | `\| $C$ \| Capacitat (de la memòria cau) \| T6, T7, T8 \|` | Reeditada: `12_sigles_simbols.qmd:121` té la fila amb «T7, T8» i una observació diferent. |
| `b81e3fa` ×1 | `## 📘 Bibliografia Complementària` | Reeditada (canvi d'slug/format posterior). |
| `fe53cfc` ×1 | Fila `$>>$` de la taula de notació | Reeditada. |
| `31f7571` ×1 | Regla de veu dels `{.callout-tip}` | **Ampliada**, no perduda: `13_contrib.qmd:268` conté la regla amb l'excepció del «nosaltres» expositiu afegida després. |
| `8f3038f` ×1 | `: {tbl-colwidths="[15,85]" .borderless}` | Atribut de taula reeditat. |

**Cap pèrdua silenciosa.** Totes 19 són reedicions posteriors o supersessions
ja aprovades i documentades.

## Conclusió de 1d

| Via | Resultat |
| :--- | :--- |
| 1 — supressions grans en fitxers no anomenats | 4 candidats post-refactor; 1 és el CAS 1, 3 deliberats |
| 2 — relació insercions/supressions anòmala | íd. (la via 2 és el refinament de la 1) |
| 3 — fitxers de treball arrossegats | 3 commits; 1 és el CAS 1, 2 amb símptoma sense dany |
| 4 — correccions declarades encara vives | 11/13 netes; 2 positius, tots dos explicats, i un destapa una inconsistència terminològica |
| 5 — remissions `§` penjades | **cap** |
| 6 — línies afegides absents de l'arbre | 55 sense fragment supervivent; 36 són el CAS 1, les 19 restants totes explicades |

**No hi ha cap tercer cas de mode 2.** Dit amb la precisió que aquest informe
es deu: no n'hi ha **cap que aquestes sis vies detectin**. El mode 2 és
invisible a la comparació amb extrets quan no en tenim, i aquestes vies
només veuen el que l'historial registra; un canvi mai comès no hi surt.

**El que sí que ha sortit**: dos commits (`b55e413`, `b81e3fa`) amb el
**mateix `git add` massa ampli** que va causar el CAS 1, el dia següent. No
van fer mal per atzar —tocaven +1 línia del fitxer exposat—, però és el
mateix hàbit. I una inconsistència terminològica («avaluació lazy») que cap
registre no recollia.

---

# 1e — El `?@` amb l'abast correcte

**Resultat: cap referència creuada no resolta, ni a l'HTML ni al PDF.** Com
s'esperava. Però ara consta amb l'abast bo i amb la xifra que el demostra.

## El problema de l'abast, mesurat

```bash
ls _book/*.html          # 5 fitxers
find _book -name "*.html" | wc -l   # 39 fitxers
```

| Directori | Fitxers HTML |
| :--- | ---: |
| `_book/` (arrel) | 5 |
| `_book/01_apunts/` | 9 |
| `_book/02_exercicis/` | 9 |
| `_book/03_solucions/` | 9 |
| `_book/04_laboratori/` | 7 |
| **Total** | **39** |

**L'abast antic (`_book/*.html`) cobria 5 de 39 fitxers: el 13 %.** I els 5
són `index`, `11_riscv`, `12_sigles_simbols`, `13_contrib` i `14_LICENSE` —
precisament els que **no** són capítols de teoria, exercicis, solucions ni
laboratori. La comprovació no mirava cap dels fitxers que la revisió toca.

## Escombrada amb l'abast bo

```bash
grep -rho '?@[a-zA-Z0-9_-]*' _book/ --include=*.html | sort | uniq -c | sort -rn
grep -rho '?@[a-zA-Z0-9_-]*' _book/ --include=*.html | wc -l          # 0
grep -c '?@' Estructura-de-computadors.tex                            # 0
pdftotext _book/Estructura-de-computadors.pdf - | grep -c '?@'        # 0
```

| Sortida | Resultat |
| :--- | :--- |
| HTML, **39 fitxers recursius** | **0** |
| LaTeX (`Estructura-de-computadors.tex`, 1,9 MB) | **0** |
| PDF renderitzat (`_book/Estructura-de-computadors.pdf`, 3,6 MB) | **0** |

També s'ha buscat la forma alternativa que Quarto pot emetre
(`?sec-…`, `?fig-…`, `?tbl-…` sense l'arrova):

```bash
grep -rho '?[a-z]*-[a-zA-Z0-9-]*' _book/ --include=*.html | sort -u
```

→ **cap resultat**.

## Un fals positiu al PDF, que val la pena registrar

La cerca del marcador de LaTeX per a referències no resoltes (`??`) al PDF
dona **13 ocurrències**:

```bash
pdftotext _book/Estructura-de-computadors.pdf - | grep -oE '\?\?' | wc -l   # 13
```

Totes 13 són **contingut deliberat**, no errors:

```
• padding: ?? (indeterminat)
36 00 43 ?? AA AA ?? ?? 3C 4F 00 00 EE ?? ?? ??
Els bytes marcats ?? corresponen a padding i el seu valor és indeterminat.
```

Origen verificat: `03_solucions/S2.qmd:336`. Ordre:
`git grep -n "corresponen a padding i el seu valor és indeterminat" -- '*.qmd' ':!TODO/'`.

**Per què consta aquí**: si algú automatitza mai la comprovació del `?@` amb
`??` sobre el PDF —una elecció raonable, perquè és el marcador nadiu de
LaTeX—, obtindrà 13 falsos positius de S2 i es pensarà que hi ha 13
referències trencades. L'escombrada correcta al PDF és `?@`, no `??`.

## Validesa de la mesura

La mesura només val si el `_book/` és posterior al darrer canvi de contingut:

```bash
stat -c '%y %n' _book/index.html Estructura-de-computadors.tex
git log -1 --format='%h %ad' --date=iso -- '*.qmd'
```

| Artefacte | Data |
| :--- | :--- |
| Darrer commit que toca un `.qmd` | `a8e5df3`, 2026-09-21 **13:09** |
| `Estructura-de-computadors.tex` | 2026-09-21 **13:11** |
| `_book/index.html` | 2026-09-21 **13:14** |

El render és **posterior** al darrer canvi de contingut. La mesura és vàlida.

## Conclusió de 1e

La xarxa primària (`make render`, que emet un warning per cada referència no
resolta i ha estat net els tres dies) **no tenia cap forat**. La xarxa
secundària sí que el tenia: mirava el 13 % dels fitxers. Ara està refeta i
confirma la primària.

**Cap troballa, que és el resultat que s'esperava.** El valor del bloc és
negatiu en el bon sentit: elimina una comprovació que donava una falsa
sensació de cobertura, i deixa escrita l'ordre correcta perquè les sessions
següents no la tornin a fer malament.

```bash
# L'ordre correcta, per a futures verificacions:
grep -rho '?@[a-zA-Z0-9_-]*' _book/ --include=*.html | sort -u
grep -c '?@' Estructura-de-computadors.tex
pdftotext _book/Estructura-de-computadors.pdf - | grep -c '?@'
```

---
---

# LLIURAMENT — Llista única per a la sessió 2, per criticitat

Tot el que la sessió 2 ha d'executar. **Cap d'aquests punts no s'ha tocat en
aquesta sessió.** Els marcats 🔒 tenen veredicte de l'usuari i es poden
executar; la resta necessita confirmació.

## 🔴 CRÍTIC — contradiu el llibre publicat o és un error tècnic verificat

| # | Acció | Lloc | Origen |
| ---: | :--- | :--- | :--- |
| 1 | 🔒 **`main:` → `suma:`, `.globl main` → `.globl suma`, i `add t0, a0, a1` → `add a0, a0, a1`** | `A2.qmd:718-720` | §1b · Traça viva del mecanisme exclòs dins el callout de bones pràctiques, tres línies abans de l'esquelet bo. El tercer canvi és obligatori: sense ell el bloc mostraria una subrutina que no retorna res. Forma canònica a `A1.qmd:205-208`. |
| 2 | **Expressions aritmètiques als operands: A4 i S4** | `A4.qmd` (20 línies), `S4.qmd:258` | §1c D4 · RARS **no assembla** `li t0, NC*4` ni `.space NF*NC*4`. Error verificat empíricament, no millora. Mitigació mínima (remetre a `@nte-rars-operands-literals`) tampoc no feta: **cap remissió des d'A4 ni S4**. |
| 3 | 🔒 **`li a7, 10` → `li a7, 93`** (+ `li a0, 0`) | `E9.qmd:72`, `S9.qmd:201` | §1b · `E9:72` afirma «les convencions del curs» i en cita la falsa. Parella enunciat/solució: la convenció els governa per defecte. |
| 4 | **Eliminar els 4 blocs de `startup.s`** | `A1.qmd:39-40` · `A2.qmd:744-810` · `A3.qmd:1541-1550` · `index.qmd:147-151` i `:160-167` | §1b · Decisió del 19/07 amb tots els professors, mai executada. Coincideix amb l'enumeració de `TODO.md:7`. ⚠️ A2 són 66 línies: confirmar abans. |
| 5 | **Treure el «TODO» del text renderitzat** | `S_criteris_seleccio.qmd:19` | §1a · Únic «TODO» escrit com a contingut. No arriba a l'alumne avui només perquè el fitxer és comentat a `_quarto.yml:95`, cosa que el `CLAUDE.md` declara temporal. |

## 🟠 ALT — incoherències que desorienten l'alumne o bloquegen feina

| # | Acció | Lloc | Origen |
| ---: | :--- | :--- | :--- |
| 6 | 🔒 **Addició a l'entrada del catàleg del servei `exit`**: dir que a EC la sortida es fa amb `li a7, 93` (`exit2`) | `A9.qmd:575` | §1b · El catàleg és correcte (el servei 10 existeix), però és l'únic lloc on l'alumne aprèn a sortir, i n'aprèn la forma que el laboratori no accepta. |
| 7 | **Desbloquejar la regla de `_start`**: els 5 blocs de L3 ja compleixen. Actualitzar `13_contrib.qmd:204` (que es contradiu a si mateix), `TODO.md:115` i `L5_tasques.md:99`, i consolidar la regla | `13_contrib.qmd:204` + registres | §1c D1 · ⚠️ «Complir la regla d'ordre» **no** vol dir que `L3:357` estigui resolt: segueix sent l'únic E1 del verificador, per un altre motiu. |
| 8 | **Retoc a la descripció del carregador**: callout `#cau-carrega-ec` després de `A3.qmd:2052` | `A3.qmd:2053` | §1b · Redacció completa proposada a l'informe, pendent de la teva lectura. La secció descriu un sistema real amb SO i no desmenteix enlloc que els programes d'EC arrenquin així. |
| 9 | **Harmonitzar «avaluació lazy» → «avaluació gandula (*lazy*)»** | `A3.qmd:372,376,661` · `L3.qmd:110,170` | §1d via 4 · La forma corregida és **minoria 1 a 5**. Cap registre no ho recull. Mateix criteri de simetria que «de menys pes» a la passada C. |
| 10 | **Decisió viva: alineació de `.dword` a RARS** | `L2.qmd:156-166` | §1a · Registrada el 20/09, **pendent de resoldre**. ⚠️ **El bolcat comparatiu MARS/RARS de `:164-166` no existeix enlloc més**: si s'elimina el comentari, s'ha de preservar al `TODO.md`. |

## 🟡 MITJÀ — correccions puntuals i verificacions

| # | Acció | Lloc | Origen |
| ---: | :--- | :--- | :--- |
| 11 | **«del hardware» → «del maquinari»** | `13_contrib.qmd:189` | §1c D5 · L'únic incompliment de la taula de substitució del corpus, i és al fitxer que la fixa. |
| 12 | **Verificació tècnica de la taula d'alineació** contra l'ABI `ilp32` i la possible col·lisió amb l'alineació a 16 del BA | `A2.qmd:1080` | §1a cat. 1 · Afecta rigor tècnic. Sense registrar enlloc. |
| 13 | **Decisió de contingut a `#cau-boolea-c`**: com identificar «unes expressions» | `A3.qmd:244` | §1a cat. 1 · Pendent d'Adrià, obert des de T3 (registre `T3 T34`). |
| 14 | **Comprovar $V^2$ (A7) vs. $V_{CC}^2$ (A6)** a la fórmula de potència dinàmica | `A6.qmd`, `A7.qmd` | §1c · Heretat de `T6 D2`. **No verificat en aquesta sessió**: requereix llegir les dues fórmules senceres. |
| 15 | **Dues definicions de `#nte-programa-esquelet` al mateix fitxer** | `A2.qmd:730` (viva) i `:746` (comentada) | Heretat del bloc 3 · **Es resol sol amb el punt 4**: la comentada és dins del bloc `745-810`. |
| 16 | **Afegir la referència a secció concreta** | `A2.qmd:1720` | §1a cat. 3 |
| 17 | **Decidir sobre `22_figs_originals/T4_multiplicador_sequencial.png`** (63 KB, al costat del `.svg` font) | — | §1c · Heretat de `T4 §8`, encara obert. |

## 🔵 DECISIONS PER AL `TODO.md` — no s'executen, es registren (sessió 3)

Els **23 pendents distints** de §1a, col·lapsats. Els duplicats van amb la
instància canònica i les ubicacions com a llista.

| Entrada | Ubicacions | Nota |
| :--- | :--- | :--- |
| Unificar format de les taules de pseudoinstruccions | `A2.qmd:578`, `:603` | 🔁 canònica `:578` |
| Passar les dues taules de memòria a figura estàndard | `A2.qmd:988`, `:1026` | 🔁 canònica `:988` |
| Consolidar versions de la taula de referències tècniques (ISO de C, GCC) | `index.qmd:209`, `:210`, `:211`, `:212` | 🔁 canònica `:209`; ja registrada a `TODO.md §index.qmd` |
| **Versió numèrica o de data per a CSR** | `index.qmd:213` | ✅ **No consta enlloc**: entrada nova |
| Consens sobre els criteris de format de codi | `A2.qmd:686` | Encaixa amb «Criteris de codi C: completar» |
| Proposta de *checker* de format | `A2.qmd:687` | Relacionat amb `verifica_laboratoris.py` |
| Figures de half-adder i full-adder (T4) | `A4.qmd:80` | No hi ha secció de figures de T4 al `TODO.md` |
| Figura de la cadena de full-adders amb XOR (T4) | `A4.qmd:81` | És decisió («?»), no tasca |
| Introduir el format R4-TYPE a T5? | `A5.qmd:5` | Decisió d'abast |
| R5-TYPE (*compressed*) com a aprofundiment, a T2? | `A5.qmd:6` | Decisió d'abast, creua T5 i T2 |
| `fig-lru-roger`: diagrama d'estats | `A7.qmd:476` | **Ja consta** a `TODO.md §T7`: el comentari és redundant i es pot eliminar |
| Completar la taula de T1 de criteris de selecció | `S_criteris_seleccio.qmd:19` | Vegeu el punt 5 |

**Entrades del `TODO.md` a retirar per caduques** (§1c):

| Entrada | Per què |
| :--- | :--- |
| `§Decisions obertes` → «Plantilles Markdown» | Executada per D3 (`733b408`). `git grep '```{.markdown'` → cap |
| `§Laboratori` → «L2 §Pseudoinstrucció `la` i `li`: el cos és només TODO» | Omplert per la Fase C (hunk L2-7) |
| `§...L4` → «Pendent: … i `L6.qmd` (≈8 ocurrències de `.space N*4`)» | L6 **ja és net** |
| `§...L4` → «Pendent: L3 … té subrutines abans de `_start`» | Els 5 blocs de L3 compleixen |

## ⚪ SENSE ACCIÓ — verificat i correcte, no tocar

Es llisten perquè la sessió 2 no els «arregli»:

| Element | Per què es queda |
| :--- | :--- |
| `13_contrib.qmd:205` «No es fa servir `startup.s`» | 🔒 És el perquè de la convenció de sortida |
| `A3.qmd:2050-2052` (rutina de *startup* de UNIX/Linux) | 🔒 Descriu un sistema real; només rep el callout del punt 8 |
| `A9.qmd:527` (catàleg: `exit` 10 i `exit2` 93) | 🔒 Documentació de RARS i justificació de la tria d'EC |
| `21_riscv/RARS_syscall_codis.qmd:7` (fila del servei 10) | 🔒 Taula de referència de RARS |
| Els 6 `main:` de traducció de C | `A2:2052`, `A2:2103`, `A3:1205`, `S3:501`, `S4:388` (+ el comentat) — meitat esquerra de la regla del bloc 2b |
| Els 9 «TODO» de `13_contrib.qmd` | Metavariables (`#nte-TODO`, `#tbl-TODO`), remissions i la regla de commit |
| `A7.qmd:480` «Cal decidir com i quan sincronitzar-les» | Prosa didàctica |
| Els 13 `??` del PDF | Bytes de padding indeterminats (`S2.qmd:336`) |

## Regles que aquesta sessió deixa escrites

1. ⭐ **Quan s'exclou un MECANISME, no n'hi ha prou d'escombrar-ne el NOM; cal
   enumerar-ne les formes sintàctiques.** (§1b — `A2:718` no contenia
   «startup» i era la traça viva.)
2. **Un grep massa literal fabrica discrepàncies que no existeixen.** El corpus
   indenta amb tabulacions; buscar `sra t0, t0, 2` amb espais dona un fals
   negatiu. (§1c)
3. **L'escombrada del `?@` va recursiva sobre `_book/`**, no sobre
   `_book/*.html`, que és el 13 % dels fitxers. I al PDF es busca `?@`, no
   `??`. (§1e)
4. **Abans d'afirmar que una línia arriba a l'alumne, comprovar `_quarto.yml`**:
   un fitxer pot ser comentat, i això no el treu del projecte. (§1a)

## Estat en tancar la sessió 1

**Blocs 1a, 1b, 1c, 1d i 1e: tancats.** Cap canvi al corpus: l'única
escriptura d'aquesta sessió és aquest informe.

La sessió 2 executa. La sessió 3 reescriu el `TODO.md`.
