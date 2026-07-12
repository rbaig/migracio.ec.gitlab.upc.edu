# T4, E4, S4 — Llista d'accions de revisió interna (revisió Fable, 2026-07-12)

*Actualitzat amb els canvis del repositori del 2026-07-12 (commits `77853ff`, `e75ed4e` i `8f3038f`: Fase C de T6 acabada, Fase B de T2 iniciada, renom `12_sigles.qmd`→`12_sigles_simbols.qmd`).*

**Nota sobre el commit `8f3038f`** (rename de `12_sigles.qmd` a `12_sigles_simbols.qmd`, secció «Símbols» pendent, i tasca transversal nova «Exercicis→Problemes»): no afecta directament `A4.qmd`/`E4.qmd`/`S4.qmd` (cap referència ni contingut de T4 en depenia), però el meu `13_contrib.qmd` (tocat per la tasca 4.8) citava el nom antic del fitxer a la secció T6 (§Sigles CMOS i CF) — **corregit** a `12_sigles_simbols.qmd`, ja aplicat al fitxer adjunt. La nova tasca transversal «Exercicis→Problemes» és d'abast global, no específica de T4; no s'ha creat cap ítem nou al fitxer de tasques per aquest motiu.

## ✅ ESTAT: TANDA C1 COMPLETADA (Sonnet High, sense Thinking)

Executades totes les tasques d'edició dirigida (seccions 1, 2, 4, 5, i els retocs de `13_contrib.qmd`/`svg.md`), aplicant en cada cas la **recomanació** indicada al fitxer (no vas confirmar cap decisió alternativa abans de C1). Detall de com s'han resolt els ítems ❓:

- **2.1** (`sw`→`sh` a `exr-p5-seq-short` a): aplicada l'opció recomanada, enunciat modificat.
- **2.2** (`exr-p5-mul-instruccions` a, no-unicitat): **NO tocat** — la resolució (presentar les dues respostes) pertany a la solució nova de §7, que és feina de la **Tanda C2**. L'enunciat es manté igual.
- **2.8** (`addi`→`li`+`add` amb N genèrica): aplicada l'harmonització recomanada.
- **4.2** (paràgraf de `sol-p5-seq-bucles` amb conceptes de T7): **NO tocat** — cap opció és clarament «recomanada per defecte» sense la teva confirmació explícita (implica registrar un punter nou a `13_contrib.qmd`). Continua pendent, vegeu més avall.
- **4.7** (`exr-p5-opt-variable-induccio` b/c): aplicada la reformulació recomanada (b sense condició al final, c la combina).
- **3** (matís `mul` mòdul 2ⁿ): **NO tocat** — és una decisió de contingut nou (afegir o no un callout a la teoria) que vaig marcar com a pendent de la teva confirmació explícita; no n'hi ha cap opció per defecte prou clara com per aplicar-la sense guiatge.
- **7.9** (`exr-p5-div-programa`, formulació): **NO tocat** — pertany a la solució nova, Tanda C2.
- **8** (figures half/full-adder): **NO tocat** — decisió de contingut nou, no és edició dirigida.

**Fitxers resultants d'aquesta tanda**: `A4.qmd`, `E4.qmd`, `S4.qmd`, `13_contrib.qmd`, `svg.md` (tots adjunts).

### Decisions que resten obertes per a tu (no s'han aplicat perquè no tenen recomanació per defecte prou clara, o depenen de contingut nou)

| # | Ítem | Estat |
|:---:|:---|:---|
| 3 | Matís `mul` mòdul 2ⁿ (callout nou a A4) | Pendent — decisió de contingut, Tanda C2 si s'aprova |
| 4.2 | Punter T4→T7 a `sol-p5-seq-bucles` | Pendent — implica registrar entrada nova a `13_contrib.qmd §Direccionalitat` |
| 8 | Figures half/full-adder (crear o eliminar TODO) | Pendent — decisió de contingut, fora d'abast de C1/C2 tal com estava previst |

Substitueix el fitxer de la revisió pre-Fable.

--- Els ítems tancats d'aquella revisió que ja són a `main` (callout `#cau-ec-no-overflow`, reordenació d'E4, terminologia arrossegament/sobreeiximent, refs selectives, neteja de `{#sec-}` dins callouts) no es repeteixen aquí.

