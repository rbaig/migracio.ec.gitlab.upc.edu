# Bloc D — Criteri backticks / LaTeX math / cursiva

Proposta per a aprovació (fase 1). Un cop aprovada (amb les modificacions que calguin), el text de §2 s'integra a `13_contrib.qmd` i s'apliquen les substitucions de §3 (fase 2, mecànica).

---

## 1. Auditoria (27 fitxers: Ax, Ex, Sx, Lx)

| Aspecte | Estat | Dades |
| :--- | :--- | :--- |
| Backticks per a codi (registres, instruccions, variables C, fitxers, hex) | **Consistent** ✓ | Criteri de `13_contrib.qmd §Backticks` ben aplicat; 0 registres en math |
| Variables d'una lletra: `i` (variable C) vs $i$ (índex matemàtic) | **Consistent de facto** ✓ | 198 backtick / 124 math, repartits pel criteri semàntic correcte |
| Unitats al cos del text («8 bits», «4 bytes») | **Consistent** ✓ | 606 casos en text pla, 0 amb el nombre en math |
| Cursives | **Consistent** ✓ | Només anglicismes; 1 sol cas anòmal (*x*) |
| Superíndexs: Pandoc `2^8^` vs math `$2^{8}$` | **Inconsistent** ✗ | 20 Pandoc (quasi tots en taules de T2) vs 34 math |
| `\text{}` dins math | **Sense criteri** — | 311 casos: unitats (` KB`, ` ns`), sigles (`CPI`, `TAM`), paraules (`índex`), camps (`offset`) |
| `\texttt{}` dins math | **Raonablement consistent** | 107 casos: hex, identificadors de codi dins fórmules |
| Math en títols de secció `{#sec-}` | **Consistent** ✓ | 0 casos (1 cas en títol de *callout*, acceptable) |
| Numeració d'equacions | **Sense criteri** — | 326 display; 38 etiquetades `{#eq-}`; 23 referenciades `@eq-` |

## 2. Criteri proposat (text per a `13_contrib.qmd`)

Substituiria l'actual §Backticks (que es manté com a llista d'exemples) afegint-hi la regla general, i completaria §Equacions.

### 2.1 Regla general: el format el determina la naturalesa de l'element

- **Backtick** (`` ` ``) — **codi**: tot allò que existeix literalment en un programa, en una ISA o en un fitxer: registres (`t0`, `mepc`), instruccions (`addi`), directives (`.data`), variables i expressions C (`i`, `p++`), camps de bits (`opcode`), adreces concretes (`0x10010000`), fitxers, comandes, etiquetes. *(Tanca el TODO dels CSR: sempre amb backtick, també en títols de secció, com ja fa T9.)*
- **LaTeX math** (`$…$`) — **matemàtiques**: quantitats, variables i expressions matemàtiques: mides genèriques ($n$ bits, $B = 2^b$), índexs de fórmules i algorismes ($q_i$), rangs ($[-2^{11}, 2^{11}-1]$), operacions ($rd = M_w[rs1 + SignExt(offset)]$).
- **Cursiva** — **llengua**: anglicismes en primera aparició i èmfasi lleu. Mai per a codi ni per a variables matemàtiques.
- **Text pla** — la resta: nombres amb unitats («8 bits», «l'adreça és a 4 bytes»), noms d'arquitectures i extensions (RISC-V, RV32I, extensió M), tipus de format (S, B).

**Cas fronterer — variables d'una lletra**: si l'element viu en un programa concret (està declarat al codi de l'exemple), backtick (`i`, `p`); si viu en una fórmula o algorisme abstracte, math ($i$, $n-1$). És el criteri que el corpus ja segueix.

**Dins de les fórmules**:

- `\text{…}`: paraules catalanes, sigles i unitats ($\text{CPI}$, $t_h = 2\text{ ns}$, $\text{núm. encerts}$).
- `\texttt{…}`: elements de codi que apareixen dins d'una fórmula ($\texttt{0x100100F}$, $\texttt{vec[i]}$).

### 2.2 Criteri per context

| Context | Backtick | Math | Cursiva |
| :--- | :---: | :---: | :---: |
| Cos del text | ✓ | ✓ | ✓ (anglicismes) |
| Títols de secció `{#sec-}` | ✓ | ✗ (reescriure el títol) | ✗ |
| Títols de callout | ✓ | ✓ | ✓ (anglicismes) |
| Cel·les de taula | ✓ | ✓ (vegeu D1) | ✓ |
| Captions de figura/taula | ✓ | ✓ | ✓ |
| Comentaris de blocs de codi | (tot és codi) | ✗ (no es renderitza) | ✗ |
| Etiquetes SVG | segons `24_specs/svg.md` (MONO per a codi); sense MathJax: notació Unicode (×, ≤, ²) | | |

### 2.3 Numeració d'equacions (proposta per a D2)

- S'etiqueten (`{#eq-nom}`) — i per tant es numeren — **només les equacions referenciades** amb `@eq-` des d'algun punt del llibre (mateix tema, PE/PS o laboratori), més les **fórmules canòniques** del tema susceptibles de ser referenciades en el futur (p. ex. la definició de TAM, la Llei d'Amdahl).
- La resta d'equacions display queden sense etiqueta ni número.
- Manteniment: si es fa referència a una equació no etiquetada, s'etiqueta en aquell moment.

## 3. Aplicació (fase 2, si s'aprova)

1. **Superíndexs**: unificar els 20 casos `2^n^` → `$2^{n}$` (vegeu D1).
2. **Cursiva anòmala**: corregir el cas únic (*x*).
3. **`{#eq-}` no referenciades**: llistar les 38−23=15 etiquetes sense referència i decidir cas per cas si són «canòniques» (es queden) o es desetiqueten.
4. Integrar §2 a `13_contrib.qmd` (§Backticks + §Equacions + nou §«Codi, matemàtiques i cursiva») i esborrar els TODO corresponents (línies 302, 480-483) i les entrades de `TODO.md §Decisions obertes` (CSR, LaTeX vs backticks, numeració d'equacions).

## 4. Decisions que has de prendre

- **D1 — Superíndexs en cel·les de taula**: (a) *recomanat*: unificar-ho tot a math `$2^{8}$` (millor tipografia, coherència; el desbordament mòbil ja està resolt); (b) mantenir Pandoc `2^8^` a les taules (render més lleuger, sense MathJax) i math fora de taules.
- **D2 — Numeració d'equacions**: (a) *recomanat*: només referenciades + canòniques (§2.3); (b) numerar-les totes; (c) numerar «les importants» (criteri subjectiu, difícil de mantenir).
- **D3 — Negretes dins de callouts** (TODO obert): (a) *recomanat*: als `#cau-`/`#imp-` (curts, sense títol) la negreta marca el nucli del recordatori, com fins ara; als `#tip-`/`#nte-`/`#wrn-` s'aplica el criteri general de §Ressaltat conceptual; (b) prohibir negretes dins de callouts curts (quedarien plans).
- **D4 — `\text{offset}` dins de fórmules**: quan `offset` (o `índex`, `etiqueta`) és el *camp* d'una instrucció o d'una adreça, (a) *recomanat*: mantenir `\text{…}` per defecte i reservar `\texttt{…}` per a literals de codi i hex (criteri simple); (b) passar els camps a `\texttt{…}` (més precís semànticament, però obliga a revisar 311 casos i xoca amb l'harmonització RV32F pendent, `TODO.md §T5`).
