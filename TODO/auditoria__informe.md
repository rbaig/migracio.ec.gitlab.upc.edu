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
| 578 | **3** | `<!-- TODO Roger unificar format taules pseudoinstruccions -->` (dins `#nte-pseudoinstruccio-la`) | Nota de progrés adreçada a una persona. **Decisió de l'usuari**: o fer la unificació i esborrar-lo, o passar-lo al `TODO.md` com a tasca transversal. No pot quedar-se al corpus. |
| 603 | **3** | Íd., dins `#imp-ec-la-offset` | Íd. (és el mateix pendent duplicat; el `TODO.md` n'ha de tenir **una** entrada, no dues). |
| 686 | **1** | `<!-- TODO hi ha consens? -->`, just abans de `#imp-codi-format-criteris` | **Decisió viva no registrada**: pregunta si els criteris de format de codi tenen consens entre professors. Candidata a `TODO.md §Decisions obertes`, i encaixa amb l'entrada oberta «Criteris de codi C: completar». |
| 687 | **1** | `<!-- TODO Miquel: podríem fer un checker -->` | **Proposta viva d'eina** (verificador de format de codi), adreçada a un professor. Va a `TODO.md`, no al corpus. Relacionada amb `25_scripts/verifica_laboratoris.py`, que ja existeix. |
| 744 | **2** | `<!-- TODO(startup.s) Reactivar si es manté l'esquelet específic d'EC amb startup.s. Si es manté, corregir abans: _start (no __start), li a7, 93 (no a7, 10). -->` | **Contradiu la decisió del 19/07.** Eliminar amb tot el bloc comentat `:745-810`. Vegeu §1b. |
| 810 | **2** | `--- TODO -->` — **tancament** del bloc comentat obert a `:745` | Desapareix amb el bloc. Nota: la grafia `--- TODO -->` és un tancament de comentari mal format (tres guions en lloc de dos), i el comptador el registra com a cas propi. |
| 988 | **3** | `<!-- TODO substituir la taula següent per un diagrama de memòria estàndard. -->` | Pendent **de figura**, no de decisió. El `TODO.md` ja té secció de figures pendents (`§T7`, `§T8`); això n'és una de T2 que no hi consta. Migrar-lo. |
| 1026 | **3** | `<!-- TODO passar a figura de memòria estàndard -->` (dins `#tip-endianness`) | Íd. — és **la mateixa tasca** que `:988` sobre una altra taula. Una entrada de `TODO.md` amb les dues ubicacions. |
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
| 162 | **1** | «Cal decidir quina versió presentar als alumnes i si s'ha d'afegir una nota sobre aquest comportament. De moment es presenten les dues versions.» | **Decisió viva.** Matís respecte de l'enunciat de la sessió: **ja consta al `TODO.md`**, a `§Tasques transversals` («`L2.qmd:163` — TODO en comentari sobre l'alineació de `.dword` a RARS», registrada el 2026-09-20). El pendent, doncs, no és registrar-la sinó **resoldre-la**. El comentari conté a més el bolcat comparatiu MARS/RARS (`:164-166`), que és **evidència que no és enlloc més**: si s'elimina el comentari, s'ha de preservar al `TODO.md`. |

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
| 209 | **1** | `<!-- TODO Determinar versió la ISO de C? -->` | **Decisió viva, i ja registrada**: `TODO.md §index.qmd` diu «Pendent encara: versió ISO de C i versió GCC (marcades amb `<!-- TODO -->`…)». Ara la taula ja cita `[@iso9899_2024]`, de manera que el pendent és **verificar i tancar**, no decidir de zero. |
| 210 | **1** | `<!-- TODO La ISO de C és tancada? -->` | Íd. — la mateixa decisió, formulada dues vegades. |
| 211 | **1** | `<!-- TODO GCC cal especificar millor -->` | Íd., per a la fila del compilador (`[@gcc16]`). Registrat al `TODO.md`. |
| 212 | **1** | `<!-- TODO Consolidar noms, versions, etc. de tot -->` | Versió genèrica dels tres anteriors. Al `TODO.md` hi ha d'anar **una** entrada, no quatre. |
| 213 | **1** | `<!-- TODO Versió numèrica de CSR o de data a la resta -->` | **No consta al `TODO.md`**: l'entrada registrada només parla d'ISO de C i GCC. Aquest és nou i afecta la fila de RISC-V (`[@riscv_csrs]`). |

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
   vegades (`:209-212`), i un cinquè (`:213`) no consta enlloc.
3. **A2 té dos pendents de figura idèntics** (`:988` i `:1026`) i dos de
   format de taules idèntics (`:578` i `:603`). El `TODO.md` reescrit ha de
   tenir una entrada per pendent, amb les ubicacions com a llista.
