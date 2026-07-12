# T3 — Revisió interna A3/E3/S3 · Llista de tasques (Fase B)

Revisió feta amb: verificació aritmètica per script (tots els càlculs), execució
empírica a **RARS 1.6** (assemblatge i execució de casos dubtosos), contrast amb
els fragments de `21_riscv/`, `13_contrib.qmd`, `S_criteris.qmd`, A1/A2/A4/A9 i
E2/E4.

Marques: **[C]** executable a la Fase C sense aprovació · **[D]** requereix
decisió de l'usuari · Prioritat: 🔴 alta · 🟡 mitjana · 🟢 baixa.

---

## 1. Correcció tècnica

### T01 🔴 [C] `sra` amb operand immediat — no assembla
- **On:** `A3.qmd:100` (`#tip-exemple-sra`).
- **Problema:** `sra t0, t0, 2` usa un immediat com a tercer operand; `sra`
  exigeix registre. **Verificat a RARS 1.6:** `Error: "2": operand is of
  incorrect type`. Contradiu també la taula pròpia
  (`RV32I_instruccions_desplacament_bits_aritmetics.qmd`: `sra rd, rs1, rs2`).
- **Acció:** canviar a `srai t0, t0, 2` (i repassar que el text del tip parli
  de la variant immediata).

### T02 🔴 [C] Exemple del cau d'extensió de signe — no assembla
- **On:** `A3.qmd:157` (`#cau-immediats-logics-extensio-signe`).
- **Problema:** `andi t0, t1, 0x800` **no assembla a RARS 1.6**: `Unsigned
  value is too large to fit into a sign-extended immediate` (0x800 = 2048 >
  2047). L'exemple, tal com està, no pot il·lustrar res perquè és rebutjat.
