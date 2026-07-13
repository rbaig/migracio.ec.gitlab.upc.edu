# T5, E5, S5 — Llista d'accions de revisió interna (revisió Fable, 2026-07-12)

Fitxers revisats: `01_apunts/A5.qmd`, `02_exercicis/E5.qmd`, `03_solucions/S5.qmd` (+ `13_contrib.qmd §T5`, `21_riscv/RV32F_*.qmd`, `03_solucions/S_criteris_seleccio.qmd`, figures `22_figs_originals/T5_*.svg`).

Fonts de veritat consultades: especificació RV32F i conveni d'assemblador de RISC-V International (`@riscv_f_ext`, `@riscv_asm_manual` de `15_bibliografia.bib`) i codi font de RARS (comportament real del simulador de l'assignatura).

**Verificació numèrica: 98 comprovacions amb aritmètica exacta (fraccions + emulació RNE/GRS). Totes les traces d'A5 i S5 són correctes** (vegeu §6). Els errors detectats són de semàntica d'instruccions, coherència, veu i format.

## LLEGENDA

- 🔴 Error crític (contingut tècnicament incorrecte)
- 🟡 Error de rigor, menor o de llenguatge
- 🔵 Coherència / harmonització
- 🟠 Pedagogia
- ⏳ Pendent d'execució (Fase C, no requereix decisió)
- ❓ Requereix decisió de l'usuari
- ✅ Fet

---

## 1. ERRORS CRÍTICS (🔴)

### 1.1 ⏳ Transversal — `fcvt.w.s` NO trunca per defecte: afirmació incorrecta del mode d'arrodoniment

**Afirmació actual del projecte** (`13_contrib.qmd §T5`, ln 153): «`fcvt.w.s` trunca cap a zero (mode RTZ) independentment del `fcsr`. Per arrodonir al més pròxim cal afegir 0,5 abans de la conversió.» Reproduïda a A5 (`#tip-conversio-int-float`, comentari «[trunca cap a zero]» i paràgraf final), a S5 (`sol-p6-ops-rv32f-conversio`, apartats a, c i sobretot d) i al fragment `21_riscv/RV32F_instruccions_conversio.qmd` («(trunca)», usat també per `11_riscv.qmd`).

**Fets verificats contra les fonts de veritat:**

1. Espec. RV32F (`@riscv_f_ext`): `fcvt.w.s` s'arrodoneix **segons el camp `rm` de la instrucció**, no pas sempre RTZ.
2. Manual d'assemblador RISC-V (`@riscv_asm_manual`, §Floating-point rounding modes): escrita **sense** operand de mode (`fcvt.w.s a0, fa0`), s'usa **`dyn`** (el `frm` del `fcsr`). Cita textual: el mode es pot especificar com a operand addicional («`fcvt.w.s a0, fa0, rtz`»); «If unspecified, the default `dyn` rounding mode will be used».
3. RARS (codi font): `src/PseudoOps.txt` expandeix `fcvt.w.s t1, f1` → `fcvt.w.s RG1, RG2, dyn`, i `fcsr` s'inicialitza a 0 → `frm = 0` = **RNE**. Per tant, a RARS, `fcvt.w.s a0, fa0` **arrodoneix al més pròxim (parell)**, no trunca.

**Conseqüència concreta:** a S5 d), per a `f = 3.9`, el codi tal com està escrit (`fcvt.w.s a0, fa0`) dona a RARS `a0 = 4` (RNE), **no `a0 = 3`** com afirma la solució. El *cast* de C `(int)` sí que trunca, però perquè el compilador emet explícitament `fcvt.w.s rd, rs1, rtz`.

**Correcció a aplicar (Fase C):**

