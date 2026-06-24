# Tasques de revisió: T3.qmd, PE_T3.qmd, PS_T3.qmd

Font: anàlisi preliminar (T3.qmd llegit al xat de T2).
Verificació numèrica profunda i generació de solucionaris: **Opus High Thinking**.

---

## Configuració recomanada

| Fase | Model | Effortness |
| :--- | :--- | :--- |
| Correccions operatives (format, cometes, etiquetes, convencions) | Sonnet 4.6 | Medium |
| Verificació tècnica aritmètica (pila, BA, adreces, desplaçaments) | Opus | High Thinking |
| Generació de solucionaris PS_T3 | Opus | High Thinking |

---

## Tasques accionables directament

### T3.qmd — Errors d'etiqueta i convencions

**T3-C1** · L. 106 — `{#cau-instruccions-no-sla}`: el slug diu «sla» però el `TODO.md` indica que hauria de ser reanomenat (el TODO.md diu «parla de `sla`/`slai`, no de `lwu`»). El contingut efectivament parla de `sla`/`slai` (instruccions que no existeixen a RV32I). El nom és correcte pel contingut actual; el TODO.md pot estar obsolet. **Verificar i tancar el TODO.md si el nom és correcte.** Decisió recomanada: mantenir `#cau-instruccions-no-sla` (el nom descriu bé el contingut).

**T3-C2** · L. 1026 — `{#wrn-rars-mapa-memoria .callout-warning}` sense `collapse=true`. Segons `07_contrib.qmd`, els `{.callout-warning}` de més d'una línia porten `collapse=true`. Afegir-ho.

**T3-C3** · Tot el fitxer PE_T3.qmd — **39 blocs de codi** (```s i ```c) sense `filename=`. Cal substituir:
- `` ```s `` → `` ```{.s filename="RV32I"} `` (o `RV32IM`, `RV32IF`, `RV32IZicsr` si és el cas)
- `` ```c `` → `` ```{.c filename="C"} ``

**T3-C4** · T3.qmd — **29 seccions `###`/`####`** sense etiqueta `{#sec-}`. Afegir slugs seguint els criteris de `CLAUDE.md` (transliteració de caràcters, guions, unicitat). Llista completa:

| L. | Títol | Slug proposat |
| ---: | :--- | :--- |
| 13 | `### Desplaçaments lògics` | `{#sec-desplacaments-logics}` |
| 81 | `### Desplaçament aritmètic a la dreta` | `{#sec-desplacament-aritmetic-dreta}` |
| 110 | `### Traducció dels operadors C \`<<\` i \`>>\`` | `{#sec-traduccio-desplacament-c}` |
| 137 | `### Aplicació d'\`sll\`/\`slli\`: divisió entera per potències de 2` | `{#sec-sll-divisio-potencies}` |
| 198 | `### Aplicació d'\`and\`: selecció de bits (màscara)` | `{#sec-and-mascara}` |
| 215 | `### Aplicació d'\`or\`: posar bits a \`1\`` | `{#sec-or-bits-a-1}` |
| 232 | `### Aplicació d'\`xor\`: complementar bits` | `{#sec-xor-complementar-bits}` |
| 258 | `### Instruccions de comparació: \`slt\` i \`sltu\`` | `{#sec-instruccions-comparacio-slt}` |
| 272 | `### Traducció de \`==\` i \`!=\`` | `{#sec-traduccio-igualtat}` |
| 314 | `### Traducció de la negació booleana \`!\`` | `{#sec-traduccio-negacio-booleana}` |
| 336 | `### Traducció de \`<\`, \`>\`, \`<=\`, \`>=\`` | `{#sec-traduccio-comparacions}` |
| 376 | `### Traducció de \`&&\` i \`||\`: Avaluació *lazy*` | `{#sec-traduccio-operadors-logics}` |
| 590 | `### Sentència \`if-then-else\`` | `{#sec-if-then-else-sentencia}` |
| 639 | `### Avaluació *lazy* als salts condicionals encadenats` | `{#sec-avaluacio-lazy-encadenats}` |
| 694 | `### Sentència \`switch\`` | `{#sec-switch}` |
| 757 | `### Sentència \`while\`` | `{#sec-while}` |
| 839 | `### Sentència \`for\`` | `{#sec-for}` |
| 886 | `### Sentència \`do-while\`` | `{#sec-do-while}` |
| 1036 | `### Accés a variables globals` | `{#sec-acces-variables-globals}` |
| 1514 | `#### Preservació del context` | `{#sec-preservacio-context}` |
| 1544 | `#### Determinació dels registres segurs necessaris` | `{#sec-determinacio-registres-segurs}` |
| 1553 | `#### Estructura general d'una subrutina multinivell` | `{#sec-estructura-subrutina-multinivell}` |
| 1583 | `#### Exemples` | `{#sec-exemples-subrutines-multinivell}` |
| 1820 | `### Compilació separada` | `{#sec-compilacio-separada}` |
| 1852 | `### Compilació` | `{#sec-compilacio-proces}` |
| 1862 | `#### Expansió de macros i pseudoinstruccions` | `{#sec-expansio-macros-pseudo}` |
| 1866 | `#### Construcció de la taula de símbols` | `{#sec-construccio-taula-simbols}` |
| 1875 | `#### Reubicació i referències externes` | `{#sec-reubicacio-referencies-externes}` |
| 1994 | `### Càrrega en memòria` | `{#sec-carrega-memoria}` |

