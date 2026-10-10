# Registre de decisions

El perquè i l'historial de les regles del llibre, datats i amb els commits. Les regles són a `13_contrib.qmd` (capítol «Contribueix-hi»), curtes i sense historial; cada regla que té entrada aquí hi enllaça amb el seu identificador.

**Format de cada entrada.** Un encapçalament que només porta l'identificador (`### D-n`), perquè GitLab i GitHub en facin la mateixa àncora (`#d-n`). A sota, una línia amb la decisió, on és la regla, la data i els commits; després, el perquè i el que la regla va substituir. Un identificador no canvia mai: una entrada nova pren el número següent, encara que vagi a una secció anterior. Una regla nova o canviada de `13_contrib.qmd` porta la seva entrada, en el mateix commit.

**Què hi va.** El que explica per què una regla és com és: el motiu, les alternatives descartades, el que va substituir i qui ho va decidir. Els plans de feina i les notes de desplegament no hi van (decisió de l'usuari, 2026-10-07, en crear el registre a la fase 7e de `CLAUDE.md §Pla de treball`).

**Els commits** són els que van escriure la regla a la guia (`git log -S` sobre `13_contrib.qmd`, que abans es deia `07_contrib.qmd` i `contrib.qmd`) i els que el text ja citava. «L'usuari» és l'editor del llibre. Fins al 2026-10-07, tot aquest text era dins de les regles mateixes, a `13_contrib.qmd`: `git show a125e3f:13_contrib.qmd` en dona l'última versió.

## Contingut

### D-1

**Precedència textual** · `13_contrib.qmd §Criteri general` · 2026-07-13 · `ccae7dd`

Es va escriure a la revisió interna de T8 com a «criteri general, aplicat aquí al bit `E`», dins de §T8. És la regla que va decidir la reescriptura dels bits `E` i `V` dels problemes heretats ([D-18](#d-18)). Des del 2026-10-07 és a §Criteri general, perquè no és pròpia de T8.

### D-2

**Les figures dels callouts del compendi, sense etiqueta ni peu** · `13_contrib.qmd §Fitxer de referència tècnica` · 2026-10-04 · `3bf711c`

Fins al 2026-10-04 (fase 7c) la regla deia que les figures dels callouts de `11_riscv.qmd` portaven `#fig-rv-*`, i cap figura del compendi no en tenia; les dels `#nte-` dels `Ax.qmd` sí que en portaven, quinze, i es van treure (decisió de l'usuari 7 de la fase 7c, opció A, amb les dues taules amb etiqueta dels `#nte-`).

### D-3

**Taules amb més d'un fragment font: fusió prèvia, fora del pre-render** · `13_contrib.qmd §Fitxer de referència tècnica` · 2026-07-08 · `e79d111`, `c5d9416`

Quarto no permet encadenar dos `{{< include >}}` consecutius dins la mateixa taula *pipe*: el primer tanca la taula i la resta cau a text cru (*line block* de Pandoc). D'aquí la fusió prèvia amb `25_scripts/gen_taules_auto.py`.

A diferència dels altres scripts de `25_scripts/`, aquest no es crida des del `pre-render` de `_quarto.yml`: Quarto resol els `{{< include >}}` dels capítols en un escaneig de configuració que s'executa *abans* del pre-render, de manera que el fitxer fusionat ha d'existir al disc abans d'invocar `quarto`.

### D-77

**Zifencei, fora de les extensions d'EC** · `13_contrib.qmd §Extensions RISC-V a EC` · 2026-10-09

Decisió de l'usuari (2026-10-09, fase 8a, decisió 2), a proposta de Claude Code. Fins llavors la taula d'extensions deia «Zifencei · Instruccions de barrera d'instruccions (`fence.i`) · T9», amb el `filename` `RV32IZicsrZifencei`, i `A2.qmd` (`#imp-ec-nomes-rv32i-m-f`) la situava a T9. Però cap fitxer de T9 no en parlava, cap bloc no portava aquell `filename`, i el mateix A2 (`#wrn-model-memoria-relaxat`) deixa `fence`, `fence.tso` i `fence.i` fora de l'abast. L'alternativa, presentar `fence.i` a A9, es va descartar. Ho va detectar la fase 7e, en partir la guia (`TODO.md §T9`, avui a l'arxiu, `24_specs/arxiu_todo.md` §Entrades retirades → Executades), i ho va confirmar la revisió tècnica d'A2 de la fase 8a.

### D-85

**Les convencions d'EC no penalitzen l'avaluació, tret que s'indiqui** · `13_contrib.qmd §Callouts` · 2026-10-09

Decisió de l'usuari (2026-10-09), en fixar les convencions de D-83 i D-84: «el no seguiment d'aquests convenis no penalitza l'avaluació de l'assignatura a no ser que estigui explícitament indicat el contrari». Es diu una sola vegada, al primer callout `#imp-` dels apunts (`#imp-convencions-ec`, A1; la presentació, `index.qmd`, en té un abans, la taula de referències tècniques), i hi remet el criteri de format del codi d'A2 (`#imp-codi-format-criteris`), que ja deia que el format no s'avalua per si mateix.

### D-97

**«Laboratori 1», o L1: no «Sessió 1» ni «S1»** · `13_contrib.qmd §Ús d'aquesta guia` · 2026-10-09 · `d325f26`

Decisió de l'usuari (2026-10-09), literal: «Laboratori: `Laboratori Y` i `LY`. Per tant, substitueix totes les instàncies `Sessió Y` o `SY`. Justificació: simplificació de la nomenclatura ("Laboratoris" -> "Laboratori 1", "L1", etc.) i resolució ambigüitat amb "Solució/ons"». «S1» volia dir alhora la primera sessió del laboratori al menú i les solucions del tema 1. L'usuari va canviar el menú i els títols (`_quarto.yml`, `_variables.yml`, `d325f26`), amb els títols curts de la resta de parts: «A1», «P1» i «S1», en lloc de «T1» a totes tres. La resta és la proposta de Claude Code que va acceptar: els textos numerats («Sessió 1» a la capçalera del calendari, l'exemple de la guia, el `README.md`, la columna «Tema» del glossari de termes, que deia «Lab. 1», i l'agent del calendari). Es queden com eren: «sessió» com a esdeveniment («abans de l'inici de la sessió»); els identificadors (`sessio1`, `#sec-sessio-*`), que no es veuen; els títols dels quaderns antics citats a `14_LICENSE.qmd` i al `.bib`; i els noms dels lliuraments (`s3_4_1.s`). De pas es va veure que `25_scripts/titols_pdf.lua` només reconeixia els títols curts de la forma «T1 …» i «S1 …»: des de `d325f26`, els marcadors del PDF dels apunts, dels problemes i del laboratori tornaven a dur el títol llarg, i només els de les solucions duien el curt. El filtre reconeix ara «A1», «P1», «S1» i «L1».

## Decisions per tema

### D-4

**`.globl`, no `.global`** · `13_contrib.qmd §T2 i T3` · 2026-10-02 · `4a5cad5`

Motiu: GCC genera `.globl` (verificat amb GCC 14.2, `gcc -S`), i RARS 1.6 assembla `.global` (verificat), de manera que l'estudiant només se'l trobarà en codi escrit a mà o d'altres arquitectures, com ARM. Des del 2026-10-02 (revisió externa de T3, fase 3b), el text de T3 (`#nte-globl`) tampoc no l'esmenta: només el recull la taula de directives del compendi.

### D-5

**Quatre formats nuclears d'instrucció, i on es presenta cada un** · `13_contrib.qmd §T2 i T3` · 2026-10-01 · `b2530c7`, `5f2f1eb`

El criteri dels quatre formats nuclears es va adoptar a la revisió interna de T2 (2026-07) i es va escriure a `A2.qmd`; fins al 2026-10-01 no era a la guia, només a una entrada del `TODO.md` (`git show 4a33a74:TODO.md`). L'escombrada del 2026-10-01 no en va trobar cap altre recompte al corpus.

On es presenta cada format és decisió de l'usuari (2026-10-01, opció b): fins llavors, `A2.qmd` ajornava el format U a T3, i a A3 el J es presentava com a «variant del format Tipus-U, presentat més avall en aquest mateix tema», abans del U. El callout `#nte-format-u` va passar a T2, al costat de `lui` (`git show f066a8e:TODO.md`). `#nte-instruccio-auipc` hi és des del 2026-10-06 (`fb634e4`).

### D-6

**Etiquetes de bucle: el prefix `fi-`, i la numeració dels bucles germans** · `13_contrib.qmd §T2 i T3` · 2026-09-23, 2026-10-07 · `a507297`

El prefix de sortida `fi-` és la forma majoritària al corpus. La numeració de les etiquetes quan hi ha dos bucles al mateix bloc és decisió de l'usuari (2026-09-23): no es toca el codi i es documenta la convenció, perquè renombrar-les a `for:`/`fifor:` hi duplicaria etiquetes i el fragment no assemblaria. L'únic cas al corpus, quan es va escriure, era la solució de `s3_4_2.s` (`L3.qmd`), on `moda` té el bucle d'inicialització de l'histograma i el de recorregut de la cadena (`24_specs/arxiu_todo.md` §Entrades retirades, «Etiquetes de bucle heterogènies a L3» i «`fwhile:` → `fiwhile:` al laboratori»).

Fins al 2026-10-07 les etiquetes de sortida numerades eren `ffor1:` i `ffor2:`, a L3 i a l'exemple de la regla, contra el prefix `fi-` de la mateixa regla. Decisió de l'usuari (2026-10-07, fase 7e): `fifor1:` i `fifor2:`, amb els seus salts; el bloc de L3 assembla igual a RARS 1.6 (49 paraules al bolcat de `.text`, idèntiques).

### D-7

**Alineació de la pila: el fet de l'ABI i el criteri d'EC, en dos callouts** · `13_contrib.qmd §T2 i T3` · 2026-10-04 · `552ff1a`

`#nte-abi-alineacio-pila` (el fet: l'ABI exigeix múltiples de 16) i `#imp-abi-alineacio-pila` (el criteri d'EC: múltiples de 4) es van separar el 2026-10-04, a petició de l'usuari.

### D-8

**`.section` no s'utilitza: RARS 1.6 no admet la forma llarga** · `13_contrib.qmd §T2 i T3` · 2026-09-23 · `6fcee2c`

Verificat executant RARS 1.6 el 2026-09-23 (el registre i les ordres de reproducció són a `24_specs/arxiu_todo.md` §Entrades retirades, «Canvi de criteri `.section` — retirat per l'experiment»). Dues fallades, totes dues cares:

- `.section .data` i `.section .text` **no assemblen**: error `.section must be followed by a section name`. Ho causa l'analitzador lèxic —`.data` i `.text` són *tokens* de directiva i, darrere de `.section`, es consumeixen com a directiva pròpia sense arribar-hi mai com a operand—, de manera que no hi ha grafia que ho salvi (tabulador, doble espai, `.SECTION`, `.DATA`, cometes).
- Les formes que **sí** que assemblen són pitjors, perquè fallen en silenci: **`.section` no commuta al segment equivocat, no commuta gens**, i l'assemblador es queda on ja era. Amb un nom reconegut (`.rodata`, `.sdata`) **descarta a més tot el codi que la segueix**, sense cap error ni avís: quatre instruccions queden en una al bolcat i el programa acaba «dropped off the bottom». **No es desen al segment equivocat: desapareixen** —el bolcat de `.data` del mateix programa diu «This segment has not been written to»—, cosa que descarta la hipòtesi natural que acabin com a dades. Contraintuïtivament, un nom **no** reconegut (`.section .foo`) és la forma segura, perquè avisa i conserva les instruccions.

L'experiment va impedir una conversió de 121 directives a la forma llarga que no hauria assemblat.

**On es presenta a teoria** (decisió de l'usuari del 2026-09-24, que el `TODO.md` d'aquell dia registra com a «ferma»; `5514d08`): la forma llarga es presenta com a forma de GNU al paràgraf «Forma llarga de la directiva», al **cos visible** de `#nte-segments-memoria` (A2, `@sec-programa-segments`), i no al `#wrn-segments-elf`, que és plegat (`collapse=true`), perquè `.section` es presenta amb els segments de memòria, on l'alumne aprèn què és una directiva de segment. `#wrn-segments-elf` es queda amb `.rodata` i `.bss`, i la fila `.section` de `21_riscv/RARS_directives.qmd` remet a `@sec-programa-segments`. **Invariant**: cap `.section` dins d'un bloc plegat d'`01_apunts/`. Es mesura per forma, no per línia: seguint la imbricació dels divs `:::` (una obertura amb atributs obre un nivell, marcat si porta `collapse`, i una tanca nua en tanca un) i comprovant que cap línia amb `.section` no és dins d'un nivell marcat. El 2026-10-09 n'hi havia tres, totes visibles: el paràgraf d'A2 i l'exemple il·lustratiu de l'RSE mínima d'A9 (dues línies). Fins al 2026-10-09, la decisió i l'invariant només constaven en una fila retirada del `TODO.md`, «`.section` a teoria com a forma de GNU» (`24_specs/arxiu_todo.md`), i al missatge de `5514d08` ([D-91](#d-91)).

### D-84

**Mode base + desplaçament: l'operand, sempre `desplaçament(base)`** · `13_contrib.qmd §T2 i T3` · 2026-10-09

Decisió de l'usuari (2026-10-09), després de la fase 8a, que va trobar que l'expansió de `ret` s'escrivia de dues maneres: `jalr x0, 0(ra)` a A1, A3 i la guia, i `jalr zero, ra, 0` a les taules de pseudoinstruccions del compendi (`TODO.md`, «Fase 8a: el que queda…»). RARS 1.6 admet totes dues formes i les codifica igual (`jalr zero, 0(ra)` i `jalr zero, ra, 0` donen `0x00008067`). La regla fixa la de les instruccions de lectura i escriptura, `desplaçament(base)`, també per a `jalr`, que és del mateix mode d'adreçament (A3, §Revisió dels modes d'adreçament), i el nom ABI del registre (`zero`, no `x0`), com la resta del codi del llibre. A2 la presenta a `#imp-notacio-base-desplacament`, just després de definir el mode.

### D-9

**Notació de la multiplicació i la divisió (T4)** · `13_contrib.qmd §T4` · 2026-10-03 · `e0ff377`

Fins al 2026-10-03 (fase 7 de `CLAUDE.md §Pla de treball`), la divisió tenia tres notacions a A4 —$x$/$y$/$q$/$r$, $D$/$d$/$q$/$r$ i $x$/$y$/$z$/$w$—, i $D$ era el dividend mentre que el registre D és el divisor.

### D-10

**«Esbiaixat» / «biaix» per a l'exponent IEEE 754** · `13_contrib.qmd §T1 i T5` · 2026-07-05 · `6d48f87`

Font: Viquipèdia cat., «Format de coma flotant de precisió simple».

### D-11

**«Mantissa», no «significand»** · `13_contrib.qmd §T1 i T5` · 2026-07-07 · `47704cf`

L'estàndard IEEE 754 en anglès prefereix formalment *significand* perquè *mantissa* ja té un significat establert en el context de logaritmes (Knuth en critica l'ús aquí per aquest motiu), però aquesta distinció és interna a l'anglès tècnic: **cap font normativa catalana la reflecteix**. Termcat (Cercaterm) només té fitxa per a «mantissa» (àmbit Matemàtiques, logaritmes); la Viquipèdia catalana, tant a «Format de coma flotant de precisió simple» com a «Format de coma flotant Bfloat16», usa «mantissa» com a terme principal («significand» hi apareix només com a manlleu anglès puntual, no com a alternativa establerta). A EC, l'ambigüitat que criticava Knuth ja queda resolta amb la distinció pròpia del projecte entre **fracció** ($F$, els bits emmagatzemats) i **mantissa** ($1{,}F$, amb el bit ocult). Es descarta, doncs, l'adopció de «significand».

### D-12

**Fracció, mantissa i precisió (T5)** · `13_contrib.qmd §T5` · 2026-10-03 · `e0ff377`

Fins al 2026-10-03, `A5.qmd §Representació binària` donava $p$ bits a la fracció, i §Notació científica normalitzada deia $n$ a l'exponent.

### D-81

**Els blocs `.default` i l'exemple *half* de §T5 són dels problemes i les solucions** · `13_contrib.qmd §T5` · 2026-10-09

Decisió de l'usuari (2026-10-09, fase 8a, decisió 8), a proposta de Claude Code. La revisió tècnica d'A5 de la fase 8a va preguntar si les dues regles obligaven també la teoria: A5 presenta els càlculs pas a pas IEEE 754 amb fórmules (`$$\begin{array}…$$`), no amb blocs `.default`, i l'exemple de no-associativitat d'A5 és de precisió simple. A5 no canvia; la guia ho diu.

### D-13

**Ordre dins de §Potència (T6)** · `13_contrib.qmd §T6` · 2026-10-01 · `666835c`

Anotació #12 de la revisió externa de T4–T6 (fase 3 de `CLAUDE.md §Pla de treball`).

### D-14

**Rendiment vs. productivitat (T6)** · `13_contrib.qmd §T6` · 2026-10-01 · `666835c`

Anotació #9 de la revisió externa de T4–T6 (fase 3 de `CLAUDE.md §Pla de treball`).

### D-15

**Guany, llei d'Amdahl i potència: la notació de la teoria a tot T6** · `13_contrib.qmd §T6` · 2026-10-03 · `ca98373`

Fins al 2026-10-03 (fase 7 de `CLAUDE.md §Pla de treball`), S6 feia servir $S$, $S_{max}$, $f$ i $k$ a la llei d'Amdahl —amb $f$ alhora fracció i freqüència dins del mateix fitxer—, $P_{din}$, $P_{est}$ i $P_{tot}$, i E6 i S6, $F_A$ i $F_B$ ($F$ és la fracció a T5).

### D-16

**Etiquetes de classe d'instruccions en català** · `13_contrib.qmd §T6` · 2026-10-03 · `9a292eb`

Decisió de l'usuari (2026-10-03). Fins llavors E6 i S6 les tenien en anglès («Load», «Store», «Load/Store», «L/S», «Branch»), també en 7 usos en prosa («les branch 2 cicles»).

### D-17

**Tipus de fallades: «d'arrencada en fred», i «obligatòria» als llocs curts** · `13_contrib.qmd §T7` · 2026-10-04 · `703af35`, `eb1838b`

Decisió de l'usuari (2026-10-04), amb els termes del PDF original (T6, §8). Fins llavors A7 deia *cold-start* com a terme principal. La resta del material (E7, S7, S8, L6 i `S_criteris_seleccio.qmd`) hi va passar el 2026-10-06, per recomanació de Claude Code acceptada per l'usuari.

### D-18

**Bits `E` i `V` de la memòria virtual** · `13_contrib.qmd §T8` · 2026-06-14 · `d926f24`, `ccae7dd`

Quan un enunciat heretat usava `W` (`1` = només lectura, polaritat oposada), s'ha reescrit a `E`, aplicant el criteri de precedència textual ([D-1](#d-1)). Els enunciats i les solucions que usaven `P` (notació x86 i dels exàmens antics d'EC) per al bit de presència s'han reescrit a `V`, aplicant el mateix criteri.

### D-19

**Model del TLB: el de RISC-V, no el de MIPS** · `13_contrib.qmd §T8` · 2026-10-05 · `fc356d7`

Decisió de l'usuari (2026-10-05), a la revisió externa de T8 (MR `!8`, Adrià Armejach), que va passar E8, S8 i A9 al model de RISC-V del TLB. Fins llavors el model era el de MIPS (TLB arquitectònic, *refill* per programari, encert de TLB amb V = 0), que es conserva com a nota històrica a `#wrn-mv-tlb-hw-walker`.

### D-82

**L'ordre d'ús de l'estat inicial del TLB, amb el sentit explícit** · `13_contrib.qmd §T8` · 2026-10-09

Decisió de l'usuari (2026-10-09, fase 8a, decisió 10), a proposta de Claude Code. Fins llavors la regla deia «l'ordre d'ús (MRU→LRU)», i l'exemple d'A8 dona l'ordre «de més antic a més recent», amb el sentit explícit, mentre que P8 el dona de la més recent a la més antiga. No hi ha ambigüitat si el sentit és explícit: la regla demana el sentit, no en fixa cap. A8 no canvia.

### D-20

**L'exemple pràctic de T8, a la secció final del tema** · `13_contrib.qmd §T8` · 2026-10-06 · `1ddd351`

Decisió de l'usuari (2026-10-06): a la secció final, com la secció 7 del PDF original.

### D-21

**Mode S a T9: la fallada de pàgina, no la de TLB** · `13_contrib.qmd §T9` · 2026-10-07 · `402ef7a`

Des del 2026-05-24 la regla deia: «el tractament de fallades de TLB per programari requereix mode S (`satp`, `stval`, `sfence.vma`). El cos del text descriu el mecanisme en mode M; l'aprofundiment cobreix mode S.» Era caducada per dues bandes: des del model de RISC-V del TLB ([D-19](#d-19), 2026-10-05), la fallada de TLB la resol el maquinari i no és una excepció (`A9.qmd`, `#cau-tlb-miss-excepcio`); i el mode S no és en cap aprofundiment, sinó al cos del text (`#sec-ei-tlb-modes`). Reformulada el 2026-10-07 (fase 7e), a proposta de Claude Code i acceptada per l'usuari.

## Problemes i solucions

### D-22

**Identificadors `#exr-t<N>-` i `#sol-t<N>-`** · `13_contrib.qmd §Problemes i solucions` · 2026-10-01 · `9dc02f6`, `1c9aae5`

Decisió de l'usuari (2026-10-01). Fins llavors el prefix era `p<N>-`, la numeració de les col·leccions MIPS, que en cinc temes no coincidia amb el tema (E2 i S2 feien servir `p3-`). Els enllaços externs a les àncores publicades amb el prefix antic van deixar de funcionar amb el canvi.

### D-23

**Etiqueta «Problema» o «Exercici» segons la part, i el «⁂» del PDF** · `13_contrib.qmd §Problemes i solucions` · 2026-10-01 · `229071c`

Decisió de l'usuari (2026-10-01). Al PDF, el mecanisme de «⁂» ve de dues formes més directes que es van provar i no funcionen: un bloc `crossref:` a la capçalera del fitxer substitueix la configuració de capítols que el llibre hi injecta (la numeració perd el capítol i les referències a capítols d'altres fitxers no resolen), i `\exercisename` escrit directament al prefix surt literal al PDF, perquè Quarto n'escapa la contrabarra. D'aquí el caràcter `⁂`, que no és a cap altre lloc del corpus. Com que una referència pren el nom de la part on és, una referència que creués parts diria el nom de la part d'origen; quan es va escriure, cap no ho feia.

### D-24

**«Problemes» i «Solucions»; «problema», i «exercici» només al laboratori** · `13_contrib.qmd §Problemes i solucions` · 2026-10-07

Decisió de l'usuari (2026-10-07, fase 7e), a proposta de Claude Code. Fins llavors no hi havia cap criteri, i el resultat era un ús inconsistent: «problemari» (la capçalera d'aquesta secció de la guia, `S5.qmd` i `S_criteris_seleccio.qmd`), «solucionari» (la guia, a §T5), «enunciats» (`_variables.yml`: «Problemes — Enunciats», sense cap ús) i «exercicis» per a problemes (`index.qmd`, E2, S2, S5, S6 i les capçaleres de `S_criteris_seleccio.qmd`). Motius:

- «Problemari» no és al DIEC2, al Termcat ni a l'Optimot.
- «Solucionari» és al Termcat, però el menú del llibre (`_quarto.yml`) ja diu «Problemes» i «Solucions», que són les formes més usades a l'HTML.
- Als exàmens es fa servir «Problema 1», «Problema 2»…, i l'etiqueta visible ja era «Problema» a les parts de problemes i «Exercici» al laboratori ([D-23](#d-23)).

Aplicada en el mateix commit a les dues ocurrències de «problemari» del corpus; els usos d'«exercici» per a un problema, a una entrada del `TODO.md`. El títol bibliogràfic «Solucionari de la Col·lecció de Problemes» de `14_LICENSE.qmd` és el d'una obra i no es toca.

### D-73

**Selecció de solucions, sense taula de criteris** · `13_contrib.qmd §Problemes i solucions` · 2026-10-08

Decisió de l'usuari (2026-10-08, fase 7g), a proposta de Claude Code: es retira `03_solucions/S_criteris_seleccio.qmd`, i el criteri passa a la guia. El fitxer era una taula, per tema, dels problemes resolts amb la dificultat i el temari, comentada a `_quarto.yml`; `index.qmd` hi remetia amb deu enllaços que, per això, no portaven enlloc (ara remeten a les solucions de cada tema). L'auditoria de la fase 7g hi va trobar 10 solucions que no hi eren (T2 2 i T4 8), cinc descripcions que no corresponien a l'enunciat i la solució, i un criteri («~1 resolt per cada 2–3») que no es complia (188 problemes, 108 solucions, 1:1,74). Mantenir-la al dia era una feina sense lector. L'escala de dificultat (1 a 5) no es conserva: cap altre fitxer no la feia servir. El fitxer es recupera amb `git show 210e6de:03_solucions/S_criteris_seleccio.qmd`.

### D-75

**Directori `02_problemes/` i fitxers `P1.qmd`–`P9.qmd`** · `README.md §Estructura del projecte` · 2026-10-08

Decisió de l'usuari (2026-10-08, fase 7g), com a part de l'harmonització de [D-24](#d-24): el directori es deia `02_exercicis/` i els fitxers, `E1.qmd`–`E9.qmd`, l'únic lloc on «exercici» encara designava els problemes. Les entrades d'aquest registre i del `TODO.md` anteriors al canvi els citen amb el nom d'abans, que és el de l'historial (`git log --follow -- 02_problemes/P1.qmd`). Les URL publicades de les pàgines de problemes canvien amb el nom (`02_exercicis/E1.html` → `02_problemes/P1.html`), com van canviar les àncores amb [D-22](#d-22).

## Laboratori

### D-25

**El punt d'entrada no porta etiqueta** · `13_contrib.qmd §Convencions globals del laboratori` · 2026-09-24 · `b2c1a4f`

Criteri de l'usuari (2026-09-23), que **inverteix** la convenció anterior, que exigia `_start` i `.globl _start`.

**Motiu, i no és de coherència interna.** A EC es programa directament sobre el processador (`@imp-directe-sobre-processador`), en un **entorn autònom** (*freestanding*, `@sec-entorn-autonom-bare-metal`): l'execució comença a la primera instrucció de `.text` i **cap agent no llegeix el nom del punt d'entrada**. A Linux, en canvi, `_start` és el símbol que l'enllaçador i el carregador resolen —hi té un consumidor—. És el mateix argument que justifica `void main()` ([D-49](#d-49)): en un entorn autònom **la forma i el nom del punt d'entrada són definits per la implementació**, i una etiqueta que ningú no resol és la mateixa ficció que un `return` que ningú no recull. Un nom qualsevol reintroduiria la idea que el punt d'entrada en té.

⚠️ **L'excepció de RARS no afecta l'argument, i per això el text ho ha de dir.** `@imp-directe-sobre-processador` declara RARS «una excepció important» a l'assumpció *bare-metal* perquè simula syscalls; l'excepció és sobre els **serveis que el programa crida**, no sobre **qui crida el programa**. Al punt d'entrada no hi intervé res.

**La segona raó: l'opció «start at main» (`sm`) només actua amb un `main` declarat global.** L'ajuda de RARS 1.6 diu literalment «*start execution at statement with global label main, if defined*»: **global** hi és determinant. Una etiqueta `main:` sense `.globl main` **no fa res** —l'execució comença igualment a la primera instrucció—, de manera que amb `.globl main` el mateix fitxer s'executaria de dues maneres segons una casella que cada alumne té activada o no: una divergència silenciosa entre dos alumnes amb el mateix codi. I no és una raó de disciplina sinó d'**impossibilitat**: sense cap etiqueta global, `sm` no té on agafar-se i les dues posicions de la casella donen el mateix resultat. La divergència no s'evita confiant que ningú no l'activi —**s'elimina**—, que és el que decideix en material que faran servir dotzenes d'alumnes amb configuracions diferents. Verificat amb RARS 1.6 (2026-09-24) mesurant l'estat final dels registres, no l'absència d'error:

```bash
# prova.s:  li t0,111  /  main:  li t1,222  /  li a7,93  /  li a0,0  /  ecall
java -jar rars1_6.jar nc    prova.s t0 t1   # t0=0x6f: comença a la 1a instrucció
java -jar rars1_6.jar nc sm prova.s t0 t1   # t0=0x6f: sense .globl main, `sm` no fa res
# el mateix fitxer amb `.globl main` afegit:
java -jar rars1_6.jar nc sm prova.s t0 t1   # t0=0x00: només aquí comença a `main`
```

📌 **`_start` no hi rebia cap tracte especial**: amb `.globl _start` i l'etiqueta en segona posició, l'execució començava igualment a la primera instrucció, amb `sm` i sense. **La convenció que s'inverteix no descansava, doncs, en cap comportament del simulador**: era convenció pura. Això fa la inversió menys arriscada del que sembla —no hi ha cap automatisme de RARS que depengui del nom— i explica alhora per què ningú no se n'havia adonat: una etiqueta inert no falla mai, i per això es pot mantenir anys sense que res la contradigui.

**Invariant.** Als `.qmd`, sense el `TODO.md` ni `13_contrib.qmd`: `_start` surt **3** vegades, totes a la prosa del callout `@nte-punt-entrada-etiqueta` d'A3; **0** definicions `_start:`; **5** línies `.globl`, totes d'un símbol que es fa servir des d'un altre fitxer o mòdul (`suma`, `abs`, `descompon`, `g` i `X`); i **0** `.globl _start`. Són quatre formes diferents —ocurrències, definicions, línies `.globl` de qualsevol símbol i línies `.globl _start`—, que l'entrada del `TODO.md` va confondre dues vegades. ⚠️ Fins al 2026-10-09 l'invariant deia **6** línies `.globl`, «que s'han de mantenir»: `40bd0d6` (fase 7g, bloc 3b, 2026-10-08) va treure `.globl compon` de `s5_3_1.s`, i el missatge del commit no ho diu. És correcte: `compon` es defineix i es crida al mateix fitxer, i L5 només demana `.globl` per a una etiqueta que es fa servir des d'un altre fitxer (§Compilació separada). Es va donar per bo el 2026-10-09, en passar l'invariant aquí, a proposta de Claude Code (l'usuari: «Endavant»). Fins llavors l'invariant només constava en una fila retirada del `TODO.md`, «`_start` surt del codi i només es presenta a teoria» (`24_specs/arxiu_todo.md`), on ningú no va veure que deixava de complir-se ([D-91](#d-91)).

```bash
X=("--" "*.qmd" ":!TODO.md" ":!13_contrib.qmd")
git grep -o "_start" "${X[@]}" | wc -l                    # 3 (2026-10-09)
git grep -hE "^_start:" "${X[@]}" | wc -l                 # 0
git grep -hE "^\s*\.globl" "${X[@]}"                      # 5: suma, abs, descompon, g i X
git grep -hE "^\s*\.globl\s+_start" "${X[@]}" | wc -l     # 0
```

**L'ordre de la pestanya de RARS, avaluable** (decisió de l'usuari, 2026-09-24). El fet general —RARS comença a la primera instrucció de `.text`, el punt d'entrada no porta etiqueta i el programa principal va abans de les subrutines— és al cos visible de `#nte-segments-memoria` (A2), amb una línia a `@nte-programa-esquelet` que hi remet (`5514d08`). El que és propi de L5 —l'ordre de la pestanya activa en assemblar diversos fitxers, i el diagnòstic— és a `@nte-rars-ordre-assemblatge`, que va passar de `#wrn-` (aprofundiment, no avaluable, plegat) a `#nte-rars-` (avaluable, visible) (`d6fb588`): el canvi d'avaluabilitat és volgut, perquè l'ordre de la pestanya és al camí normal de l'exercici i, si és la dolenta, el programa no arrenca. La proposta original, un `#nte-` a L1, es va descartar: `@nte-programa-esquelet` ja és la lectura prèvia obligatòria de L1. Fins al 2026-10-09 només constava en una fila retirada del `TODO.md`, «Punt d'entrada de RARS: cap material no l'explicava a l'alumne» (`24_specs/arxiu_todo.md`).

### D-26

**Tres blocs del laboratori sense punt d'entrada** · `13_contrib.qmd §Convencions globals del laboratori` · 2026-09-24 · `b2c1a4f`

L'exempció ja constava quan la convenció exigia `_start`; el criteri nou ([D-25](#d-25)) en deixa caduc el motiu —ja no hi ha etiqueta que els falti—, però **la particularitat dels tres blocs es manté i cal conservar-la**.

### D-27

**Oracle a l'enunciat, tècnica a la solució** · `13_contrib.qmd §Convencions globals del laboratori` · 2026-09-21 · `cf2dd43`

- L'oracle va a l'enunciat perquè l'estudi previ es lliura **abans** de la sessió i hi haurà una versió del llibre sense solucions: un oracle dins d'un `{#sol-...}` és inabastable justament quan fa falta.
- La fixació d'una entrada va amb el resultat perquè un valor sense la seva precondició no és reproduïble.
- El callout de la tècnica se suprimeix si no té contingut propi perquè un callout que només existeix per no deixar el lloc buit és soroll.

### D-28

**`### Lliuraments` i `### Lectura prèvia`, de nivell 3** · `13_contrib.qmd §Ordre i atribut de seccions no numerades` · 2026-07-13 · `fe53cfc`

És un *dirty hack* per evitar que la capçalera de pàgina del PDF quedi fixada a «Lectura prèvia», efecte que sí que es produeix amb el nivell 2.

## Llenguatge

### D-29

**Fonts de correcció lèxica: DIEC2, Termcat i Optimot, per aquest ordre** · `13_contrib.qmd §Referència normativa` · 2026-10-07

Decisió de l'usuari (2026-10-07, fase 7e): «afegeix l'Optimot i el DIEC2 com a fonts de correcció lèxica. […] Ordre jeràrquic: DIEC2, Termcat, Optimot». Fins llavors la guia deia «La norma general és l'**IEC** (Institut d'Estudis Catalans): DIEC2 i Optimot», sense cap ordre i sense el Termcat, que era la font de les decisions terminològiques de la taula de substitucions (ròssec, farciment, multinucli, amplada de banda).

### D-86

**Prefixos decimals: fora l'excepció de les referències de mercat d'A7** · `13_contrib.qmd §Criteris generals` · 2026-10-09

A proposta de la revisió tècnica d'A7 de la fase 8a, aplicada amb el permís de l'usuari del 2026-10-09 («Fer tots els canvis que creguis oportuns»). La regla reservava els prefixos decimals (KB, GB…) també per a «les referències de mercat aproximades» de `#sec-gap-memoria`, però dins d'aquesta secció només hi ha amplades de banda, que ja eren a la regla, i «80 GiB», que és binari; les capacitats en GB i TB són a §Tecnologies, i les cobreix l'emmagatzematge secundari. L'excepció no cobria res.

### D-87

**Unitats i percentatges: un espai que no es parteix** · `13_contrib.qmd §Criteris generals` · 2026-10-09

Decisió de l'usuari (2026-10-09, després de la fase 8a): «Recomanació acceptada, regla nova. També s'aplica a totes les unitats de mesura». La lectura lingüística d'A6 va trobar que el corpus escrivia el % enganxat al nombre («80%») i l'Optimot hi demana un espai; a la mesura del 2026-10-09 n'hi havia 142 i cap amb espai, i les unitats ja portaven espai («32 bits»). L'escombrada va posar l'espai a 99 percentatges de la prosa i les fórmules (els altres eren atributs d'amplada, `width: 80%`, que no es toquen). Perquè l'espai no es parteixi sense omplir el font de marques, el posa un filtre del render (`espai_unitats.lua`), amb la llista d'unitats.

### D-88

**Terme català o anglès: l'Optimot i Softcatalà, i les excepcions documentades** · `13_contrib.qmd §Anglicismes i terminologia obligatòria`; les excepcions, a la segona taula de `12_sigles_simbols.qmd §Termes` (des del 2026-10-09, D-100) · 2026-10-09

Decisió de l'usuari (2026-10-09, en respondre els dubtes de la lectura lingüística d'A1–A8), literal: «Si un terme no és a l'Optimot ni al diccionari Anglès-Català de Softcatalà, es fa servir el terme anglès. S'admeten accepcions quan el terme català és poc usat, per exemple "heap-monticle", aquests casos s'han de documentar explícitament.» Primers casos, del mateix dia: *host* → «amfitrió» (A1, A3 i la figura de la Pico 2); *target*, en anglès (no és a l'Optimot); *heap*, en anglès (l'Optimot dona *monticle*, que l'usuari troba massa lluny de l'ús, i Claude Code hi coincideix: el terme del Termcat és de l'estructura de dades); i *caller*/*callee*, «la funció que crida» i «la funció cridada» al text, i en anglès a les figures, per l'espai. L'usuari va demanar que se'n faci una revisió completa (`TODO.md`).

### D-30

**Amplada dels hexadecimals** · `13_contrib.qmd §Criteris generals` · 2026-10-01 · `7d78615`, `171cf18`

Decisió de l'usuari (2026-10-01). L'excepció del format reduït té dos casos, `exr-t7-fallades-programa` i `exr-t8-mv-proteccio`: l'usuari va declarar (2026-10-01) que el format hi és correcte i que s'explicita amb la nota. Fins al 2026-10-07 les tres regles dels hexadecimals (majúscules, amplada i separadors) eren a dos llocs de la guia.

**A les figures** (`24_specs/svg.md §9`), les adreces segueixen la mateixa regla. Fins a la fase 7c, `svg.md` hi deia «espai cada 4 dígits», contra el text; decisió de l'usuari 10 de la fase 7c (2026-10-03), aplicada el 2026-10-05 a les tres figures que en portaven, `A3_mapa_memoria`, `A7_mc_encert` i `A7_mc_fallada` (`06f0c0c`) (fins al 2026-10-09, a `24_specs/svg.md`).

### D-31

**Ordre substantiu–adjectiu** · `13_contrib.qmd §Criteris generals` · 2026-10-01 · `681556a`, `d50b0ba`

Decisió de l'usuari (2026-10-01). Aplicada a tot el corpus el 2026-10-01: el material de T5 (teoria, problemes, solucions, laboratori i figures), després de fusionar `temes456`.

### D-72

**Adjectius qualificatius, preferentment darrere del nom** · `13_contrib.qmd §Criteris generals` · 2026-10-08

Decisió de l'usuari (2026-10-08, fase 7g): «Per aquests casos la preferència és l'adjectiu després del substantiu, per tant, «una creixent importància» → «una importància creixent»». El revisor lingüístic havia marcat el cas de S6 com a error contra D-31, i Claude Code el va rebaixar a qüestió d'estil, perquè «creixent» és qualificatiu i D-31 només parlava dels classificadors; l'usuari en fixa la preferència. Les excepcions de D-31 (ordinals, quantificadors, «mateix», «propi», «altre», valoratius idiomàtics) continuen valent.

### D-32

**«No» davant d'un nom, amb guionet** · `13_contrib.qmd §Criteris generals` · 2026-10-01 · `bb12c2b`

Decisió de l'usuari (2026-10-01), que confirma la forma que el corpus ja feia servir.

### D-33

**Veu: impersonal, 2a del singular als exemples i 2a del plural als enunciats** · `13_contrib.qmd §Criteris generals` · 2026-07-12 · `31f7571`, `ccae7dd`, `87ecbcb`

- La 2a persona del singular dels `{.callout-tip}` és el criteri revisat el 2026-07 a la revisió interna de T2 (xat A2-E2-S2).
- El «nosaltres» expositiu dels exemples narrats és pràctica consolidada a T7 i T8, revisada el 2026-07 a la revisió interna de T8 (xat A8-E8-S8).
- La 2a persona del plural dels enunciats s'aplica a `E1.qmd`–`E9.qmd` des del 2026-10-01; fins llavors només E4 i E6 la seguien. Les solucions no hi entren: són a `.callout-tip`.

Fins al 2026-10-07 la veu dels enunciats era a §Problemari i solucionari, i la taula de callouts la tornava a dir.

### D-34

**«Imbricat», no «aniuat»** · `13_contrib.qmd §Formes que no s'han de fer servir` (fins al 2026-10-09, §Substitucions obligatòries) · 2026-10-04 · `552ff1a`

Decisió de l'usuari (2026-10-04). «Aniuat», que la taula donava fins llavors com a substitució d'«anidat», no és el terme informàtic en català.

### D-35

**«Lectura/escriptura» per *load/store*** · `12_sigles_simbols.qmd §Termes` (el glossari, des del 2026-10-09; D-100) · 2026-10-07 · `9f8e746`

Aplicat a tot el corpus el 2026-10-07 (decisió de l'usuari): fins llavors A2 presentava *load* i *store* com a «càrrega» i «emmagatzematge»/«emmagatzemament».

### D-36

**«Ròssec», «semisumador» i «sumador complet»** · `12_sigles_simbols.qmd §Termes` (el glossari, des del 2026-10-09; D-100) · 2026-10-03 · `e49c014`

«Ròssec» és el terme del Termcat (decisió de l'usuari, 2026-10-03), i substitueix «arrossegament», que el corpus usava fins aleshores. «Semisumador» i «sumador complet» són de la mateixa sessió (fase 5); l'usuari no els va poder trobar a la interfície nova del Termcat, i els va confirmar el 2026-10-09 (literal: «Confirmat»).

### D-37

**«Coma flotant», no «punt flotant»** · `13_contrib.qmd §Formes que no s'han de fer servir` (fins al 2026-10-09, §Substitucions obligatòries) · 2026-10-01 · `c1bac38`

És el terme del corpus: 113 ocurrències contra 4, totes a `A2.qmd`, unificades el 2026-10-01.

### D-38

**«Farciment» i «multinucli»** · `12_sigles_simbols.qmd §Termes` (el glossari, des del 2026-10-09; D-100) · 2026-10-07 · `ca6c01a`, `4625835`

*Padding* → «farciment» és a la taula des del 2026-07-21. *Multicore* → «multinucli» és decisió de l'usuari (2026-10-07), amb el Termcat com a referència.

### D-39

**«Enter» i «natural»** · `13_contrib.qmd §Anglicismes i terminologia obligatòria` · 2026-10-02 · `ee78460`

Proposta de la revisió externa de T3 (`A3.qmd:121`, a `ab48732`) i decisió de l'usuari (2026-10-02), amb l'escombrada del corpus feta el mateix dia.

### D-40

**VPN i PPN, a la taula de sigles** · `13_contrib.qmd §Sigles, símbols i notació` · 2026-10-03 · `8e19383`

Decisió de l'usuari (2026-10-03). Fins llavors el criteri d'exclusió les posava d'exemple de nom de camp exclòs, i la taula les incloïa.

### D-79

**Les sigles, sense plural** · `13_contrib.qmd §Sigles, símbols i notació` · 2026-10-09

Decisió de l'usuari (2026-10-09, fase 8a: «regles noves acceptades»), a proposta de Claude Code. S'aplicava des de la fase 7g (A9: «SOs», «PTEs»), però no era escrita. La fase 8a en va trobar cinc a A1–A8 («APIs», «ISAs», «LEDs», «GPUs» ×2), que es van corregir en el mateix commit que la regla. És el criteri de l'Optimot: la sigla és invariable, i el nombre el diu el determinant.

### D-80

**L'article i la preposició davant de les sigles, segons la pronúncia (GIEC)** · `13_contrib.qmd §Sigles, símbols i notació` · 2026-10-09

Decisió de l'usuari (2026-10-09, fase 8a, decisió 6: «el de la GIEC («l'ISA», «l'MMU», «l'LSB»…)»; l'abast, «a tot el corpus», en respondre una pregunta de Claude Code el mateix dia). Fins llavors el corpus barrejava les formes («la ISA» i «l'ISA»), i «la MMU», «la MC», «la MP», «la RSE» i «el SO» anaven sense apostrofar. L'escombrada del 2026-10-09 les va canviar a tot el corpus, figures i generadors inclosos (les sigles en negreta, «la **ISA**», en una segona passada, al tancament de la fase 8a); als generadors, amb l'apòstrof tipogràfic de la resta dels seus rètols. Es van deixar fora els originals conservats que el llibre no consumeix ([D-68](#d-68)), que esmena l'editor, i els marcadors d'`index.qmd`. Les sigles que es llegeixen com un mot que comença en consonant no s'apostrofen («la RAM», «de RARS»).

Ampliació (decisió de l'usuari, 2026-10-09, en revisar el tancament de la fase 8a): «d'RV32I» i «d'RV32F», que es lletregen («erra-ve»); «d'UNIX», com dona el Termcat a l'Optimot; i «d'NVIDIA», pel mateix criteri que UNIX. «La IA» es manté, que és la forma de l'Optimot.

Segona ampliació (decisió de l'usuari, 2026-10-09: «Sí, s'estén al codi»): el mateix criteri val davant d'un identificador de codi. El corpus feia les dues coses (40 «de» davant de codi que comença en vocal, contra 23 «d'»). Criteri de Claude Code, que la decisió no detallava: el codi es llegeix com un mot, de manera que s'apostrofa davant de vocal («d'`addi`», «l'`a0`», «d'`if-then-else`») i no davant de consonant («de `lw`», «la `sp`»), encara que el registre es pogués lletrejar («essa-pe»). L'escombrada en va canviar 44.

### D-89

**Les sigles s'expandeixen només a la primera aparició del llibre** · `13_contrib.qmd §Sigles, símbols i notació` · 2026-10-09

Decisió de l'usuari (2026-10-09, després de la fase 8a), literal: «L'expansió de les sigles només es fa a la primera aparició. Justificació: hi ha un compendi de sigles.» Era el criteri pendent de la fase 7i («sigles sense expandir a la primera aparició del fitxer»), i un inventari per capítol en va trobar unes 94 sense expandir a A1–A8 (`TODO.md`, entrada retirada). Fins llavors, la regla deia «la primera vegada» sense dir si era del llibre o del fitxer, i §T6 demanava expandir CMOS i CF a cada fitxer. Amb la regla nova, l'escombrada del 2026-10-09 (en l'ordre dels `chapters:` de `_quarto.yml`) va trobar 34 primeres aparicions sense expandir, i se'n van expandir 24; la resta eren títols amb l'expansió a la primera frase del cos, una taula amb l'expansió al paràgraf següent o el nom d'una altra expansió. Les expansions que ja hi havia en capítols posteriors no es treuen.

### D-41

**`\texttt{…}`, no `\mathtt{…}`** · `13_contrib.qmd §Codi, matemàtiques i cursiva` · 2026-10-03 · `d61a848`

El corpus feia servir `\mathtt{…}` 44 vegades (S1, S4 i A1) fins al 2026-10-03, i es va unificar a `\texttt{…}` a la fase 7 de `CLAUDE.md §Pla de treball`.

### D-42

**Subíndexs en cursiva també quan són sigles, i l'excepció de les taules ISA** · `13_contrib.qmd §Codi, matemàtiques i cursiva` · 2026-10-03 · `477b9ca`

Totes dues són decisions de l'usuari (2026-10-03, fase 7 de `CLAUDE.md §Pla de treball`) que escriuen l'ús del corpus. A les taules ISA, escriure $PC$ amb `\text{…}` el separaria tipogràficament dels altres operands de la mateixa fórmula.

### D-43

**Operacions lògiques (AND, OR, XOR, NOT)** · `13_contrib.qmd §Codi, matemàtiques i cursiva` · 2026-10-01 · `c4c247a`

Decisió de l'usuari (2026-10-01), que escriu l'ús que el corpus ja feia majoritàriament i n'hi alinea les desviacions.

### D-100

**El glossari de termes és l'única font del lèxic anglès–català** · `13_contrib.qmd §Anglicismes i terminologia obligatòria`, `12_sigles_simbols.qmd §Termes`, `24_specs/glossari.toml` · 2026-10-09

Decisió de l'usuari (2026-10-09), literal: «Decsisió ferma, la del glosari. Substitueix la llista de `13_contib.qmp` per una remissió al glossari i l'obligació d'emprar el lèxic del glosssari o ampliar-lo»; i sobre els termes que es mantenen en anglès: «Com que l'entrada és per l'anglès, penso que és el lloc adequat per llistar els termes anglesos que hem fet servir en anglès perquè el terme català no existeix o és molt poc usat. Si es fa, caldrà afegir l'explicació al text d'introducció de la taula de del glossari. Si ho creus convenient, fes-ho.» Fins llavors, el lèxic anglès–català era a dos llocs: la taula de §Substitucions obligatòries de la guia (34 formes, de les quals 13 també eren al glossari, sense contradiccions) i el glossari, que surt del text. La guia diu ara que el lèxic és el del glossari, i que un terme nou s'hi afegeix presentant-lo al text. Les decisions de detall, propostes de Claude Code que l'usuari va acceptar totes («Endavant i opció (a)»): (1) els termes de la taula de la guia que el text feia servir però no presentava en negreta, i que per això el glossari no tenia, s'hi presenten a la primera aparició (*cache*, *branches*, *jumps*, *floating point*, *carry-in*, *carry-out*, *ripple carry*, *bandwidth*, *event* i *embedded systems*: de 108 a 117 termes); (2) les observacions d'ús de la taula (l'abast de lectura/escriptura, «biaix» i no «excés», *multinucli* invariable, el símbol `PAD`…) passen a una columna del glossari, i les genèriques («Terme preferent», «Primera aparició en un fitxer…») se'n van; (3) les formes que no són angleses (*fallo*, *aniuat*, *tamany*, «punt flotant»…) es queden a la guia, a §Formes que no s'han de fer servir, perquè no poden anar a un glossari anglès–català; (4) els termes que es mantenen en anglès (D-88) passen a una segona taula del glossari; (5) *target* es manté en anglès, com deia D-88: A1 el presentava com «**Màquina destí** (***target***)», i el glossari en deia «màquina destí», en contradicció amb la regla; (6) la negreta d'*underflow* cobreix només «subdesbordament». El que no surt del text (les observacions i la segona taula) és a `24_specs/glossari.toml`, i `gen_glossari.py` ho escriu entre els marcadors; `--comprova` avisa d'una observació d'un terme que el glossari ja no té. La regla de mantenir els identificadors quan canvia un terme ([D-35](#d-35)) passa a ser general. L'agent `revisor-linguistic` revisa contra el glossari.

**Seguiment del 2026-10-10** (decisions de l'usuari sobre les presentacions dubtoses del glossari, `e1a0f67`, i les recomanacions de Claude Code que va acceptar, «endavant»). (1) El generador deixa fora les presentacions en què l'anglès és l'expansió d'una sigla que ja és a §Sigles: «**NaN** (*Not a Number*)» i «**codi ASCII** (*American Standard Code for Information Interchange*)» tenen la forma d'una presentació de terme, però no són traduccions, i sortien a §Sigles i a §Termes. (2) *pipeline* es manté en anglès, a la taula de termes mantinguts en anglès, pel segon supòsit de [D-88](#d-88): el Termcat (Neoloteca, termes normalitzats pel Consell Supervisor, Informàtica > Estructura de les dades) dona *pipeline* → «canal» i *pipelining* → «canalització», amb l'anglès com a sinònim complementari, i «canonada» només en àrees que no són d'informàtica; «canal» és molt poc usat en arquitectura de computadors i es confon amb un canal de comunicació. Només surt a l'aprofundiment `#wrn-flux-pipeline` d'A9, que ara explica què és un *pipeline*. (3) Les cinc taules del capítol (Sigles, Símbols, Notació, Termes i Termes mantinguts en anglès) porten peu curt, etiqueta `#tbl-` i la classe `.striped`, i la de Sigles, capçalera i un paràgraf d'introducció (petició de l'usuari: «Aquestes taules també s'han de normalitzar (caption, label, colswidth, etc.) i optimitzar l'amplada de les columnes»). El paràgraf de presentació de cada subsecció es queda com a text i no passa al peu: a l'HTML el peu surt en lletra petita i grisa, i al PDF, darrere de «Taula N.:», i els paràgrafs fixen convencions de lectura de la taula.

### D-106

**Sis formes més a la taula de formes que no s'han de fer servir: «comanda», «solapar», «encuar», «descomposar», «rotar» i «indentar»** · `13_contrib.qmd §Formes que no s'han de fer servir` · 2026-10-10

Decisió de l'usuari (2026-10-10, fase 12), literal: «Sí», a la proposta de Claude Code d'afegir-hi indentar → sagnar, solapar → superposar, encuar → posar a la cua, comanda → ordre, descomposar → descompondre i rotar → girar, amb la seva entrada al registre; i «Valora com s'haurà de mantenir aquesta taula (manualment?, amb un script?)». Les va trobar la passada de `hunspell` i LanguageTool sobre la prosa (l'entrada «Fase 12» del `TODO.md`, `0ddb36a`). Cap no és al DIEC amb el sentit del text: «comanda» hi és un encàrrec comercial, i «rotar», fer rots; «descomposar», «encuar» i «solapar» no hi són (consultat el 2026-10-10, també a l'Optimot, que només té «solapar» com a entrada castellana). Les formes bones són les del Termcat («ordre» i «línia d'ordres»; «posar a la cua») o les del DIEC («superposar», «descompondre», «girar»).

- **«indentar» hi entra el mateix dia, al vespre, amb «sagnat»** per a *indentation* (decisió de l'usuari, literal: «Recomanació acceptada. "sagnat"», a la proposta de Claude Code): el DIEC defineix «sagnia» remetent a «sagnat», i el Termcat diu «sagnat». Fins llavors esperava la tria entre «sagnat» i «sagnia», que és la que deia el missatge de `2a3d595`, en què l'usuari va treure «indenta» i «indentació» del diccionari de VS Code.
- **Les files entren amb el corpus ja corregit**: des de [D-105](#d-105), `lint_prosa.py` llegeix la taula i atura el commit amb les formes que hi són.
- **De «descomposar» i de «rotar» hi van les formes conjugades, no l'infinitiu**: `lint_prosa.py` llegeix un verb en *-ar* com l'arrel seguida de qualsevol terminació, i «descomposició» i «rotació», que són correctes, també hi entrarien.
- **«solapar»** es diu de dues maneres segons el sentit: «superposar-se» a l'espai (dues meitats d'un registre, dos camps de bits) i «fer-se alhora» o «coincidir» en el temps (dos renders, dues operacions).

### D-107

**Noms de persona: com els escriu la Viquipèdia, i si no, la Wikipedia en anglès** · `13_contrib.qmd §Referència normativa` · 2026-10-10

Decisió de l'usuari (2026-10-10, fase 12), literal: «von Neumann», i «Regla general (afegeix-la o toqui): Per a noms de persones la font de veritat, per ordre de preferència, és la Wikipedia catalana i la Wikipedia anglesa.» El cas: el corpus deia «Von Neumann» vuit vegades (A1, A2 i P5, i el títol de la figura `A1_von_neumann.svg`) i «John von Neumann» una (A1). La Viquipèdia en diu «John von Neumann» i «Arquitectura de von Neumann» (consultat el 2026-10-10). Les fonts de correcció lèxica de [D-29](#d-29) (el DIEC2, el Termcat i l'Optimot) no cobreixen els noms de persona.

## Format

### D-70

**Punter cap endavant T3 → T6: temps d'execució i CPI** · `13_contrib.qmd §Referències creuades` · 2026-10-08

Decisió de l'usuari (2026-10-08, fase 7g, decisió 8), a proposta de Claude Code. Dos problemes de T3, `exr-t3-bucles-for` (apartats c i d) i `exr-t3-bucles-multiplicacio` (apartats d i e), demanen temps d'execució i CPI, que la teoria presenta a T6 (`@eq-texe2`); a A1–A3 i E1–E2 no hi ha cap ocurrència de «CPI» (mesurat a `7a1640e`). Venen de l'original de MIPS, on el rendiment era a T1. L'alternativa, treure o moure aquells apartats, es va descartar: la dependència és de càlcul, amb la fórmula citada a la solució (S3), i es pot seguir com a punter explícit.

### D-78

**Els punters cap endavant de la fase 8a, inscrits a la llista** · `13_contrib.qmd §Referències creuades` · 2026-10-09

Decisió de l'usuari (2026-10-09, fase 8a: «regles noves acceptades»), a proposta de Claude Code. La revisió tècnica d'A1–A8 de la fase 8a va trobar onze punters cap endavant que no eren a la llista: d'A1, cap a T3 (el *heap*), T4 (l'extensió M) i T5 (l'exponent en excés); d'A2, cap a T3 (els formats B i J, l'expansió de `la`, els salts, els desplaçaments i les instruccions lògiques) i cap a T9 (les pseudoinstruccions dels CSR). Tots eren explícits, i el text s'entén sense seguir-los: es van inscriure a la llista sense tocar el text, i A1:779 («Tema 4», sense enllaç) va passar a enllaçar-hi. En aplicar les correccions de la mateixa fase n'hi van entrar tres més, des d'A1: `ecall` (T9), les pseudoinstruccions i els salts indirectes (T2/T3) i `@wrn-mul-modul-2n` (T4).

### D-44

**Una remissió `@fig-` a cada figura del cos del text** · `13_contrib.qmd §Referències creuades` · 2026-10-03 · `e806916`

Decisió de l'usuari 8 de la fase 7c (2026-10-03), aplicada el 2026-10-06 a les 25 figures que no en tenien. Fins al 2026-10-09 la regla era a tres llocs de la guia: la fila «Figura» de la taula de §Callouts i dues vinyetes de §Referències creuades; en esporgar la guia, es va deixar en una.

Fins al 2026-10-07, §Referències creuades deia també «Figures i Taules: no han d'estar necessàriament referenciades al text», que la contradeia per a les figures des del 2026-10-03. Decisió de l'usuari (2026-10-07, fase 7e): «Figures sempre, taules opcional».

### D-45

**El títol dels blocs de pseudocodi** · `13_contrib.qmd §Blocs de codi` · 2026-10-01 · `f066a8e`

Decisió de l'usuari (2026-10-01), a partir de l'anotació #4 de la revisió externa de T4. Que «—» surt com a `---` al PDF es va verificar a `make render-complet` el 2026-10-01.

### D-46

**Algorismes en rodona** · `13_contrib.qmd §Blocs de codi` · 2026-10-02 · `f066a8e`

La mateixa decisió que [D-45](#d-45) (anotació #4). Al PDF, la cursiva venia de l'estil *plain* del `\newtheorem` que genera Quarto, i `preamble.tex` la treu redefinint aquest estil (2026-10-02; `24_specs/arxiu_todo.md` §Entrades retirades, «Anotacions de la revisió externa de T4–T6»).

### D-47

**Ressaltat propi dels blocs `.s`** · `13_contrib.qmd §Blocs de codi` · 2026-10-07 · `f508b0f`

Feta des de zero el 2026-10-07 (decisió de l'usuari): fins llavors Pandoc feia servir `gnuassembler`, que no ressaltava `.eqv` ni `.end_macro` (de RARS) i donava el mateix color a instruccions i registres; partir de la d'x86 volia dir canviar-ne totes les llistes. El 2026-10-07 cobria tots els mnemònics i directives dels blocs `.s` del corpus.

### D-48

**La marca `codi_erroni`** · `13_contrib.qmd §Blocs de codi` · 2026-10-06 · `0d33d13`, `9f8e746`

La marca exclou el bloc de les eines **per forma**, en lloc d'una llista de línies que caduca. Sense la marca, el contraexemple de `@nte-rars-noms-reservats`, amb un `.eqv B, 16` escrit a posta, compta com un xoc real en una escombrada dels símbols `.eqv` i obliga a aturar-se a decidir-ho. Decidit el 2026-10-06 (`TODO.md`, entrada retirada); fins llavors la marca no tenia fila a la taula de blocs de codi. Al corpus hi havia quatre blocs, tots a A2, amb aquesta forma; fins al 2026-10-07 dos en feien servir variants, sense els senyals (`codi_erroni__gcc_tipus.c`) i amb espais.

### D-49

**`void main()` a la notació, `int main` al C que es compila** · `13_contrib.qmd §Estil de codi C` · 2026-09-21 · `d713262`, `b3072a6`

**Per què `void main()`, si el C estàndard demana `int main`.** L'estàndard exigeix `int main` a les implementacions **allotjades** (*hosted*): les que corren sota un sistema operatiu que en recull el codi de retorn. En un entorn **autònom** (*freestanding*) la forma i el nom del punt d'entrada són **definits per la implementació**, i és aquest el cas d'EC: s'hi treballa directament sobre el processador, sense SO (@imp-directe-sobre-processador). A més, aquell C **no es compila mai**: és la notació del programa que l'alumne tradueix a mà a assemblador. Un `return` que ningú no recull seria una ficció, i `void` ho diu sense enganyar.

Això val **dins d'EC i pel motiu dit**, no en general: en un programa de C normal, compilat per a un SO, **cal `int main`**. L'estàndard n'especifica dues formes, `int main(void)` i `int main(int argc, char *argv[])`; **cap de les dues no és més canònica que l'altra**, i la tria depèn de si el programa fa servir els arguments de la línia d'ordres.

Els blocs que porten `int main` **no són excepcions: són l'altra meitat de la regla**, i hi són perquè el corpus la demostri sencera en lloc d'afirmar-ne només una meitat:

| Bloc | Per què hi va `int main` |
| :--- | :--- |
| `A2.qmd` @tip-forcar-error-tipus | És l'únic C del corpus del qual se cita literalment la sortida del compilador: es compila de debò amb `gcc -Wall -Wextra -Wpedantic`. Amb `void main()`, gcc hi afegiria un diagnòstic nou i la citació deixaria de ser reproduïble. |
| `P3.qmd`/`S3.qmd` @exr-t3-compilacio-relocacio | El problema tracta del **flux de compilació i enllaçat**: el C hi és l'objecte d'estudi, no notació. El `return f(x)` és justament el que fa visible la referència externa que s'ha de resoldre en l'enllaçat. |

### D-83

**Comentaris del C, sempre amb `//`, línia per línia** · `13_contrib.qmd §Estil de codi C` · 2026-10-09

Decisió de l'usuari (2026-10-09), després de la fase 8a. Fins llavors la regla era «d'una sola línia, `//`; de més d'una línia, `/* */`», i el corpus no la seguia (a `f1e67ec`, 89 comentaris `/* */` d'una línia als blocs C, i dos més dins de vinyetes, contra 19 `//`); la fase 8a va aplicar-la als d'una línia (decisió 3, `66b6cab`). La regla nova en fa un sol cas: amb `//` a cada línia, un bloc sencer es pot desactivar envoltant-lo amb `/* … */`, cosa que no és possible si ja conté comentaris `/* … */`, perquè C no els admet imbricats. A2 ho explica a `#imp-codi-format-criteris`, el primer lloc on el llibre parla de com comentar el codi.

### D-50

**Format del codi RISC-V: F1–F5** · `13_contrib.qmd §Estil de codi RISC-V` · 2026-10-03 · `0e25c9f`

Escrit el 2026-10-03 a partir de la proposta d'un *checker* que deixava un marcador a A2. **F5 entra al callout el 2026-10-06** (decisió de l'usuari, a proposta de Claude Code): és l'estil de tota la teoria i les solucions (1 176 línies d'instrucció, contra 596 amb els operands a la columna 13 o 14 als laboratoris i a E2–E4 i E8, i 93 amb un sol espai), i és on cauen els operands del codi que genera `gcc -S`, amb tabuladors de 8. Els operands ja se separaven amb una coma i un espai (1 799 de 1 799 línies amb comes). La columna dels comentaris no es regula perquè 199 dels 213 blocs amb comentaris ja els tenien en una sola columna. Decidit per l'usuari perquè la reunió del grup de treball del 2026-10-05 no ho va arribar a tractar.

### D-66

**Pseudoinstruccions: un sol esquema de columnes i un sol prefix de títol** · `13_contrib.qmd §Fitxer de referència tècnica`, `§Callouts` · 2026-10-07 · `75ea6c6`

Fins al 2026-10-07 les taules de pseudoinstruccions tenien cinc esquemes de columnes: «Pseudoinstrucció, Operació, Expansió», «Pseudoinstrucció, Expansió, Ús», «Pseudoinstrucció, Condició, Expansió», «Pseudoinstrucció, Expansió, Condició» i «Pseudoinstrucció, Expansió». «Condició» hi volia dir dues coses: a `li`, quan s'aplica cada expansió; als salts amb zero, la condició del salt, escrita amb la sintaxi de C («salta si `rs == 0`») i no amb la de les taules ISA. `fmv.s`, `csrr` i `csrw` eren files de taules ISA (les dues de Zicsr, amb «Tipus I»). Els títols feien servir tres prefixos: «Pseudoinstrucció —» (A2, A3 i A4), «RV32I ABI —» (els salts d'A3 i el compendi) i «RV32F ABI —» (A5).

