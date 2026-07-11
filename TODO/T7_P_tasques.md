# T7-E7-S7 — Revisió interna profunda: llista d'accions

**Fitxers objectiu:** `01_apunts/A7.qmd`, `02_exercicis/E7.qmd`, `03_solucions/S7.qmd`, `22_figs_originals/T7_lru_exemple.svg`
**Llegenda:** 🔴 error · 🟡 millora · 🔵 decisió · ✅ fet · ⏳ pendent

Nota de context: `A7.qmd` ja va passar una revisió interna profunda (vegeu
`T7_tasques.md` antic, tasques A–E tancades). Aquest xat fa el pas combinat
E7+S7 (adaptació + revisió pròpia) i una segona passada de coherència
sobre T7. Els càlculs de S7 s'han verificat íntegrament pas a pas.

---

## A — Errors tècnics (execució directa) ✅ APLICATS

### A7.qmd

- 🔴✅ **A1 — Exemples d'escriptura (§Exemples 1–3): índex de `@252` incorrecte al text.**
  L'adreça 252 = `0xFC` → bloc 63 (`111111`) → índex = 63 mod 2 = **1**, no 0.
  El text dels tres exemples diu «índex 0» i «reemplaçant el bloc 2»; les
  **figures SVG són correctes** (mostren `etiq 11111, idx 1` i el bloc 63 a la
  **línia 1**, reemplaçant el bloc 1). Correcció només textual:
  - Ex. 1: `sw @252` (bloc 63, índex 1) → còpia a la línia 1, reemplaça el bloc 1.
  - Ex. 2: idèntic canvi d'índex (la MC no s'altera, sense més impacte).
  - Ex. 3: `sw @252` → «Fallada amb $D=0$ a la **línia 1**: es copia el bloc 63
    a la línia 1 (reemplaça el bloc 1)». La història del *dirty bit* a la línia 0
    (`sw @10` / `lw @0`) no canvia.
- 🔴✅ **A2 — `#tip-lru-exemple`: anotacions LRU errònies als passos 1–2.**
  Després de `@38` (ocupa la via 1), la LRU és la **via 0**, no la via 1.
  Passos 3–4 correctes. Es reescriuen les anotacions dels passos 1–2 en
  coherència amb la figura (que no anota res en aquests passos).
- 🔴✅ **A3 — Pseudo-LRU de 4 vies: «dos bits» → «tres bits».**
  El pseudo-LRU en arbre per a 4 vies necessita 3 bits per conjunt (1 bit de
  parella + 1 bit dins de cada parella). Es corregeix la xifra i es precisa la
  descripció.
- 🔴✅ **A4 — §Tecnologies: cicles d'un accés SSD.** 0,05–0,1 ms / 0,25 ns =
  200.000–400.000 cicles → «centenars de milers de cicles», no «desenes de
  milers» (el càlcul del disc dur, «desenes de milions», és correcte).
- 🔴✅ **A5 — Terminologia obligatòria:** «mecanisme hardware senzill» →
  «mecanisme de maquinari senzill» (§Aleatori).
- 🔴✅ **A6 — Català normatiu:** «varis MB» → «diversos MB» (`#tbl-disseny-l1-l2`);
  «tarda … **en** respondre» → «tarda … **a** respondre» (§Multinivell).

### S7.qmd

- 🔴✅ **A7 — `#sol-p7-cache-adreces`: classificació de fallades errònia.**
  El paràgraf final diu que les fallades 5, 8, 10 i 11 són «de conflicte».
  Segons la definició de T7 (§Tipologia), les 5, 8 i 10 són **obligatòries**
  (primer accés als blocs 12, 7 i 15); només la **11** és de conflicte (el
  bloc 3, expulsat, tornaria a ser un encert en una MC completament
  associativa de la mateixa capacitat). Es reescriu: 8 fallades = 7
  obligatòries + 1 de conflicte, mantenint el comentari sobre la competència
  dels blocs 3/7/15 per la línia 3.

### E7.qmd

- 🔴✅ **A8 — Veu: 2a persona del plural.** Cinc enunciats usen el singular
  («calcula», «Proposa», «Raona», «Indica», «Considera», «Justifica»):
  `exr-p7-cache-matriu`, `exr-p7-cache-alternatives`,
  `exr-p7-assoc-completament` (e), `exr-p7-fallades-tipologia`,
  `exr-p7-fallades-programa`. S'harmonitzen al plural (convenció del projecte).