- `13_contrib.qmd §T5`: reescriure el punt: la instrucció s'arrodoneix segons `rm`; sense operand de mode → `dyn` → `frm` (RNE per defecte a RARS); el *cast* `(int)` de C es tradueix amb `fcvt.w.s rd, rs1, rtz`.
- `21_riscv/RV32F_instruccions_conversio.qmd`: «(trunca)» → «(arrodoniment segons `rm`; `rtz` per al *cast* de C)» a `fcvt.w.s`/`fcvt.wu.s` (edició única; propaga a A5 i `11_riscv.qmd`).
- A5 `#tip-conversio-int-float`: codi amb `fcvt.w.s a0, fa0, rtz` + paràgraf final reescrit (vegeu també la decisió D3 sobre el replantejament de l'exemple).
- S5 `sol-p6-ops-rv32f-conversio`: `rtz` als codis d'a) i c); reescriure l'explicació de d) (la conversió amb `rtz` trunca → 3; sense mode, RARS arrodoniria a 4).
- E5: l'enunciat no canvia (d) continua tenint sentit: «explica si es produeix truncament o arrodoniment»).

---

## 2. ERRORS DE RIGOR O MENORS (🟡)

### 2.1 ⏳ A5 — «la darrera revisió és de 2008» (ln 56)

Existeix IEEE 754-**2019**. Canviar a «la darrera revisió és de 2019». La menció posterior «L'IEEE-754 (revisió de 2008) defineix cinc modes» (ln 392) és històricament correcta (RMM s'hi va introduir el 2008) i es pot mantenir; opcionalment «des de la revisió de 2008».

### 2.2 ❓ S5 — `sol-p6-ops-variancia` a): justificació incorrecta de la seguretat de registres (paral·lel del bug de T4)

La taula d'anàlisi afirma que `i` i `m` han d'anar a registres segurs perquè «cal sobreviure a les crides». **Fals en tots dos casos:** `i` mor en acabar el bucle, *abans* de la primera crida a `mitjana`; `m` s'assigna *després* de la segona (i última) crida. Estrictament, només `vec` (usat entre les dues crides) i `q` (assignada abans de la segona crida i usada després) han de sobreviure a una crida. El codi és **correcte** (usar segurs de més és segur), però la justificació — que és precisament el que l'apartat a) demana raonar — és errònia. Opcions:

- **(A) recomanada**: mantenir el codi; reescriure la taula i el paràgraf distingint «ha de sobreviure a una crida» (`vec`, `q`) de «tria còmoda/uniforme» (`i`, `m`), fent explícit el raonament de vida de cada variable.
- **(B)**: versió mínima: `vec`→`s0`, `q`→`fs0`, `i`→temporal, `m`→temporal; BA de 412 B. Més fidel al criteri, però reescriu el codi i el disseny del BA.

### 2.3 ⏳ A5 — `#cau-exces-comparacio`: matís del signe (ln 100-107)

«Comparar nombres en coma flotant amb el mateix circuit que compara naturals» només val directament per a **nombres positius** (amb `S = 1` l'ordre de les codificacions s'inverteix: signe-magnitud, no Ca2). Afegir el matís («per a nombres del mateix signe positiu» o una frase breu sobre el cas negatiu).

### 2.4 ⏳ A5 — `§Denormals`: reformular l'exponent implícit (ln 353)

«L'exponent implícit és sempre −126, independentment del valor emmagatzemat al camp E (= 0000 0000)» és confús (E només pot valer 0). Reformular per remarcar la trampa real: l'exponent dels denormals és $1 - 127 = -126$ (el mateix que el normal més petit), **no** $0 - 127 = -127$.

### 2.5 ⏳ Figures SVG (`22_figs_originals/`) — terminologia i ortografia

| Figura | Correcció |
| :--- | :--- |
| `T5_recta_global.svg` | «les potències de 2 **estàn** equiespaiades» → «estan»; «±∞ si **M**=0, NaN si **M**≠0» → **F** (el camp emmagatzemat és la fracció; «M» contradiu la distinció fracció/mantissa del projecte). |
| `T5_recta_zoom_zero.svg` | «±0 si **M**=0, denormals si **M**≠0» → **F**. |
| `T5_taula_codificacions.svg` | Eix «**Mantissa (F)**» → «**Fracció (F)**». |
| `T5_exponent.svg` | «IEEE754» → grafia canònica (vegeu D1); opcional: notació `1,1754944e-38` vs `·10⁻³⁸` de les altres figures (harmonització menor). |