- **Acció:** reescriure l'exemple amb `andi t0, t1, -2048` i comentari
  `# t0 = t1 & 0xFFFFF800`, tot conservant el missatge didàctic: l'immediat
  s'estén amb signe, i una «màscara» com `0x800` ni tan sols és expressable com
  a immediat positiu (l'assemblador la rebutja). Mantenir l'advertiment
  «(no `t1 & 0x00000800`!)» adaptat a la nova redacció.

### T03 🔴 [C] Operació de `jalr` al fragment compartit — ordre d'assignacions incorrecte quan `rd = rs1`
- **On:** `21_riscv/RV32I_instruccions_salt_incondicional_indirecte.qmd`.
- **Problema:** l'operació està escrita com
  $rd \leftarrow PC+4;\; PC \leftarrow rs1 + SignExt(imm12)$. Si `rd = rs1`
  (cas de `@exr-p4-memoria-jalr`!), llegit literalment el destí es calcularia
  amb el `rs1` ja sobreescrit — el contrari del comportament real (el destí es
  calcula amb el valor **original** de `rs1`), que és exactament el que S3:561
  explica bé. El fragment és compartit amb T2 i `11_riscv.qmd`.
- **Acció:** reescriure l'operació de manera que l'ordre sigui inequívoc, p.
  ex. $PC \leftarrow rs1 + SignExt(imm12);\; rd \leftarrow PC_{anterior}+4$ o
  amb variable temporal
  ($t \leftarrow rs1 + SignExt(imm12);\; rd \leftarrow PC+4;\; PC \leftarrow t$).

### T04 🔴 [C] Typo a la taula de comparacions (fragment compartit)
- **On:** `21_riscv/RV32I_instruccions_comparacio.qmd` (4 files).
- **Problema:** «set **les** than» → «set **less** than» (×4).
- **Acció:** corregir el fragment (afecta T2, T3 i `11_riscv.qmd`).

### T05 🔴 [C] Anàlisi de S3 f) incoherent amb les definicions d'A4
- **On:** `S3.qmd:411` (`#sol-p4-bucles-suma-vector`, apartat f).
- **Problema:** diu que «l'apartat e) ja elimina la variable d'inducció …
  (optimitzacions #2 i #3)». Segons A4 (`#sec-opt-eliminacio-induccio`),
  eliminar la variable d'inducció vol dir substituir el comptador per la
  comparació del punter amb una sentinella; **e) conserva el comptador `t1`**
  (aplica #1 accés seqüencial i #2 condició al final); és **f)** qui elimina la
  variable d'inducció. A més, «la millora restant és treure la càrrega del
  `li t1, N` fora del bucle» és falsa: a e) el `li` ja és fora del bucle; la
  millora real és suprimir l'`addi t1, t1, -1` de cada iteració.
- **Acció:** reescriure el paràgraf introductori de f): e) aplica accés
  seqüencial (#1) i avaluació de la condició al final (#2); f) hi afegeix
  l'eliminació de la variable d'inducció (#3) comparant el punter amb la
  sentinella (`bltu`, adreces sense signe, coherent amb `#cau-opt3` d'A4).

### T06 🔴 [C] Cost comparatiu de S3 f) — «1 instrucció addicional» i punt d'equilibri
- **On:** `S3.qmd:434`.
- **Problema:** «s'estalvia 1 cicle per iteració a cost d'**1 instrucció**
  d'inicialització addicional». Verificat: e) té 3 instruccions
  d'inicialització i f) en té 5 → són **2** instruccions (+2 cicles). Amb
  $9N+2$ vs $8N+4$: iguals a $N=2$, f) millor per a $N \ge 3$ (verificat per
  script).
- **Acció:** corregir a «2 instruccions (+2 cicles)» i precisar el punt
  d'equilibri («iguals per a $N = 2$; f) és millor per a $N \ge 3$»).

### T07 🟡 [C] Adreça del vector a `exr-p4-bucles-ordenacio` fora del `.data` de RARS
- **On:** `E3.qmd:333`.
- **Problema:** «`Array` està ubicat a l'adreça `0x10000000`», però el `.data`
  de RARS comença a `0x10010000` (`RARS_memoria_regions.qmd`); una declaració
  amb `.data` mai no quedaria a `0x10000000`.
- **Acció:** canviar a `0x10010000` (coherent amb el mapa de memòria del
  llibre).

### T08 🟡 [C] Fons de pila: dos valors sense explicar la diferència
- **On:** `A3.qmd:1516` (`#nte-rars-fons-pila`) vs taula inclosa a `A3.qmd:1047`
  (`RARS_memoria_regions.qmd`).
- **Problema:** la taula dona la pila a `0x7FFFFFFC` (límit superior de la
  regió) i la nota diu que el fons de pila (sp inicial) és `0x7fffeffc`. Tots
  dos valors són correctes a RARS, però mostrats sense reconciliar confonen.
- **Acció:** afegir un incís a la nota: la regió de pila arriba fins a
  `0x7FFFFFFC`, però RARS inicialitza `sp` a `0x7FFFEFFC` (espai reservat per
  sobre). Unificar també la caixa (majúscules/minúscules) segons T27.

### T09 🟡 [C] «tret de `auipc` i `ecall`» — excepcions incompletes
- **On:** `A3.qmd`, §revisió dels modes d'adreçament (text previ a la taula).
- **Problema:** RV32I també conté `fence` i `ebreak`, no presentades ni
  classificades.
- **Acció:** reformular, p. ex. «totes les instruccions de processament i de
  control de flux de la base RV32I, tret de `auipc` (…) i `ecall` (…); les de
  sistema (`fence`, `ebreak`) queden fora de l'abast d'EC».

### T10 🟡 [C] Vector de salts del `switch` amb el defecte com a entrada indexable
- **On:** `A3.qmd` (`#tip-traduccio-switch`).
- **Problema:** el vector és `.word cas_0, cas_1, cas_2, cas_defecte`: el
  defecte només s'hi arriba si l'expressió val exactament 3, cosa que no és la
  semàntica de `default` (el wrn posterior sí que ho tracta bé amb `bgeu`).
- **Acció:** al tip, usar quatre casos reals (`cas_0`–`cas_3`) i remetre el
  tractament del defecte al wrn; o bé incorporar la comprovació de rang al
  mateix tip. Preferida: la primera (canvi mínim).

### T11 🟢 [C] `#nte-bloc-activacio`: «L'ABI imposa…» + TODO pendent
- **On:** `A3.qmd` (nota amb `<!-- TODO Verificar que ho diu l'ABI -->`).
- **Problema:** el psABI de RISC-V no exigeix reservar tot l'espai del BA a
  l'inici; és una convenció (i un criteri d'EC).
- **Acció:** reformular «Per conveni —i com a criteri a EC— les subrutines
  reserven tot l'espai del seu bloc d'activació a l'inici…» i eliminar el TODO.

---

## 2. Coherència entre Teoria, Enunciats i Solucions

### T12 🔴 [D] Optimitzacions #2 i #3 presentades a T3 amb numeració que, segons `13_contrib.qmd`, «es defineix a T4»
- **On:** `A3.qmd` (`#tip-optimitzacio-bucle-2-avaluacio-condicio-final` i
  `#tip-optimitzacio-eliminacio-variable-induccio`) ↔ `A4.qmd`
  (`#sec-optimitzacions-bucle`) ↔ `13_contrib.qmd`.
- **Problema:** (a) contrib fixa que les tres optimitzacions numerades es
  defineixen a T4 §4.5; (b) A4 les presenta com a noves («les tres
  optimitzacions que es presenten a continuació») sense remetre a T3; (c) A3 ja
  n'introdueix dues amb títol numerat, duplicant explicació; (d) el títol del
  tip #2 d'A3 diu «Recorregut d'un vector: …» però l'exemple és el bucle de
  divisió per restes successives (no hi ha cap vector).
- **Opcions:**
  - **A (recomanada, alineada amb contrib):** a A3, treure la numeració dels
    títols i retitular («Avaluació de la condició al final» — corregint també
    el «Recorregut d'un vector» — i «Eliminació de la variable d'inducció»),
    afegint punter endavant explícit a `@sec-opt-condicio-final` i
    `@sec-opt-eliminacio-induccio` («aquesta transformació es formalitza com a
    Optimització #2/#3 a T4»). Cap canvi a A4.
  - **B:** mantenir la numeració a T3 i reescriure la introducció d'A4 perquè
    hi remeti; caldria també actualitzar `13_contrib.qmd`.

### T13 🟡 [C] Ordre de solucions invertit a S3 (for ↔ switch)
- **On:** `E3.qmd:129` (`switch`) < `E3.qmd:147` (`for`); `S3.qmd:204` (`for`) <
  `S3.qmd:255` (`switch`).
- **Acció:** moure `#sol-p4-bucles-switch` davant de `#sol-p4-bucles-for` per
  respectar l'ordre dels enunciats.

### T14 🟡 [C] Sintaxi de `jalr`: dues formes conviuen
- **On:** `E3.qmd:527` i `S3.qmd:557,561` (`jalr ra, 0(ra)` /
  `jalr rd, offset(rs1)`) vs taula canònica del fragment i A3
  (`jalr rd, rs1, imm`).
- **Verificat a RARS 1.6:** totes dues formes assemblen; és només qüestió de
  consistència.
- **Acció:** harmonitzar E3/S3 a la forma canònica de 3 operands
  (`jalr ra, ra, 0`; al text de S3, `jalr rd, rs1, offset`).

### T15 🟡 [C] Taules duplicades inline a A3 que ja existeixen com a fragments
- **On:** `A3.qmd:171` (`not`), `428` (pseudo salt condicional), `439` (pseudo
  salt zero), `544` (`j`), `565` (pseudo salt indirecte), `1578` (resum ABI de
  registres) ↔ `21_riscv/RV32I_pseudo_*.qmd` i `RV32I_abi_registres_resum.qmd`.
- **Problema:** `13_contrib.qmd` els llista com a «usats a T3», però A3 té les
  taules escrites inline; ja hi ha una divergència real (`not`: `rd = ~rs` a
  A3:178 vs $rd \leftarrow \sim rs$ al fragment).
- **Acció:** substituir cada taula inline pel `{{< include >}}` corresponent,
  fent primer un diff per no perdre contingut (capçaleres/columnes extres es
  reconcilien al fragment si cal).

### T16 🟡 [C] «muntatge» vs «assemblatge» als títols de secció
- **On:** `E3.qmd` i `S3.qmd` («Compilació, muntatge i càrrega») i la taula T3
  de `S_criteris.qmd`, vs `A3.qmd` («Compilació, assemblatge, enllaçat i
  càrrega»); el cos d'E3 (`exr-p4-compilacio-relocacio`) ja usa «assemblatge».
- **Acció:** unificar els títols d'E3/S3/S_criteris amb el d'A3.

### T17 🟢 [C] Repetició ×3 de «no existeix cap salt condicional indirecte»
- **On:** `A3.qmd`: nota de la taula de taxonomia de salts +
  `#cau-salts-condicionals-relatius-pc` + `#cau-salts-incondicionals`.
- **Acció:** deixar l'afirmació al cau principal (i, si de cas, a la nota de la
  taula); treure-la del tercer lloc.

### T18 🟢 [C] `funcA` crida `funcB` abans d'haver explicat la preservació de `ra`
- **On:** `A3.qmd` (`#tip-exemple-pas-vector`, secció de pas de paràmetres).
- **Problema:** `funcA` fa `jal` i acaba amb `ret` (amb `...` pel mig) sense
  cap menció a la preservació de `ra`; el concepte multinivell arriba més tard.
- **Acció:** afegir una nota breu de punter endavant: «`funcA` és una subrutina
  multinivell: haurà de preservar `ra` (vegeu §…); s'omet aquí per centrar
  l'exemple en el pas de paràmetres».

---

## 3. Eficiència pedagògica / format

### T19 🟡 [C] 14 blocs de codi nus a E3
- **On:** `E3.qmd`, 14 ocurrències de ` ```c `/` ```s ` sense atributs
  (concentrades a «Subrutines: introducció» i posteriors).
- **Acció:** normalitzar a ```` ```{.c filename="C"} ```` i
  ```` ```{.s filename="RV32I"} ```` com a la resta del llibre.

### T20 🟢 [C] Indentació no estàndard del codi d'un enunciat
- **On:** `E3.qmd` (`#exr-p4-logica-rotacio`, apartat b).
- **Acció:** realinear el bloc a l'estil de columnes del llibre (etiqueta a
  l'esquerra, mnemònics alineats).

### T21 🟢 [C] Aniuament de figures dins callouts amb el mateix nivell de colons
- **On:** `A3.qmd:1400/1406` (`#tip-func-uninivell-bloc-activacio` conté
  `#fig-func-uninivell-pila`) i `A3.qmd:1791` (`#fig-ba-exemple` dins
  `#tip-exemple-exemple`), tots amb `:::`; en canvi `#nte-format-b/j/u` usen
  correctament `::::` per al contenidor.
- **Acció:** passar els dos callouts contenidors a `::::` (renderitza igual,
  però queda coherent amb l'estil del llibre i és més robust).

### T22 🟢 [C] Etiqueta `endif` fora de la convenció del tema
- **On:** `A3.qmd:501-503` (`#tip-exemple-and-mascara-2`).
- **Problema:** la resta del tema usa `sino`/`fisi`; a més l'ID del tip
  («and-mascara-2») no descriu el contingut («Execució condicional amb `bne`»).
- **Acció:** canviar `endif` → `fisi`. L'ID no està referenciat enlloc
  (verificat): renombrar-lo a `#tip-execucio-condicional-bne` és segur, però
  opcional.

### T23 🟢 [C] Línia en blanc que falta abans d'un títol de secció a E3
- **On:** `E3.qmd`, entre el `:::` final i «## Subrutines: context i bloc
  d'activació».
- **Acció:** afegir la línia en blanc.

### T24 🟢 [D] Precisió de l'enunciat de la multiplicació per sumes
- **On:** `E3.qmd` (`#exr-p4-bucles-multiplicacio`).
- **Problema:** amb `b` negatiu, el patró de sumes successives no acaba, i la
  pregunta del «nombre màxim d'instruccions» pressuposa `b` acotat.
- **Acció proposada:** precisar «dues variables **naturals**» (o «amb
  `b ≥ 0`»). Canvi mínim d'enunciat: demano confirmació perquè pot venir d'un
  examen original.

---

## 4. Català normatiu i llengua

### T25 🟡 [C] Grafia pre-2016: «dóna» ×2
- **On:** `A3.qmd:144` («la divisió … dóna quocient … dóna quocient»).
- **Acció:** «dona» (normativa IEC vigent, coherent amb la resta del llibre).

### T26 🟡 [C] «trucada al sistema operatiu» → «crida al sistema»
- **On:** `A3.qmd:603`.
- **Acció:** «…invoca una crida al sistema operatiu (@sec-ei-ecall)» (coherent
  amb T9).

### T27 🟢 [D] Convenció de dígits hexadecimals (majúscules/minúscules)
- **On:** general. Exemples dins del mateix T3: `0xE6666666` i `0x0040000C` vs
  `0x0fc10000` (A3:1113-1115) i `0x7fffeffc` (A3:1516); el fragment RARS usa
  `0x7FFFFFFC`; A2 barreja (28 línies amb majúscules, 7 amb minúscules).
- **Acció proposada:** fixar «dígits en majúscula, prefix `0x` en minúscula» i
  aplicar-ho. **Decisió d'abast:** només T3 en aquest xat (i anotar la tasca
  global), o tot el llibre en una passada a part.

### T28 🟢 [C] «mig-word» → «mitja paraula»
- **On:** `A3.qmd:1063` («les variants de byte i mig-word»).
- **Acció:** «…de byte i de mitja paraula» (terme fixat a T2 per a `lh`/`sh`).

### T29 🟢 [C] Primera aparició de *lazy* amb l'ordre invertit
- **On:** `A3.qmd:363` («de forma ***lazy*** (gandula)»).
- **Acció:** «de forma **gandula** (***lazy***)», segons la regla de primera
  aparició d'anglicismes de `13_contrib.qmd`. (El títol de §361 pot mantenir
  «Avaluació *lazy*».)

