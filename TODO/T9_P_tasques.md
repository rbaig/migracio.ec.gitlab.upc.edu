# T9-PE_T9-PS_T9 — Revisió interna profunda: llista d'accions

**Fitxers objectiu:** `01_apunts/A9.qmd`, `02_exercicis/E9.qmd`, `03_solucions/S9.qmd`
**Fitxers col·laterals:** `21_riscv/RV32I_csr_mip_mie_taula.qmd`,
`21_riscv/RARS_syscall_registres.qmd`, `21_riscv/Zicsr_pseudo_immediats.qmd`,
`13_contrib.qmd`, `CLAUDE.md`, `TODO/TODO.md`, `03_solucions/S_criteris_seleccio.qmd` (C9)
**Llegenda:** 🔴 error · 🟡 millora · 🔵 decisió · ✅ fet · ⏳ pendent

Nota de context: tots els valors numèrics del tema (codis `mcause`, posicions
de bits de tots els CSR, offsets de pila de les dues RSE, adreces i màscares de
PS_T9, codis de servei RARS i números de crida Linux) s'han verificat contra la
RISC-V Privileged Spec 20240411, `21_specs/registres.toml`, la documentació de
RARS i `include/uapi/asm-generic/unistd.h` del nucli Linux (les traces de pila
s'han comprovat mecànicament per script). Només han aflorat les incidències
llistades a A1, A2 i A12.

---

## A — Errors tècnics (execució directa) ✅

### T9.qmd

- 🔴✅ **A1 — `#wrn-ecall-taula-linux`: crida 48 mal identificada.** La fila
  «`48 | fadvise64 | a0=fd, a1=offset, a2=len, a3=advice`» és incorrecta:
  segons `asm-generic/unistd.h`, **48 = `faccessat`** (`a0`=dirfd, `a1`=path,
  `a2`=mode → `a0`=0 o error); `fadvise64` és la **223**. Corregir la fila a
  `faccessat` (més rellevant que `fadvise64` per a una taula de «més
  rellevants»).
- 🔴✅ **A2 — `#wrn-ecall-taula-linux`: crida 113 inexistent a RV32.** La fila
  «`113 | clock_gettime`» no és aplicable: el port **RV32** de Linux es va
  integrar només amb `time_t` de 64 bits i no cableja les crides *time32*
  (guarda `__ARCH_WANT_TIME32_SYSCALLS` del header, que RV32 no defineix). La
  crida equivalent a RV32 és **`403 | clock_gettime64`** (mateixos arguments).
  Substituir la fila (o eliminar-la; vegeu C8 per a la resta de subtileses
  32/64 bits).
- 🔴✅ **A3 — `#nte-satp`: falta el camp `ASID` al text.** La llista de camps
  només descriu `MODE` (bit 31) i `PPN` (bits 21:0), però la figura i
  `registres.toml` mostren també **`ASID` (bits 30:22)**. Afegir el bullet:
  «**`ASID`** (bits 30:22, *Address Space Identifier*): identificador de
  l'espai d'adreces, que permet al TLB distingir traduccions de processos
  diferents sense haver-lo de buidar en cada canvi de context.» (Coherent amb
  l'operand `rs2` de `sfence.vma`, que ja parla d'ASID.)
- 🔴✅ **A4 — §Sincronització per enquesta: codi invàlid.** Al bloc de
  *polling*, `bne t0, READY, bucle` usa `READY` com si fos un registre.
  Corregir a:
  ```
  bucle:
          lw      t0, ESTAT_DISPOSITIU    # llegir l'estat del dispositiu
          li      t1, READY               # valor que indica «llest»
          bne     t0, t1, bucle           # esperar fins que estigui llest
      # continuar quan el dispositiu ha acabat
  ```
  i canviar el `filename` del bloc a `RV32I` (no usa cap instrucció CSR; vegeu
  B2).
- 🔴✅ **A5 — «Pseudoinstruccions» incorrecte per a `csrrwi`/`csrrsi`/`csrrci`.**
  Són **instruccions reals** de Zicsr (l'immediat `uimm5` va al camp `rs1`),
  no pseudoinstruccions — a diferència de `csrr`/`csrw`, que sí que ho són i
  estan ben marcades. Corregir el títol del callout interior:
  «`## Zicsr ISA — Pseudoinstruccions d'accés als CSR (immediats)`» →
  «`## Zicsr ISA — Instruccions d'accés als CSR amb immediat`». (Els renoms
  d'ids i de fitxer associats són a C6.)
- 🔴✅ **A6 — `tbl-colwidths` que no sumen 100** (criteri de `07_contrib
  §Taules`; el PDF no renderitza bé): taula de modes de privilegi
  (`[5,8,10,40, 8]` = 71; a més té un espai espuri) → p. ex. `[8,12,20,50,10]`;
  taula de modes de `mtvec` (`[5,5,40]` = 50) → p. ex. `[10,15,75]`.
- 🔴✅ **A7 — `#nte-ecall-convencio-rars`: duplicació DRY.** El callout
  reprodueix inline els dos bullets de
  `21_riscv/RARS_syscall_registres.qmd` en lloc de fer-ne `include` (com fa
  `05_riscv.qmd §RARS — Registres de crida al sistema`). Substituir el cos per
  `{{< include ../21_riscv/RARS_syscall_registres.qmd >}}`.
- 🔴✅ **A8 — Títols dels callouts RARS: guió i espaiat.** «`## RARS – Registres
  de crida al sistema`» i «`##  RARS – Codis de servei més rellevants`» usen
  guió mitjà `–` (la convenció de `07_contrib §Callouts` és el guió llarg `—`)
  i el segon té doble espai. Corregir tots dos a «`## RARS — …`».
- 🔴✅ **A9 — Gramàtica «de més rellevants» (×2).** Al títol del wrn
  «`## RV32I Linux — ABI: Codis de crides al sistema de més rellevants`» i al
  caption de `#tbl-syscalls-rars` («RARS: Codis de crides al sistema de més
  rellevants.»). Eliminar el «de» espuri i, al caption, harmonitzar amb el
  títol del callout i amb `05_riscv.qmd`: «RARS: codis de servei més
  rellevants.» (minúscula després de dos punts; vegeu també B3 i C4).
- 🔴✅ **A10 — Definició de CSR duplicada (§El model de privilegis).** Dos
  paràgrafs consecutius expandeixen la sigla («**registres de control i
  estat** (***Control and Status Registers***, **CSR**)»). Mantenir la primera
  expansió i, al segon paràgraf, dir només «les instruccions d'accés als CSR».
- 🔴✅ **A11 — Gramàtica (§El model de privilegis).** «determinen quines
  **instruccions** pot executar el processador i **adreces de memòria** pot
  accedir» → «…i **a quines adreces de memòria** pot accedir».
- 🔴✅ **A13 — `#sec-ei-csr-mepc`: frase introductòria imprecisa.** «guarda
  l'adreça de la instrucció que el processador estava executant quan s'ha
  produït l'excepció o interrupció» és falsa per a les interrupcions (hi
  guarda la *següent*, com els bullets posteriors i el TOML ja diuen bé).
  Reescriure: «guarda l'adreça on la RSE ha de retornar el control en acabar:
  la de la instrucció causant o la de la següent, segons el tipus
  d'esdeveniment.»

### PS_T9.qmd

- 🔴✅ **A12 — `sol-p9-exc-rse`: `x0` a la pila i observació errònia.** La
  solució reserva 124 bytes i desa `x0` a `120(sp)` «per simetria», però:
  el comentari inicial diu «(x1-x31, excepte sp=x2)» (conjunt de 30 registres,
  que no inclou `x0`); la teoria (`@sec-ei-rse-exemple`) usa 120 bytes sense
  `x0`; i l'observació «el `lw` de restauració no el modifica gràcies a la
  propietat de `x0`» descriu una instrucció que **no existeix** al codi (no es
  restaura `x0`). Harmonitzar amb la teoria: eliminar `sw x0, 120(sp)`,
  passar a `addi sp, sp, -120`/`+120`, i eliminar l'observació (mantenint les
  altres dues, sobre `mtvec` i sobre `j`).

### Altres fitxers

- 🔴✅ **A14 — `CLAUDE.md`: rutes de `TODO.md` desactualitzades.** El fitxer
  s'ha mogut a `TODO/TODO.md`; actualitzar les mencions de `CLAUDE.md`
  (§Fitxers de referència obligatòria, §Repartiment de responsabilitats,
  §IAs si escau).
- 🔴✅ **A15 — `TODO/TODO.md §T9`: ítem E3 obsolet.** «Slugs sense prefix:
  `sec-introduccio`, `sec-flux-hardware`…» ja està resolt: totes les capçaleres
  de T9 usen el prefix `sec-ei-*` (verificat). Eliminar l'ítem o marcar-lo fet.
- 🔴✅ **A16 — `13_contrib.qmd`: fila inexacta a la taula de fitxers
  `11_riscv/`.** La fila `Zicsr_pseudo_immediats.qmd | T9, 05_riscv.qmd`
  contradiu el paràgraf «Contingut d'Aprofundiment exclòs de `05_riscv.qmd`»
  del mateix fitxer (que explica que **no** s'hi inclou). Corregir la columna
  «Usat a» a «T9». (Si s'aprova C6, aplicar-hi també el rename.)

---

## B — Millores i harmonitzacions menors (execució directa) ✅

- 🟡✅ **B1 — `hardware` → `maquinari` a T9.** T9 usa «hardware» 26 vegades
  (inclosos els títols «Suport hardware: …» i «Flux hardware en detectar…»)
  i «maquinari» només 4, mentre que PE_T9, PS_T9 i T8 usen «maquinari» i el
  mateix T9 usa sempre «programari» (mai «software»). La taula de
  **substitucions obligatòries** de `07_contrib` marca «maquinari» com a terme
  preferent. Substituir a la prosa i als títols («Suport de maquinari: …»,
  «Flux de maquinari en detectar…»), **mantenint**: els slugs actuals
  (`sec-ei-flux-hardware*`, per estabilitat de les referències des de PS) i
  l'anglicisme fixat en cursiva *hardware page-table walker* (terme establert
  a T8).
- 🟡✅ **B2 — `filename` dels blocs de codi segons les extensions realment
  usades.** Blocs etiquetats `RV32IZicsr` que només usen RV32I base
  (cap instrucció CSR): T9 — el bloc de *polling* (A4) i els 8 exemples
  d'`ecall` (4 RARS + 4 Linux); PS_T9 — els 4 blocs de `sol-p9-syscall-basic`.
  Tots → `filename="RV32I"`. (Els blocs amb `csrr`/`csrrs`/`csrw` queden
  correctament com a `RV32IZicsr`.)
- 🟡✅ **B3 — Harmonització «codi de servei».** `CLAUDE.md §T9` i el títol
  canònic de `05_riscv.qmd` fixen «codi de servei»; en canvi: el cos de T9 diu
  «RARS estableix `a7` per codi de la crida al sistema» (a més amb preposició
  coixa: «per **al** codi… i `a0` per **a** l'argument…»), el fragment
  `RARS_syscall_registres.qmd` diu «codi de la crida al sistema» i PE
  (`exr-p9-syscall-basic`) diu «El número de crida al sistema … i els
  arguments a `a0`». Unificar a «codi de servei» al context RARS (cos de T9,
  fragment compartit — que propaga a `05_riscv` — i PE: «El codi de servei es
  passa al registre `a7` i l'argument principal a `a0`»). Al context Linux es
  manté «codi de la crida al sistema (*syscall number*)».
- 🟡✅ **B4 — PE: «mode màquina» → «mode M».** La teoria fixa «mode M»
  (`@nte-modes-privilegi`); PE usa «mode màquina» (×4) i l'anglicisme
  «(M-mode)» (×1). Substituir per «mode M» i eliminar «(M-mode)».
- 🟡✅ **B5 — `#cau-terminologia`: minúscula després de dos punts.**
  «**Excepció**: Esdeveniment…» i «**Interrupció**: Esdeveniment…» →
  «esdeveniment» (criteri de `07_contrib §Puntuació` per a explicacions breus).
- 🟡✅ **B6 — `@tbl-tipologia`: cel·la de la fila d'interrupció.** «Continua a
  instrucció+4» és equívoc per a les interrupcions (`mepc` ja apunta a la
  següent; no hi ha cap «+4»). → «Continua a la instrucció següent». La fila
  d'`ecall` es manté («+4» hi és literal: l'ajust de la RSE).
- 🟡✅ **B7 — `#nte-mip-mie`: matís de «sols lectura».** L'afirmació «`mip` …
  És de **sols lectura** per al programari» només és certa per als bits de
  mode M; els bits `S*IP` són escrivibles des de mode M. Reescriure: «Els bits
  de mode M (`MEIP`, `MTIP`, `MSIP`) són de sols lectura per al programari
  (els actualitza el maquinari).»
- 🟡✅ **B8 — Presentar `sret`.** El `page_fault_handler` usa `sret` sense que
  s'hagi introduït enlloc (només `mret` té taula). Afegir una frase a
  `@sec-ei-csr-modes` (o just abans del codi): «L'equivalent de `mret` en mode
  S és la instrucció `sret`, amb la mateixa semàntica sobre els camps `S*` de
  `sstatus` i sobre `sepc`.»
- 🟡✅ **B9 — Motivar el tercer paràmetre del *dispatcher*.** El text de
  `@sec-ei-rse-exemple` diu que el *dispatcher* rep «un punter als registres
  salvats» sense explicar per què. Afegir la motivació: li permet llegir els
  paràmetres de la crida al sistema i **modificar els valors que es
  restauraran** (p. ex. escriure el resultat d'una crida a la posició salvada
  d'`a0`, que és la que tornarà al programa).
- 🟡✅ **B10 — Títols de subsecció de §Crida al sistema.** «### Crides al
  sistema» (`#sec-ei-ecall-abi-rars`) i «### Convenció ABI»
  (`#sec-ei-ecall-abi-linux`) no identifiquen el context que els slugs sí que
  recullen. → «### Convenció de crides al sistema a RARS» i «### Convenció
  ABI de Linux» (slugs intactes).
- 🟡✅ **B11 — Redacció d'`exit`/`exit2`.** «permet especificar el codi de
  sortida … per al procés que l'ha cridat (normalment el SO)» → «…codi de
  sortida (normalment 0 per a una terminació correcta), que es retorna al
  procés pare (normalment el SO)». Opcional: nota que el codi 93 d'`exit2`
  coincideix expressament amb el número de la crida `exit` de Linux/RISC-V.
- 🟡✅ **B12 — Nota de `#nte-sfence`.** «No pertany ni a Zicsr ni a cap altra
  extensió estàndard» és ambigua. → «Forma part de l'arquitectura privilegiada:
  està disponible sempre que el processador implementi el mode S.»

---

## C — Decisions de Roger ✅ (totes acceptades, opció (a))

- 🔵✅ **C1 — `sol-p9-exc-interrupcions-io` contradiu el criteri «salvar-ho
  tot».** La RSE de teclat salva només `t0`, `t1`, `t2` i `ra` (i `ra` ni tan
  sols s'hi modifica: no hi ha cap crida), mentre que `@cau-rse-registres`,
  la teoria i `CLAUDE.md §T9` estableixen que «cal salvar **tots** els
  registres generals sense excepció». A més, el pas 1 de
  `@sec-ei-rse-responsabilitats` és internament ambigu («tots els registres …
  **que pugui modificar** … cal salvar-los **tots sense excepció**»).
  - **(a) Recomanada:** teoria: eliminar «que pugui modificar» del pas 1
    (la regla queda absoluta i el perquè ja hi és); PS: salvament complet dels
    30 registres amb el mateix patró de `sol-p9-exc-rse` (llarg, però coherent
    amb el criteri absolut i amb el que s'exigiria en un examen).
  - (b) Mantenir el salvament parcial afegint una justificació explícita («RSE
    tancada que només modifica `t0`–`t2`; la regla general de
    `@cau-rse-registres` s'aplica quan la RSE executa codi arbitrari») i
    matisar el criteri de la teoria i de `CLAUDE.md` («per al cas general»).
  - (c) Retoc mínim: només eliminar `sw`/`lw` de `ra` (−16 → −12) i assumir la
    incoherència. *(No recomanada.)*
- 🔵✅ **C2 — Fila `LCOFIP`/`LCOFIE` del fragment
  `RV32I_csr_mip_mie_taula.qmd`.** El bit 13 (desbordament de comptador de
  rendiment) pertany a l'extensió **Sscofpmf**, no apareix a les figures de
  `mip`/`mie` (el TOML no el defineix), no s'usa enlloc del llibre i trenca
  l'ordre descendent de bits de la taula. El canvi propaga automàticament a
  `05_riscv.qmd` (mateix fragment).
  - **(a) Recomanada:** eliminar la fila (fora de l'abast d'EC; taula = figura).
  - (b) Mantenir-la amb la nota «(extensió Sscofpmf)», moure-la a la posició
    d'ordre correcta i afegir el bit 13 a les dues figures del TOML.
- 🔵✅ **C3 — Sintaxi `li t0, (1 << 11)` (×2) i `(1 << 3)` (×2) a PS_T9.**
  L'expressió `(1 << n)` és sintaxi de GNU `as`, no de RARS ni notació
  ensenyada al curs.
  - **(a) Recomanada:** `li t0, 0x800` amb comentari «bit 11 (`MEIE`)» i
    `li t0, 0x8` amb «bit 3 (`MIE`)» (executable a RARS i estil de pissarra).
  - (b) Mantenir `(1 << n)` com a notació expressiva (cap dels blocs és
    executable a RARS en mode M, de tota manera).
- 🔵✅ **C4 — Estructura de §Convenció ABI (Linux).** Tot el contingut viu dins
  `#wrn-ecall-abi-linux` (aprofundiment **no avaluable**), però: `CLAUDE.md
  §T9` recull la convenció Linux (`a7`, sis arguments) com a **decisió de
  curs**; el wrn conté aniuats un `#cau-` i dos `#tip-` (tipus **avaluables**);
  i el títol del wrn no segueix el patró «Aprofundiment: …».
  - **(a) Recomanada:** treure del wrn la introducció, els tres bullets de la
    convenció i `#cau-ecall-convencio-linux` (passen a cos avaluable de la
    secció, retitulada segons B10); deixar en aprofundiment els exemples
    (retitulats «Aprofundiment: exemples de crides al sistema Linux/RISC-V») i
    la taula gran (ja titulada «Aprofundiment: …»).
  - (b) Mantenir-ho tot com a aprofundiment: retitular el wrn («Aprofundiment:
    convenció ABI de Linux») i degradar el `cau` interior a text pla — quedaria
    coherent en avaluabilitat, però xocaria amb la decisió de `CLAUDE.md`.
  - (c) Status quo. *(No recomanada: incoherència d'avaluabilitat.)*
- 🔵✅ **C5 — Prefix de títol per als callouts de CSR.** T9 i `05_riscv.qmd`
  titulen els callouts de `mcause`/`mepc`/`mstatus`/`mtvec`/`mip`-`mie`/
  `satp`/taules CSR com a «RV32I ISA — …» (tot i ser arquitectura
  privilegiada) i `sfence.vma` com a «Supervisor ISA — …», un prefix **no
  registrat** a la llista de `07_contrib §Callouts`.
  - **(a) Recomanada (mínima):** afegir «`## Supervisor ISA — `» a la llista de
    títols admesos de `07_contrib` i mantenir «RV32I ISA» com a abreviatura de
    curs per als CSR de la variant RV32 (cap retoc a T9/05_riscv).
  - (b) Crear el prefix «Privileged ISA — » i retitular els ~9 callouts de CSR
    a T9 i `05_riscv.qmd` (més precís; més tocs i afecta la revisió externa).
- 🔵✅ **C6 — Renoms associats a A5 («pseudo» a les variants immediates).**
  Cap referència `@` externa als ids (verificat); el fitxer només s'inclou des
  de T9 i apareix 2 cops a `07_contrib`.
  - **(a) Recomanada:** rename complet: `21_riscv/Zicsr_pseudo_immediats.qmd` →
    `Zicsr_instruccions_immediats.qmd` (+ include de T9 + 2 mencions de
    `07_contrib`, una de les quals ja es toca per A16); ids
    `#wrn-zicsr-pseudoinstruccions` → `#wrn-zicsr-immediats` i
    `#nte-zicsr-pseudoinstruccions` → `#nte-zicsr-immediats`.
  - (b) Només el títol visible (A5), deixant noms interns com estan.
- 🔵✅ **C7 — Precisió 32/64 bits de la taula Linux (RV32).** A banda d'A1/A2,
  diverses files usen el nom genèric `__NR3264`: a RV32, 25 és `fcntl64`, 62 és
  `llseek` (signatura diferent: 5 arguments, offset de 64 bits partit), 79 és
  `fstatat64`, 80 és `fstat64`, i el 222 (`mmap`) rep l'offset **en pàgines**
  (semàntica `mmap2`). Els números són correctes; els noms/arguments són els de
  la variant de 64 bits.
  - **(a) Recomanada:** mantenir els números i noms genèrics i afegir una nota
    al peu de la taula («A RV32, les crides 25/62/79/80 corresponen a les
    variants `*64`, i `mmap` rep l'offset en pàgines de 4 KiB»), corregint
    només la fila 62 (arguments de `llseek`) o eliminant-la.
  - (b) Purga de les files amb divergència 32/64 poc rellevants per a EC
    (25, 62, 79; mantenir 80 i 222 amb nota).
  - (c) Precisió completa fila a fila. *(Desproporcionat per a un
    aprofundiment.)*
- 🔵✅ **C8 — `.section .text.trap, "ax"` a l'exemple de RSE de la teoria.**
  `07_contrib §T2 i T3` estableix que `.section` no s'usa (només `.data` i
  `.text`), però l'exemple —marcat explícitament com a «il·lustratiu (no
  executable directament)»— l'usa, junt amb `.align 2`.
  - **(a) Recomanada:** mantenir-ho (l'excepció és conscient: una RSE real no
    viu al `.text` d'usuari) i afegir mitja frase al text que ho digui
    («l'exemple usa directives de GNU `as` fora de l'abast de RARS»).
  - (b) Eliminar les dues directives i deixar només l'etiqueta `rse:`.
- 🔵✅ **C9 — Alineació d'estructura PE ↔ PS ↔ `PS_criteris`.** PE agrupa
  `exr-p9-exc-mepc-mtvec`, `exr-p9-exc-tlb-miss` i
  `exr-p9-exc-interrupcions-io` sota «Entrada/Sortida» (els dos primers no en
  són); PS crea tres seccions que PE no té («Registres `mepc` i `mtvec`»,
  «Fallada de pàgina», «Interrupcions d'entrada/sortida»); i `PS_criteris §T9`
  assigna seccions que no coincideixen amb cap dels dos.
  - **(a) Recomanada:** reordenar PE seguint l'ordre de la teoria —
    §Excepcions i interrupcions (`conceptes`, `causes`, `rse`, `mepc-mtvec`),
    §Crides al sistema (`basic`, `programa`, `vector`), §Entrada/Sortida
    (`io-conceptes`, `io-polling`, `interrupcions-io`), §Fallada de pàgina
    (`tlb-miss`) — i alinear-hi les seccions de PS i la columna «Secció» de
    `PS_criteris §T9`.
  - (b) Mantenir PE tal com està i retitular les seccions de PS perquè el
    calquin.
  - (c) Status quo.
- 🔵ℹ️ **C10 — `exr-p9-syscall-programa`: sortida amb `li a7, 10` vs.
  `li a7, 93`.** Sense acció en aquest xat: és la decisió oberta de
  `startup.s` ja registrada a `TODO/TODO.md §Decisions obertes`, que
  n'especifica explícitament la unificació futura.

---

## E — Verificacions completades sense incidència ✅

- **Taula de codis `mcause`** (`RV32I_csr_mcause_taula.qmd`): les 17 files
  (excepcions 0–9, 11–13, 15; interrupcions 3, 7, 11) coincideixen exactament
  amb la Privileged Spec 20240411.
- **Posicions de bits de tots els CSR**, text i `registres.toml`: `mstatus`
  (desglossament complet de 21 camps, `MIE`=3, `MPIE`=7, `MPP`=12:11),
  `mip`/`mie` (bits 1–11 de modes M i S), `mtvec` (`BASE`=31:2, `MODE`=1:0),
  `mcause` (bit 31 + 31 bits de codi), `satp` Sv32 (`MODE`=31, `ASID`=30:22,
  `PPN`=21:0; només mancava al text: A3). Semàntica de `mepc` (excepció:
  causant; interrupció: següent) conforme a la spec.
- **Semàntica de `mret`** ($MIE \leftarrow MPIE$; $MPIE \leftarrow 1$;
  $mode \leftarrow MPP$; $MPP \leftarrow U$): coherent amb la spec per a
  implementacions amb mode U (la spec diu «el mode menys privilegiat
  suportat»; la simplificació d'EC és correcta en el context del tema).
  Fórmula del mode vectoritzat `BASE + 4 × causa` (només interrupcions;
  excepcions a `BASE`): correcta.
- **Les 5 accions del flux hardware** (PC→`mepc`, causa→`mcause`,
  `MIE`→`MPIE`+inhibició, mode→`MPP`+pas a M, salt a `mtvec`): conformes.
- **RSE de la teoria**: 30 registres (x1–x31 llevat de `sp`), offsets 0–116
  verificats mecànicament (seqüència `sw` = seqüència `lw`, sense duplicats),
  120 bytes exactes. **RSE de PS**: offsets 0–120 correctes (única esmena:
  `x0`/124 bytes, A12).
- **Aritmètica de PS_T9**: `0x80001000` (causant), `0x80002004 + 4 =
  0x80002008`, `BASE + 4×7 = BASE + 28`, màscares `0x800` (bit 11), `0x8`
  (bit 3) i `0x8000000B` (bit 31 + codi 11): totes correctes.
- **Taula RARS** (13 codis de servei, arguments i retorns): conforme a la
  documentació de RARS. Exemples RARS (1, 5, 4, 10) i Linux (64, 63, 93, 214)
  correctes.
- **Taula Linux**: 39 de les 41 files verificades número a número contra
  `asm-generic/unistd.h`; les 2 discrepàncies són A1 i A2.
- **`page_fault_handler`**: coherent amb T8 (bit V = bit 0 de la PTE, `D=0`
  en carregar, *write-back* de la víctima si `D=1`, `sfence.vma` abans de
  `sret`, `sepc` sense modificar per forçar la reexecució).
- **Referències creuades**: les ~40 referències `@` de T9/PE/PS resolen totes
  (T9 intern, T7, T8 i `05_riscv.qmd`); la menció de MIPS a
  `exr-p9-exc-tlb-miss` queda coberta per l'explícita de
  `@wrn-mv-tlb-hw-walker` (T8).
- **Cobertura del solucionari** = selecció documentada a `PS_criteris §T9`
  (7 de 10; sense solució: `causes`, `syscall-programa`, `syscall-vector`,
  `io-polling` i l'apartat c de `tlb-miss`, que la solució declara
  explícitament fora de la selecció).
- **Sigles**: totes les del tema (RSE, CSR, SO, E/S, TLB, PTE, MMU, ABI, VPN,
  PPN, RARS) consten a `06_sigles.qmd`; `MIE`/`MEIP`/`ASID` exclosos
  correctament (noms de camps de bits).
- **Figures**: `T9_cicle_interrupcio.svg` existeix a `12_figs_originals/`;
  les 8 figures de registres estan definides al TOML i el caption d'`mcause`
  documenta l'abreviatura «Int.». Caption del cicle d'interrupció coherent amb
  la semàntica de `mepc` (i+1 en curs → `mepc` = i+2).
- **Callouts `#cau-` sense títol** (×6 a T9): coherent amb el criteri vigent
  de `07_contrib` i amb el recompte de la decisió oberta de `TODO/TODO.md`.
- **Etiquetes `{#sec-}`**: totes les capçaleres `##`–`####` de T9 porten slug
  amb prefix `sec-ei-*` (motiu d'A15).

---

## Fitxers modificats (Fase C, execució completa)

`01_apunts/A9.qmd` · `02_exercicis/E9.qmd` · `03_solucions/S9.qmd` ·
`21_riscv/RV32I_csr_mip_mie_taula.qmd` (C2) ·
`21_riscv/RARS_syscall_registres.qmd` (A7/B3) ·
`21_riscv/Zicsr_pseudo_immediats.qmd` → renombrat a
`21_riscv/Zicsr_instruccions_immediats.qmd` (C6) · `13_contrib.qmd` (A16, C5,
C6) · `CLAUDE.md` (A14) · `TODO/TODO.md` (A14, A15) · `03_solucions/S_criteris_seleccio.qmd`
(C9)

Totes les verificacions de sanitat (ids únics, balanç de blocs `:::`,
`tbl-colwidths` = 100, referències `@` resoltes, `include` vàlids,
coherència numèrica de les RSE) s'han repetit després de cada bloc (A, B, C)
sense incidències.