## LLEGENDA
- ✅ Fet / verificat
- ⏳ Pendent d'execució (Fase C, sense decisió de l'usuari)
- ❓ Requereix decisió de l'usuari
- 🔴 Error crític (aritmètic o tècnic)
- 🟡 Error menor, de rigor o lingüístic
- 🔵 Millora pedagògica o de coherència

---

## 1. ERRORS CRÍTICS (🔴) — correccions a S4 mai incorporades al repositori

La revisió pre-Fable els va marcar com a corregits, però `S4.qmd` a `main` encara conté les taules errònies (verificat per recàlcul complet). Les taules correctes es donen aquí senceres perquè la Fase C les pugui incorporar directament.

**Convenció unificada de les taules de seguiment** (afegir com a nota al callout): cada fila mostra l'estat **final** de la iteració; les columnes MR[0]/Signe i Acció indiquen el que s'ha **executat en aquella iteració** (decidit amb el valor **abans** del desplaçament); la fila inicial porta «—».

### 1.1 ✅ S4 — `sol-p5-mul-passos` a) — taula errònia des de la iteració 2

Error sistemàtic: llegia MR[0] post-desplaçament. El binari final mostrat (`001100 111000₂` = 824) no és 760. Taula correcta:

| Iter. | P (12 bits) | MD (12 bits) | MR (6 bits) | MR[0] | Acció |
| :---: | :---: | :---: | :---: | :---: | :--- |
| inicial | `000000 000000` | `000000 101000` | `010011` | — | — |
| 1 | `000000 101000` | `000001 010000` | `001001` | 1 | suma |
| 2 | `000001 111000` | `000010 100000` | `000100` | 1 | suma |
| 3 | `000001 111000` | `000101 000000` | `000010` | 0 | no suma |
| 4 | `000001 111000` | `001010 000000` | `000001` | 0 | no suma |
| 5 | `001011 111000` | `010100 000000` | `000000` | 1 | suma |
| 6 | `001011 111000` | `101000 000000` | `000000` | 0 | no suma |

Resultat: $P = 001011\,111000_2 = 760_{10}$ ✓ (40 × 19; comprovació: 40 + 80 = 120; 120 + 640 = 760).

### 1.2 ✅ S4 — `sol-p5-mul-passos` b) — columnes MR[0]/Acció desfasades una iteració

P i resultat final (216) correctes. Taula correcta:

| Iter. | P (12 bits) | MD (12 bits) | MR (6 bits) | MR[0] | Acció |
| :---: | :---: | :---: | :---: | :---: | :--- |
| inicial | `000000 000000` | `000000 110110` | `000100` | — | — |
| 1 | `000000 000000` | `000001 101100` | `000010` | 0 | no suma |
| 2 | `000000 000000` | `000011 011000` | `000001` | 0 | no suma |
| 3 | `000011 011000` | `000110 110000` | `000000` | 1 | suma |
| 4 | `000011 011000` | `001101 100000` | `000000` | 0 | no suma |
| 5 | `000011 011000` | `011011 000000` | `000000` | 0 | no suma |
| 6 | `000011 011000` | `110110 000000` | `000000` | 0 | no suma |

Resultat: $P = 000011\,011000_2 = 216_{10}$ ✓ (54 × 4).

### 1.3 ✅ S4 — `sol-p5-div-passos` — reformatar i corregir valors intermedis

Format net: columna «R − D» amb el valor intermedi de la resta; columna «R (final)» amb l'estat ja restaurat si cal; sense files intercalades de restauració; fila inicial amb «—».

**a) X = `101000` (40) ÷ Y = `010011` (19)** — errors als valors de R−D de les iteracions 1–3 de la versió actual:

