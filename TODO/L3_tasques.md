# L3_tasques.md — Revisió interna de `04_laboratori/L3.qmd`

Data: 2026-07-19. Fase B completada (Fable 5 High + Thinking). Verificació numèrica de totes les seccions crítiques: **superada** (vegeu §V al final). Les tasques marcades **[DECISIÓ]** requereixen aprovació de l'usuari abans d'executar-se; la resta són executables directament a la Fase C.

Prioritats: 🔴 crítica · 🟠 alta · 🟡 mitjana · 🔵 baixa.

---

## T — Correcció tècnica

### T1 🔴 [DECISIÓ — convenció transversal] `_start` després de les subrutines: els programes no s'executen a RARS

**Fet verificat al codi font de RARS** (`Settings.START_AT_MAIN`, per defecte `false`; `RegisterFile.initializeProgramCounter`; `SymbolTable.startLabel = "main"`): el PC inicial és **la primera instrucció de `.text`**; l'única alternativa és l'opció «Initialize program counter to global 'main'», que només reconeix l'etiqueta `main` — **mai `_start`**. La directiva `.globl _start` no hi té cap efecte.

Conseqüència: a `s3_4_2.s` l'execució comença dins d'`update`/`moda` i a `s3_5_1.s` dins de `g`, amb `a0`/`a1` = 0 → accés a l'adreça `0x0` → excepció immediata.

- **Blocs afectats a L3**: `sol-moda` (bloc L357) i `exr-depuracio`/`sol-depuracio` (blocs L490 i L599).
- **Transversal**: L4 (`subr`, bloc L204; `suma_col`, bloc L395), L5 (`cfixa`, bloc L286; `cfixa`+`cflotant`, bloc L380). L1, L2 i L6 no afectats (`_start` sempre primer).
- **Proposta**: (a) moure el codi de `_start` al **principi de `.text`** en tots els blocs afectats (reubicant el comentari «inseriu el codi aquí»); (b) afegir la convenció a `13_contrib.qmd §Convencions globals del laboratori`: «El codi de `_start` va al principi de `.text`, abans de les subrutines: RARS inicia l'execució a la primera instrucció del segment de text»; (c) anotar a `TODO.md` la correcció pendent de L4 i L5 (o autoritzar-la ara en aquest mateix xat).

### T2 🔴 [DECISIÓ — redacció] El C d'`exr-compta-caracter` no és equivalent a l'assemblador

El comentari `i++; /* reutilitzem i com a comptador */` fa que `i` sigui alhora índex i comptador: (1) **cap variable acaba contenint 12**; (2) després de cada coincidència el recorregut **salta un caràcter**; (3) com que l'**últim** caràcter de `w` és `'4'`, l'incrément doble salta el sentinella i llegeix `w[32]`, **fora del vector** (comportament indefinit). Simulació: el C literal no computa el recompte; l'assemblador de la solució sí (`s0 = 12`).

- **Proposta de C corregit** (manté índex al C ↔ punter a l'assemblador, coherent amb la Nota de l'enunciat):

```c
char w[32] = "4444185720444938167204449251044";
int  n = 0;

void main() {
    int  i   = 0;
    char car = '4';
    while (w[i] != '\0') {
        if (w[i] == car)
            n++;
        i++;
    }
}
```

  i ajustar l'enunciat: «…compti a `n` (registre `s0`) quantes vegades…» o mantenir «deixi el resultat a `s0`» mapant `n → s0`. Nota: `n` global no s'ha de declarar a `.data` si només viu a `s0` — precisar-ho a l'enunciat o fer `n` local.

### T3 🟠 [DECISIÓ] `exr-depuracio` s'autoresol

Els comentaris del codi de l'**enunciat** revelen literalment els errors: «`(B) ra no es desa`», «`(C) passa pfraseout en lloc de pfrasein`», «`(D) escriu a pfrasein en lloc de pfraseout`», «`(E) ra no es restaura`». Opcions:

- (a) Eliminar totes les marques i els comentaris delators; la solució cita les línies directament.
- (b) Mantenir marques neutres `(A)`–`(E)` en línies candidates (amb `(A)` correcta com a distractor) i reformular l'enunciat: «tres de les cinc línies marcades contenen errors».
- (c) Substituir els comentaris per la **intenció** del C (p. ex. `# crida g(alfabet, pfrasein)` a la línia errònia), que és el patró de comentari de la resta del fitxer i deixa la detecció a l'estudiant.