### 22_figs_originals/T7_lru_exemple.svg (figura manual de Roger)

- 🔴✅ **A9 — Tres errades de retolació:**
  1. Mapa MP, files dels bytes 52–55: etiqueta binària «1111» → «**0011**»
     (×4) i número de bloc «63» → «**13**» (52 = `0011·01·00`; el 4t panell ja
     ho descompon bé).
  2. Rètol del 4t panell: «2n accés» → «**4t accés**».
  3. Panell del 2n accés, via 1: «byte 7» → «**byte 39**» (bloc 9 = bytes 36–39; el 3r i el 4t panells ja eren correctes).
  La variant dark es regenera automàticament al pre-render.

## B — Millores i harmonitzacions menors (execució directa) ✅ APLICADES

Extra aplicat: «un altra escriptura» → «una altra escriptura» (Exemple 3, A7.qmd).

- 🟡✅ **B1 (PS)** Títol de secció «## Tipologia de fallades» → «## Tipologia de
  les fallades» (harmonitza amb T7 i E7).
- 🟡✅ **B2 (PS)** «tag» → «etiqueta» a les descomposicions matemàtiques i
  capçaleres de taula (T7 usa «etiqueta» a les descomposicions; «Tag» resta
  només com a anglicisme ja introduït a la prosa de T7).
- 🟡✅ **B3 (PS)** `#sol-p7-assoc-2vies`: «64 blocs» → «64 línies» (distinció
  línia/bloc de la teoria); «quatre etiquetes: 0x54, 0x5C, 0x64, i de nou
  0x5C» → «tres blocs diferents (etiquetes 0x54, 0x5C i 0x64)».
- 🟡✅ **B4 (PS)** «*writeback*» → «*write-back*» (grafia de T7).
- 🟡✅ **B5 (PS)** `#sol-p7-rend-politiques`: afegir l'aclariment d'hipòtesi que
  connecta el $p_e$ de l'enunciat (fracció d'escriptures sobre els accessos)
  amb el $p_e$ de la fórmula (fracció de fallades que són escriptures):
  taxa de fallades suposada independent del tipus d'accés.
- 🟡✅ **B6 (PE)** Taula d'`exr-p7-rend-cpi-separat`: fila «$n_r$ per
  instrucció» → «Accessos per instrucció» ($n_r$ és el paràmetre global; la
  solució ja usa el rètol correcte).
- 🟡✅ **B7 (T7)** Captions pendents: es redacta el caption de
  `fig-assoc-conjunts-taula` (figura ja integrada) i es fixen els captions de
  `fig-cd-diagrama`, `fig-assoc-conjunts-diagrama`, `fig-ca-diagrama` i
  `fig-texe-diagrama` a partir dels esborranys dels comentaris HTML (les
  figures continuen pendents de LO Draw, però el `TODO caption.` desapareix).
- 🟡✅ **B8 (T7)** §Polítiques — Resum: es redacta el text introductori
  (`<!-- TODO text introductori -->`).
