# T8 — Revisió interna profunda: llista d'accions

Objectiu: `T8.qmd` (Memòria virtual). Intensitat: profunda.
Estat: pendent de confirmació de l'usuari abans d'aplicar cap canvi.

---

## Resum executiu

**Fortaleses detectades** (no requereixen acció):

- Totes les capçaleres `##`/`###` ja tenen `{#sec-}` (T8 ja segueix el patró de T4; no cal la tasca sistemàtica pendent a T1–T3, T5–T9).
- Estructura pedagògica sòlida: problema → paginació → taula de pàgines → fallada de pàgina → TLB → protecció → integració amb la memòria cau. Cap concepte s'usa abans d'introduir-lo.
- Anglicismes ben formatats (`desplaçament` (*page offset*), `fallada de pàgina` (*page fault*), etc.).
- `tbl-colwidths` sumen 100 a totes les taules amb caption.
- Cap marca `TODO` pendent.
- Càlculs de l'exemple del callout de traducció (`0x00001801` → `0x2801`) verificats: correctes.
- Derivació de la condició VIPT `C ≤ a·T` verificada: correcta.

**Punts que requereixen acció**: 1 error tècnic (LRU), 1 referència creuada trencada,
terminologia `cache`→`cau`, inconsistències numèriques amb T7, i diverses decisions de
coherència mecanisme/exemple al TLB.

Llegenda: **[APLICAR]** = correcció clara, l'aplico en confirmar · **[DECISIÓ]** = cal que triïs · **[POSTERIOR]** = fase de figures.

---

## Tasca B — Revisió tècnica

### B1. [DECISIÓ — error tècnic] Ordre LRU incorrecte a l'«Exemple de traducció amb TLB» (Accés 3, línia 292)

L'enunciat de l'ordre LRU al TLB després de l'Accés 2 és **incorrecte**. El text diu:

> «L'ordre LRU actual al TLB és VPN = `0x00003` (el més antic), VPN = `0x00000`, VPN = `0x00001`, VPN = `0x00002` (el més recent).»

Reconstrucció correcta de la recència (de més antic a més recent):

- Història inicial (línia 280): `3`, `0`, `2` (de més antic a més recent).
- Accés 1 = escriptura a VPN = `2` (encert) → `2` continua sent el més recent.
- Accés 2 = lectura a VPN = `1` (es carrega) → `1` passa a ser **el més recent**.
- Ordre resultant de més antic a més recent: **`3`, `0`, `2`, `1`** (no `3, 0, 1, 2`).

L'error és haver llistat els VPN en ordre numèric (`…1, 2`) en lloc d'ordre de recència
(`…2, 1`). La **víctima continua sent VPN = `3`** (el més antic), de manera que el
resultat final de l'accés no canvia, però l'explicació de l'ordre és errònia.

**Proposta**: corregir la frase a «… VPN = `0x00002`, VPN = `0x00001` (el més recent)».

### B2. [DECISIÓ] La taula de pàgines de l'exemple no té columna `E` (línies 271–278)

El TLB de l'exemple té camp `E` (línies 261–266) i la PTE definida a `@cau-mv-pte`
inclou `E`, però la **taula de pàgines de l'exemple només té columnes `VPN, P, D, PPN`**.
Quan a l'Accés 2 i 3 es copia una PTE al TLB, el valor d'`E` que adopta l'entrada del TLB
queda **indeterminat**.

**Opcions**:

- (a) Afegir columna `E` a la taula de pàgines de l'exemple (recomanat: rigor i bona definició; coherent amb la decisió de T8 a `contrib.qmd` de definir tot el que les adreces impliquen).
- (b) Afegir una frase que fixi `E = 1` per a les pàgines de dades carregades.

### B3. [DECISIÓ] Coherència entre el mecanisme de fallada de TLB i l'exemple

El cos del text (`@sec-mv-tlb-fallada`, línies 208–213) descriu un mecanisme de **dos
passos**: en una fallada de TLB es copia la PTE al TLB *encara que `P = 0`* (l'entrada
queda amb `V = 0`); en reintentar l'accés, el `V = 0` provoca la fallada de pàgina.

L'exemple (Accés 2, línia 288) fa servir un model **d'un sol pas**: detecta `P = 0` en
llegir la PTE, resol la fallada de pàgina immediatament i només llavors copia la PTE
(ja actualitzada, `P = 1`) al TLB. L'estat final és correcte, però **no il·lustra el
mecanisme del bit `V`** que la secció emfatitza.

**Opcions**:

- (a) Reescriure l'Accés 2 perquè segueixi el mecanisme de dos passos del cos del text (còpia amb `V = 0` → reintent → fallada de pàgina → reinicialització de l'entrada).
- (b) Mantenir l'exemple com està i afegir una nota que aclareixi que és una descripció compactada del mecanisme de `@sec-mv-tlb-fallada`.
- (c) Revisar el cos del text perquè descrigui el model d'un sol pas (detecció de `P = 0` durant la lectura de la PTE), que és el comportament habitual del hardware.

