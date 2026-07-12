# T6-E6-S6 — Revisió interna profunda: llista d'accions

**Fitxers objectiu:** `01_apunts/A6.qmd`, `02_exercicis/E6.qmd`, `03_solucions/S6.qmd` (+ `13_contrib.qmd`, `TODO/TODO.md`, `12_sigles.qmd`)
**Llegenda:** 🔴 error · 🟡 millora · 🔵 decisió · ✅ fet · ⏳ pendent

Nota de context: pas combinat E6+S6 (adaptació + revisió pròpia) i revisió
profunda de T6. Tots els càlculs de S6 i dels `#tip-` d'A6 es van verificar
pas a pas amb Python (aritmètica exacta) a la Fase B. **Totes les accions
d'aquest registre (A, B, C) s'han aplicat** a la Fase C (2026-07-12,
Sonnet High sense Thinking). Verificat per script que cap resultat numèric
en `\mathbf{}` de S6 s'ha alterat respecte a l'original (32/32 idèntics).

---

## A — Errors tècnics i de normativa ✅ APLICATS

### A6.qmd

- 🔴✅ **A1** — §Potència: «és l'energia dissipada» → «és l'energia dissipada
  **per unitat de temps**».
- 🔴✅ **A2** — `#tip-comparacio-versions-programa`: «Càlcul el núm
  d'instruccions» → «Calculeu el nombre d'instruccions»; «Calculem dels CPI»
  → «Calculeu els CPI».
- 🔴✅ **A3** — «a conjunt de programes» → «a un conjunt de programes».
- 🔴✅ **A4** — «Al conduir» ×2 → «En conduir» (`#wrn-RC`).
- 🔴✅ **A5** — Cometes rectes → guillemets (l. 15, 55).
- 🔴✅ **A6** — «Km/h» → «km/h»; «Joules» → «joules».
- 🔴✅ **A7** — `@eq-guany3`: $P_{X}$ → $P_{x}$ (×2).
- 🔴✅ **A8** — «tc» en text pla → $t_{clock}$ (`#tip-augment-freq`).
- 🔴✅ **A9** — Apòstrofs tipogràfics (’) → rectes (') a les 5 línies
  afectades.
- 🔴✅ **A10** — «puja per sobre de cert llindar» → «per sobre d'un cert
  llindar».

### E6.qmd

- 🔴✅ **A11** — «la única millora» → «l'única millora».
- 🔴✅ **A12** — «ràtio» femení: «els ràtios» → «les ràtios» (×2).
- 🔴✅ **A13** — Cometes rectes → guillemets («10 vegades més ràpid»).
- 🔴✅ **A14** — «multiplicador hardware» → «multiplicador per maquinari».
- 🔴✅ **A15** — Veu 2a persona del plural: 14 substitucions (Contesta→
  Contesteu, Calcula→Calculeu, Considera→Considereu, Troba→Trobeu,
  Raona→Raoneu, tries→trieu).

### S6.qmd

- 🔴✅ **A16** — `#sol-p2-rendiment-coma-flotant`: retirada la dada
  inventada de les «200 instruccions» (no és a l'enunciat); reescrit en
  termes de l'enunciat real (reducció ×10 d'instruccions CF).
- 🔴✅ **A17** — `#sol-p2-amdahl-multicomponent`: generalització d'Amdahl
  corregida amb el terme $(1-\sum f_i)$ explícit i nota de la condició
  aplicada en aquest exercici concret.
- 🔴✅ **A18** — `#sol-p2-amdahl-limit` c): conclusió corregida (1,54× és el
  límit **assolible**, no inassolible); redacció final revisada.
- 🔴✅ **A19** — `#sol-p2-rendiment-classes`: retirat el terme «pipeline»
  (no introduït en aquest punt del temari); reescrit sense el concepte.
- 🔴✅ **A20** — `tbl-colwidths` escalat de `[5,22,12,7,8,8,8,10]` (suma 80)
  a `[6,28,15,9,10,10,10,12]` (suma 100).
- 🔴✅ **A21** — «1.350» → «1 350» (separador de milers amb espai).
- 🔴✅ **A22** — «ràtio» femení: «El ràtio màxim» → «La ràtio màxima» (×2);
  «dels ràtios» → «de les ràtios».