L'esquema de l'operació és el de les taules ISA perquè la pseudoinstrucció es llegeix al costat de la instrucció en què s'expandeix. La columna «Ús» de `j`, `jr` i `ret` es va treure sense perdre res: el rang de ±1 MiB és a la prosa d'A3 (`jal`), i el retorn de subrutina, a §Subrutines. El prefix no porta extensió, com «Directives —», perquè les pseudoinstruccions no són ISA ni ABI: les defineix el manual de l'assemblador (*RISC-V Assembly Programmer's Manual*, `riscv_asm_manual` a `15_bibliografia.bib`).

Era l'opció B de l'entrada del `TODO.md` «Unificar el format de les taules de pseudoinstruccions». El 2026-10-03 (fase 7b) l'usuari va triar l'A, que unificava A2 i afegia `la` al compendi, perquè la B tocava fitxers en revisió externa. La B es va decidir el 2026-10-07 (declaració de l'usuari, que accepta la proposta de Claude Code: «Propostes acceptades: 1, 2 i 3»), per fer-la abans que els equips de revisió comencin (fase 7f de `CLAUDE.md §Pla de treball`). El prefix, «Pseudoinstruccions —», la columna de `li` i l'abast (`fmv.s`, i `csrr` i `csrw` a A9 i al compendi), decisions de l'usuari del mateix dia, a proposta de Claude Code.

### D-90

**Exemples plegables a l'HTML i remissió de l'enunciat a la solució: pilot de T1** · `13_contrib.qmd §Problemes i solucions`, `§Callouts`, `§Renderitzar el projecte` · 2026-10-09

Decisió de l'usuari (2026-10-09, després de la fase 8a), literal: «Fes T1 com a pilot», sobre l'entrada del `TODO.md` «Exemples i solucions plegables a l'HTML» (petició del 2026-10-08, fase 7g: «Fer els exemples dinàmics? És a dir, que per veure la solució calgui prémer un botó. […] I segurament també les solucions dels problemes»). El pilot fa, només a T1, les dues coses de la valoració de Claude Code, totes dues amb un filtre, `25_scripts/plegables.lua`:

- **Exemples**: dels 19 `#tip-` d'A1, els cinc que tenen el format **Pregunta** → **Solució** → **Resposta** (`tip-natural-interpretacio`, `tip-natural-representacio`, `tip-notacio-hexadecimal`, `tip-ca2-interpretacio` i `tip-ca2-representacio-negatiu`) porten la solució i la resposta dins d'un div `.resposta`, que a l'HTML es plega sota «Mostra la solució» (`<details>`) i al PDF queda igual. La resta són il·lustratius, sense una pregunta per intentar abans (els de multiplicació i divisió en Ca2 acaben amb una **Resposta**, però l'exemple és el procediment), i no es pleguen.
- **Solucions**: cada enunciat `#exr-t1-` que té solució a S1 (15 de 15) acaba amb la remissió `@sol-t1-…` («Solució 19.1»), a l'HTML i al PDF. Abans, cap enunciat no remetia a la seva solució (0 `@sol-` a P1–P9).