| Iter. | D (12 bits) | R − D | Signe | Acció | R (final) | Q |
| :---: | :---: | :---: | :---: | :--- | :---: | :---: |
| inicial | `010011 000000` | — | — | — | `000000 101000` | `000000` |
| 1 | `001001 100000` | `110111 001000` | neg. | restaura; `Q<<1` | `000000 101000` | `000000` |
| 2 | `000100 110000` | `111011 111000` | neg. | restaura; `Q<<1` | `000000 101000` | `000000` |
| 3 | `000010 011000` | `111110 010000` | neg. | restaura; `Q<<1` | `000000 101000` | `000000` |
| 4 | `000001 001100` | `111111 011100` | neg. | restaura; `Q<<1` | `000000 101000` | `000000` |
| 5 | `000000 100110` | `000000 000010` | pos. | `Q = (Q<<1)\|1` | `000000 000010` | `000001` |
| 6 | `000000 010011` | `111111 101111` | neg. | restaura; `Q<<1` | `000000 000010` | `000010` |

Quocient $Q = 000010_2 = 2$, residu $R[5{:}0] = 000010_2 = 2$ ✓ (19 × 2 + 2 = 40 ✓).

**b) X = `010101` (21) ÷ Y = `100100` (36)** — substituir el resum «1–6 sempre negatiu» pel detall complet:

| Iter. | D (12 bits) | R − D | Signe | Acció | R (final) | Q |
| :---: | :---: | :---: | :---: | :--- | :---: | :---: |
| inicial | `100100 000000` | — | — | — | `000000 010101` | `000000` |
| 1 | `010010 000000` | `101110 010101` | neg. | restaura; `Q<<1` | `000000 010101` | `000000` |
| 2 | `001001 000000` | `110111 010101` | neg. | restaura; `Q<<1` | `000000 010101` | `000000` |
| 3 | `000100 100000` | `111011 110101` | neg. | restaura; `Q<<1` | `000000 010101` | `000000` |
| 4 | `000010 010000` | `111110 000101` | neg. | restaura; `Q<<1` | `000000 010101` | `000000` |
| 5 | `000001 001000` | `111111 001101` | neg. | restaura; `Q<<1` | `000000 010101` | `000000` |
| 6 | `000000 100100` | `111111 110001` | neg. | restaura; `Q<<1` | `000000 010101` | `000000` |

Quocient $Q = 0$, residu $R[5{:}0] = 010101_2 = 21$ ✓.

### 1.4 ✅ S4 — `sol-p5-matrius-func-veci` b) — `main` corromp `p` i `fi` en cridar `func`

`main` guarda `p` a `t0` i `fi` a `t1`, però `func` (apartat a de la mateixa solució) sobreescriu `t0`, `t1` i `t2`: després de la primera crida el bucle és incorrecte. Cal usar **registres segurs** (`s0`, `s1`) desats al BA, i explicar-ho al text de la solució (concepte de T3). Codi correcte:

```{.s filename="RV32I"}
main:
        addi    sp, sp, -12
        sw      ra, 8(sp)
        sw      s1, 4(sp)
        sw      s0, 0(sp)

        la      s0, mati            # s0 = p = @mati[0][0]  (segur: sobreviu a la crida)
        addi    s1, s0, 5*4*4       # s1 = fi = @mati[5][0]
        bgeu    s0, s1, fimain      # comprovació inicial (5 > 0, mai s'executa)
bucle:
        mv      a0, s0              # a0 = p
        jal     ra, func
        addi    s0, s0, 4*4         # p += 4  (4 ints = 16 bytes)
        bltu    s0, s1, bucle
fimain:
        lw      s0, 0(sp)
        lw      s1, 4(sp)
        lw      ra, 8(sp)
        addi    sp, sp, 12
        ret
```

BA de 12 bytes (múltiple de 4, criteri EC ✓). Ajustar el text introductori de l'apartat b («p → `t0`, fi → `t1`» → registres segurs, amb el motiu).

---

## 2. ERRORS DE RIGOR O MENORS (🟡)

### 2.1 ✅ E4 — `exr-p5-seq-short` a) — `sw` + escalat ×4 sobre un vector de `short`

El codi donat (`slli t2, t2, 2` + `sw zero`) escriu 4 bytes (dos `short`) a `p1[2(p2+3)]` i `p1[2(p2+3)+1]`: no s'expressa netament amb «una única sentència» en C sobre `short`. Herència probable d'una versió amb `int`. **Proposta**: canviar l'enunciat a `slli t2, t2, 1` + `sh zero, 0(t2)` → resposta neta `p1[p2+3] = 0;` (coherent amb l'apartat b, que sí que treballa amb `short`). *Decisió: modificar l'enunciat (recomanat) o mantenir-lo i acceptar la resposta amb cast `*(int *)&p1[...]`.*