- 🔴✅ **A23** — hardware/HW → maquinari: 2 títols de secció + 3 aparicions
  al cos.
- 🔴✅ **A24** — `#sol-p2-rendiment-coma-flotant` a): precisió del «13% més
  lent» → «rendiment un 13% inferior (triga un 14,8% més)».

## B — Millores i harmonitzacions menors ✅ APLICADES

- 🟡✅ **B1** — Línia en blanc i doble espai corregits (`eq-n-cicles`),
  resolt en desetiquetar-la (C9).
- 🟡✅ **B2** — `\text{}` per a paraules catalanes en itàlica math:
  `eq-rendiment`, `eq-guany1`, `t_millorat`/`t_no-millorat` a `eq-guany2`.
- 🟡✅ **B3** — Unitats amb espai dins math: `\mu s`, `GHz`, `s` als tips
  d'A6.
- 🟡✅ **B4** — Definició d'$\alpha$ precisada: «fracció mitjana de portes
  que commuten en cada cicle».
- 🟡✅ **B5** — «material i grandària… i connectors connectats» → «material
  i mida… i de les interconnexions».
- 🟡✅ **B6** — «(**fan-out**)» → «(*fan-out*)».
- 🟡✅ **B7** — «disseny multicore» → «disseny multinucli (*multicore*)».
- 🟡✅ **B8** — NMOS/PMOS expandits simètricament; «circuit-obert» →
  «circuit obert»; «*nmos*»/«*pmos*» → NMOS/PMOS.
- 🟡✅ **B9** — «si la suma és inferior» → «si la suma total de cicles
  resultant és inferior».
- 🟡✅ **B10** — «no és segur que hi hagi guanyat» → «no és segur que s'hi
  guanyi».
