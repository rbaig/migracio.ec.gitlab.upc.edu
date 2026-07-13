# T8-E8-S8 — Revisió interna profunda: llista d'accions

**Fitxers objectiu:** `01_apunts/A8.qmd`, `02_exercicis/E8.qmd`, `03_solucions/S8.qmd`
**Fitxers col·laterals:** `12_sigles.qmd`, `13_contrib.qmd`, `TODO.md`, `02_exercicis/E7.qmd` (A9)
**Llegenda:** 🔴 error · 🟡 millora · 🔵 decisió · ✅ fet · ⏳ pendent

Nota de context: totes les traces numèriques de S8 i dels tres enunciats
sense solució s'han verificat per simulació (LRU de pàgines, TLB, comptadors
de fallades de MC/TLB). Les figures es difereixen (decisió de Roger, Fase A):
en aquest xat només es completen les especificacions i els captions.

**Fase C executada (2026-07-13, Sonnet High, sense Thinking):** tots els
ítems dels blocs A (10) i B (19) aplicats i verificats. Les 9 especificacions
de figura pendents (B17) s'han enriquit amb classe de canvas (`estàndard`/
`ampla` segons `24_specs/svg.md §2`) i colors amb codis hex de la paleta
oficial (`svg.md §10`); els captions es donen per definitius. **Nota
important detectada durant l'execució (relacionada amb C6):** el caption
d'una de les figures (`fig-mv-vipt`) usava «aliasing» sense adaptar; s'ha
corregit a «aliàsing» per coherència amb el text ja existent a S8.qmd — la
resta d'ocurrències a A8.qmd (5×, totes en cursiva `*aliasing*`) es deixen
intactes fins que resolguis C6. Bloc C (7 decisions) intacte, pendent de la
teva resposta.

---

## A — Errors tècnics (execució directa) ✅ APLICATS

### A8.qmd

- 🔴✅ **A1 — §Fallada de pàgina: ordre de magnitud del cost d'accés al disc.**
  «un accés al disc és **desenes de milers** de vegades més lent que un accés a
  la memòria principal» — amb els valors de `@tbl-mv-jerarquia` (SSD 0,05–0,1 ms
  vs. DRAM 50–100 ns), la ràtio és **500–2 000×** → «centenars o milers de
  vegades». Coherent amb la correcció anàloga de T7 (A4 del xat T7). Es pot
  afegir que amb disc magnètic la ràtio sí que arriba a desenes o centenars de
  milers.
- 🔴✅ **A2 — §VIPT: notació de la mida de bloc.** «mida de bloc **$b$**» →
  **$B$** (T7 estableix $B$ = mida del bloc en bytes i $b = \log_2 B$ bits).
  Fórmula: $\log_2(C / (a \cdot B))$.
- 🔴✅ **A3 — `#tip-mv-tlb-exemple`: adreces físiques mal formades i mida de la
  memòria física no declarada.** Amb 4 marcs (16 KiB), l'adreça física té
  14 bits: «`0x02A0B`» → **`0x2A0B`**; «`0x03F21`» → **`0x3F21`**; «`0x0020C`» →
  **`0x020C`** (les formes actuals concatenen el PPN com si fos de 8 bits).
  Afegir a l'inici de l'exemple «i una memòria física de 16 KiB (4 marcs de
  pàgina)» (criteri de bona definició, `07_contrib §T8`).
- 🔴✅ **A4 — `#tip-mv-traduccio-exemple`: art ASCII desalineat.** Les fletxes
  «|←— VPN —→||←— desplaçament —→|» són més amples que els grups de bits de la
  línia superior (34 i 28 caràcters per a camps de 24 i 14). Reconstruir el bloc
  amb amplades exactes.
- 🔴✅ **A5 — `@fig-mv-flux-traduccio`: caption «TODO caption.»** → redactar-lo:
  «Flux complet de traducció d'una adreça en un sistema amb TLB i memòria
  virtual.» (ja proposat al comentari HTML).

