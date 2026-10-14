# Registre de decisions

El perquè de les regles del llibre. Les regles són a `13_contrib.qmd` (capítol «Contribueix-hi»), curtes i sense historial; cada regla que té entrada aquí hi enllaça amb el seu identificador.

**Format de cada entrada.** Un encapçalament que només porta l'identificador (`### D-n`), perquè GitLab i GitHub en facin la mateixa àncora (`#d-n`). A sota, una línia amb la decisió, on és la regla, la data i els commits; després, el perquè i les alternatives descartades. Un identificador no canvia mai: una entrada nova pren el número següent, encara que vagi a una secció anterior. Una regla nova o canviada de `13_contrib.qmd` porta la seva entrada, en el mateix commit. **Una entrada que canvia s'edita al lloc**: la línia de la decisió hi afegeix la data i el commit, i el text diu la regla d'avui, sense paràgrafs «Seguiment del…» ni «fins al … deia …»; el text d'abans és a git.

**Què hi va.** La decisió, el perquè, les alternatives descartades i qui ho va decidir. Una cita de l'usuari només hi va si fixa l'abast de la regla, i en prosa descriptiva. L'historial (com es va trobar un problema, les xifres d'una escombrada, el text d'abans) és a git ([D-122](#d-122)): l'etiqueta `arxiu/pre-neteja-2026-10-14` conserva aquest registre sencer, abans de compactar-lo. «L'usuari» és l'editor del llibre. Els commits són els que van escriure la regla a la guia (`git log -S` sobre `13_contrib.qmd`, que abans es deia `07_contrib.qmd` i `contrib.qmd`).

**Una entrada retirada** (substituïda per una altra, o sense regla vigent) es queda amb l'encapçalament i una sola línia: el títol, la data de la retirada i l'entrada que la substitueix, perquè les remissions continuïn resolent.

## Contingut

### D-1

**Precedència textual** · `13_contrib.qmd §Criteri general` · 2026-07-13 · `ccae7dd`

