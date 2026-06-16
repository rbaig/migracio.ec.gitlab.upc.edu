# T4.qmd — Revisió interna completada

Totes les tasques tancades. Resum executiu per a futures sessions.

---

## Verificacions tècniques (sense errors)

Recalculades a mà i correctes: traces del multiplicador seqüencial de 4 bits (→130) i divisor amb restauració de 4 bits (→q=5, r=1); pseudocodis `#thm-multiplicacio-secuencial` i `#thm-divisio-secuencial-restauracio`; taules ISA `mul*`/`div*`/`rem*`; condicions de sobreeiximent HW/SW; fórmula `@mat[i][j]` i taula d'strides; optimitzacions #1/#2/#3; casos especials de divisió (÷0 i overflow −2³¹/−1) contra l'especificació RISC-V.

---

## Tasques aplicades

### Arreglos segurs (C1–C6, B3–B5)
- **C1** «d'sobreeiximent» → «de sobreeiximent» (×8).
- **C2** `{.C` → `{.c` (×11).
- **C3** Callout `neg`: títol, format de taula i etiqueta corregits.
- **C4** Negreta penjada a §4.2.1 tancada.
- **C5** Punt final al caption de `@fig-matriu-offset-ij`.
- **C6** Etiqueta malformada `#imp-mul-` → `#imp-ec-mul-adreces`.
- **B3** `filename="RV32I"` → `"RV32IM"` al bloc d'optimització #2 (conté `mul`).
- **B4** «múltiples de dos» → «potències de 2» a `#imp-ec-mul-adreces`.
- **B5** Reformulació stride/sentinella a `@tip-sumacolumna-sequencial`.

### Decisions de fons (B1, B2, B7, B8, C7, C8)
- **B1** Taula `add`/`sub` duplicada eliminada; substituïda per referència a `@nte-instruccions-aritmetica-entera-rv32i` + recordatori breu. `neg` conservat.
- **B2** `#imp-sobreeiximent-riscv` (`.callout-important`, mal classificat) → `#cau-sobreeiximent-extensio-m` (`.callout-caution`); text estén el criteri de T2 a l'extensió M.
- **B7** Llegendes `#thm-` unificades a «naturals de $n$ bits»; `#thm-multiplicacio-secuencial` parametritzat (`31→n-1`, `63→2n-1`, `fins a 32→fins a n`).
- **B8** `#### Multiplicació de naturals` i `#### Divisió de naturals` eliminats (un sol ítem per nivell); text integrat directament sota `### Algorisme`.
- **C7** `#imp-eqv-dimensions`: títol i blocs de codi eliminats; reescrit com a Criteri EC legítim («A EC, es recomana…», sense títol, negretes).
- **C8** `filename="Pseudocodi"` afegit al bloc `{.default}` del mentre→do-while (línia ~517); bloc numèric de la multiplicació manual deixat sense `filename`.

### Figures (D1–D4)
- **D1** `T4_multiplicador_sequencial_light.svg`: MD (2n, desplaça ←), sumador, P (2n, acumulador), MR (n, desplaça →); control `MR[0]` en discontínua. Integrat amb `#fig-multiplicador-sequencial`.
- **D2** `T4_multiplicador_arbre_light.svg`: arbre binari de sumadors (8 PP → 4 → 2 → 1 → Z); profunditat ⌈log₂ n⌉, n=32 → 5 nivells. Integrat amb `#fig-multiplicador-arbre`.
- **D3** `T4_divisor_sequencial_light.svg`: D (2n, desplaça →), sumador/restador R−D amb restauració R+D, R (2n, dividend/residu), Q (n, desplaça ←); control signe R[2n−1]. Integrat amb `#fig-divisor-sequencial`.
- **D4** SVGs de matrius (`T4_matriu_{emmagatzematge,offset_ij,recorreguts_strides}_{light,dark}.svg`) ja existien al repo. Cap acció.

Totes les figures light/dark s'integren amb el bloc `content-visible` estàndard del projecte. Les variants dark es generen automàticament al pre-render.

### Dependències externes
- **X1** `@sec-enters-en-ca2` i `@eq-rang-ca2` existeixen a `T1.qmd` (línies 482 i 487). Cap acció.
- **X2** `add`/`sub`/`addi` confirmats a T2 `#nte-instruccions-aritmetica-entera-rv32i`. Rellevant per a B1.

---

## Tasques opcionals no aplicades

- **B6** Subíndexs unicode `×ᵤ ×ₛᵤ ÷ᵤ modᵤ` a les taules ISA: pendent de verificar render PDF. Si hi ha problemes de glyph, substituir per `$\times_u$` o text «(naturals)/(enters)».
- **C9** Etiquetes `#thm-…-secuencial` → «sequencial» (baixa prioritat).
- **C10** Afegir `{#sec-}` a seccions no referenciades (baixa prioritat).