Les etiquetes «Mantissa:» de les rectes que mostren valors `1+0,99…` / `0+0,00000012` són **correctes** (mostren $1{,}F$ / $0{,}F$): no tocar. Editar només els fitxers font; el pre-render regenera `auto_figs/`.

### 2.6 ⏳ A5 — «Excés de l'exponent» → «Biaix de l'exponent» (taula `#nte-ieee754-formats`, ln 71)

`13_contrib.qmd` (§T1 i T5): «El valor numèric del biaix s'anomena "biaix" (no "excés")».

### 2.7 ⏳ S5 — reagrupar el binari de `sol-p6-ieee-interpretacio` c) (ln 60)

`$$A = +11{,}110011000000101011001 1_2$$` (22 bits sense agrupar, amb un espai espuri) → `$$A = +11{,}1100\,1100\,0000\,1010\,1100\,11_2$$`. Valor verificat correcte (≈ 3,797).

---

## 3. COHERÈNCIA (🔵)

### 3.1 ⏳ S5 — reordenar les solucions segons l'ordre dels enunciats d'E5

Criteri establert a T4 (§4.1 de `T4_P_tasques.md`). Ordre actual de «Suma i multiplicació» a S5: assemblador-cf → rv32f-memoria → rv32f-conversio → suma-simple → half-suma → half-multiplicacio → variancia. Ordre d'E5: **suma-simple → half-suma → half-multiplicacio → assemblador-cf → variancia → rv32f-memoria → rv32f-conversio**. Moure els blocs (sense canvis de contingut).

### 3.2 ❓ Grafia: «IEEE-754» (A5, ×13 + títols de callout + figures) vs «IEEE 754» (E5 ×7, S5 ×8, `S_criteris_seleccio`, majoria de `13_contrib`)