Es va escriure a la revisió interna de T8 com a «criteri general, aplicat aquí al bit `E`», dins de §T8. És la regla que va decidir la reescriptura dels bits `E` i `V` dels problemes heretats ([D-18](#d-18)). Des del 2026-10-07 és a §Criteri general, perquè no és pròpia de T8.

### D-2

**Les figures dels callouts del compendi, sense etiqueta ni peu** · `13_contrib.qmd §Fitxer de referència tècnica` · 2026-10-04 · `3bf711c`

Decisió de l'usuari (fase 7c, decisió 7, opció A, que incloïa les dues taules amb etiqueta dels `#nte-`): cap figura dels callouts `#nte-`, ni dels de `11_riscv.qmd` ni dels dels `Ax.qmd`, no porta etiqueta ni peu. Les quinze figures dels `#nte-` dels `Ax.qmd` que en portaven els van perdre.

### D-3

**Taules amb més d'un fragment font: fusió prèvia, fora del pre-render** · `13_contrib.qmd §Fitxer de referència tècnica` · 2026-07-08 · `e79d111`, `c5d9416`

Quarto no permet encadenar dos `{{< include >}}` consecutius dins la mateixa taula *pipe*: el primer tanca la taula i la resta cau a text cru (*line block* de Pandoc). D'aquí la fusió prèvia amb `25_scripts/gen_taules_auto.py`.

A diferència dels altres scripts de `25_scripts/`, aquest no es crida des del `pre-render` de `_quarto.yml`: Quarto resol els `{{< include >}}` dels capítols en un escaneig de configuració que s'executa *abans* del pre-render, de manera que el fitxer fusionat ha d'existir al disc abans d'invocar `quarto`.

### D-77

**Zifencei, fora de les extensions d'EC** · `13_contrib.qmd §Extensions RISC-V a EC` · 2026-10-09

Decisió de l'usuari, a proposta de Claude Code. La taula d'extensions situava Zifencei (`fence.i`) a T9, però cap fitxer de T9 no en parlava, cap bloc no portava el `filename` `RV32IZicsrZifencei`, i A2 (`#wrn-model-memoria-relaxat`) deixa `fence`, `fence.tso` i `fence.i` fora de l'abast. L'alternativa, presentar `fence.i` a A9, es va descartar.

### D-85

**Les convencions d'EC no penalitzen l'avaluació, tret que s'indiqui** · `13_contrib.qmd §Callouts` · 2026-10-09

Decisió de l'usuari (2026-10-09), en fixar les convencions de D-83 i D-84: no seguir les convencions d'EC no penalitza l'avaluació, tret que s'indiqui explícitament el contrari. Es diu una sola vegada, al primer callout `#imp-` dels apunts (`#imp-convencions-ec`, A1), i hi remet el criteri de format del codi d'A2 (`#imp-codi-format-criteris`), que ja deia que el format no s'avalua per si mateix.

### D-97

**«Laboratori 1», o L1: no «Sessió 1» ni «S1»** · `13_contrib.qmd §Ús d'aquesta guia` · 2026-10-09 · `d325f26`

Decisió de l'usuari: «Laboratori Y» i «LY» en lloc de «Sessió Y» i «SY», per simplificar la nomenclatura i perquè «S1» volia dir alhora la primera sessió del laboratori i les solucions del tema 1. Els títols curts de les parts són «A1», «P1», «S1» i «L1». Es queden com eren: «sessió» com a esdeveniment («abans de l'inici de la sessió»); els identificadors (`sessio1`, `#sec-sessio-*`), que no es veuen; els títols dels quaderns antics citats a `14_LICENSE.qmd` i al `.bib`; i els noms dels lliuraments (`s3_4_1.s`).

## Decisions per tema

### D-4

**`.globl`, no `.global`** · `13_contrib.qmd §T2 i T3` · 2026-10-02 · `4a5cad5`

Motiu: GCC genera `.globl` (verificat amb GCC 14.2, `gcc -S`), i RARS 1.6 assembla `.global` (verificat), de manera que l'estudiant només se'l trobarà en codi escrit a mà o d'altres arquitectures, com ARM. El text de T3 (`#nte-globl`) no l'esmenta: només el recull la taula de directives del compendi.

### D-5

**Quatre formats nuclears d'instrucció, i on es presenta cada un** · `13_contrib.qmd §T2 i T3` · 2026-10-01, 2026-10-12 · `b2530c7`, `5f2f1eb`, `363385e`

El criteri dels quatre formats nuclears és de la revisió interna de T2 (2026-07). On es presenta cada format, decisió de l'usuari (2026-10-01): R, I, S i U a T2, i B i J a T3; abans A2 ajornava el U a T3, i A3 presentava el J com a variant d'un U que encara no havia sortit. La figura de `#nte-instruccions-tipus` (A2) mostra tots els formats com a visió de conjunt, i és el text el que diu on es presenta cadascun (decisió de l'usuari, 2026-10-12, a proposta de Claude Code).

### D-6

**Etiquetes de bucle: el prefix `fi-`, i la numeració dels bucles germans** · `13_contrib.qmd §T2 i T3` · 2026-09-23, 2026-10-07 · `a507297`

El prefix de sortida `fi-` és la forma majoritària al corpus. Quan hi ha dos bucles al mateix bloc, les etiquetes es numeren (`fifor1:`, `fifor2:`), en lloc de renombrar-les a `for:`/`fifor:`, que hi duplicaria etiquetes i el fragment no assemblaria (decisió de l'usuari, 2026-09-23; la forma `fifor`, del 2026-10-07, segueix el prefix de la regla). Quan es va escriure, l'únic cas era la funció `moda` de la solució de `s3_4_2.s` (L3).

### D-7

**Alineació de la pila: el fet de l'ABI i el criteri d'EC, en dos callouts** · `13_contrib.qmd §T2 i T3` · 2026-10-04 · `552ff1a`

`#nte-abi-alineacio-pila` (el fet: l'ABI exigeix múltiples de 16) i `#imp-abi-alineacio-pila` (el criteri d'EC: múltiples de 4) es van separar el 2026-10-04, a petició de l'usuari.

### D-8

**`.section` no s'utilitza: RARS 1.6 no admet la forma llarga** · `13_contrib.qmd §T2 i T3` · 2026-09-23, 2026-09-24 · `6fcee2c`, `5514d08`

Verificat executant RARS 1.6 (2026-09-23; reproduït el 2026-10-14). La proposta de l'usuari era fer `.section` obligatòria a tots els fragments d'assemblador, i es va aturar en provar-la. `.section .data` i `.section .text` no assemblen: l'analitzador lèxic consumeix `.data` i `.text` com a directives pròpies, i cap grafia no ho salva. Les formes que assemblen fallen en silenci: `.section` no commuta de segment, i amb un nom reconegut (`.rodata`, `.sdata`) descarta tot el codi que la segueix, sense error ni avís. Per això `.section .foo`, que RARS no reconeix, és més segura que les que sí que reconeix.

| Forma | Assembla? | Què fa |
| :--- | :---: | :--- |
| `.section .data`, `.section .text` | No | Error: `.section must be followed by a section name` |
| `.section .rodata`, `.section .sdata` | Sí | No commuta de segment, i el codi que la segueix desapareix |
| `.section .bss`, `.section data`, `.section .foo` | Avís | `section name "X" is ignored`; l'assemblador es queda al segment on era |
| `.section .data.x`, `.section .text.trap, "ax"` | Sí | És la forma de l'exemple il·lustratiu d'A9 |

Com es reprodueix, amb el `.jar` de la skill `rars`:

```bash
printf '.section .data\nx: .word 1\n' > t1.s
java -jar rars1_6.jar nc t1.s          # .section must be followed by a section name
printf '.data\na: .word 0xAA\n.section .rodata\nb: .word 0xBB\n.text\n la t0,a\n la t1,b\n li a7,10\n ecall\n' > t2.s
java -jar rars1_6.jar nc t2.s t0 t1    # t0 = 0x10010000, t1 = 0x10010004: contigües, no ha commutat
printf '.text\n li t0,0x77\n.section .rodata\n li t1,0x88\n li a7,10\n ecall\n' > t3.s
java -jar rars1_6.jar nc a t3.s dump .text HexText /dev/stdout   # només 07700293: de quatre instruccions, una
java -jar rars1_6.jar nc a t3.s dump .data HexText /dev/stdout   # «has not been written to»: no són enlloc
printf '.section .bss\nx: .word 1\n' > t4.s
java -jar rars1_6.jar nc a t4.s        # avís, i «.word cannot appear in text segment»: es queda al de text
```

**On es presenta a teoria** (decisió de l'usuari, 2026-09-24): com a forma de GNU, al cos visible de `#nte-segments-memoria` (A2), on l'alumne aprèn què és una directiva de segment, i no a `#wrn-segments-elf`, que és plegat. **Invariant**: cap `.section` dins d'un bloc plegat d'`01_apunts/`, mesurat per forma (seguint la imbricació dels divs `:::`, cap línia amb `.section` no és dins d'un nivell obert amb `collapse`).

### D-84

**Mode base + desplaçament: l'operand, sempre `desplaçament(base)`** · `13_contrib.qmd §T2 i T3` · 2026-10-09

Decisió de l'usuari (2026-10-09). L'expansió de `ret` s'escrivia de dues maneres, `jalr x0, 0(ra)` i `jalr zero, ra, 0`, que RARS 1.6 codifica igual (`0x00008067`). La regla fixa la forma de les instruccions de lectura i escriptura, `desplaçament(base)`, també per a `jalr`, que és del mateix mode d'adreçament (A3, §Revisió dels modes d'adreçament), i el nom ABI del registre (`zero`, no `x0`), com la resta del codi del llibre. A2 la presenta a `#imp-notacio-base-desplacament`, just després de definir el mode.

### D-114

**Títols «C — »: només quan el contingut és només de C** · `13_contrib.qmd §T2 i T3` · 2026-10-13

Recomanació de Claude Code, acceptada per l'usuari, a partir dels títols de §Punters i §Vectors d'A2 que l'usuari havia harmonitzat a mà (`5aa5bc9`): «C — » quan la secció no té part en RV32I, també als títols dels callouts; i els fills d'una secció «C — » no el repeteixen. Un exemple amb part en RV32I (`#tip-desreferencia-punters-c`) no el porta.

### D-9

**Notació de la multiplicació i la divisió (T4)** · `13_contrib.qmd §T4` · 2026-10-03 · `e0ff377`

Fins al 2026-10-03, la divisió tenia tres notacions a A4 —$x$/$y$/$q$/$r$, $D$/$d$/$q$/$r$ i $x$/$y$/$z$/$w$—, i $D$ era el dividend mentre que el registre D és el divisor.

### D-10

**«Esbiaixat» / «biaix» per a l'exponent IEEE 754** · `13_contrib.qmd §T1 i T5` · 2026-07-05 · `6d48f87`

Font: Viquipèdia cat., «Format de coma flotant de precisió simple».

### D-11

**«Mantissa», no «significand»** · `13_contrib.qmd §T1 i T5` · 2026-07-07 · `47704cf`

L'IEEE 754 en anglès prefereix *significand* perquè *mantissa* ja té un sentit als logaritmes (Knuth en critica l'ús), però la distinció és interna a l'anglès: cap font catalana no la reflecteix (el Termcat només té «mantissa», i la Viquipèdia la fa servir com a terme principal). A EC, l'ambigüitat ja queda resolta amb la distinció entre **fracció** ($F$, els bits emmagatzemats) i **mantissa** ($1{,}F$, amb el bit ocult).

### D-12

**Fracció, mantissa i precisió (T5)** · `13_contrib.qmd §T5` · 2026-10-03 · `e0ff377`

Fins al 2026-10-03, `A5.qmd §Representació binària` donava $p$ bits a la fracció, i §Notació científica normalitzada deia $n$ a l'exponent.

### D-81

**Els blocs `.default` i l'exemple *half* de §T5 són dels problemes i les solucions** · `13_contrib.qmd §T5` · 2026-10-09

Decisió de l'usuari (2026-10-09), a proposta de Claude Code. La revisió tècnica d'A5 va preguntar si les dues regles obligaven també la teoria: A5 presenta els càlculs pas a pas IEEE 754 amb fórmules (`$$\begin{array}…$$`), no amb blocs `.default`, i l'exemple de no-associativitat d'A5 és de precisió simple. A5 no canvia; la guia ho diu.

### D-13

**Ordre dins de §Potència (T6)** · `13_contrib.qmd §T6` · 2026-10-01 · `666835c`

Anotació #12 de la revisió externa de T4–T6.

### D-14

**Rendiment vs. productivitat (T6)** · `13_contrib.qmd §T6` · 2026-10-01 · `666835c`

Anotació #9 de la revisió externa de T4–T6.

### D-15

**Guany, llei d'Amdahl i potència: la notació de la teoria a tot T6** · `13_contrib.qmd §T6` · 2026-10-03 · `ca98373`

Fins al 2026-10-03, S6 feia servir $S$, $S_{max}$, $f$ i $k$ a la llei d'Amdahl —amb $f$ alhora fracció i freqüència dins del mateix fitxer—, $P_{din}$, $P_{est}$ i $P_{tot}$, i P6 i S6, $F_A$ i $F_B$ ($F$ és la fracció a T5).

### D-16

**Etiquetes de classe d'instruccions en català** · `13_contrib.qmd §T6` · 2026-10-03 · `9a292eb`

Decisió de l'usuari (2026-10-03). Fins llavors P6 i S6 les tenien en anglès («Load», «Store», «Load/Store», «L/S», «Branch»), també en prosa («les branch 2 cicles»).

### D-17

**Tipus de fallades: «d'arrencada en fred», i «obligatòria» als llocs curts** · `13_contrib.qmd §T7` · 2026-10-04 · `703af35`, `eb1838b`

Decisió de l'usuari (2026-10-04), amb els termes del PDF original (T6, §8). Fins llavors A7 deia *cold-start* com a terme principal. La regla val per a tot el material, des del 2026-10-06 (recomanació de Claude Code, acceptada).

### D-18

**Bits `E` i `V` de la memòria virtual** · `13_contrib.qmd §T8` · 2026-06-14 · `d926f24`, `ccae7dd`

Quan un enunciat heretat usava `W` (`1` = només lectura, polaritat oposada), s'ha reescrit a `E`, aplicant el criteri de precedència textual ([D-1](#d-1)). Els enunciats i les solucions que usaven `P` (notació x86 i dels exàmens antics d'EC) per al bit de presència s'han reescrit a `V`, aplicant el mateix criteri.

### D-19

**Model del TLB: el de RISC-V, no el de MIPS** · `13_contrib.qmd §T8` · 2026-10-05 · `fc356d7`

Decisió de l'usuari (2026-10-05), a la revisió externa de T8 (MR `!8`, Adrià Armejach), que va passar P8, S8 i A9 al model de RISC-V del TLB. Fins llavors el model era el de MIPS (TLB arquitectònic, *refill* per programari, encert de TLB amb V = 0), que es conserva com a nota històrica a `#wrn-mv-tlb-hw-walker`.

### D-82

**L'ordre d'ús de l'estat inicial del TLB, amb el sentit explícit** · `13_contrib.qmd §T8` · 2026-10-09

Decisió de l'usuari (2026-10-09), a proposta de Claude Code. Fins llavors la regla deia «l'ordre d'ús (MRU→LRU)», i l'exemple d'A8 dona l'ordre «de més antic a més recent», amb el sentit explícit, mentre que P8 el dona de la més recent a la més antiga. No hi ha ambigüitat si el sentit és explícit: la regla demana el sentit, no en fixa cap. A8 no canvia.

### D-20

**L'exemple pràctic de T8, a la secció final del tema** · `13_contrib.qmd §T8` · 2026-10-06 · `1ddd351`

Decisió de l'usuari (2026-10-06): a la secció final, com la secció 7 del PDF original.

### D-119

**Excepció i interrupció: els termes anglesos, junts a T9** · `13_contrib.qmd §T9` i `§Anglicismes i terminologia obligatòria` · 2026-10-14

Proposta de l'usuari (2026-10-14): *exception* i *interrupt* es presenten junts a `#cau-terminologia` (A9), on es defineixen l'un al costat de l'altre, encara que l'excepció ja surti abans, a A2 (una excepció d'alineació de RARS, que hi queda sense l'anglès). L'usuari reconeix que trenca la regla de la primera aparició, i ho considera justificat. *Interrupt* i no *interruption*: és el terme de l'especificació de RISC-V i de Harris & Harris, i el que A9 ja fa servir als noms dels CSR i dels bits (*Machine Interrupt Enable*, el bit *Interrupt* de `mcause`). El glossari situa tots dos termes a T9.

### D-21

**Mode S a T9: la fallada de pàgina, no la de TLB** · `13_contrib.qmd §T9` · 2026-10-07 · `402ef7a`

Reformulada a proposta de Claude Code, acceptada per l'usuari. La regla anterior (2026-05-24) deia que el tractament de les fallades de TLB per programari requeria mode S, cobert per un aprofundiment, i era caducada per dues bandes: des del model de RISC-V del TLB ([D-19](#d-19)), la fallada de TLB la resol el maquinari i no és una excepció (`#cau-tlb-miss-excepcio`); i el mode S és al cos del text (`#sec-ei-tlb-modes`), no en cap aprofundiment.

## Problemes i solucions

### D-22

**Identificadors `#exr-t<N>-` i `#sol-t<N>-`** · `13_contrib.qmd §Problemes i solucions` · 2026-10-01 · `9dc02f6`, `1c9aae5`

Decisió de l'usuari (2026-10-01). Fins llavors el prefix era `p<N>-`, la numeració de les col·leccions MIPS, que en cinc temes no coincidia amb el tema (P2 i S2 feien servir `p3-`). Els enllaços externs a les àncores publicades amb el prefix antic van deixar de funcionar amb el canvi.

### D-23

**Etiqueta «Problema» o «Exercici» segons la part, i el «⁂» del PDF** · `13_contrib.qmd §Problemes i solucions` · 2026-10-01 · `229071c`

Decisió de l'usuari (2026-10-01). Al PDF, el mecanisme de «⁂» ve de dues formes més directes que es van provar i no funcionen: un bloc `crossref:` a la capçalera del fitxer substitueix la configuració de capítols que el llibre hi injecta (la numeració perd el capítol i les referències a capítols d'altres fitxers no resolen), i `\exercisename` escrit directament al prefix surt literal al PDF, perquè Quarto n'escapa la contrabarra. D'aquí el caràcter `⁂`, que no és a cap altre lloc del corpus. Com que una referència pren el nom de la part on és, una referència que creués parts diria el nom de la part d'origen; quan es va escriure, cap no ho feia.

### D-24

**«Problemes» i «Solucions»; «problema», i «exercici» només al laboratori** · `13_contrib.qmd §Problemes i solucions` · 2026-10-07

Decisió de l'usuari (2026-10-07), a proposta de Claude Code, per acabar amb un ús inconsistent («problemari», «solucionari», «enunciats», «exercicis»). «Problemari» no és al DIEC2, al Termcat ni a l'Optimot; «solucionari» és al Termcat, però el menú del llibre ja diu «Problemes» i «Solucions»; i als exàmens es diu «Problema 1», «Problema 2»… ([D-23](#d-23)). Pel mateix motiu, `02_exercicis/E<N>.qmd` va passar a `02_problemes/P<N>.qmd` (2026-10-08). El títol «Solucionari de la Col·lecció de Problemes» de `14_LICENSE.qmd` és el d'una obra i no es toca.

### D-73

**Selecció de solucions, sense taula de criteris** · `13_contrib.qmd §Problemes i solucions` · 2026-10-08

Decisió de l'usuari (2026-10-08), a proposta de Claude Code: es retira `03_solucions/S_criteris_seleccio.qmd`, una taula per tema dels problemes resolts amb la dificultat i el temari, i el criteri passa a la guia. Mantenir-la al dia era una feina sense lector: no era al dia, el criteri que donava («~1 resolt per cada 2–3») no es complia, i cap altre fitxer no feia servir l'escala de dificultat. Es recupera amb `git show 210e6de:03_solucions/S_criteris_seleccio.qmd`. Si es resolen tots els problemes (decisió de la reunió del 2 de novembre, `TODO.md`), aquesta regla canvia.

### D-75

**Directori `02_problemes/` i fitxers `P1.qmd`–`P9.qmd`** · Retirada el 2026-10-14: fet executat sense regla pròpia; el perquè és a [D-24](#d-24).

## Laboratori

### D-25

**El punt d'entrada no porta etiqueta** · `13_contrib.qmd §Convencions globals del laboratori` · 2026-09-24 · `b2c1a4f`, `5514d08`, `d6fb588`

Criteri de l'usuari (2026-09-23), que inverteix la convenció anterior (`_start` i `.globl _start`). Dos motius:

- **Cap agent no llegeix el nom del punt d'entrada.** En l'entorn autònom d'EC (`@sec-entorn-autonom-bare-metal`), l'execució comença a la primera instrucció de `.text`; a Linux, `_start` el resolen l'enllaçador i el carregador. És l'argument de `void main()` ([D-49](#d-49)): una etiqueta que ningú no resol és una ficció. Que RARS simuli crides al sistema no hi afecta: és sobre els serveis que el programa crida, no sobre qui el crida.
- **L'opció «start at main» (`sm`) de RARS només actua amb un `main` global.** Amb `.globl main`, el mateix fitxer s'executaria de dues maneres segons la casella de cada alumne; sense cap etiqueta global, la divergència desapareix. `_start` no hi rebia cap tracte especial: la convenció anterior era convenció pura. Verificat amb RARS 1.6 pel valor dels registres:

```bash
# prova.s:  li t0,111  /  main:  li t1,222  /  li a7,93  /  li a0,0  /  ecall
java -jar rars1_6.jar nc sm prova.s t0 t1   # t0=0x6f: sense .globl main, `sm` no fa res
# amb `.globl main` afegit:
java -jar rars1_6.jar nc sm prova.s t0 t1   # t0=0x00: comença a `main`
```

**Invariant**: als `.qmd` (sense el `TODO.md` ni la guia), cap definició `_start:` ni cap `.globl _start`, i `.globl` només per a un símbol que es fa servir des d'un altre fitxer (L5, §Compilació separada).

```bash
X=("--" "*.qmd" ":!TODO.md" ":!13_contrib.qmd")
git grep -hE "^_start:" "${X[@]}" | wc -l                 # 0
git grep -hE "^\s*\.globl" "${X[@]}"                      # suma, abs, descompon, g i X (2026-10-09)
git grep -hE "^\s*\.globl\s+_start" "${X[@]}" | wc -l     # 0
```

**L'ordre de la pestanya de RARS, avaluable** (decisió de l'usuari, 2026-09-24): el fet general és al cos visible de `#nte-segments-memoria` (A2), i l'ordre de la pestanya en assemblar diversos fitxers, a `@nte-rars-ordre-assemblatge` (L5), visible i avaluable, perquè és al camí normal de l'exercici i amb la pestanya dolenta el programa no arrenca.

### D-26

**Tres blocs del laboratori sense punt d'entrada** · `13_contrib.qmd §Convencions globals del laboratori` · 2026-09-24 · `b2c1a4f`

Són fitxers de subrutines que s'enllacen amb el fitxer que porta el programa principal. L'exempció ja constava quan la convenció exigia `_start`; amb [D-25](#d-25) ja no hi ha etiqueta que els falti, però la particularitat dels tres blocs es manté, perquè ningú no els «arregli».

### D-27

**Oracle a l'enunciat, tècnica a la solució** · `13_contrib.qmd §Convencions globals del laboratori` · 2026-09-21 · `cf2dd43`

- L'oracle va a l'enunciat perquè l'estudi previ es lliura **abans** de la sessió i hi haurà una versió del llibre sense solucions: un oracle dins d'un `{#sol-...}` és inabastable justament quan fa falta.
- La fixació d'una entrada va amb el resultat perquè un valor sense la seva precondició no és reproduïble.
- El callout de la tècnica se suprimeix si no té contingut propi perquè un callout que només existeix per no deixar el lloc buit és soroll.

### D-28

**`### Lliuraments` i `### Lectura prèvia`, de nivell 3** · `13_contrib.qmd §Ordre i atribut de seccions no numerades` · 2026-07-13 · `fe53cfc`

És un *dirty hack* per evitar que la capçalera de pàgina del PDF quedi fixada a «Lectura prèvia», efecte que sí que es produeix amb el nivell 2.

### D-125

**La sortida del programa, amb `exit2`; no es fa servir `startup.s`** · `13_contrib.qmd §Convencions globals del laboratori` · 2026-07-19 · `3843c5a`

Decisió de l'assignatura, de tots els professors (2026-07-19): el mecanisme `startup.s` (una rutina d'arrencada que crida `main` i, quan torna, fa la sortida) en queda exclòs, i el programa acaba amb `li a7, 93` + `ecall`. La regla ja era a la guia des de `3843c5a`; amb la decisió, A2 en va perdre els quatre blocs comentats, i E9 i S9 van passar a la mateixa sortida. És coherent amb [D-25](#d-25): ningú no crida el programa. El bolcat de RARS d'un programa amb `startup.s` i les dues versions del fitxer (la que presentava A2, i l'original de RARS, amb `__start` i el servei 10) només tenen valor si la decisió es reobre: `git show arxiu/pre-neteja-2026-10-14:24_specs/arxiu_todo.md`, §Dades preservades del bloc eliminat `A2.qmd:744-810`.

## Llenguatge

### D-29

**Fonts de correcció lèxica: DIEC2, Termcat i Optimot, per aquest ordre** · Retirada el 2026-10-14: substituïda per [D-116](#d-116).

### D-86

**Prefixos decimals: fora l'excepció de les referències de mercat d'A7** · `13_contrib.qmd §Criteris generals` · 2026-10-09

A proposta de la revisió tècnica d'A7, amb el permís de l'usuari. La regla reservava els prefixos decimals (KB, GB…) també per a «les referències de mercat aproximades» de `#sec-gap-memoria`, però en aquesta secció només hi ha amplades de banda, que ja eren a la regla, i «80 GiB», que és binari; les capacitats en GB i TB són a §Tecnologies, i les cobreix l'emmagatzematge secundari. L'excepció no cobria res.

### D-87

**Unitats i percentatges: un espai que no es parteix** · `13_contrib.qmd §Criteris generals` · 2026-10-09

Decisió de l'usuari (2026-10-09): un espai entre el nombre i el %, com demana l'Optimot, i el mateix per a totes les unitats de mesura, que ja el portaven («32 bits»). Els atributs d'amplada (`width: 80%`) no hi entren. Perquè l'espai no es parteixi sense omplir el font de marques, el posa un filtre del render (`espai_unitats.lua`), amb la llista d'unitats.

### D-88

**Terme català o anglès: l'Optimot i Softcatalà, i les excepcions documentades** · Retirada el 2026-10-14: substituïda per [D-116](#d-116).

### D-30

**Amplada dels hexadecimals** · `13_contrib.qmd §Criteris generals` · 2026-10-01 · `7d78615`, `171cf18`, `06f0c0c`

Decisió de l'usuari (2026-10-01). L'excepció del format reduït té dos casos, `exr-t7-fallades-programa` i `exr-t8-mv-proteccio`: l'usuari va declarar que el format hi és correcte i que s'explicita amb la nota. A les figures (`24_specs/svg.md §9`), les adreces segueixen la mateixa regla (decisió de l'usuari, fase 7c).

### D-31

**Ordre substantiu–adjectiu** · `13_contrib.qmd §Criteris generals` · 2026-10-01 · `681556a`, `d50b0ba`

Decisió de l'usuari (2026-10-01), aplicada a tot el corpus el mateix dia.

### D-72

**Adjectius qualificatius, preferentment darrere del nom** · `13_contrib.qmd §Criteris generals` · 2026-10-08

Decisió de l'usuari (2026-10-08): «una importància creixent», no «una creixent importància». D-31 només parlava dels classificadors, i el revisor lingüístic havia marcat aquest cas com a error contra D-31; és una preferència, i l'usuari la fixa. Les excepcions de D-31 (ordinals, quantificadors, «mateix», «propi», «altre», valoratius idiomàtics) continuen valent.

### D-32

**«No» davant d'un nom, amb guionet** · `13_contrib.qmd §Criteris generals` · 2026-10-01 · `bb12c2b`

Decisió de l'usuari (2026-10-01), que confirma la forma que el corpus ja feia servir.

### D-33

**Veu: impersonal, 2a del singular als exemples i 2a del plural als enunciats** · `13_contrib.qmd §Criteris generals` · 2026-07-12 · `31f7571`, `ccae7dd`, `87ecbcb`

- La 2a persona del singular dels `{.callout-tip}` és el criteri de la revisió interna de T2 (2026-07).
- El «nosaltres» expositiu dels exemples narrats és pràctica consolidada a T7 i T8 (revisió interna, 2026-07).
- La 2a persona del plural dels enunciats val per a P1–P9 des del 2026-10-01. Les solucions no hi entren: són a `.callout-tip`.

### D-34

**«Imbricat», no «aniuat»** · `13_contrib.qmd §Formes que no s'han de fer servir` · 2026-10-04 · `552ff1a`

Decisió de l'usuari (2026-10-04). «Aniuat», que la taula donava fins llavors com a substitució d'«anidat», no és el terme informàtic en català.

### D-35

**«Lectura/escriptura» per *load/store*, i els identificadors no canvien amb el terme** · `13_contrib.qmd §Anglicismes i terminologia obligatòria` · 2026-10-07 · `9f8e746`

Decisió de l'usuari (2026-10-07): A2 presentava *load* i *store* com a «càrrega» i «emmagatzematge». En canviar-ho a tot el corpus, els identificadors (`#nte-load-store`, `#sec-carrega-…`) es van mantenir, i des del 2026-10-09 és la regla general: quan canvia el terme d'un concepte, els identificadors no canvien, perquè canviar-los trenca els enllaços a les àncores publicades ([D-22](#d-22)).

### D-36

**«Ròssec», «semisumador» i «sumador complet»** · Retirada el 2026-10-14: substituïda per [D-116](#d-116).

### D-37

**«Coma flotant», no «punt flotant»** · `13_contrib.qmd §Formes que no s'han de fer servir` · 2026-10-01 · `c1bac38`

És el terme del corpus: 113 ocurrències contra 4, totes a `A2.qmd`, unificades el 2026-10-01.

### D-38

**«Farciment» i «multinucli»** · Retirada el 2026-10-14: substituïda per [D-116](#d-116).

### D-39

**«Enter» i «natural»** · `13_contrib.qmd §Anglicismes i terminologia obligatòria` · 2026-10-02 · `ee78460`

Proposta de la revisió externa de T3 i decisió de l'usuari (2026-10-02), amb l'escombrada del corpus feta el mateix dia.

### D-40

**VPN i PPN, a la taula de sigles** · `13_contrib.qmd §Sigles, símbols i notació` · 2026-10-03 · `8e19383`

Decisió de l'usuari (2026-10-03). Fins llavors el criteri d'exclusió les posava d'exemple de nom de camp exclòs, i la taula les incloïa.

### D-79

**Les sigles, sense plural** · `13_contrib.qmd §Sigles, símbols i notació` · 2026-10-09

Decisió de l'usuari (2026-10-09), a proposta de Claude Code, que escriu un criteri que ja s'aplicava. És el de l'Optimot: la sigla és invariable, i el nombre el diu el determinant («els SO», no «els SOs»).

### D-80

**L'article i la preposició davant de les sigles, segons la pronúncia (GIEC)** · `13_contrib.qmd §Sigles, símbols i notació` · 2026-10-09

Decisió de l'usuari (2026-10-09), per a tot el corpus: l'article i la preposició davant d'una sigla segueixen la pronúncia, com diu la GIEC («l'ISA», «l'MMU», «la RAM», «de RARS»). Ampliacions de l'usuari: «d'RV32I», que es lletreja; «d'UNIX», com dona el Termcat, i «d'NVIDIA»; «la IA», com dona l'Optimot. Davant d'un identificador de codi (decisió de l'usuari; el criteri, de Claude Code), el codi es llegeix com un mot: «d'`addi`», «l'`a0`», «de `lw`», «la `sp`».

### D-89

**Les sigles s'expandeixen només a la primera aparició del llibre** · `13_contrib.qmd §Sigles, símbols i notació` · 2026-10-09

Decisió de l'usuari (2026-10-09): una sigla s'expandeix només a la primera aparició del llibre, en l'ordre dels `chapters:` de `_quarto.yml`, perquè hi ha un compendi de sigles. Fins llavors la regla deia «la primera vegada» sense dir si era del llibre o del fitxer, i §T6 demanava expandir CMOS i CF a cada fitxer. Les expansions que ja hi havia en capítols posteriors no es treuen. El format de l'expansió i la comprovació són a [D-118](#d-118).

### D-41

**`\texttt{…}`, no `\mathtt{…}`** · `13_contrib.qmd §Codi, matemàtiques i cursiva` · 2026-10-03 · `d61a848`

El corpus feia servir `\mathtt{…}` 44 vegades (S1, S4 i A1) fins al 2026-10-03, i es va unificar a `\texttt{…}`.

### D-42

**Subíndexs en cursiva també quan són sigles, i l'excepció de les taules ISA** · `13_contrib.qmd §Codi, matemàtiques i cursiva` · 2026-10-03 · `477b9ca`

Totes dues són decisions de l'usuari (2026-10-03) que escriuen l'ús del corpus. A les taules ISA, escriure $PC$ amb `\text{…}` el separaria tipogràficament dels altres operands de la mateixa fórmula.

### D-43

**Operacions lògiques (AND, OR, XOR, NOT)** · `13_contrib.qmd §Codi, matemàtiques i cursiva` · 2026-10-01 · `c4c247a`

Decisió de l'usuari (2026-10-01), que escriu l'ús que el corpus ja feia majoritàriament i n'hi alinea les desviacions.

### D-100

**El glossari de termes és l'única font del lèxic anglès–català** · Retirada el 2026-10-14: substituïda per [D-115](#d-115), que la va invertir.

### D-106

**Sis formes més a la taula de formes que no s'han de fer servir: «comanda», «solapar», «encuar», «descomposar», «rotar» i «indentar»** · `13_contrib.qmd §Formes que no s'han de fer servir`; `24_specs/termes.toml` (`[no_admeses]`) · 2026-10-10

Decisió de l'usuari, a proposta de Claude Code. Cap no és al DIEC amb el sentit del text; les formes bones són les del Termcat o del DIEC, i el motiu de cadascuna és a l'`obs` de `termes.toml`. De «descomposar» i «rotar» hi van les formes conjugades i no l'infinitiu, perquè la comprovació llegeix un verb en *-ar* com l'arrel més qualsevol terminació, i hi entrarien «descomposició» i «rotació», que són correctes.

### D-107

**Noms de persona: com els escriu la Viquipèdia, i si no, la Wikipedia en anglès** · `13_contrib.qmd §Referència normativa` · 2026-10-10

Decisió de l'usuari (2026-10-10): per als noms de persona, la font és la Viquipèdia i, si no hi són, la Wikipedia en anglès. Les fonts lèxiques ([D-116](#d-116)) no cobreixen els noms de persona. El cas: el corpus deia «Von Neumann», i la Viquipèdia diu «John von Neumann» i «Arquitectura de von Neumann».

### D-108

**Glossari: majúscula inicial a cada cel·la, els termes en singular, i les taules del capítol normalitzades** · `13_contrib.qmd §Sigles, símbols i notació` (`## Termes`), `24_specs/termes.toml` · 2026-10-10, 2026-10-12

Decisions de l'usuari: cada cel·la comença en majúscula, i els termes van en singular, tret dels que rarament es fan servir en singular («Excepcions precises»); la forma és la de `termes.toml` ([D-115](#d-115)). Les taules del capítol porten peu curt, etiqueta `#tbl-` i `.striped`. El paràgraf de presentació de cada subsecció no passa al peu, perquè fixa convencions de lectura i el peu surt en lletra petita.

### D-115

**El lèxic anglès–català, a `24_specs/termes.toml`: el fitxer mana i el text s'hi comprova** · `13_contrib.qmd §Anglicismes i terminologia obligatòria`, `§Sigles, símbols i notació`, `§Registres`; `24_specs/termes.toml`, `25_scripts/gen_glossari.py` · 2026-10-13

Declaració de l'usuari: com a política general, cada informació ha de tenir una sola font, perquè la duplicació dificulta el manteniment i trenca la consistència. La forma catalana d'un terme era a tres o quatre llocs, i la comprovació i el que es comprovava eren la mateixa cosa. Propostes de Claude Code, acceptades:

- **Inverteix D-100**: `termes.toml` decideix *què* es diu (la forma, les observacions, els termes en anglès, les formes no admeses), i el text, *on* es presenta. La comprovació (`gen_glossari.py --comprova`, a cada commit) atura una presentació que no hi lliga. El cost, dues edicions per a un terme nou, s'accepta.
- **El glossari i la taula de formes no admeses es generen en renderitzar** (`auto_termes/`) i no es versionen ([D-104](#d-104)). `lint_prosa.py` llegeix les formes de `[no_admeses]`, i, quan canvia `termes.toml`, les busca a tots els `.qmd`.
- **El diccionari de termes** es genera de `termes.toml` i es versiona, perquè VS Code el llegeix sense render; cap plural no es calcula, perquè els calculats hi feien entrar formes que no existeixen.
- **El detector de presentacions** llegeix els fragments de `21_riscv/` on els inclou el capítol, i `[no_presentacions]` recull, amb el motiu, les glosses que semblen presentacions i no ho són.

Alternativa descartada: una columna castellana al glossari, amb el Termcat com a referència. L'usuari la va retirar el 2026-10-09, com a decisió ferma, el mateix dia que l'havia acceptada.

### D-116

**Terme català o anglès: les fonts per ordre de precedència, el sintagma transparent i l'anglès sempre en cursiva** · `13_contrib.qmd §Referència normativa`, `§Anglicismes i terminologia obligatòria`, `§Codi, matemàtiques i cursiva`, `§T6`; `24_specs/termes.toml` · 2026-10-13

Decisions de l'usuari sobre l'anàlisi del lèxic (`24_specs/lexic/revisio_2026-10-12.md`), amb les recomanacions de Claude Code acceptades. Substitueix D-29, D-88, D-36 i D-38.

- **Les fonts, en una sola llista** per ordre de precedència: DIEC2, Termcat, Optimot, Softcatalà i Viquipèdia. La Viquipèdia pot aportar formes noves (a proposta de l'usuari: si no, casos com «taula de salts» no es resolien), amb dues condicions, perquè no és normativa: l'article ha de ser del concepte informàtic, amb la forma al títol o a l'entradeta, i no pot contradir les altres fonts.
- **L'anglès, només en dos casos**: quan no hi ha cap forma catalana, o quan el llibre ha decidit no fer-la servir (*heap*: «memòria en monticle» és massa lluny de l'ús). `[en_angles]` els recull tots, amb el motiu.
- **El sintagma transparent**: si cap font no té el terme, el sintagma català (*page fault*). Si no, desenes de termes fets amb mots catalans haurien passat a l'anglès.
- **Entre dues formes, la de més precedència**, tret que la fitxa del Termcat sigui d'una altra àrea o confongui conceptes que el llibre distingeix; llavors mana el llibre, amb el motiu a l'observació (*branch*, *throughput*…).
- **Després de la presentació, sempre el català**; la glossa es pot repetir a cada fitxer, perquè els problemes, les solucions i el laboratori es llegeixen sols. **L'anglès, sempre en cursiva**, també a les taules i a les figures, però no als comentaris del codi.
- **L'anglès en pla atura el commit** (`lint_prosa.py`), amb les excepcions a `[angles_en_pla]`.
- **Les fonts de cada terme**, una llista i no un sol valor, perquè si una font canvia les altres sostenen la forma. Sense URL, perquè les fitxes no tenen identificadors estables.
- **Formes decidides per l'usuari**: «ròssec», «semisumador», «sumador complet», «farciment» i «multinucli» (2026-10-03 a 2026-10-09); «subnormal», el terme de l'estàndard (DNRM es manté, perquè és la dels exàmens); «preprocessament» i «assemblatge», del DIEC.

### D-118

**Les sigles, a `24_specs/termes.toml`: el compendi de sigles es genera, i l'expansió es comprova** · `13_contrib.qmd §Sigles, símbols i notació`, `§Registres`; `24_specs/termes.toml` (`[sigles]`), `25_scripts/sigles.py` · 2026-10-13, 2026-10-14

Petició de l'usuari: les sigles a `termes.toml` i la comprovació de [D-89](#d-89). Decisions de l'usuari sobre les propostes de Claude Code:

- **`[sigles]`**, amb la sigla com a clau i els camps `ca`, `en`, `obs` i `excepcio`. La taula se'n genera en renderitzar, per ordre alfabètic.
- **El format únic de l'expansió**, el de l'usuari, que en va demanar un de sol: «disc d'estat sòlid (*solid-state drive*, SSD)», amb tres variants: «ca (*en*, SIGLA)», «*en* (SIGLA)» i «ca (SIGLA)». L'anglès en minúscula, llevat dels noms propis; la negreta, només a la forma catalana.
- **Hi són les sigles del cos del text**, sense les variants de RISC-V, les dels aprofundiments i les institucionals conegudes (UPC).
- **La comprovació** (`sigles.py`, atura) llegeix el llibre en l'ordre de `chapters:`. La primera aparició és la primera fora dels aprofundiments, perquè el cos s'ha de poder llegir sense; si és en un títol, una taula o una fórmula, l'expansió va al paràgraf següent. `[no_sigles]` recull, amb el motiu, els mots en majúscules que no són sigles. Als aprofundiments també atura les variants que el format exclou.

## Format

### D-70

**Punter cap endavant T3 → T6: temps d'execució i CPI** · `13_contrib.qmd §Referències creuades` · 2026-10-08

Decisió de l'usuari (2026-10-08), a proposta de Claude Code. Dos problemes de T3, `exr-t3-bucles-for` (apartats c i d) i `exr-t3-bucles-multiplicacio` (d i e), demanen temps d'execució i CPI, que la teoria presenta a T6 (`@eq-texe2`); vénen de l'original de MIPS, on el rendiment era a T1. Treure o moure els apartats es va descartar: la dependència és de càlcul, amb la fórmula citada a la solució (S3), i es pot seguir com a punter explícit.

### D-78

**Els punters cap endavant de la fase 8a, inscrits a la llista** · `13_contrib.qmd §Referències creuades` · 2026-10-09

Decisió de l'usuari (2026-10-09), a proposta de Claude Code. La revisió tècnica d'A1–A8 va trobar punters cap endavant que no eren a la llista de la guia. Tots eren explícits, i el text s'entén sense seguir-los: es van inscriure a la llista sense tocar el text.

### D-44

**Una remissió `@fig-` a cada figura del cos del text** · `13_contrib.qmd §Referències creuades` · 2026-10-03 · `e806916`

Decisió de l'usuari (fase 7c, 2026-10-03; i 2026-10-07): figures sempre referenciades al text, taules opcionalment. Fins llavors la guia deia que ni les unes ni les altres no calia referenciar-les.

### D-117

**Als blocs de codi s'hi remet amb `@lst-`, i només es numeren els llistats** · `13_contrib.qmd §Referències creuades` i `§Presentació visual` · 2026-10-13

Decisió de l'usuari (2026-10-09): remissions `@lst-` en lloc de «el codi següent», arran de l'RSE d'A9, que al PDF havia flotat lluny ([D-69](#d-69)). Al PDF, Quarto numerava tots els blocs amb `filename`, i l'HTML cap; amb `#lst-`, cada format hauria donat un número diferent. Decisions de l'usuari, a recomanació de Claude Code: el PDF numera només els llistats `#lst-`, com l'HTML; la forma de div, perquè les comprovacions de l'ortografia llegeixen el peu; la remissió substitueix la remissió per posició; el peu diu què fa el codi; i l'abast és per la forma, no pel nom. No són remissions les sèries d'apartats amb lletra ni les presentacions amb dos punts («es declara així:»). Als enunciats, el peu és neutre («Fragment de l'apartat b).»), perquè no doni la resposta.

### D-121

**Els llistats i les remissions als blocs de codi, comprovats** · `13_contrib.qmd §Referències creuades` i `§Comprovacions per nivells`; `25_scripts/verifica_llistats.py` · 2026-10-14

Petició de l'usuari: automatitzar les comprovacions de D-117 dins del sistema de proves. `verifica_llistats.py` atura una forma de llistat incorrecta i un llistat sense remissió o una remissió sense llistat; avisa d'un peu sense punt i d'una remissió per posició (L7), que és un avís perquè triar entre una remissió i una presentació és de qui escriu. L7 es va calibrar sobre el llibre d'abans de D-117, sense cap fals positiu. Després del render, `--sortida` compara la numeració de l'HTML i del PDF.

### D-45

**El títol dels blocs de pseudocodi** · `13_contrib.qmd §Blocs de codi` · 2026-10-01 · `f066a8e`

Decisió de l'usuari (2026-10-01), a partir de l'anotació #4 de la revisió externa de T4. Que «—» surt com a `---` al PDF es va verificar a `make render-complet` el 2026-10-01.

### D-46

**Algorismes en rodona** · `13_contrib.qmd §Blocs de codi` · 2026-10-02 · `f066a8e`

La mateixa decisió que [D-45](#d-45) (anotació #4). Al PDF, la cursiva venia de l'estil *plain* del `\newtheorem` que genera Quarto, i `preamble.tex` la treu redefinint aquest estil.

### D-47

**Ressaltat propi dels blocs `.s`** · `13_contrib.qmd §Blocs de codi` · 2026-10-07 · `f508b0f`

Feta des de zero el 2026-10-07 (decisió de l'usuari): fins llavors Pandoc feia servir `gnuassembler`, que no ressaltava `.eqv` ni `.end_macro` (de RARS) i donava el mateix color a instruccions i registres; partir de la d'x86 volia dir canviar-ne totes les llistes. El 2026-10-07 cobria tots els mnemònics i directives dels blocs `.s` del corpus.

### D-48

**La marca `codi_erroni`** · `13_contrib.qmd §Blocs de codi` · 2026-10-06 · `0d33d13`, `9f8e746`

La marca exclou el bloc de les eines **per forma**, en lloc d'una llista de línies que caduca: sense la marca, el contraexemple de `@nte-rars-noms-reservats`, amb un `.eqv B, 16` escrit a posta, compta com un xoc real en una escombrada dels símbols `.eqv` i obliga a aturar-se a decidir-ho.

### D-49

**`void main()` a la notació, `int main` al C que es compila** · `13_contrib.qmd §Estil de codi C` · 2026-09-21 · `d713262`, `b3072a6`

L'estàndard de C exigeix `int main` a les implementacions allotjades (*hosted*), que corren sota un SO que en recull el codi de retorn. En un entorn autònom (*freestanding*), com el d'EC, la forma del punt d'entrada la defineix la implementació. A més, aquell C no es compila mai: és la notació que l'alumne tradueix a mà, i un `return` que ningú no recull seria una ficció. Fora d'EC, en un programa compilat per a un SO, cal `int main`.

Els blocs que porten `int main` són l'altra meitat de la regla:

| Bloc | Per què hi va `int main` |
| :--- | :--- |
| `A2.qmd` @tip-forcar-error-tipus | Se'n cita literalment la sortida de `gcc -Wall -Wextra -Wpedantic`; amb `void main()` hi sortiria un diagnòstic més. |
| `P3.qmd`/`S3.qmd` @exr-t3-compilacio-relocacio | El C hi és l'objecte d'estudi: el `return f(x)` fa visible la referència externa que resol l'enllaçament. |

### D-83

**Comentaris del C, sempre amb `//`, línia per línia** · `13_contrib.qmd §Estil de codi C` · 2026-10-09

Decisió de l'usuari (2026-10-09). Fins llavors la regla era «d'una sola línia, `//`; de més d'una línia, `/* */`», i el corpus no la seguia. La regla nova en fa un sol cas: amb `//` a cada línia, un bloc sencer es pot desactivar envoltant-lo amb `/* … */`, cosa que no és possible si ja conté comentaris `/* … */`, perquè C no els admet imbricats. A2 ho explica a `#imp-codi-format-criteris`, el primer lloc on el llibre parla de com comentar el codi.

### D-50

**Format del codi RISC-V: F1–F5** · `13_contrib.qmd §Estil de codi RISC-V` · 2026-10-03 · `0e25c9f`

Escrit a partir de la proposta d'un *checker* que deixava un marcador a A2. F5 (els operands a la columna 16) és decisió de l'usuari (2026-10-06), a proposta de Claude Code, perquè la reunió del grup de treball del 2026-10-05 no ho va arribar a tractar: és l'estil de tota la teoria i les solucions (1 176 línies d'instrucció, contra 596 amb els operands a la columna 13 o 14), i és on cauen els operands del codi que genera `gcc -S`, amb tabuladors de 8. La columna dels comentaris no es regula perquè gairebé tots els blocs amb comentaris (199 de 213) ja els tenien en una sola columna.

### D-66

**Pseudoinstruccions: un sol esquema de columnes i un sol prefix de títol** · `13_contrib.qmd §Fitxer de referència tècnica`, `§Callouts` · 2026-10-07 · `75ea6c6`

Decisions de l'usuari, a proposta de Claude Code. Hi havia cinc esquemes de columnes i tres prefixos, i «Condició» volia dir dues coses. L'esquema «Pseudoinstrucció, Operació, Expansió» és el de les taules ISA, perquè la pseudoinstrucció es llegeix al costat de la instrucció en què s'expandeix; «Condició» només queda a `li`. La columna «Ús» es va treure sense perdre res: el que deia ja és a la prosa d'A3. El prefix, «Pseudoinstruccions —», no porta extensió, perquè les pseudoinstruccions no són ISA ni ABI: les defineix el manual de l'assemblador (`riscv_asm_manual`).

### D-90

**Exemples plegables a l'HTML i remissió de l'enunciat a la solució: pilot de T1** · `13_contrib.qmd §Problemes i solucions`, `§Callouts`, `§Renderitzar el projecte` · 2026-10-09

Decisió de l'usuari: un pilot a T1. El filtre `plegables.lua` plega a l'HTML, amb `<details>`, la solució dels exemples d'A1 amb el format **Pregunta** → **Solució** → **Resposta** (div `.resposta`), i afegeix a cada enunciat de P1 la remissió a la seva solució. La remissió la genera el filtre a partir de l'slug compartit ([D-22](#d-22)): escrita a mà, seria una segona còpia de la correspondència. `<details>` i no un callout imbricat, perquè el plegable és part de l'exemple. Estendre-ho és decisió de la reunió del 2 de novembre (`TODO.md`).

### D-101

**«📑 Continguts»: l'índex dels apunts a l'HTML, generat des dels `.qmd`** · `13_contrib.qmd §Renderitzar el projecte`, `10_continguts.qmd`, `25_scripts/continguts.lua` · 2026-10-10

Petició de l'usuari: una vista de les seccions de tots els temes alhora a l'HTML, com l'índex del PDF. Decisions de l'usuari: A1–A9, fins al nivell `###`, entre la Presentació i els Apunts (és massa llarga per ser a la Presentació), i els títols dels temes sense número. Recomanacions de Claude Code, acceptades: sense plegar, fora de la cerca i sense enllaç des de la Presentació. Un filtre i no un script de pre-render, perquè no genera cap fitxer ni afegeix cap pas, i llegeix les fonts amb el lector de Pandoc. Al PDF, que ja té índex, el filtre en treu el capítol: `.content-visible when-format="html"` no n'hi ha prou.

### D-109

**PDF: l'índex es diu «Continguts», la columna «Operació» va amb sagnat francès, els números no porten punt, i l'ordre de les pàgines inicials no és el de l'HTML** · `13_contrib.qmd §Renderitzar el projecte` · 2026-10-12

Peticions de l'usuari: «Continguts» com a títol de l'índex del PDF; sagnat francès a la columna «Operació» (`sagnat_operacio.lua`); i els números sense punt, com a l'HTML (`numbers=noendperiod`: el punt el posava KOMA perquè hi ha números romans a les parts). **L'ordre de les pàgines inicials és una no coincidència acceptada** (declaració de l'usuari): a l'HTML, la Presentació fa de portada i va davant de «📑 Continguts»; al PDF, que té portada pròpia, l'índex va davant, que és la pràctica habitual.

### D-102

**Una taula amb etiqueta `#tbl-` porta peu** · `13_contrib.qmd §Taules` · 2026-10-10

Una taula amb etiqueta i sense peu Quarto la numera igualment i en deixa el peu buit («Taula 6.1» sola a l'HTML). Proposta de Claude Code, acceptada per l'usuari: posar-hi peu, d'acord amb el seu criteri de «totes les taules amb `#tbl-`», en lloc de treure'n l'etiqueta; i que `verifica_taules.py` ho avisi, al peu de la taula o al div que la porta. Fins llavors la guia només demanava el peu al cos del text.

### D-112

**Després d'una fórmula destacada, «on» en minúscula** · `13_contrib.qmd §Codi, matemàtiques i cursiva` · 2026-10-12

Recomanació de Claude Code, acceptada per l'usuari: la fórmula destacada forma part de la frase, i el que la segueix la continua, en minúscula. És el que ja feia la major part del corpus (17 de les 21 línies que començaven per «on», el 2026-10-12).

### D-111

**Cap etiqueta ni constant `b` o `B` als blocs d'assemblador** · `13_contrib.qmd §T2 i T3` · 2026-10-12

Regla de l'usuari (2026-10-12): cap etiqueta `B:` als blocs `.s`, perquè `b` és la pseudoinstrucció de salt. L'abast i els noms, decisions de l'usuari sobre les propostes de Claude Code: també la minúscula, i també les constants; les sèries de tres o menys passen a `X`, `Y`, `Z` (`x`, `y`, `z`), i les més llargues, a lletres consecutives a partir de `P`, amb el nom C i el text que les citen. A RARS 1.6, una etiqueta `B:` assembla, però una constant `.eqv B` no (@nte-rars-noms-reservats). `verifica_format_codi.py` ho comprova (F6) i, a diferència de les altres regles de format, atura el commit, perquè és una prohibició i no una qüestió d'estil (recomanació de Claude Code, acceptada).

### D-110

**Cap callout dins d'un altre** · `13_contrib.qmd §Imbricacions` · 2026-10-12

Regla de l'usuari (2026-10-12): no es permet la imbricació de callouts. Criteri de Claude Code per desfer, cas a cas, les que hi havia: un aprofundiment dins d'un callout RISC-V surt a continuació, perquè té sentit sol; un exemple o una taula que només tenen sentit dins d'un aprofundiment s'hi fonen, amb el títol en negreta, perquè fora haurien passat a ser matèria avaluable; i un `#cau-` dins d'una solució passa a un paràgraf que comença amb «**Atenció**:». `verifica_callouts.py`, a `comprova.py`, atura el commit si en troba cap, també a través d'un `include`.

## Figures

### D-51

**El `<desc>` com a text alternatiu, i una mida comuna a l'HTML** · `13_contrib.qmd §Figures i material gràfic` · 2026-10-06 · `e806916`

Que el `<desc>` no repeteixi el peu és decisió de l'usuari (fase 7c). L'amplada a l'HTML, la del `viewBox` per 1,4, també (2026-10-06): fins llavors, una figura amb `width="100%"` s'estirava a tota la columna, i una amb l'amplada en px es quedava a la mida natural. La mida la fixa el filtre `figures.lua` per a totes. Les figures estretes dels generadors (`gen_BA.py`, `gen_mapa.py` i `gen_memoria.py`, `24_specs/svg.md §2`) porten l'amplada en px, que s'hi va posar perquè no s'estiressin a l'HTML; amb el filtre ja no hi influeix, i es manté perquè és innòcua.

### D-52

**Camps horitzontals a les figures de registres** · `13_contrib.qmd §Política de generació SVG` · 2026-10-03 · `2dbf236`

La clau `horitzontals` es va afegir el 2026-10-03 a petició de la revisió externa de T5, per a la «S» de `T5_ieee754_format_registre`.

### D-53

**L'estat d'una figura no va al nom del fitxer** · `13_contrib.qmd §Convencions SVG` · 2026-10-04 · `4fa6fd3`

Els altres sufixos de fitxer font que hi havia (`__drawio`, `__org`, `____error____`, `__net__`) eren de fitxers orfes, retirats a la fase 7c. Revisat i escrit el 2026-10-04, amb els sufixos d'origen `__BA` i `__subrutina` proposats per l'usuari.

### D-54

**La foto del xip de T7 és CC0 1.0** · `13_contrib.qmd §Convencions SVG` (figures externes) · 2026-10-06 · `0d33d13`

Fins al 2026-10-06 el `.bib` hi deia CC BY-SA 2.0 i només Fritzchens Fritz; la pàgina del fitxer a Wikimedia Commons diu CC0 1.0 i tots dos autors, i el `.bib` es va corregir per decisió de l'usuari.

### D-55

**Figures dinàmiques a l'HTML, seqüència estàtica al PDF** · `13_contrib.qmd §Figures dinàmiques` · 2026-10-04 · `2d14b8f`

Decisió de l'usuari 4 de la fase 7c. Prototip: `#fig-lru-exemple`.

### D-56

**Imatges sense peu centrades als callouts del PDF** · `13_contrib.qmd §Presentació visual` · 2026-10-06 · `74507d7`

Fins al 2026-10-06 sortien alineades a l'esquerra. Quan es va escriure, totes les imatges sense peu dels callouts eren figures de registres més amples que el callout, de manera que la regla no hi tenia cap efecte visible: és per a la primera que no ho sigui.

### D-69

**Blocs de codi al PDF: no floten i es parteixen entre pàgines** · `13_contrib.qmd §Presentació visual` · 2026-10-08

Quarto escriu cada bloc amb `filename` com a flotant `codelisting`: fora dels callouts, LaTeX el posava on li cabia (l'RSE d'A9, deu pàgines enllà del «El codi següent…»), i dins, com una caixa que no es parteix (la de S9 es tallava al peu de la pàgina). `preamble.tex` el redefineix com un bloc normal; dins d'un callout, sense el fons gris de `framed`, que `tcolorbox` no sap partir. Descartades: `[H]` per a tots, que no es parteix; i treure el `filename`, que és la convenció. Des de [D-117](#d-117), el comptador i el peu només són dels llistats `#lst-`.

### D-57

**Fórmules en línia a l'HTML: `overflow` només a les llargues** · `13_contrib.qmd §Presentació visual` · 2026-10-06 · `74507d7`

Fins al 2026-10-06 l'`overflow-x: auto` era a totes, i un `inline-block` amb un `overflow` que no sigui `visible` es recolza en la vora inferior (CSS 2.1 §10.8.1): les fórmules pujaven d'1 a 6 px per sobre de la línia de text (mesurat a A6, 40 fórmules) i feien créixer l'interlineat. Després del canvi, a l'escriptori, cap fórmula d'A4, A5, A6 i S6 no era llarga i totes eren a 0 px de la línia; en un mòbil de 375 px, n'eren llargues 4, 14, 2 i 1.

### D-71

**BA: vectors massa llargs amb el tram del mig d'alçada fixa** · `24_specs/svg.md §3` · 2026-10-08

Decisió de l'usuari (2026-10-08): el BA de `variancia` de S5 passa de taula a figura de `gen_BA.py`. El vector `vquadrats` (`float[100]`, 400 bytes) faria 4 000 px d'alt a ×½ i 2 000 a ×¼, l'escala més petita de §3. `gen_BA.py` admet `mig` als vectors: el tram elidit es dibuixa amb aquesta alçada, i la mida i els desplaçaments rotulats continuen sent els reals (la funció `alcada` dibuixa, `mida` compta).

### D-67

**El generador dels mapes de memòria, `gen_mapa.py` (sufix `__mapa`)** · `13_contrib.qmd §Convencions SVG`; `24_specs/svg.md §2`, `§4`, `§7` i `§9` · 2026-10-07

Generador germà de `gen_BA.py`, per al mapa de memòria de RARS i les piles en fila d'A3, amb les primitives compartides de `columna_memoria.py`, perquè les dues famílies dibuixin igual. `__mapa` perquè totes dues figures són mapes de la memòria. Decisions de l'usuari (fase 7f), a proposta de Claude Code:

- La classe `estreta` (340 px), amb `w_rect` de 244 px, perquè el marge dret sigui de 10 px, com els altres.
- La línia de `sp` de les piles pren el color de la zona del cim, com als BA: el vermell és de les dependències de dades.
- Les vores de cada zona, per dins de la seva àrea (`svg.md §7`), perquè la frontera no depengui de l'ordre de dibuix; les ratlles de dos colors es van descartar, perquè la línia discontínua ja vol dir «elidit». Per això l'alineació porta contorn continu (§4): els seus bytes són del BA.

### D-68

**Els originals substituïts per una figura generada es conserven, a `22_figs_originals/conservats/`** · `13_contrib.qmd §Convencions SVG` · 2026-10-04, 2026-10-09

Decisió de l'usuari: els originals substituïts per una figura generada es conserven, perquè l'usuari els fa servir per a les diapositives i n'esmena ell mateix el que calgui. Des del 2026-10-09 són a `conservats/`, i el directori és el criteri (abans l'inventari els deduïa per l'arrel del nom). Les expressions del pre-render a `_quarto.yml` van ancorades a l'inici del camí (`^22_figs_originals/`, `^auto_figs/`): sense l'àncora, també processaven els *worktrees* de `.claude/worktrees/`.

### D-76

**Noms de les figures pel fitxer que les consumeix: `A<N>_`, `P<N>_`, `S<N>_`, `L<N>_`** · `13_contrib.qmd §Figures i material gràfic` · 2026-10-08

Decisió de l'usuari (2026-10-08); l'abast, a proposta de Claude Code. Fins llavors el prefix era el del tema (`T3_`), que no deia on surt la figura. Les figures que també surten al compendi (`11_riscv.qmd`) prenen el prefix del tema; els originals conservats ([D-68](#d-68)), el de la versió generada. Els scripts conserven el nom (`gen_T4_sumador.py`, `gen_T7.py`, `gen_T8.py`). Els textos anteriors al canvi citen els noms d'abans (`git log --follow`).

### D-92

**Les figures natives, a la paleta: dos colors afegits, els de fora migrats i les figures de T6 retocades** · Retirada el 2026-10-14: substituïda per [D-113](#d-113).

### D-93

**Portes lògiques: la forma distintiva ANSI/IEEE 91** · `24_specs/svg.md §16` · 2026-10-03 · `184832c`

Convenció fixada a la fase 5 (2026-10-03, decisió de l'usuari), amb les figures del sumador de T4 (`#fig-semisumador-sumador-complet` i `#fig-sumador-propagacio-rossec`, de `25_scripts/gen_T4_sumador.py`). La forma distintiva és la de les diapositives de l'assignatura i la d'IC; es descarta la rectangular de l'IEC.

### D-94

**Figures generades: model (a) per a les soltes, model (b) per a les famílies** · `24_specs/svg.md §17` · 2026-10-03 · `4fa6fd3`

Model de generació de la fase 7c (2026-10-03, decisió de l'usuari). En el model (b), la definició és un TOML i l'SVG no es versiona: una convenció nova s'aplica a tota la família d'un sol cop. En el model (a), l'SVG versionat és el font i l'script el regenera, amb `--comprova` perquè un retoc fet a mà a l'SVG i no a l'script surti com a diferència.

### D-95

**Figures de memòria cau: seqüència, traça i estat** · `24_specs/svg.md §17` · 2026-10-04 · `218e195`, `d59ae41`

Decisió de l'usuari (fase 7c): al PDF, la seqüència per als exemples curts i la traça per als llargs, amb l'estat inicial com a subfigura a totes dues, perquè l'alumne faci la transició d'una a l'altra; a l'HTML, la figura dinàmica ([D-55](#d-55)). El tercer estil, `estat`, és per a les taules d'organització d'A7 (2026-10-06).

### D-99

**Vores compartides a totes les figures: cada zona, per dins de la seva àrea** · `24_specs/svg.md §7` · 2026-10-09, 2026-10-12

L'usuari va estendre la regla de [D-67](#d-67) a totes les figures: dos `<rect>` amb traç de color diferent que comparteixen una vora es tapen a mitges segons l'ordre de dibuix. Detalls de Claude Code, acceptats: en horitzontal i en vertical, també les vores de fora, i un ressalt sense farciment es dibuixa després de les zones que toca. És un postprocés de l'SVG acabat (`vores_compartides()`, a `figlib.py`), i no una reestructuració dels generadors, perquè cadascun dibuixa les cel·les a la seva manera. `comprova_vores.py`, a `comprova.py`, avisa d'un traç que un `<rect>` posterior tapa en part.

### D-113

**La paleta: 17 colors, i les figures natives només en fan servir d'aquests** · `24_specs/svg.md §10`, `§13`, `§14` i `§15` · 2026-10-06, 2026-10-13 · `c7180d9`, `77e6bce`

Cada color té un paper, i cada paper un sol color. Decisions de l'usuari, a proposta de Claude Code: `#e6f1fb` (contenidor) i `#dee2e6` (graella) s'hi van afegir perquè diverses figures ja els feien servir amb aquest paper (2026-10-06); els colors de fora de la paleta es van migrar, i §13 només conserva les substitucions que algun fitxer fa servir; i tres colors en van sortir perquè repetien un paper amb un to gairebé igual (2026-10-13). Les figures extretes de PDF (§15) no porten `textLength`, que `rsvg-convert` no implementa.

### D-124

**`A1_flux_compilacio`: «Objecte», no «Fitxer objecte»** · `22_figs_originals/A1_flux_compilacio.svg` · 2026-09-23

La Fase C de T1 va proposar que l'etiqueta digués «Fitxer objecte», com el text, i ho va descartar perquè no cabia al requadre. L'usuari va revisar la figura en tancar la revisió interna de T1 i la dona per correcta: l'etiqueta es queda com és.

## Eines

### D-58

**`make render-complet`, obligatori abans de tocar el PDF** · `13_contrib.qmd §Verificació de l'entorn` · 2026-09-22 · `5589801`

Un render HTML no exercita el PDF: el 2026-09-22 el corpus tenia **83 blocs `when-format="pdf"`**, i almenys cinc convencions de la guia existien precisament perquè el PDF es comporta diferent (la duplicació de figures si no se separen les variants, `tbl-colwidths` que ha de sumar 100, les capçaleres `###` del laboratori, `[@sec-]` que només funciona a PDF, i la guia mateixa, que és HTML-only).

### D-62

**Les afirmacions sobre RARS es resolen executant RARS, i les eines externes al `.cache/` del clon** · `13_contrib.qmd §Verificació empírica a RARS` · 2026-09-23, 2026-10-10 · `6fcee2c`, `fbf7c3d`

Dues afirmacions sobre RARS han resultat falses en executar-lo: l'alineació de `.dword`, que RARS fa a 4 bytes i no a 8, i la forma llarga de `.section` ([D-8](#d-8)). Es comprova pel resultat, no per l'absència d'error, perquè algunes formes de `.section` assemblaven i no feien el que semblava. El procediment és a la skill `rars`.

El `.jar` no es versiona. Les eines externes (RARS, LanguageTool) es baixen un sol cop al `.cache/` del clon principal, que git ignora i que els *worktrees* comparteixen (decisió de l'usuari, 2026-10-10; `25_scripts/eines_externes.py`); les variables d'entorn (`RARS_JAR`, `LANGUAGETOOL_DIR`) hi passen al davant.

### D-59

**Push directe a `main`: la restricció és per als revisors, no per a l'editor** · `13_contrib.qmd §Push directe a main` · 2026-04-29, 2026-10-07 · `1d4308d`

La restricció als canvis trivials és del 2026-04-29. Declaració de l'usuari (2026-10-07): la restricció és per als revisors externs, no per a l'editor, fins al segon quadrimestre del curs 2026-27. Des del 2026-10-14, les sessions de Claude Code treballen a la branca `operacions` ([D-123](#d-123)), i el push a `main` és el de l'editor.

### D-60

**DejaVu Sans Mono, la font monoespaiada del PDF** · `13_contrib.qmd §Renderitzar el projecte` · 2026-10-06 · `74507d7`

Des del 2026-10-06. Amb DejaVu Sans Mono el registre de LaTeX ja no hi dona cap «Missing character». Escalada a l'altura de les minúscules del text, és més estreta que Latin Modern Mono, i cap bloc de codi ni cap taula no surt del marge (`pdftotext -bbox`).

### D-61

**El hook d'abans del commit avisa, però no pregunta; i no renderitza si el render no llegeix cap fitxer canviat** · Retirada el 2026-10-14: substituïda per [D-103](#d-103).

### D-74

**Calendari del laboratori: `verifica_calendari.py`, l'agent `verificador-calendari` i el hook** · `13_contrib.qmd §IA` · 2026-10-08, 2026-10-09

Decisió de l'usuari: com que el calendari canvia cada quadrimestre, un agent el comprova en els commits que el toquen. La part mecànica (dates, dies, ordre) la fa `verifica_calendari.py`, perquè no depengui del model; el que demana judici (quadrimestre, festius), l'agent, que només informa. El calendari és només de l'HTML.

**És una demo** (declaració de l'usuari, 2026-10-09): mostra el quadrimestre de primavera, el que té més grups, i no s'ha de mantenir al dia. **Un canvi de dia** (patró que va demanar l'usuari, proposta de Claude Code) es marca en vermell i amb †, `[07/05 †]{.canvi-dia}`, amb una nota sota la taula: la † perquè no depengui només del color, i el vermell perquè la negreta ja marca l'examen.

### D-96

**Errades del material publicat: una *issue* amb l'etiqueta `errada`, i el commit que la tanca** · `13_contrib.qmd §Errades del material publicat` · 2026-10-09

Proposta de Claude Code, acceptada per l'usuari: la mínima que encaixa amb el que ja hi havia. Les *issues* de GitLab, perquè no cal ser membre del grup per veure-les i deixen rastre; la correcció pel camí de qualsevol canvi ([D-59](#d-59)); i `Closes #n`, perquè la *issue* es tanqui quan el commit arribi a `main`. Queden fora, perquè són decisions de política: si es publica una llista d'errades per als alumnes i com s'avisa d'una correcció un cop començades les classes.

### D-98

**Fitxers orfes: `25_scripts/orfes.py`, a `make inventari` i al hook** · `13_contrib.qmd §Figures i material gràfic`, `§IA` · 2026-10-09

Proposta de Claude Code, acceptada: un script i no un agent, perquè és una comprovació mecànica. Un fitxer versionat és orfe si cap altre no en cita el nom o l'arrel; per a les figures, el nom de la sortida del pre-render, perquè el `.qmd` cita `auto_figs/…`. No compten les cites dels fitxers que citen fitxers retirats pel nom (el `TODO.md`, el registre). Triga menys d'un segon i el hook el passa a cada commit; avisa, no atura.

### D-103

**Comprovacions per nivells: `comprova.py`, el hook de Claude Code i els hooks de git** · `13_contrib.qmd §Comprovacions per nivells`, `§Verificació de l'entorn`, `§Renderitzar el projecte`, `§IA` · 2026-10-10 · `722c522`, `980434b`

Petició de l'usuari: nivells de comprovació, perquè hi havia proves innecessàries (renderitzar quan només canvia el `TODO.md`), amb una opció per fer-les totes i documentats per als revisors. Proposta de Claude Code, acceptada. Substitueix D-61.

- **El nivell es dedueix dels fitxers canviats**, amb una sola classificació, la de `comprova.py`, que també fan servir `orfes.py` i `escombrada.sh` (abans n'hi havia cinc llistes que no coincidien). El nivell 0 (fitxers operatius) no renderitza; als nivells 3 i 4, render complet, perquè les figures i la configuració trenquen el PDF sense que l'HTML ho mostri.
- **El render ha d'acabar net**, també sense cap WARNING de Quarto.
- **El hook d'abans del commit crida `comprova.py`**. Els errors aturen el commit; els avisos no aturen ni pregunten (decisió de l'usuari).
- **Hooks de git opcionals** (`.githooks/`), per a qui no fa servir Claude Code, i `flock` als renders del `Makefile`, perquè el pre-render esborra `auto_figs/`.
- **La CI de les branques**, als *runners* de GitHub, perquè el GitLab de la UPC no en té. Un *runner* propi es va descartar: demanava mantenir-lo i executar-hi el codi de qualsevol branca.

### D-104

**Registres: una sola política, i les durades en rangs** · `13_contrib.qmd §Comprovacions per nivells`, `§Figures i material gràfic`, `§Fitxer de referència tècnica` · 2026-10-10

Petició de l'usuari: inventariar els registres i reduir-los (una sola font, fusions, fora els irrellevants), amb una sola política d'actualització. Com que regenerar-los tots triga menys d'un segon, els `--comprova` passen a cada commit. El que es pot generar es genera i no es versiona (l'inventari de figures, que portava números de línia i no era al dia); les taules de la guia que una ordre pot donar s'eliminen; l'arbre del `README.md` és l'única llista de fitxers. **Les durades, en rangs** (decisió de l'usuari): una durada precisa seria un registre més per mantenir.

### D-105

**Ortografia amb `hunspell`, gramàtica amb LanguageTool, i les formes que no s'han de fer servir, comprovades** · `13_contrib.qmd §Comprovacions per nivells`, `§Requisits previs` · 2026-10-10

Pregunta de l'usuari: si un corrector local reduiria la dependència de Claude Code. Una prova va trobar errors reals que la revisió interna no havia vist. Propostes de Claude Code, acceptades:

- **`hunspell`**, a cada commit, sobre les línies afegides; avisa, perquè un mot desconegut pot ser legítim. Un sol diccionari, `24_specs/diccionari.txt`, per a VS Code i `hunspell`.
- **Les formes no admeses aturen el commit**: mecanitzar les regles que ja són mecàniques redueix la dependència del model.
- **LanguageTool**, a `make comprova-tot` i `make gramatica`, no a cada commit: la primera vegada baixa uns 250 MB. El soroll es desactiva a `gramatica.toml`, a mà, amb el perquè.
- **El revisor lingüístic parteix de les eines** i dedica la lectura al que no veuen; una persona comença igual. Justificació de l'usuari: no pot obligar els revisors ni els contribuïdors futurs a fer servir Claude Code.

### D-120

**Autoproves de les comprovacions: cada eina, sobre llibres mínims amb errors coneguts** · `13_contrib.qmd §Comprovacions per nivells`; `25_scripts/autoproves.py`, `25_scripts/comprova.py`, `Makefile` · 2026-10-14

Petició de l'usuari: un sistema de proves automàtiques prou complet per als revisors externs, i ben documentat. Proposta de Claude Code, acceptada: un executor comú, `autoproves.py`, amb una bateria per comprovació. Cada bateria té un text correcte i un text per cada error que ha d'aturar; cada cas munta un llibre mínim en un directori temporal i hi executa l'eina real, de manera que no toca el llibre ni en depèn. Només demanen Python i git. La taula de la guia es genera de l'script, perquè no es quedi enrere dels casos. Les comprovacions que fan servir eines externes i les de les figures encara no en tenen (`TODO.md`).

## Operació de les sessions

Els perquès de les regles de `CLAUDE.md`.

### D-63

**Una declaració de l'usuari no es verifica: es registra** · `CLAUDE.md §Flux de treball` · 2026-09-23, 2026-10-14 · `397c2da`

El cas: la fusió de les dues seccions d'estat de `CLAUDE.md` (2026-09-23) va descartar tres declaracions de l'usuari per «no verificables», i es van haver de recuperar de git. Des de [D-122](#d-122), es registren les declaracions vigents, en prosa; les que només tenen valor històric són a git.

### D-64

**Fusió de prova abans de tocar un fitxer que una branca de revisió també toca** · `CLAUDE.md §Regles de la revisió externa` · 2026-10-01

El cas: `980434b` (2026-09-25) va afegir un conflicte a `.gitignore` amb `temes456` per no haver-la feta: `!preamble.tex` va caure just al costat del `.DS_Store` que hi afegia la branca, un fitxer que el `TODO.md` ja deia que la branca tocava (`TODO.md §Decisions obertes → Branques del remot`).

### D-65

**Harmonitzar abans que la revisió externa arribi a un fitxer** · `CLAUDE.md §Regles de la revisió externa` · 2026-10-01, 2026-10-14

Amb altres professors dins de la revisió, qualsevol canvi transversal té un cost de coordinació molt més alt: el que es pot harmonitzar s'ha de fer abans que la revisió externa arribi al fitxer, i, als fitxers on ja és en curs, coordinar-ho amb els revisors. L'abast declarat és A1–A8 sencer (2026-10-06). Des del 2026-10-14, que l'usuari va comunicar als revisors que podien reprendre la revisió, un canvi transversal a A1–A8 es coordina amb els equips, i Claude Code treballa per branca ([D-123](#d-123)).

### D-91

**El passat del `TODO.md` va a un arxiu, literal** · Retirada el 2026-10-14: substituïda per [D-122](#d-122); l'arxiu es va esborrar en fer la fase 10b.

### D-122

**Els fitxers operatius només guarden el que serveix d'ara endavant; el passat és a git** · `CLAUDE.md §Flux de treball` i `§Pla de treball` (fase 10) · 2026-10-14 · etiqueta `arxiu/pre-neteja-2026-10-14`

L'usuari va demanar una neteja profunda dels fitxers operatius (`TODO.md`, el seu arxiu, aquest registre, `13_contrib.qmd`, `CLAUDE.md`, les skills): s'hi ha de quedar només el que té sentit per gestionar i millorar el repositori, i el que s'hi guardava només per raons històriques se'n va. La política, proposada per Claude Code i acceptada per l'usuari amb dos matisos seus:

- **Una etiqueta anotada abans de començar**, `arxiu/pre-neteja-2026-10-14` (sobre `ae6c355`), conserva l'estat sencer dels fitxers: és el punt de recuperació, en lloc d'un arxiu dins del repositori.
- **L'arxiu del `TODO.md` s'esborra**, després de moure on toqui el que encara és viu. D-91 es retira en fer-ho.
- **Aquest registre**: cada entrada vigent queda amb la decisió, el perquè i les alternatives descartades. Una cita de l'usuari només s'hi queda si fixa l'abast de la regla, i passa a prosa descriptiva (matís de l'usuari). Una entrada substituïda o sense regla vigent queda reduïda a una línia que diu quan es va retirar i quina la substitueix, perquè l'identificador no canviï i les remissions continuïn resolent. L'historial de l'estat del projecte surt, i l'estat vigent és a `CLAUDE.md`.
- **Les declaracions de l'usuari** ([D-63](#d-63)): es registren les vigents, en prosa, on són vigents. Les que només tenen valor històric són a git.
- **`24_specs/lexic/` es conserva sencer**, amb la documentació de com fer servir els scripts i dels criteris del lèxic (matís de l'usuari).
- **Perquè no tornin a créixer** (fase 10c): una entrada d'aquest registre o del `TODO.md` que canvia s'edita al lloc, sense «Seguiment del…», sense la xifra d'abans al costat de la nova i sense cadenes de procedència; una entrada del `TODO.md` que es tanca s'esborra, i el commit en diu el motiu; el `TODO.md` no porta cap recompte de les seves entrades, que era un registre més per mantenir.

L'alternativa, conservar a l'arxiu un índex curt de les entrades retirades, es va descartar: l'etiqueta ja dona el text sencer, i un índex seria un registre més que caldria mantenir.

### D-123

**Les sessions de Claude Code treballen a la branca `operacions`** · `CLAUDE.md §Flux de treball`, `13_contrib.qmd §Convenció de noms de branques` · 2026-10-14

Proposta de l'usuari, el dia que va comunicar als revisors externs que podien reprendre la revisió: les sessions de Claude Code treballen per branques, com els equips, sempre a la mateixa, `operacions`, i s'hi va fusionant. Fins llavors empenyien directament a `main`, amb el permís de l'editor ([D-59](#d-59)). Amb els equips treballant a les seves branques, els canvis de Claude Code a `main` arribaven sense revisió prèvia i es barrejaven amb els seus.

Detalls, a proposta de Claude Code i confirmats per l'usuari:

- **És una branca permanent**: a l'inici de cada sessió hi entra `origin/main`, i quan l'usuari confirma un bloc, `git merge --no-ff operacions` a `main`. El commit de fusió marca cada bloc a l'historial de `main`.
- **La CI del mirall** hi passa `make comprova-branca` a cada push, com a qualsevol branca que no sigui `main`.
- **Una segona sessió simultània** treballa a `operacions-2`: git no admet alhora una branca `operacions` i una `operacions/<x>`.
