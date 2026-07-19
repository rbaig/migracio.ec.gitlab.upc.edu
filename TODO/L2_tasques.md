# L2_tasques.md — Revisió interna `L2.qmd` (Fase B, 2026-07-19)

Revisió profunda de `04_laboratori/L2.qmd` (Sessió 2: Assemblador RISC-V i tipus bàsics de dades).
Fitxers de context llegits: `CLAUDE.md`, `13_contrib.qmd`, `TODO/TODO.md`, `A2.qmd` (destí de les 19 referències creuades), `L1.qmd` (estil establert).

---

## A. Verificació tècnica — resultats

Tota la verificació numèrica s'ha fet **executant els programes a RARS 1.6 real** (mode línia de comandes, OpenJDK 21), no només sobre paper.

| # | Contingut | Resultat |
| :--- | :--- | :--- |
| A1 | `s2_1_1`: representacions (−5→`0xFB`, −344→`0xFEA8`, −3 dword→`FD FF…FF`, `0xA0`, 5799→`0x16A7`, −1→`0xFFFF`) | ✅ Correctes |
| A2 | `s2_1_2`, solució GCC/MARS (`.dword` alineat a 8): adreces, padding i taula byte a byte | ✅ Correcta i internament consistent |
| A3 | `s2_1_2`, solució RARS (`.dword` alineat a 4): **verificada empíricament** — el dump de RARS 1.6 és exactament `fea800fb fffffffd ffffffff 000000a0 000016a7 0000ffff 0000…` | ✅ Coincideix byte a byte amb la taula i amb el bolcat de `s2_1_3` |
| A4 | `#cau-rars-vista-memoria`: 8 words/fila, files alineades a `0x20`, byte de major adreça a l'esquerra del word | ✅ Correcte (comportament observat de la finestra *Data Segment*) |
| A5 | `s2_1_3`: taula de solució vs. dump | ✅ Consistent (usa el comportament RARS, com ha de ser al laboratori) |
| A6 | `s2_2_1`: `dada` half @`0x10010000`, `pdada` word @`0x10010004` (2 B padding); dump `00000003`, `10010000` | ✅ Adreces, padding i les 5 expressions correctes |
| A7 | `s2_2_2`: executat — `s0 = 0xC` (12), `A = {3, 12, 7}`, `punter = 0x10010008` (=&A[2]) | ✅ Traça i comentaris correctes |
| A8 | `s2_3_1`: fragment executat amb `s2 = 7` → `s1 = 2` (= `vec[7]`) | ✅ Correcte |
| A9 | `s2_3_2`: executat — `fib = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34}` en memòria | ✅ Correcte |
| A10 | `s2_4_1`: executat — memòria final `0x36383931`, `0x00000035` (= `"19865\0"`); `vec` a `0x10010008` (2 B padding rere `cadena`) | ✅ Correcte; encaixa perfectament amb `@cau-rars-vista-memoria` |
| A11 | `la rd, etiqueta+offset` a RARS 1.6 | ✅ Rebutjada («Too many or incorrectly formatted operands»), tal com afirma `@imp-ec-la-offset` |
| A12 | Fitxer només `.data` (sense `.text`): RARS l'**assembla sense error**; si s'executa, acaba amb «dropped off the bottom» | ℹ️ Vegeu decisió D2 |
| A13 | Taula d'alineacions de `@nte-restricicons-alineacio` (char 1 / short 2 / int 4 / long long 8) contra l'ABI `ilp32` del psABI de RISC-V International | ✅ Correcta (l'alineació a 16 de la pila és una restricció independent, ja tractada a T3) |
| A14 | Totes les 19 referències creuades de L2 resolen (totes a `A2.qmd`) | ✅ Cap referència trencada |

**Cap error de càlcul detectat.** El TODO de `#sol-mapa-memoria` (`.dword` GCC/MARS vs. RARS) **es manté intacte** per a la revisió externa (decisió teva del 2026-07-19); la verificació A3 confirma que el dump empíric hi coincideix.

---

## B. Accions d'execució directa (Fase C — no requereixen aprovació)

### B1. Redactar la secció «Pseudoinstruccions `la` i `li`» (decisió teva del 2026-07-19)

Substituir el cos «TODO» (i pluralitzar el títol) pel contingut següent, ja verificat (A11):

```markdown
## Pseudoinstruccions `la` i `li`

Tots els programes d'aquesta sessió operen amb variables globals emmagatzemades
en memòria. Com que l'únic mode d'adreçament per accedir a memòria en RV32I és
el mode base + desplaçament (@sec-operands-base-desplacament), abans de cada
accés cal haver carregat l'adreça de la variable en un registre. Per fer-ho
s'usen dues pseudoinstruccions (@sec-pseudoinstruccions):

- **`la rd, etiqueta`** (***load address***, @nte-pseudoinstruccio-la): carrega
  a `rd` l'**adreça** de la variable `etiqueta`. Per exemple, `la t0, vec`
  deixa a `t0` l'adreça de `vec`.
- **`li rd, valor`** (***load immediate***, @nte-pseudoinstruccio-li): carrega
  a `rd` el **valor immediat** indicat, de fins a 32 bits. Per exemple,
  `li t1, 10`.

RARS les expandeix en una o dues instruccions reals segons el cas, tal com
s'ha vist a la sessió anterior (@exr-rars-pseudoinstruccio).

::: {#cau-rars-la-offset .callout-caution}
**RARS no suporta** la sintaxi `la rd, etiqueta+offset` admesa a la teoria i
als exàmens (@imp-ec-la-offset): al laboratori cal substituir-la per la
parella `la` + `addi`.

```{.s filename="RV32I"}
        la      t0, vec         # t0 = @vec
        addi    t0, t0, 8       # t0 = @vec + 8 (@vec[2])
```
:::
```

Un cop redactada, esborrar l'entrada corresponent de `TODO/TODO.md §Laboratori`.

### B2. Correccions de taules

- `#exr-mapa-memoria` (taula de variables, i la seva còpia dins la plantilla `.markdown`): les files tenen **5 cel·les per a 6 columnes** — afegir la cel·la final buida a cada fila.
- Unificar les capçaleres de la taula de variables de l'enunciat amb les de la solució: `Mida [B]`, `Alineació [B]`, `*Padding*` → `Padding [B]` (vegeu B4 per a la cursiva).
- `#exr-rars-vista-memoria` i `#sol-rars-vista-memoria` (i la plantilla `.markdown`): la fila separadora té **6 especificadors per a 7 columnes** — afegir-n'hi un i centrar la columna `+3` com les altres.
- Unificar les capçaleres de columna de byte: actualment coexisteixen `` `+0` `` i ``@`+1` ``/``@`+2` ``/``@`+3` `` (i el callout usa ``@`+0` ``…). Unificar-les totes a `` `+0` ``–`` `+3` `` **sense** `@` (coincideix amb l'estil de columnes del propi RARS, «Value (+0)»).

### B3. Format d'adreces: `0x1001 0000` → `0x10010000`

Les ~64 adreces de les taules byte a byte usen separador cada 4 nibbles, en contra de la decisió explícita de `13_contrib.qmd §T2 i T3` («Format d'adreces de memòria: sense espais»). L2 és **l'únic fitxer del repositori** amb aquest format. Substitució mecànica.

### B4. Cursives d'anglicisme en aparicions posteriors

Primera aparició correcta a la introducció («**bytes de farciment** (*padding*)»). Les posteriors han d'anar sense cursiva (`13_contrib.qmd §Anglicismes`): capçaleres `*Padding*`, «bytes de *padding*» (enunciats i solucions), «`aa`, *padding*, `bb`», etc.

### B5. Harmonització terminològica i lingüística

- «el byte de **menor** pes s'emmagatzema…» (intro §Representació) → «de **menys** pes» (forma d'A2 §endianness i de L1, que L2 recapitula). També a `s2_4_1`: «ordenats de menor a major pes» → «de menys a més pes», «de major a menor pes» → «de més a menys pes».
- «per garantir les restriccions d'alineació» → «per respectar les restriccions…» (mateixa frase d'A2 §1081).
- §Cadenes: «n'hi ha prou de recórrer-**lo**» → «recórrer-**la**» (antecedent: *la cadena*).
- §Cadenes: la referència del concepte ASCII apunta al callout de directives; canviar «codificació ASCII de 7 bits (@nte-directives-ascii-asciz-string)» → «(@sec-codificacio-caracters)».
- `s2_4_1`: «del nombre `19865`» → «del nombre 19865» (els nombres van en text pla, no en backticks); reformular «l'emmagatzema a la cadena `cadena`, ordenat de major a menor pes per poder-lo imprimir correctament» → «i l'emmagatzema a la cadena `cadena`; els caràcters queden ordenats de més a menys pes per poder imprimir el nombre correctament» (antecedent ambigu de «-lo»).
- Nota de `s2_4_1`: «Consulteu el @cau-rars-vista-memoria per interpretar…» renderitza «el Essencial 2.x»; reformular en parentètic, l'estil de tot el corpus: «Per interpretar el contingut de `cadena` a la vista de memòria de RARS, vegeu @cau-rars-vista-memoria.»

### B6. Lectura prèvia — completar files

- «Punters: declaració, `&`, `*`, aritmètica»: hi falta la referència a l'aritmètica → afegir `@sec-aritmetica-punters` (usada a `s2_2_2`).
- «Pseudoinstrucció `la`» → «Pseudoinstruccions `la` i `li` | @nte-pseudoinstruccio-la, @nte-pseudoinstruccio-li» (`li` s'usa a totes les solucions).
- «Caràcters i cadenes de caràcters | @nte-directives-ascii-asciz-string» → referenciar la secció sencera: `@sec-caracters-cadenes` (el callout de directives n'és un subconjunt).

### B7. Fórmules d'adreça — harmonitzar amb la notació canònica de la teoria

- Intro §Vectors: `$$@\texttt{v[i]} = @\texttt{v} + i \times \texttt{mida\_element}$$` → forma canònica d'`@eq-acces-aleatori-vector` (A2): `$$@\texttt{v[i]} = @\texttt{v[0]} + i \cdot T$$`, citant l'equació («…es calcula segons l'@eq-acces-aleatori-vector:»), amb «on $T$ és la mida en bytes de cada element».
- `#sol-vectors-declaracio`: `@\texttt{vec} + i \times 4` → `@\texttt{vec[0]} + i \cdot 4`, afegint l'equivalència «(o, equivalentment, $@\texttt{vec} + i \cdot 4$, ja que `vec` = `&vec[0]`, @sec-punters-vectors)» — així es valida també la resposta que l'estudiant escriurà més naturalment.

### B8. Afegir callouts «Comprovació pràctica» (convenció de laboratori; L2 no en té cap)

Dins el `{#sol-…}` corresponent, amb els valors **ja verificats a RARS** (secció A):

- `#sol-punters-valors`: word a `0x10010000` = `0x00000003`; word a `0x10010004` = `0x10010000`.
- `#sol-punters-codi`: en acabar, `s0 = 0x0000000C`; word a `0x10010004` (`A[1]`) = `0x0000000C`; `punter` (`0x1001000C`) = `0x10010008`.
- `#sol-vectors-declaracio`: provar el fragment amb `li s2, 7` davant → `s1 = 0x00000002` (= `vec[7]`).
- `#sol-vectors-fibonacci`: en acabar, el segment de dades mostra `0, 1, 1, 2, 3, 5, 8, 0xD, 0x15, 0x22`.
- `#sol-strings-ascii`: en acabar, word a `0x10010000` = `0x36383931` i word a `0x10010004` = `0x00000035` — exemple directe de @cau-rars-vista-memoria («19865» llegit per bytes).

### B9. Amplada dels valors a `#sol-punters-valors`

`dada` i `*pdada` són `short` (2 bytes): mostrar `0x0003` en lloc de `0x00000003` (les adreces es mantenen en 8 dígits), afegint a l'explicació que en carregar-lo amb `lh` el registre mostrarà `0x00000003` (extensió de signe a 32 bits).

### B10. Slug amb errata: `#nte-restricicons-alineacio` → `#nte-restriccions-alineacio`

Definició a `A2.qmd` + única referència a `L2.qmd` (verificat: cap altre fitxer l'usa). Canvi mecànic de 2 fitxers, dins el mandat d'harmonització pre-revisió-externa de `CLAUDE.md`.

### B11. Actualitzar `TODO/TODO.md` (verificacions fetes en aquest xat)

- §Neteja A2 (`sec-opt-acces-sequencial` duplicat): **verificat 2026-07-19 amb el repositori complet** — única definició a `A4.qmd` L463; cap duplicat enlloc. Marcar com a resolta (el warning devia ser antic).
- §Neteja A4 (`@sec-ecall`, `@sec-operands-memoria`, `@imp-ec-alineacio-pila`): **verificat 2026-07-19 amb el repositori complet** — cap ocurrència en cap `.qmd`. Marcar com a resoltes.
- §Laboratori: eliminar l'entrada de L2 §`la`/`li` quan B1 estigui aplicada.

---

## C. Decisions que et corresponen (es presentaran al final de la Fase C)

### D1. Renumeració dels lliuraments (conseqüència de mantenir la secció `la`/`li`) — **recomanada**

Amb la secció «Pseudoinstruccions `la` i `li`» com a §2.2, les seccions passen a: 2.1 Representació, 2.2 Pseudoinstruccions, 2.3 Punters, 2.4 Vectors, 2.5 Cadenes. La convenció `s<N>_<S>_<E>` (S = secció) obliga a renumerar: `s2_2_*` → `s2_3_*`, `s2_3_*` → `s2_4_*`, `s2_4_1` → `s2_5_1` (taula de Lliuraments, títols dels `{#exr-}`, atributs `filename=` i plantilles).

- **Opció a (recomanada)**: renumerar. Coherent amb el precedent de L1 (§1.1 sense exercicis, fitxers segueixen el número real de secció).
- **Opció b**: fer la secció `{.unnumbered}` — evita tocar noms de fitxers, però trenca el patró (les no numerades són només Lliuraments/Lectura prèvia, per un *dirty hack* de PDF).

*Si em confirmes l'opció a en reprendre, l'executo dins la Fase C; si no, deixo la numeració intacta.*

### D2. Esquelet a `s2_1_1.s`

`#cau-format-codi-esquelet` (L1) declara format i esquelet **obligatoris en tots els programes lliurats**, però `s2_1_1.s` és només `.data`. Verificat (A12): RARS l'assembla igualment (n'hi ha prou per a `s2_1_3`), però executat «cau pel final».

- **Opció a (recomanada)**: afegir l'esquelet mínim a la solució (`.globl _start` + `.text` + `_start:` + sortida 93) i una frase a l'enunciat («Afegiu-hi l'esquelet mínim del programa»). Cost nul, coherència total.
- **Opció b**: mantenir només `.data` i afegir una nota d'excepció explícita.

### D3. Plantilles `.markdown` (recordatori)

L2 és l'únic laboratori amb blocs plantilla `{.markdown filename="…"}`; la decisió «posar-ne a tots o treure'ls de L2» ja figura a `TODO/TODO.md §Decisions obertes`. **Cap acció en aquest xat** (les plantilles es corregeixen, B2, però no s'eliminen).

---

## D. Observacions transversals (fora de l'abast de L2 — per als xats corresponents)

- **«menys pes» vs. «menor pes»**: conviuen al corpus (A2/A4/A7/L1: «menys»; A3/A5/A8: «menor»). Candidata a decisió de `13_contrib.qmd §Substitucions` i substitució global posterior.
- **`void main()` (laboratoris, A2, A3) vs. `int main()` (E2/E3/E4/E7, S3/S4)**: inconsistència transversal de criteri de codi C; encaixa amb el TODO obert «Criteris de codi C: completar».
- **L4 §Accés a elements**: la fórmula reproduïda diverge de la canònica d'A4 (`\texttt{@mat}` vs. `@\texttt{mat[0][0]}`; `NB` vs. `T`) — mateix patró que s'ha corregit aquí (B7); per al xat L4–L6.
- **L5**: usa la grafia «IEEE-754» amb guionet, contrària a la decisió «IEEE 754» de la revisió de T5 — per al xat L5.
- **«words»**: revisat i **mantingut** a L2 (i L1): terminologia RARS sancionada per `@imp-terminologia-c-vs-rars` («.word o word»).