### E8.qmd

- 🔴✅ **A6 — «instruccions en negreta» impossibles.** `exr-p8-tlb-basic` i
  `exr-p8-tlb-optimitzacio` diuen «per a cadascun dels accessos a dades de
  memòria (instruccions en negreta)», però als blocs de codi no hi pot haver
  negreta (herència del PDF MIPS original). Reformular: «per a cadascuna de les
  quatre instruccions d'accés a dades de memòria (`lw`/`sw`)» (resp. `lh`/`sh`).
- 🔴✅ **A7 — Veu: 2a persona del plural.** Els 10 enunciats usen el singular
  (18 imperatius: «Indica», «Omple», «Considera», «Calcula», «Compara»,
  «Raona», «Respon», «Repeteix», «Explica») → plural, convenció aplicada a
  E7 (A8 del xat T7). Afegir nota a `TODO.md` perquè E3 (que va quedar en
  singular: 35 imperatius) s'harmonitzi en un xat posterior.
- 🔴✅ **A8 — Blocs de codi sense atributs.** ` ```c ` (×3) i ` ```s ` (×2) →
  ` ```{.c filename="C"} ` i ` ```{.s filename="RV32I"} ` (`07_contrib §Blocs
  de codi`; totes les instruccions dels dos llistats són RV32I base).

### Altres fitxers

- 🔴✅ **A9 — E7.qmd: mateixa mancança que A8.** Els 3 blocs ` ```c ` de
  E7 van quedar sense atributs a la revisió de T7. Aplicar-hi
  ` ```{.c filename="C"} `.
- 🔴✅ **A10 — `12_sigles.qmd`: falta MRU.** Usada als callout-tip de S8
  («pila LRU (MRU→LRU)») → afegir `| **MRU** | *Most Recently Used* |`
  (criteri d'inclusió: sigles en callouts tip).

---

## B — Millores i harmonitzacions menors (execució directa) ✅ APLICADES

- 🟡✅ **B1 — «la cau» → «la MC»** a S8 (9×) i E8 (3×), seguint la
  pràctica de S7 («la MC», 22×). Els títols de secció mantenen «memòria cau».
- 🟡✅ **B2 — «gambada» → «stride»** (S8 ×2). El terme del projecte és
  l'anglicisme *stride*, introduït a T2 («una quantitat fixa (*stride*)»); en
  aparicions posteriors, sense cursiva.
- 🟡✅ **B3 — «de sols lectura» / «en mode sols lectura» (T8 ×3) → «només de
  lectura»**. La llegenda compacta de bits de `exr-p8-mv-proteccio`
  («0 = només lectura») pot mantenir-se.
- 🟡✅ **B4 — Separador de milers dins de math:** `65536` (S8 ×2) →
  `65\,536` («65 536», convenció de `07_contrib`).
- 🟡✅ **B5 — §Multinivell (cos):** «representa 4 MiB per procés» — explicitar
  el supòsit «(amb entrades de 4 bytes)», que ara només apareix al `wrn`.
- 🟡✅ **B6 — `#wrn-mv-multinivell`: nivells de Linux.** «Linux usa taules de
  pàgines de quatre nivells en arquitectures de 64 bits (x86-64, AArch64,
  RISC-V de 64 bits)» és imprecís: a RISC-V de 64 bits el valor per defecte és
  Sv39 (**tres** nivells); x86-64 amb LA57 pot usar-ne **cinc**. Proposta:
  «Linux usa taules de tres a cinc nivells segons l'arquitectura i la
  configuració (per exemple, quatre a x86-64; tres a RISC-V amb Sv39)».
- 🟡✅ **B7 — §Pàgines i marcs: redundància.** «de manera completament
  associativa, com una memòria cau completament associativa
  (@sec-completament-associativa)» → «de manera completament associativa, com
  en una MC d'aquest tipus (@sec-completament-associativa)».
- 🟡✅ **B8 — Format de sigles amb anglicisme (T8):** «(***memory management
  unit*** o **MMU**)» (negreta-cursiva) vs. «(*virtual page number* o **VPN**)»
  (cursiva simple, com PTE, TLB…). Unificar a cursiva simple: la negreta ja la
  porta el terme català; `07_contrib` reserva `***` per a quan l'anglicisme
  mateix és el concepte nuclear ressaltat.
- 🟡✅ **B9 — *overlays* sense traducció prèvia** (§Disc): «una tècnica
  coneguda com a *overlays*» → «una tècnica de superposicions (*overlays*)»
  (regla de primera aparició d'anglicismes).
- 🟡✅ **B10 — `exr-p8-mv-tlb-cau`: mida d'adreça no declarada.** La solució
  assumeix adreces virtuals de 32 bits; afegir-ho a l'enunciat (criteri de bona
  definició).
- 🟡✅ **B11 — `exr-p8-tlb-basic` / `-optimitzacio`: precisions.** Dir «TLB
  **de dades**» (com fa `exr-p8-mv-cache-tlb`) per excloure explícitament els
  accessos d'instruccions; a `-optimitzacio`, afegir «completament associatiu»
  (l'altre ja ho diu).
- 🟡✅ **B12 — Ordre de columnes de les taules d'estat (E8):**
  `exr-p8-tlb-estat` usa «V | VPN | PPN»; la teoria usa «VPN | V | D | E | PPN»
  (VPN primer, com a clau). Harmonitzar a l'ordre de la teoria.
- 🟡✅ **B13 — `sol-p8-mv-multinivell` c):** «… = 4 KiB + 4 MiB = 4 MiB +
  4 KiB» — el darrer pas és una reordenació trivial; deixar «= 4 MiB + 4 KiB».
- 🟡✅ **B14 — `exr-p8-mv-cache-tlb`: estat inicial.** La solució assumeix MC i
  TLB inicialment buits; afegir-ho a l'enunciat («Considereu la MC i el TLB
  inicialment buits»).