- 🟡✅ **B11** — Nota al peu `[^CPIins]`: *loads*/*stores* → «instruccions
  de lectura/escriptura»; «No obstant,» → «No obstant això,»; veu
  impersonal.
- 🟡✅ **B12** — Taula del tip: `style="width: 70%; margin: auto;"`.
- 🟡✅ **B13 (PE+PS)** — Notació de potència estàtica homogeneïtzada:
  $P_{s} = V_{CC} \cdot I_{fuita}$; $I_{leak}$ → $I_{fuita}$ (×3 a S6);
  «fuita de corrent» → «corrents de fuita» (plural, com a fenomen).
- 🟡✅ **B14 (PE)** — «El nombre mitjà d'instruccions… subrutines» → «El
  nombre d'instruccions de coma flotant executades».
- 🟡✅ **B15 (PE)** — Retirat `@eq-energia` de la nota de secció (cap
  exercici l'usa).
- 🟡✅ **B16 (PS)** — «era de l'escalada de freqüència» → «era del
  creixement de la freqüència».
- 🟡✅ **B17 (T6)** — Caption de `@fig-amdahl` reformulat.

## C — Decisions de Roger ✅ APLICADES (resoltes 2026-07-12)

- 🔵✅ **C1** — Ordre i noms de secció: **E6 i S6 reordenats** al mirall
  d'A6 (Rendiment → Amdahl → Potència, els tres fitxers ara coincideixen);
  secció renombrada «Potència i consum» → «Potència».
- 🔵✅ **C2** — Notació del tema: **opció (a)** — formes llargues
  ($t_{clock}$, $f_{clock}$, $n_{ins}$) a les definicions, abreviatures
  ($t_c$, $f$, $N$) explícitament introduïdes i usades lliurement després.
  Registrat a `13_contrib.qmd §T6`.
- 🔵✅ **C3** — «Capacitat equivalent» com a terme principal, amb
  «(capacitància)» a la primera aparició de cada fitxer. Aplicat a A6, E6
  (×2) i S6 (títol + cos).
- 🔵✅ **C4** — CMOS i CF expandides a la primera aparició del cos de cada
  fitxer (E6, S6) + entrades noves a `12_sigles.qmd`; FPU substituïda per
  «unitat de coma flotant» a S6 (4 aparicions).
- 🔵✅ **C5** — «Guany» com a terme principal; *speedup* en cursiva només a
  la primera aparició de cada fitxer (aplicat a A6).
- 🔵📌→TODO **C6** — Etiquetes de classe en anglès (Load/Store/Branch a les
  taules d'E6/S6): **sense canvi ara**, anotat a `TODO.md §T6` per a
  decisió transversal futura.
- 🔵✅ **C7** — Minúscula al cos del text per a «llei d'Amdahl», «llei de
  Moore» i «escalat de Dennard» (11 aparicions corregides a A6 i S6); els
  títols de secció/callout mantenen la majúscula de frase.
- 🔵✅ **C8** — **Opció (a)**: títol `##` afegit als 8 `#tip-` d'A6 que no en
  tenien.
- 🔵✅ **C9** — **Opció (a)**: desetiquetades `eq-guany1`, `eq-guany2` i
  `eq-n-cicles` (passos intermedis no referenciats); mantingudes
  `eq-rendiment`, `eq-texe1`, `eq-texe3` (canòniques) i totes les
  referenciades des d'E6/S6 (`eq-texe2`, `eq-cpi`, `eq-guany3`,
  `eq-amdahl`, `eq-potencia*`, `eq-energia`).
- 🔵✅ **C10** — **Opció (a)**: `width="100%"` normalitzat a les 5 figures
  del `wrn-RC` i les de `fig-amdahl`/`fig-tc-tc-prima` (atribut de la
  imatge dins el `.qmd`); entrada obsoleta de `TODO.md §T6` (versions
  «`___tracable____`» inexistents) substituïda per una nota de resolució.
- 🔵✅ **C11** — Criteri documentat i aplicat: amplada uniforme HTML/PDF per
  bloc Quarto (sense divergència de format): `40%` per a `fig-amdahl` i
  `fig-tc-tc-prima`; `50%` per a les tres `fig-not-*`. Registrat a
  `13_contrib.qmd §T6`.
- 🔵✅ **C12** — CPI del disseny original fet explícit a l'enunciat
  d'`exr-p2-rendiment-speedup-mul` («Al disseny original, totes les
  instruccions tenen un CPI mitjà de 3»).

## D — Fora d'abast d'aquest xat ✅ ANOTAT

- 🔵✅ **D1** — Veu singular a E5: anotat a `TODO.md §T5` per a una propera
  passada d'harmonització.
- 🟡 **D2** — $V^2$ (A7) vs. $V_{CC}^2$ (A6) a la fórmula de potència
  dinàmica: micro-harmonització transversal opcional, no aplicada (fora
  d'abast de T6).

## E — Verificacions completades sense incidència ✅

(Vegeu la Fase B per al detall complet.) Tots els càlculs de S6 i els tips
d'A6 verificats aritmèticament correctes. Coherència estructural:
aparellament `#exr-`↔`#sol-` complet (14/14, mantingut després del
reordenament); IDs de T6 únics a tot el llibre (39 a A6, 15 a E6, 15 a S6,
cap duplicat); totes les referències internes (`@eq-*`, `@sec-*`, `@fig-*`,
`@tip-*`, `@wrn-*`) resolen correctament als tres fitxers després de totes
les edicions; les referències externes cap a T6 des d'A7 i `index.qmd`
resten intactes (cap etiqueta ni slug canviat). Cap resultat numèric de S6
alterat (verificació automàtica: 32/32 `\mathbf{}` idèntics abans/després).

---

## Fitxers modificats en aquest xat

| Fitxer | Estat |
|:---|:---|
| `01_apunts/A6.qmd` | ✅ A1–A10, B1–B12, B17, C2, C3, C4, C5, C7, C8, C9, C10, C11 |
| `02_exercicis/E6.qmd` | ✅ A11–A15, B13–B15, C1, C3, C4, C5, C6 (→TODO), C7, C12 |
| `03_solucions/S6.qmd` | ✅ A16–A24, B13, B16, C1, C2, C3, C4, C6 (→TODO), C7 + `tbl-colwidths` corregit a suma 100 |
| `13_contrib.qmd` | ✅ nova subsecció `#### T6` (C1–C5, C7, C10, C11) |
| `TODO/TODO.md` | ✅ §T6 reescrit (retirada entrada obsoleta, afegit C6); §T5 (D1) |
| `12_sigles.qmd` | ✅ entrades CF i CMOS afegides (C4) |
| `22_figs_originals/T6_*.svg` | Sense canvi (el `width` intern del SVG és irrellevant; només calia l'atribut del bloc Quarto) |
