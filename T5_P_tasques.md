# T5 / PE_T5 / PS_T5 — Llista de tasques proposades (revisió interna)

Anàlisi fet sobre: `T5.qmd`, `PE_T5.qmd`, `PS_T5.qmd`, `07_contrib.qmd`, `CLAUDE.md`, `svg.md`,
`registres.toml`, `05_riscv.qmd` + `11_riscv/`, `09_bibliografia.bib`, `T4.qmd`, `TODO.md`,
`T5_revisio_canvis.md`, `T5_figures_integracio.md`, `_quarto.yml`, `index.qmd`.

Verificació numèrica completa (Python) de tots els càlculs binaris/IEEE-754 de T5.qmd i PS_T5.qmd.

---

## A. Errors trobats — acció directa (sense necessitat de decisió)

### A1. 🔴 Error numèric a `T5.qmd` — error de representació de l'exemple de codificació

**Ubicació:** `#tip-ieee754-codificacio`, apartat g) "Error de representació" (línies ~182–191).

El document calcula l'error de representació com la diferència entre el valor **arrodonit** i el
valor **truncat a 23 bits** (és a dir, entre dos valors ja aproximats), en lloc de la diferència
entre el valor **arrodonit** (el que realment s'emmagatzema) i el valor **decimal exacte original**
$-1029{,}68$.

- Valor que dona el document: $\varepsilon = 5{,}722 \times 10^{-5}$.
- Valor correcte (verificat numèricament, `struct.pack` i `Decimal` amb 50 xifres de precisió):
  $\varepsilon = |{-1029{,}68005371\ldots} - ({-1029{,}68})| = 5{,}371 \times 10^{-5}$.

L'error del document prové de mesurar només la distància del pas d'arrodoniment (1 ULP = $2^{-13}
\approx 1{,}221\times10^{-4}$, dividit per 2 en valor absolut donaria un altre número, no coincident
tampoc), en lloc de la distància respecte del valor original. La codificació final `0xC480B5C3` **sí
és correcta** (verificada bit a bit); només l'error declarat és incorrecte.

**Acció proposada:** refer el pas g) partint del valor arrodonit real ($-1029{,}68005371\ldots_{10}$,
que s'obté revertint la codificació `0xC480B5C3`) i el valor exacte ($-1029{,}68$), donant
$\varepsilon \approx 5{,}371 \times 10^{-5}$. Cal decidir també si es vol mantenir el mètode
"per bits descartats" (aleshores cal explicar per què no dona el resultat correcte tal com estava
plantejat) o canviar-lo pel mètode directe (valor arrodonit − valor exacte), que és més senzill i
coincideix amb la definició donada a `@sec-error-representacio`.

**Impacte:** `PS_T5.qmd` no reutilitza aquest valor, no hi ha propagació de l'error a altres fitxers.

---

## B. Inconsistències detectades — proposta de correcció sistemàtica

### B1. 🟡 `TODO.md` — recompte de callouts `.callout-caution` amb/sense títol desactualitzat

`TODO.md` (§Decisions obertes) indica que T5 té **4/7** callouts `.callout-caution` amb títol. El
recompte real sobre el `T5.qmd` actual és **6/7** (només `#cau-cardinalitat-codificacions` no en té).
Sembla que el recompte es va fer abans d'алguna revisió posterior, o hi ha hagut canvis des
d'aleshores. Proposo actualitzar la xifra a `TODO.md` (afecta la decisió pendent sobre unificació de
criteri, ja que canvia el nombre de callouts a retocar en cada branca de la decisió).

### B2. 🟡 Notació de la mantissa binària: coma catalana (`$1{,}...$`) a T5.qmd vs. punt (`1.xxx`) dins de blocs `.default` a PS_T5.qmd