- 🟡✅ **B15 — `#tip-mv-tlb-exemple`, Accés 3: actualitzacions de la TP.**
  Explicitar les dues escriptures («VPN 3 → V = 0; VPN 4 → V = 1,
  PPN = `0x00`») en lloc del genèric «S'actualitza la TP i el TLB».
- 🟡✅ **B16 — `#tip-mv-tlb-exemple`: LRU del TLB vs. LRU de pàgines.** «L'ordre
  LRU actual al TLB és…» s'usa per triar la *pàgina* víctima; conceptualment,
  el reemplaçament de pàgines el gestiona el SO. Aquí coincideixen perquè totes
  les pàgines residents són al TLB: dir-ho («l'ordre d'ús de les pàgines
  residents —que en aquest exemple coincideix amb l'ordre LRU del TLB, ja que
  totes hi tenen entrada— és…»).
- 🟡✅ **B17 — Especificacions de les 9 figures pendents.** Enriquir cada
  comentari HTML (`fig-mv-espais`, `-pagines-marcs`, `-taula-pagines`,
  `-taula-multinivell`, `-tlb-estructura`, `-flux-traduccio`, `-comparticio`,
  `-pipt`, `-vipt`) amb: classe de canvas (`estreta`/`estàndard`/`ampla` + W),
  colors per zona semàntica de la paleta (`svg.md §10`), contingut concret de
  totes les files/etiquetes/fletxes i el **text definitiu del caption** —
  perquè un xat futur generi cada figura sense cap context addicional. Nota: el
  `T8_mv_flux_traduccio.svg` actual del repositori és un **placeholder** amb el
  text «TODO» (canvas 680); es manté per resoldre la referència.
- 🟡✅ **B18 — `TODO.md §T8`:** actualitzar el recompte («8 figures» → 9
  comentaris de figura pendents, un amb placeholder al repositori) i anotar que
  les especificacions + captions queden completes (B17). Afegir la nota sobre
  E3 (A7).