*(Nota: Claude Code és l'eina recomanada per a aquesta tasca sistemàtica.)*

### T3.qmd — Cometes rectes → guillemets o cursiva

**T3-L1** · L. 112 — `("desplaçament a l'esquerra")` → `(*desplaçament a l'esquerra*)` (terme tècnic en cursiva).

**T3-L2** · L. 1071 — `fitxer objecte "reubicable"` → `fitxer objecte *reubicable*` (terme tècnic, primera aparició).

**T3-L3** · L. 1124 — `La columna "Qui el guarda (*Saver*)"` → `La columna «Qui el guarda (*Saver*)»` (referència a un títol de columna).

**T3-L4** · L. 1380 — `l'operador \`&\` ("adreça de")` → `l'operador \`&\` (*adreça de*)` (terme tècnic).

**T3-L5** · L. 1834 — `es diu "compilar"` → `es diu «compilar»` (ús metalingüístic).

### T3.qmd — Terminologia «mode memòria» → «base+desplaçament»

**T3-T1** · Verificar que T3.qmd no conté cap ocurrència de «mode memòria» o «mode d'adreçament de memòria» (*resultat: 0 ocurrències* ✓ — T3 no requereix canvis en aquest punt).

### T3.qmd — TODOs pendents

**T3-TODO1** · L. 154–155 — `TODO Roger \`git show a288aaf\`` i `TODO @Adria: validar...`: integració del patch d'Adrià. Deixar fins a validació (no és una tasca de revisió de contingut).

**T3-TODO2** · L. 253 — `TODO Adrià: tu has proposat "unes expressions"...`: decisió terminològica sobre «les expressions» vs. «unes expressions». Cal resolució conjunta.

**T3-TODO3** · L. 1333 — `TODO Verificar que ho diu l'ABI`: referència a la psABI sobre la reserva de l'espai del BA. Verificar contra psABI (decisió pendent al `TODO.md` global: «Verificació ABI sobre el BA»).

### T3.qmd — Verificació tècnica (requereix Opus High Thinking)

**T3-V1** · Aritmètica de la pila: tots els exemples de blocs d'activació (BA) — verificar que els desplaçaments `sp`, la mida del BA i l'ordre de push/pop son coherents amb l'ABI i entre ells.

**T3-V2** · Exemple de subrutina multinivell (§`#sec-multinivell`): verificar que els registres salvats/restaurats (`ra`, `s0`–`s11`) i el BA corresponen exactament al codi RISC-V mostrat.

**T3-V3** · `#nte-la-auipc` (L. 1049–1072): verificar l'exemple numèric d'`auipc` (`@AA = 0x10010000`, PC = `0x00400000`, offset = `0x0fc10000`).

**T3-V4** · Exemples de `switch` amb jump table (§`#sec-switch`): verificar que els índexos, desplaçaments i etiquetes del codi RISC-V generat son correctes.

**T3-V5** · TODO.md L. 1333: confirmar contra psABI que «les subrutines reserven tot l'espai del BA a l'inici i l'alliberen just abans de retornar».

---

### PE_T3.qmd — Correccions

**PE3-C1** · Tot el fitxer — 39 blocs de codi sense `filename=`. Substituir sistemàticament (igual que PE_T2, aplicable amb Claude Code o script).

**PE3-C2** · Verificar coherència dels enunciats amb les seccions corresponents de T3 revisat (ordre, terminologia, profunditat dels exercicis).

---

### PS_T3.qmd — Correccions i solucionaris pendents

**PS3-C1** · Verificar coherència de totes les solucions amb el T3.qmd revisat.

**PS3-C2** · Verificar tots els càlculs numèrics de les solucions (desplaçaments de BA, valors de registres, etc.) — **Opus High Thinking**.

**PS3-NOU** · Revisar si hi ha exercicis de PE_T3 sense solució a PS_T3 (anàleg al PS-MANCANTS de T2). Llistar i decidir quins s'afegeixen.

---

## Tasques que requereixen decisió de l'usuari

**D-T3-1** · `#cau-instruccions-no-sla` (L. 106): el `TODO.md` indica que cal reanomenar-lo (diu «parla de `sla`/`slai`, no de `lwu`»). El contingut efectivament parla de `sla`/`slai`. El slug sembla correcte per al contingut actual.
- **Opció A**: Mantenir `#cau-instruccions-no-sla` i tancar el punt del `TODO.md`.
- **Opció B**: Reanomenar per raons que no s'aprecien en la revisió (potser hi havia una versió anterior diferent).

**D-T3-2** · TODOs d'Adrià (ls. 159 i 253): cal coordinació amb Adrià Armejach (BSC) per validar el patch i la terminologia.

**D-T3-3** · Decisió global pendent (TODO.md): `@sec-compilacio` (T3) és referenciat des d'altres temes?. Verificar que el slug no col·lisioni amb cap altre fitxer.

**D-T3-4** · Solucionaris nous PS_T3: quins exercicis de PE_T3 sense solució cal cobrir? (Decidir abans de la fase d'Opus).

---

## Refs externes de T3 a verificar al xat de revisió

Totes apunten a seccions d'altres temes. Cal confirmar que existiran un cop revisats:

| Referència | Probable ubicació |
| :--- | :--- |
| `@imp-exception-handler` | T2 o T9 |
| `@imp-modes-adrecament-llista` | T3 (secció `#sec-modes-adrecament-revisio`) — revisar slug |
| `@nte-pseudoinstruccions-salt-condicional-zero` | T2 |
| `@nte-registres-proposit-general` | T2 o compendi `05_riscv.qmd` |
| `@nte-riscv-rv32i` | T2 (`#nte-riscv-rv32i`) ✓ |
| `@nte-segments-memoria` | T2 o T3 |
| `@sec-codificacio-enters` | T4 |
| `@sec-ecall` | T9 |
| `@sec-host-vs-target` | T3 (`#sec-compilacio`) — verificar slug |
| `@sec-macros` | T3 — verificar slug |
| `@sec-nivells-abstraccio` | T1 |
| `@sec-traduccio-c-asm` | T3 — verificar slug |
| `@wrn-codificacio-enters-ca1` | T4 |

---

## Resum per prioritat

| Prioritat | Fitxer | Ítem | Descripció |
| :--- | :--- | :--- | :--- |
| **Alta** (format) | PE_T3.qmd | PE3-C1 | 39 blocs de codi sense `filename=` |
| **Alta** (convencions) | T3.qmd | T3-C2 | `#wrn-rars-mapa-memoria` sense `collapse=true` |
| **Alta** (convencions) | T3.qmd | T3-C4 | 29 seccions sense `{#sec-}` (Claude Code) |
| **Mitjana** (normes) | T3.qmd | T3-L1..5 | 5 cometes rectes → guillemets/cursiva |
| **Verificació** (Opus) | T3.qmd | T3-V1..5 | Aritmètica de pila, BA, auipc, switch |
| **Verificació** (Opus) | PS_T3.qmd | PS3-C2 | Càlculs numèrics de les solucions |
| **Pendent** | T3.qmd | T3-TODO1..3 | TODOs d'Adrià i psABI |
| **Pendent decisió** | Tots | D-T3-1..4 | Decisions obertes |
