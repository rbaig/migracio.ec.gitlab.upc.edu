# L6 — Registre de tasques de la revisió interna

Data: 2026-07-21.

# Estat

- **Fase A (exploració i comprensió): completada.** Mapa validat per l'usuari.
- **Fase B (verificació numèrica dirigida i anàlisi profund): completada.** Verificació empírica amb **RARS 1.6** headless (assemblatge, recompte d'instruccions, dump de memòria, inspecció de registres) contra el codi font del `CacheSimulator`/`InstructionStatistics` de RARS, més **simulació Python** de la memòria cau amb la semàntica exacta del simulador (tot accés —lectura o escriptura— idèntic: encert → actualitza LRU; fallada → al·loca amb reemplaçament LRU).
- **Fase C (execució): completada.** Executada en Opus High + Thinking (a petició de l'usuari; prioritat de correcció). Tots els ítems aplicats a `L6.qmd` i als fitxers auxiliars (`A7.qmd`, `13_contrib.qmd`, `TODO/TODO.md`); les 4 decisions d'usuari, resoltes.
- **Pendent**: res propi de L6. Les troballes cross-file s'han derivat a `TODO/TODO.md` (L4, A7, terminologia de títols).

# Correccions aplicades (Fase C)

## A. Errors tècnics / numèrics (crítics)

1. **T1 — `.space` amb expressions aritmètiques** (`suma_vector.s`, `suma_vectors.s`, `s6_4_2.s`, `matvec.s`, `s6_5_1.s`): RARS no avalua expressions als operands («Invalid language element: N*4»), de manera que 4 dels 6 programes **no assemblaven**. Substituïdes per literals amb la fórmula al comentari (p. ex. `.space 512  # int A[128]: 512 = 128·4 bytes`). Verificat: els 6 programes assemblen i s'executen.
2. **T2 — `s6_1_1`**: (a) etiqueta de `0x1001014C` corregida de `0x080040` a `0x080080` (binari `0001 0000 0000 0001 0000 000`); (b) apartat 3 redefinit — el bloc de l'enunciat era `0x10` (índex 16 ≠ 20), canviat a `0x1001034` (índex 20 = `0x14`, etiqueta `0x080081`), coherent amb la línia seleccionada.
3. **T3 — `s6_2_4`**: (a) $n_{ins}$ 509 → **510** (`la` s'expandeix a `auipc`+`addi`, 2 instruccions; és el valor que reporta Instruction Statistics); (b) valors finals substituïts: $t_{exe}$ amb cau = 12 950 ns ≈ 12,95 µs, sense cau = 15 200 ns, guany ≈ 1,17; (c) «son» → «són».
4. **T4 — `s6_3_1`**: (a) vector resultant corregit a **`{45, 20, 12, −1, −18}`** (descendent; el solucionari deia `{−18, −1, 12, 20, 45}`, error verificat amb dump de RARS); (b) files «depenent» de la traça omplertes amb els valors concrets; (c) apartats 2-3 completats (36 accessos = 12+10+8+6, 2 fallades cold-start, taxa 34/36 ≈ 0,944).
5. **T5 — `s6_4_3`**: contradicció interna eliminada (afirmava fallades de capacitat i després concloïa, correctament, que totes són cold-start); reescrit al voltant del *working set* instantani (3 blocs).
6. **T8 — `s6_4_2`**: criteri general del farciment precisat — cal que `0`, `PAD/16` i `2·PAD/16` siguin tres línies diferents mòdul 16 (el criteri anterior, «no múltiple de 256», era insuficient: `PAD = 128` fa col·lidir `C` amb `A`).

## B. Correcció tècnica sobre RARS (verificat empíricament amb el codi font)

7. **T6 — política d'escriptura**: eliminada la instrucció de configurar la «política d'escriptura immediata amb assignació» al Data Cache Simulator (§3, §4): **RARS no permet triar-la**. Afegida una nota única a §3: el simulador tracta tot accés igual (al·loca en fallada), cosa que a efectes de recompte coincideix amb la immediata amb assignació. Les taxes esperades no canvien.
8. **T7 — `s6_4_1`**: taxa d'encerts **exactament 0** (el simulador només observa el segment de dades, no el codi de control); eliminat el parèntesi erroni sobre «accessos del codi de control».
9. **T9 — `s6_4_3`/`s6_4_4`**: etiquetes reals de RARS («**Fully Associative**», no «Placement policy: Full»; **Set size** + **Number of blocks** explicitats: 64 blocs per a 16 conjunts × 4 vies, 32 per a × 2 vies); «potència de 2 més proper a 3» → «immediatament superior a 3».

## C. Pedagogia i coherència

10. **T10 — `s6_3_3`**: redacció reforçada (mínim 16 blocs justificat pel fet que qualsevol bloc expulsat es torna a referenciar; 16 blocs consecutius mapen a 16 línies diferents); inicialització del vector de 64 elements precisada a l'enunciat (`.space 256`).
11. **T11 — §5 (tiling)**: taula de geometries reubicada a l'exercici amb id `{#tbl-tiling-geometries}` i referenciada des de la intro i la solució; «blocs de columnes» → «grups de columnes» (per no sobrecarregar «bloc»); nota d'`a0` corregida (s'usa dins el bucle, no només a la sortida); coherència del codi C (`tmp` declarat a la capçalera, `V1` global inicialitzat a 0).
12. **T12 — codificació**: unificada a **En** = encert, **F** = fallada, **L** = lectura, **E** = escriptura a tot L6 (abans §2 usava E = encert i §3 usava E = escriptura, en col·lisió).
13. **Nou exercici `s6_4_5`** (decisió d'usuari, vegeu §E.4): Runtime Log del Data Cache Simulator per classificar les fallades segons les tres C (cold-start / conflicte), reaprofitant `s6_4_1` (CD) i `s6_4_3` (completament associativa). Variant mínima (cold + conflicte) aprovada per l'usuari.

## D. Llengua (català normatiu)

14. **T13**: «**farciment** (*padding*)» amb el patró d'anglicismes de `13_contrib.qmd` (i «farciment» a la resta de la prosa; el símbol `PAD` del codi es manté); *stride* en cursiva amb remissió a `@sec-opt-acces-sequencial` a la primera aparició; «per qué» → «per què».
15. **T14 — `13_contrib.qmd`**: afegida l'entrada `padding → farciment` a la taula de substitucions obligatòries (font: Termcat, Informàtica > Estructura de les dades).
16. **C3 — `A7.qmd`**: «s'obtenen partir de l'adreça» → «s'obtenen **a** partir de l'adreça».

## E. Decisions d'usuari (resoltes)

1. **Taula de geometries del tiling**: buida a l'enunciat (per a l'estudiant) i **omplerta a la solució** com a clau de correcció, amb valors verificats amb RARS (format tiling / original).
2. **Terminologia loop tiling / stride**: mantinguts com a manlleus; **cursiva al títol de §5 mantinguda** (decisió de l'usuari). Afegida una nota a `13_contrib.qmd` que permet manlleus en cursiva als títols de secció, i un TODO a `TODO.md` per revisar tots els títols del corpus.
3. **Notació de §1** ($N_P$/$n_p$): mantinguda, amb una nota de correspondència amb la teoria ($B = 4 \cdot N_P = 2^{n_p+2}$ bytes, $b = n_p+2$; $N_L$ és el mateix símbol que a `@sec-mc-organitzacio`).
4. **TODO del Runtime Log**: resolt amb l'exercici `s6_4_5`; el comentari TODO del capdavant de `L6.qmd` s'ha eliminat.

Decisió ajornada (sense canvi): **terminologia «blocs» vs «línies»** de la geometria de la cau — apuntada a `TODO.md` per a la revisió externa.

# Verificacions superades (constància)

- Els **6 programes** assemblen i s'executen amb RARS 1.6 headless després dels canvis.
- Totes les **taxes d'encerts** verificades amb simulació exacta: `s6_2` (0,75 amb 32×4w i 64×4w; 0,87 amb 32×8w), `s6_2_3` (0,75 invers), `s6_3_1` (34/36 ≈ 0,944), `s6_3_3` (16 fallades amb 32 i 16 blocs; 496 amb 8), `s6_4` (0 en CD; 0,75 en completament associativa i amb grau ≥ 3), `s6_5` (`V1` idèntic al de `matvec.s` amb dades conegudes).
- **Desglossament 3C** de `s6_4_5`: correspondència directa 96 cold + 288 conflicte + 0 capacitat (384); completament associativa 96 cold (96).
- **Taula del tiling** calculada per a 5 capacitats × 5 geometries (accessos: original 528, tiling 640).
- Divs Quarto **equilibrats**; **les 22+ referències creuades resolen** (inclosa la nova `@sec-mc-organitzacio`); cap col·lisió d'IDs.
- `_start` **net** (sense pròleg/epíleg innecessari) en tots els programes.

# Troballes derivades a `TODO/TODO.md` (fora de L6)

- **L4**: la referència `@imp-eqv-dimensions` (enunciat de `s4_1_1`) **no té definició** al repositori (ref trencada); la revisió de L4 ho va passar per alt en corregir el `.space`.
- **A7**: incoherència «word» vs «paraula» respecte d'A2/L6.
- **Global**: revisió de manlleus en cursiva a tots els títols de secció (segons el nou criteri de `13_contrib.qmd`).
- **Coincidència amb la revisió de L4 (2026-07-19)**: va detectar independentment el mateix bug de `.space`; el `.space` de L6 s'ha marcat com a fet a la seva entrada del TODO.

# Fitxers finals modificats

- `04_laboratori/L6.qmd` — tots els canvis anteriors (blocs Quarto equilibrats; 6 programes assemblen).
- `01_apunts/A7.qmd` — correcció del typo «a partir».
- `13_contrib.qmd` — entrada `padding → farciment` + nota de manlleus en cursiva als títols.
- `TODO/TODO.md` — decisions pendents de L6 i troballes cross-file.
- `TODO/L6_tasques.md` — aquest registre.
