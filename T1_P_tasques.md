# T1_P_tasques — Revisió interna: T1, PE_T1, PS_T1

Data: 2026-06-25
Fitxers principals: `T1.qmd`, `PE_T1.qmd`, `PS_T1.qmd`
Fitxers de referència llegits: `CLAUDE.md`, `07_contrib.qmd`, `_quarto.yml`, `TODO.md`, `09_bibliografia.bib`, `T2.qmd`, `PE_T2.qmd`, `PS_T2.qmd`

## Estat final

**Totes les tasques completades.**

---

## Resum de canvis aplicats

### `T1.qmd`

| # | Tipus | Descripció |
| :--- | :--- | :--- |
| 1 | Error tècnic | L.86: «fa una crida a l'**ABI** (crida al sistema)» → «fa una crida al sistema (`ecall`), seguint les convencions de l'**ABI**» |
| 2 | Tipogràfic | L.101: «**les**» en negreta eliminat; coma afegida |
| 3 | Imprecisió tècnica | L.228: «salt incondicional» → «salt indirecte a l'adreça continguda al registre `ra`»; expansió `jalr x0, 0(ra)` explicitada |
| 4 | Millora tècnica | L.593: «carry que desbordés de la posició n-1» → «carry de sortida (*carry-out*) que depassi el bit de signe (n-1)» |
| 5 | Referència anticipatòria | Flux de generació: ABI usat abans de definir-se → afegit `(vegeu @sec-interficies)` |
| 6 | Referència creuada | §Traducció: afegida referència a `@sec-interficies` i `@fig-flux-compilacio` |
| 7 | Contingut nou | Secció `## Operacions aritmètiques en complement a 2 {#sec-operacions-ca2}` amb subseccions de suma, resta, multiplicació i divisió, callouts d'exemple i `#imp-multiplicacio-isa` |
| 8 | Slugs | 30 identificadors `{#sec-}` nous afegits a totes les capçaleres `##`/`###`/`####` estructurals (total: 45 slugs únics) |

### `PE_T1.qmd`

| # | Tipus | Descripció |
| :--- | :--- | :--- |
| 1 | Exercici nou | `exr-p1-naturals`: interpretació bits→nat i representació nat→bits (cobria buit de la teoria) |
| 2 | Reordenació | `exr-p1-enters-minim13` i `exr-p1-enters-maxim13` desplaçats al davant de `exr-p1-enters-taules` (prerequisit lògic) |
| 3 | Exercici nou | `exr-p1-enters-extensio-signe`: extensió de signe de 8 a 16 bits |
| 4 | Apartat nou | `exr-p1-aritm-suma` apartat e): cas de signes contraris (sobreeiximent impossible) |
| 5 | Exercicis nous | `exr-p1-aritm-suma`, `exr-p1-aritm-resta`, `exr-p1-aritm-multiplicacio`, `exr-p1-aritm-divisio`: aritmètica Ca2 |
| 6 | Consistència | Títol secció: «Representació de naturals i enters» → «Codificació de nombres naturals i enters» |

### `PS_T1.qmd`

| # | Tipus | Descripció |
| :--- | :--- | :--- |
| 1 | Error tècnic | Cel·la (8, Excés a 7): `NC` → `` `1111` ``; observacions reescrites |
| 2 | Reescriptura | `sol-p1-jerarquia-python`: format callout, concepte de compilador creuat explicat, TODO eliminat |
| 3 | Solució nova | `sol-p1-jerarquia-c`: afegida (mancava completament) |
| 4 | Solució nova | `sol-p1-naturals`: interpretació i representació de naturals |
| 5 | Solució nova | `sol-p1-enters-extensio-signe`: extensió de signe, referència `@sec-extensio-zeros` |
| 6 | Solucions noves (×6) | `sol-p1-enters-conversio8`, `sol-p1-enters-codificacio`, `sol-p1-enters-ca2-16bits`, `sol-p1-enters-implicit`, `sol-p1-enters-minim13`, `sol-p1-enters-maxim13` |
| 7 | Solucions noves (×4) | `sol-p1-aritm-suma` (amb apartat e), `sol-p1-aritm-resta`, `sol-p1-aritm-multiplicacio`, `sol-p1-aritm-divisio` |
| 8 | Correcció | `S\&M` → `S&M` (6 aparicions; backslash innecessari en Markdown) |
| 9 | Consistència | Títol secció alineat amb T1 i PE_T1 |
| 10 | Ordre | Totes les solucions alineades 1:1 amb l'ordre dels exercicis de PE_T1 (14/14) |

### `PE_T2.qmd`

| # | Tipus | Descripció |
| :--- | :--- | :--- |
| 1 | Convenció | Etiqueta `{#nte-p3-remissio-enters}` afegida al callout de remissió (estava sense etiquetar) |

---

## Cobertura final de PE_T1 i PS_T1

| # | ID exercici | Solució |
| :---: | :--- | :---: |
| 1 | `exr-p1-jerarquia-python` | `sol-p1-jerarquia-python` ✓ |
| 2 | `exr-p1-jerarquia-c` | `sol-p1-jerarquia-c` ✓ |
| 3 | `exr-p1-naturals` | `sol-p1-naturals` ✓ |
| 4 | `exr-p1-enters-minim13` | `sol-p1-enters-minim13` ✓ |
| 5 | `exr-p1-enters-maxim13` | `sol-p1-enters-maxim13` ✓ |
| 6 | `exr-p1-enters-taules` | `sol-p1-enters-taules` ✓ |
| 7 | `exr-p1-enters-conversio8` | `sol-p1-enters-conversio8` ✓ |
| 8 | `exr-p1-enters-implicit` | `sol-p1-enters-implicit` ✓ |
| 9 | `exr-p1-enters-extensio-signe` | `sol-p1-enters-extensio-signe` ✓ |
| 10 | `exr-p1-enters-ca2-16bits` | `sol-p1-enters-ca2-16bits` ✓ |
| 11 | `exr-p1-enters-codificacio` | `sol-p1-enters-codificacio` ✓ |
| 12 | `exr-p1-aritm-suma` | `sol-p1-aritm-suma` ✓ |
| 13 | `exr-p1-aritm-resta` | `sol-p1-aritm-resta` ✓ |
| 14 | `exr-p1-aritm-multiplicacio` | `sol-p1-aritm-multiplicacio` ✓ |
| 15 | `exr-p1-aritm-divisio` | `sol-p1-aritm-divisio` ✓ |
