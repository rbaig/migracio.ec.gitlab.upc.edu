# T5.qmd — Llista d'accions de la revisió interna

> Fitxer objectiu: `01_T/T5.qmd` (Tema 5: Coma flotant) · Intensitat: **profunda**
> Model de referència: `T4.qmd` · Convencions: `CLAUDE.md`, `contrib.qmd`, `svg_specs.md`
> Llegenda de severitat: 🔴 crític · 🟠 important · 🟡 menor/cosmètic · 🔵 decisió pendent

---

## Resum executiu

S'han verificat **bit a bit els quatre exemples numèrics IEEE-754** del tema. Tres són
correctes en el resultat final (amb errors menors en passos intermedis); **un té el
resultat final incorrecte** i s'ha de refer:

| Exemple | Callout | Resultat al text | Resultat correcte | Estat |
|---|---|---|---|---|
| Codificació −1029,68 | `tip-ieee754-codificacio` | `0xC480B5C3` | `0xC480B5C3` | ✅ correcte (errors menors als passos) |
| Descodificació | `tip-ieee754-decodificacio` | `4136,15625` | `4136,15625` | ✅ correcte (un terme espuri al pas d) |
| Suma | `tip-suma-ieee754` | `0xC0500005` | `0xC0500005` | ✅ correcte (binari d'error mal alineat) |
| **Multiplicació** | `tip-multiplicacio-ieee754` | `0xBEB60004` | **`0xBEB60002`** | 🔴 **RESULTAT FINAL INCORRECTE** |

---

## B. Revisió tècnica (rigor ISA i numèric)

### 🔴 B1 — Multiplicació IEEE-754: resultat final incorrecte (`tip-multiplicacio-ieee754`, ~ln 499–545)

Cal refer l'exemple sencer. Verificació independent des de zero:

- `x = 0x3F600000` = +1,75 × 2⁻¹ = **0,875**
- `y = 0xBED00002` = −(1,625 + 2⁻²²) × 2⁻² = **−0,40625005960…**
- `z = x·y` = **−0,35546880215…**
- Float més proper (e = −2): fracció k = 3 538 946 = `0110 1100 … 010`
- **`z = 0xBEB60002`** ✔ (el text diu `0xBEB60004`)

Cadena d'errors encadenats que cal corregir:

| Pas | Línia aprox. | Al text (incorrecte) | Correcte |
|---|---|---|---|
| Pas 2 (producte) | 522 | `…0000 0111 10` (sobren 2 bits) | `10.1101 1000 0000 0000 0000 0111` (24 bits frac., **sense** `10` final) |
| Pas 4 (normalitzar) | 529 | `…0011 110 × 2⁻²` | `1.0110 1100 0000 0000 0000 0011 1 × 2⁻²` |
| Pas 5 (bits de guarda) | 533 | `110` (G=1,R=1) | només es descarten **2 bits**: **G=1, R=1** amb guarda `11` |
| Pas 5 (frac. retinguda) | 535–539 | `…011 → +1 → …100` | `…001 → +1 → …010` |
| Pas 6 (codificar) | 544 | `0xBEB60004` | **`0xBEB60002`** |

### 🟡 B2 — Codificació: error binari intermedi (`tip-ieee754-codificacio`, ~ln 165)
El binari de l'error `0,0000…0001 111 × 2¹⁰` té l'1 capdavanter a la posició 24;
hauria d'estar a la **posició 25** perquè `× 2¹⁰ ≈ 1,111₂ × 2⁻¹⁵`. Cosmètic (el
resultat `5,722 × 10⁻⁵` és correcte).

### 🟡 B3 — Suma: error binari intermedi (`tip-suma-ieee754`, ~ln 462)
El binari de l'error `0,0000…001 × 2¹` mostra l'1 a la posició 23 → daria 2⁻²².
Per obtenir `2⁻²⁴` (≈ 6,0 × 10⁻⁸, que sí és correcte) l'1 ha d'anar a la **posició 25**.

---

## C. Revisió pedagògica / discursiva