**Recomanació**: (c); alternativament (a).

### T4 🟡 [DECISIÓ menor] Fidelitat C↔dades a `exr-depuracio`

`char w1[16] = "ARQUITECTURA"` (C) vs `.asciz` (13 bytes reservats). Proposta mínima: `char w1[] = "ARQUITECTURA";` al C (13 bytes, coincideix amb `.asciz`). `alfabet[27]` i `w2[16]` ja coincideixen exactament.

### T5 🔵 Precisió de la conseqüència de l'error (B)/(E) a `sol-depuracio`

«Quan `codifica` executa `ret`, salta a una adreça incorrecta i el programa falla» → precisar: `ret` salta a l'adreça de retorn de l'**última crida a `g`** (la instrucció següent al `jal` dins del bucle), de manera que l'execució reprèn en un punt incorrecte del cos del bucle amb l'estat ja restaurat.

### T6 🔵 [DECISIÓ — redacció] Ambigüitat del límit d'instruccions a `exr-bits-invertir`

«El programa ha de tenir menys de 5 instruccions» no aclareix si compta la seqüència de sortida (3 instruccions més). Proposta: «El càlcul (sense la seqüència de sortida) ha de tenir com a màxim 4 instruccions».

---

## C — Coherència L3 ↔ A3

### C1 🟡 Precisió de la regla de registres segurs (§4, intro)

«Cal preservar `ra` i els registres segurs (`s0`–`s11`) que continguin valors generats abans d'una crida i usats després» barreja el criteri d'**assignació** (`@sec-determinacio-registres-segurs`: valors generats abans i usats després → registre segur) amb el deure de **preservació** (`@cau-regla-registres-segurs`: tota subrutina deixa els `s` que usa com els ha trobat). Proposta: «cal assignar a registres segurs (`s0`–`s11`) els valors generats abans d'una crida i usats després, i la subrutina ha de desar i restaurar tant aquests registres com `ra`».

### C2 🔵 Nexe compta-caracter ↔ moda sobrevalorat

`exr-moda`: «segueix **exactament** el mateix patró de recorregut **amb punter**» — a `moda` la traducció és literal amb **base+índex** (`add t0, s0, s2`), no amb punter (la mateixa `sol-moda` ho matisa bé). Suavitzar: «el mateix patró de recorregut seqüencial caràcter a caràcter (ara amb índex explícit)». Coherentment, a la Nota d'`exr-compta-caracter`: «és un patró que reapareixerà, amb variacions, a l'exercici de subrutines».

### C3 🔵 Lectura prèvia: pseudoinstruccions de salt que les solucions usen

Les solucions usen `bgt`, `ble` i `beqz` (pseudos), però la fila de salts condicionals només referencia les natives. Afegir `@nte-pseudoinstruccions-salt-condicional` i `@nte-pseudoinstruccions-salt-zero` a la fila corresponent. Valorar també una fila per a l'avaluació lazy (`@sec-traduccio-operadors-logics`, `@imp-ec-lazy-evaluation`), que ara només apareix al cos de §2.

### C4 🔵 Referència més precisa per al lazy encadenat (§2, intro)

A més de `@sec-if-then-else`, referenciar `@sec-avaluacio-lazy-encadenats` (A3), que és exactament el contingut que l'exercici aplica (criteri contrib: «com més precises, millor»).

### C5 🔵 Formulació d'`exr-update`

«Determineu quins registres, si n'hi ha, necessiten ser segurs» → alinear amb A3: «Determineu quins valors, si n'hi ha, cal assignar a registres segurs».

---

## P — Pedagogia i format

### P1 🟡 [DECISIÓ — convenció transversal] Convenció «Comprovació pràctica» vs. pràctica real

`13_contrib` mana posar les verificacions RARS com a `{.callout-tip title="Comprovació pràctica"}` dins de `{#sol-}`. Realitat: L3 en té 0 (les tres comprovacions amb valors esperats són al final dels **enunciats**), L2 en té 0, L1 en té 1. Observació pedagògica: **els lliuraments es fan abans de la sessió**, així que l'estudiant necessita els valors esperats mentre treballa amb l'enunciat — la ubicació actual és defensable. Opcions:

- (a) Aplicar la convenció tal com està escrita (moure les comprovacions a tips dins de les solucions).
- (b) **[Recomanada]** Actualitzar la convenció a `13_contrib`: els valors esperats de verificació van al final de l'enunciat (perquè el lliurament és previ); el callout «Comprovació pràctica» dins de `{#sol-}` es reserva per a instruccions d'ús del depurador o verificacions addicionals.

### P2 🟡 [DECISIÓ] Lliurament d'`exr-depuracio` incomplet respecte del que es demana

Es demana «identifiqueu cada error, **expliqueu** per què és incorrecte i escriviu la línia corregida», però només es lliura `s3_5_1.s`. Opcions: (a) afegir `s3_5_1.md` per a les explicacions (com `s3_4_2.md`); (b) demanar les explicacions com a comentaris dins del `.s` (afegint la frase a l'enunciat); (c) reduir l'enunciat a lliurar només el programa corregit. **Recomanació**: (b) o (a).

### P3 🔵 [DECISIÓ — harmonització] `filename` dels blocs de codi

- `exr-depuracio`: `{.c filename="..."}` (placeholder literal) → `filename="s3_5_1.c"`; `{.s}` sense filename → `filename="s3_5_1.s"` (és el punt de partida que l'estudiant corregeix).
- `exr-update`: `filename="C"` vs. el patró `s3_X_Y.c` de la resta d'exercicis (`s3_2_1.c`, `s3_3_1.c`, `s3_4_2.c`). Harmonitzar (proposta: `s3_4_1.c`) o establir criteri a `13_contrib` (la seva taula actual només preveu `filename="C"`).

### P4 🔵 Referències `@` dins de comentaris de codi (no es resolen)

`# update: vegeu @sol-update (inseriu el codi aquí)` i `# for (...) ← mateix patró que exr-compta-caracter` es renderitzen literalment. Substituir per text pla: «vegeu la solució de `s3_4_1.s`; inseriu-hi el codi» i «mateix patró que s3_3_1.s».

### P5 🔵 Justificació dubtosa a la intro de §1

«…sense recórrer a operacions aritmètiques costoses»: la solució usa `addi` (aritmètica), i el contrast cost-aritmètica/lògica no s'ha establert enlloc. Proposta: «Les operacions de desplaçament i lògiques bit a bit permeten construir i aplicar màscares per manipular bits individuals».

### P6 🔵 «dígits numèrics» → «dígits decimals»

A `exr-compta-caracter` («31 dígits numèrics» és redundant).

---

## L — Llengua

### L1 🟡 Primera aparició de «lazy» a L3 sense marcar

A3 estableix «**gandula** (***lazy***)» i després «lazy» sense cursiva; la regla de primera aparició és per fitxer. A L3 (línia 87): «L'avaluació lazy» → «L'avaluació gandula (*lazy*)» (les aparicions posteriors, com la de l'enunciat, queden en rodona, correctes tal com estan).

### L2 🔵 Apostrofació: «del cos del `else` exterior» → «de l'`else` exterior»

(línia 87; s'apostrofa davant de mot començat en so vocàlic, també quan és codi).

### L3 🔵 [DECISIÓ — estil] Notació del rang a `exr-bits-invertir`

«`X` (X ∈ [0,31])» barreja text pla amb símbols matemàtics. Opcions: `$0 \le X \le 31$` (math, criteri contrib per a rangs) o prosa «(amb `X` entre 0 i 31)». En qualsevol cas, no deixar `∈`/`[0,31]` en text pla.

### L4 🔵 Sigla BA sense expandir a L3

Primera menció de la sigla: «El BA és buit» (`sol-update`). Expandir a la primera aparició del concepte al fitxer (§4 intro, línia 241): «…al bloc d'activació (BA)…»; a partir d'aquí «BA» lliurement.

### L5 ℹ️ Aspectes verificats i nets

Cap «ample de banda», cap unitat decimal fora de criteri, cap cometa recta en prosa, cap doble espai, veu correcta (enunciats en 2a p. plural; explicacions impersonals; cap «nosaltres» fora de lloc), punts finals correctes, hexadecimals en majúscules, etiquetes de bucle descriptives admeses («en la pràctica s'admeten etiquetes descriptives», A3) — vegeu però X6.

---

## X — Transversals (fora de L3; anotar a `TODO.md` o executar amb aprovació)

- **X1** (lligada a T1): correcció de `_start` a L4 (2 blocs) i L5 (2 blocs) + convenció a `13_contrib.qmd`.
- **X2** — TODO §A2 «identificador duplicat `sec-opt-acces-sequencial`»: als laboratoris només hi ha **referències** (L4:32, L4:303, L6:49), cap definició → la cerca de la segona definició queda acotada a `Ex.qmd`/`Sx.qmd`.
- **X3** — TODO §A4 referències trencades (`@sec-ecall`, `@sec-operands-memoria`, `@imp-ec-alineacio-pila`, `@imp-exception-handler`): **cap** als laboratoris L1–L6 → acotat a E9/S9/`13_contrib.qmd`.
- **X4** — TODO «ample de banda» i «KB/KiB»: **L1–L6 nets** (verificat 2026-07-19) → es poden marcar els laboratoris com a revisats en aquestes dues entrades.
- **X5** — `13_contrib.qmd §Bibliografia`: «Definició: al fitxer `bibliografia.qmd`» → el fitxer real és `15_bibliografia.bib` (`_quarto.yml: bibliography:`).
- **X6** 🔵 [DECISIÓ] Slug `nte-instruccions-desplacament-arithmetic` (grafia anglesa) vs. la resta d'slugs en català. Reanomenar a `...-aritmetic` tocaria A3 (definició), L3 i L5 (referències). Baixa prioritat; si es fa, cerca-reemplaça global.
- **X7** — `CLAUDE.md` línia 79: «zobacz `TODO.md`» → «vegeu `TODO.md`» (mot polonès).
- **X8** ℹ️ — Etiquetes `{#sec-}` a les capçaleres `##` dels laboratoris: L3 no en té cap, com L2/L4/L5 (L1 en té algunes). La regla de `CLAUDE.md` només obliga els `Ax.qmd`; cap referència externa apunta a seccions internes de L3 (només `#sec-sessio-traduccio`, usada per `Lcalendari.qmd`, que resol correctament). **Cap acció necessària**; només etiquetar si en el futur cal referenciar-les.

---

## V — Registre de verificació numèrica (Fase B, sense accions)

| Secció | Verificació | Resultat |
| :--- | :--- | :--- |
| `sol-bits-invertir` | Simulació asm vs. C per a X = 0, 1, 5, 31 (incl. semàntica `sll` amb 5 bits baixos) | ✅ idèntics; 4 instruccions de càlcul |
| `sol-classifica-caracter` | Traça asm vs. C dels 5 valors (`0x6D`,`0x5A`,`0x20`,`0x21`,`0x37`); avaluació lazy | ✅ `'m'`→`num`, `'Z'`→`num`, `' '`→0, `'!'`→0, `'7'`→−1; lazy respectada als dos `&&` i als dos `||` |
| `exr-compta-caracter` | Longitud cadena = 31; recompte `'4'` = 12; asm → `s0`=12 | ✅ (el C, en canvi, no ho computa: vegeu T2) |
| `sol-update` | Escalat `slli ×4`, direcció `ble` (¬(h[i]>h[imax])), cas `i == imax` | ✅ correcte (empat → retorna `imax`, coherent amb `>` estricte) |
| `sol-moda` | Simulació completa fidel al registre; histograma; BA | ✅ histo = [3,3,3,1,12,2,1,2,2,2] (Σ=31); resultat `'4'` (`0x34`); recàrrega de `t1` després de la crida correcta; offsets +0–39/40/44/48/52/56 i mida 60 conformes a la disposició canònica de `@nte-abi-variables-locals` (locals → segurs → `ra`) i a `@nte-abi-alineacio-pila` |
| `sol-depuracio` | `g` pas a pas; simetria A↔Z; traça completa | ✅ `"ARQUITECTURA"` → `"ZIJFRGVXGFIZ"`; `i` retornat = 12; BA de `codifica` (16 bytes, `ra`@12) conforme |
| Alineació `.data` | `num: .byte` seguit de `result: .word` | ✅ RARS auto-alinea `.word` a múltiple de 4 (verificat a `Assembler.java`, `autoAlign`) |
| Referències creuades | Les 24 refs externes de L3 | ✅ totes resolen a A3; cap duplicat (A5 usa sufix `-f`) |
| Lliuraments/numeració | `s3_<S>_<E>` vs. seccions numerades; taula de lliuraments | ✅ coherents (renumeració TODO 2026-07-05 aplicada) |