A `T5.qmd` (teoria), la mantissa binària sempre s'expressa en LaTeX math amb coma catalana:
`$1{,}1111\ldots$`. A `PS_T5.qmd`, dins dels blocs `` ```{.default} `` (traces de càlcul pas a pas),
s'usa punt: `1.1111010110...`. Com que és dins de blocs de codi, no infringeix estrictament la regla
de puntuació (que aplica al cos del text), però crea una lectura visualment inconsistent entre teoria
i solucionari per representar el mateix concepte. **No sé si voleu:**
- (a) mantenir-ho així (criteri: dins de blocs `.default` el punt és notació de traça, no de prosa;
  és el mateix criteri que ja s'aplica a T4.qmd en les traces de multiplicador/divisor), o
- (b) unificar a coma catalana també dins dels blocs `.default` de PS_T5 per coherència visual amb
  T5.qmd.

És una decisió d'estil, no un error. Ho deixo com a pregunta oberta (§D).

### B3. 🟢 Confirmació de correccions ja aplicades (F3, D2, E1, B1-B3 de `T5_revisio_canvis.md`)

He verificat contra el `T5.qmd` que tinc que les correccions documentades a `T5_revisio_canvis.md`
com a "✔ Estat" estan efectivament aplicades:
- B1 (multiplicació `0xBEB60002`): ✔ confirmat, valor recalculat i correcte.
- B2/B3 (reposicionament d'errors a codificació/suma): ✔ el text actual no conté els errors descrits.
- D2 (underflow → subdesbordament): ✔ aplicat consistentment.
- E1 (`{.C}` → `{.c}`): ✔ ambdós blocs en minúscula.
- F3 (extracció de taules RV32F a `11_riscv/`): ✔ els 6 fitxers existeixen i tenen el contingut
  correcte; a més, **`05_riscv.qmd` ja no és un "stub"** com deia la nota de `T5_revisio_canvis.md`:
  ja inclou tota la secció F (registres, `fcsr`, ISA) amb els mateixos includes. Sembla que
  `05_riscv.qmd` s'ha desenvolupat en un xat posterior a la redacció d'aquell document.

No calen accions per a aquest punt, és només confirmació.

---

## C. Verificació tècnica — resultat (tot correcte tret d'A1)

He recalculat numèricament (Python, `struct`/`Decimal`, i validació creuada amb `numpy.float16` per
als exercicis en format *half*) tots els càlculs binaris i hexadecimals de:

- **T5.qmd**: exemple de codificació (`0xC480B5C3` ✔, error ✘ vegeu A1), descodificació
  (`4136,15625` ✔), suma IEEE-754 (`0xC0500005` ✔), multiplicació IEEE-754 (`0xBEB60002` ✔, ja
  corregit respecte de la versió anterior), divisió IEEE-754 (`0x402AAAAB` ✔).
- **PS_T5.qmd**: interpretació de bits (natural, Ca2, IEEE-754, instrucció `sub t0,t1,t2` /
  `addi a0,s0,-100` — tots ✔ verificats bit a bit), rang IEEE-754 (`0x7F7FFFFF`, `0x00800000`,
  `0x00000001` — tots ✔), simple/doble precisió d'$A=-1609{,}5$ i $B=-938{,}8125$ (`0xC4C93000`,
  `0xC099260000000000`, `0xC46AB400`, `0xC08D568000000000` — tots ✔), suma `ft2+ft4` (`0x41820000`,
  16,25 ✔), mida del BA de `variancia` (420 bytes ✔), no-associativitat en *half* precision
  ($(A+B)+C=1$, $A+(B+C)=0$ — ✔ confirmat també amb `numpy.float16` independentment del càlcul manual
  del document).

**Cap altre error numèric detectat.**

---

## D. Decisions preses (actualitzat)

1. **A1 (error de representació)**: ✅ **aplicat** (Fable). Nou pas g) amb el mètode directe: desfer
   la normalització (coma 10 posicions a la dreta), constatar que la part entera (1029) no canvia,
   i calcular la diferència de parts fraccionàries: $5571/8192 - 0{,}68 = 0{,}44/8192 =
   5{,}37109375\times10^{-5} \approx 5{,}371\times10^{-5}$ (exacte, verificat per doble via:
   `Decimal` i `struct`). Estructura paral·lela als passos c)–e) de `#tip-ieee754-decodificacio`.

   *Diagnòstic refinat de l'error original* (corregeix el diagnòstic provisional de la fase Sonnet
   d'aquest mateix document): el pas g) antic no comparava «arrodonit vs. truncat», sinó que feia la
   resta binària «arrodonit − exacte» amb la cua de l'exacte tallada al bit 28 i amb l'acarreig mal
   resolt: donava $0{,}\ldots1111\ldots$ ($\approx 1{,}111_2\times2^{-15}$) on la resta correcta dona
   $0{,}\ldots1110\,0001\ldots$ ($\approx 1{,}1100\,001_2\times2^{-15}$). D'aquí el $5{,}722$ en lloc
   de $5{,}371$. La conclusió (valor erroni) no varia.