### 🟠 C1 — Codificació: línia duplicada i amb notació malmesa (`tip-ieee754-codificacio`, ~ln 167)
Hi ha **dues** línies seguides que calculen el mateix error. La primera (ln 167) té la
notació errònia `… /2 × 10⁵`. **Suprimir la ln 167** i conservar la ln 169
(`… × 2⁻¹⁵ = 1,875/32768 = 5,722 × 10⁻⁵`), que és correcta.

### 🟠 C2 — Descodificació: terme espuri (`tip-ieee754-decodificacio`, ~ln 199)
`1 0000 0010 1000₂ = 2¹² + 2⁵ + 2³ + 2² = 4096 + 32 + 8 = 4136` → el terme **`+ 2²`
sobra** (el bit 2² no està actiu i tampoc s'ha sumat). Correcte: `2¹² + 2⁵ + 2³`.

---

## D. Revisió lingüística (català normatiu)

### 🟡 D1 — Majúscula després de punt (~ln 473)
`…Normalitzar el resultat. cal comprovar…` → `…**C**al comprovar…`.

### 🔵 D2 — *underflow* vs terme català
Apareix *underflow* en cursiva (anglicisme) i com a títol de secció. Cal decidir si
s'unifica amb un terme català (p. ex. **subdesbordament**, ja usat en altres temes
segons les substitucions de `contrib.qmd`) amb `(*underflow*)` a la primera aparició,
o si es manté *underflow* com a terme tècnic acceptat. → **decisió**.

---

## E. Revisió de format Quarto

### 🟡 E1 — `{.C}` → `{.c}` (ln 766 i 811)
Dos blocs de codi C usen `{.C filename="C"}` (majúscula). La convenció i la resta del
fitxer fan servir `{.c filename="C"}` (minúscula). Unificar a minúscula.

### ✅ E2 — Slugs `{#sec-}`: COMPLET (cap acció)
Verificat: les **18** capçaleres reals de secció (`##/###/####`) ja porten `{#sec-…}`
correcte. Les 35 capçaleres `##` sense slug són **títols de callout**, que per
convenció **no** han de portar `{#sec-}`. Aquesta tasca ja està feta a T5.

### 🟡 E3 — Coherència de títols en `.callout-caution`
`contrib.qmd` indica que `.callout-caution` (Essencial) no porta títol; a T5 alguns
en porten. Cal una passada de coherència (o bé acceptar-ho com a excepció documentada).
→ revisió menor.

---

## F. Figures SVG

### 🔵 F1 — T5 no té CAP figura
Confirmat: T5.qmd no referencia cap `figures/*.svg` (T4, en contrast, en té 18). El
tema és intrínsecament visual. Candidates proposades (a decidir):

1. **Disposició de camps S | E | F** (32 bits, simple precisió) — molt recomanable.
2. **Recta numèrica rang/precisió** amb denormals i forat al voltant del zero.
3. **Esquema d'arrodoniment GRS** (bits de guarda/round/sticky).
4. **Paral·lelisme registres enters ↔ coma flotant** (ja hi ha taula; potser no cal).

→ **decisió**: quines (si cap) generar aquesta sessió i amb quin abast.

### 🔵 F2 — Taula de registres FP: inline vs include
T5 té la taula inline (`nte-registres-coma-flotant`); el repo ja conté
`riscv/RV32I_registres_coma_flotant.qmd` (versió diferent, més verbosa). Per la
convenció «contingut compartit → include a `/riscv/` usat a tema i compendi», caldria
reconciliar-les. Les dues versions difereixen en estil. → **decisió** sobre quina és
canònica.

### 🔵 F3 — Taules d'instruccions RV32F inline
Les taules de l'extensió F (càrrega/emmagatzemament, aritmètiques, moviments,
comparacions, conversions) són inline a T5; a `/riscv/` només hi ha includes `RV32I_*`
(cap de l'extensió F). Possible tasca: factoritzar-les a includes si també han
d'aparèixer a `riscv.qmd`. → **decisió**.

---

## Pla d'execució proposat

**Bloc 1 — correccions no controvertides (sense aprovació):** B1 (refer multiplicació),
B2, B3, C1, C2, D1, E1. → lliurar `T5.qmd` corregit.

**Bloc 2 — decisions pendents (requereixen vistiplau):** D2, E3, F1, F2, F3.