### 2.2 ⏳ E4 — `exr-p5-mul-instruccions` a) — la resposta no és única

`mul` opera mòdul $2^{32}$: tant `t2 = 0xFFFFFFFD` (−3) com `t2 = 0x7FFFFFFD` donen `2 × t2 ≡ 0xFFFFFFFA`. *Decisió*: (a) restringir l'enunciat (p. ex. «sabent que `t2` conté un enter negatiu») o (b) mantenir-lo i que la futura solució presenti les dues respostes vàlides (didàcticament interessant: enllaça amb l'ítem 3). Recomanació: (b).

### 2.3 ✅ E4 — `exr-p5-div-programa` — explicitar quin registre és el dividend

«dos naturals ... guardats als registres `t3` i `t1`» és ambigu. Reescriure: «... el dividend al registre `t3` i el divisor a `t1`».

### 2.4 ✅ E4 — `exr-p5-seq-diagonal-ptr` — condició N ≤ M no declarada

El recorregut amb `p += M + 1` només escriu la diagonal `matriu[i][i]` per a tot `i` si $N \leq M$; si $N > M$ el punter «cau» de la diagonal. Afegir a l'enunciat «Suposa que `N` i `M` són constants, amb $N \leq M$» (criteri de rigor anàleg al de T8 sobre dades implícites).

### 2.5 ✅ E4 — `exr-p5-sr-overflow-naturals-8bits` — préstec a l'apartat d)

L'apartat d) és una resta: el concepte pertinent és el **préstec** (*borrow*, definit a A1), no l'arrossegament. Reescriure el peu de l'enunciat: «... indica si s'ha produït arrossegament (*carry*) o, en el cas de la resta, préstec (*borrow*)».

### 2.6 ✅ S4 — `sol-p5-matrius-adreces` f) — prosa contradiu el codi

La frase «cal `mul` tant per calcular la fila com per escalar-la per `NC`» suggereix dues multiplicacions; el codi (correcte) ho resol amb un únic `mul` per l'invariant `10*NC*4`. Reescriure: «les dues multiplicacions es fusionen en una: l'invariant `10*NC*4` permet resoldre-ho amb un únic `mul`».

### 2.7 ✅ A4 — `tip-sumacolumna-sequencial` — afirmació categòrica sobre NC

«Com que `NC` no és potència de 2» → «Com que, en general, `NC` no té per què ser potència de 2» (coherent amb la formulació de `@sec-extensio-m`).

### 2.8 ✅ S4 — `sol-p5-seq-bucles` a) — `addi t4, t3, N*4` amb N genèrica

Amb `N` simbòlica, `N*4` pot excedir el rang de l'immediat de 12 bits (N > 511). El patró de la teoria (opt. #3) és `li` + `add`. *Decisió*: harmonitzar amb `li t2, N*4` + `add t4, t3, t2` (robust) o mantenir `addi` (més curt; vàlid per a N petites). Recomanació: harmonitzar.

### 2.9 ✅ S4 — `sol-p5-sr-overflow-enters-8bits` b) — carry descartat no mostrat

La suma de b) també genera *carry-out* (231 + 34 = 265 > 255), però el bloc no el mostra, a diferència de l'apartat a). Mostrar `1 0000 1001` amb la mateixa anotació «(descartant el carry de sortida: 0x09)».

### 2.10 ✅ A4 — dobles espais (lint)