2. **B2 (notació punt vs. coma dins de blocs `.default`)**: ✅ **decidit mantenir el criteri actual**
   (punt dins de traça = notació tècnica, no de prosa, coherent amb T4.qmd). Cap canvi necessari.

3. **Cobertura de PS_T5.qmd**: ✅ **procedent en aquest xat**. Anàlisi completada (vegeu §F); pendent
   de la decisió de l'usuari sobre quines solucions afegir.

4. **Harmonització notacional RV32I↔RV32F**: ✅ **resolt**. Criteri acordat: `\leftarrow`
   (assignació) + `offset` sencer (no abreujat) arreu. Abast decidit:
   - **RV32F** (7 fitxers `11_riscv/RV32F_*.qmd`, dins l'abast d'aquest xat): delegat a **Claude
     Code** mitjançant prompt dedicat (`prompt_claude_code_harmonitzacio_rv32f.md`, lliurat a
     l'usuari). No es toca directament en aquest xat de revisió web.
   - **RV32I** (8 fitxers, ~27 ocurrències, usats des de T2/T3/T4/T9): **fora d'abast** d'aquest xat;
     el prompt de Claude Code instrueix afegir-ho com a nova entrada a `TODO.md` (secció global, no
     T5) per tractar-ho en un xat de revisió propi d'aquells temes.

5. **P7 (ordre taula codificacions especials)**: ✅ **aplicat**. S'ha permutat l'ordre de les
   subseccions a `T5.qmd`: abans Zero→Infinit→NaN→Denormals, ara **Zero→Infinit→Denormals→NaN**,
   coincidint amb l'ordre de la taula `#imp-ieee754-codificacions-especials`
   (Zero/Denormal/Normalitzat/Infinit/NaN). Cap referència creuada (`@sec-`) apuntava a aquestes
   subseccions, per la qual cosa el canvi és segur. TODO eliminat de `TODO.md`.

   **`#cau-underflow` → `#cau-subdesbordament`**: ✅ **decidit no fer el canvi**. Etiqueta interna es
   manté com està. Tasca eliminada de `TODO.md` i d'aquest document.

6. **Terminologia "mantissa" vs. "significand"** (tema addicional plantejat per l'usuari): investigat
   i **descartat l'ús de "significand"**. Cap font normativa catalana (Termcat, Viquipèdia) reflecteix
   la distinció interna a l'anglès tècnic (IEEE-754 usa formalment *significand*; Knuth criticava
   "mantissa" per ambigüitat amb el sentit logarítmic clàssic). Termcat només té fitxa per a
   "mantissa" (àmbit Matemàtiques); la Viquipèdia catalana sobre coma flotant usa "mantissa" com a
   terme principal. **Nota afegida a `07_contrib.qmd §T1 i T5`** documentant la decisió per a
   referència futura.

## D'. Fitxers de treball eliminats

- `T5_revisio_canvis.md` i `T5_figures_integracio.md`: ✅ eliminats (contingut ja incorporat/
  verificat a `T5.qmd`, ja no aporten informació útil).

---

## E. Fora d'abast d'aquest xat (necessito fitxers o decisions externes)

- **F1 (figures pendents)**: disposició S|E|F, recta numèrica amb denormals, esquema d'arrodoniment
  GRS — totes tres requereixen LO Draw de Roger, tal com ja indica `TODO.md`. No action item per a
  mi ara.
- **F2 (`RV32I_registres_coma_flotant.qmd` divergent)**: marcat com a pendent a
  `T5_revisio_canvis.md`; **en revisar-lo ara, el contingut de l'include ja coincideix exactament
  amb la taula usada a T5.qmd** (mateixa alineació, negretes i verbositat). Sembla que aquest punt ja
  està resolt des de la redacció d'aquell document; ho confirmo com a check, no com a tasca.
- **Taules de camps `fcsr`** (`frm`/`fflags` com a includes `11_riscv/` o inline): decisió de disseny
  pendent, oberta a `T5_revisio_canvis.md`. Demano la vostra decisió si voleu que l'apliqui ara.

---

## F. D3 — Anàlisi de cobertura i idoneïtat de PS_T5.qmd (Fable)

**Base empírica**: caracterització numèrica (Python: `struct`, `Decimal`, `numpy.float16`) de TOTS els
exercicis, resolts i no resolts, per determinar quins produeixen arrodoniment real, quins són
trivials i quins exhibeixen fenòmens especials (∞, NaN).

### F.1 Estat: 9 solucions / 22 exercicis (41%)

| Secció PE | Exercicis | Resolts |
| :--- | :---: | :---: |
| Representació IEEE 754 | 8 | 3 (interpretacio, rang, doble-precisio) |
| Suma i multiplicació | 12 | 5 (assemblador-cf, rv32f-memoria, rv32f-conversio, suma-simple, variancia) |
| No associativitat | 2 | 1 (assoc-suma, apartat a) |

### F.2 Llacunes detectades al conjunt resolt (per ordre de gravetat)

1. **Cap solució mostra una decisió d'arrodoniment GRS que canviï el resultat** (sumar 1 ULP):
   `sol-p6-ops-suma-simple` té $G=R=S=0$ (exacta); `sol-p6-assoc-suma` té $G=0$ (truncar);
   `sol-p6-ieee-doble-precisio` té $\varepsilon=0$ en tots dos valors. La teoria en té tres exemples
   (suma, mult, divisió), però el paper del PS («detall pas a pas») és precisament la pràctica
   guiada, i no n'hi ha cap.
2. **Cap solució de codificació amb error de representació no nul** (els dos valors de
   doble-precisio són exactes). El buit natural el cobreix `exr-p6-ieee-decimal-a-hex` apartat b)
   $44{,}4$ (únic apartat amb error: $\varepsilon = 1{,}526\times10^{-6}$; a, c, d, e són exactes).
