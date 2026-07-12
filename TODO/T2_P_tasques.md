# T2_P_tasques.md — Revisió interna A2-E2-S2

Registre d'accions de la revisió interna del tema 2 (`01_apunts/A2.qmd`, `02_exercicis/E2.qmd`, `03_solucions/S2.qmd`). Generat a la Fase B (Fable 5 High + Thinking). La Fase C (Sonnet High, sense Thinking) executa la secció A i presenta la secció B a l'usuari.

Fonts de veritat consultades: especificació no privilegiada de RISC-V International (riscv-isa-manual, `main`), RISC-V Assembly Programmer's Manual, codi font de RARS (`PseudoOps.txt`, `Assembler.java`, `Directives.java`), verificació numèrica pròpia amb Python (totes les codificacions i layouts recalculats de manera independent).

---

## A. Accions executables (no requereixen aprovació)

### A2.qmd

1. **[Tècnic] Recompte RV32I 41 → 40** (`#nte-riscv-rv32i`, ~L164). L'especificació diu «RV32I contains 40 unique instructions»; `fence.tso` es codifica com a variant de `fence` (camp `fm`), no com a instrucció pròpia. Canviar «Nombre d'instruccions: **41**» → «**40**» i a la línia «**Sistema**: `ecall`, `ebreak`, `fence`, `fence.tso`» deixar «`ecall`, `ebreak`, `fence`» amb nota entre parèntesis: «(`fence.tso` és una variant codificada dins `fence`)».
2. **[Tècnic] Typo `imm12$`** (L464): `(`imm12$`)` → `(`imm12`)`.
3. **[Tècnic] Macro `zero_elem`** (`#wrn-macros-rars`, ~L631): `sll t6, %idx, 2` → `slli t6, %idx, 2`. Verificat: RARS no defineix cap pseudo `sll` amb immediat (`PseudoOps.txt`); el codi actual no assembla.
4. **[Tècnic] Fragment `21_riscv/RV32I_instruccions_lectura_escriptura.qmd`**: columna Nom de `lhu` «load half» → «load half **unsigned**» i de `lbu` «load byte» → «load byte **unsigned**». Afecta A2 i `11_riscv.qmd` (mateix include).
5. **[Tècnic] Taula `#nte-registres-proposit-general`** (~L1233): la fila d'alineació té 5 especificadors (`| :---: | :---: | :--- | :--- | :--- |`) per a 4 columnes de capçalera. Eliminar-ne un.
6. **[DRY] Pseudos `mv` i `li` → include**: a `#nte-pseudoinstruccio-mv` i `#nte-pseudoinstruccio-li`, substituir les files inline de la taula per `{{< include ../21_riscv/RV32I_pseudo_mv.qmd >}}` / `RV32I_pseudo_li.qmd` (mantenint la capçalera de 3 columnes; contingut verificat idèntic). Actualitzar a `13_contrib.qmd` la taula de fitxers `21_riscv/`: «T2 (pendent)» → «T2» a les dues files.
7. **[Format] `tbl-colwidths` que no sumen 100** (escalar proporcionalment a 100):
   - L195 `#tbl-gcc-rvimf` `[15,5,55]` → `[20,7,73]`
   - L308 (taula de camps de `#tip-codificacio-instruccions`) `[5,15,5,5,5,5,5,5,7]` → `[9,26,9,9,9,9,9,8,12]`
   - L394 (`#nte-segments-memoria`) `[10,10,15,20]` → `[18,18,27,37]`
   - L401 (`#wrn-segments-elf`) `[10,5,40]` → `[18,9,73]`
   - L902 i L914 (`#imp-variables-mida-*`) `[25,10,18,23]` → `[33,13,24,30]`
   - L1000 `#tbl-LSb-LSB` `[25,25,10]` → `[42,42,16]`
   - L1350 (`#nte-load-store`) `[5,20,40,15,5]` → `[6,24,47,17,6]`
   - **NO tocar** L786 (`[15,15,25,55]`): és dins el bloc HTML comentat de `startup.s` (vegeu B.12).