Línies 464 i 466 («inicialitzar un····punter», «sumar-li····l'stride») i espai final sobrer a la línia 344. Repassar la resta del fitxer amb el criteri de linting de `13_contrib.qmd` (fora de blocs de codi).

---

## 3. MATÍS `mul` MÒDUL 2ⁿ — pendent P3 heretat d'A1 (❓)

El pendent (decisió P3 de la revisió interna d'A1, 2026-07-11) demana valorar, en treballar T4, si cal un matís explícit que connecti el mètode signe+magnituds d'A1 amb el fet que `mul` no distingeix signes. *(L'entrada corresponent de `TODO/TODO.md` ja ha estat retirada en el commit del 2026-07-12: la propietat del pendent és d'aquest xat i es tanca aquí, en un sentit o altre.)*

**Anàlisi**: A4 presenta a `@sec-algorisme-multiplicacio` l'algorisme general (valors absoluts + ajust de signe) i a `@sec-sobreeiximent-en-la-multiplicacio` el paper de `mulh`/`mulhu`, però enlloc no s'explicita *per què* hi ha un únic `mul` vàlid per a enters i naturals mentre que la part alta necessita tres variants. El matís tanca aquest buit i, a més, dona la clau de la no-unicitat de l'ítem 2.2.

**Proposta (recomanada)**: afegir a A4 un callout d'Aprofundiment just després del bloc de detecció de sobreeiximent de `@sec-sobreeiximent-en-la-multiplicacio`:

```markdown
::: {#wrn-mul-modul-2n .callout-warning collapse=true}
## Per què `mul` no distingeix el signe dels operands

A @sec-algorisme-multiplicacio s'ha presentat l'algorisme general per a enters:
treballar amb els valors absoluts i ajustar el signe al final. Estrictament, però,
per a la part **baixa** del resultat aquest ajust no és necessari: el producte
mòdul $2^n$ (els $n$ bits de menys pes) és **idèntic** tant si els operands
s'interpreten com a naturals com si s'interpreten com a enters en Ca2. Per això
RV32M té una única instrucció `mul` per als bits $[31{:}0]$, vàlida per a tots
dos casos. En canvi, la part **alta** ($[63{:}32]$) sí que depèn de la
interpretació dels operands, i per això existeixen `mulh`, `mulhu` i `mulhsu`.
:::
```

*Opcions*: (a) `#wrn-` com el de dalt (recomanada: no avaluable, no trenca la línia pedagògica); (b) nota breu al cos del text; (c) descartar (donar-ho per cobert amb `mulh`/`mulhu`).

---

## 4. COHERÈNCIA (🔵)

### 4.1 ✅ S4 — reordenar seccions

Ordre actual: Suma i resta → Multiplicació → **Divisió** → Matrius → Accés seqüencial. Harmonitzar amb A4/E4: Suma i resta → Multiplicació → Matrius → Accés seqüencial → **Divisió** (moure el bloc `## Divisió` + `sol-p5-div-passos` al final). Les solucions noves (§7) s'insereixen a la secció corresponent seguint l'ordre dels enunciats d'E4.

### 4.2 ❓ S4 — `sol-p5-seq-bucles` — paràgraf «Contrast entre els dos recorreguts» amb conceptes de T7

Usa «fallades de memòria cau», «línia de cau» i «localitat espacial», no introduïts fins a T7, sense punter explícit (la llista de punters acceptats de `13_contrib.qmd §Direccionalitat` no inclou T4 → T7). *Opcions*: (a) afegir el punter «(aquests conceptes s'estudien a @sec-tema-mc)» i registrar T4 → T7 a la llista de `13_contrib.qmd`; (b) suavitzar la redacció sense termes de T7 («el recorregut per fila accedeix a posicions consecutives de memòria, cosa que el maquinari de la jerarquia de memòria aprofita millor; ho veureu a T7»); (c) eliminar el paràgraf. Recomanació: (a).

### 4.3 ✅ E4 + S4 — `void main()` → `int main()`

`exr-p5-matrius-func-veci` usa `void main()`; el precedent d'E2/E3 és `int main()`. Harmonitzar a E4 i al bloc C reproduït dins `sol-p5-matrius-func-veci`.

### 4.4 ✅ E4 — «estudiat a classe» (2×)

`exr-p5-mul-algorisme` i `exr-p5-div-algorisme`: el material és un llibre autocontingut → «estudiat a la teoria» (les refs `@thm-...` ja hi són).

### 4.5 ✅ S4 — `sol-p5-matrius-func-veci` a) — comentari «NC=4»

El 4 és la longitud del vector `veci`, no un NC: «# comprovació inicial (longitud 4 > 0: mai no s'executa)».

### 4.6 ✅ S4 — `sol-p5-opt-condicio-final` b) — referenciar el prerequisit

On diu «S'han extret `li t1, N` i `la t2, v` com a invariants fora del bucle», afegir la referència: «(extracció d'invariants, @sec-extraccio-invariants, prerequisit de tota optimització)».

### 4.7 ✅ E4 — `exr-p5-opt-variable-induccio` — sigla «IV» i solapament b)/c)

c) usa «eliminació IV» (sigla no definida enlloc) → desenvolupar «eliminació de la variable d'inducció». A més, la solució de b) ja incorpora la condició al final, i c) queda buit (la solució actual ho reconeix honestament). *Opcions*: (a) reformular b) perquè demani només l'eliminació de la variable d'inducció mantenint la condició a l'inici, i que c) faci la combinació real; (b) mantenir com ara. Recomanació: (a), amb el retoc corresponent de la solució.