3. **Cap multiplicació resolta** (ni divisió). Nota: `exr-p6-ops-multiplicacio` (simple precisió) és
   trivial —$32{,}0\times0{,}0625$, mantisses $1{,}0\times1{,}0$, només suma d'exponents—; en canvi
   `exr-p6-ops-half-multiplicacio` té arrodoniment real als dos apartats (a: err $=0{,}0143$;
   b: err $=2{,}625$, bo per discutir «precisió del resultat»).
4. **Cap solució exhibeix ∞/NaN en aritmètica**: `exr-p6-assoc-distributiva` b) és una joia
   pedagògica no explotada: $A{\cdot}B \to +\infty$ (sobreeiximent), $A{\cdot}C \to -\infty$,
   $AB+AC = \infty-\infty = \text{NaN}$, mentre que $A(B+C) = -59360$ representable. L'apartat a)
   mostra que la distributivitat *pot* complir-se. Únic exercici que lliga amb
   `@sec-codificacio-infinit`/`@sec-codificacio-nan`.
5. **Cap solució toca el reconeixement de denormals**: `exr-p6-ieee-tipus` (taula de classificació
   NRM/DNRM/0/INF/NAN) seria la clau de correcció barata que ho cobreix.

### F.3 Caracterització dels exercicis no resolts (dades)