La remissió la genera el filtre a partir de l'slug compartit ([D-22](#d-22)), en lloc d'escriure-la als `.qmd`: escrita a mà, als 108 enunciats amb solució seria una segona còpia de la correspondència, que pot caducar. `<details>` i no un callout imbricat amb `collapse=true` (com els `#wrn-`): el plegable és una part de l'exemple, no un altre bloc amb títol i color. El filtre s'executa `at: pre-ast` perquè, més tard, els divs `#exr-` ja són nodes propis de Quarto i no s'hi pot afegir res; la remissió que hi afegeix la resol el `crossref` com qualsevol altra `@sol-`.

**Estendre-ho** és una decisió de l'usuari, en valorar el pilot (`TODO.md`). Per a les solucions, n'hi ha prou d'afegir el tema a la taula `PILOT` del filtre, sense tocar cap `.qmd`. Per als exemples, cal marcar a mà el div `.resposta` a cada exemple amb pregunta (a A1–A8, 16 amb el format **Pregunta**: A1 5, A3 2, A6 5 i A7 4), i A2–A8 són als fitxers que revisen els equips (D-65).

### D-101

**«📑 Continguts»: l'índex dels apunts a l'HTML, generat des dels `.qmd`** · `13_contrib.qmd §Renderitzar el projecte`, `10_continguts.qmd`, `25_scripts/continguts.lua` · 2026-10-10