8. **[Format] Duplicat literal** (L813-820, `#sec-declaracio-variables-escalars`): el bloc `<tipus> <nom> [= valor_inicial];` apareix dues vegades seguides. Eliminar el segon.
9. **[Llengua] «mig paraula» → «mitja paraula»** (L1380 títol, L1391, L1408, L1409, L1422 —aquest és el correcte, referència—, L1427; i S2 L217). Mantenir els slugs existents `{#sec-acces-mig-paraula-byte}` i `{#sec-carrega-naturals-mig-paraula-byte}` (cap referència externa, però estabilitat d'URL; si es prefereix regenerar-los, cap risc: verificat 0 referències).
10. **[Llengua]** L836: «Un *dirty hack* cometre errades» → «Un *dirty hack* **és** cometre errades».
11. **[Llengua]** L2001 (nota `[^comram]`): «cas d'us» → «cas d'ús».
12. **[Llengua]** L1771: «una múltiple de 2^n» → «un múltiple de $2^n$»; i a la taula de `#nte-directives-align-space`: «frontera 2ⁿ bytes» → «frontera de $2^n$ bytes» (superíndex Unicode → math, criteri de `13_contrib.qmd`).
13. **[Tècnic] `.balign`**: al títol de `#nte-directives-align-space` («`.space`, `.align`, `.balign`»), eliminar «`.balign`»: RARS no la suporta (verificat a `Directives.java`) i la taula tampoc no la llista.
14. **[Format] Títol de callout** L263: «RV32I ISA — Tipus de format de les instruccions RV32I.» → «RV32I ISA — Tipus de format de les instruccions» (sense punt final ni repetició).
15. **[Format]** L72: «G - Extensions més comunes» → «G — Extensions més comunes» (guió llarg).
16. **[Llengua] Apòstrofs tipogràfics** U+2019 (13 línies a A2, p. ex. «d’adreces»): normalitzar a apòstrof recte `'`.
17. **[Tècnic] Terminologia** `#tip-desreferencia-punters-c`: «es copia l'etiqueta en `t2` amb la **macro** `la`» → «amb la **pseudoinstrucció** `la`» (T2 és justament on es defineix la distinció).
18. **[Format] Notació de l'equació** `{#eq-acces-aleatori-vector}`: normalitzar a `$$@\texttt{vec[i]} = @\texttt{vec[0]} + i \cdot T$$` (índex `[0]` dins `\texttt`, $T$ en math coherent amb el text posterior, sense espai després de `@`).
19. **[Tècnic] Referències locals dels bucles** (`#sec-acces-vectors-bucles`): «L'**accés aleatori** (@sec-matrius-acces-aleatori)» → «(@sec-vectors-acces-aleatori; per a matrius, @sec-matrius-acces-aleatori)»; «L'**accés seqüencial**(@sec-opt-acces-sequencial)» → «L'**accés seqüencial** (@sec-acces-sequencial-exemple; optimització definida a @sec-opt-acces-sequencial)» — i afegir l'espai que hi falta abans del parèntesi.
20. **[Format] `#nte-punters-32-bits` sense títol** (L1457): afegir «## RV32I — Mida dels punters» (contrib: els `#nte-` porten títol).
21. **[Estil]** `#nte-rv32i-model-memoria`: «de **32** bits (/línies)» → «de **32** bits» (el parèntesi «(quantitat de línies del bus d'adreces)» anterior ja ho explica).
22. **[Contrib] Referència errònia a `13_contrib.qmd`** (§Prefixos de mida): «les referències de mercat aproximades de `A2.qmd §El problema de la diferència entre processador i memòria`» → la secció és a **`A7.qmd`** (`{#sec-gap-memoria}`). Corregir fitxer i, si es vol, referenciar el slug.

### E2.qmd

23. **[Tècnic] `#exr-p3-immediats-declaracio`**: eliminar la taula de «continguts inicials de memòria» (`00 01 02 03...`) i la frase que la introdueix — **contradiu les declaracions `.data`** del mateix enunciat (residu copiat d'`#exr-p3-memoria-lw-sw`). Verificat que l'exercici es resol completament amb les declaracions: a) `t2 = 0x10010008` (valor de `D[0]`), `lb 8(t2)` = byte de `C[1]` = `0xFF` → −1; `B` = 3; **B final = 2**. Mantenir «Tots els apartats parteixen del mateix estat inicial».
24. **[Tècnic] `#exr-p3-immediats-luiaddi` a)**: «Quina seqüència d'instruccions genera el **compilador**» → «l'**assemblador**».
25. **[Estil] `#exr-p3-memoria-lw-sw`**: la primera frase presenta les variables `A`, `B` i `C` que el codi no usa. Reformular: «Donats els continguts inicials de registres i memòria següents (en hexadecimal):» eliminant la frase de les variables.
26. **[Tècnic] Nota d'`#exr-p3-ascii-align`**: precisar la semàntica real de RARS (verificada a `Assembler.java`): «la directiva `.align 0` desactiva l'alineació automàtica **fins al final del segment `.data` actual** (cap `.align n` posterior no la reactiva; només una nova directiva `.data`)». Nota: el layout de l'exercici és idèntic amb les dues interpretacions (verificat), per tant només cal ajustar el text de la Nota.
27. **[Format] `#nte-p3-remissio-enters` sense títol** (L224): afegir títol curt (p. ex. «## Remissió — Representació de naturals i enters») o deixar-lo sense títol si es pren la decisió B.9 en sentit contrari (vegeu-la).
28. **[Llengua] Secció «## Strings»** (L596) → «## Cadenes de caràcters» (substitució obligatòria de `13_contrib.qmd`).

### S2.qmd

29. **[Llengua] Secció «## Strings»** (L651) → «## Cadenes de caràcters».
30. **[Llengua]** L18: «Cal tres `add` encadenats» → «Calen tres `add` encadenats».
31. **[Llengua]** L217: «byte i mig paraula» → «byte i mitja paraula».
32. **[Format] Callout sense ID** (L282, remissió a S1): afegir ID, p. ex. `{#nte-p3-remissio-enters-solucions .callout-note}`.
33. **[Tècnic] `#sol-p3-registre-rtovc`**: afegir una observació al final de cada apartat (a i b): el codi **modifica també `g` (`t1`)** —i a b) també `i` (`t3`)—, de manera que la sentència C equivalent estricta inclouria aquests efectes laterals; la resposta dona el valor final de `f` en funció dels valors **inicials** de les variables.
34. **[Tècnic] `#sol-p3-vectors-bucle` c)**: la nota «`t0`–`t6` exhaurits» és falsa (`t1`/`suma` no s'usa a l'apartat c). Reescriure el bucle només amb `t0`–`t6` reutilitzant `t6` després del `lw` i usant `t1` per a l'adreça destí, i eliminar la nota sobre `a0`/`a1`:

    ```
            la      t2, v           # invariant: @v[0]
            la      t3, w           # invariant: @w[0]
            li      t4, 10          # invariant: N
            li      t5, 9           # invariant: N - 1
            li      t0, 0           # i = 0
    bucle_c:
            bge     t0, t4, fibucle_c
            slli    t6, t0, 2       # t6 = i * 4
            add     t6, t6, t2      # t6 = @v[i]
            lw      t6, 0(t6)       # t6 = v[i] (l'adreça ja no cal)
            sub     t1, t5, t0      # t1 = 9 - i
            slli    t1, t1, 2       # t1 = (9 - i) * 4
            add     t1, t1, t3      # t1 = @w[9 - i]
            sw      t6, 0(t1)       # w[9 - i] = v[i]
            addi    t0, t0, 1       # i++
            j       bucle_c
    fibucle_c:
    ```
    (Codi verificat lògicament; `suma`/`t1` només està assignada per l'exercici als apartats que la usen.)
35. **[Format] `#sol-p3-strings-copia`**: «(com al bucle de @exr-p3-strings-longitud)» → «@sol-p3-strings-longitud» (el bucle és a la solució, no a l'enunciat).

### Verificat correcte (cap acció)

- Totes les codificacions de `#tip-codificacio-instruccions` (6 instruccions + abocament RARS) i de `#sol-p3-format-ctom` (4 instruccions): recalculades bit a bit, **totes correctes**.
- Expansions de `li` (`0x11223344`, `0x11223800`, `0xDEADBEEF`) i tota l'aritmètica `hi20`/`lo12` de `#sol-p3-immediats-luiaddi`: **correctes**.
- Nota d'expansió de `mv` a RARS (`add rd, zero, rs`): **correcta** (verificat a `PseudoOps.txt`; l'estàndard usa `addi rd, rs, 0`, tal com diu el text).
- `la` → `auipc` + `addi` (2 instruccions): **correcte**.
- Layouts i padding d'`#exr-p3-immediats-contingut`, `#exr-p3-memoria-declaracio` (`0x1001000C` = `0xFE`, `0x1001001C` = `0x78`), `#exr-p3-memoria-contingut`, `#exr-p3-ascii-align`, i la solució `#sol-p3-ascii-contingut`: **tots recalculats i correctes** (RARS alinea automàticament cada directiva a la seva mida, `.dword` inclòs).
- Traces de `#sol-p3-memoria-lw-sw`, `#sol-p3-memoria-endianness`, `#sol-p3-memoria-lb-lh`, `#tip-load-store-half-byte`, `#tip-load-half-byte-unsigned`: **correctes**.
- Desassemblatges d'`#exr-p3-format-mtoc`: a) `add a2, a0, a1`, b) `addi s0, a0, -4`, c) `sw t1, 0(t0)`, d) `slt t0, t0, t1` (vegeu B.4).
- `#exr-p3-ascii-char-int` b): `t0 = 0x00000042`. `#exr-p3-strings-minus`: coherent («FUNCIONA» → minúscules).
- Recomptes M = 8 i F = 26: **correctes** segons l'especificació.
- Bucles de `#tip-vector-acces-aleatori` (5 instruccions de control) i `#tip-optimitzacio-acces-sequencial` (4): recomptes i traces **correctes**.
- Codi de `#sol-p3-vectors-cerca`, `#sol-p3-vectors-punter-aritm`, `#sol-p3-strings-longitud`, `#sol-p3-strings-copia`: **correcte**.
- Referències creuades externes d'A2/E2/S2: totes resolubles **excepte** `@imp-llenguatges-de-referencia` (vegeu B.13).

---

## B. Decisions de l'usuari

1. ~~**Figura del compendi a `#nte-instruccions-tipus`**~~ **RESOLTA (criteri: font de veritat RISC-V International, `@riscv_rv32i`).** La font (`docs.riscv.org`, citada a `15_bibliografia.bib`) diu explícitament «four core instruction formats (R/I/S/U)»; B i J són variants de S i U. Aplicat a A2.qmd: el text ara diu «quatre formats nuclears» amb cita `[@riscv_rv32i]`, i el callout `#nte-instruccions-tipus` (ara `#fig-compendi-registres`, renombrat del prefix reservat `fig-rv-`) aclareix que el caption («tipus R, I i S») només cobreix els formats ja vistos a T2, amb un paràgraf que anuncia B/U (aquest tema, `#nte-instruccio-lui`) i el detall complet de B/U/J a T3 (@nte-format-b, @nte-format-u, @nte-format-j), i R4 com a possible contingut de T5 (`#sec-tema-coma-flotant`; pendent de decisió, TODO d'A5 confirmat: `<!-- TODO: cal introduir el R4-TYPE? (Harris) -->`). **Acció addicional feta a A3.qmd** (fora de l'abast estricte del xat, però demanada explícitament i coherent amb la política de correccions sistemàtiques de `13_contrib.qmd`): afegides referències creuades cap a T2 als tres callouts `#nte-format-b`, `#nte-format-j`, `#nte-format-u`, indicant que B/J/U són variants o continuació de S/U ja presentats a T2.
**Nota tècnica**: la figura en si (`compendi_registres__registre_*.svg`) es genera automàticament pel pipeline `25_scripts/gen_regs.py` a partir de `24_specs/registres.toml`, que conté totes les entrades `T2_instruccio_tipus_*` a `T9_*` en un sol compendi (vegeu `13_contrib.qmd §Fitxer de referència tècnica`); no és editable des d'un fitxer `.qmd`. La imatge mostrada seguirà incloent R/I/S/B/U/J/R4; la solució aplicada actua sobre el **text i el caption** que l'envolten, no sobre el contingut visual de la figura. Si es vol una figura visual que mostri només R/I/S, cal una nova entrada al TOML (fora de l'abast d'aquest xat, que només toca `.qmd`).

2. ~~**«Sis formats bàsics»**~~ **RESOLTA (mateix criteri que B.1):** «sis formats d'instrucció» → «quatre formats nuclears d'instrucció [@riscv_rv32i]», amb el matís de B/J com a variants explicat al mateix paràgraf. Frase enredada del *word* corregida de passada: «un **word** (32 bits, 4 bytes, a RISC-V 32 bits)» → «un **word** (a **RV32I**, 32 bits, 4 bytes)».
3. ~~**Instruccions no introduïdes usades a T2**~~ **RESOLTA (criteri: remissions puntuals lleugeres).** Afegit un nou callout `#cau-avancament-instruccions-bucles` a A2.qmd, just abans del primer bucle (`#tip-vector-acces-aleatori`), que explica intuïtivament `beq`, `j` i `slli` amb remissió al detall formal a T3 (@sec-desplacaments-de-bits, @sec-salts). Una única remissió cobreix els dos blocs de bucle de la secció (el segon només reusa `beq`/`j`, ja explicades). A la macro `zero_elem` (`#wrn-macros-rars`, aprofundiment opcional, primera aparició de `slli` al document), s'ha afegit un comentari puntual al codi amb la mateixa remissió, sense duplicar tot el callout.
4. ~~**`#exr-p3-format-mtoc` d)** desassembla a `slt`~~ **RESOLTA (criteri: mantenir `slt` amb remissió).** Afegida remissió a l'apartat d) de l'enunciat (E2.qmd) cap a `@sec-instruccions-comparacio-slt` (A3.qmd, T3). No hi ha solució d'aquest exercici a S2.qmd (no forma part dels 13/31 seleccionats), per tant no calia tocar-lo.
5. **`#exr-p3-memoria-byte-noexcepcio`** — ambigu i possiblement infactible tal com està: si «el valor de `t1`» és la **paraula sencera**, el mínim sense desplaçaments són **10 línies** (`la` + `sw` a `A` + 4 parells `lb`/`sb` de dalt a baix), per sobre del límit de 8; si és només el **byte** LSB, són 2 línies i la pista sobre valors temporals a `A` sobra. Opcions: (a) reescriure per a la paraula sencera amb límit de 10-12 línies; (b) explicitar «el byte de menys pes de `t1`» i treure la pista.
6. **`#exr-p3-ascii-suma`** — per què `d3` té 2 bytes si la suma màxima (9+9=18) cap en 1? Si «algorisme de suma dígit a dígit» implica resultat de **dos dígits decimals** (desena + unitat), cal dir-ho (i si en binari o en ASCII). Proposta de reescriptura disponible en qualsevol de les dues direccions.
7. **Prefixos d'IDs**: E1 = `p1-`, **E2 = `p3-`**, E3 = `p4-` (numeració llegada de les col·leccions MIPS). Renumerar E2/S2 a `p2-` (canvi coordinat als dos fitxers; 0 referències externes verificades) o mantenir el llegat.
8. **Ordre de seccions d'E2/S2 vs. A2**: «Format de les instruccions» apareix a E2 després de «Representació de caràcters», mentre que a A2 és la secció 2. Reordenar E2/S2 seguint A2, o mantenir (l'ordre actual va de menys a més dificultat operativa).
9. **Veu dels `#tip-`**: `13_contrib.qmd` mana 2a persona del **plural** («calculeu»), però la pràctica real d'A2 («Determina»), A3 («Calcula»), A4 i de tots els enunciats E1-E3 («Tradueix», «Escriu») és el **singular**. Harmonització transversal: (a) actualitzar `13_contrib.qmd` al singular (canvi de 1 línia, coherent amb la pràctica); (b) passar tots els fitxers al plural (canvi extens). Afecta també la tasca A.27.
10. **`#cau-`/`#imp-` llargs o amb títol** contra la convenció («sense títol, curt, en negretes»): `#cau-arquitectura-vs-estructura`, `#cau-extensions-vs-profiles`, `#cau-dades-escalars-en-regs-estructurades-en-mem`, `#imp-ec-nomes-rv32i-m-f`, `#imp-operador-adreca-de`, `#imp-codi-format-criteris`, `#imp-memoria-mw-mh-mb`... És un patró estès a tot el llibre: decidir si es relaxa la convenció a `13_contrib.qmd` (p. ex. «títol admès si el callout supera N línies») o es reescriuen. *Recomanació: relaxar la convenció; reescriure-ho tot és desproporcionat.*
11. **«És virtual» al model de memòria** (`#nte-rv32i-model-memoria`): presentar la memòria virtual com a característica del model de memòria de RV32I és imprecís (la traducció d'adreces pertany a l'arquitectura privilegiada; a RARS es treballa sense traducció). Proposta: «— Les adreces del programa **poden ser virtuals**: en un sistema amb SO, la MMU les tradueix a adreces físiques (@sec-mv-espais, T8). A RARS no hi ha traducció.» Validar redacció.
12. ~~**`#tip-alineacio-incorrecte`** — incoherència amb l'adreça `0x00400020`...~~ **RESOLTA (canvi extern, `TODO/TODO.md` ara accessible):** la hipòtesi de treball confirmada per l'usuari és **no hi ha `startup.s`** durant la revisió interna (decisió ajornada a la revisió externa). El bloc `#imp-programa-esquelet`/`#imp-exception-handler` d'A2.qmd (L719-784 aprox.) s'ha de tractar amb aquesta hipòtesi: l'esquelet actiu és el que **no** usa `startup.s` (`li a0,0` + `li a7,93` + `ecall`, ja correcte a A2). Acció derivada: a `#tip-alineacio-incorrecte`, com que no hi ha `startup.s`, el punt d'entrada és directament `_start` a `0x00400000`; recalcular l'adreça de l'excepció suposant només el codi de l'exemple (sense les 3 instruccions de `startup.s`): `la t0,AA` (2 instr.) + `lb`+`lh`+`lw` (3 instr.) = 5 instruccions abans de `lh t4,5(t0)` → adreça `0x00400000 + 5×4 = 0x00400014`. **Acció executable derivada per a la propera Fase C**: canviar `0x00400020` → `0x00400014` a `#tip-alineacio-incorrecte`.
13. ~~**`@imp-llenguatges-de-referencia` trencada**~~ **RESOLTA (canvi extern):** el callout `#imp-llenguatges-de-referencia` ara existeix a `index.qmd` (L239). Les referències des d'A1 (L16) i A2 (L11) ja resolen correctament; no cal cap acció. `TODO/TODO.md §index.qmd` indica que encara hi ha una tasca de consolidació pendent en aquell callout (entrada duplicada de toolchain), però és responsabilitat d'`index.qmd`, fora de l'abast d'aquest xat (A2/E2/S2).
14. **Matrius a T2**: exemples de declaració, decaïment i `sizeof` amb matrius quan són matèria de T4. Mantenir amb les remissions actuals (ja hi són: `@sec-matrius-declaracio` etc.) o retallar. *Recomanació: mantenir; les remissions existeixen i la declaració conjunta és natural.*
15. **Solapament §Declaració ↔ §Visibilitat i durada**: el paràgraf inicial de «Visibilitat i durada» repeteix la definició de declaració/tipus/nom/valor inicial. Fusionar o retallar el paràgraf repetit (DRY).
16. **Cobertura de S2**: 13/31 exercicis resolts. Confirmar que la selecció és la prevista per `S_criteris.qmd` o encarregar ampliació (probablement fora de l'abast d'aquest xat).
17. ~~**TODO.md**: no és al mirror públic~~ **RESOLTA (canvi extern):** ara accessible a `TODO/TODO.md` (la ruta ha canviat; `CLAUDE.md` i `13_contrib.qmd` ja actualitzats amb la nova ruta). Contingut revisat: no hi ha cap tasca pendent específica de T2/A2/E2/S2 més enllà de les ja detectades (`startup.s` → vegeu B.12, resolta; substitucions globals de cometes → coherent amb A.16). Sí rellevant transversalment: decisió oberta sobre coherència de títols als `.callout-caution` (relacionat amb B.10 d'aquest registre, però l'anàlisi del propi `TODO.md` és més detallada per temes — la decisió es pren a nivell de tot el llibre, no només T2).

---

*Fase C pendent. Bloc comentat de `startup.s` (A2, L747-795): no tocar (decisió de l'usuari pendent).*