| Exercici | Fenomen | Valor pedagògic marginal si es resol |
| :--- | :--- | :--- |
| `ieee-hex-a-decimal` | 4 descodificacions | Baix (cobert per interpretacio-c i teoria) |
| `ieee-tipus` | classificació, denormals | Mitjà (única cobertura de denormals; barat) |
| `ieee-decimal-a-hex` | b) únic amb error | **Alt** (llacuna 2; habilitat nuclear del tema) |
| `ieee-half-a` / `half-b` | conversions half | Baix (tècnica mostrada a assoc-suma) |
| `ops-suma-simple2` | **exacta** (sense GRS!) | Baix (idèntica en tot a suma-simple ja resolta) |
| `ops-multiplicacio` | **trivial** (mantisses 1,0) | Baix |
| `ops-half-suma` | a i b amb arrodoniment | Mitjà (GRS en suma; tècnica parcial a assoc-suma) |
| `ops-half-multiplicacio` | a i b amb arrodoniment | **Alt** (llacunes 1+3: renormalització + GRS) |
| `ops-half-divisio` | a i b **exactes** | Baix (sense arrodoniment; divisió amb GRS ja a teoria) |
| `ops-absdif` | trampa flt.s en funció completa | Mitjà (complementa variancia: fulla vs no-fulla) |
| `ops-half-assemblador` | FP per programari (RV32I) | Especial: llarg i difícil; segons criteris PS |
| `assoc-distributiva` | b) amb ∞/NaN | **Alt** (llacuna 4; fenomen únic) |

### F.4 Proposta prioritzada de noves solucions

