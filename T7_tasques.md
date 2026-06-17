# T7 — Revisió interna profunda: llista d'accions

**Fitxer objectiu:** `01_T/T7.qmd` (804 línies)
**Estat:** anàlisi feta (Tasca A). Pendent de confirmació abans d'executar.
**Llegenda de severitat:** 🔴 error (cal corregir) · 🟡 millora · 🔵 decisió de l'usuari · ⚪ neteja menor

> Les línies citades són les del fitxer subministrat i poden desplaçar-se a mesura
> que s'apliquin els canvis.

---

## Tasca A — Exploració (FET)

- Llegits `CLAUDE.md`, `contrib.qmd`, `svg_specs.md`, `_quarto.yml`, `TODO.md`, `T7.qmd`.
- Inventari de referències creuades, callouts, taules, equacions i figures fet (vegeu seccions F/G i «Referències»).

---

## Tasca B — Revisió tècnica (rigor ISA, números, models)

### B1 🔴 Exemple de fallades de conflicte — error de contingut (`@sec-exemple-conflicte`, L687–698)

Problemes:

1. L687: «difereixen en el **bit 2** del num_bloc (és a dir, en el **bit d'índex**, ja que $n_l=2$)». Amb $n_l=2$, l'índex són els bits [1:0]; el bit 2 és el **bit de menys pes de l'etiqueta**. La col·lisió es deu al fet que l'**índex coincideix** i l'**etiqueta difereix**.
2. L687: «tots els blocs de `A[i]` i `B[i]` es mapen a la **mateixa línia 0**». Fals. `A`→blocs 0–3, `B`→blocs 4–7. Per a cada `i`, `A[i]` i `B[i]` comparteixen línia *entre ells* (els seus blocs difereixen en $N_L=4$), però la línia és L0 (i=0,1), L1 (i=2,3), L2 (i=4,5), L3 (i=6,7).
3. L697–698: «les de la primera iteració són cold-start; **totes** les posteriors són de conflicte». Fals. Hi ha **8 fallades obligatòries** (primer accés de cada bloc: i=0,2,4,6) i **8 de conflicte** (i=1,3,5,7).

Es manté correcte que **els 16 accessos fallen**.

**Proposta de redacció (pendent d'aprovació):**

> Cada vector ocupa quatre blocs: `A` els blocs 0–3 i `B` els blocs 4–7. Per a
> cada índex `i`, `A[i]` i `B[i]` es troben en blocs que difereixen exactament en
> $N_L = 4$ (p. ex. `A[0]` al bloc 0 i `B[0]` al bloc 4). Com que sumar $N_L$ no
> altera els bits d'índex (els $n_l$ bits de menys pes del número de bloc), tots
> dos blocs tenen el **mateix índex** però **etiquetes diferents**: es mapen a la
> mateixa línia i s'expulsen mútuament a cada iteració.
>
> - **i=0:** `lw A[0]` (bloc 0, L0) → fallada obligatòria (carrega bloc 0). `lw B[0]` (bloc 4, L0) → fallada obligatòria (reemplaça bloc 0).
> - **i=1:** `lw A[1]` (bloc 0, L0) → fallada de conflicte. `lw B[1]` (bloc 4, L0) → fallada de conflicte.
> - **i=2:** `lw A[2]` (bloc 1, L1) → fallada obligatòria. `lw B[2]` (bloc 5, L1) → fallada obligatòria.
> - … (el patró es repeteix: a les iteracions parelles, primer accés al bloc → obligatòria; a les senars, reaccés a un bloc expulsat → conflicte).
>
> En total, 8 fallades obligatòries i 8 de conflicte: **els 16 accessos fallen**.
> Una memòria cau associativa per conjunts de 2 vies eliminaria les 8 fallades de
> conflicte (`A[i]` i `B[i]` coexistirien a les dues vies del mateix conjunt).

### B2 🔴 Cicles d'un accés a disc (L13)

«un accés a disc dur, **centenars de milers**» → amb $t_c=0{,}25$ ns i disc de 5 ms, surten ~$2\cdot10^7$ cicles. Proposta: **«desenes de milions de cicles»**.

### B3 🔴 Latència de memòria incoherent (L14 vs `@tbl-tecnologies-memoria`)

- DRAM: L14 diu «al voltant de **20 ns**»; la taula diu **50–100 ns**. Unificar (recomanat 50–100 ns; ajustar també el text i, si cal, els «100–200 cicles» de L29).
- SSD: L13 diu «**0,02 ms**»; la taula diu **0,05–0,1 ms**. Unificar.

### B4 🟡 Aprofundiment GPU — latència vs. ample de banda (`@wrn-gpu-memoria`, L61)

«la GDDR6 i l'HBM **redueixen molt la latència**… gràcies a la proximitat física» contradiu la frase anterior («la latència segueix sent el problema») i és tècnicament imprecís: GDDR6/HBM milloren sobretot l'**ample de banda**, no la latència. Proposta: reescriure per deixar clar que augmenten l'ample de banda i que la latència roman comparable a la de la DRAM.

### B5 🔵 Callout `@cau-errata-tam` (L592–600)

Repeteix la fórmula ja deduïda al cos (L590). Sembla documentar una **errata del PDF original** (multiplicar $t_h$ per $(1+p_m)$). Decisió: (a) mantenir-lo com a advertiment didàctic, (b) reanomenar l'etiqueta (no és una errata d'aquest document, sinó una prevenció), o (c) eliminar-lo per DRY i deixar només la deducció del cos.

### B6 ⚪ Símbol `α` reutilitzat

`α` = fracció d'Amdahl (L31–37) i `α` = factor d'activitat de potència (L99, ref. a T6). Contextos i seccions diferents; valorar una nota aclaridora o canvi de símbol en un dels dos.

### B7 ✅ Verificacions correctes (sense canvi)

Comprovats i correctes: descomposició de `0x100100F8` (L154, L299); exemple CD índex=7 (L289–301); exemple associatiu conjunt=1 (L321–333); traça LRU 4/38/6/52 (L407–411); penalitzacions per política (L533–559); deduccions de `@eq-tam-nr`, `CPI_penal`, `@eq-texe`, `@eq-tam-multinivell`; exemple de capacitat `g(int V[16])` (L703–723).

---

## Tasca C — Revisió pedagògica

### C1 🟡 Traça LRU — anotacions de les dues primeres fallades (L407–408)

«via 0 lliure, **LRU = via 0**» / «via 1 lliure, **LRU = via 1**»: en una fallada a via lliure no es consulta el LRU (s'omplen primer les vies buides). Aclarir la redacció perquè no doni a entendre que el LRU determina l'emplaçament quan hi ha vies lliures.

### C2 🟡 Títol de secció repetit

«Memòries cau separades d'instruccions i dades» apareix com a `####` (L602, dins de TAM) i com a `###` `@sec-multinivell-split` (L776). Tracten coses diferents (fórmula del TAM vs. organització física L1i/L1d). Proposta: diferenciar els títols (p. ex. L602 → «TAM amb memòries cau separades»).

### C3 🔵 `@tip-mc-numbloc` conté una figura (L149–177)

El callout `{.callout-tip}` inclou un bloc `#fig-` amb caption (a més, duplicat — vegeu E1). Decisió: treure la figura del callout i deixar-la al cos (les figures amb `#fig-`/caption no haurien d'anar dins callouts), o convertir-la en la figura de descomposició de bits que descriu el comentari (vegeu F/«fig-adreca-numbloc-offset»).

---

## Tasca D — Revisió lingüística (català normatiu + convencions)

### D1 🔵 `offset` vs. `desplaçament` (criteri global al fitxer)

`contrib.qmd` imposa la substitució obligatòria *offset → desplaçament*, però el fitxer usa «offset» a la prosa (L147, L200…), als títols («word offset», L157) i com a token de fórmula. Decisió de criteri: ① «desplaçament» a tota la prosa i deixar `offset`/`word_offset` només com a identificadors dins fórmules/codi, o ② mantenir l'statu quo. Recomanació: ①.

### D2 🟡 Anglicismes de les «tres C» dins la prosa (L690–696)

«**Cold-start miss**», «**Conflict miss**» en anglès i en negreta dins la traça. Un cop introduïts a L652–656, usar les formes catalanes: «fallada obligatòria (*cold-start*)», «fallada de conflicte». (Encaixa amb la reescriptura B1.)

### D3 🟡 `multicore` / `cores` (L47, L52, L789, L795)

Tractament inconsistent (cap, negreta, *cursiva*). Fixar primera aparició: «processadors **multinucli** (*multicore*)» i ús posterior coherent.

### D4 🟡 Cometes rectes → guillemets (L400)

«"el bloc que fa més temps que no s'usa"… "el bloc que s'usarà més tard"» → «…» (alineat amb `TODO.md`).

### D5 ⚪ Nombres petits en lletres (`contrib` §Llenguatge)

L16 «almenys **6** transistors» → «sis transistors». Revisar casos similars.

### D6 ⚪ Dobles espais heretats de l'extracció del PDF

Nombrosos (L13, L72–73, L107–108, L124, L184, L583, L606–607, L718, L752…). En Markdown es col·lapsen (inofensius a la sortida) però convé netejar la font.

### D7 🔵 Sigles a `sigles.qmd`/`sigles.md`

Verificar/afegir: MC, TAM, AMAT, SRAM, DRAM, SSD, RAM, CPI, GPU, HBM, GDDR6, ALU, PC. *(Cal el fitxer de sigles — vegeu «Fitxers necessaris».)*

### D8 ⚪ Veu en callout `@cau-errata-tam` (L599)

«**Noteu** que $t_h$…» (2a persona) dins un `{.callout-caution}`; la veu hauria de ser impersonal («Cal notar que…»). (Subjecte a la decisió B5.)

---

## Tasca E — Format Quarto

### E1 🔴 Etiqueta `#fig-mc-organitzacio` duplicada (L128 i L163)

La segona instància (dins `@tip-mc-numbloc`) reapunta al mateix SVG i caption que la primera, però el comentari (L161) descriu una figura diferent (descomposició dels 32 bits de `0x100100F8`). Acció: eliminar la duplicació i resoldre segons C3/F.

### E2 🔴 Nota al peu buida (L804)

`[^Core_i9-13900K_Labelled_Die_Shot]:` només conté un comentari HTML → nota buida. Acció: afegir text de nota (URL/atribució) o eliminar la referència.

### E3 🔴 Manquen `{#sec-}` a capçaleres `####`

- L41 `#### El punt d'inflexió: la fi de l'escalat de Dennard` → `{#sec-fi-escalat-dennard}`
- L50 `#### El *gap* avui` → `{#sec-gap-avui}`
- L581 `#### memòria cau unificada` → `{#sec-tam-mc-unificada}` (+ E4)
- L602 `#### Memòries cau separades d'instruccions i dades` → `{#sec-tam-mc-separades}` (+ C2)

### E4 🔴 Capçalera en minúscula (L581)

`#### memòria cau unificada` → `#### Memòria cau unificada`.

### E5 🔴 Slug amb errada `reemplacement` → `reemplacament`

Definició L385 `{#sec-politica-reemplacement}` i referència L314 `@sec-politica-reemplacement`. Transliteració correcta de «reemplaçament»: ç→c → `reemplacament`. Actualitzar definició i totes les referències.

### E6 ⚪ Centrat dels blocs de figura

Els blocs `{.light-content}`/`{.dark-content}` de T7 no porten `style="text-align: center;"` (que sí apareix a l'exemple d'integració de `contrib`). Valorar afegir-lo per coherència (baixa prioritat; el wrapper `#fig-` ja centra).

### E7 ⚪ Comentari de figura desat (L203–211)

Bloc `<!-- ... -->` antic de `fig-mc-encert` sense el wrapper `content-visible`. Es pot eliminar (el bloc actiu L212–225 ja és correcte).

---

## Tasca F/G — Figures (ATURADA fins a decidir extracció del PDF, pas 7)

### Figures ja integrades (SVG suposadament existent a `../figures/`)

| ID | SVG | Notes |
|:---|:---|:---|
| `@fig-jerarquia-piramide` | `T7_jerarquia_piramide` | OK |
| `@fig-mc-organitzacio` | `T7_mc_organitzacio` | **duplicada** (E1) |
| `@fig-mc-encert` | `T7_mc_encert` | OK |
| `@fig-mc-fallada` | `T7_mc_fallada` | OK |
| `@fig-cd-descomposicio-bits` | `T7_cd_descomposicio_bits` | OK |

### Figures pendents (referència `@` trencada → prioritàries)

| ID referenciat | Origen probable | Base PDF |
|:---|:---|:---|
| `@fig-gap-processador-memoria` (L29) | extreure/recrear | gràfic clàssic processador-memòria |
| `@fig-cd-diagrama` (L304) | recrear SVG (esquema) | Fig. 6.13 |
| `@fig-assoc-conjunts-diagrama` (L338) | recrear SVG | Fig. 6.24 |
| `@fig-ca-diagrama` (L356) | recrear SVG | — |
| `@fig-texe-diagrama` (L639) | recrear SVG | pàg. 24 PDF |
| `@wrn-dennard` (L43) | **no és figura**: és un callout referenciat no definit aquí → confirmar si és a T6 |

### Figures pendents (comentari-placeholder, sense `@` o amb `#fig-`/`#TODO`)

- `fig-adreca-numbloc-offset` (descomposició de `0x100100F8`; comentari L161) — la que hauria d'anar a `@tip-mc-numbloc`.
- `fig-assoc-conjunts-taula` (L336)
- `fig-lru-exemple` (L413, taula d'evolució LRU)
- `fig-lru-roger` (L416, «diagrama d'estats») — 🔵 **propòsit poc clar: cal aclarir o eliminar**
- `fig-escriptura-estat-inicial` (L481)
- `fig-escriptura-immediata-assignacio` (L491)
- `fig-escriptura-immediata-sense-assignacio` (L502)
- `fig-escriptura-retardada` (L514) + taula amb columna `D` (L434)
- figura de barres de les «tres C» per associativitat (L658)
- `fig-conflicte-exemple` (L699) — coherent amb la reescriptura B1
- `fig-capacitat-exemple` (L723)
- `fig-multinivell-diagrama` (L739)
- `fig-multinivell-multicore` (L791)

**Total aproximat:** ~18–20 figures. Segons el pas 7, abans de generar-les mirarem
d'extreure del PDF les que tinguin text seleccionable (esp. el gràfic del *gap* i,
potser, els diagrames de blocs). Les taules d'estat de la MC probablement es faran
com a SVG natiu (paleta `svg_specs.md §10`: blau=MC, verd=MP, etc.).

---

## Referències creuades — estat

**Internes resoltes:** `@sec-multinivell`, `@sec-politica-emplacament`, `@sec-mc-organitzacio`, `@sec-tipologia-fallades`, `@sec-texe-mc`, `@eq-tam`, `@eq-texe`, `@fig-jerarquia-piramide`, `@fig-mc-encert`, `@fig-mc-fallada`, `@fig-cd-descomposicio-bits`.

**Internes a corregir:** `@sec-politica-reemplacement` (E5).

**Externes (verificar a T6):** `@sec-amdahl`, `@sec-potencia-dinamica`, `@wrn-dennard`.

**Trencades (figures a crear):** `@fig-gap-processador-memoria`, `@fig-cd-diagrama`, `@fig-assoc-conjunts-diagrama`, `@fig-ca-diagrama`, `@fig-texe-diagrama`.

---

## Decisions que necessito de tu

- **B1** — aprovar la reescriptura de l'exemple de conflicte.
- **B3** — quins valors de latència fixem (DRAM 50–100 ns? SSD 0,05–0,1 ms?).
- **B5** — què fem amb `@cau-errata-tam` (mantenir / reanomenar / eliminar).
- **C3 / E1 / F** — la figura de `@tip-mc-numbloc`: la treiem del callout i/o la convertim en la figura de descomposició de bits?
- **D1** — criteri `offset` vs. `desplaçament`.
- **F** — propòsit de `fig-lru-roger`.
- **G** — cometes `«…»`: ho apliquem ja a T7 o ho deixem per a la passada global?

## Fitxers que necessito

- **PDF original del tema (MIPS, cap. 6 «memòria cau»)** — imprescindible per al pas 7 (extracció de figures).
- **`sigles.qmd`** (o `sigles.md`) — per a D7.
- **`T6.qmd`** — per verificar `@sec-amdahl`, `@sec-potencia-dinamica`, `@wrn-dennard` i decidir on viu `@fig-gap-processador-memoria`.
- *(Opcional)* `index.qmd`, `scripts/svg_generate_dark.py` + `dark_exclusions.txt` (per a F/G), `_variables.yml`.

## Model i effortness

`CLAUDE.md` recomana **Sonnet 4.6 / Normal** per a la revisió tècnica i lingüística de teoria. La reescriptura de l'exemple B1 i la generació de figures es beneficien d'un raonament més alt (Opus / High). Ara mateix vaig amb Opus; digues si vols que mantingui Opus per a tot el xat o si canviem a Sonnet per a les passades C–E.