---

### 4.8 ✅ E4 — veu dels enunciats: 2a persona del singular → 2a del plural **(nou, derivat dels canvis del 2026-07-12)**

La convenció establerta a partir de la revisió de T7/T6 (documentada a `TODO/TODO.md §T5` i aplicada a `E6.qmd`: «Contesteu», «Calculeu», «Considereu») és la **2a persona del plural** als enunciats. `E4.qmd` usa sistemàticament el singular (~38 formes): Tradueix (×12) → Traduïu; Suposa (×6) → Suposeu; Escriu (×5) → Escriviu; Converteix (×3) → Convertiu; Completa (×3) → Completeu; Indica (×2) → Indiqueu; Considera (×2) → Considereu; Aplica (×2) → Apliqueu; Identifica → Identifiqueu; Enumera → Enumereu; Determina → Determineu; també «descriu» → «descriviu», «codifica» → «codifiqueu», «realitza» → «realitzeu», «exprés-la» → «expresseu-la», i qualsevol pronom o concordança associats. Les solucions noves (§7) han de seguir la mateixa veu quan reprodueixin imperatives. **A més**: la convenció només consta a `TODO.md §T5`; registrar-la formalment a `13_contrib.qmd §Problemari i solucionari (PE/PS)`.

### 4.9 🔵 A4 — harmonització menor de `@eq-acces-aleatori-matriu` amb la nova forma d'A2 (opcional, baixa prioritat)

La revisió de T2 (2026-07-12) ha deixat `@eq-acces-aleatori-vector` com a $@\texttt{vec[i]} = @\texttt{vec[0]} + i \cdot T$ (base explícita `vec[0]`, $T$ en math). L'equació d'A4 usa $@\texttt{mat}$ com a base (sense `[0][0]`); el $T$ ja és coherent. Valorar canviar la base a $@\texttt{mat[0][0]}$ per paral·lelisme exacte, o deixar-ho (ambdues formes són correctes). Si es canvia, repassar les aparicions textuals de la fórmula a A4 i S4.

## 5. LLENGUATGE (🟡)

### 5.1 ✅ A4 — «No obstant,» → «No obstant això,» (2 ocurrències: línies 203 i 531; forma normativa IEC).

### 5.2 ✅ A4 — primera aparició de «stride» (línia 452): `**stride**` → `***stride***` (regla dels triples asteriscs: anglicisme en primera aparició + concepte nuclear).

### 5.3 ✅ «l'stride» — VERIFICAT CORRECTE, no tocar: Optimot confirma que davant de manlleus començats amb essa líquida s'apostrofa l'article masculí («l'statu quo»).

### 5.4 ✅ `24_specs/svg.md` §3 — «razonable» → «raonable» (fora dels tres fitxers principals; detectat de passada).

---

## 6. VERIFICAT CORRECTE (sense acció) — per no repetir feina