Petició de l'usuari (2026-10-09), literal: «Té sentit a la versió HTML afegir un índex de continguts per poder tenir una visió general? (com en el PDF)». A l'HTML, la barra lateral mostrava els capítols, i la «Taula de continguts» de cada pàgina, les seccions del capítol obert: cap vista no mostrava les seccions de tots els temes alhora. Decisions de l'usuari, literals: el 2026-10-09, «Abast: Només A1--A9», «Profunditat: fins a nivell `###`» i «Posició: entre `👋 Presentació` i `Apunts`. Justificació: és massa llarga per formar part de `👋 Presentació`»; el 2026-10-10, el nom, «"Fitxer": 10_continguts.qmd» i «"títol i menú": «📑 Continguts»», i «Acceptades la resta de propostes» de Claude Code:

- **El títol de cada tema, sense el número**: «Tema 1: Introducció». La proposta de Claude Code, acceptada amb les altres, era el de l'índex del PDF i de la pàgina del tema, «1 Tema 1: Introducció», encara que repetís el número; l'alternativa, «A1 Introducció», la del menú. Decisió de l'usuari (2026-10-10, després de publicar la pàgina), literal: «Elimina els nombres inicials dels títols de tema. Per exemple "1 Tema 1: Introducció" - > "Tema 1: Introducció"». Les seccions conserven el número de l'HTML («1.4 Codificació…»).
- **Sense plegar**: la «Taula de continguts» de la pàgina mateixa, amb els nou temes, fa de salt d'un tema a l'altre. La valoració inicial deia «plegada per parts», quan l'abast era tot el llibre.
- **Fora de la cerca** (`search: false`): la pàgina té tots els títols de secció dels apunts, i cada cerca d'un títol la retornaria també.
- **Cap enllaç des de la Presentació**: sortiria també al PDF, i el menú ja hi porta.

**Un filtre, i no un script de pre-render** (la valoració inicial): no genera cap fitxer ni afegeix cap pas al `Makefile` o al CI, i llegeix les fonts amb el lector de Pandoc, que ja separa els callouts i els blocs de codi. Hi surten les mateixes capçaleres que a la «Taula de continguts» de cada pàgina, amb el mateix número: les 269 `##` i `###` d'A1–A9 coincideixen una per una, en número, àncora i text, amb les de les pàgines renderitzades a `b4bd57c`. Les de dins d'un div que no sigui un callout no hi surten, com tampoc no surten a la de la pàgina, perquè Pandoc només hi posa les del primer nivell del document.

**Al PDF, la pàgina no hi deixa res**: el PDF ja té el seu índex. Embolcallar-la amb `.content-visible when-format="html"` no n'hi ha prou, perquè Quarto en treu el títol del capítol i el PDF rebia igualment `\chapter*{…}`, la línia de l'índex i el marcador; per això és el filtre el que en treu la capçalera i el div. Amb la pàgina, el PDF del `make render-complet` és el mateix que a `b4bd57c` (comprovat el 2026-10-10): 574 pàgines, i el text, línia a línia, igual llevat de la data i el hash de la portada (`versio.lua`). El `.tex` només hi canvia, a més, l'ordre de les definicions `\newtheorem` d'«Algorisme» i de «⁂», independents: Quarto les escriu recorrent una taula amb `pairs` (`tkeys`), sense ordenar-la, i l'ordre pot variar d'un render a l'altre.

### D-102

**Una taula amb etiqueta `#tbl-` porta peu** · `13_contrib.qmd §Taules` · 2026-10-10

L'usuari va veure que `#tbl-exemple-comparacio-versions-progs` (A6) no tenia peu, i va preguntar si era un fals positiu de `verifica_taules.py`. No ho era: l'script no mirava els peus. Una taula amb etiqueta i sense peu Quarto la numera igualment i en deixa el peu buit: «Taula 6.1» sola a l'HTML (classe `quarto-uncaptioned`) i «Taula 6.1.» al PDF. N'hi havia quatre, cap amb cap remissió: `#tbl-exemple-comparacio-versions-progs` (A6), `#tbl-tres-c` i `#tbl-disseny-l1-l2` (A7) i `#tbl-syscalls` (A9). Proposta de Claude Code, acceptada per l'usuari («Endavant»): posar-los peu, d'acord amb el seu criteri de «totes les taules amb `#tbl-`», en lloc de treure'ls l'etiqueta; i que `verifica_taules.py` ho avisi, al peu de la taula o al div que la porta. Fins llavors la guia només deia que el peu era obligatori al cos del text.

## Figures

### D-51

**El `<desc>` com a text alternatiu, i una mida comuna a l'HTML** · `13_contrib.qmd §Figures i material gràfic` · 2026-10-06 · `e806916`

Que el `<desc>` no repeteixi el peu és la decisió 6 de la fase 7c (2026-10-03). L'amplada del `viewBox` per 1,4 a l'HTML és decisió de l'usuari (2026-10-06). Fins llavors, una figura amb `width="100%"` s'estirava a tota la columna, i una amb l'amplada en px es quedava a la mida natural (`TODO.md`, «Mida de les figures a l'HTML», avui a `24_specs/arxiu_todo.md`).

**Les figures estretes generades** (`gen_BA.py`, `gen_mapa.py` i `gen_memoria.py`, `24_specs/svg.md §2`) porten l'amplada en px, i no `width="100%"`, per una decisió anterior de l'usuari (2026-10-05, fase 7c, bloc 11): a l'HTML, una figura de 326 o 340 px amb `width="100%"` s'estirava a tota la columna (937 px, ×2,9) i el text hi sortia a uns 31 px; amb l'amplada en px es mostrava a la mida natural, i en un visor estret s'encongia igualment fins a l'amplada de la columna. Al PDF no canviava res: `rsvg-convert` ja en feia servir la mida del `viewBox`. Des del bloc 12 (2026-10-06), la mida a l'HTML la fixa el filtre `figures.lua` per a totes les figures, i l'amplada en px d'aquests generadors ja no hi influeix; es manté perquè és innòcua (fins al 2026-10-09, a `24_specs/svg.md`).

### D-52

**Camps horitzontals a les figures de registres** · `13_contrib.qmd §Política de generació SVG` · 2026-10-03 · `2dbf236`

La clau `horitzontals` es va afegir el 2026-10-03 (fase 7c) a petició de la revisió externa de T5, per a la «S» de `T5_ieee754_format_registre`.

### D-53

**L'estat d'una figura no va al nom del fitxer** · `13_contrib.qmd §Convencions SVG` · 2026-10-04 · `4fa6fd3`

Els altres sufixos de fitxer font que hi havia (`__drawio`, `__org`, `____error____`, `__net__`) eren de fitxers orfes, retirats a la fase 7c. Revisat i escrit el 2026-10-04 (fase 7c), amb els sufixos d'origen `__BA` i `__subrutina` proposats per l'usuari.

### D-54

**La foto del xip de T7 és CC0 1.0** · `13_contrib.qmd §Convencions SVG` (figures externes) · 2026-10-06 · `0d33d13`

Fins al 2026-10-06 el `.bib` hi deia CC BY-SA 2.0 i només Fritzchens Fritz; la pàgina del fitxer a Wikimedia Commons diu CC0 1.0 i tots dos autors, i el `.bib` es va corregir per decisió de l'usuari.

### D-55

**Figures dinàmiques a l'HTML, seqüència estàtica al PDF** · `13_contrib.qmd §Figures dinàmiques` · 2026-10-04 · `2d14b8f`

Decisió de l'usuari 4 de la fase 7c. Prototip: `#fig-lru-exemple` (bloc 9 de la fase 7c, 2026-10-04) (fins al 2026-10-09, a `24_specs/svg.md`).

### D-56

**Imatges sense peu centrades als callouts del PDF** · `13_contrib.qmd §Presentació visual` · 2026-10-06 · `74507d7`

Fins al 2026-10-06 sortien alineades a l'esquerra. Quan es va escriure, totes les imatges sense peu dels callouts eren figures de registres més amples que el callout, de manera que la regla no hi tenia cap efecte visible: és per a la primera que no ho sigui.

### D-69

**Blocs de codi al PDF: no floten i es parteixen entre pàgines** · `13_contrib.qmd §Presentació visual` · 2026-10-08

Detectat a la fase 7g, a partir d'una observació de l'usuari: la secció «Exemple: RSE mínima en RISC-V» d'A9 (§9.4.4) diu «El codi següent…» i, al PDF, no hi havia cap codi. Quarto escriu cada bloc amb `filename` com a flotant `codelisting` (paquet `float`, estil `ruled`). Dels 559 llistats del llibre (2026-10-08), els 349 de dins dels callouts porten `[H]`, que en fa una caixa que no es parteix, i els 210 de fora, la posició per defecte `h`: LaTeX els posa on li caben. Conseqüències mesurades sobre el PDF: l'RSE d'A9 (96 línies) sortia deu pàgines més enllà, al final del capítol, i els llistats de laboratori de més d'una pàgina (`s3_4_2.s`, `s4_2_2.s`, `s6_5_1.s`) també anaven a parar al final de la sessió; i la solució de l'RSE de S9 (106 línies, dins d'un callout) es tallava al peu de la pàgina, i la resta no sortia enlloc.

