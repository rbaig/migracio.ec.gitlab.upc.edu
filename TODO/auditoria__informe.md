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

Proposta (a confirmar a la sessió 2), després de `:2052`:

> A **EC** no hi ha SO ni carregador (@imp-directe-sobre-processador): els
> programes tenen `_start` com a punt d'entrada i acaben amb `li a7, 93` +
> `ecall` (@nte-programa-esquelet). El mecanisme descrit aquí és el d'un
> sistema real amb SO.

Justificació de la forma: és el mateix patró de `#cau-void-main`
(`A2.qmd:2028`, afegit al bloc 3a), que resol un cas idèntic —C que no es
compila— dient explícitament què val a EC i què val en un sistema normal.
**No és una excepció inventada: és la forma que el corpus ja fa servir.**

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

### Judici sobre `A2.qmd:718-719`

**No és eliminable sense més**, perquè el bloc no il·lustra el punt d'entrada:
il·lustra **la indentació** (directives a columna 0, instruccions tabulades).
La correcció mínima que el posa d'acord amb la convenció és substituir les
dues línies per `.globl _start` / `_start:` i acabar amb la sortida canònica
en lloc de `ret`.

Però hi ha una objecció, i la deixo oberta per a l'usuari: `ret` al final d'un
`main` que no és punt d'entrada és **correcte** si es llegeix com una
subrutina qualsevol. Dues opcions:

1. **`main` → `_start`** amb sortida `li a7, 93` + `ecall`. Coherent amb la
   convenció; allarga el bloc dues línies.
2. **`main` → un nom de subrutina neutre** (p. ex. `suma:`), conservant el
   `ret`. Elimina la traça sense allargar el bloc ni prometre res sobre el
   punt d'entrada.

**Recomano la 2**: el bloc és sobre format, no sobre estructura de programa, i
la 1 hi encabiria un mecanisme que la secció encara no ha presentat
(l'esquelet arriba a `§Esquelet d'un programa`, la secció següent). Decisió de
l'usuari.

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

**Veredicte: no són errors del mateix tipus que `E9.qmd:72`.** Però sí que hi
ha una incoherència real, i és d'un altre ordre: el corpus ensenya l'`exit`
(10) com a exemple canònic de finalització, mentre la convenció d'EC és
l'`exit2` (93), i **l'alumne que copiï l'exemple de T9 escriurà codi que
contradiu el que li exigeix el laboratori**.

Tres sortides, per ordre de preferència:

1. **Canviar els exemples a `li a7, 93` + `li a0, 0`** i deixar la menció del
   servei 10 només a `:527` (que l'explica) i a la taula de RARS. Uniforme
   amb tot el corpus; costa una línia més a cada exemple (el `li a0, 0`).
2. Deixar-los i afegir una remissió a la convenció (`@nte-programa-esquelet`).
   Conserva el valor il·lustratiu del servei 10, però deixa dos exemples que
   l'alumne no ha de copiar.
3. Deixar-los tal com són. **No recomanada**: és la situació actual, i és la
   que produeix `E9.qmd:72`.

**Recomanació: 1**, i en tot cas `E9.qmd:72` s'ha de corregir sigui quina sigui
l'opció, perquè aquella línia **afirma** una convenció falsa.

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
| — errors clars | **1** (`E9.qmd:72`) |
| — a jutjar | 2 (A9:575, S9:201) |
| Mencions del servei 10 en prosa/taules, legítimes | 2 (`A9:527`, `RARS_syscall_codis.qmd:7`) |

**La lliçó metodològica del bloc**: l'escombrada per la paraula clau
(`startup`) donava 16 ocurrències i un panorama tranquil —13 comentades, 3
vives i totes tres previstes. La traça que de debò contradiu la decisió al
llibre publicat (`A2.qmd:718-719`) **no conté la paraula**. S'ha trobat
escombrant el **mecanisme** (`.globl`, `^main:`), no el nom. És el mateix
error que la passada C va documentar a 1a amb `11_riscv.qmd`, en una altra
dimensió: allà s'escapava un **directori**, aquí s'escapa un **sinònim**.