**Recomanació: «IEEE 754»** (grafia oficial de l'estàndard, «IEEE Std 754»; majoritària al repositori). Implica editar la prosa i títols de callout d'A5, `T5_exponent.svg` i la línia 144 de `13_contrib.qmd` («L'estàndard IEEE-754 en anglès…»). Els IDs (`#sec-ieee754`, `#tip-ieee754-*`, `#nte-ieee754-formats`…) **no** es toquen. Decisió global de grafia: confirma-la abans d'executar.

### 3.3 ⏳ «No associativitat» → «No-associativitat» (E5 ln 204, S5 ln 906, `S_criteris_seleccio` ln 89-90)

L'ortografia IEC prescriu guionet per a «no» + substantiu («no-associativitat», «no-distributivitat»); sense guionet davant adjectiu («no és associativa» ✓). A5 ja ho fa bé (`### No-associativitat`). Revisar també «No distributivitat» al títol de `sol-p6-assoc-distributiva` («Solució: no distributivitat…» → «no-distributivitat») i la cel·la de `S_criteris_seleccio`.

### 3.4 ❓ Taula de títols de callout de `13_contrib.qmd §Callouts` vs pràctica real

La taula diu `## M ISA —` i `## F ISA —`, però la pràctica uniforme del repositori és `## RV32IM ISA —` (A4, `11_riscv.qmd`) i `## RV32F ISA —` / `## RV32F ABI —` (A5, `11_riscv.qmd`). **Recomanació: actualitzar la taula de `13_contrib.qmd`** a la pràctica real (cap fitxer usa les formes curtes). Alternativa (descartable): renomenar tots els títols dels fitxers.

### 3.5 ⏳ A5 — títol de `#nte-instruccions-moviment-f`: «RV32F ABI — Moviments»

Conté només la pseudoinstrucció `fmv.s`. Proposta alineada amb T2/T3 («RV32I ABI — Pseudoinstruccions …»): «**RV32F ABI — Pseudoinstrucció `fmv.s`**» (o «— Pseudoinstruccions de còpia»).

### 3.6 ❓ A5 — `#tip-ieee754-codificacio`: dependència cap endavant d'arrodoniment i ULP

El tip (dins `§L'estàndard IEEE-754`) arrodoneix amb la regla RNE i usa el terme «ULP» abans que s'introdueixin (`§Arrodoniment` i `§Error de representació`, posteriors). La justificació inline actual el fa quasi autocontingut, però «ULP» hi apareix sense definir. Opcions:

- **(A) recomanada, mínima**: al pas d), substituir «(sumar 1 ULP al valor truncat)» per «(sumar 1 al bit de menys pes)» i afegir un punter explícit «(el criteri d'arrodoniment es formalitza a @sec-arrodoniment)».
- **(B)**: moure el tip després de `§Arrodoniment` (canvi d'estructura més gran; trenca el fil de la secció IEEE-754).

### 3.7 ⏳ E5 — «coprocessador de coma flotant» (`exr-p6-ops-assemblador-cf`, ln 131)

Terme heretat (MIPS); A5 presenta RV32F com a **extensió** amb registres propis, mai com a «coprocessador». Reformular: «…emmagatzemades als registres de coma flotant `fa2` i `fa4`…».

### 3.8 ❓ E5/S5 — títol de secció «Suma i multiplicació»

Conté també divisió, conversions i traducció a assemblador. Renomenar (p. ex. «Operacions») implicaria tocar E5, S5 i `S_criteris_seleccio`. **Recomanació: deixar-ho com està** (nom heretat, poc cost de confusió); decideix si vols el canvi.

### 3.9 ❓ A5 — `#tip-conversio-int-float`: exemple poc significatiu (lligat a 1.1)

La funció `arrodoneix(int n)` converteix un **enter** a `float`, hi suma 0,5 i trunca: per a qualsevol `n` enter retorna `n` — l'exemple mai no «arrodoneix» res. En corregir 1.1, opcions:

- **(A) recomanada**: replantejar amb entrada real: `int arrodoneix(float x)` → `fcvt.w.s a0, fa0, rtz` sobre `x + 0,5` (arrodoniment «al més pròxim, mig amunt» per a positius), contrastant-ho amb `fcvt.w.s a0, fa0` (RNE, empat al parell) i amb `rtz` sol (*cast* de C).
- **(B)**: mantenir l'estructura actual i només corregir la semàntica (menys valor pedagògic).

---

## 4. LLENGUATGE (🟡)

### 4.1 ⏳ E5 — veu dels enunciats: 2a singular → 2a plural (sistemàtic)

Convenció de `13_contrib.qmd §Problemari i solucionari` (aplicada a E4/E6; pendent d'E5 segons `TODO.md §T5`). ~28 línies: «Suposa→Suposeu», «Contesta→Contesteu», «Converteix→Convertiu», «Marca→Marqueu», «Expressa→Expresseu», «Determina→Determineu», «Calcula→Calculeu», «calcula'n→calculeu-ne», «Tradueix→Traduïu», «Escriu→Escriviu», «Tingues→Tingueu», «Dona→Doneu», «Fes→Feu», «Usa→Useu», «Converteix-los→Convertiu-los», «vegeu» ja ✓. En tancar-ho, eliminar l'entrada corresponent de `TODO.md §T5`.

### 4.2 ⏳ A5 — veu dels `#tip-`: 2a plural → 2a singular (12 línies)

Criteri revisat 2026-07 (revisió T2): els `{.callout-tip}` usen 2a **singular**. Línies 27, 133, 202, 425, 470, 492, 556, 578, 626, 670, 877, 922: «Expresseu→Expressa», «Codifiqueu…calculeu→Codifica…calcula», «Convertiu→Converteix», «Arrodoniu→Arrodoneix», «Calculeu→Calcula», «Comproveu→Comprova», «Convertiu…sumeu-hi…convertiu→Converteix…suma-hi…converteix», «Traduïu→Tradueix». Compte: **no** tocar els imperatius dels enunciats E5 (plural) ni el «Fixeu-vos/Observeu» del solucionari (vegeu 4.3).

### 4.3 ⏳ S5 — 1a persona del plural → veu impersonal (referència: S3, amb 0 ocurrències)

Línies 14 i 278 «Treballem amb…» → «Es treballa amb…» (o «Amb `A = …` i `B = …`:»); ln 40 «Descomposem» → «Es descompon cada valor…»; ln 58 «desplacem la coma» → «es desplaça la coma»; ln 828 «Triem registres» → «Es trien registres»; comentari de codi ln 862 «preservem l'argument» → «preserva l'argument». Els «Fixeu-vos» (ln 630, 1107) es mantenen (2a plural adreçada a l'estudiant, coherent amb «Observeu» de S3).

### 4.4 ⏳ S5 — separador decimal als blocs `.default`: punt → coma (~64 línies)

Els blocs de `sol-p6-ieee-interpretacio` (i tots els d'A5) usen coma («Mantissa = 1,111 0011…»), però de `sol-p6-ops-suma-simple` en avall s'usa punt («Mantissa = 1.0011111110», «B alineat: 0.0000101000…», «Producte = 1.1000…»). Harmonitzar-ho tot a **coma** (convenció catalana; coherent amb la notació $1{,}F$). Compte de no tocar els valors hexadecimals ni els «`b`» de sufix.

### 4.5 ⏳ A5 — «operam» → «operem» (ln 592).

### 4.6 ⏳ A5 — «Decodificar» (ln 208) i «Decodificació» (ln 499) → «Descodificar»/«Descodificació» (forma principal DIEC2; la resta del tema ja la usa).

### 4.7 ⏳ A5 — cometes rectes en prosa (ln 20): «la coma "es desplaça"» → «la coma «es desplaça»». Opcional: cometes del comentari TODO de la ln 6.

### 4.8 ⏳ S5 — dobles espais en prosa (ln 831-833, llista de registres de `sol-p6-ops-variancia`); es resol de passada amb 2.2.

### 4.9 ⏳ E5 — «números binaris» → «nombres binaris» (ln 30; «nombre» per a quantitat matemàtica).

### 4.10 ⏳ E5 — ln 12: «per ells mateixos» → «per si mateixos»; «una arquitectura Von Neumann» → «una arquitectura de Von Neumann» (pràctica d'A1).

### 4.11 ⏳ E5 — ln 131: reformular «l'assemblador no admet nombres decimals fraccionaris en qualsevol context» (ambigu) → p. ex. «l'assemblador només admet literals fraccionaris a les directives de dades (`.float`), mai com a operands d'instrucció».

### 4.12 ⏳ Cursives repetides de *sticky*: primera aparició per fitxer en cursiva ✓ (A5 ln 411, E5 ln 110); aparicions posteriors sense cursiva (A5 ln 734, 759; E5 ln 209).

---

## 5. VERIFICAT CORRECTE (sense acció) — per no repetir feina

**Verificació numèrica exhaustiva (98 comprovacions, aritmètica exacta):**

- A5: codificació −1029,68 → `0xC480B5C3`, error 0,44/8192 ≈ 5,371·10⁻⁵ ✓; descodificació `0x45814140` = 4136,15625 ✓; $v_{\max}$ ✓; taula RNE (5 casos) ✓; exemple GRS del `#wrn-bits-guarda` ✓; suma base 10 ✓; suma IEEE `0x3F40000D + 0xC0800004 = 0xC0500005`, error 2⁻²⁴ ≈ 6·10⁻⁸ ✓ (la correcció pre-Fable B1/B3 és bona); multiplicació base 10 ✓; multiplicació IEEE → `0xBEB60002` ✓; divisió 8/3 → `0x402AAAAB` ✓; contraexemple de no-associativitat ✓.
- S5: interpretació (naturals, Ca2, floats ≈3,797 / ≈−1,272·10³⁵, descodificació d'instruccions `sub t0,t1,t2` i `addi a0,s0,-100`) ✓; classificació de patrons ✓; rang (3 valors i hex) ✓; decimal→hex (5 valors; error de 44,4 = 0,2/131072 ≈ 1,526·10⁻⁶) ✓; simple/doble precisió (4 codificacions, tots exactes, hex de 64 bits inclosos) ✓; suma simple → `0x41820000` = 16,25 exacta ✓; *half*: suma a (absorció, G=0 amb R=S=1) i b (`0x4DF0` = 23,75, fites d'error) ✓; multiplicació a (`0x5215`) i b (`0x785F` = 35 808, cas límit e=15, error absolut vs relatiu) ✓; no-associativitat a ✓; no-distributivitat a (les 5 operacions, inclòs l'únic empat «al parell»: `A×B` = `0x280A` amb residu exactament ½ ULP; camins exactes 15,21533/15,21906) i b (2128 exacte; `0xFB3F` = −59 360; sobreeiximents → ±∞ → NaN; |A×B| ≈ 2,26·10⁵ i |A×C| ≈ 2,85·10⁵, coherents amb els «≈2,3/2,8·10⁵» del text) ✓; 3,9 emmagatzemat = 3,9000000953… ✓.
- E5: tots els valors de `exr-p6-ieee-half-a`/`-half-b` codifiquen **exactament** als hex reutilitzats per la resta d'exercicis ✓; la correspondència declarada half-b (b,c) ↔ distributiva (a,b) és correcta ✓.
- Enunciats no seleccionats: ben plantejats (suma-simple2 → `0xC05D7000` = −3,4599609375 exacte; multiplicació → `0x40000000` = 2,0 exacte; divisions *half* exactes; assoc-suma b → 41,1875 ≠ 41,21875, demostra la propietat).

**Altres comprovacions:** cobertura de S5 = `S_criteris_seleccio.qmd` (14 solucions, `assoc-suma` només apartat a, per disseny) ✓; totes les referències creuades sortints resolen (A1/A2/A3/A9) ✓; les 4 figures + `T5_fcsr` (`registres.toml`) existeixen ✓; sigles ULP/NaN/IEEE/RNE a `12_sigles_simbols.qmd` ✓; fragments `21_riscv/RV32F_*` conformes a l'espec (mapa ABI `f0`–`f31`, semàntica d'instruccions, `flt.s` amb NaN → 0, `fmv.s` = `fsgnj.s`, F depèn de Zicsr, camps i codis del `fcsr`) ✓, amb l'única excepció del «(trunca)» de 1.1; valors numèrics de les figures (1,1754942/1,1754944·10⁻³⁸, 3,4028235·10³⁸, 2²³−1 denormals) ✓; alineació i offsets del BA de `variancia` (420 B, epíleg simètric) ✓; codi RISC-V de totes les solucions semànticament correcte ✓.

---

## 6. PENDENTS HERETATS QUE ROMANEN OBERTS

- ~~`TODO.md §T5 F1`: figures addicionals~~ **Resolta el 2026-07-13** (vegeu §Figures noves creades, més avall): ja no és pendent.
- `TODO.md §T5 P8`: dependència endavant `fcsr` → `@nte-zicsr` — ja gestionada com a punter explícit; cap acció.
- `TODO.md §Tasques transversals`: migració d'IDs `p<N>-` → `t<N>-` (Claude Code, tot el repositori) — **no es toca aquí**; E5/S5 mantenen `p6-` coherent internament.
- Fitxers `22_figs_originals/T5_*__org.svg` i `T5_*__drawio.svg` no referenciats per A5: neteja opcional (housekeeping, fora d'abast).

---

## RESUM DE DECISIONS (totes resoltes, 2026-07-13)

| # | Ítem | Resolució |
| :--- | :--- | :--- |
| D1 | §3.2 Grafia «IEEE 754» vs «IEEE-754» | ✅ Adoptada «IEEE 754» (oficial i majoritària) |
| D2 | §3.4 Taula de títols de callout de `13_contrib` | ✅ Actualitzada a la pràctica real (`RV32IM ISA —`, `RV32F ISA/ABI —`) |
| D3 | §2.2 `variancia`: justificació de registres | ✅ Opció A aplicada (codi mantingut, anàlisi reescrita: només `vec` i `q` han de sobreviure a una crida) |
| D4 | §3.9 Replantejament del `#tip-conversio-int-float` | ✅ Opció A aplicada (entrada `float`, contrast `rtz`/`dyn`+RNE amb 2,5 i 3,5) |
| D5 | §3.6 Dependència endavant del `#tip-ieee754-codificacio` | ✅ Opció A aplicada (reformulació sense «ULP» + punter a @sec-arrodoniment) |
| D6 | §3.8 Títol de secció «Suma i multiplicació» | ✅ Mantingut sense canvis |
| (a) | Harmonització notacional `21_riscv/` RV32I/RV32M | ✅ Verificat: **ja estava fet** a tot `21_riscv/` (RV32I, RV32M, RV32F); no calia cap canvi |
| (b) | Taula ABI inline d'A5 vs. include | ✅ Es manté sense canvis (resum de 3 categories vs. desglossament ABI de 6 trams) |
| (c) | Taules de camps de `fcsr` | ✅ Es mantenen inline |
| (d) | Ordre de la taula de codificacions especials vs. subseccions | ✅ Subseccions reordenades: Zero → Denormals → Infinit → NaN (coincidint amb l'ordre de la taula) |
| (e) | Criteris de numeració/aparença de callouts | ✅ Documentat: numeració ja nativa via `_quarto.yml §language` (`crossref-*-prefix`); icones `tip`/`important` es deixen amb les de Quarto per defecte (decidit, sense homogeneïtzar amb `note`/`warning`/`caution`) |
| F1 | Figures addicionals pendents (S\|E\|F, recta rang/precisió, esquema GRS) | ✅ (1) i (3) creades en aquest xat; (2) ja existia (`T5_recta_global.svg` + `T5_recta_zoom_zero.svg`) — vegeu detall a §Figures noves més avall |

---

## FIGURES NOVES CREADES (F1, 2026-07-13)

**F1(1) — Disposició de bits S\|E\|F (32 bits):** entrada `T5_ieee754_format` afegida a `24_specs/registres.toml`, generada pel pipeline existent `gen_regs.py` (mateix mecanisme que `T5_fcsr` i `T5_instruccio_tipus_R4`; validat sense errors). Inserida a `A5.qmd` com `#fig-ieee754-format`, just després de la fórmula S·E·F i abans dels subapartats de cada camp. Colors: S vermell, E ambre, F blau (paleta pròpia de `gen_regs.py`).

**F1(2) — Recta numèrica rang/precisió amb denormals:** revisat i confirmat que **ja existia**, repartida en dues figures ja inserides: `T5_recta_global.svg` (rang complet, a §Rang i precisió) i `T5_recta_zoom_zero.svg` (detall dels denormals al voltant de zero, a §Denormals). Cap acció necessària; l'entrada del TODO estava desactualitzada.

**F1(3) — Esquema d'arrodoniment GRS:** SVG natiu nou `22_figs_originals/T5_grs_esquema.svg`, estil pla coherent amb `T5_recta_global.svg` (sense dependència d'Inkscape). Mostra la mantissa retinguda, els tres bits G/R/S acolorits i etiquetats, i un resum de la regla RNE. Inserida a `A5.qmd` com `#fig-grs-esquema`, després de la llista de definicions G/R/S i abans de la taula de la regla RNE.

**Fitxers nous/modificats per aquesta tasca:** `24_specs/registres.toml` (entrada `T5_ieee754_format` afegida), `22_figs_originals/T5_grs_esquema.svg` (nou), `A5.qmd` (dues insercions de figura). S'adjunta també el SVG ja generat (`T5_ieee754_format__registre_light.svg`) per revisió visual immediata; el pipeline de pre-render de Quarto el regenerarà igualment a partir del TOML.

---

## NOVA EINA: RETALLS (CROPS) SVG A PARTIR D'UNA FIGURA FONT ÚNICA (2026-07-13)

A petició de l'usuari, s'ha construït un mecanisme genèric perquè una figura "detall"/"zoom" es pugui definir com una simple finestra `(x, y, w, h)` sobre el `viewBox` d'una figura font ja existent, evitant mantenir dues fonts sincronitzades manualment quan el detall és un subconjunt visual net de la figura completa.

**Fitxers nous:**
- `25_scripts/gen_crops.py`: script generador (coherent amb l'estil de `gen_regs.py`/`norm_font.py`). Només reescriu `viewBox`/`width`/`height` de l'element arrel; no toca cap altre contingut del SVG.
- `24_specs/retalls.toml`: fitxer de definicions (encara buit, amb l'esquema documentat com a comentari — llest per al primer ús real).

**Fitxers modificats:**
- `_quarto.yml`: nou pas al `pre-render`, `gen_crops.py`, inserit entre `gen_regs.py` i `gen_dark.py` (necessita la font ja normalitzada per `norm_font.py`, i el retall generat ha de rebre la seva variant dark de `gen_dark.py`).
- `13_contrib.qmd §Figures i material gràfic`: nova subsecció «Retalls (crops) d'una figura font única» documentant el format del TOML i la condició d'aplicabilitat.
- `TODO.md §Tasques transversals`: entrada nova descrivint l'eina disponible.

**Verificació realitzada:** script provat de cap a cap (validació de camps obligatoris, detecció de fitxer font inexistent, retall real sobre `T5_recta_global.svg` renderitzat i inspeccionat visualment, comportament net amb `retalls.toml` buit o inexistent, `_quarto.yml` validat com a YAML sintàcticament correcte).

**Cap ús real encara.** Es va valorar aplicar-lo dues vegades:

1. Unificar `T5_recta_zoom_zero.svg` com a retall de `T5_recta_global.svg` — **descartat**: `T5_recta_zoom_zero.svg` no és geomètricament un subconjunt de `T5_recta_global.svg` — és un dibuix diferent (fet a Inkscape, amb la seva pròpia disposició) que mostra informació pròpia dels denormals (per exemple hexadecimals concrets com `0x00000001`) que la recta global no té espai per representar.
2. A petició de l'usuari, es va investigar `22_figs_originals/T5_coma_flotant_racionals__drawio.svg` (7465 línies, viewBox 1640×490), un fitxer **orfe** (no referenciat per cap `.qmd`) que sembla l'esborrany original a partir del qual es van crear manualment `T5_recta_global.svg` i `T5_recta_zoom_zero.svg` — mostra tot el contingut (rang global + zoom de zero + denormals) en un sol dibuix. Renderitzat i comparat visualment amb les figures actuals: **descartat també en l'estat actual**, perquè el drawio (estil amb fletxes i icones pròpies de drawio) no comparteix coordenades ni disseny amb `T5_recta_global.svg` (estil pla, 73 línies) — les figures actuals són una **reconstrucció completa** en un altre estil, no un retall del drawio.

**TODO futur (anotat a `TODO.md §Tasques transversals`):** investigar l'ús de `gen_crops.py` directament sobre una figura global com la primigènia, és a dir, com a **font única redibuixada des de zero** (en estil pla natiu, no drawio) en lloc d'intentar-lo a posteriori sobre figures ja separades. Implicaria: (i) redibuixar el contingut complet (rang global + zoom + denormals) com a única font de veritat; (ii) definir a `retalls.toml` les finestres corresponents a les vistes actuals com a retalls d'aquesta font; (iii) verificar que cada retall és net. Fora de l'abast d'aquesta revisió textual (implica redibuixar una figura complexa des de zero).

Les tres figures es mantenen com a fitxers independents, tal com ja estaven.

---

## FITXERS MODIFICATS EN AQUESTA REVISIÓ (Fase C, 2026-07-13)

`01_apunts/A5.qmd` · `02_exercicis/E5.qmd` · `03_solucions/S5.qmd` · `13_contrib.qmd` · `21_riscv/RV32F_instruccions_conversio.qmd` · `03_solucions/S_criteris_seleccio.qmd` · `22_figs_originals/T5_recta_global.svg` · `22_figs_originals/T5_recta_zoom_zero.svg` · `22_figs_originals/T5_taula_codificacions.svg` · `22_figs_originals/T5_exponent.svg` · `TODO/TODO.md` · `24_specs/registres.toml` · `22_figs_originals/T5_grs_esquema.svg` (nou) · `25_scripts/gen_crops.py` (nou) · `24_specs/retalls.toml` (nou) · `_quarto.yml`

Verificat abans i durant l'execució: el repositori remot va rebre canvis externs a `13_contrib.qmd`/`CLAUDE.md`/`TODO.md` i altres `Ax.qmd` (T1–T4, L1–L3) provinents d'altres sessions de treball, sense solapament amb les línies editades per aquesta revisió de T5. Les meves edicions de `13_contrib.qmd` i `TODO.md` s'han refet sobre la base remota més recent per no perdre aquell treball independent.
