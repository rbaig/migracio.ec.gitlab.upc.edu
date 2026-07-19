# L4 — Revisió interna: llista d'accions

Data: 2026-07-19 · Xat: `EC L4 Revisió interna` · Fase B completada.

**Mètode de verificació**: execució empírica amb **RARS 1.6** (release oficial `rars1_6.jar`, `@rars_v16`) per a assemblabilitat, punt d'entrada i estat final de memòria; aritmètica exacta amb Python per a totes les taules i fórmules. Tots els valors numèrics de L4 (taula d'adreces de `s4_2_1`, traça de `s4_2_2`, valors 1/4/3/1 als offsets 0/44/68/108, `resultat = 20`, stride 24, sentinella `@m+104`, mides de BA 12 i 4) han quadrat: **cap error de càlcul**. Els errors detectats són d'assemblabilitat, executabilitat i coherència.

---

## A. Errors crítics (el codi no assembla o falla en execució a RARS)

### A1. `.space` amb expressions `.eqv` no assembla — `s4_1_1.s` i `s4_2_2.s` [CRÍTIC]

**Evidència empírica** (RARS 1.6): `mat1: .space NF1*NC1*4` → «Invalid language element: NF1*NC1*4». RARS **no avalua cap expressió aritmètica** en cap operand: ni `.space 5*6*4` (literals), ni `li t0, NC*4`, ni `la t0, mat+8`, ni `.eqv T, 5*6*4`. Un símbol `.eqv` només és vàlid com a substitució d'un **literal únic** (també en hexadecimal; un valor negatiu com `.eqv NEG, -4` també falla: «Malformed .eqv directive»).

**Afecta**: `s4_1_1.s` (3 ocurrències: `.space NF1*NC1*4`, `.space NF2*NC2*1`, `.space NF3*NC3*8`) i `s4_2_2.s` (1: `.space NF1*NC1*4`).