- 🟡✅ **B9 (T7)** Gerundis de posterioritat/conseqüència: caption de
  `fig-gap-processador-memoria` («generant un *gap*…» → «cosa que genera…») i
  §Jerarquies actuals («reduint el nombre d'accessos…» → «cosa que redueix…»).
- 🟡✅ **B10 (T7)** `#wrn-gpu-memoria`: «GDDR6» → «GDDR6 o GDDR6X» (la RTX 4090
  de l'exemple usa GDDR6X).

## C — Decisions de Roger (resoltes 2026-07-11: C1, C4–C12 aplicades amb la recomanació; C2 i C3 anotades a `TODO.md §T7`)

- 🔵✅ **C1 — $t_{block}$ (T7) vs. $t_{bloc}$ (E7, S7).** Notació
  inconsistent per al mateix paràmetre. Recomanació: **$t_{bloc}$** a tot
  arreu (política catalana del projecte); implica retocar T7 (§Model de temps,
  `@cau-model-temps`, `@cau-errata-tam`, §TAM) i registrar-ho a
  `13_contrib.qmd` (caldria crear la subsecció `#### T7`).
- 🔵✅ **C2 — $t_{am}$ (enunciats PE) vs. TAM (T7 i solucions PS).** Resolt (2026-07-11): «TAM» a tot arreu. 5 substitucions a E7.qmd (`exr-p7-rend-taxa-traffic`, `-rend-cpi-separat`, `-rend-cpi-unica`, `-rend-mida-bloc`, `-assoc-tam`); S7 ja usava TAM consistentment.
- 🔵📌→TODO **C3 — `exr-p7-assoc-multinivell`: seqüència truncada.** L'enunciat diu
  «seqüència de 28 adreces … : `0, 5, 10, 12, 34, 0, 66, ...`» — amb els tres
  punts l'exercici no és resoluble. Interpretació probable: **7 adreces
  repetides 4 vegades (28 accessos)**. Recomanació: reescriure com «la
  seqüència de 7 adreces següent, repetida 4 vegades (28 accessos en total):
  `0, 5, 10, 12, 34, 0, 66`». **Cal contrastar amb el PDF original** (no el
  tinc disponible en aquest xat).
- 🔵✅ **C4 — `exr-p7-cache-politiques`: columnes «Lectura dades MC» i
  «Escriptura dades MC»** de la taula de l'enunciat no apareixen a les taules
  de la solució. Opcions: (a) afegir-les a les dues taules de la solució
  (recomanat: manté la intenció de l'exercici); (b) retirar-les de l'enunciat.
- 🔵✅ **C5 — `exr-p7-fallades-programa` c): `B` a `0x200` se solapa amb `A`**
  (`0x000`–`0x3FF`). Opcions: (a) canviar l'enunciat a `0x600` (48 blocs de
  distància, mateix múltiple de 16 → mateixa conclusió, sense solapament;
  recomanat) i retirar la nota final de la solució; (b) mantenir `0x200` i
  només polir la redacció de la nota.
- 🔵✅ **C6 — Unitats KB/MB (T7) vs. KiB/MiB (E7).** T7 usa KB/MB/GB a
  `#tbl-tecnologies-memoria`, `#wrn-gpu-memoria` i `#tbl-disseny-l1-l2`;
  E7 usa KiB/MiB («8 KiB», «1 MiB»). T1 no usa cap de les dues. Opcions:
  (a) binari explícit (KiB/MiB/GiB) per a capacitats de MC/MP i decimal per a
  costos ($/GB) i discs; (b) KB/MB pertot. Decisió transversal: registrar a
  `13_contrib.qmd`.
- 🔵✅ **C7 — «ample de banda» (4×) vs. «amplada de banda» (2×) a T7.**
  El Termcat normalitza «amplada de banda». Recomanació: unificar-hi i
  afegir-la a les substitucions obligatòries de `13_contrib.qmd`.
- 🔵✅ **C8 — «va tocar sostre als 3–4 GHz»** (§Fi de l'escalat de Dennard): els
  processadors actuals arriben a 5,5–6 GHz en *boost*. Opcions: (a) matisar
  («la freqüència sostinguda es va estancar en els 3–5 GHz»); (b) mantenir.
- 🔵✅ **C9 — Slug `#cau-errata-tam`.** El nom «errata» és un residu de la
  migració. Cap referència externa: reanomenar a `#cau-tam-retardada`?
- 🔵✅ **C10 — «blocs» per «línies/vies» als enunciats PE.** Set enunciats diuen
  «la MC té N blocs» / «4 blocs per conjunt» per referir-se a línies/vies
  (`cache-matriu`, `rend-mida-bloc` (implícit), `assoc-versions`,
  `assoc-multinivell`, `assoc-completament`, `fallades-tipologia`,
  `fallades-programa`); la teoria i PS distingeixen línia (contenidor) de bloc
  (contingut) — `sol-p7-fallades-tipologia` ja diu «8 línies» quan l'enunciat
  diu «8 blocs». Opcions: (a) harmonitzar sistemàticament («N línies», «N vies
  per conjunt»); (b) mantenir l'ús col·loquial dels enunciats.
- 🔵✅ **C11 — $p_e$ com a distractor.** `exr-p7-rend-cpi-separat` dona
  $p_e = 40\%$ i no es fa servir (les penalitzacions ja es donen per bloc
  modificat/no modificat); `exr-p7-rend-cpi-unica` dona $p_e = 15\%$ i la mida
  de bloc, tampoc necessaris. Opcions: (a) mantenir com a distractors i
  afegir una línia a la solució de `-cpi-separat` que ho digui (recomanat);
  (b) eliminar dels enunciats.
- 🔵✅ **C12 — Notació $m_1/m_2$ sobrecarregada:** a `sol-p7-rend-politiques`
  designen les dues polítiques; a `exr-p7-assoc-tam`, els nivells L1/L2, i la
  teoria usa $m_{L1}/m_{L2}$ i $m_i/m_d$. Cada exercici la defineix
  localment. Opcions: (a) acceptar; (b) diferenciar (p. ex. $m_{L1}$ a
  `assoc-tam`, alineant amb `@eq-tam-multinivell`).

## D — Decisions heretades del xat anterior (recordatori)

- 🔵 **D1** `fig-capacitat-exemple`: dues figures separades o una de combinada (HTML).
- 🔵 **D2** `fig-lru-roger` (màquina d'estats LRU): figura independent o n'hi
  ha prou amb `T7_lru_exemple.svg`.
- ⏳ **D3** 8 figures pendents de LO Draw / referència externa (vegeu `TODO.md §T7`).

## E — Verificacions completades sense incidència ✅

Càlculs verificats pas a pas i correctes: `sol-p7-cache-adreces` (taula E/F),
`sol-p7-cache-politiques` (les dues taules i el resum 74/144 B),
`sol-p7-rend-politiques` (18,8 / 31,5 ns), `sol-p7-rend-cpi-separat`
(1,85 cicles; 28,6 ns; 90,7%; 70,6%), `sol-p7-assoc-2vies` (descomposicions
bit a bit, evolució LRU dels conjunts 19 i 23, 1 encert), `sol-p7-assoc-tam`,
`sol-p7-fallades-tipologia` (A/B/C i apartats b–c), `sol-p7-fallades-programa`
(mapatges, 512 fallades, contraexemple `0x420`). Exemples de T7 verificats:
`tip-mc-numbloc`, `tip-cd-exemple`, `tip-assoc-conjunts-exemple`, seqüència
inicial d'escriptura, exemple de conflicte (16/16 fallades) i de capacitat.
Enunciats sense solució comprovats com a resolubles i ben definits
(`cache-matriu`, `cache-alternatives`, `rend-taxa-traffic`, `rend-cpi-unica`,
`rend-mida-bloc`, `assoc-versions`, `assoc-completament`), amb l'excepció de
`assoc-multinivell` (C3). Referències creuades PE/PS→T7 comprovades: totes
existeixen. Cobertura PE↔T7 completa; selecció PS (8/16) equilibrada per
seccions. `S_criteris.qmd` no existeix al mirall (comentat a `_quarto.yml`).

---

## Fitxers modificats en aquest xat

| Fitxer | Estat |
|:---|:---|
| `01_apunts/A7.qmd` | ✅ A1–A6, B7–B10, extra, C1, C6–C9 |
| `02_exercicis/E7.qmd` | ✅ A8, B6, C5, C10, C12 |
| `03_solucions/S7.qmd` | ✅ A7, B1–B5, C4, C5, C11, C12 + 8 `tbl-colwidths` corregits a suma 100 |
| `22_figs_originals/T7_lru_exemple.svg` | ✅ A9 |
| `13_contrib.qmd` | ✅ nova subsecció `#### T7` (t_bloc, línia/bloc, notació multinivell, unitats) + fila «amplada de banda» a substitucions |
| `TODO.md` | ✅ C2 i C3 a §T7; escombrades globals «amplada de banda» i KB/KiB a §Contingut global |

---

## Segona tanda (2026-07-11, Sonnet 5 High)

Aplicades C1, C4–C12 (recomanacions acceptades per Roger); C2 i C3 anotades a
`TODO.md §T7`. Extra: 8 taules de S7 amb `tbl-colwidths` que no sumaven 100
(convenció de `13_contrib.qmd §Taules`) corregides per escalat proporcional.
Detall C4: les columnes «Lect. MC» / «Escr. MC» s'han definit com a indicadors
S/N d'accés a la matriu de dades de la MC, amb la casuística explicada als
punts de «Comportament per tipus d'accés» de cada apartat.

---

## Tercera tanda (2026-07-11)

C2 resolta: «TAM» harmonitzat a tot arreu (5 substitucions a E7.qmd:
`temps mitjà d'accés a memòria ($t_{am}$)` → `temps d'accés mitjà (TAM)`,
nom canònic de `@sec-tam`). S7 ja era consistent. Pendent a `TODO.md §T7`:
només C3 (seqüència truncada d'`exr-p7-assoc-multinivell`).