- 🟡✅ **B19 — Lint final** dels tres fitxers: dobles espais fora de blocs de
  codi, cometes rectes fora d'atributs, punts finals de llista.

---

## C — Decisions de Roger ✅ RESOLTES (2026-07-13, opció (a) en totes)

- 🔵✅ **C1 — Bit de presència: P (PE/PS) vs. V (teoria).** **Resolt: opció
  (a).** P→V aplicat a totes les taules i mencions de E8.qmd i S8.qmd (17
  substitucions en total, incloent-hi 2 ocurrències addicionals de «P
  1/PPN» detectades durant l'execució que no constaven a l'estimació
  inicial). **Tasca addicional aplicada:** el criteri de precedència
  textual de `13_contrib.qmd §T8` («la teoria preval sobre l'enunciat»)
  s'ha generalitzat: «els apunts (`Ax.qmd`) prevalen sobre els problemes
  (`Ex.qmd`) i solucions (`Sx.qmd`). Dins dels apunts, el cos del text i
  `.callout-note` prevalen sobre els altres callouts i continguts», amb
  una entrada específica nova per al bit `V`.
- 🔵✅ **C2 — `sol-p8-tlb-estat` apartat b (16 KiB sobre estat fix).**
  **Resolt: opció (a).** Reformulat en clau qualitativa: es dona el nombre
  de pàgines diferents per a cada llista (2 i 3, respectivament, totes dues
  abans de 5) i s'explica per què no és comparable donar un nombre exacte
  de fallades (l'estat inicial del TLB deixa de tenir sentit amb la nova
  mida de pàgina), amb referència a `13_contrib.qmd §T8`.
- 🔵✅ **C3 — `exr-p8-mv-matriu-lru`: `int` de 16 bits.** **Resolt: opció
  (a).** `int MAT[32][256]` → `short MAT[32][256]`; text actualitzat a
  «Els `short` es codifiquen en 16 bits (2 bytes)».
- 🔵✅ **C4 — `#wrn-mv-notacio-v`: atribució a Patterson & Hennessy.**
  **Resolt: opció (a)** (no s'ha pogut verificar la citació concreta —
  cerca web sense confirmació). Redacció neutra aplicada: «Alguns textos i
  els exàmens anteriors d'EC anomenen aquest camp **P** (*Present*), com fa
  l'arquitectura x86»; títol del callout actualitzat a «`V` a EC vs. `P` en
  altres fonts».
- 🔵✅ **C5 — `exr-p8-tlb-optimitzacio` c): política del TLB redissenyat.**
  **Resolt: opció (a).** Afegit «, mantenint el reemplaçament LRU,» a
  l'enunciat de l'apartat c).
- 🔵✅ **C6 — «aliàsing» vs. «*aliasing*».** **Resolt: opció (a).** Les 5
  ocurrències d'A8.qmd («*aliasing*» en cursiva, una en negreta-cursiva
  triple) uniformitzades a «aliàsing», amb la primera aparició en la forma
  «**aliàsing** (*aliasing*)». **Tasca addicional aplicada:** entrada nova a
  `13_contrib.qmd §Substitucions obligatòries`: `aliasing → aliàsing`, amb
  observació sobre la primera aparició.
- 🔵✅ **C7 — Veu dels exemples de teoria (transversal T7+T8).** **Resolt:
  opció (b).** `13_contrib.qmd §Veu impersonal` esmenat: s'admet el
  «nosaltres» expositiu als exemples *narrats* dins `{.callout-tip}`
  («Considerem un sistema amb...», «Suposem que...»), distingit de les
  instruccions directes a l'estudiant (2a persona del singular: «calcula»,
  «indica»), amb el criteri explícit de quan usar cadascuna. No calia tocar
  cap fitxer de T7 ni T8: els 3 `#tip-` d'A8.qmd ja seguien aquest patró.