Recomanació: decidir un únic model i aplicar-lo de manera coherent a la secció i a l'exemple.

### B4. [DECISIÓ] Conflació entre reemplaçament de *pàgina* i reemplaçament d'*entrada del TLB* (Accés 3)

A l'Accés 3 conviuen **dos reemplaçaments diferents** que el text barreja:

1. **Reemplaçament de marc de pàgina** (fallada de pàgina, no hi ha marc lliure): cal alliberar un marc físic. Es reusa `PPN = 0x00`, que conté la pàgina VPN = `3`; com que aquesta pàgina és *dirty* (`D = 1` a la seva PTE), s'escriu primer al disc.
2. **Reemplaçament d'entrada del TLB** (el TLB és ple): cal expulsar una entrada per encabir la traducció de VPN = `4`; per LRU, la víctima és VPN = `3`.

El text justifica la víctima amb «l'ordre LRU **al TLB**» i diu «`D = 1`: s'escriu primer
al disc», cosa que suggereix —incorrectament— que **expulsar una entrada del TLB**
provoca una escriptura al disc. Expulsar una entrada del TLB no escriu mai cap pàgina al
disc (el bit `D` ja s'ha propagat a la PTE per escriptura immediata, `@sec-mv-tlb-bitd`);
l'escriptura al disc es deu al fet que la **pàgina del marc reusat** és *dirty*.

**Opcions**:

- (a) Separar explícitament els dos reemplaçaments i deixar clar que l'escriptura al disc es deu a la pàgina del marc reusat (`PPN = 0x00`, VPN = `3`, `D = 1` a la PTE), no a l'expulsió de l'entrada del TLB.
- (b) Mantenir la simplificació però precisar la redacció perquè no impliqui que el TLB escriu al disc.

### B5. [APLICAR] «escriptura diferida» → «escriptura retardada» (línia 171)

T7 fixa el terme **escriptura retardada** (*write-back*); T8 diu «escriptura **diferida**».
Substituir per coherència i, opcionalment, afegir referència a `@sec-escriptura-encert`.

---

## Tasca C — Revisió pedagògica

### C1. [DECISIÓ] `### Taules de pàgines multinivell` sense cos de text (línies 133–150)

La secció `@sec-mv-multinivell` consta **únicament de dos `{.callout-warning}`** (no
avaluables) sense cap frase de cos. A més, el títol de la secció i el títol del primer
callout són idèntics («Taules de pàgines multinivell»).

**Opcions**: (a) afegir una o dues frases introductòries de cos que motivin el problema (mida de la taula) abans dels aprofundiments; (b) deixar-ho com a aprofundiment pur; (c) fusionar els dos aprofundiments.

### C2. [APLICAR — menor] Recap de la jerarquia amb referència creuada

El `@sec-mv-disc` i `@tbl-mv-jerarquia` repeteixen contingut de T7. Afegir una referència
(p. ex. «vegeu `@sec-tecnologies-memoria`») per reforçar el principi DRY.

---

## Tasca D — Revisió lingüística i terminològica

### D1. [DECISIÓ] `cache` → `memòria cau` / `cau` (36 ocurrències)

La secció «Integració del TLB i la memòria cau» (i els seus títols) fa servir l'anglicisme
**`cache`** de manera sistemàtica, contra la substitució obligatòria de `contrib.qmd`
(`cache → cau`, «especialment en títols») i contra l'ús de tot T7 (`memòria cau` / `MC`).

Afecta: títols `### Cache indexada físicament/virtualment`, cos del text (línies 340, 344,
348, 350, 354, 356–358, 362, 366, 378) i comentaris de figura.

**Proposta**: substituir `cache` per `memòria cau` (primera aparició de cada paràgraf) o
`cau`, mantenint les sigles **PIPT/VIVT/VIPT** i la seva expansió anglesa en cursiva.
Els *slugs* `#sec-mv-cache-*` es poden conservar (no es referencien enlloc).

### D2. [DECISIÓ] Inconsistències numèriques amb la taula de jerarquia de T7

| Nivell | T7 (`@tbl-tecnologies-memoria`) | T8 (`@tbl-mv-jerarquia`) |
|:---|:---|:---|
| Memòria cau | 0,5 – **5** ns | 0,5 – **40** ns |
| Secundària (SSD) | **0,05** – 0,1 ms | **0,02** – 0,1 ms |

**Proposta**: alinear T8 als valors de T7 (capítol de referència de la jerarquia):
cau `0,5 – 5 ns`, SSD `0,05 – 0,1 ms`. Confirma'm si prefereixes uns altres valors canònics.

### D3. [DECISIÓ — menor] «Emmagatzematge secundari» → «Memòria secundària»

T7 usa «memòria secundària»; T8 (etiqueta de taula) usa «Emmagatzematge secundari».
Unificar per coherència.

### D4. [APLICAR — menor] `aliasing`: cursiva a la primera aparició

Primera aparició (línia 350) en negreta `**aliasing**`. Com a anglicisme sense traducció
catalana establerta, hauria d'anar en cursiva (*aliasing*). Decidir si manté la negreta.

### D5. [DECISIÓ — menor, global] «de sols lectura»

Apareix a T8 (línies 311, 312, 332) i també a T7 (L1i). No és la forma més normativa
(«de només lectura» / «de sola lectura»). Com que és consistent a tot el projecte, és una
decisió **global**: mantenir o esmenar a tot arreu.

### D6. [DECISIÓ — menor] Glossa del bit `D`

T7: «bit de modificació (*dirty bit*, `D`)». T8: «Bit `D` (*dirty*)». Alinear la
nomenclatura de la primera aparició si es vol uniformitat estricta.

---

## Tasca E — Revisió format Quarto

### E1. [CRÍTIC] Referència creuada trencada `@fig-mv-flux-traduccio` (línia 242)

La línia 242 conté «La `@fig-mv-flux-traduccio` resumeix…», però la figura **no existeix**
(només hi ha el comentari HTML descriptiu a la línia 244). Quarto la renderitzarà com a
`??`.

**Opcions**:

- (a) Generar la figura ara (és el diagrama de flux complet; vegeu Tasca F5) i deixar la `@`-referència.
- (b) Convertir-la temporalment en referència provisional descriptiva segons `contrib.qmd` (enllaç + comentari HTML) fins que es generi la figura.

### E2. [DECISIÓ — menor] `tbl-colwidths` a les taules sense caption

Les taules dels callouts (`@cau-mv-tlb-estructura`, taules de l'exemple del TLB) no tenen
`tbl-colwidths`. No és obligatori, però convé revisar-ne el render a PDF. Opcional.

---

## Tasca F — Figures SVG (POSTERIOR, després d'aprovar el text)

Vuit figures de **nova creació** (no hi ha PDF original per a T8; no apliquen els mètodes
d'extracció de `svg_specs.md §14`). Totes seguiran `svg_specs.md` (font Source Sans Pro,
paleta del projecte, variant dark automàtica via `svg_generate_dark.py`).

1. `T8_mv_espais` — espais lògic (P1/P2) vs. físic + MMU.
2. `T8_mv_pagines_marcs` — assignació VPN → PPN (completament associativa) + disc.
3. `T8_mv_taula_pagines` — estructura de la taula de pàgines (VPN índex, P/D/E/PPN).
4. `T8_mv_tlb_estructura` — taula de pàgines vs. TLB (còpia parcial).
5. `T8_mv_flux_traduccio` — **diagrama de flux complet** (prioritari: referenciat al cos).
6. `T8_mv_comparticio` — compartició d'una pàgina física entre P1 i P2.
7. `T8_mv_pipt` — diagrama de blocs PIPT (sèrie).
8. `T8_mv_vipt` — diagrama de blocs VIPT (paral·lel + comparador).

Nota: el flux de T7 va incloure una pausa per intentar extreure figures del PDF original.
Per a T8 **no hi ha PDF d'origen** (contingut nou), de manera que totes es generen de zero.

---

## Tasca G — Integració de figures (POSTERIOR)

Per a cada figura, aplicar el patró `content-visible` light/dark de `contrib.qmd`
(bloc HTML amb les dues variants + bloc PDF amb la variant light), substituint els
comentaris `<!-- fig-… -->` actuals.

---

## Fitxers que necessito (per completar la revisió)

- `_quarto.yml` i `index.qmd` — lectura obligatòria segons `CLAUDE.md`; confirmar `var tema8` i la inclusió de T8.
- `sigles.md` — per afegir-hi les sigles noves de T8: **MMU, VPN, PPN, PTE, TLB, PIPT, VIPT, VIVT** (exclou camps de bits i sigles de `{.callout-warning}` com IPI).
- `T9.qmd` — per verificar la referència `#sec-tema-excepcions-interrupcions` (línia 303) i alinear la terminologia de modes privilegiats («mode sistema» vs. «mode S/M» de T9).

---

## Actualitzacions finals (en tancar la sessió)

- `T8.qmd` — totes les correccions aprovades.
- `sigles.md` — sigles noves.
- `T8_tasques.md` — aquest fitxer, amb l'estat final.
- `CLAUDE.md` — passar T8 de «pendent de revisió interna» a «preparat per a revisió externa».
- `contrib.qmd` — només si es pren alguna decisió de format/terminologia nova (p. ex. D5).
