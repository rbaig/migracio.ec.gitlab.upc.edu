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

El prefix de sortida `fi-` és la forma majoritària al corpus. La numeració de les etiquetes quan hi ha dos bucles al mateix bloc és decisió de l'usuari (2026-09-23): no es toca el codi i es documenta la convenció, perquè renombrar-les a `for:`/`fifor:` hi duplicaria etiquetes i el fragment no assemblaria. L'únic cas al corpus, quan es va escriure, era la solució de `s3_4_2.s` (`L3.qmd`), on `moda` té el bucle d'inicialització de l'histograma i el de recorregut de la cadena (`TODO.md §Entrades retirades`, «Etiquetes de bucle heterogènies a L3» i «`fwhile:` → `fiwhile:` al laboratori»).

Fins al 2026-10-07 les etiquetes de sortida numerades eren `ffor1:` i `ffor2:`, a L3 i a l'exemple de la regla, contra el prefix `fi-` de la mateixa regla. Decisió de l'usuari (2026-10-07, fase 7e): `fifor1:` i `fifor2:`, amb els seus salts; el bloc de L3 assembla igual a RARS 1.6 (49 paraules al bolcat de `.text`, idèntiques).

### D-7

**Alineació de la pila: el fet de l'ABI i el criteri d'EC, en dos callouts** · `13_contrib.qmd §T2 i T3` · 2026-10-04 · `552ff1a`

`#nte-abi-alineacio-pila` (el fet: l'ABI exigeix múltiples de 16) i `#imp-abi-alineacio-pila` (el criteri d'EC: múltiples de 4) es van separar el 2026-10-04, a petició de l'usuari.

### D-8

**`.section` no s'utilitza: RARS 1.6 no admet la forma llarga** · `13_contrib.qmd §T2 i T3` · 2026-09-23 · `6fcee2c`