- A4: traces `tip-seguiment-multiplicacio` (130 ✓), `tip-seguiment-divisio` (q=5, r=1 ✓), `tip-multiplicacio-naturals` (130 ✓), `tip-divisio-naturals` (q=5, r=1 ✓).
- A4: tot el codi assemblador dels exemples (deteccions de sobreeiximent, 4 accessos a `mat[i][j]`, optimitzacions #1/#2/#3 amb recomptes de control 5→4→3→2 ✓, `sumacolumna` aleatori i seqüencial), pseudocodis `@thm-*`, equacions de sobreeiximent HW/SW, taula d'strides (T, NC·T, (NC±1)·T ✓).
- A4 `#wrn-circuit-multiplicacio-combinacional`: «de 33 a 63 bits» és coherent interpretat com a amplada d'operands dels sumadors (PP1 = 33 bits … PP31 = 63 bits); «5 sumadors» = log₂32 ✓; «≈6 vegades» = 31/5 ✓.
- A4 casos especials de la divisió conformes amb l'especificació RISC-V (div/0 → q = −1, r = dividend; −2³¹ ÷ −1 → q = −2³¹, r = 0) ✓.
- S4 `sol-p5-sr-overflow-enters-8bits`: els quatre càlculs i vered­ictes de sobreeiximent ✓ (només 2.9).
- S4 `sol-p5-matrius-adreces` a)–e) ✓; `sol-p5-seq-bucles` strides i sentinelles ✓ (llevat 2.8); `sol-p5-opt-condicio-final` (13N+4, 10N+3, 23,1 % ✓); `sol-p5-opt-variable-induccio` (15/13 cicles, 6 instruccions ✓); `sol-p5-matrius-func-veci` a) ✓.
- Enunciats numèrics sense solució, ben definits: `exr-p5-mul-instruccions` b) (q = −2 = 0xFFFFFFFE, r = +1), `exr-p5-matrius-longlong` (1960 + 1384 = 3344 = 418·8 → `mat[8][18]`), `exr-p5-matrius-punter-offset` (`addi t0, t0, -25`), `exr-p5-seq-mixed` b) (8 / 8 / 60 / 12), `exr-p5-matrius-inversa` (`for (j = 0; j < 10; j++) b[n][j] = 0;`).
- Referències creuades externes de T4 (13 labels a A1/A2/A3): totes existeixen ✓, **re-verificades després dels canvis d'A2.qmd i A3.qmd del 2026-07-12** (revisions de T2 i T6) → **tanca l'ítem 2.2–2.9 de la revisió pre-Fable**. Els labels d'A4 referenciats des de fora (`sec-matrius-acces-aleatori`, `eq-acces-aleatori-matriu`, ara també citats des del nou A2.qmd) es mantenen intactes ✓.
- Criteri global nou «quatre formats nuclears d'instrucció» (adoptat a T2, 2026-07-12): T4 no esmenta enlloc el nombre total de formats (només «R» a la columna Tipus, que és format nuclear) → **no afecta T4** ✓.
- Cometes rectes en prosa: cap a T4 (només atributs Quarto) → l'ítem global «« »» és N/A per a T4.

---

## 7. SOLUCIONS NOVES PER A S4 (⏳ Fase C) — selecció aprovada per l'usuari (2026-07-12)

Generar seguint el format PS (`**Enunciat:** @exr-...` → explicació → blocs de càlcul → resultat; codi en `.s filename="RV32I(M)"`; refs a teoria integrades). Inserir cada solució a la seva secció, en l'ordre dels enunciats. Notes de resolució (resultats verificats a la Fase B):