### T30 🟢 [C] «naïve» → «ingènua»
- **On:** `A3.qmd:885` («Traducció naïve del bucle `for`»).
- **Acció:** «Traducció ingènua del bucle `for`».

### T31 🟢 [C] Concordança a E3
- **On:** `E3.qmd:162` («si el nombre d'instruccions executades **fossin** 10»).
- **Acció:** «fos 10».

### T32 🟢 [C] Frase dels segments amb pleonasme i concordança
- **On:** `A3.qmd:996` («…`.data` per a les variables globals i constants
  simbòliques, **a les quals** en temps de compilació **s'hi** escriu…»).
- **Acció:** reformular, p. ex.: «…als quals s'escriu en temps de compilació
  mitjançant les directives de segment (@nte-segments-memoria)».

### T33 🟢 [C] Microlint
- **On:** `A3.qmd:72` (triple espai «perquè   els positius»);
  `A3.qmd` `#cau-instruccions-no-sla` (espai abans del punt: «~~slai~~ .»);
  `21_riscv/RV32I_instruccions_desplacament_bits_aritmetics.qmd` (espai inicial
  abans de `|` a les files de la taula).
- **Acció:** netejar.

### T34 🟢 [D] Pendent d'autor ja marcat al text
- **On:** `A3.qmd:238` (`#cau-boolea-c`): TODO d'Adrià sobre «unes expressions
  no nul·les…» — cal decidir com identificar quines expressions sí i quines no.
- **Acció:** requereix decisió teva de contingut; puc proposar una redacció a
  la Fase C si m'ho confirmes.

---

## 5. Verificacions superades (sense incidència — registre)

- **Càlculs (script):** `slli`/`srli`/`srai` dels tips; deducció Ca2→Ca1
  (−51: `0xCD`→`0xCC`, i validació algèbrica general); codificació
  `beq x0,x0,+12` = `0x00000663`; exemple de `la` (`0x0FC10000`, `hi_20`,
  reconstitució); adreces de l'exemple d'enllaçat (`0x00400050`, `0x00400060`,
  `0x0040008B`, `0x10010008`); `#sol-p4-logica-bitabit` (4 resultats);
  rotació de 16 posicions (traça equivalent verificada per simulació);
  desplaçaments de 64 bits **inclosa la versió genèrica amb n = 0** (simulació
  exhaustiva n ∈ {0,1,5,31}); recompte de 55 instruccions, temps i CPI del
  `for`; costos $13N+6$, $13N+5$, $12N+1$, $11N+1$, $9N+2$, $8N+4$ (tots
  correctes); alineacions i offsets dels 4 blocs d'activació (52, 12, 60 i 12
  bytes).
- **RARS 1.6 (empíric):** `la` s'expandeix en 2 instruccions (etiqueta del
  `jalr` a base+12, com pressuposa S3); traça de `jalr` amb `rd = rs1` → 3
  execucions (resposta c ✓); `li t3, ' '` vàlid (`0x20`); les dues sintaxis de
  `jalr` assemblen.