---

## E — Verificacions completades sense incidència ✅

- **Traces de S8 verificades per simulació, correctes fins a l'últim dígit**
  (llevat del b) de `sol-p8-tlb-estat`, C2): `paginacio-basica` (5 fallades,
  expulsions 2 i 0, pila LRU), `taula-referencies` (les 6 files, l'únic
  *writeback* a `L 6600`, estats finals de TP i memòria física),
  `tlb-estat` llistes 1 i 2 (files, TLB finals, víctimes LRU raonades),
  `proteccio` (els 5 casos), `tlb-cau` (descomposició 20/12 i 6/5 bits,
  condició $2\text{ KiB} \leq 1 \times 4\text{ KiB}$), `cache-tlb` (fórmules de
  conjunt i pàgina; 16 384 / 64 / 131 072 / 65 536 exactes).
- **Els 3 exercicis sense solució són resolubles i ben definits** (amb les
  esmenes A6/B11/C3/C5). Resultats de referència per simulació:
  `tlb-basic` → 252 pàgines i 252 fallades (8 KiB); 504 pàgines i 1 500
  fallades (4 KiB). `tlb-optimitzacio` → 8 pàgines per accés, 12 en total i
  17 fallades (1 KiB, TLB-4); 3 pàgines i 3 fallades (4 KiB); mínim 12 fallades
  amb 6 entrades LRU. `matriu-lru` → primera fallada: `MAT[0][0..255]` i
  `MAT[1][0..255]` (per files) / `MAT[0..31][0..15]` (per columnes); 16 i 512
  fallades respectivament.
- **Cobertura del solucionari** = selecció documentada a `S_criteris_seleccio §T8`
  (7 de 10; els 3 no resolts hi consten com a no seleccionats).
- **Referències creuades externes:** totes existeixen (`sec-jerarquia`,
  `tbl-tecnologies-memoria`, `sec-completament-associativa`,
  `sec-escriptura-combinacions` a T7; `cau-prefixos-binaris` a T2;
  `sec-tema-excepcions-interrupcions`, `sec-ei-csr-privilegis` a T9). El punter
  T8→T9 consta a `07_contrib §Direccionalitat`.
- **Sigles:** MMU, PTE, TLB, PIPT, VIVT, VIPT, SSD, TAM, LRU presents;
  VPN/PPN correctament excloses (camps de bits); IPI només al `wrn`
  (exclosa). Només hi falta MRU (A10).
- **Correcció tècnica de la resta de la teoria:** Sv32 (34 bits físics,
  16 GiB, 2 nivells), Sv39/48/57 (3/4/5 nivells), mides de TP (4 MiB;
  $2^{36}$ entrades a 48 bits; 8 PiB a 64 bits), condició VIPT
  $C \leq a \cdot T$ amb l'exemple de 16 KiB, escriptura immediata del bit D,
  doble paper del bit V del TLB (coherent amb les traces dels problemes),
  taula PIPT/VIVT/VIPT: **tot correcte**.
- **Decisions `07_contrib §T8` ja aplicades correctament:** bit E amb polaritat
  de la teoria; mides de pàgina explícites als enunciats; ordre d'ús MRU→LRU
  especificat a `exr-p8-tlb-estat` i `exr-p8-mv-taula-referencies`.
- **No es toca:** títols dels `callout-caution` (6/6 amb títol a T8) — decisió
  expressament oberta a `TODO.md`.

---

## Fitxers modificats (Fase C, blocs A+B+C, completa)

`01_apunts/A8.qmd` · `02_exercicis/E8.qmd` · `03_solucions/S8.qmd` ·
`12_sigles_simbols.qmd` · `02_exercicis/E7.qmd` (A9) · `13_contrib.qmd`
(C1, C6, C7)

**Estat: revisió interna de T8 tancada.** Blocs A, B i C íntegrament
aplicats i verificats. Cap tasca pendent d'aquest xat.
