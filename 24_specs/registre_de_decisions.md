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

### D-70

**Punter cap endavant T3 → T6: temps d'execució i CPI** · `13_contrib.qmd §Referències creuades` · 2026-10-08

Decisió de l'usuari (2026-10-08, fase 7g, decisió 8), a proposta de Claude Code. Dos problemes de T3, `exr-t3-bucles-for` (apartats c i d) i `exr-t3-bucles-multiplicacio` (apartats d i e), demanen temps d'execució i CPI, que la teoria presenta a T6 (`@eq-texe2`); a A1–A3 i E1–E2 no hi ha cap ocurrència de «CPI» (mesurat a `7a1640e`). Venen de l'original de MIPS, on el rendiment era a T1. L'alternativa, treure o moure aquells apartats, es va descartar: la dependència és de càlcul, amb la fórmula citada a la solució (S3), i es pot seguir com a punter explícit.

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
| `P3.qmd`/`S3.qmd` @exr-t3-compilacio-relocacio | El problema tracta del **flux de compilació i enllaçat**: el C hi és l'objecte d'estudi, no notació. El `return f(x)` és justament el que fa visible la referència externa que s'ha de resoldre en l'enllaçat. |

### D-50

**Format del codi RISC-V: F1–F5** · `13_contrib.qmd §Estil de codi RISC-V` · 2026-10-03 · `0e25c9f`

Escrit el 2026-10-03 a partir de la proposta d'un *checker* que deixava un marcador a A2. **F5 entra al callout el 2026-10-06** (decisió de l'usuari, a proposta de Claude Code): és l'estil de tota la teoria i les solucions (1 176 línies d'instrucció, contra 596 amb els operands a la columna 13 o 14 als laboratoris i a E2–E4 i E8, i 93 amb un sol espai), i és on cauen els operands del codi que genera `gcc -S`, amb tabuladors de 8. Els operands ja se separaven amb una coma i un espai (1 799 de 1 799 línies amb comes). La columna dels comentaris no es regula perquè 199 dels 213 blocs amb comentaris ja els tenien en una sola columna. Decidit per l'usuari perquè la reunió del grup de treball del 2026-10-05 no ho va arribar a tractar.

### D-66

**Pseudoinstruccions: un sol esquema de columnes i un sol prefix de títol** · `13_contrib.qmd §Fitxer de referència tècnica`, `§Callouts` · 2026-10-07 · `75ea6c6`

Fins al 2026-10-07 les taules de pseudoinstruccions tenien cinc esquemes de columnes: «Pseudoinstrucció, Operació, Expansió», «Pseudoinstrucció, Expansió, Ús», «Pseudoinstrucció, Condició, Expansió», «Pseudoinstrucció, Expansió, Condició» i «Pseudoinstrucció, Expansió». «Condició» hi volia dir dues coses: a `li`, quan s'aplica cada expansió; als salts amb zero, la condició del salt, escrita amb la sintaxi de C («salta si `rs == 0`») i no amb la de les taules ISA. `fmv.s`, `csrr` i `csrw` eren files de taules ISA (les dues de Zicsr, amb «Tipus I»). Els títols feien servir tres prefixos: «Pseudoinstrucció —» (A2, A3 i A4), «RV32I ABI —» (els salts d'A3 i el compendi) i «RV32F ABI —» (A5).

L'esquema de l'operació és el de les taules ISA perquè la pseudoinstrucció es llegeix al costat de la instrucció en què s'expandeix. La columna «Ús» de `j`, `jr` i `ret` es va treure sense perdre res: el rang de ±1 MiB és a la prosa d'A3 (`jal`), i el retorn de subrutina, a §Subrutines. El prefix no porta extensió, com «Directives —», perquè les pseudoinstruccions no són ISA ni ABI: les defineix el manual de l'assemblador (*RISC-V Assembly Programmer's Manual*, `riscv_asm_manual` a `15_bibliografia.bib`).