`preamble.tex` redefineix `codelisting` com un bloc normal que conserva el peu, el comptador, la llista de llistats i les ratlles de l'estil `ruled`. Dins d'un callout, el bloc va sense el fons gris (`Shaded`, de `framed`), que `tcolorbox` no sap partir. El PDF passa de 588 a 569 pàgines: eren els buits que deixaven els flotants. Alternatives descartades: `\floatplacement{codelisting}{H}` per a tots, que hauria fet caixes sense salt de pàgina (els llistats de més d'una pàgina haurien desbordat el peu, com el de S9); i treure el `filename` dels blocs, que és la convenció de §Blocs de codi.

### D-57

**Fórmules en línia a l'HTML: `overflow` només a les llargues** · `13_contrib.qmd §Presentació visual` · 2026-10-06 · `74507d7`

Fins al 2026-10-06 l'`overflow-x: auto` era a totes, i un `inline-block` amb un `overflow` que no sigui `visible` es recolza en la vora inferior (CSS 2.1 §10.8.1): les fórmules pujaven d'1 a 6 px per sobre de la línia de text (mesurat a A6, 40 fórmules) i feien créixer l'interlineat. Després del canvi, a l'escriptori, cap fórmula d'A4, A5, A6 i S6 no era llarga i totes eren a 0 px de la línia; en un mòbil de 375 px, n'eren llargues 4, 14, 2 i 1.

### D-71

**BA: vectors massa llargs amb el tram del mig d'alçada fixa** · `24_specs/svg.md §3` · 2026-10-08

Decisió de l'usuari (2026-10-08, fase 7g, decisió 10): el BA de `variancia` de S5 passa de taula a figura de `gen_BA.py`, com els de L3 i S3 de la fase 7f. El vector `vquadrats` (`float[100]`, 400 bytes) faria 4 000 px d'alt a ×½ i 2 000 a ×¼, l'escala més petita de §3. `gen_BA.py` admet ara `mig` als vectors: el tram elidit es dibuixa amb aquesta alçada, i la mida i els desplaçaments rotulats continuen sent els reals (la funció `alcada` dibuixa, `mida` compta). Les sis figures de BA que ja hi havia queden idèntiques byte a byte.

### D-67

**El generador dels mapes de memòria, `gen_mapa.py` (sufix `__mapa`)** · `13_contrib.qmd §Convencions SVG` · 2026-10-07

És el generador germà de `gen_BA.py` que preveia el pla de l'entrada del `TODO.md` «Generador de BA (`gen_BA.py`): on es pot fer servir, i pla d'aplicació» (2026-10-04), i completa la família de memòria de la decisió 13 de la fase 7c: el mapa de memòria de RARS (tipus `regions`) i les piles en fila (tipus `piles`) d'A3, que eren SVG dibuixats a mà. Comparteix amb `gen_BA.py` les primitives de la columna de memòria (`25_scripts/columna_memoria.py`), perquè les dues famílies dibuixin igual les zones, les ratlles, les etiquetes i les fletxes. El nom, `__mapa`, perquè les dues menes de figura són mapes de la memòria: la memòria sencera o la pila en diversos moments; `__pila` no hauria encaixat amb el mapa de RARS.

Amb el generador, les figures de BA i el mapa passen a la classe `estreta` de `24_specs/svg.md §2` (340 px), amb `w_rect` de 244 px: el marge dret queda de 10 px, com el superior i l'inferior. L'altra opció, mantenir `w_rect` a 230 px, deixava un marge dret de 24 px. La que proposava el `TODO.md`, 254 px, s'havia calculat amb el rectangle a x = 76, que és l'amplada de la columna d'etiquetes; els generadors i `svg.md §5` el posen a x = 86. A les piles, la línia de `sp` deixa el vermell `#cc0000`, que la paleta reserva a les dependències de dades, i pren el color de la zona del cim, com «sp →» als BA (`svg.md §9`). Les piles no porten el codi C a dins, que ja és al bloc C del callout, just a sobre. En revisar les figures, l'usuari en va afegir dues convencions a `svg.md`: les vores horitzontals de cada zona, per dins de la seva àrea, perquè la frontera entre dues zones de color diferent no depengui de l'ordre de dibuix (§7, opció A de Claude Code; la de ratlles de dos colors, de l'usuari, es va descartar perquè la línia discontínua ja vol dir «elidit»); i un byte de línia contínua a cada extrem del tram elidit d'un vector o d'una zona genèrica (§4, proposta de l'usuari). Per decisió de l'usuari, a proposta de Claude Code, l'alineació passa a tenir contorn continu `#adb5bd` (§4): els seus bytes són del BA, i així la línia discontínua només vol dir contingut elidit o espai lliure. També a petició de l'usuari, cada zona de les piles en fila porta el seu contorn (§9). Els rètols «creix» del mapa es desplacen 6 px cap a la punta de la fletxa, perquè la «c» no toqui la vora (§11). Decisions de l'usuari (2026-10-07, fase 7f), a proposta de Claude Code. De pas, a petició de l'usuari, `ba.toml` i `mc.toml` passen a `BA.toml` i `MC.toml`, per coherència amb els seus generadors (`gen_BA.py`, `gen_MC.py`).

**De `svg.md`** (fins al 2026-10-09 hi era com a historial, al costat de les regles): fins a la fase 7f, les figures de BA i el mapa de memòria eren de 326 px, amb `w_rect=230 px`, i les piles, de 310 i 510 px (§2). L'alineació tenia les vores verticals discontínues i cap vora horitzontal, com si fos un buit (§4). Cada zona era un `<rect>` amb el traç centrat a la vora, i la que es dibuixava després tapava la meitat del traç de l'anterior amb el farciment i, si en tenia, l'altra meitat amb el seu traç: el resultat depenia de l'ordre de dibuix (mitja línia vermella sota la blava entre `.text` i `.data`; la vora inferior del heap, a mig gruix sota l'espai lliure) (§7). I amb `desplacaments = true` (`gen_BA.py`), cada zona del BA porta el seu desplaçament des de `sp`, de manera que la figura fa la feina de la taula «Desplaçament des de `sp`», que ja no cal (decisió de l'usuari, 2026-10-07; §9): per això les dues taules de desplaçaments d'A3 van sortir.

### D-68

**Els originals substituïts per una figura generada es conserven, a `22_figs_originals/conservats/`** · `13_contrib.qmd §Convencions SVG` · 2026-10-04 · 2026-10-07 · 2026-10-09

Decisió de l'usuari del 2026-10-04 (fase 7c), quan A3 va passar a consumir els BA de `multi` i d'`exemple` generats per `gen_BA.py`: els originals es conserven, perquè l'usuari també els fa servir per a les diapositives, i les esmenes que necessitin les fa ell mateix (`TODO.md §Tasques per tema → T3`, «Retocs manuals pendents»). Fins al 2026-10-07 només constava a `24_specs/svg.md §17` i a l'inventari, que els llista a part dels orfes. Es va escriure com a regla el 2026-10-07 (fase 7f), en conservar també, per decisió de l'usuari, els originals de `T3_ba_func`, `T3_ba_general`, `T3_mapa_memoria`, `T3_pila_uninivell` i `T3_pila_multinivell`.

**El directori, des del 2026-10-09** (petició de l'usuari, 2026-10-08, fase 7g, literal: «Valora si té sentit crear un directori a on posar els fitxers orfes que es volen guardar; d'aquesta manera, es pot crear un agent (o el mecanisme que pertoqui) per buscar orfes fora d'aquest directori i presentar-los demanant si cal moure'ls al directori de fitxers orfes o esborrar»; proposta de Claude Code, acceptada el 2026-10-09). Els 15 originals conservats —set de T3 i vuit de T7— van passar a `22_figs_originals/conservats/`. Fins llavors l'inventari els deduïa: un original sense consumir era «conservat» si hi havia una figura generada amb la mateixa arrel (o amb una arrel que en fos el començament, com `A7_capacitat_exemple`), i «orfe» si no. Ara el criteri és el directori, i un original de `conservats/` que el llibre consumís seria un avís. De pas, el pre-render ja no els converteix: l'expressió de `norm_font.py` a `_quarto.yml` no entra als subdirectoris, i des del mateix dia va ancorada a l'inici del camí (`^22_figs_originals/`), perquè `norm_font.py` recorre tot l'arbre i també convertia els 74 SVG del *worktree* `.claude/worktrees/fase8a/`. `gen_dark.py` tenia el mateix defecte amb l'`auto_figs/` d'aquell *worktree*, i la seva expressió també va ancorada (`^auto_figs/`): sense l'àncora, després de moure els conservats, el pre-render en continuava escrivint les 15 variants fosques, a partir de les clares del *worktree*. Els fitxers del repositori es processen després que els del *worktree*, i per això les figures del llibre no se'n van ressentir.

### D-76

**Noms de les figures pel fitxer que les consumeix: `A<N>_`, `P<N>_`, `S<N>_`, `L<N>_`** · `13_contrib.qmd §Figures i material gràfic` · 2026-10-08

Decisió de l'usuari (2026-10-08): «noms de fitxers de figures `Tx_*` -> `Ax_*`, `Px_*`, `Sx_*`, `Ly_*`»; l'abast, a proposta de Claude Code. Fins llavors el prefix era el del tema (`T3_`), que no deia on surt la figura, i tres figures de les solucions i del laboratori duien el prefix d'un tema que no les consumeix. Es va fer abans que els equips de revisió comencessin, dins de la finestra de canvis de [D-65](#d-65), perquè toca A1–A9. De 96 arrels consumides, 93 passen a `A<N>_` (les set que també surten al compendi, `11_riscv.qmd`, prenen el prefix del tema: A5 i A9); `T3_ba_A`, `T5_ba_variancia` i `T3_ba_moda` passen a `S3_`, `S5_` i `L3_`. Els 15 originals conservats (D-68) prenen el de la versió generada (`A3_`, `A7_`). Canvien els fitxers de `22_figs_originals/`, `23_figs_externes/` i el `.gv` de `24_specs/`, les seccions dels `.toml` dels generadors, les sortides d'`auto_figs/`, `svg.md`, el `TODO.md` viu i els `.qmd`. Els scripts conserven el nom (`gen_T4_sumador.py`, `gen_T7.py`, `gen_T8.py`), com dos noms que no són figures: `T4_P_tasques.md` (un fitxer històric) i `PDF_originals/01_apunts/T6_Memoria_cache.pdf`. Les entrades d'aquest registre i del `TODO.md` anteriors al canvi citen els noms d'abans (`git log --follow`).

### D-92

**Les figures natives, a la paleta: dos colors afegits, els de fora migrats i les figures de T6 retocades** · `24_specs/svg.md §10`, `§14` i `§15` · 2026-10-06 · `c7180d9`, `77e6bce`

Decisions de l'usuari (2026-10-06, a proposta de Claude Code), en tancar els avisos de l'inventari de la fase 7c (D5–D8). **Dos colors afegits a §10**, perquè ja els feien servir diverses figures amb aquest paper: `#e6f1fb` (zona o contenidor), a `A1_von_neumann` i `A8_mv_flux_traduccio`, i `#dee2e6` (graella i vores secundàries), a `A4_matriu_emmagatzematge`, `A4_matriu_offset_ij` i `A7_gap_processador_memoria`. **Els colors de fora de la paleta, migrats.** Fins llavors, diverses figures natives (T1, T3, T5, T6, T7) en feien servir, que §13 convertia per al fosc; dues, `A3_pila_uninivell` i `A3_pila_multinivell`, en feien servir un (`#e6e9ec`) que no hi era, i al fosc la memòria lliure sortia d'un gris molt clar. Es van passar a la paleta: el negre de les figures natives de T5, a `#343a40`; els blaus de T1 i d'`A7_mc_fallada`, a `#084298` i `#cfe2ff`; els grisos de text de T3, a `#343a40`; els de traç de T1, a `#adb5bd`; i el de la pila, a `#f8f9fa`. §13 va perdre les 32 entrades que ja no feia servir cap fitxer: les 23 de les figures externes de T7 retirades a la fase 7c i les 9 que la migració va deixar lliures. **Les cinc figures de T6, extretes de PDF** (§15): se'ls va treure el `textLength`, els subíndexs es van passar a `<tspan dy>` dins d'un sol `<text>` (a `A6_amdahl`, els 38 `<text>` d'un caràcter o d'un subíndex es van refer en 15), el text es va posar en la notació d'A6 ($V_{CC}$, $V_{in}$, $V_{out}$, $s_x$, $t_{\text{no-millorat}}$, PMOS i NMOS) i els colors, a la paleta (el negre a `#343a40`, i el gris mig de les barres, `#999999` i `#b3b3b3`, a `#adb5bd`). Fins al 2026-10-09, tot això era a `svg.md` com a historial, al costat de les regles. La paleta té pendent una revisió per reduir-ne els colors (`TODO.md`).

### D-93

**Portes lògiques: la forma distintiva ANSI/IEEE 91** · `24_specs/svg.md §16` · 2026-10-03 · `184832c`

Convenció fixada a la fase 5 (2026-10-03, decisió de l'usuari), amb les figures del sumador de T4 (`#fig-semisumador-sumador-complet` i `#fig-sumador-propagacio-rossec`, de `25_scripts/gen_T4_sumador.py`). La forma distintiva és la de les diapositives de l'assignatura i la d'IC; es descarta la rectangular de l'IEC. Fins al 2026-10-09, la data i la decisió eren a `svg.md §16`.

### D-94

**Figures generades: model (a) per a les soltes, model (b) per a les famílies** · `24_specs/svg.md §17` · 2026-10-03 · `4fa6fd3`

Model de generació de la fase 7c (2026-10-03, decisió de l'usuari), escrit a `svg.md` l'endemà, amb els primers generadors del pre-render (`4fa6fd3`). En el model (b), la definició és un TOML i l'SVG no es versiona: una convenció nova s'aplica a tota la família d'un sol cop. En el model (a), l'SVG versionat és el font i l'script el regenera, amb `--comprova` perquè un retoc fet a mà a l'SVG i no a l'script surti com a diferència (`make comprova-figures`). Fins al 2026-10-09, la data i la decisió eren a `svg.md §17`.

### D-95

**Figures de memòria cau: seqüència, traça i estat** · `24_specs/svg.md §17` · 2026-10-04 · `218e195`, `d59ae41`

Decisió de l'usuari (2026-10-04, fase 7c): al PDF, la seqüència per als exemples curts (estat inicial, polítiques d'escriptura, LRU) i la traça per als llargs (conflicte, capacitat); l'estat inicial, en totes dues, com a subfigures, perquè l'alumne faci la transició d'una a l'altra; i a l'HTML, la figura dinàmica ([D-55](#d-55)). La terminologia de les figures («Lectura», «Escriptura», «Encert», «Fallada» i les fallades «obligatòria», «de capacitat» i «de conflicte») és la decisió 11 de la fase 7c. El tercer estil, `estat`, és del 2026-10-06 (`d59ae41`, decisions D1–D4 de l'usuari): les tres taules d'organització d'A7 (`#fig-mc-organitzacio`, `#fig-assoc-conjunts-taula` i `#fig-escriptura-dirty-bit`), que fins llavors eren natives. Fins al 2026-10-09, les dates i les decisions eren a `svg.md §17`.

### D-99

**Vores compartides a totes les figures: cada zona, per dins de la seva àrea** · `24_specs/svg.md §7` · 2026-10-09

La regla de [D-67](#d-67) (2026-10-07, fase 7f) només s'aplicava a la columna de memòria de `gen_BA.py` i `gen_mapa.py`; l'usuari en va decidir l'extensió a la resta de figures el mateix dia (decisió G2), i la fase 7h de `CLAUDE.md §Pla de treball` (acceptada el 2026-10-08) la va fer. A la resta, dos `<rect>` amb traç de color diferent compartien una vora i el segon tapava mig traç del primer, o un farciment sense traç en tapava mitja: el que es veia depenia de l'ordre de dibuix (la fila grisa de sota tapava la vora inferior de la fila blava d'una MC; el camp `x=0` d'un format d'instrucció perdia la meitat esquerra del traç, fora del `viewBox`). La mesura de l'entrada del `TODO.md` (`git show 7983a87:TODO.md`) en donava 54: 44 de consumides i 10 originals conservats. Els conservats, de fet, eren 12: el filtre dels fotogrames (`'_pas' in f`) també excloïa `A7_capacitat_exemple_bucle_primera_passada` i `…_segona_passada`.

La generalització, a proposta de Claude Code, acceptada per l'usuari amb el pla de la fase (2026-10-09): la regla val en horitzontal i en vertical, per a qualsevol parell de zones que es toquen; les vores de fora també van per dins, com les de dalt i de baix de `vores()`; una zona amb `rx` dibuixa totes les vores per dins, perquè una línia compartida entre dues cantonades arrodonides no té sentit; i un ressalt sense farciment es dibuixa després de les zones que toca. La implementació, de Claude Code: un postprocés de l'SVG acabat (`vores_compartides()`, de `figlib.py`) i no reestructurant els quatre generadors, perquè cadascun dibuixa les cel·les a la seva manera (`cel()`, `rect()`, els camps dels registres) i el postprocés en cobreix tots els casos amb el mateix codi; només redibuixa els grups amb conflicte, de manera que les figures sense cap vora en conflicte surten iguals byte a byte. Als natius s'hi va aplicar la mateixa funció, un cop, i se'n van passar a atributs els `style` d'Inkscape que sobreescrivien els colors dels `<rect>` (`A7_mc_encert`, `A7_mc_fallada`).

Els 12 originals conservats no s'hi van tocar, per decisió de l'usuari (2026-10-09, opció (a)): són per a les diapositives i les esmenes les fa l'usuari ([D-68](#d-68)). De pas: el tram blau d'`A9_cicle_interrupcio` entrava 10 px dins del verd (de x = 200 a 210), i el ressalt dels marcs d'`A8_mv_exemple_tlb` i la vora del marc compartit d'`A8_mv_comparticio` es dibuixaven abans del marc següent, que en tapava la meitat. Després del canvi, la mesura de l'entrada sobre les figures consumides en dona 3, i són ressalts sense farciment dibuixats després de les cel·les que toquen (la columna d'`A7_escriptura_dirty_bit` i les files d'`A8_mv_comparticio` i d'`A8_mv_exemple_tlb`): la mesura només mira la geometria, no l'ordre de dibuix.

## Eines

### D-58

**`make render-complet`, obligatori abans de tocar el PDF** · `13_contrib.qmd §Verificació de l'entorn` · 2026-09-22 · `5589801`

Un render HTML no exercita el PDF: el 2026-09-22 el corpus tenia **83 blocs `when-format="pdf"`**, i almenys cinc convencions de la guia existien precisament perquè el PDF es comporta diferent (la duplicació de figures si no se separen les variants, `tbl-colwidths` que ha de sumar 100, les capçaleres `###` del laboratori, `[@sec-]` que només funciona a PDF, i la guia mateixa, que és HTML-only).

### D-62

**Les afirmacions sobre RARS es resolen executant RARS, i el `.jar` fora del repositori** · `13_contrib.qmd §Verificació empírica a RARS` · 2026-09-23 · `6fcee2c`, `fbf7c3d`

Ja ha passat dues vegades: la comprovació que RARS alinea `.dword` a 4 bytes i no a 8, com demana l'ABI (a L2 des del juliol del 2026 com a molt tard; des del 2026-10-03, la nota de `@nte-directives-alineacio-inicialitzacio` a A2 i el `.align 3` de la solució de `s2_1_1.s`), i l'experiment de `.section` (2026-09-23, [D-8](#d-8)), que va impedir una conversió de 121 directives que no hauria assemblat. Que es comprovi pel resultat i no per l'absència d'error ve del mateix experiment: tres de les formes provades assemblaven sense queixar-se i no feien el que semblava (el cas, a la skill `rars`).

El `.jar` va ser al repositori fins a `fbf7c3d` (2026-07-11), que el va eliminar deliberadament. El procediment de les sessions de Claude Code, que eren a la mateixa secció de la guia fins al 2026-10-07, és a la skill `rars`.

**Seguiment del 2026-10-10, a la nit: les eines, al `.cache/` del clon.** Decisió de l'usuari (fase 12), literal: «El meu plantejament era que `.cache/' estigués dins del repositori per a ús local (per això afegir-lo a `.gitignore`) i per haver de baixar només un cop el programari necessari sempre que no estigui disponible al sistema. Si ho veus raonable, implementa-ho. Valora si cal fer `mv ~/.cache/ec/* .cache/` o similar abans per no haver de tornar a baixar el programari.» Fins llavors, RARS (des de [D-103](#d-103)) i LanguageTool ([D-105](#d-105)) es baixaven a `~/.cache/ec/`, fora del clon, perquè aquesta entrada deia «fora de l'arbre del projecte»; el que la regla vol, però, és que el `.jar` no es versioni, i `.cache/` és al `.gitignore`. `25_scripts/eines_externes.py` en dona el directori: el `.cache/` del clon principal, el pare del directori de git comú, de manera que els *worktrees* el comparteixen i cada eina es baixa un sol cop. Les variables d'entorn (`RARS_JAR`, `LANGUAGETOOL_DIR`) hi passen al davant, per a una còpia que ja és al sistema. El que hi havia a `~/.cache/ec/` (RARS i LanguageTool) es va moure al `.cache/` del clon de l'editor, i no es va haver de tornar a baixar res. Quarto no hi entra, perquè no renderitza els directoris que comencen per punt.

### D-59

**Push directe a `main`: la restricció és per als revisors, no per a l'editor** · `13_contrib.qmd §Push directe a main` · 2026-04-29, 2026-10-07 · `1d4308d`

La restricció als canvis trivials és del 2026-04-29. Declaració de l'usuari (2026-10-07, fase 7e): «La restricció és per als revisors externs. No per a l'editor, que soc jo, fins al segon quadrimestre d'aquest curs (2026-27).» Fins llavors la guia no ho deia, i les sessions de Claude Code empenyien a `main` canvis grans (`3ee92f4`, per exemple, toca 19 fitxers) amb l'autorització de `CLAUDE.md`, en contradicció aparent amb la regla.

### D-60

**DejaVu Sans Mono, la font monoespaiada del PDF** · `13_contrib.qmd §Renderitzar el projecte` · 2026-10-06 · `74507d7`

Des del 2026-10-06. Amb DejaVu Sans Mono el registre de LaTeX ja no hi dona cap «Missing character». Escalada a l'altura de les minúscules del text, és més estreta que Latin Modern Mono, i cap bloc de codi ni cap taula no surt del marge (`pdftotext -bbox`).

### D-61

**El hook d'abans del commit avisa, però no pregunta; i no renderitza si el render no llegeix cap fitxer canviat** · `13_contrib.qmd §IA` · 2026-10-03, 2026-10-09 · `722c522`, `980434b`

Fins al 2026-10-03 la revisió de prosa i l'avís de `make render-complet` demanaven confirmació; decisió de l'usuari: no cal, perquè el flux ja fa `make render-complet` abans de cada push. El `make render` del hook va trigar **2 min 38 s** el 2026-09-25.

Des del 2026-10-09 el hook se salta el `make render` quan el commit només toca fitxers que el render no llegeix: `TODO.md`, `CLAUDE.md`, `README.md`, el registre de decisions, l'arxiu del `TODO.md`, l'inventari de figures (`24_specs/figures.md`, que l'escriu `make inventari`) i `.claude/`. Ho va demanar l'usuari (2026-10-09: «hi ha testos innecessaris (per exemple, no cal renderitzar quan només hi ha canvis a `TODO.md`)»), i la llista és la proposta de Claude Code que va acceptar. Es mira, com la resta del hook, l'arbre de treball sencer respecte d'`HEAD`: si qualsevol altre fitxer ha canviat, encara que sigui d'una altra sessió, renderitza. `LICENSE.md` no hi és perquè `14_LICENSE.qmd` l'inclou. Des del 2026-10-10, la llista és la classe «operatiu» de la classificació de `25_scripts/comprova.py`, i els nivells de comprovació de cada mena de canvi, [D-103](#d-103).

### D-74

**Calendari del laboratori: `verifica_calendari.py`, l'agent `verificador-calendari` i el hook** · `13_contrib.qmd §IA` · 2026-10-08

Decisió de l'usuari (2026-10-08, fase 7g): «Com que canviarà a cada quadrimestre, escriu un agent per fer-ne la comprovació i afegeix-lo al protocol de comprovació de commits que afectin a `Lcalendari.qmd`». L'auditoria de la fase hi va trobar una data que no cau en el dia de la seva fila (el 07/05/2026, dijous, a la fila dels divendres). La part mecànica (dates, dies, ordre i sessions) la fa un script, perquè no depengui del model; el que demana judici (quadrimestre vigent, festius, una data amb l'horari d'un altre dia), l'agent, que només informa. El hook d'abans del commit hi afegeix el pas 4, que no bloqueja, com els altres avisos (D-61). Al mateix temps, el calendari passa a ser només de l'HTML: al PDF, un capítol «Calendari» amb la remissió al web (abans hi sortia un capítol buit amb el títol del quadrimestre, perquè Quarto en treia el títol fora del bloc HTML).

**El calendari és una demo** (declaració de l'usuari, 2026-10-09, literal: «demo del quadrimestre natural (quan hi ha més grups)»): mostra el quadrimestre de primavera, el que té més grups, i no s'ha de mantenir al dia per a cada quadrimestre. La data que l'auditoria hi va trobar, el 07/05/2026 (dijous) a la fila dels divendres, es va deixar primer com a error conegut de la demo (recomanació de Claude Code); i el mateix dia, l'usuari en va demanar un patró, literal: «Com que el canvi d'algun dia per algun altre és força freqüent, si tens alguna proposta ferma, com ara passar la font de la data a vermell o alguna altra manera de resaltar-la i una explicació, aplica-la directament. D'aquesta manera ja ens servirà de patró.» **Patró del canvi de dia** (proposta de Claude Code, aplicada directament): la data en vermell i amb †, `[07/05 †]{.canvi-dia}`, i una nota sota la taula que comença amb `[†]{.canvi-dia}`. La † fa que el canvi no depengui només del color (accessibilitat), i el vermell no és la negreta, que ja marca l'examen. El vermell és el de les fallades de la paleta de les figures (`#dc3545`; al mode fosc, `#f07080`, el de la seva substitució a `svg.md §13`), a `styles.css`. `verifica_calendari.py` no marca com a error una data amb `.canvi-dia` que no cau en el dia de la fila, sinó com a informació; i sí que és error que una data marcada hi caigui, o que hi hagi canvis de dia sense la nota.

### D-96

**Errades del material publicat: una *issue* amb l'etiqueta `errada`, i el commit que la tanca** · `13_contrib.qmd §Errades del material publicat` · 2026-10-09

Fins al 2026-10-07, `13_contrib.qmd` tenia una capçalera buida, «Gestió d'errades», i el `TODO.md` en tenia l'entrada «Gestió d'errades post-commit: definir protocol». Decisió de l'usuari (2026-10-09): «Si tens una proposta clara, aplica-la. Si no, elimina l'entrada». La proposta de Claude Code és la mínima que encaixa amb el que ja hi havia: les *issues* de GitLab per informar-ne, perquè no cal ser membre del grup per veure-les i deixen rastre; la correcció pel camí de qualsevol canvi (la branca `fix/` de §Convenció de noms de branques, o el push directe de l'editor, [D-59](#d-59)); i `Closes #n`, perquè GitLab tanqui la *issue* quan el commit arribi a `main`. Queden fora, perquè són decisions de política i no de procediment: si es publica una llista d'errades per als alumnes i com s'avisa d'una correcció un cop començades les classes. El 2026-10-09 el projecte no tenia cap etiqueta ni cap *issue* oberta (`glab api projects/7916/labels`). L'etiqueta `errada` (vermella, `#dc3545`, el vermell de la paleta de les fallades) la va crear Claude Code el mateix dia, amb l'autorització de l'usuari («Fes-ho»).

### D-98

**Fitxers orfes: `25_scripts/orfes.py`, a `make inventari` i al hook** · `13_contrib.qmd §Figures i material gràfic`, `§IA` · 2026-10-09

La mateixa petició de l'usuari que [D-68](#d-68) (2026-10-08). Proposta de Claude Code, acceptada el 2026-10-09: un script i no un agent, perquè és una comprovació mecànica. Un fitxer versionat és orfe si cap altre no en cita el nom o l'arrel; per a les figures, el criteri és el nom de la sortida del pre-render (`<arrel>__original`, `<arrel>__extern`), perquè el `.qmd` cita `auto_figs/…` i no el font; i un fotograma `_pas<k>` d'una figura dinàmica es consumeix si es consumeix la figura. No compten com a cites les del `TODO.md`, el seu arxiu, el registre i l'inventari, que citen fitxers retirats pel nom (regla 12 de les escombrades). Queden fora `conservats/`, la configuració de les eines (`.github/`, `.vscode/`, `.claude/`) i els PDF de referència. El 2026-10-09, abans de moure els conservats, en donava 15, exactament els conservats; després, cap. Limitació coneguda: una arrel que és un mot comú (`placeholder`, `orfes`) surt citada per altres textos i no es marca. Triga menys d'un segon, i per això el hook el passa a cada commit: si n'hi ha cap, avisa (no bloqueja) amb la pregunta de moure'l o esborrar-lo.

### D-103

**Comprovacions per nivells: `comprova.py`, el hook de Claude Code i els hooks de git** · `13_contrib.qmd §Comprovacions per nivells`, `§Verificació de l'entorn`, `§Renderitzar el projecte`, `§IA` · 2026-10-10

Petició de l'usuari (2026-10-09, literal): «En algun moment caldrà explicitar els protocols d'execució dels scripts generadors i de testeig. Penso que cal definir nivells (per exemple "commit menor", "commit major", "revisió estètica", "revisió de continguts", "refer llista de continguts") perquè tal com està ara em sembla que hi ha testos innecessaris (per exemple, no cal renderitzar quan només hi ha canvis a `TODO.md`)». I, en encarregar la fase: «Hi ha d'haver una opció per fer tots els testos. S'ha de documentar bé per als revisors i contribuidors.» La proposta és de Claude Code, i l'usuari la va acceptar el 2026-10-10 en tres respostes: «Recomanacions acceptades» (el nivell 1 sense render, el render complet als nivells 3 i 4 i la taula generada), «Totes les recomanacions acceptades, 1--7» (entre altres, que un WARNING aturi el commit i la memòria cau de RARS) i «1--3 confirmades» (l'ortografia, [D-105](#d-105)).

El nivell es dedueix dels fitxers canviats, amb una sola classificació, la de `25_scripts/comprova.py`, que també fan servir `orfes.py` i `escombrada.sh`: abans n'hi havia cinc llistes a mà en tres fitxers (dues al hook, dues a `orfes.py` i una a `escombrada.sh`), que no coincidien. La taula de nivells de la guia la genera l'script, de manera que no pot divergir del que fa el hook. Amb la classificació de `comprova.py`, dels últims 400 commits sense fusions fins a `d0490cd`, 53 haurien estat de nivell 0, 11 de nivell 1, 237 de nivell 2 (79 amb formes que afecten el PDF) i 99 de nivells 3 i 4 (`python3 25_scripts/comprova.py --historial 400 --des-de d0490cd`; una ruta que ja no existeix compta com a nivell 2). La proposta en donava cap de nivell 1: el prototip que ho mesurava comptava com a canviades les línies buides de la sortida de git, i el mateix error es va repetir a la primera versió de `--historial`, fins que l'`auditor-xifres` no hi va trobar la diferència. El 2026-10-10, a `d0490cd`, `time make render` va trigar 88 s i `time make render-complet`, 277 s. El nivell 1, sense render, és per a les correccions de prosa, com les de les errades del material publicat ([D-96](#d-96)), i per als canvis de codi dins d'un bloc que no porten marcatge: el render no els interpreta, i els dels laboratoris els comprova RARS. Als nivells 3 i 4, el hook fa el render complet: les figures i la configuració són on el PDF es trenca sense que l'HTML ho mostri. Al 2, l'avís de PDF continua.

**El render ha d'acabar net**, també sense cap WARNING de Quarto: el 2026-10-10 no n'hi havia cap (`make comprova-tot`, comprovació «Render»). Com a conseqüència, deixa de valer la regla de §Verificació de l'entorn que permetia referències sense resoldre cap a elements encara no creats: una referència així s'escriu com a text, amb el comentari HTML.

**El hook d'abans del commit crida `comprova.py`**, i les quatre comprovacions que no s'executaven soles (el format del codi, les taules del PDF, el `--comprova` del glossari i el dels SVG de model (a), que la guia i les skills citaven com a ordres a mà, l'última com a `make comprova-figures`) passen a cada commit: cap no triga més d'un segon (`python3 25_scripts/comprova.py -v` en dona el temps de cadascuna). Els avisos continuen sense aturar ni preguntar ([D-61](#d-61)). Al comentari del hook i al missatge de `722c522` hi deia que el flux ja feia `make render-complet` abans de cada push, i citaven `CLAUDE.md §Flux de treball`. `CLAUDE.md` no ha tingut mai aquesta regla: `git log -S'render-complet' -- CLAUDE.md` en dona tres commits (`e3a7cc3`, `41ce419`, `de004da`), i la menció és sempre la de la fila de la fase 1 del pla de treball. D-61 en conserva el raonament de l'usuari; des d'aquesta decisió, el render complet dels nivells 3 i 4 el fa el hook.

**Hooks de git opcionals** (`.githooks/`, `make instal·la-hooks`), per a qui no fa servir Claude Code: el `pre-commit` passa les comprovacions sense el render, i el `pre-push`, les de la branca amb el render. L'usuari ho va acceptar amb una observació, literal: «Recomanació acceptada, però atenció pq l'upc no té runners. Hauria de comprovar si els puc aportar jo des del meu server si l'esforç d'aprender a fer-ho i de manteniment queden justificats (em sembla que amb github queda cobert)». La CI de les branques al mirall de GitHub és una tasca pendent (`TODO.md`).

**Bloqueig dels renders**: dos renders del mateix *worktree* no es poden fer alhora, perquè el pre-render esborra `auto_figs/`. `flock` als objectius de render del `Makefile`, amb el fitxer al directori de git del *worktree*: el segon espera fins a 15 min. No cobreix `quarto render` cridat directament ni la previsualització de VS Code. Les sessions de Claude Code que treballen alhora, cadascuna al seu *worktree* (`CLAUDE.md`).

**RARS**: proposta de l'usuari (2026-10-10, literal): «l'script comprova si RARS està a la màquina o al directori del repo i, si no hi és, el baixa d'internet i hi fa els canvis necessaris perquè es pugui executar. Si Java Runtime Environment (JRE) version 1.6 o superior no està instal·lat es genera un WARNING.» Amb dos ajustos: el `.jar` va a la memòria cau de l'usuari (`~/.cache/ec/`), fora de l'arbre, perquè [D-62](#d-62) no el vol al directori del repositori; i el Java que demana RARS 1.6 és el 8 o posterior (1.6 és la versió de RARS). Fins llavors, `verifica_laboratoris.py` buscava el `.jar` en una ruta fixa de la màquina de l'editor i, si el trobava, sortia amb 0 fos quin fos el resultat.

### D-104

**Registres: una sola política, i les durades en rangs** · `13_contrib.qmd §Comprovacions per nivells`, `§Figures i material gràfic`, `§Fitxer de referència tècnica` · 2026-10-10

Petició de l'usuari (2026-10-10, literal): «Cal fer un inventari de tots els registres que hi ha, comptant-hi el de l'índex continguts de l'HTML; optimitzar-ne la quantitat: una única font de veritat, fusions, eliminació dels irrellevants, etc.; fer scripts d'actualització dels registres preservats; definir una política d'actualitzció d'aquests registres; una de sola si el consum de temps no és significatiu». La proposta de Claude Code els va repassar un per un. Com que regenerar-los tots triga menys d'un segon (`comprova.py -v`, comprovació «Registres»), la política és una de sola, i els `--comprova` passen a cada commit. El model és l'índex «📑 Continguts», que es genera en renderitzar i no es versiona ([D-101](#d-101)).

Què va canviar:

- **L'inventari de figures** (`24_specs/figures.md`, versionat en 37 commits) es genera a demanda, en un fitxer que git ignora. Portava números de línia, que canvien a cada edició, i el 2026-10-10 ja no era al dia: la capçalera deia `7983a87`, i fins a `d0490cd` hi havia set commits més que tocaven `.qmd` o figures (`git log --oneline 7983a87..d0490cd -- '*.qmd' 22_figs_originals 23_figs_externes 24_specs/registres.toml | wc -l`). Els avisos passen a ser una comprovació de cada commit. En fer-ho, es va veure que no reconeixia cap figura «extreta de PDF» des que les arrels es van reanomenar de `T<N>_` a `A<N>_` ([D-76](#d-76)): el patró només acceptava `T…`. Ara les reconeix, les cinc de T6.
- **Les taules de la guia que una ordre pot donar s'eliminen**: la dels 46 fitxers de `21_riscv/` i la de les figures Graphviz. Les que tenen text que no es pot generar (les peces del render, el directori `.claude/`, els sufixos d'origen) es conserven, amb una comprovació que avisa si els falta o els sobra una fila.
- **Una sola llista de fitxers al `README.md`**: la taula de fitxers transversals i l'arbre de directoris, que no coincidien, es fusionen en l'arbre, amb una comprovació. Hi faltaven `figures_dinamiques.html` i `formules_en_linia.html`, i hi deia que `auto_riscv/` s'esborrava a cada render.
- **`dark_exclusions.txt` s'esborra**: no tenia cap patró, cap script no el llegia, i citava un nom antic de `gen_dark.py`. `orfes.py` no el veia perquè l'arbre del `README.md` cita tots els fitxers de l'arrel; ara les cites del README no compten.
- **Les ordres de `make`**: `make help`, generat dels comentaris del `Makefile`, en lloc de les dues còpies de la guia i del README.

**Les durades s'escriuen en rangs** (decisió de l'usuari, 2026-10-10, literal: «Converteix les infos precises a rangs [...]. Justificació: mantenibilitat (no volem que aquesta info sigui un registre pq llavors ha de ser tractat com a tal: script d'actulització, etc.)»). La guia, el README i el `Makefile` deien que `make render` trigava «segons», i n'eren 88; i el render complet, «~7 min» la guia i el README, i «~5 min aquí, ~7 al CI» el `Makefile`: en local, 277 s.

### D-105

**Ortografia amb `hunspell`, i les formes que no s'han de fer servir, comprovades** · `13_contrib.qmd §Comprovacions per nivells`, `§Requisits previs` · 2026-10-10

Pregunta de l'usuari (2026-10-10): si un corrector local reduiria la dependència de Claude Code, i si valia la pena mantenir el diccionari de VS Code. Una prova sobre la prosa del corpus (`d0490cd`), amb `hunspell` (català i anglès) i amb LanguageTool 6.6, va trobar errors reals que la revisió interna no havia vist: «Descomposem» i «sil·lici» (A7), «diversos hosts» (A1, contra [D-88](#d-88)) i calcs com «resulten en» o «consisteix en lliurar». Proposta de Claude Code, acceptada («1--3 confirmades»):

- **`hunspell`, a cada commit, sobre les línies afegides**: només avisa, perquè un mot desconegut també pot ser un mot legítim que cal afegir al diccionari. Si no hi ha `hunspell`, la comprovació surt com a omesa.
- **Un sol diccionari del projecte**, `24_specs/diccionari.txt`, que llegeixen el corrector de VS Code i `hunspell`. Abans era la clau `cSpell.words` de `.vscode/settings.json`. Dels 131 mots que tenia a `d0490cd`, dos amagaven formes no normatives, «indenta» i «indentació», que l'usuari va treure el mateix dia (`2a3d595`); i dels 129 que hi van quedar, deu no els feia servir cap fitxer, sense comptar el `TODO.md`, el seu arxiu i el registre, que documenten casos (els de MIPS, entre altres).
- **Les formes que no s'han de fer servir** es llegeixen de la taula de la guia i aturen el commit: són les formes exactes de la taula (amb el plural, el femení o la conjugació), i el 2026-10-10 no en donaven cap al corpus, fora de la guia, que les cita. És la manera de reduir la dependència del model: mecanitzar les regles de la guia que ja són mecàniques.
- **LanguageTool**, opcional i a demanda, en un bloc posterior: el zip de la versió 6.6 fa 252 MB, el seu `README.md` demana Java 17 o posterior, i sense configurar fa molt de soroll (`TODO.md`).

**Seguiment del 2026-10-10, al vespre: LanguageTool, integrat** (fase 12). Petició de l'usuari, literal: «Conserva el `languagetool-commandline.jar` al `.cache/`, posa `.cache/` al `.gitignore`, modifica l'script pertinent per la instal·lació del LanguageTool com has fet amb el RARS amb les mateixes polítiques, introdueix el LanguageTool al sistema de tes i documenta'n l'ús al README, si correspon; documenta que cal manternir a ma, on correspongui». `25_scripts/gramatica.py` fa amb LanguageTool el que `verifica_laboratoris.py` fa amb RARS ([D-62](#d-62)): el busca a `--lt`, a `LANGUAGETOOL_DIR` i a `~/.cache/ec/`, i si no hi és, el baixa, en comprova el sha256 i el descomprimeix, fora de l'arbre; sense Java 17, la comprovació surt com a omesa. languagetool.org no publica cap suma: el sha256 és el de la baixada del 2026-10-10. `.cache/` al `.gitignore` només cobreix el cas que `XDG_CACHE_HOME` apunti dins del clon. Tres decisions de Claude Code, a partir de la passada sobre el corpus:

- **Una sola execució de Java per a tots els fitxers**, amb un paràgraf del font per paràgraf del text: el corpus sencer, en uns segons (17 s el 2026-10-10, multifil), contra uns minuts amb una execució per fitxer.
- **A `make comprova-tot` i a `make gramatica`, no a cada commit**, com deia aquesta decisió («opcional i a demanda»): la primera vegada baixa uns 250 MB, i la gramàtica no té l'urgència de les formes que atura `lint_prosa.py`.
- **El soroll, a `24_specs/gramatica.toml`, a mà i sense xifres** (les dona `gramatica.py --resum`): de les 1 829 coincidències de la primera passada (`2a3d595`), 681 només tocaven el marcador, i la resta eren errors (corregits a la fase 12) o soroll, que s'hi desactiva regla a regla o forma a forma, amb el perquè. `MORFOLOGIK_RULE_CA_ES`, l'ortografia de LanguageTool, hi és desactivada: la fa `ortografia.py`, amb el diccionari del projecte. Les preferències d'estil, desactivades (decisió de l'usuari); COMMA_ADVERB, activa («Aplica COMMA_ADVERB»).

## Operació de les sessions

Els perquès de les regles de `CLAUDE.md`, que fins al 2026-10-07 hi eren al costat.

### D-63

**Una declaració de l'usuari no es verifica: es registra** · `CLAUDE.md §Flux de treball` · 2026-09-23 · `397c2da`

El cas: la fusió de les dues seccions d'estat de `CLAUDE.md` (2026-09-23) va descartar tres declaracions del 2026-07-12 per «no verificables», i es van haver de recuperar de `git show 397c2da:CLAUDE.md`. Fins al 2026-10-07 la regla era dues vegades a `CLAUDE.md` (§Estat dels materials i §Flux de treball).

### D-64

**Fusió de prova abans de tocar un fitxer que una branca de revisió també toca** · `CLAUDE.md §Regles de la revisió externa` · 2026-10-01

El cas: `980434b` (2026-09-25) va afegir un conflicte a `.gitignore` amb `temes456` per no haver-la feta: `!preamble.tex` va caure just al costat del `.DS_Store` que hi afegia la branca, un fitxer que el `TODO.md` ja deia que la branca tocava (`TODO.md §Decisions obertes → Branques del remot`).

### D-65

**Harmonitzar abans que la revisió externa arribi a un fitxer** · `CLAUDE.md §Regles de la revisió externa` · 2026-10-01

Amb altres professors ja dins de la revisió, qualsevol canvi transversal té un cost de coordinació molt més alt. Per a T3, T4, T5, T6 i T8 això ja havia passat el 2026-10-01 (la revisió externa hi era en curs), i des del 2026-10-06 l'abast declarat és A1–A8 sencer.

**Suspesa fins al 2026-10-09 a la tarda** (declaració de l'usuari, 2026-10-08, literal: «fins demà a la tarda pots fer canvis a tots els fitxers. Els revisors externs ja s'adaptaran a aquests canvis.»). Ho va dir en respondre la proposta de Claude Code de revisar A1–A8 només amb informes, sense canvis. Durant la finestra s'apliquen a A1–A8 els canvis transversals pendents, sense coordinar-los abans; la comprovació de les branques (`git ls-remote`, fusió de prova) continua.

**Allargada fins al diumenge 2026-10-11** (declaració de l'usuari, 2026-10-09, literal: «La finestra s'allarga fins a diumenge 11 d'octubre»). La comprovació de les branques continua igual.

### D-91

**El passat del `TODO.md` va a un arxiu, literal** · `CLAUDE.md §Fitxers de referència obligatòria` i la capçalera del `TODO.md` i de `24_specs/arxiu_todo.md` · 2026-10-09

Petició de l'usuari (2026-10-09): «En algun moment, aviat, caldrà fer pruning dels fitxers operatius, tant de Claude com d'humans (`TODO.md`, `13_contrib.qmd`, etc.)». El `TODO.md` feia 207 kB: 128 kB d'entrades retirades i dades preservades, 14 kB d'historial dels recomptes, i la resta, les entrades vives, amb l'historial de les parts ja fetes. Una sessió nova el llegeix sencer abans de començar. Proposta de Claude Code, acceptada per l'usuari («Endavant»): les entrades retirades, les dades preservades, la mesura dels slugs, l'historial de la capçalera i el text d'abans de sis entrades vives que es retallen van a `24_specs/arxiu_todo.md`, **literals**. Moure-les sense reescriure-les fa que cap declaració de l'usuari no es perdi per construcció ([D-63](#d-63)), i es comprova línia a línia: cada línia que surt del `TODO.md` és a l'arxiu. L'historial dels recomptes no hi va: és el registre de canvis del fitxer mateix (`git log -p TODO.md`), i només hi surten títols d'entrades i xifres. Alternativa descartada: substituir les entrades retirades per un punter al darrer commit que les contenia, que és el que D-63 prohibeix (les tres declaracions del 2026-07-12 es van haver de recuperar amb `git show`). Dues invariants i dues decisions de l'usuari que eren vigents i només constaven en files retirades van passar al registre ([D-8](#d-8), [D-25](#d-25)), i en passar-les es va veure que una de les invariants ja no es complia. L'arxiu s'exclou de les escombrades i de l'avís de `make render-complet` del hook d'abans del commit, com el `TODO.md` i el registre.

## Historial de l'estat del projecte

Fins al 2026-10-07 era a `CLAUDE.md §Revisió interna`, §Estat dels materials i §Pla de treball. Les declaracions de l'usuari es conserven literals; el detall de cada tancament de tema és a l'arxiu del `TODO.md`, `24_specs/arxiu_todo.md` §Entrades retirades.

### Revisió interna

El contingut de teoria (T1–T9), laboratori (L1–L6) i solucions (S2–S8) es va generar abans de la revisió. **La revisió interna és tancada sencera**, per declaracions de l'usuari: teoria i laboratori el 2026-09-23, enunciats i solucions el 2026-10-01.

- **Teoria: tancada, T1–T9, el 2026-09-23** (declaracions de l'usuari, una per tema, al llarg del Bloc 4d). El tancament de cada tema —amb l'estat que tenia, el commit que el declarava i què en sobreviu— és a `24_specs/arxiu_todo.md` §Entrades retirades. Quatre casos hi van necessitar una decisió o una execució abans de tancar-se: **T5** (revisió declarada «parcial»: auditats els 29 ítems del seu registre, executats els tres que restaven), **T6** (S6 harmonitzada sencera a $V_{CC}$), **T7** (C3, l'enunciat truncat d'`exr-t7-assoc-multinivell`, reparat contra el PDF original) i **T9** (contradicció entre l'assumpte del commit i el registre, resolta per decisió a favor del registre).
- **Enunciats i solucions: tancats, `E1.qmd`–`E9.qmd` i `S1.qmd`–`S9.qmd`, el 2026-10-01.** Declaració de l'usuari, literal: «les revisions internes es poden donar per acabades». `E3.qmd` i `S3.qmd` ja hi constaven com a completats des del 2026-07-12 (`614f576`). ⚠️ Fins al 2026-10-01, `CLAUDE.md` deia que els altres setze fitxers eren «pendents d'un pas combinat», i des del juliol no era cert: la frase es va escriure el 2026-06-19 (`879f3e7`), quan els fitxers encara es deien `PE_Tx` i `PS_Tx`, i `614f576` només en va canviar els noms. Les revisions de tema de juliol ja eren A-E-S conjuntes: els nou registres declaren E<x> i S<x> com a abast (`git show a211bbf:TODO/T<x>_P_tasques.md`, al títol o a «Fitxers objectiu»), i els de T6 i T7 diuen literalment «pas combinat E6+S6» i «E7+S7 (adaptació + revisió pròpia)». La skill `/pas-combinat` (`980434b`), feta sobre aquella frase sense preguntar a l'historial, es va retirar amb ella.
- **Laboratori: tancat, `L1.qmd`–`L6.qmd`, el 2026-09-23** (declaracions de l'usuari, una per fitxer). Dos avisos que el tancament no esborra, perquè descriuen l'historial i seguiran despistant qui el llegeixi:
  - ⚠️ **`ca6c01a` es diu «L6 Fase B» però conté la Fase C sencera**: toca els quatre fitxers que el registre de L6 llistava com a modificats (`L6.qmd`, `A7.qmd`, `13_contrib.qmd` i el registre mateix), i s'hi verifiquen els ítems de Fase C (literals als `.space`, «farciment», l'exercici nou `s6_4_5`, la correcció d'`A7.qmd`). L'assumpte del commit enganya; el contingut, no.
  - ⚠️ **`3cae913` és l'únic commit de revisió que ha tocat mai `L4.qmd`**, i el seu assumpte diu que és *previ* a les passades finals. L'usuari les va donar per cobertes en tancar L4.

«Fase C executada» **no** volia dir «revisió interna acabada». Entre les dues hi havia les *passades finals*, i el tancament es declarava per separat per a les tres revisions —**pedagògica, tècnica i lingüística**—. Com es va tancar cada ítem és a `24_specs/arxiu_todo.md` §Entrades retirades → Executades («Passades finals pendents»), i la plantilla que feia les tres preguntes, a l'historial (`git show 980434b:26_prompts/Lx__revisio_interna__plantilla.md`).

Les capçaleres `##`–`####` de tots els `A1.qmd`–`A9.qmd` tenen etiqueta `{#sec-}` (estat que `CLAUDE.md` registrava com a «complet»; la mesura és a `24_specs/arxiu_todo.md` §Mesura dels slugs).

### Revisió externa

La revisió interna tancada és la **condició prèvia** de l'externa, que fan altres professors de l'assignatura.

- **T4, T5 i T6, a `temes456` (MR `!7`).** El grup de treball hi va revisar `A4.qmd`, `A5.qmd` i `A6.qmd` del 21 de juliol al 7 d'agost (11 commits). Una fusió de prova (2026-10-01) donava tres conflictes: `A4.qmd`, `A5.qmd` i `.gitignore`. **La MR es va tancar sense fusionar el 2026-10-01** (`pedro.martinez.ferrer`, 16:21; GitLab la marcava `cannot_be_merged`). Decisió de l'usuari (2026-10-01, al vespre, substituint la d'esperar el grup): **la fusió la fa una sessió de Claude Code**, amb l'aprovació de l'usuari de cada conflicte resolt abans del push. Fusionada el mateix dia: `451c3ef` (commit de fusió, autoria dels 11 commits conservada), seguida de `40396e8` (errades que portava la branca) i `454a82e` (marca dels termes anglesos, de les sigles i d'«A **EC**», restaurada per decisió de l'usuari). Les 10 anotacions de la branca van passar a marcadors a `main`.
- **T3, a `contingut/t3-traduccio` (MR `!5`, Pedro J. Martinez-Ferrer, 2026-07-06).** Un sol commit, amb rutes d'abans de la reorganització de directoris, que git no pot fusionar. El port a les rutes actuals l'havia de fer l'autor de la MR (decisió de l'usuari, 2026-10-01). **La MR es va tancar sense fusionar el 2026-10-01** (16:20, el mateix autor). Decisió de l'usuari (al vespre): **el port el fa una sessió de Claude Code**, hunk a hunk i amb `Co-authored-by` de l'autor. Portada el mateix dia: `ab48732`. Els vuit comentaris del revisor van ser marcadors a `main`; set es van resoldre el 2026-10-02 (fase 3b) i el vuitè, la «↔» d'`A3.qmd:322`, a la fase 4 (`0d7bd5c`).
- **T8, a `tema8` (MR `!8`, Adrià Armejach, 2026-10-05 i 06).** 32 commits sobre `A8.qmd`, `A9.qmd`, `E8.qmd`, `S8.qmd`, `13_contrib.qmd §T8` i les figures de T8 (`gen_T8.py`): el TLB passa al model de RISC-V. **Fusionada a `main` el 2026-10-06 per l'usuari, des del GitLab, sense conflictes: `80f8946`**, amb commit de fusió i sense *squash*. **La revisió és parcial**: la descripció de la MR diu «Canvis fets fins a la secció 8.7 (exclosa)», de manera que §Integració del TLB i la memòria cau encara no s'ha revisat. La branca es conserva, perquè el revisor hi pugui continuar.
- **La resta d'A1–A8 (T1, T2, T7 i el que queda de T8), i una segona volta de T3–T6.** Declaracions de l'usuari (2026-10-06): la revisió externa afecta, de moment, **A1–A8**, «també T3--T6»; **A9, Ex, Sx i Ly en queden fora** de moment, i **les branques les crea cada equip**. Text literal: «de moment, la revisió externa només afecta A1--A8. A9 de moment n'ha quedat fora i també Ex, Sx i Ly»; «Inclou també T3--T6»; «Les branches de revisió les crearà cada equip de revisió» (fins al 2026-10-09, el literal només era al `TODO.md`, §Decisions obertes → Branques del remot; el text sencer d'aquella entrada és a `24_specs/arxiu_todo.md`). El mateix dia no hi havia cap revisor extern actiu ni cap branca d'equip a `origin` (`git ls-remote --heads origin`: `main`, `tema8`, ja dins de `main`, `temes456` i `contingut/t3-traduccio`).

### Fases del pla de treball

El pla es va refer el 2026-10-01 sobre l'inventari del grup de treball de T4–T6 (`TODO.md §Decisions obertes → Anotacions de la revisió externa de T4–T6`, avui a l'arxiu, `24_specs/arxiu_todo.md` §Entrades retirades), i va substituir el del matí del mateix dia, en què la línia 1 era «esperar el grup de treball». Les fases 1 i 2 anaven abans que les altres perquè, mentre la revisió de T3–T6 no fos a `main`, cada canvi que hi entrés era un conflicte més. Les harmonitzacions de la línia 2 de l'antic pla fora d'A3–A6 es van fer el 2026-10-01 (`24_specs/arxiu_todo.md` §Entrades retirades). Descripció de cada fase feta, tal com era a `CLAUDE.md`:

- **1. Integració de la revisió externa** (decisions de l'usuari, 2026-10-01). Fusionar `temes456` amb un commit de fusió, sense *rebase*, per conservar l'autoria dels 11 commits, i resoldre els 3 conflictes (`A4.qmd`, `A5.qmd`, `.gitignore`) conservant alhora els canvis dels revisors i les harmonitzacions de `main`. Portar `!5` a `A3.qmd` i `21_riscv/` hunk a hunk, amb `Co-authored-by` de l'autor. Abans del push, presentar a l'usuari la resolució de cada conflicte i els casos dubtosos del port. Registrar al `TODO.md` les 10 anotacions [br] i fer `make render-complet`. ✅ Feta el 2026-10-01: `temes456` fusionada (`451c3ef`, `40396e8`, `454a82e`), `!5` portada (`ab48732`), anotacions de totes dues registrades i `make render-complet` net.
- **2. Harmonitzacions pendents a A3–A6**: tornar a passar totes les escombrades del 2026-10-01 (la branca porta text d'abans): cometes (`A4.qmd:119`), «precisió simple» al material de T5, «l'X següent», amplada dels hexadecimals, tanques i quatre formats a A3; la regla d'`AND`/`OR` (decisió de l'usuari, `13_contrib.qmd §Codi, matemàtiques i cursiva`), i la convenció de l'anotació #4 (algorismes, blocs «Pseudocodi»), escrita i aplicada als títols; la cursiva dels algorismes, a la fase 4. ✅ Feta el 2026-10-01 (`d50b0ba`, `2693ec3`, `f066a8e` i el format U a T2).
- **3. Estructura pedagògica**: anotacions #12 (reordenar §Potència), #9 (temps i rendiment a §Definicions) i #3 (moure `#cau-sobreeiximent-extensio-m`). ✅ Feta el 2026-10-01 (`4759902`, `457e9cd`, `666835c`): les tres resoltes i els cinc marcadors esborrats; l'ampliació de #12 va quedar a la fase 6.
- **3b. Revisió externa de T3** (afegida el 2026-10-02): valorar i resoldre els set comentaris de contingut de Pedro J. Martinez-Ferrer. ✅ Feta el 2026-10-02 (decisions de l'usuari, a proposta de Claude Code; de `fec6d95` a `4a5cad5`): criteri de traduccions literals, «enter»/«natural» amb escombrada i regla a `13_contrib.qmd`, `slli` per a vectors i matrius, «NOT», fusió dels callouts *lazy*, bucles `while` → `do-while` → `for` i `.global` fora de T3. La «↔» (`A3.qmd:322`) va quedar a la fase 4.
- **4. Una sola passada de render** (HTML clar i fosc, i PDF): anotacions #7, #8, #10 i #11, la cursiva dels algorismes al PDF (#4), la «↔» d'`A3.qmd:327` i la figura de `#nte-instruccions-tipus` d'A2, que mostrava els set formats en lloc de R, I i S (`TODO.md §T2`, avui a l'arxiu, `24_specs/arxiu_todo.md` §Entrades retirades). ✅ Feta el 2026-10-02 (`0d7bd5c`, `e532380`, `70865b6`, `c450782`): #8 verificada sense canvi, #11 partida, cursiva fora (`preamble.tex`), «↔» → «LSb». #7, #10 i la figura d'A2 ja no eren de render: SVG retocats i una variant a `gen_regs.py` (`COMPENDIS`), fets amb Opus per decisió de l'usuari.
- **5. Figures** #1 i #2 (*half-adder*, *full-adder*, cadena amb XOR), en SVG natiu segons `24_specs/svg.md`. ✅ Feta el 2026-10-03 (`e49c014`, `184832c` i el commit de la #2): `#fig-semisumador-sumador-complet` i `#fig-sumador-propagacio-rossec`, generades per `25_scripts/gen_T4_sumador.py`, i la convenció de portes a `svg.md §16`. De pas, decisions de l'usuari: *carry* → «ròssec» a tot el corpus, i «semisumador» i «sumador complet», pendents de confirmar al Termcat.
- **6. Decisions per als revisors**: #5 R4-TYPE, #6 R5-TYPE i l'ampliació de #12. ✅ Feta el 2026-10-02 (decisions de l'usuari, a proposta de Claude Code): #6, no (`1ca023a`); #5, sí, com a aprofundiment (`0fb688a`); ampliació de #12, sí, com a aprofundiment (`99be9b8`). En analitzar #5 es va trobar l'errada de la figura de `#nte-instruccions-tipus` d'A2, que va anar a la fase 4.
- **7. Símbols i notació** (`12_sigles_simbols.qmd`), després de les fases 1 i 2, perquè llegeix A3–A6. ✅ Feta el 2026-10-03 (decisions de l'usuari, a proposta de Claude Code; de `a5340f3` a `d61a848`): CPI i la resta de sigles dins de fórmules amb `\text{}`; S6 i E6 amb la notació d'A6 (guany, Amdahl, potència); una sola notació per a la divisió de T4; el glossari verificat contra el corpus (Símbols 100 → 109 files, Notació 17 → 27), i les excepcions de subíndexs i de taules ISA escrites a `13_contrib.qmd`. Toca A3–A6 (notació, i una correcció a A5), cosa que el grup de revisió ha de saber. En van sortir dues entrades del `TODO.md`: «guany» per *speedup* a E6 i S6 (fase 7b), i VPN i PPN a Sigles (decidida el mateix dia, `8e19383`).
- **7b. Neteja prèvia a la revisió externa de la resta** (afegida el 2026-10-03): tancar els pendents dels fitxers que entraran a la fase 8, perquè cap revisor no hi trobi marcadors ni incoherències. A2: verificar la taula de restriccions d'alineació contra l'ABI `ilp32`, unificar el format de les taules de pseudoinstruccions i la taula de `#tip-codificacio-instruccions`, que sortia del callout al PDF. E6, S6 i `S_criteris_seleccio.qmd`: «guany» per *speedup*. L2: decidir l'alineació de `.dword` a RARS. Format del codi: aplicar el que decidís la reunió del grup de treball del 2026-10-05 (consens i alineació dels operands, `TODO.md §Decisions obertes` → «Criteris de codi C»). Ja fet el 2026-10-03, abans d'obrir-la: Load/Store/Branch → Lectura/Escriptura/Salt (`9a292eb`), VPN i PPN (`8e19383`) i el *checker* de format amb la indentació (`c27c68a`). ✅ Feta el 2026-10-03, excepte el format del codi, que esperava la reunió (decisions de l'usuari, a proposta de Claude Code; de `5684c8a` a `a7876b9`): la taula d'alineació, correcta, amb l'alineació dels punters i el límit de la relaxació de `sp`; `.dword` a RARS, que només s'alinea a 4 (error d'A2), i L2 amb una sola solució i `.align 3`; `la` amb taula i al compendi; la taula de codificació, dins del callout; «guany» a E6, S6 i `S_criteris_seleccio.qmd`; i el literal de `.dword` d'E2 i S2, que RARS llegia amb signe. ✅ El format del codi, fet el 2026-10-06 (decisió de l'usuari, perquè la reunió no ho va tractar; `0e25c9f` i el commit següent): operands a la columna 16 (F5) al callout `#imp-codi-format-criteris`, el format no s'avalua per si mateix, i 849 línies reformatades a A1–A3, A5, A9, E2–E4, E8, S2, S4, S5 i L2–L6. Toca A3 i A6 (una frase i una cursiva), cosa que el grup de revisió ha de saber. En van sortir quatre entrades del `TODO.md`: l'opció B de les pseudoinstruccions, les etiquetes dins dels `#nte-`, la distribució de columnes de totes les taules i `auipc` al compendi.
- **7c. Figures** (afegida el 2026-10-03): la revisió general de les figures de `TODO.md §Tasques transversals` («Revisió general de les figures i generació per script», detallada a `608a71f`: inventari, integració, model de generació, pilot de T7 i figures dinàmiques), amb les pendents de T7 i T8, les taules de memòria de T2 i el gris del text de figura. ✅ Feta del 2026-10-03 al 2026-10-06 (decisions de l'usuari 1–13, a proposta de Claude Code; de `1f5f006` a `e806916`, en dotze blocs): inventari de figures pel contingut (`make inventari`), 29 fitxers orfes retirats, generadors al pre-render (`__BA`, `__subrutina`, `__MC`, `__memoria`) i de model (a) amb `--comprova` (`gen_T4_sumador.py`, `gen_T7.py`, `gen_T8.py`), totes les figures de T7 i T8 en SVG natiu, figures dinàmiques a l'HTML, les taules de memòria de T2, text alternatiu des del `<desc>`, una mida comuna a l'HTML i una remissió a cada figura del cos del text. Toca A3–A6 (remissions i, a A3, figures), cosa que el grup de revisió ha de saber. ✅ Les dues entrades noves, fetes el 2026-10-06 (decisions de l'usuari D1–D8, a proposta de Claude Code; `d59ae41`, `c7180d9`, `77e6bce` i `42ac228`): les tres taules de MC de T7, de `gen_MC.py` (estil `estat`), amb els originals retirats; els colors fora de la paleta, migrats, i `#e6f1fb` i `#dee2e6`, afegits a `svg.md §10`; les figures de T6, sense `textLength` i amb la notació d'A6; i la resta d'avisos de l'inventari. Toca SVG de T3–T6 i A2, A7 i A9; declaració de l'usuari (2026-10-06): ara mateix no hi ha cap revisor extern actiu. En van sortir dues entrades del `TODO.md`: la revisió de la paleta per reduir-ne els colors i el ✓ que no surt al PDF.
- **7d. Tasques independents dels equips de revisió** (afegida el 2026-10-06, continuació de la 7c, amb les declaracions de l'usuari del mateix dia sobre l'abast A1–A8 i les branques per equip). ✅ Feta del 2026-10-06 al 2026-10-07 (recomanacions de Claude Code acceptades per l'usuari, i les decisions puntuals que no cobrien; de `82e7c99` a `35be646` i el commit del bloc 5), en sis blocs: (0) registre de l'abast i neteja del `TODO.md`; (1) A1–A8, abans que els equips en parteixin: la freqüència de sostre d'A6, com la d'A7 i datada cap al 2003–2005, i `auipc` presentada a A2, amb fragment de `21_riscv/` i taula al compendi (de pas, una errada tècnica d'A3 sobre l'expansió de `la`); (2) render: ✓ i DejaVu Sans Mono al PDF, imatges centrades als callouts, fórmules en línia alineades a l'HTML, marcadors del PDF amb els títols curts i hash del commit a la data; (3) A9, Ex, Sx i Ly: «d'arrencada en fred» en lloc de *cold-start*, la taula de T1 de `S_criteris_seleccio.qmd` i el bloc no autònom deduït a `verifica_laboratoris.py`; (4) les 296 taules del PDF verificades amb una eina nova, `verifica_taules.py`, i 52 corregides; (5) `codi_erroni` a `13_contrib.qmd`, la taula de figures externes (la foto de T7 és CC0 1.0, no CC BY-SA 2.0: `.bib` corregit) i el glossari anglès–català generat (`gen_glossari.py`). Abans de cada bloc que tocava A1–A8, `git ls-remote --heads origin`: cap branca d'equip. Toca A1–A6, A9 i el compendi, cosa que els equips han de saber. `TODO.md`: 33 → 23 entrades. Seguiment del 2026-10-07 (decisions de l'usuari sobre els pendents; `9f8e746` i el commit següent): «lectura/escriptura» per *load/store* a tot el corpus (69 substitucions en 16 fitxers), els glifs que faltaven al PDF (`\newunicodechar`), les marques `codi_erroni` d'A2, una sintaxi pròpia de RISC-V i RARS per als blocs `.s` (`24_specs/riscv.xml`), i la llista de llocs i solucions de l'HTML al mòbil. `TODO.md`: 23 → 21. Després, el mateix dia: «Solució» a les referències `@sol-` del PDF, les quatre correccions de l'amplada del mòbil (totes les pàgines a 375 px) i, al glossari, «farciment» i «multinucli» (`TODO.md`: 21 → 20).
- **7e. Partir `13_contrib.qmd`** (`TODO.md §Tasques globals → Eines`): les regles per a humans al capítol «Contribueix-hi», l'historial al registre de decisions i els procediments de Claude Code a skills; i aprimar `CLAUDE.md`. Acceptada per l'usuari el 2026-10-07 («Propostes acceptades: 1, 2 i 3»), a proposta de Claude Code, abans de la fase 8, perquè els revisors llegiran `13_contrib.qmd`. Inventari previ de cada paràgraf, acceptat per l'usuari amb les seves decisions: el nom i el format d'aquest registre i el criteri de què hi va; els casos de les regles de les skills, al costat de la regla; «Problemes» i «Solucions» (D-24); les fonts lèxiques per ordre (D-29); l'excepció del push de l'editor (D-59); §T9 «Mode S» reformulada (D-21); el web a `https://rbaig.github.io/migracio.ec.gitlab.upc.edu/`; i, durant la fase, `fifor1:`/`fifor2:` a L3 (D-6) i les figures sempre referenciades (D-44). ✅ Feta el 2026-10-07, en cinc commits (`f2c8ed2`, `924321a`, `c0f44b9`, `de004da` i el que retira l'entrada del `TODO.md`): `13_contrib.qmd`, de 1 408 a 1 038 línies (de 137 a 104 KB); `CLAUDE.md`, de 36,8 a 14,3 KB; aquest registre, amb 65 entrades i l'historial; quatre skills (`escombrada`, ampliada, `render`, `rars` i `figures`); i `README.md` sense els duplicats de la guia. Comprovació mecànica final: tots els fets de les línies tretes són en algun destí, tret dels descartats amb motiu, i cap frase llarga no és a dos fitxers. En surten tres entrades del `TODO.md`: Zifencei a T9, `Zicsr_pseudo_immediats.qmd` orfe i els usos d'«exercici» per a un problema.
- **7f. Pseudoinstruccions (opció B) i família de figures de memòria d'A3** (`TODO.md §Decisions obertes` i `§Tasques globals → SVG`): un sol esquema de columnes i un sol prefix de títol a les taules de pseudoinstruccions d'A2–A5 i del compendi; i el pla del generador de BA, amb un generador germà per a les piles i el mapa de memòria, la classe `estreta` i el `#cc0000` de les piles. Acceptada per l'usuari el 2026-10-07 («Propostes acceptades: 1, 2 i 3»), a proposta de Claude Code, per fer-la abans que els equips de revisió comencin. ✅ Feta el 2026-10-07 (decisions de l'usuari P1–P5 i F1–F8, a proposta de Claude Code), en dos commits. `75ea6c6`: l'esquema «Pseudoinstrucció, Operació, Expansió» a les 19 taules, amb «Condició» a `li`, i el prefix «Pseudoinstruccions —» (D-66), amb `fmv.s`, `csrr` i `csrw` fora de les taules ISA. El commit següent: `gen_mapa.py` (sufix `__mapa`, D-67) i `gen_BA.py` ampliat, amb les primitives compartides de `columna_memoria.py`; el mapa de memòria, les dues piles en fila i els BA de `func` i el general, generats; dos BA nous a les solucions de L3 i S3, en lloc de les taules, i les dues taules de desplaçaments d'A3, fora; la classe `estreta`, amb `w_rect` de 244 px; les vores de cada zona, per dins (`svg.md §7`), i un byte continu a cada extrem dels trams elidits (§4), després de revisar les figures; el `#cc0000` fora de les piles; `ba.toml` i `mc.toml` passen a `BA.toml` i `MC.toml`; i la conservació dels originals substituïts, escrita com a regla (D-68). Abans de cada bloc, `git ls-remote --heads origin`: cap branca d'equip. Toca A2–A5, A9, el compendi, L3 i S3, cosa que els equips han de saber. `TODO.md`: 24 → 23, amb tres entrades noves: els 23 títols de callouts `#nte-` amb un prefix de fora de la llista, l'escombrada d'«offset» i les vores compartides de la resta de figures.
- **7g. Control de qualitat fora de la revisió externa i petits pendents** (`TODO.md §Tasques transversals`, `§T4` i `§Tasques globals → Contingut global`): una passada tècnica i lingüística d'A9, els problemes, les solucions i el laboratori, que la revisió externa no cobreix (declaració de l'usuari, 2026-10-06), amb els subagents i els verificadors i la coherència amb la 7d i la 7f; l'slug `#sec-casos-especials` d'A4; i les línies partides dels blocs de codi al mòbil. Acceptada per l'usuari el 2026-10-07 («Propostes acceptades: 1, 2 i 3»), a proposta de Claude Code. ✅ Feta el 2026-10-08 (decisions de l'usuari 1–12 i ítems nous del mateix dia, a proposta de Claude Code), en nou commits: `ca02ad8`, l'slug, `#sec-casos-especials-divisio`; `753a74b`, la sagnia de continuació de les línies partides (de 2 500 línies mal alineades a 0 al mòbil); `bc478ba`, els blocs de codi del PDF, que ja no floten (D-69; de 588 a 569 pàgines), trobat perquè l'usuari no veia l'RSE d'A9; `f450bad`, `40bd0d6` i `210e6de`, les troballes de 34 informes dels subagents sobre `7a1640e`: totes les errades (A9, P3–P6, P8, S2–S8, L1, L2, L4–L6 i `index.qmd`, verificades amb Python i RARS 1.6; les fallades de L6, amb les classes del simulador), totes les harmonitzacions (veu dels enunciats i de les solucions, L/E, línies de MC a L6, la terminologia d'A8 a P8 i S8, els oracles a l'enunciat, «problema») i els suggeriments amb una proposta concreta, amb les regles noves D-70, D-71 i D-72; `8c009f9`, els ítems nous de l'usuari: `S_criteris_seleccio.qmd` retirat (D-73), el calendari només a l'HTML, amb un script, un agent i un pas del hook que el comproven (D-74), el projecte d'innovació docent a la llicència i l'autor de RARS al `.bib`; `6a17af1`, `02_problemes/` i `P1.qmd`–`P9.qmd` (D-75); i el de tancament (`060ab36`), amb dues regressions dels blocs anteriors (la concordança d'«el VPN» a S8 i una redundància d'A9). Abans de tocar A2, A3, A4 i `21_riscv/`, `git ls-remote --heads origin`: cap branca d'equip. Toca A2 i A3 (tres frases de «problema»), A4 (l'slug), `21_riscv/` (un fragment retirat, que no incloïa ningú), i el PDF sencer (D-69), cosa que els equips han de saber. `TODO.md`: 23 → 25, amb cinc entrades executades i set de noves: tres decisions que va demanar l'usuari (els fitxers orfes, els exemples i les solucions plegables i «el codi següent»), el calendari per confirmar, les possibles errades d'A1–A8, tres desajustos de la guia i del glossari, i 88 suggeriments sense proposta. **Seguiment del mateix dia, dins de la finestra de canvis** (declaració de l'usuari: «fins demà a la tarda pots fer canvis a tots els fitxers»; D-65, suspesa fins al 2026-10-09 a la tarda), en quatre commits i el de tancament: `03e3d7c`, les possibles errades d'A1–A8 i la frase d'A3 de les capçaleres alternatives; `63cb6e2`, els 21 títols `#nte-` amb un prefix de la llista; `3cc5dd0`, «offset» a A2, A3, A7, S7 i tres figures de T7 (37 de 110); i `18a94aa`, els noms de les figures pel fitxer que les consumeix (D-76). Abans, `git ls-remote --heads origin`: cap branca d'equip. Toca A1–A9, el compendi, S3, S5, S7–S9, L3 i les figures, cosa que els equips han de saber. `TODO.md`: 25 → 22. Fases noves al pla: 7h (vores de les figures), 7i (els suggeriments i la guia) i 8a (revisió d'A1–A8 amb canvis, abans que els equips comencin).
- **7h. Vores compartides de la resta de figures** (`TODO.md §Tasques globals → SVG`): 54 figures amb dues vores que comparteixen el traç (`svg.md §7`), als generadors i als SVG natius. Acceptada per l'usuari el 2026-10-08, a proposta de Claude Code. ✅ Feta el 2026-10-09 (Opus, effort alt; un commit), amb la decisió de l'usuari sobre els originals conservats (opció (a): no es toquen, [D-68](#d-68)): la regla de §7, generalitzada a qualsevol parell de zones que es toquen ([D-99](#d-99)), i `vores_compartides()` a `25_scripts/figlib.py`, que la fan servir `gen_regs.py`, `gen_MC.py`, `gen_T7.py` i `gen_T8.py`; els 9 natius, amb la funció aplicada un cop; dos ressalts de `gen_T8.py` que el marc següent tapava a mitges, i el tram blau d'`A9_cicle_interrupcio`, que entrava 10 px dins del verd. Les 44 figures consumides canvien (amb els fotogrames de les dinàmiques), i cap altra. Verificat comparant cada família abans i després, amb `make comprova-figures`, `make inventari` i un `make render-complet`, amb les figures mirades en clar i en fosc. Abans, `git ls-remote --heads origin`: cap branca d'equip; `contingut/t3-traduccio`, l'única que no és ancestre de `main`, no toca cap figura. Toca figures d'A2–A5, A7–A9 i del compendi, cosa que els equips han de saber. `TODO.md`: 19 → 19: surt l'entrada de la fase i n'entra una per als 12 originals conservats (no 10: la mesura de l'entrada excloïa els dos `…_passada` com si fossin fotogrames).
- **8a. Revisió tècnica i lingüística d'A1–A8, amb canvis** (proposta de Claude Code del 2026-10-08, acceptada per l'usuari el mateix dia, dins de la finestra de canvis de D-65: «fins demà a la tarda pots fer canvis a tots els fitxers»). Una passada com la de la 7g sobre `f1e67ec`, per trossos (subagents `auditor-xifres` fins que va caure pel límit setmanal d'Opus; la resta, la sessió principal), amb les troballes registrades al `TODO.md` abans d'aplicar-ne cap (`feb9183`, `f5b6124`). ✅ Feta el 2026-10-09 (decisions de l'usuari 1–11, a proposta de Claude Code), en quatre commits: `2b52382`, les errades (entre d'altres, la regla de sobreeiximent de la resta d'A1, les funcions que retornaven `short` o `char` sense estendre'n el signe a A3 i A4, la condició VIPT d'A8 i la figura del zoom al zero d'A5), amb `char` amb signe com a convenció d'EC i Zifencei fora de l'abast (D-77); `66b6cab`, les harmonitzacions, amb dues regles noves que s'apliquen a tot el corpus, les sigles sense plural (D-79) i l'article davant de les sigles segons la pronúncia (D-80), els comentaris d'una línia del C amb `//`, la barra de `imm[…]`, els punters cap endavant inscrits a la guia (D-78) i l'abast de les regles de §T5 i §T8 (D-81, D-82); `19b9913`, els suggeriments amb proposta; i el de tancament, `0bd83ea`. Verificat a cada bloc amb RARS 1.6 (els blocs `.s` que canviaven), els tres verificadors, `make comprova-figures` i un `make render-complet` amb els fragments nous cercats a l'HTML i al PDF i les figures mirades en clar i en fosc. Abans de cada bloc, `git ls-remote --heads origin`: cap branca d'equip. No es va fer la lectura lingüística frase a frase (decisió 11); al tancament, un `revisor-linguistic` (Sonnet) va revisar la prosa nova de la fase, i se'n van aplicar les correccions, entre les quals l'article davant de les sigles en negreta («la **ISA**»), que l'escombrada no havia vist. Toca A1–A8, el compendi, `21_riscv/`, el glossari, la guia, S5, S8, i, per les regles transversals, també A9 i els problemes, les solucions i el laboratori. **Seguiment del mateix dia, a petició de l'usuari**: les convencions noves del C (D-83) i del mode base + desplaçament (D-84), la de l'avaluació (D-85), l'article de RV32I, UNIX i NVIDIA (D-80), el títol `§IA` de la guia, els suggeriments que no tenien proposta, l'excepció dels prefixos (D-86) i la lectura lingüística frase a frase d'A1–A8 (sis subagents `revisor-linguistic`, Sonnet; se n'aplica el que és clar, i el que demana una decisió és al `TODO.md`; `5e55cc8`). I, al migdia, amb les decisions de l'usuari sobre el que quedava: el % i les unitats amb un espai que no es parteix (D-87, amb un filtre del render), l'article davant del codi (D-80), la regla de lèxic anglès/català (D-88: «amfitrió», *heap* i *target* en anglès, «la funció que crida» i «la funció cridada») i dos dubtes tècnics d'A1; les remissions `@lst-`, decidides, es deleguen a una sessió nova (`b71fa6b`; i `2d0bc11`, la lectura del compendi i la revisió de les correccions). I, a la tarda: les sigles, expandides només a la primera aparició del llibre (D-89; 24 expansions noves), la frase de la capacitat d'A6, la nota final d'`index.qmd` en una sola versió, què vol dir «Tx» (`index.qmd`, `README.md` i la guia) i el pilot de T1 dels exemples plegables i de la remissió de l'enunciat a la solució (D-90; `c29b58d`). `TODO.md`: de 23 entrades (a `f5b6124`, amb la de les troballes) a 22: se'n retiren dues, executades (Zifencei i les troballes), i hi entra «Fase 8a: el que queda de la revisió d'A1–A8».