- **P1 (alta)**: `sol-p6-ieee-decimal-a-hex` — els 5 apartats (4 ràpids exactes + b amb derivació
  completa d'arrodoniment i error).
- **P2 (alta)**: `sol-p6-ops-half-multiplicacio` — els 2 apartats (renormalització + GRS real;
  b amb discussió de la precisió).
- **P3 (mitjana-alta)**: `sol-p6-assoc-distributiva` — els 2 apartats (a: es compleix; b: ∞/NaN).
- **P4 (mitjana)**: `sol-p6-ieee-tipus` — taula clau de correcció (denormals).
- **P5 (mitjana)**: `sol-p6-ops-absdif` — funció fulla amb la trampa `flt.s`.
- **No prioritzats**: la resta (vegeu F.3); en particular `half-assemblador` es deixa a criteri de
  `PS_criteris.qmd`.

### F.5 Observacions laterals sobre PE_T5 (sense proposta de canvi, només constatació)

- Els dos exercicis de `fadd.s` en simple precisió (suma-simple i suma-simple2) són exactes (sense
  GRS), i el de `fmul.s` és trivial. Sembla un disseny deliberat (simple precisió per a la mecànica
  de l'algorisme; *half* per a la pràctica d'arrodoniment), però es fa constar per si es vol que
  algun exercici de simple precisió exerciti l'arrodoniment.
- `PS_criteris.qmd` no s'ha aportat en aquest xat: les prioritats F.4 s'han d'acarar amb els
  criteris oficials de selecció (dificultat, representativitat) abans d'escriure res.

---

## G. D3 — Execució (Fable) i troballes addicionals

### G.1 Solucions afegides a PS_T5.qmd (5 noves; total 14/22)

Selecció final (criteri pedagògic prioritari sobre la ràtio, per decisió de l'usuari):

| Solució nova | Dif. | Aporta |
| :--- | :---: | :--- |
| `sol-p6-ieee-tipus` | 1 | Classificació NRM/DNRM/0/∞/NaN; única cobertura de reconeixement de denormals |
| `sol-p6-ieee-decimal-a-hex` | 3 | Codificació amb error de representació real (apartat b, 44,4); mètode d'error idèntic al nou pas g) de T5 |
| `sol-p6-ops-half-suma` | 3 | a) absorció amb G=0 i R=S=1 (mostra que R=S=1 no basta per arrodonir); b) arrodoniment +1 ULP genuí (satisfà la intenció «amb arrodoniment» del criteri) |
| `sol-p6-ops-half-multiplicacio` | 4 | Producte de mantisses, renormalització, GRS; b) toca el límit e=15 i il·lustra error absolut gran / relatiu acotat |
| `sol-p6-assoc-distributiva` | 5 | a) coincidència fortuïta amb 4 arrodoniments (inclòs l'**únic empat «al parell» del problemari**, ½ ULP exacte a A×B); b) sobreeiximent → ±∞ → NaN |

Es descarta `absdif` (trampa `flt.s` ja coberta 3 vegades) i la resta (vegeu §F.3).
**Tots els valors verificats** amb simulador exacte (`Fraction`) + validació creuada `numpy.float16`,
i totes les línies de codificació «S | E | F = 0x…» del fitxer reverificades per script.

### G.2 `PS_criteris.qmd` actualitzat

- 5 files noves a la taula T5 (dificultats 1/3/3/4/5).
- Temari de `suma-simple` corregit: «amb arrodoniment» → «renormalització per transport, cas exacte (G=R=S=0)»; la suma amb arrodoniment passa a la fila de `half-suma` (decisió de l'usuari).
- Fila `assoc-suma` precisada: «(apartat a)» (la solució existent només cobreix l'apartat a).

### G.3 🔴 Errata preexistent trobada i corregida a `sol-p6-ops-suma-simple`

La verificació automàtica de codificacions ha detectat que el Pas 4 escrivia
$F = 000\,0001\,0000\ldots$ quan la mantissa $1{,}0000010\ldots$ dona $F = 000\,0010\,0000\ldots$
(un bit desplaçat). El resultat hex `0x41820000` era correcte; només la cadena de bits era errònia.
**Corregit** (línies 567 i 569).

### G.4 🔴 Troballa: 3 errates a `exr-p6-ieee-half-a` (PE_T5.qmd) — DECISIÓ PENDENT

`half-a`/`half-b` són les conversions els resultats de les quals són els operands dels exercicis
aritmètics (a→half-suma a; b→half-suma b; c→half-mult b; d→assoc-suma a; half-b: a→assoc-suma b;
b→assoc-distributiva a; c→assoc-distributiva b). `half-b` és 9/9 consistent ✓; `half-a` té tres
errates, totes al valor B (verificat amb codificació exacta):

| Apartat | PE diu | Hauria de ser | Causa aparent |
| :--- | :--- | :--- | :--- |
| a) B | $-3{,}90625$ (=0xC3D0) | $-3{,}90625\times10^{-1}$ (=0xB640) | exponent ×10⁻¹ perdut |
| b) B | $6{,}391601562\times10^{-1}$ (truncat, **no representable exactament**) | $6{,}3916015625\times10^{-1}$ (=0x391D) | últim dígit 5 perdut |
| c) B | $5{,}796875\times10^1$ (=0x533F) | $5{,}79375\times10^1$ (=0x533E) | transcripció (1 ULP) |

**Recomanació**: corregir els tres decimals de `half-a` (els hex dels exercicis aritmètics són
canònics i ja tenen solucions escrites contra ells; l'alternativa —canviar els hex— tocaria dos
exercicis i les seves traces). ✅ **Resolt**: usuari confirma; els 3 decimals corregits a
`PE_T5.qmd` i reverificats (els 9 valors de half-a codifiquen exactament als hex canònics).