Era l'opció B de l'entrada del `TODO.md` «Unificar el format de les taules de pseudoinstruccions». El 2026-10-03 (fase 7b) l'usuari va triar l'A, que unificava A2 i afegia `la` al compendi, perquè la B tocava fitxers en revisió externa. La B es va decidir el 2026-10-07 (declaració de l'usuari, que accepta la proposta de Claude Code: «Propostes acceptades: 1, 2 i 3»), per fer-la abans que els equips de revisió comencin (fase 7f de `CLAUDE.md §Pla de treball`). El prefix, «Pseudoinstruccions —», la columna de `li` i l'abast (`fmv.s`, i `csrr` i `csrw` a A9 i al compendi), decisions de l'usuari del mateix dia, a proposta de Claude Code.

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

### D-68

**Els originals substituïts per una figura generada es conserven** · `13_contrib.qmd §Convencions SVG` · 2026-10-04 · 2026-10-07

Decisió de l'usuari del 2026-10-04 (fase 7c), quan A3 va passar a consumir els BA de `multi` i d'`exemple` generats per `gen_BA.py`: els originals es conserven, perquè l'usuari també els fa servir per a les diapositives, i les esmenes que necessitin les fa ell mateix (`TODO.md §Tasques per tema → T3`, «Retocs manuals pendents»). Fins al 2026-10-07 només constava a `24_specs/svg.md §17` i a l'inventari, que els llista a part dels orfes. Es va escriure com a regla el 2026-10-07 (fase 7f), en conservar també, per decisió de l'usuari, els originals de `T3_ba_func`, `T3_ba_general`, `T3_mapa_memoria`, `T3_pila_uninivell` i `T3_pila_multinivell`.

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

### D-74

**Calendari del laboratori: `verifica_calendari.py`, l'agent `verificador-calendari` i el hook** · `13_contrib.qmd §IAs` · 2026-10-08

Decisió de l'usuari (2026-10-08, fase 7g): «Com que canviarà a cada quadrimestre, escriu un agent per fer-ne la comprovació i afegeix-lo al protocol de comprovació de commits que afectin a `Lcalendari.qmd`». L'auditoria de la fase hi va trobar una data que no cau en el dia de la seva fila (el 07/05/2026, dijous, a la fila dels divendres). La part mecànica (dates, dies, ordre i sessions) la fa un script, perquè no depengui del model; el que demana judici (quadrimestre vigent, festius, una data amb l'horari d'un altre dia), l'agent, que només informa. El hook d'abans del commit hi afegeix el pas 4, que no bloqueja, com els altres avisos (D-61). Al mateix temps, el calendari passa a ser només de l'HTML: al PDF, un capítol «Calendari» amb la remissió al web (abans hi sortia un capítol buit amb el títol del quadrimestre, perquè Quarto en treia el títol fora del bloc HTML).

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

## Historial de l'estat del projecte

Fins al 2026-10-07 era a `CLAUDE.md §Revisió interna`, §Estat dels materials i §Pla de treball. Les declaracions de l'usuari es conserven literals; el detall de cada tancament de tema és a `TODO.md §Entrades retirades`.

### Revisió interna

El contingut de teoria (T1–T9), laboratori (L1–L6) i solucions (S2–S8) es va generar abans de la revisió. **La revisió interna és tancada sencera**, per declaracions de l'usuari: teoria i laboratori el 2026-09-23, enunciats i solucions el 2026-10-01.

- **Teoria: tancada, T1–T9, el 2026-09-23** (declaracions de l'usuari, una per tema, al llarg del Bloc 4d). El tancament de cada tema —amb l'estat que tenia, el commit que el declarava i què en sobreviu— és a `TODO.md §Entrades retirades`. Quatre casos hi van necessitar una decisió o una execució abans de tancar-se: **T5** (revisió declarada «parcial»: auditats els 29 ítems del seu registre, executats els tres que restaven), **T6** (S6 harmonitzada sencera a $V_{CC}$), **T7** (C3, l'enunciat truncat d'`exr-t7-assoc-multinivell`, reparat contra el PDF original) i **T9** (contradicció entre l'assumpte del commit i el registre, resolta per decisió a favor del registre).
- **Enunciats i solucions: tancats, `E1.qmd`–`E9.qmd` i `S1.qmd`–`S9.qmd`, el 2026-10-01.** Declaració de l'usuari, literal: «les revisions internes es poden donar per acabades». `E3.qmd` i `S3.qmd` ja hi constaven com a completats des del 2026-07-12 (`614f576`). ⚠️ Fins al 2026-10-01, `CLAUDE.md` deia que els altres setze fitxers eren «pendents d'un pas combinat», i des del juliol no era cert: la frase es va escriure el 2026-06-19 (`879f3e7`), quan els fitxers encara es deien `PE_Tx` i `PS_Tx`, i `614f576` només en va canviar els noms. Les revisions de tema de juliol ja eren A-E-S conjuntes: els nou registres declaren E<x> i S<x> com a abast (`git show a211bbf:TODO/T<x>_P_tasques.md`, al títol o a «Fitxers objectiu»), i els de T6 i T7 diuen literalment «pas combinat E6+S6» i «E7+S7 (adaptació + revisió pròpia)». La skill `/pas-combinat` (`980434b`), feta sobre aquella frase sense preguntar a l'historial, es va retirar amb ella.
- **Laboratori: tancat, `L1.qmd`–`L6.qmd`, el 2026-09-23** (declaracions de l'usuari, una per fitxer). Dos avisos que el tancament no esborra, perquè descriuen l'historial i seguiran despistant qui el llegeixi:
  - ⚠️ **`ca6c01a` es diu «L6 Fase B» però conté la Fase C sencera**: toca els quatre fitxers que el registre de L6 llistava com a modificats (`L6.qmd`, `A7.qmd`, `13_contrib.qmd` i el registre mateix), i s'hi verifiquen els ítems de Fase C (literals als `.space`, «farciment», l'exercici nou `s6_4_5`, la correcció d'`A7.qmd`). L'assumpte del commit enganya; el contingut, no.
  - ⚠️ **`3cae913` és l'únic commit de revisió que ha tocat mai `L4.qmd`**, i el seu assumpte diu que és *previ* a les passades finals. L'usuari les va donar per cobertes en tancar L4.

«Fase C executada» **no** volia dir «revisió interna acabada». Entre les dues hi havia les *passades finals*, i el tancament es declarava per separat per a les tres revisions —**pedagògica, tècnica i lingüística**—. Com es va tancar cada ítem és a `TODO.md §Entrades retirades → Executades` («Passades finals pendents»), i la plantilla que feia les tres preguntes, a l'historial (`git show 980434b:26_prompts/Lx__revisio_interna__plantilla.md`).

Les capçaleres `##`–`####` de tots els `A1.qmd`–`A9.qmd` tenen etiqueta `{#sec-}` (estat que `CLAUDE.md` registrava com a «complet»; la mesura és a `TODO.md §Mesura dels slugs`).

### Revisió externa

La revisió interna tancada és la **condició prèvia** de l'externa, que fan altres professors de l'assignatura.

- **T4, T5 i T6, a `temes456` (MR `!7`).** El grup de treball hi va revisar `A4.qmd`, `A5.qmd` i `A6.qmd` del 21 de juliol al 7 d'agost (11 commits). Una fusió de prova (2026-10-01) donava tres conflictes: `A4.qmd`, `A5.qmd` i `.gitignore`. **La MR es va tancar sense fusionar el 2026-10-01** (`pedro.martinez.ferrer`, 16:21; GitLab la marcava `cannot_be_merged`). Decisió de l'usuari (2026-10-01, al vespre, substituint la d'esperar el grup): **la fusió la fa una sessió de Claude Code**, amb l'aprovació de l'usuari de cada conflicte resolt abans del push. Fusionada el mateix dia: `451c3ef` (commit de fusió, autoria dels 11 commits conservada), seguida de `40396e8` (errades que portava la branca) i `454a82e` (marca dels termes anglesos, de les sigles i d'«A **EC**», restaurada per decisió de l'usuari). Les 10 anotacions de la branca van passar a marcadors a `main`.
- **T3, a `contingut/t3-traduccio` (MR `!5`, Pedro J. Martinez-Ferrer, 2026-07-06).** Un sol commit, amb rutes d'abans de la reorganització de directoris, que git no pot fusionar. El port a les rutes actuals l'havia de fer l'autor de la MR (decisió de l'usuari, 2026-10-01). **La MR es va tancar sense fusionar el 2026-10-01** (16:20, el mateix autor). Decisió de l'usuari (al vespre): **el port el fa una sessió de Claude Code**, hunk a hunk i amb `Co-authored-by` de l'autor. Portada el mateix dia: `ab48732`. Els vuit comentaris del revisor van ser marcadors a `main`; set es van resoldre el 2026-10-02 (fase 3b) i el vuitè, la «↔» d'`A3.qmd:322`, a la fase 4 (`0d7bd5c`).
- **T8, a `tema8` (MR `!8`, Adrià Armejach, 2026-10-05 i 06).** 32 commits sobre `A8.qmd`, `A9.qmd`, `E8.qmd`, `S8.qmd`, `13_contrib.qmd §T8` i les figures de T8 (`gen_T8.py`): el TLB passa al model de RISC-V. **Fusionada a `main` el 2026-10-06 per l'usuari, des del GitLab, sense conflictes: `80f8946`**, amb commit de fusió i sense *squash*. **La revisió és parcial**: la descripció de la MR diu «Canvis fets fins a la secció 8.7 (exclosa)», de manera que §Integració del TLB i la memòria cau encara no s'ha revisat. La branca es conserva, perquè el revisor hi pugui continuar.
- **La resta d'A1–A8 (T1, T2, T7 i el que queda de T8), i una segona volta de T3–T6.** Declaracions de l'usuari (2026-10-06): la revisió externa afecta, de moment, **A1–A8**, «també T3--T6»; **A9, Ex, Sx i Ly en queden fora** de moment, i **les branques les crea cada equip**. El mateix dia no hi havia cap revisor extern actiu ni cap branca d'equip a `origin` (`git ls-remote --heads origin`: `main`, `tema8`, ja dins de `main`, `temes456` i `contingut/t3-traduccio`).

### Fases del pla de treball

El pla es va refer el 2026-10-01 sobre l'inventari del grup de treball de T4–T6 (`TODO.md §Decisions obertes → Anotacions de la revisió externa de T4–T6`, avui a §Entrades retirades), i va substituir el del matí del mateix dia, en què la línia 1 era «esperar el grup de treball». Les fases 1 i 2 anaven abans que les altres perquè, mentre la revisió de T3–T6 no fos a `main`, cada canvi que hi entrés era un conflicte més. Les harmonitzacions de la línia 2 de l'antic pla fora d'A3–A6 es van fer el 2026-10-01 (`TODO.md §Entrades retirades`). Descripció de cada fase feta, tal com era a `CLAUDE.md`:

- **1. Integració de la revisió externa** (decisions de l'usuari, 2026-10-01). Fusionar `temes456` amb un commit de fusió, sense *rebase*, per conservar l'autoria dels 11 commits, i resoldre els 3 conflictes (`A4.qmd`, `A5.qmd`, `.gitignore`) conservant alhora els canvis dels revisors i les harmonitzacions de `main`. Portar `!5` a `A3.qmd` i `21_riscv/` hunk a hunk, amb `Co-authored-by` de l'autor. Abans del push, presentar a l'usuari la resolució de cada conflicte i els casos dubtosos del port. Registrar al `TODO.md` les 10 anotacions [br] i fer `make render-complet`. ✅ Feta el 2026-10-01: `temes456` fusionada (`451c3ef`, `40396e8`, `454a82e`), `!5` portada (`ab48732`), anotacions de totes dues registrades i `make render-complet` net.
- **2. Harmonitzacions pendents a A3–A6**: tornar a passar totes les escombrades del 2026-10-01 (la branca porta text d'abans): cometes (`A4.qmd:119`), «precisió simple» al material de T5, «l'X següent», amplada dels hexadecimals, tanques i quatre formats a A3; la regla d'`AND`/`OR` (decisió de l'usuari, `13_contrib.qmd §Codi, matemàtiques i cursiva`), i la convenció de l'anotació #4 (algorismes, blocs «Pseudocodi»), escrita i aplicada als títols; la cursiva dels algorismes, a la fase 4. ✅ Feta el 2026-10-01 (`d50b0ba`, `2693ec3`, `f066a8e` i el format U a T2).
- **3. Estructura pedagògica**: anotacions #12 (reordenar §Potència), #9 (temps i rendiment a §Definicions) i #3 (moure `#cau-sobreeiximent-extensio-m`). ✅ Feta el 2026-10-01 (`4759902`, `457e9cd`, `666835c`): les tres resoltes i els cinc marcadors esborrats; l'ampliació de #12 va quedar a la fase 6.
- **3b. Revisió externa de T3** (afegida el 2026-10-02): valorar i resoldre els set comentaris de contingut de Pedro J. Martinez-Ferrer. ✅ Feta el 2026-10-02 (decisions de l'usuari, a proposta de Claude Code; de `fec6d95` a `4a5cad5`): criteri de traduccions literals, «enter»/«natural» amb escombrada i regla a `13_contrib.qmd`, `slli` per a vectors i matrius, «NOT», fusió dels callouts *lazy*, bucles `while` → `do-while` → `for` i `.global` fora de T3. La «↔» (`A3.qmd:322`) va quedar a la fase 4.
- **4. Una sola passada de render** (HTML clar i fosc, i PDF): anotacions #7, #8, #10 i #11, la cursiva dels algorismes al PDF (#4), la «↔» d'`A3.qmd:327` i la figura de `#nte-instruccions-tipus` d'A2, que mostrava els set formats en lloc de R, I i S (`TODO.md §T2`, avui a §Entrades retirades). ✅ Feta el 2026-10-02 (`0d7bd5c`, `e532380`, `70865b6`, `c450782`): #8 verificada sense canvi, #11 partida, cursiva fora (`preamble.tex`), «↔» → «LSb». #7, #10 i la figura d'A2 ja no eren de render: SVG retocats i una variant a `gen_regs.py` (`COMPENDIS`), fets amb Opus per decisió de l'usuari.
- **5. Figures** #1 i #2 (*half-adder*, *full-adder*, cadena amb XOR), en SVG natiu segons `24_specs/svg.md`. ✅ Feta el 2026-10-03 (`e49c014`, `184832c` i el commit de la #2): `#fig-semisumador-sumador-complet` i `#fig-sumador-propagacio-rossec`, generades per `25_scripts/gen_T4_sumador.py`, i la convenció de portes a `svg.md §16`. De pas, decisions de l'usuari: *carry* → «ròssec» a tot el corpus, i «semisumador» i «sumador complet», pendents de confirmar al Termcat.
- **6. Decisions per als revisors**: #5 R4-TYPE, #6 R5-TYPE i l'ampliació de #12. ✅ Feta el 2026-10-02 (decisions de l'usuari, a proposta de Claude Code): #6, no (`1ca023a`); #5, sí, com a aprofundiment (`0fb688a`); ampliació de #12, sí, com a aprofundiment (`99be9b8`). En analitzar #5 es va trobar l'errada de la figura de `#nte-instruccions-tipus` d'A2, que va anar a la fase 4.
- **7. Símbols i notació** (`12_sigles_simbols.qmd`), després de les fases 1 i 2, perquè llegeix A3–A6. ✅ Feta el 2026-10-03 (decisions de l'usuari, a proposta de Claude Code; de `a5340f3` a `d61a848`): CPI i la resta de sigles dins de fórmules amb `\text{}`; S6 i E6 amb la notació d'A6 (guany, Amdahl, potència); una sola notació per a la divisió de T4; el glossari verificat contra el corpus (Símbols 100 → 109 files, Notació 17 → 27), i les excepcions de subíndexs i de taules ISA escrites a `13_contrib.qmd`. Toca A3–A6 (notació, i una correcció a A5), cosa que el grup de revisió ha de saber. En van sortir dues entrades del `TODO.md`: «guany» per *speedup* a E6 i S6 (fase 7b), i VPN i PPN a Sigles (decidida el mateix dia, `8e19383`).
- **7b. Neteja prèvia a la revisió externa de la resta** (afegida el 2026-10-03): tancar els pendents dels fitxers que entraran a la fase 8, perquè cap revisor no hi trobi marcadors ni incoherències. A2: verificar la taula de restriccions d'alineació contra l'ABI `ilp32`, unificar el format de les taules de pseudoinstruccions i la taula de `#tip-codificacio-instruccions`, que sortia del callout al PDF. E6, S6 i `S_criteris_seleccio.qmd`: «guany» per *speedup*. L2: decidir l'alineació de `.dword` a RARS. Format del codi: aplicar el que decidís la reunió del grup de treball del 2026-10-05 (consens i alineació dels operands, `TODO.md §Decisions obertes` → «Criteris de codi C»). Ja fet el 2026-10-03, abans d'obrir-la: Load/Store/Branch → Lectura/Escriptura/Salt (`9a292eb`), VPN i PPN (`8e19383`) i el *checker* de format amb la indentació (`c27c68a`). ✅ Feta el 2026-10-03, excepte el format del codi, que esperava la reunió (decisions de l'usuari, a proposta de Claude Code; de `5684c8a` a `a7876b9`): la taula d'alineació, correcta, amb l'alineació dels punters i el límit de la relaxació de `sp`; `.dword` a RARS, que només s'alinea a 4 (error d'A2), i L2 amb una sola solució i `.align 3`; `la` amb taula i al compendi; la taula de codificació, dins del callout; «guany» a E6, S6 i `S_criteris_seleccio.qmd`; i el literal de `.dword` d'E2 i S2, que RARS llegia amb signe. ✅ El format del codi, fet el 2026-10-06 (decisió de l'usuari, perquè la reunió no ho va tractar; `0e25c9f` i el commit següent): operands a la columna 16 (F5) al callout `#imp-codi-format-criteris`, el format no s'avalua per si mateix, i 849 línies reformatades a A1–A3, A5, A9, E2–E4, E8, S2, S4, S5 i L2–L6. Toca A3 i A6 (una frase i una cursiva), cosa que el grup de revisió ha de saber. En van sortir quatre entrades del `TODO.md`: l'opció B de les pseudoinstruccions, les etiquetes dins dels `#nte-`, la distribució de columnes de totes les taules i `auipc` al compendi.
- **7c. Figures** (afegida el 2026-10-03): la revisió general de les figures de `TODO.md §Tasques transversals` («Revisió general de les figures i generació per script», detallada a `608a71f`: inventari, integració, model de generació, pilot de T7 i figures dinàmiques), amb les pendents de T7 i T8, les taules de memòria de T2 i el gris del text de figura. ✅ Feta del 2026-10-03 al 2026-10-06 (decisions de l'usuari 1–13, a proposta de Claude Code; de `1f5f006` a `e806916`, en dotze blocs): inventari de figures pel contingut (`make inventari`), 29 fitxers orfes retirats, generadors al pre-render (`__BA`, `__subrutina`, `__MC`, `__memoria`) i de model (a) amb `--comprova` (`gen_T4_sumador.py`, `gen_T7.py`, `gen_T8.py`), totes les figures de T7 i T8 en SVG natiu, figures dinàmiques a l'HTML, les taules de memòria de T2, text alternatiu des del `<desc>`, una mida comuna a l'HTML i una remissió a cada figura del cos del text. Toca A3–A6 (remissions i, a A3, figures), cosa que el grup de revisió ha de saber. ✅ Les dues entrades noves, fetes el 2026-10-06 (decisions de l'usuari D1–D8, a proposta de Claude Code; `d59ae41`, `c7180d9`, `77e6bce` i `42ac228`): les tres taules de MC de T7, de `gen_MC.py` (estil `estat`), amb els originals retirats; els colors fora de la paleta, migrats, i `#e6f1fb` i `#dee2e6`, afegits a `svg.md §10`; les figures de T6, sense `textLength` i amb la notació d'A6; i la resta d'avisos de l'inventari. Toca SVG de T3–T6 i A2, A7 i A9; declaració de l'usuari (2026-10-06): ara mateix no hi ha cap revisor extern actiu. En van sortir dues entrades del `TODO.md`: la revisió de la paleta per reduir-ne els colors i el ✓ que no surt al PDF.
- **7d. Tasques independents dels equips de revisió** (afegida el 2026-10-06, continuació de la 7c, amb les declaracions de l'usuari del mateix dia sobre l'abast A1–A8 i les branques per equip). ✅ Feta del 2026-10-06 al 2026-10-07 (recomanacions de Claude Code acceptades per l'usuari, i les decisions puntuals que no cobrien; de `82e7c99` a `35be646` i el commit del bloc 5), en sis blocs: (0) registre de l'abast i neteja del `TODO.md`; (1) A1–A8, abans que els equips en parteixin: la freqüència de sostre d'A6, com la d'A7 i datada cap al 2003–2005, i `auipc` presentada a A2, amb fragment de `21_riscv/` i taula al compendi (de pas, una errada tècnica d'A3 sobre l'expansió de `la`); (2) render: ✓ i DejaVu Sans Mono al PDF, imatges centrades als callouts, fórmules en línia alineades a l'HTML, marcadors del PDF amb els títols curts i hash del commit a la data; (3) A9, Ex, Sx i Ly: «d'arrencada en fred» en lloc de *cold-start*, la taula de T1 de `S_criteris_seleccio.qmd` i el bloc no autònom deduït a `verifica_laboratoris.py`; (4) les 296 taules del PDF verificades amb una eina nova, `verifica_taules.py`, i 52 corregides; (5) `codi_erroni` a `13_contrib.qmd`, la taula de figures externes (la foto de T7 és CC0 1.0, no CC BY-SA 2.0: `.bib` corregit) i el glossari anglès–català generat (`gen_glossari.py`). Abans de cada bloc que tocava A1–A8, `git ls-remote --heads origin`: cap branca d'equip. Toca A1–A6, A9 i el compendi, cosa que els equips han de saber. `TODO.md`: 33 → 23 entrades. Seguiment del 2026-10-07 (decisions de l'usuari sobre els pendents; `9f8e746` i el commit següent): «lectura/escriptura» per *load/store* a tot el corpus (69 substitucions en 16 fitxers), els glifs que faltaven al PDF (`\newunicodechar`), les marques `codi_erroni` d'A2, una sintaxi pròpia de RISC-V i RARS per als blocs `.s` (`24_specs/riscv.xml`), i la llista de llocs i solucions de l'HTML al mòbil. `TODO.md`: 23 → 21. Després, el mateix dia: «Solució» a les referències `@sol-` del PDF, les quatre correccions de l'amplada del mòbil (totes les pàgines a 375 px) i, al glossari, «farciment» i «multinucli» (`TODO.md`: 21 → 20).
- **7e. Partir `13_contrib.qmd`** (`TODO.md §Tasques globals → Eines`): les regles per a humans al capítol «Contribueix-hi», l'historial al registre de decisions i els procediments de Claude Code a skills; i aprimar `CLAUDE.md`. Acceptada per l'usuari el 2026-10-07 («Propostes acceptades: 1, 2 i 3»), a proposta de Claude Code, abans de la fase 8, perquè els revisors llegiran `13_contrib.qmd`. Inventari previ de cada paràgraf, acceptat per l'usuari amb les seves decisions: el nom i el format d'aquest registre i el criteri de què hi va; els casos de les regles de les skills, al costat de la regla; «Problemes» i «Solucions» (D-24); les fonts lèxiques per ordre (D-29); l'excepció del push de l'editor (D-59); §T9 «Mode S» reformulada (D-21); el web a `https://rbaig.github.io/migracio.ec.gitlab.upc.edu/`; i, durant la fase, `fifor1:`/`fifor2:` a L3 (D-6) i les figures sempre referenciades (D-44). ✅ Feta el 2026-10-07, en cinc commits (`f2c8ed2`, `924321a`, `c0f44b9`, `de004da` i el que retira l'entrada del `TODO.md`): `13_contrib.qmd`, de 1 408 a 1 038 línies (de 137 a 104 KB); `CLAUDE.md`, de 36,8 a 14,3 KB; aquest registre, amb 65 entrades i l'historial; quatre skills (`escombrada`, ampliada, `render`, `rars` i `figures`); i `README.md` sense els duplicats de la guia. Comprovació mecànica final: tots els fets de les línies tretes són en algun destí, tret dels descartats amb motiu, i cap frase llarga no és a dos fitxers. En surten tres entrades del `TODO.md`: Zifencei a T9, `Zicsr_pseudo_immediats.qmd` orfe i els usos d'«exercici» per a un problema.
- **7f. Pseudoinstruccions (opció B) i família de figures de memòria d'A3** (`TODO.md §Decisions obertes` i `§Tasques globals → SVG`): un sol esquema de columnes i un sol prefix de títol a les taules de pseudoinstruccions d'A2–A5 i del compendi; i el pla del generador de BA, amb un generador germà per a les piles i el mapa de memòria, la classe `estreta` i el `#cc0000` de les piles. Acceptada per l'usuari el 2026-10-07 («Propostes acceptades: 1, 2 i 3»), a proposta de Claude Code, per fer-la abans que els equips de revisió comencin. ✅ Feta el 2026-10-07 (decisions de l'usuari P1–P5 i F1–F8, a proposta de Claude Code), en dos commits. `75ea6c6`: l'esquema «Pseudoinstrucció, Operació, Expansió» a les 19 taules, amb «Condició» a `li`, i el prefix «Pseudoinstruccions —» (D-66), amb `fmv.s`, `csrr` i `csrw` fora de les taules ISA. El commit següent: `gen_mapa.py` (sufix `__mapa`, D-67) i `gen_BA.py` ampliat, amb les primitives compartides de `columna_memoria.py`; el mapa de memòria, les dues piles en fila i els BA de `func` i el general, generats; dos BA nous a les solucions de L3 i S3, en lloc de les taules, i les dues taules de desplaçaments d'A3, fora; la classe `estreta`, amb `w_rect` de 244 px; les vores de cada zona, per dins (`svg.md §7`), i un byte continu a cada extrem dels trams elidits (§4), després de revisar les figures; el `#cc0000` fora de les piles; `ba.toml` i `mc.toml` passen a `BA.toml` i `MC.toml`; i la conservació dels originals substituïts, escrita com a regla (D-68). Abans de cada bloc, `git ls-remote --heads origin`: cap branca d'equip. Toca A2–A5, A9, el compendi, L3 i S3, cosa que els equips han de saber. `TODO.md`: 24 → 23, amb tres entrades noves: els 23 títols de callouts `#nte-` amb un prefix de fora de la llista, l'escombrada d'«offset» i les vores compartides de la resta de figures.
- **7g. Control de qualitat fora de la revisió externa i petits pendents** (`TODO.md §Tasques transversals`, `§T4` i `§Tasques globals → Contingut global`): una passada tècnica i lingüística d'A9, els problemes, les solucions i el laboratori, que la revisió externa no cobreix (declaració de l'usuari, 2026-10-06), amb els subagents i els verificadors i la coherència amb la 7d i la 7f; l'slug `#sec-casos-especials` d'A4; i les línies partides dels blocs de codi al mòbil. Acceptada per l'usuari el 2026-10-07 («Propostes acceptades: 1, 2 i 3»), a proposta de Claude Code. ✅ Feta el 2026-10-08 (decisions de l'usuari 1–12 i ítems nous del mateix dia, a proposta de Claude Code), en nou commits: `ca02ad8`, l'slug, `#sec-casos-especials-divisio`; `753a74b`, la sagnia de continuació de les línies partides (de 2 500 línies mal alineades a 0 al mòbil); `bc478ba`, els blocs de codi del PDF, que ja no floten (D-69; de 588 a 569 pàgines), trobat perquè l'usuari no veia l'RSE d'A9; `f450bad`, `40bd0d6` i `210e6de`, les troballes de 34 informes dels subagents sobre `7a1640e`: totes les errades (A9, P3–P6, P8, S2–S8, L1, L2, L4–L6 i `index.qmd`, verificades amb Python i RARS 1.6; les fallades de L6, amb les classes del simulador), totes les harmonitzacions (veu dels enunciats i de les solucions, L/E, línies de MC a L6, la terminologia d'A8 a P8 i S8, els oracles a l'enunciat, «problema») i els suggeriments amb una proposta concreta, amb les regles noves D-70, D-71 i D-72; `8c009f9`, els ítems nous de l'usuari: `S_criteris_seleccio.qmd` retirat (D-73), el calendari només a l'HTML, amb un script, un agent i un pas del hook que el comproven (D-74), el projecte d'innovació docent a la llicència i l'autor de RARS al `.bib`; `6a17af1`, `02_problemes/` i `P1.qmd`–`P9.qmd` (D-75); i el de tancament, amb dues regressions dels blocs anteriors (la concordança d'«el VPN» a S8 i una redundància d'A9). Abans de tocar A2, A3, A4 i `21_riscv/`, `git ls-remote --heads origin`: cap branca d'equip. Toca A2 i A3 (tres frases de «problema»), A4 (l'slug), `21_riscv/` (un fragment retirat, que no incloïa ningú), i el PDF sencer (D-69), cosa que els equips han de saber. `TODO.md`: 23 → 25, amb cinc entrades executades i set de noves: tres decisions que va demanar l'usuari (els fitxers orfes, els exemples i les solucions plegables i «el codi següent»), el calendari per confirmar, les possibles errades d'A1–A8, tres desajustos de la guia i del glossari, i 88 suggeriments sense proposta.