Verificat executant RARS 1.6 el 2026-09-23 (el registre i les ordres de reproducció són a `TODO.md §Entrades retirades`, «Canvi de criteri `.section` — retirat per l'experiment»). Dues fallades, totes dues cares:

- `.section .data` i `.section .text` **no assemblen**: error `.section must be followed by a section name`. Ho causa l'analitzador lèxic —`.data` i `.text` són *tokens* de directiva i, darrere de `.section`, es consumeixen com a directiva pròpia sense arribar-hi mai com a operand—, de manera que no hi ha grafia que ho salvi (tabulador, doble espai, `.SECTION`, `.DATA`, cometes).
- Les formes que **sí** que assemblen són pitjors, perquè fallen en silenci: **`.section` no commuta al segment equivocat, no commuta gens**, i l'assemblador es queda on ja era. Amb un nom reconegut (`.rodata`, `.sdata`) **descarta a més tot el codi que la segueix**, sense cap error ni avís: quatre instruccions queden en una al bolcat i el programa acaba «dropped off the bottom». **No es desen al segment equivocat: desapareixen** —el bolcat de `.data` del mateix programa diu «This segment has not been written to»—, cosa que descarta la hipòtesi natural que acabin com a dades. Contraintuïtivament, un nom **no** reconegut (`.section .foo`) és la forma segura, perquè avisa i conserva les instruccions.

L'experiment va impedir una conversió de 121 directives a la forma llarga que no hauria assemblat.

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

### D-30

**Amplada dels hexadecimals** · `13_contrib.qmd §Criteris generals` · 2026-10-01 · `7d78615`, `171cf18`

Decisió de l'usuari (2026-10-01). L'excepció del format reduït té dos casos, `exr-t7-fallades-programa` i `exr-t8-mv-proteccio`: l'usuari va declarar (2026-10-01) que el format hi és correcte i que s'explicita amb la nota. Fins al 2026-10-07 les tres regles dels hexadecimals (majúscules, amplada i separadors) eren a dos llocs de la guia.

### D-31

**Ordre substantiu–adjectiu** · `13_contrib.qmd §Criteris generals` · 2026-10-01 · `681556a`, `d50b0ba`

Decisió de l'usuari (2026-10-01). Aplicada a tot el corpus el 2026-10-01: el material de T5 (teoria, problemes, solucions, laboratori i figures), després de fusionar `temes456`.

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

**«Imbricat», no «aniuat»** · `13_contrib.qmd §Substitucions obligatòries` · 2026-10-04 · `552ff1a`

Decisió de l'usuari (2026-10-04). «Aniuat», que la taula donava fins llavors com a substitució d'«anidat», no és el terme informàtic en català.

### D-35

**«Lectura/escriptura» per *load/store*** · `13_contrib.qmd §Substitucions obligatòries` · 2026-10-07 · `9f8e746`

Aplicat a tot el corpus el 2026-10-07 (decisió de l'usuari): fins llavors A2 presentava *load* i *store* com a «càrrega» i «emmagatzematge»/«emmagatzemament».

### D-36

**«Ròssec», «semisumador» i «sumador complet»** · `13_contrib.qmd §Substitucions obligatòries` · 2026-10-03 · `e49c014`

«Ròssec» és el terme del Termcat (decisió de l'usuari, 2026-10-03), i substitueix «arrossegament», que el corpus usava fins aleshores. «Semisumador» i «sumador complet» són de la mateixa sessió (fase 5), pendents de confirmar al Termcat.

### D-37

**«Coma flotant», no «punt flotant»** · `13_contrib.qmd §Substitucions obligatòries` · 2026-10-01 · `c1bac38`

És el terme del corpus: 113 ocurrències contra 4, totes a `A2.qmd`, unificades el 2026-10-01.

### D-38

**«Farciment» i «multinucli»** · `13_contrib.qmd §Substitucions obligatòries` · 2026-10-07 · `ca6c01a`, `4625835`

*Padding* → «farciment» és a la taula des del 2026-07-21. *Multicore* → «multinucli» és decisió de l'usuari (2026-10-07), amb el Termcat com a referència.

### D-39

**«Enter» i «natural»** · `13_contrib.qmd §Anglicismes i terminologia obligatòria` · 2026-10-02 · `ee78460`

Proposta de la revisió externa de T3 (`A3.qmd:121`, a `ab48732`) i decisió de l'usuari (2026-10-02), amb l'escombrada del corpus feta el mateix dia.

### D-40

**VPN i PPN, a la taula de sigles** · `13_contrib.qmd §Sigles, símbols i notació` · 2026-10-03 · `8e19383`

Decisió de l'usuari (2026-10-03). Fins llavors el criteri d'exclusió les posava d'exemple de nom de camp exclòs, i la taula les incloïa.

### D-41

**`\texttt{…}`, no `\mathtt{…}`** · `13_contrib.qmd §Codi, matemàtiques i cursiva` · 2026-10-03 · `d61a848`

El corpus feia servir `\mathtt{…}` 44 vegades (S1, S4 i A1) fins al 2026-10-03, i es va unificar a `\texttt{…}` a la fase 7 de `CLAUDE.md §Pla de treball`.

### D-42

**Subíndexs en cursiva també quan són sigles, i l'excepció de les taules ISA** · `13_contrib.qmd §Codi, matemàtiques i cursiva` · 2026-10-03 · `477b9ca`

Totes dues són decisions de l'usuari (2026-10-03, fase 7 de `CLAUDE.md §Pla de treball`) que escriuen l'ús del corpus. A les taules ISA, escriure $PC$ amb `\text{…}` el separaria tipogràficament dels altres operands de la mateixa fórmula.

### D-43

**Operacions lògiques (AND, OR, XOR, NOT)** · `13_contrib.qmd §Codi, matemàtiques i cursiva` · 2026-10-01 · `c4c247a`

Decisió de l'usuari (2026-10-01), que escriu l'ús que el corpus ja feia majoritàriament i n'hi alinea les desviacions.

## Format

### D-44

**Una remissió `@fig-` a cada figura del cos del text** · `13_contrib.qmd §Callouts`, `§Referències creuades` · 2026-10-03 · `e806916`

Decisió de l'usuari 8 de la fase 7c (2026-10-03), aplicada el 2026-10-06 a les 25 figures que no en tenien.

Fins al 2026-10-07, §Referències creuades deia també «Figures i Taules: no han d'estar necessàriament referenciades al text», que la contradeia per a les figures des del 2026-10-03. Decisió de l'usuari (2026-10-07, fase 7e): «Figures sempre, taules opcional».

### D-45

**El títol dels blocs de pseudocodi** · `13_contrib.qmd §Blocs de codi` · 2026-10-01 · `f066a8e`

Decisió de l'usuari (2026-10-01), a partir de l'anotació #4 de la revisió externa de T4. Que «—» surt com a `---` al PDF es va verificar a `make render-complet` el 2026-10-01.

### D-46

**Algorismes en rodona** · `13_contrib.qmd §Blocs de codi` · 2026-10-02 · `f066a8e`

La mateixa decisió que [D-45](#d-45) (anotació #4). Al PDF, la cursiva venia de l'estil *plain* del `\newtheorem` que genera Quarto, i `preamble.tex` la treu redefinint aquest estil (2026-10-02; `TODO.md §Entrades retirades`, «Anotacions de la revisió externa de T4–T6»).

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
| `E3.qmd`/`S3.qmd` @exr-t3-compilacio-relocacio | El problema tracta del **flux de compilació i enllaçat**: el C hi és l'objecte d'estudi, no notació. El `return f(x)` és justament el que fa visible la referència externa que s'ha de resoldre en l'enllaçat. |

### D-50

**Format del codi RISC-V: F1–F5** · `13_contrib.qmd §Estil de codi RISC-V` · 2026-10-03 · `0e25c9f`

Escrit el 2026-10-03 a partir de la proposta d'un *checker* que deixava un marcador a A2. **F5 entra al callout el 2026-10-06** (decisió de l'usuari, a proposta de Claude Code): és l'estil de tota la teoria i les solucions (1 176 línies d'instrucció, contra 596 amb els operands a la columna 13 o 14 als laboratoris i a E2–E4 i E8, i 93 amb un sol espai), i és on cauen els operands del codi que genera `gcc -S`, amb tabuladors de 8. Els operands ja se separaven amb una coma i un espai (1 799 de 1 799 línies amb comes). La columna dels comentaris no es regula perquè 199 dels 213 blocs amb comentaris ja els tenien en una sola columna. Decidit per l'usuari perquè la reunió del grup de treball del 2026-10-05 no ho va arribar a tractar.

## Figures

### D-51

**El `<desc>` com a text alternatiu, i una mida comuna a l'HTML** · `13_contrib.qmd §Figures i material gràfic` · 2026-10-06 · `e806916`

Que el `<desc>` no repeteixi el peu és la decisió 6 de la fase 7c (2026-10-03). L'amplada del `viewBox` per 1,4 a l'HTML és decisió de l'usuari (2026-10-06).

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

Decisió de l'usuari 4 de la fase 7c.

### D-56

**Imatges sense peu centrades als callouts del PDF** · `13_contrib.qmd §Presentació visual` · 2026-10-06 · `74507d7`

Fins al 2026-10-06 sortien alineades a l'esquerra. Quan es va escriure, totes les imatges sense peu dels callouts eren figures de registres més amples que el callout, de manera que la regla no hi tenia cap efecte visible: és per a la primera que no ho sigui.

### D-57

**Fórmules en línia a l'HTML: `overflow` només a les llargues** · `13_contrib.qmd §Presentació visual` · 2026-10-06 · `74507d7`

Fins al 2026-10-06 l'`overflow-x: auto` era a totes, i un `inline-block` amb un `overflow` que no sigui `visible` es recolza en la vora inferior (CSS 2.1 §10.8.1): les fórmules pujaven d'1 a 6 px per sobre de la línia de text (mesurat a A6, 40 fórmules) i feien créixer l'interlineat. Després del canvi, a l'escriptori, cap fórmula d'A4, A5, A6 i S6 no era llarga i totes eren a 0 px de la línia; en un mòbil de 375 px, n'eren llargues 4, 14, 2 i 1.

## Eines

### D-58

**`make render-complet`, obligatori abans de tocar el PDF** · `13_contrib.qmd §Verificació de l'entorn` · 2026-09-22 · `5589801`

Un render HTML no exercita el PDF: el 2026-09-22 el corpus tenia **83 blocs `when-format="pdf"`**, i almenys cinc convencions de la guia existien precisament perquè el PDF es comporta diferent (la duplicació de figures si no se separen les variants, `tbl-colwidths` que ha de sumar 100, les capçaleres `###` del laboratori, `[@sec-]` que només funciona a PDF, i la guia mateixa, que és HTML-only).

### D-62

**Les afirmacions sobre RARS es resolen executant RARS, i el `.jar` fora del repositori** · `13_contrib.qmd §Verificació empírica a RARS` · 2026-09-23 · `6fcee2c`, `fbf7c3d`

Ja ha passat dues vegades: la comprovació que RARS alinea `.dword` a 4 bytes i no a 8, com demana l'ABI (a L2 des del juliol del 2026 com a molt tard; des del 2026-10-03, la nota de `@nte-directives-alineacio-inicialitzacio` a A2 i el `.align 3` de la solució de `s2_1_1.s`), i l'experiment de `.section` (2026-09-23, [D-8](#d-8)), que va impedir una conversió de 121 directives que no hauria assemblat. Que es comprovi pel resultat i no per l'absència d'error ve del mateix experiment: tres de les formes provades assemblaven sense queixar-se i no feien el que semblava (el cas, a la skill `rars`).

El `.jar` va ser al repositori fins a `fbf7c3d` (2026-07-11), que el va eliminar deliberadament. El procediment de les sessions de Claude Code, que eren a la mateixa secció de la guia fins al 2026-10-07, és a la skill `rars`.

### D-59

**Push directe a `main`: la restricció és per als revisors, no per a l'editor** · `13_contrib.qmd §Push directe a main` · 2026-04-29, 2026-10-07 · `1d4308d`

La restricció als canvis trivials és del 2026-04-29. Declaració de l'usuari (2026-10-07, fase 7e): «La restricció és per als revisors externs. No per a l'editor, que soc jo, fins al segon quadrimestre d'aquest curs (2026-27).» Fins llavors la guia no ho deia, i les sessions de Claude Code empenyien a `main` canvis grans (`3ee92f4`, per exemple, toca 19 fitxers) amb l'autorització de `CLAUDE.md`, en contradicció aparent amb la regla.

### D-60

**DejaVu Sans Mono, la font monoespaiada del PDF** · `13_contrib.qmd §Renderitzar el projecte` · 2026-10-06 · `74507d7`

Des del 2026-10-06. Amb DejaVu Sans Mono el registre de LaTeX ja no hi dona cap «Missing character». Escalada a l'altura de les minúscules del text, és més estreta que Latin Modern Mono, i cap bloc de codi ni cap taula no surt del marge (`pdftotext -bbox`).

### D-61

**El hook d'abans del commit avisa, però no pregunta** · `13_contrib.qmd §IAs` · 2026-10-03 · `722c522`, `980434b`

Fins al 2026-10-03 la revisió de prosa i l'avís de `make render-complet` demanaven confirmació; decisió de l'usuari: no cal, perquè el flux ja fa `make render-complet` abans de cada push. El `make render` del hook va trigar **2 min 38 s** el 2026-09-25.