- **Referències creuades:** les 17 etiquetes referenciades des de T3 cap a
  A1/A2/A4/A9/E2 existeixen totes; cap col·lisió d'IDs `p4-` (E4 usa `p5-`).
- **Cobertura de solucions:** S3 conté exactament els 12 exercicis de la taula
  T3 de `S_criteris.qmd` — **no cal afegir-ne** (el criteri ~1 de cada 2-3 es
  compleix: 12/37).
- **Sigles:** `BA`, `ABI`, `LIFO` presents a `12_sigles.qmd`.
- **Terminologia T2↔T3 (pendent antic de `CLAUDE.md`):** A2 usa la columna
  «Qui el guarda (*Saver*)» amb Caller/Callee; A3 introdueix
  temporals/segurs mapant-los explícitament a caller-saved/callee-saved
  (`A3.qmd:1572`) i el resum ABI coincideix fila a fila amb el fragment.
  L'encaix sembla ja resolt; només T15 (include) hi afecta.

---

## 6. Ordre d'execució proposat per a la Fase C

1. Correccions tècniques [C]: T01–T11 (sense T12).
2. Coherència [C]: T13–T18.
3. Format/pedagogia [C]: T19–T23.
4. Llengua [C]: T25, T26, T28–T33.
5. Presentar les decisions [D]: **T12** (recomanem opció A), **T24**, **T27**
   (abast), **T34**.