1. `exr-p5-sr-conversio` — `0x0D34`: natural 3380; Ca2 +3380; SM +3380. `0xBA1D`: natural 47 645; Ca2 −17 891; SM −14 877 (magnitud `0x3A1D` = 14 877).
2. `exr-p5-sr-overflow-deteccio-natural` — `add t0, t1, t2` + `sltu t3, t0, t1` (2 instruccions, sense salts; indicació de l'enunciat).
3. `exr-p5-mul-instruccions` — a) `t2 = 0xFFFFFFFD` (−3); segons decisió 2.2, esmentar també `0x7FFFFFFD` i (si s'aprova §3) referenciar `@wrn-mul-modul-2n`. b) q = −2 (`0xFFFFFFFE`), r = +1 (signe del dividend). c) únic cas: −2³¹ ÷ −1.
4. `exr-p5-matrius-diagonal` — un sol `mul` de l'invariant `(N+1)*4`: `la` @M; `li (N+1)*4`; `mul`; `add`; `lw +4`; `lw +N*4`; `sub`; `add suma` (offsets vàlids si N*4 ≤ 2047).
5. `exr-p5-seq-bucles` c)–d) — c) diagonal: stride `(N+1)*4`, sentinella amb `mul` (N·(N+1)·4). d) stride constant `3*(N-1)*4` (Δlineal = 3N−3); com que el nombre d'iteracions és ⌈N/3⌉, és més net mantenir `i` com a comptador (`i += 3`, `blt i, N`) i el punter només per a l'accés a `A`.
6. `exr-p5-seq-mixed` — a) `z[4][j]` = `z + 4*3*4 + j*4` (z és `[5][3]`); b) justificar les constants 8 / 8 / 60 / 12.
7. `exr-p5-seq-short` — coordinar amb la decisió 2.1. a) resposta `p1[p2+3] = 0;` (si es corregeix l'enunciat). b) `p = p1;` / `*p = 0;` / `p++;` → `sh zero, 0(t1)` + `addi t1, t1, 2`.
8. `exr-p5-div-algorisme` — derivar el pseudocodi de `@thm-divisio-sequencial-restauracio` comentant el paper de cada registre.
9. `exr-p5-div-programa` — ❓ *(decisió menor)*: la traducció literal del circuit demana R i D de 64 bits (parells de registres); la formulació equivalent estàndard desplaça el residu a l'esquerra i hi injecta els bits del dividend, amb registres de 32 bits. Recomanació: usar la formulació equivalent amb una nota d'equivalència explícita amb el circuit («desplaçar D a la dreta equival a desplaçar R a l'esquerra»).

---

## 8. PENDENTS HERETATS QUE ROMANEN OBERTS

- ❓ A4 `#wrn-sobreeiximent-maquinari`: dos `<!-- TODO -->` de figures (half-adder/full-adder; cadena de full-adders amb XOR). Decidir si es creen (SVG natiu segons `24_specs/svg.md`) o s'eliminen els TODO.
- 🟡 `22_figs_originals/T4_multiplicador_sequencial.png`: artefacte al costat del `.svg` font; confirmar si es pot eliminar.
- Suggeriment opcional (baixa prioritat): slug `{#sec-casos-especials}` és genèric; si mai cal desambiguar, `{#sec-casos-especials-divisio}` (ara no es referencia des d'enlloc; canviar-lo no trenca res, però tampoc no urgeix).

---

## RESUM DE DECISIONS PENDENTS DE L'USUARI (❓)

| # | Ítem | Opcions (recomanació en negreta) |
|:---:|:---|:---|
| 2.1 | `exr-p5-seq-short` a) `sw`→`sh` | **modificar enunciat** / mantenir amb cast |
| 2.2 | `exr-p5-mul-instruccions` a) no-unicitat | restringir enunciat / **solució amb les dues respostes** |
| 2.8 | `addi ... N*4` vs `li`+`add` | **harmonitzar amb li+add** / mantenir |
| 3 | Matís `mul` mòdul 2ⁿ | **wrn a A4 (text proposat)** / nota al cos / descartar |
| 4.2 | Paràgraf T7 a `sol-p5-seq-bucles` | **punter @sec-tema-mc + registrar T4→T7** / suavitzar / eliminar |
| 4.7 | `exr-p5-opt-variable-induccio` b)/c) | **reformular b)** / mantenir |
| 7.9 | `exr-p5-div-programa` formulació | **equivalent 32 bits amb nota** / parells de registres |
| 8 | Figures half/full-adder | crear SVG / eliminar TODO |

## FITXERS QUE MODIFICARÀ LA FASE C

| Fitxer | Canvis |
|:---|:---|
| `S4.qmd` | 1.1–1.4, 2.6, 2.8, 2.9, 4.1, 4.2, 4.3 (bloc C), 4.5, 4.6, 4.9 (si s'aplica), §7 (9 solucions noves) |
| `E4.qmd` | 2.1, 2.3, 2.4, 2.5, 4.3, 4.4, 4.7, 4.8 (veu plural, ~38 formes) |
| `A4.qmd` | 2.7, 2.10, 3 (si s'aprova), 4.9 (opcional), 5.1, 5.2 |
| `13_contrib.qmd` | registrar el punter T4→T7 (si s'aprova 4.2a) i la convenció de veu plural dels enunciats (4.8) |
| `24_specs/svg.md` | 5.4 |

*(Nota: `TODO/TODO.md` ja no requereix cap canvi des d'aquest xat — l'entrada P3 va ser retirada al commit del 2026-07-12.)*