**Acció**: substituir per literals amb el càlcul al comentari (forma verificada que assembla i s'executa):

```
mat1:   .space 120              # int mat1[5][6]: NF1*NC1*4 = 120 bytes
```

**Depèn de la decisió B2** (què fer amb els `.eqv` que queden sense ús a `s4_1_1.s`).

### A2. Subrutina abans de `_start`: el programa falla en execució — `s4_2_2.s` i `s4_3_1.s` [CRÍTIC]

**Evidència empírica**: RARS 1.6 inicia l'execució a la **primera instrucció de `.text`**, tant en CLI com en GUI amb configuració per defecte. L'opció «Initialize Program Counter to global "main" if defined» (flag `sm` en CLI) només reconeix l'etiqueta **`main`**; **`_start` no és cap punt d'entrada per a RARS** (verificat amb programa de prova). Amb l'ordre actual de L4:

- `s4_2_2.s`: l'execució comença a `subr` amb `a0 = 0` → «Runtime exception: address out of range 0x00000000».
- `s4_3_1.s`: comença a `suma_col` amb `a0 = 0` → mateixa excepció; `resultat` queda a 0.

Reordenats amb `_start` primer, tots dos s'executen correctament i **tots els valors de les Comprovacions pràctiques es compleixen** (verificat: 1/4/3/1 als offsets 0/44/68/108; `resultat = 20`).

**Acció**: moure `_start` com a **primera etiqueta de `.text`** als dos programes (patró que ja segueixen sistemàticament L2 i L6). Vegeu també la troballa transversal D2 (L3 i L5 tenen el mateix problema) i D3 (documentar el comportament del PC inicial).

---

## B. Decisions que requereixen la teva aprovació

### B1. `_start` amb pròleg/epíleg complet (L4) vs. `_start` sense preservar res (L3)

A L3, `_start` crida subrutines **sense** desar `ra` ni crear BA (i el material no ho problematitza). A L4, els dos exercicis demanen classificar `_start` com a uninivell/multinivell i les solucions li fan pròleg/epíleg complet (desar `s0`, `s1`, `ra`).

Tècnicament, `_start` no té caller: no ha de restaurar registres segurs per a ningú, `ra` no conté cap adreça de retorn útil, i el programa acaba amb `ecall` exit (mai `ret`). Desar `s0`/`s1`/`ra` és codi mort. En canvi, **usar** `s0`/`s1` sense desar-los és correcte i suficient perquè els valors sobrevisquin les crides (l'ABI garanteix que `subr` els preserva).

**Opcions**:

- **(a) Simplificar `_start` (recomanada, coherent amb L3)**: eliminar pròleg/epíleg de `_start` als dos programes; `_start` usa `s0`/`s1` directament. Reformular la pregunta 2 de `#exr-subr-matrius` i el pas 5 de `#exr-suma-columna` (p. ex.: «`_start` fa crides però no és el callee de ningú i acaba amb `ecall` exit: no ha de desar ni restaurar res. Sí que ha d'usar registres **segurs** per a les dades que han de sobreviure les crides»). La pregunta 3 (identificar dades abans/després de crida → registres segurs) es manté intacta i guanya protagonisme.
- **(b) Mantenir el pròleg/epíleg com a disciplina pedagògica**: exigiria afegir-lo també a L3 per coherència, i idealment una nota que expliqui que a `_start` és una convenció d'estil, no una necessitat de l'ABI.

En el cas (a), el «Pas 4. Blocs d'activació» de `#sol-subr-matrius` canvia (BA de `_start` buit) i la fila «`ra` | `ra` (desat al BA)» de la taula del Pas 3 desapareix (vegeu C6).

### B2. Destí dels `.eqv` de `s4_1_1.s` un cop `.space` passi a literals

Amb A1 aplicat, els 8 `.eqv` de `s4_1_1.s` queden sense cap ús al codi (el `.text` és només l'exit). L'enunciat diu «Useu `.eqv` per a les dimensions de cada matriu (@imp-eqv-dimensions)».

**Opcions**:

- **(a) Mantenir els `.eqv`** com a documentació de dimensions (i coherència amb `s4_2_2.s`, on `NC1`/`NC4` sí que s'usen al codi), esmentant a la solució que RARS no permet usar-los dins `.space`.
- **(b) Retirar el requisit `.eqv` de `s4_1_1`** (les dimensions van només als comentaris) i introduir-los a `s4_2_2`, on tenen ús real.

En tots dos casos, cal una **frase explícita a la solució** (o un callout breu) que digui que RARS no avalua expressions als operands i que per això la mida de `.space` s'escriu com a literal. Recomanació: opció (a) + frase explicativa.

### B3. Abast de la correcció transversal de les expressions aritmètiques (D1) i de l'ordre `_start` (D2)

Els mateixos dos problemes crítics afecten fitxers fora de L4 (detall a D1/D2). Cal decidir si: (a) es corregeixen en aquest xat (jo mateix a la Fase C), (b) s'anoten al `TODO.md` per als xats corresponents (L3, L5, L6 tenen revisió interna pendent; A4 està «preparat per a revisió externa» però `CLAUDE.md` prioritza l'harmonització prèvia), o (c) una combinació (p. ex. jo faig A4 aquí i L3/L5/L6 s'ho troben anotat). Recomanació: **(c)** — A4 aquí (és la teoria de referència de L4 i el criteri d'harmonització ho empara), L3/L5/L6 anotats al TODO per als seus xats.

---

## C. Correccions directes a L4 (no requereixen aprovació; les executaré a la Fase C)

### Tècniques i de coherència

- **C1. Unificar `NB` → `T`** (mida d'element): L4 §1 i §2 usen `NB`; L4 §3 i tota la teoria (A4, `@eq-acces-aleatori-matriu`) usen $T$. Canvis: intro de §1 («elements de $T$ bytes… `NF*NC*T`» — vegeu C2 per al format), fórmula de §2, columna «`NB`» → «$T$» de la taula de `#sol-adreces-matrius` i les dues mencions en prosa.
- **C2. Harmonitzar la fórmula de §2 amb la forma canònica d'A4**: `$$\texttt{@mat[i][j]} = \texttt{@mat} + (i \cdot NC + j) \cdot NB$$` → `$$@\texttt{mat[i][j]} = @\texttt{mat[0][0]} + (i \cdot \texttt{NC} + j) \cdot T$$` (tres coses: `@` fora del `\texttt`, com a la resta del llibre i a la mateixa L4 §3; `\texttt{NC}` en lloc de cursiva matemàtica, que es llegeix com a producte $N \cdot C$; base `@mat[0][0]` com a l'equació de la teoria). Mateixa harmonització a la fórmula repetida dins `#sol-adreces-matrius`.
- **C3. Nota d'estil a `#sol-suma-columna` sobre l'estructura del bucle**: la solució elimina la variable d'inducció `i` (compara amb sentinella, com a l'optimització #3) mantenint l'estructura while del C. Afegir una frase que ho expliciti amb referències: comparació d'adreces com a naturals → `bgeu`/`bltu` (@cau-opt3-eliminacio-induccio), i remissió a @sec-opt-eliminacio-induccio. Ara mateix la solució usa `bgeu`/`bltu` sense justificar-ho enlloc de L4.
- **C4. Taula del Pas 4 de `#sol-suma-columna`**: diu «`*p` → `t4`», però `t4` també s'usa abans del bucle com a temporal per a `NF` (`li t4, NF`). Afegir una nota breu («`t4` es reutilitza abans del bucle com a temporal per calcular la sentinella») o passar el temporal a `t5`. Triaré la nota (canvi mínim).
- **C5. Precisió a `#sol-declaracio-matrius`**: «tot i que `.align 3` de `mat3` ja garanteix alineació a 4 bytes» — el que ho garanteix és que `mat3` comença en múltiple de 8 **i ocupa 32 bytes** (múltiple de 4). Reformular: «tot i que, com que `mat3` comença en una adreça múltiple de 8 i ocupa 32 bytes, l'adreça següent ja és múltiple de 4». (Layout verificat empíricament: `mat1` = base, `mat2` = base+120, `mat3` = base+136 —múltiple de 8—, `mat4` = base+168.)
- **C6. Taula del Pas 3 de `#sol-subr-matrius`**: fila «`ra` | `ra` (desat al BA)» — presentació confusa (la «dada» és l'adreça de retorn). Es resol segons B1: amb l'opció (a) desapareix; amb la (b), reformular la cel·la esquerra com a «adreça de retorn».
- **C7. Repetició a `#sol-subr-matrius`**: «`subr` és uninivell… BA buit» apareix al Pas 1–2, al final del Pas 3 i de nou al Pas 4. Deixar-ho al Pas 1–2 i compactar les altres dues mencions.
- **C8. `mat` de `s4_3_1.s` en 4 línies `.word`** (una per fila), seguint el patró recomanat a A2 (@tip-rv32i-declaracio-inicialitzacio-vects-mats) per visualitzar l'estructura bidimensional. Verificat que assembla igual.

### Llenguatge (català normatiu i terminologia del projecte)

- **C9. «offset» → «desplaçament» en prosa** (substitució obligatòria de `13_contrib.qmd`): «amb els offsets de cada element» (`#exr-subr-matrius`, pas 4), capçaleres «Offset des de `sp`» (×2) → «Desplaçament des de `sp`», «sumant l'offset a l'adreça base» (Comprovació pràctica 1). Els `offset` dins de codi/fórmules no es toquen.
- **C10. «*breakpoint*» → «punt d'aturada»** (×2, Comprovacions pràctiques): el terme establert i definit a L1 és «**punt d'aturada** (*breakpoint*)»; L2, L3 i L5 ja no usen l'anglicisme sol. (L6 en té 1 cas: anotat a D6.)
- **C11. «secció `.data`» → «segment `.data`»** (`#exr-declaracio-matrius`): terme del projecte segons `13_contrib.qmd` («directives de segment») i A2 («segment de dades»). (L3 té el mateix cas: anotat a D6.)
- **C12. Primera aparició de «stride» a L4**: `l'**stride**` → `l'***stride***` (anglicisme en primera aparició al fitxer + concepte nuclear, mateix criteri que A4).
- **C13. Punts finals a les tres vinyetes** de l'enunciat de `#exr-declaracio-matrius` («…`.align 2`)», «…d'alineació)», «…(@cau-long-long-2-regs)») — regla de puntuació del projecte. Les vinyetes de `#exr-adreces-matrius` (`@mat1[4][3]`…) són ítems de notació, sense punt: correctes.
- **C14. Estil menor**: reordenar «correspon a sumar l'stride calculat a l'apartat anterior en assemblador» → «correspon, en assemblador, a sumar l'stride calculat a l'apartat anterior» (pregunta 3 de `#exr-suma-columna`); netejar els dobles espais del comentari `# t0 = x[i][j] = *(  @x + … )`.

---

## D. Troballes transversals (fora de L4)

- **D1. Expressions aritmètiques als operands — sistèmic** (vegeu B3):
  - `A4.qmd`: `.space NF*NC*4` (L. 339); `li tX, NC*4` / `NC*2` (7 ocurrències als tips d'optimització i sumacolumna); `la t3, mat + 5*4`, `la t3, mat + 3*NC*4`, `la t3, mat + 3*NC*4 + 5*4` (tips d'accés amb índexs constants — `la` amb `label+const` tampoc és vàlid a RARS: «Expected: la t1,label»).
  - `L6.qmd`: `.space N*4` i similars (≈8 ocurrències amb `.eqv`).
  - Els fragments d'A4 són genèrics/il·lustratius (NF/NC no definits), però els estudiants en copien el patró. Si es mantenen simbòlics, cal com a mínim un `#imp-` que adverteixi que RARS només accepta literals; si es passa a literals, la coherència amb el laboratori queda garantida.
- **D2. Ordre subrutina/`_start`**: L3 (2 blocs: `moda`; `codifica`/`g`) i L5 (3 blocs: `abs`; `descompon`; `compon`) tenen subrutines abans de `_start` → mateixa fallada d'execució que A2. L2 i L6 ja posen `_start` primer.
- **D3. Documentar el punt d'entrada de RARS**: cap material (L1 inclòs) explica que RARS comença a la primera instrucció de `.text` i que `_start` no és una etiqueta reconeguda pel simulador. Proposta: (i) afegir a `13_contrib.qmd §Convencions globals del laboratori` la regla «`_start` ha de ser la **primera etiqueta** de `.text`»; (ii) valorar un `#nte-` RARS breu (a L1 §Punts d'aturada/execució o a A2) que ho expliqui a l'estudiant.
- **D4. `12_sigles_simbols.qmd §Símbols`**: `NF`, `NC`, $T$ (mida d'element) i *stride* apareixen en fórmules de T4/L4 i no tenen entrada. Encaixa amb la tasca transversal ja oberta al TODO («nodrir les taules de Símbols i Notació»). Puc proposar les entrades concretes a la Fase C si vols.
- **D5. Etiquetes de bucle**: el patró dominant és `for:`/`fifor:` (10+10 ocurrències, L4 inclòs); L3 usa `for1`/`for2`/`ffor1`/`ffor2` en un exercici. Harmonització menor candidata per al xat de L3.
- **D6. Casos paral·lels dels punts C10/C11**: «*breakpoint*» sol a L6 (1 ocurrència); «secció `.data`» a L3 (L. 94) i «secció `.text`» a A2 (L. 364).
- **D7. `.eqv` amb valor negatiu no és vàlid a RARS** («Malformed .eqv directive») — cap material actual en depèn; anotat com a coneixement de referència per a futurs exercicis.

---

## E. Verificat sense canvis

- **Totes les 16 referències creuades** de L4 resolen (A2 ×3, A3 ×4, A4 ×8, L6 ×1); l'àncora `#sec-sessio-matrius-subrutines` és apuntada correctament des d'`index.qmd` i `Lcalendari.qmd`.
- **Tota l'aritmètica**: mides (120/15/32), taula d'adreces (108/14/16/8), paraula baixa/alta de `mat3[1][0]` (+16/+20), traça C de `s4_2_2` (1/4/3/1), fórmula `@m+24i+8`, stride 24, equivalència `p += 6` ↔ 24 bytes, sentinella `@m[4][2] = @m+104`, `resultat = 20`, mides de BA (12 i 4, múltiples de 4 conforme a @nte-abi-alineacio-pila).
- **Disposició del BA de `_start`** (`s0`, `s1`, `ra` de baix a dalt) conforme a @nte-abi-variables-locals.
- **Convencions de laboratori**: `### Lliuraments`/`### Lectura prèvia` (Heading 3, unnumbered, frases d'introducció idèntiques a L2/L3), títols d'`#exr-` = noms de fitxer, numeració `s4_<secció>_<exercici>` coherent amb les seccions, `.eqv` abans del primer segment, `.data`/`.text` a columna 0, sortida `li a7, 93` + `li a0, 0` + `ecall`, Comprovacions pràctiques com a `callout-tip` sense etiqueta `#tip-`, `#wrn-` amb `collapse="true"` i títol.
- **Semàntica dels accessos**: `bgeu`/`bltu` per a comparació d'adreces és correcte (C3 només hi afegeix la justificació); `lw a1, 8(s1)` = `mat4[0][2]` correcte; `mul` + `slli` per al càlcul d'adreces conforme a @imp-ec-mul-adreces.
- **Alineació de `long long` a 8 bytes** (`.align 3`): conforme a l'ABI ILP32 de RISC-V; layout verificat empíricament a RARS.
- **Veu**: enunciats en 2a persona del plural i Comprovacions pràctiques en imperatiu plural (instruccions operatives), conforme a la guia.
- **Enllaç `[Sessió 6](#sec-sessio-mc)`**: funciona entre capítols a Quarto book i segueix el precedent d'A2 (`[Tema 8](#sec-tema-mv)`).
- **Taula d'strides de §3** (fila/columna): subconjunt correcte i coherent amb @sec-matrius-recorreguts.
