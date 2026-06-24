# Tasques de revisió: T2.qmd, PE_T2.qmd, PS_T2.qmd

## Estat: COMPLETAT (xat `EC T2, PE_T2 i PS_T2 Revisió interna`)

Totes les tasques accionables directament han estat aplicades.
Decisions D1–D13 resoltes.
Pendent: PS-NOU-1 a PS-NOU-4 (solucionaris nous, xat separat, Opus High Thinking).

---

## Tasques aplicades

### T2.qmd

| Ítem | Descripció | Estat |
| :--- | :--- | :--- |
| T2-T12 | Taula little/big-endian: continguts intercanviats (error crític) | ✅ |
| T2-T2 | `0xFFFFF800` → `-2048` com a immediat d'`addi` | ✅ |
| T2-T3 | Coma incorrecta a la comanda GCC `-Wall, -Wextra` | ✅ |
| T2-T4 | `la`/`li` "macros" → "pseudoinstruccions" | ✅ |
| T2-T5 | `#wrn-punters-x86` afegit `collapse=true` | ✅ |
| T2-T6 | Espai: `vec`es → `vec` es | ✅ |
| T2-T7/T8 | "la opció" → "l'opció"; coma afegida | ✅ |
| T2-T9 | Etiqueta `{#sec-opt-acces-sequencial}` afegida | ✅ |
| T2-T10 | TODO octal eliminat (0101₈=65 ✓) | ✅ |
| T2-T11 | Nota `.byte` sense operands corregida + TODO eliminat | ✅ |
| T2-T13 | Cometes al callout Mx eliminades → cursiva | ✅ |
| T2-T14 | Cometes al voltant de "llegiu" eliminades | ✅ |
| T2-T15 | `"Execute"` → `«Execute»` | ✅ |
| T2-T16 | `"Extensió de rang"` → L'**extensió de rang** | ✅ |
| T2-T17 | Cometes al voltant de noms d'extensions eliminades | ✅ |
| T2-T18 | `"reduït"` → `«reduït»` | ✅ |
| T2-T19 | `"32 vs. 64 bits"` → text sense cometes | ✅ |
| T2-T20 | "punter a enter/caràcter" → cursiva | ✅ |
| T2-T21 | `operador "indexació"` → `operador d'indexació` | ✅ |
| T2-T22 | `"ç"`, `"ü"`, `"à"` → cursiva | ✅ |
| T2-T23 | `"tipus de dada específic"` → sense cometes | ✅ |
| T2-T24 | Redundància "modularitat" L.86 reformulada | ✅ |
| T2-T25 | `*data **type***` → `*data type*` | ✅ |
| T2-T26 | Caption afegit a `#tbl-tipus-alineacio` | ✅ |
| T2-T27 | Notació `lo~12~`/`hi~20~` → LaTeX al callout `li` | ✅ |
| T2-T28/29 | Format interior callout `#tip-codificacio-instruccions` | ✅ |
| T2-T30 | `"0x"` → `0x` sense cometes | ✅ |
| T2-C1 | Redundància L.86 "modularitat" | ✅ |
| T2-C3 | TODO ISA `li` amb `lo12==0` eliminat | ✅ |
| D3 | Secció «mode memòria» → «mode base+desplaçament»; callout `#cau-mode-base-desplacament` creat | ✅ |
| D13 | 4 títols `## RARS —` → `## Directives —` (directives estàndard GNU AS) | ✅ |

### PE_T2.qmd

| Ítem | Descripció | Estat |
| :--- | :--- | :--- |
| PE-C1 | 36 blocs de codi (23 `.s` + 13 `.c`) amb `filename=` afegit | ✅ |
| PE-C6 | Nota `la+offset` + excepció d'alineació afegida | ✅ |
| PE-C7 | Enunciat rang `addi` precisat | ✅ |
| PE-C8 | Columna «Excés» → «Excés a 7» | ✅ |
| PE-C9 | Format resultat `d3` especificat (binari natural) | ✅ |
| D7 | «bytes» → «byte ... a cada una de les adreces» (singular, explícit) | ✅ |

### PS_T2.qmd

| Ítem | Descripció | Estat |
| :--- | :--- | :--- |
| PS-C1 | Reformulació extensió de signe ($lo_{12} - \texttt{0x1000}$) | ✅ |
| PS-C2 | Comentari `# t2 = punter` → `# t2 = valor de punter (adreça apuntada)` | ✅ |
| PS-C3 | Nota `a0`/`a1` caller-saved en context de subrutines | ✅ |
| PS-C4 | «bloc d'activació» → terminologia de T2 | ✅ |

### 07_contrib.qmd

| Ítem | Descripció | Estat |
| :--- | :--- | :--- |
| D1 | Zifencei afegit a la taula d'extensions d'EC | ✅ |
| D10 | Decisió `.globl` documentada a §T2 i T3 | ✅ |

### TODO.md

| Ítem | Descripció | Estat |
| :--- | :--- | :--- |
| T2 (6 punts) | Tots els punts de T2 marcats com a resolts o actualitzats | ✅ |
| D10 | `.globl` marcat com a resolt | ✅ |
| D11 | `ret` vs `jalr`: criteri provisional `ret` documentat | ✅ |
| D12 | Adreces: criteri provisional sense espais documentat | ✅ |
| D13 | `## Directives —` vs `## RARS —`: decisió documentada | ✅ |

---

## Tasques pendents (no aplicades en aquest xat)

### PS_T2.qmd — Solucionaris nous (requereixen Opus High Thinking)

| Ítem | Exercici PE_T2 | Descripció |
| :--- | :--- | :--- |
| PS-NOU-1 | `#exr-p3-memoria-endianness` | *Little-endian*, ordre de bytes, resultat de `lb` |
| PS-NOU-2 | `#exr-p3-vectors-cerca` | Cerca en vector, retorn −1 si no es troba |
| PS-NOU-3 | `#exr-p3-vectors-punter-aritm` | Aritmètica de punters sobre `short` (2B/element) |
| PS-NOU-4 | `#exr-p3-strings-copia` | Còpia de cadena (`src` → `dst`, inclòs `'\0'`) |

### Decisions obertes (D2, D4–D6)

| Decisió | Descripció | Estat |
| :--- | :--- | :--- |
| D2 | `startup.s`: mantenir fins a consens del professorat | Pendent consens |
| D4 | `@sec-von-neumann` a T2: verificar que existeix a T1 | Pendent revisió T1 |
| D5 | `@nte-la-auipc` a T2: apunta a T3 (✓ confirmat L.1049) | Resolt quan T3 estigui revisat |
| D6 | `@sec-optimitzacions-bucle` a T4 | Confirmat per l'usuari ✓ |
