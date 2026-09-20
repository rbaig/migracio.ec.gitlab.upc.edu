# Recuperació de diffs — informe de la Passada 1

Fitxer **transitori**. S'esborra en tancar la feina de recuperació.

Col·lecció analitzada: `/home/roger/tmp/EC_RV_migracio_claude_clara/extrets/`
(70 fitxers, 14 subdirectoris = 14 xats).

Sessió A (grups 1 i 2) — data: 2026-09-20. Model: Opus 5.

---

## Passada 0 — resultats consolidats

### Patch `L2_revisio_interna/L2_revisio_faseC.patch`

No aplica amb `-p1` (paths asimètrics: `--- /tmp/L2.orig` vs `+++ 04_laboratori/L2.qmd`).

**Amb `-p0`:**

| Hunk | Estat | Volum |
| :--- | :--- | :--- |
| `04_laboratori/L2.qmd` | aplica net | +175 / −142 |
| `01_apunts/A2.qmd` | aplica net | +1 / −1 |
| `TODO/TODO.md` | **no aplica** | irrellevant: fitxer de REGISTRE, exclòs |

### Marcadors de verificació del grup 1 (reconfirmats 2026-09-20)

Tots quatre presents, doncs la base del grup 1 es manté vigent:

- `restricicons` a `04_laboratori/L2.qmd:33` i `01_apunts/A2.qmd:1085` ✔
- `zobacz` a `CLAUDE.md:79` ✔
- `bibliografia.qmd` a `13_contrib.qmd:404,601` ✔
- `gandula` absent de `04_laboratori/L3.qmd` ✔

### Control positiu (grup 2)

`L6_revisio_interna/L6.qmd` vs `04_laboratori/L6.qmd`: **idèntic byte a byte**.
La classificació no produeix falsos positius en aquest fitxer.

### Inventari de comparació (fitxers de CONTINGUT)

Idèntics (tancats, cap feina pendent): `A1`, `E1`, `S1`, `A3`(A3E3S3), `E3`, `S3`,
`RV32I_instruccions_comparacio`, `RV32I_instruccions_desplacament_bits_aritmetics`,
`RV32I_instruccions_salt_incondicional_indirecte`, `E4`, `S4`, `A2`(L4-3passades),
`L4`(L4-3passades), `A9`, `E9`, `RARS_syscall_registres`, `RV32I_csr_mip_mie_taula`,
`S9`, `Zicsr_instruccions_immediats`, `L5`(Revisio_final_L5), `12_sigles_simbols`
(EC_sigles_i_símbols_T7_T8), `A7`(L6), `L6`(L6), i els 3 SVG de T1 (hash idèntic).

Amb diferències: vegeu el detall per fitxer a sota i, per al grup 3, la secció
«Pendent — sessió B».

---

## Sessió A — veredictes

### 1. `L2_revisio_interna/` — GRUP 1

Premissa del grup 1 verificada de nou en aquesta sessió:

- `04_laboratori/L2.qmd`: darrer commit `c5d9416` (2026-07-11, refactor
  estructural). Cap canvi posterior. Base byte a byte confirmada.
- `01_apunts/A2.qmd`: darrer commit `3cae913` (2026-07-21, «L4 revisió interna
  pre passades finals»). **Matís respecte de la premissa**: sí que hi ha un
  commit del 21/07, però afegeix un callout nou (`#nte-rars-operands-literals`)
  a la línia ~448, zona disjunta de la línia 1085 que toca la Fase C. El hunk
  rellevant conserva la base intacta, i el patch hi aplica net. Premissa
  vàlida per al hunk.

**Prova de consistència interna del paquet**: tots els identificadors que el
text nou de L2 referencia existeixen ja a `A2.qmd` al repositori
(`sec-aritmetica-punters`, `sec-caracters-cadenes`, `nte-pseudoinstruccio-la`,
`nte-pseudoinstruccio-li`, `imp-ec-la-offset`, `eq-acces-aleatori-vector`,
`sec-codificacio-caracters`, `sec-punters-vectors`, `sec-pseudoinstruccions`,
`sec-operands-base-desplacament`), **excepte** `nte-restriccions-alineacio`,
que és precisament el que corregeix el hunk d'`A2.qmd`. L2 i A2 formen un
paquet atòmic: aplicar-ne només un deixaria referències trencades.

**Discriminador `git log -S`** (tot i ser grup 1, executat per prudència):

| Fragment | Resultat |
| :--- | :--- |
| `Pseudoinstruccions \`la\` i \`li\`` | cap commit — mai ha existit al repo |
| `Comprovació pràctica` | cap commit — mai ha existit al repo |
| `cau-rars-la-offset` | cap commit |
| `nte-restriccions-alineacio` (a A2) | cap commit — la grafia correcta mai hi ha estat |

Cap contingut de la Fase C ha existit mai al repositori: **no hi ha risc de
revertir feina posterior**.

#### `01_apunts/A2.qmd` — 1 hunk, categoria A

| # | Línia | Actual | Proposat |
| :--- | :--- | :--- | :--- |
| A2-1 | 1085 | `::: {#nte-restricicons-alineacio .callout-note}` | `::: {#nte-restriccions-alineacio .callout-note}` |

Errata tipogràfica a l'identificador. Arregla la referència `@nte-restriccions-alineacio`
que L2 (Fase C) farà servir. Sense aquest canvi, el hunk L2-1 deixaria una
referència trencada.

#### `04_laboratori/L2.qmd` — 317 línies, tot categoria A

Agrupació temàtica dels canvis (tots del mateix paquet de Fase C):

| # | Abast | Naturalesa | Criticitat |
| :--- | :--- | :--- | :--- |
| L2-1 | Taula de repàs, l. 33–39 | Correcció de 4 referències creuades: `restricicons`→`restriccions`; afegeix `@sec-aritmetica-punters`; `@nte-directives-ascii-asciz-string`→`@sec-caracters-cadenes`; «Pseudoinstrucció `la`»→«Pseudoinstruccions `la` i `li`» amb les dues refs | Alta (refs) |
| L2-2 | l. 45 | Redacció: «per garantir»→«per respectar» les restriccions; «byte de menor pes»→«de menys pes» (comparatiu correcte) | Baixa |
| L2-3 | Taules d'exercici i solució (l. 85–290) | Capçaleres amb unitats: `Mida`→`Mida [B]`, `Alineació`→`Alineació [B]`, `*Padding*`→`Padding [B]`; afegeix la 6a cel·la buida que faltava a les files de la taula d'exercici (la taula d'enunciat tenia 6 columnes i només 5 separadors per fila) | **Alta (taula mal formada)** |
| L2-4 | Totes les adreces hex del fitxer | `0x1001 0000` → `0x10010000` (elimina l'espai de separació, harmonitza amb la resta del corpus) | Mitjana (coherència) |
| L2-5 | `*Padding*` → `Padding` en prosa i taules | Deixa de tractar «padding» com a estrangerisme en cursiva de manera inconsistent | Baixa |
| L2-6 | l. 301, 323, 341 | Errata `@\`+1\`` → `\`+1\`` a capçaleres de taula (l'`@` hi era per error, Quarto ho interpretaria com a referència creuada); afegeix l'alineació `:---:` que faltava a la darrera columna | **Alta (sintaxi)** |
| L2-7 | §«Pseudoinstruccions `la` i `li`» (l. 356) | **Secció que al repositori és literalment «TODO»**: la Fase C hi aporta el cos redactat (2 vinyetes `la`/`li` + callout `#cau-rars-la-offset` sobre `la` amb desplaçament no suportat per RARS) | **Màxima (forat de contingut)** |
| L2-8 | Solució `sol-punters-valors` (l. 421–428) | **Correcció tècnica**: `dada` i `*pdada` són `short` (2 bytes); el valor era `0x00000003` (32 bits) i passa a `0x0003`, amb nota explicativa que `lh` l'estén en signe a `0x00000003` en carregar-lo | **Màxima (error tècnic)** |
| L2-9 | §Vectors (l. 502–512, 532) | Fórmula d'accés: `@v[i] = @v + i × mida_element` → `@vec[i] = @vec[0] + i · T`, alineada amb l'`@eq-acces-aleatori-vector` d'A2; nom de variable `v`→`vec`; nota d'equivalència amb `@vec` (ja que `vec` és `&vec[0]`) | Alta (coherència notacional amb A2) |
| L2-10 | §Cadenes (l. 636) | Ref. `@nte-directives-ascii-asciz-string`→`@sec-codificacio-caracters`; concordança «recórrer-lo»→«recórrer-la» (cadena, femení) | Mitjana |
| L2-11 | Enunciat `exr-strings-ascii` (l. 645) | Redacció: «el nombre `19865`» (codi)→«el nombre 19865» (no és codi); «de menor a major pes»→«de menys a més pes»; reformula la frase de l'ordre dels caràcters | Baixa |
| L2-12 | l. 662 | Redacció: «Consulteu el @cau-…»→«…vegeu @cau-…» (sense article davant de referència) | Baixa |
| L2-13 | 5 llocs (l. 496, 549, 627, 714 i solució de punters) | **Afegeix 5 callouts nous `Comprovació pràctica`** amb els valors concrets que l'alumne ha de veure a RARS en acabar cada exercici | Alta (valor pedagògic) |

**Total: 13 hunks temàtics, tots categoria A.** Cap categoria B, C ni D:
és un fitxer del grup 1 amb base intacta i cap contingut preexistent al repo.

**Observació**: `L2.qmd` no acaba amb salt de línia ni al repositori ni a
l'extret; el patch no ho canvia.

#### Evidència addicional: `TODO/L2_tasques.md` (ja al repositori)

És el registre Fase B d'aquell xat, i confirma la conclusió per una via
independent:

- La verificació numèrica es va fer **executant els programes a RARS 1.6
  real** (mode línia de comandes, OpenJDK 21), no sobre paper.
- Els valors del registre coincideixen exactament amb els dels 5 callouts
  «Comprovació pràctica» de L2-13: `s0 = 0xC` (A7), `s1 = 2` amb `s2 = 7`
  (A8), la sèrie de Fibonacci (A9), `0x36383931`/`0x00000035` (A10).
- L'entrada A11 confirma empíricament el contingut del callout
  `#cau-rars-la-offset`: RARS 1.6 rebutja `la rd, etiqueta+offset` amb
  «Too many or incorrectly formatted operands».
- Reconciliació del 2026-07-20 al capdamunt del fitxer: «`L2.qmd` **no l'ha
  modificat cap xat**», amb els tres marcadors (secció `la`/`li` en «TODO»,
  adreces amb espai, errata `restricicons`).

#### Comprovació ampliada del parell atòmic

`grep -rn 'restricicons'` a tot el repositori: només
`04_laboratori/L2.qmd:33` i `01_apunts/A2.qmd:1085` (a banda d'aquest informe
i de `TODO/L2_tasques.md`, que són registres). **Cap tercer fitxer** no
referencia l'identificador mal escrit, de manera que el commit 1 es limita al
parell.

### APLICAT — L2 i A2 tancats (2026-09-20)

Aplicat `L2_revisio_faseC.patch` amb `git apply -p0` (hunks de `L2.qmd` i
`A2.qmd`; el de `TODO/TODO.md` s'ha descartat per ser registre). Resultat
verificat **byte a byte idèntic** als fitxers extrets.

Repartit en tres commits segons l'agrupació acordada:

| Commit | Hash | Contingut |
| :--- | :--- | :--- |
| 1 | `1489c84` | L2-7, L2-8 i el hunk d'A2 (parell atòmic) |
| 2 | `254509b` | L2-3, L2-6, L2-1, L2-9, L2-13, L2-4, L2-10 |
| 3 | `12bac2c` | L2-2, L2-5, L2-11, L2-12 (redacció) |

#### Verificació post-aplicació

- `make render` complet: **cap warning**. Les úniques línies coincidents amb
  el patró de cerca són resums d'scripts de generació, tots amb `0 errors`
  (`gen-taules-auto`, `norm-font` ×2, `gen-regs`, `gen-crops`, `gen-dark`).
- **Cap referència creuada no resolta**: `grep -ro '?@[a-z-]*'` sobre tot
  `_book/` no retorna cap ocurrència.
- El parell atòmic ha quedat consistent: `nte-restriccions-alineacio` resol a
  `_book/04_laboratori/L2.html`.
- El callout nou `#cau-rars-la-offset` existeix a la sortida i queda numerat.
- Les altres referències noves de la Fase C resolen totes:
  `sec-aritmetica-punters`, `sec-caracters-cadenes`, `nte-pseudoinstruccio-li`,
  `eq-acces-aleatori-vector`, `sec-codificacio-caracters`, `imp-ec-la-offset`.

**Nota de procediment**: `git add -p` interactiu no és disponible en aquest
entorn. La partició en tres commits s'ha fet construint estadis intermedis
del fitxer i verificant, per diferència, que cada estadi conté exactament
els hunks previstos i que els commits posteriors no alteren els anteriors.

**Nota cronològica** (correcció de l'usuari): el commit `3cae913` d'`A2.qmd`
és del 21/07 i el xat de revisió de L2 és del 27/07. El commit és **anterior**
al xat, no posterior; per això la base coincidia. La prova de consistència
dels identificadors ho confirma independentment.

---

### 2. `L3_revisio_interna/` — GRUP 1

Premissa del grup 1 verificada:

- `04_laboratori/L3.qmd`: darrer commit `fe53cfc` (2026-07-13). Base intacta.
- `CLAUDE.md`: darrer commit `614f576` (2026-07-12). Base intacta. Marcador
  `zobacz` encara present.
- `13_contrib.qmd`: darrers commits `025b580` i `3debb1e` (2026-09-19, regla
  d'ordre de `_start`). **Divergit**, com estava previst.

**Cap hunk dels extrets toca l'ordre de `_start` a `L3.qmd`.** La Decisió 1
d'aquell xat no forma part dels canvis recuperats, tal com es va anticipar.

#### `CLAUDE.md` — 1 hunk, categoria A

| # | Línia | Actual | Proposat |
| :--- | :--- | :--- | :--- |
| CM-1 | 79 | `Tasques vives pendents: zobacz \`TODO.md\`.` | `... vegeu \`TODO.md\`.` |

`zobacz` és un mot polonès infiltrat al text català. `git log -S`: cap commit
n'ha tocat mai la forma correcta en aquest punt.

#### `04_laboratori/L3.qmd` — 10 hunks, tots categoria A

Discriminador `git log -S` aplicat als 12 fragments nous: **cap commit**. Cap
contingut ha existit mai al repositori.

Tots els identificadors nous que el text referencia existeixen a `A3.qmd`:
`nte-pseudoinstruccions-salt-condicional`, `nte-pseudoinstruccions-salt-zero`,
`sec-avaluacio-lazy-encadenats`.

| # | Línia | Naturalesa | Criticitat |
| :--- | :--- | :--- | :--- |
| L3-1 | 32 | Taula de repàs: la fila de salts condicionals no esmentava les pseudoinstruccions (`bgt`, `ble`, `beqz`); s'hi afegeixen amb les dues referències noves | Alta (cobertura) |
| L3-2 | 241 | **Correcció conceptual**: «cal preservar els registres segurs que continguin valors...» → «els *valors* generats abans d'una crida i usats després s'han d'assignar a registres segurs; la subrutina ha de desar i restaurar aquests registres i `ra`». Alinea amb A3 §`sec-determinacio-registres-segurs`, que parla de determinar **dades**, no registres; i separa la regla de `ra` (caller-saved) dels `s0`–`s11` | **Màxima (conceptual)** |
| L3-3 | 263 | Coherent amb L3-2: «quins registres necessiten ser segurs» → «quins valors cal assignar a registres segurs» | Alta |
| L3-4 | 565 | **Precisió tècnica** a l'Error 1 de `#sol-depuracio`: «salta a una adreça incorrecta i el programa falla» → descriu el comportament real (torna a la instrucció següent a `jal ra, g`, l'execució reprèn dins del bucle de `codifica` i el programa no acaba correctament). Verificat contra el codi del bloc: `ra` conté l'adreça de `sb a0, 0(s0)` | **Alta (rigor)** |
| L3-5 | 366 | `# update: vegeu @sol-update` → `vegeu la solució de s3_4_1.s`. La línia és **dins d'un bloc de codi** `.s`, on Quarto no resol les referències creuades: es renderitzaria literalment `@sol-update`, i a més és un comentari que l'alumne copia al seu fitxer | **Alta (ref. inoperant)** |
| L3-6 | 395 | Mateix cas: `← mateix patró que exr-compta-caracter` dins d'un bloc de codi → `mateix patró que s3_3_1.s` | Alta |
| L3-7 | 87 | «avaluació lazy» → «avaluació gandula (*lazy*)»; «del cos del `else`» → «de l'`else`» (apostrofació); afegeix `@sec-avaluacio-lazy-encadenats` | Mitjana (terminologia) |
| L3-8 | 333 | El «nexe» afirmava «exactament el mateix patró de recorregut amb punter», però el segon `for` de `moda` usa **índex explícit**, no punter. Es corregeix a «mateix patró de recorregut seqüencial caràcter a caràcter (ara amb índex explícit en lloc de punter)» | **Alta (error factual)** |
| L3-9 | 184, 200 | «dígits numèrics» → «dígits decimals»; «és el patró que reapareixerà» → «és un patró que reapareixerà, amb variacions» (coherent amb L3-8) | Mitjana |
| L3-10 | 44 | Redacció: «sense recórrer a operacions aritmètiques costoses» (afirmació de rendiment no justificada) → «permeten construir màscares i manipular bits individuals» | Baixa |

#### `13_contrib.qmd` — 6 hunks, classificació sencera

El parany funciona exactament com estava descrit. Discriminador per a tots:

| # | Hunk | `git log -S` | Categoria |
| :--- | :--- | :--- | :--- |
| C-1 | Elimina la regla **«`_start` ha de ser la primera etiqueta de `.text`»** | `3debb1e` (2026-09-19) | **B** — feina posterior. L'extret de juliol no la pot contenir. NO aplicar |
| C-2 | Elimina la fila `padding → farciment` de la taula de terminologia | `ca6c01a` (L6 Fase B) | **B** — el repositori té contingut més nou |
| C-3 | Elimina el paràgraf **«Manlleus en cursiva als títols de secció»** i en simplifica la fila de la taula | `ca6c01a` (L6 Fase B) | **B** — íd. |
| C-4 | Elimina la fila de branca `revisio/<grup>-t<N>-t<M>` i el seu paràgraf | `99c8543` (2026-09-19) | **B** — feina posterior |
| C-5 | `bibliografia.qmd` → `15_bibliografia.bib` (§Exemples d'aplicació) | vegeu sota | **A** (regressió) |
| C-6 | `bibliografia.qmd` → `15_bibliografia.bib` (§Bibliografia) | vegeu sota | **A** (regressió) |

**Quatre hunks de sis són categoria B.** Confirma l'advertència central: en un
fitxer divergit, la majoria de diferències són feina posterior.

---

## 🔴 TROBALLA FORA D'ABAST — reversió accidental a `13_contrib.qmd` (12/07)

Els hunks C-5 i C-6 no són una millora del xat de L3: són la **supervivència
d'un text correcte que el repositori va perdre**. Cronologia reconstruïda amb
`git log -S` i `git show`:

| Data | Commit | Què va passar |
| :--- | :--- | :--- |
| 12/07 | `614f576` «Fase C: Sanejament dels fitxers operacionals» | Corregeix **deliberadament** `bibliografia.qmd` → `15_bibliografia.bib`. Consta al missatge del commit: «actualitzat references sigles.md→12_sigles_simbols.qmd, bibliografia.qmd→15_bibliografia.bib» |
| 12/07 (h. després) | `4f973d5` «12_sigles_simbols.qmd afegida secció de notació» | **Desfà `614f576` a `13_contrib.qmd`**. El commit inclou un `A3.qmd_` de 2110 línies: va arrossegar fitxers de treball i una còpia antiga del fitxer |
| Juliol | xat L3 | Treballa sobre una còpia que encara tenia la correcció bona. D'aquí que l'extret la conservi |

**L'estat actual encara arrossega la reversió.** No es va reparar mai:

| Contingut perdut el 12/07 | Present avui a `13_contrib.qmd`? |
| :--- | :--- |
| §«Política de generació SVG» (sencera) | ❌ 0 ocurrències |
| §«Criteris de generació de l'slug» | ❌ 0 ocurrències |
| `15_bibliografia.bib` (2 llocs) | ❌ 0 ocurrències — diu `bibliografia.qmd`, **que no existeix** |
| Errata «l'esclat» (per «l'escalat»), «e.g.» | ⚠️ encara present |
| §«Sigles» → «Sigles, símbols i notació» | ✅ recuperat |

Conseqüències verificades:

- `15_bibliografia.bib` **existeix** i `_quarto.yml:213` l'hi apunta
  (`bibliography: 15_bibliografia.bib`); `bibliografia.qmd` **no existeix**.
  `13_contrib.qmd` documenta un fitxer inexistent en dos llocs.
- `CLAUDE.md:93` remet a «`13_contrib.qmd §Etiquetes `{#sec-}` a les
  capçaleres`» i `CLAUDE.md:135` a «`13_contrib.qmd §Figures i material
  gràfic`». **Cap de les dues seccions existeix** a `13_contrib.qmd`: les va
  eliminar la reversió.

Això depassa l'abast de la recuperació de diffs (és una pèrdua del repositori,
no un deliverable no integrat).

**Correcció de l'usuari (2026-09-20)**: `CLAUDE.md:135` remet a
`13_contrib.qmd §Figures i material gràfic`, que **sí existeix**
(`13_contrib.qmd:467`): aquella remissió resol, i el que falta és la
subsecció `#### Política de generació SVG` de dins. És una secció
empobrida, no una remissió trencada. L'única remissió que apunta al buit és
**`CLAUDE.md:93`** → `§Etiquetes {#sec-} a les capçaleres`. `A3.qmd_` ja no
existeix al repositori; l'única seqüela viva és `13_contrib.qmd`.

**Decisió presa**: C-5 i C-6 s'apliquen ara, amb la resta dels candidats A.
Són un error factual autocontingut (un fitxer que no existeix, en dos llocs)
i es corregeixen independentment de si les seccions es restauren. La
restauració del 12/07 va a part.

### Reconstrucció del que es va perdre el 12/07

`git show 614f576 -- 13_contrib.qmd`: +57 / −29.
`git show 4f973d5 -- 13_contrib.qmd`: +38 / −58 (la reversió és més gran que
el sanejament: va desfer també text anterior).

**De les 41 línies de contingut que `614f576` va afegir, 40 segueixen
absents avui.** Agrupades:

| Bloc perdut | Línies | Estat avui |
| :--- | :--- | :--- |
| `#### Política de generació SVG` (sencera: prioritat de SVG natiu, figures de nova creació, figures extretes de PDF amb `pymupdf`, figures de registres de bits, flux de pre-render, font de veritat de fonts i colors) | 18 | ❌ absent |
| `### Etiquetes {#sec-} a les capçaleres` (criteris 1–7 de generació de l'slug + excepcions) | 13 | ❌ absent — és la secció que `CLAUDE.md:93` referencia |
| `15_bibliografia.bib` (§Exemples d'aplicació i §Bibliografia) | 2 | ❌ absent (= hunks C-5 i C-6) |
| Fitxers obligatoris per a les IAs: remissió a `CLAUDE.md §Fitxers de referència obligatòria` i a `§Model i effortness` | 3 | ❌ absent (avui hi ha la llista antiga duplicada, `13_contrib.qmd:792`) |
| Taula Graphviz corregida | 1 | ⚠️ cas propi, vegeu sota |
| Errata «l'esclat» → «l'escalat», «e.g.» → «p. ex.» | 1 | ❌ absent (l'errata és viva) |
| Callout de separació de figures, referències provisionals | 2 | ❌ absent |

**Descomptat com a NO-pèrdua** (reescriptura posterior legítima, no cal
restaurar):

- `- **Sortida del programa**: ... syscall `exit`. Hipòtesi de treball...`:
  avui diu `syscall `exit2`. No es fa servir `startup.s`.`
  (`13_contrib.qmd:205`). El text actual és **posterior i millor**: la
  hipòtesi s'ha resolt. Categoria B.
- `referencias` → `referències`: la forma correcta ja va guanyar. Cap acció.

**Text obsolet que la reversió va reintroduir i encara és viu** (20 línies),
el més visible:

| Línia | Problema |
| :--- | :--- |
| `13_contrib.qmd:404` | `Noms de fitxers `A1.qmd`, `bibliografia.qmd`` — fitxer inexistent (= C-5) |
| `13_contrib.qmd:601` | `Definició: al fitxer `bibliografia.qmd`` — íd. (= C-6) |
| `l'esclat es fa amb width="40%"` | Errata ortogràfica + `e.g.` en lloc de `p. ex.` |
| `13_contrib.qmd:792` | Llista de fitxers obligatoris duplicada, en lloc de la remissió a `CLAUDE.md` |
| 4 comentaris `<!-- TODO: ... -->` | Es van migrar a `TODO.md` i van tornar |

**Cas propi — taula Graphviz** (`13_contrib.qmd:512`). No és una restauració
mecànica: **cap de les dues versions és correcta**. Avui diu origen
`24_specs/T7_mc_politiques_resum__graphviz.svg` i destí
`22_figs_originals/T7_mc_politiques_resum__graphviz.svg.svg` (doble
extensió). Comprovat al disc:

- Existeix: `22_figs_originals/T7_mc_politiques_resum__graphviz.svg` (origen).
- Existeixen: `auto_figs/T7_mc_politiques_resum__graphviz__original_{light,dark}.svg`
  (destins reals).
- No existeix res a `24_specs/` amb aquest nom, ni cap `.svg.svg`.

La versió de juliol (`22_figs_originals/T7_mc_politiques_resum.gv` →
`auto_figs/T7_mc_politiques_resum_light.svg`) tampoc coincideix amb els noms
actuals. **Cal redactar-la de nou contra l'estat real**, no restaurar-la.

**Pla acordat**: la reparació de `13_contrib.qmd` es fa **un cop classificat
també contra `L6_revisio_interna/`**, en un sol bloc que inclogui els
candidats A dels dos xats i la restauració del 12/07. Un fitxer, una decisió,
un bloc de commits. Motiu de prioritat: `13_contrib.qmd` és el fitxer de
convencions que llegeix cada sessió nova en arrencar; mentre estigui
incomplet, cada sessió comença amb convencions parcials.

### 3. `L6_revisio_interna/` — GRUP 2 (control)

*(pendent en aquesta sessió)*

### 4. `EC_sigles_i_símbols_T7_T8/` — GRUP 3 per presumpció, tancat a la Passada 0

`12_sigles_simbols.qmd`: **idèntic** al repositori. Cap feina.

Nota: el mateix fitxer apareix a `baixat_EC_A1_E1_S1_Fable/` amb 327 línies de
diferència. Aquell és grup 3 i va a la **sessió B**. La comparació entre les
dues versions extretes i el repositori s'ha de fer allà.

---

## Estat de la sessió A

| Xat | Fitxer | Estat |
| :--- | :--- | :--- |
| `L2_revisio_interna/` | `L2.qmd` | ✅ **Aplicat** (`1489c84`, `254509b`, `12bac2c`) |
| `L2_revisio_interna/` | `A2.qmd` | ✅ **Aplicat** (`1489c84`) |
| `L3_revisio_interna/` | `L3.qmd` | ✅ **Aplicat** (`f136762`, `c52538a`, `7f0703c`) + reordenació (`b6c8124`) |
| `L3_revisio_interna/` | `CLAUDE.md` | ✅ **Aplicat** (`0951e74`) |
| `L3_revisio_interna/` | `13_contrib.qmd` | ✅ C-5/C-6 aplicats (`8f363d2`); 4 hunks B descartats |
| `L6_revisio_interna/` | `L6.qmd` | ✅ tancat: idèntic (control superat) |
| `L6_revisio_interna/` | `A7.qmd` | ✅ tancat: idèntic |
| `L6_revisio_interna/` | `13_contrib.qmd` | ⏳ pendent (classificació sencera) |
| `EC_sigles_i_símbols_T7_T8/` | `12_sigles_simbols.qmd` | ✅ tancat: idèntic |

## Pendent immediat (resta de la sessió A)

1. `L6_revisio_interna/13_contrib.qmd` (4 lín.) — classificació sencera.
   **És l'últim pas abans de poder fer la reparació única del fitxer.**
2. `L6_revisio_interna/A7.qmd` — idèntic, tancat.
3. `L6_revisio_interna/L6.qmd` — idèntic, control superat, tancat.

### Encàrrec per a la reparació única de `13_contrib.qmd`

Un cop classificat contra `L6_revisio_interna/`, es fa **una sola passada**
sobre el fitxer que inclogui alhora:

- Els candidats A dels dos xats (L3 ja aplicats: C-5, C-6).
- La restauració del 12/07: política de generació SVG, criteris d'slug,
  remissions a `CLAUDE.md` per als fitxers obligatoris, errata «l'esclat».
- **Les 20 línies de text obsolet** que la reversió va reintroduir, la
  **llista de fitxers obligatoris duplicada** (`13_contrib.qmd:792`) i els
  **quatre `<!-- TODO -->`** ja migrats a `TODO.md`.
- **Fila Graphviz**: l'usuari ha confirmat que l'origen
  `22_figs_originals/T7_mc_politiques_resum__graphviz.svg` és el bo. El
  **destí no s'ha d'inventar**: cal derivar-lo de `25_scripts/gen_dark.py`,
  que és qui el genera, i documentar d'on s'ha tret.

**Recordatori explícit**: si a `L6.qmd` hi apareguessin candidats A, NO
s'apliquen — voldria dir que falla la classificació. No és el cas: és idèntic.

### APLICAT — L3, CLAUDE.md i C-5/C-6 tancats (2026-09-20)

| Commit | Contingut |
| :--- | :--- |
| `f136762` | L3-2, L3-3, L3-4 (conceptuals) |
| `c52538a` | L3-1, L3-5, L3-6, L3-8 (referències i nexe) |
| `7f0703c` | L3-7, L3-9, L3-10 (redacció) |
| `0951e74` | `CLAUDE.md`: `zobacz` → `vegeu` |
| `8f363d2` | `13_contrib.qmd`: C-5 i C-6 (nom del fitxer de bibliografia) |
| `b6c8124` | Reordenació de `_start` a `#exr-depuracio` (vegeu sota) |

`L3.qmd` després dels tres primers commits: **idèntic** a l'extret.

**L3-4 ampliat a petició de l'usuari.** El text aprovat afegeix el símptoma
observable a la causa, perquè en un exercici de depuració val tant com la
causa: l'epíleg ja ha restaurat `s0` amb el valor heretat de `_start` (0), de
manera que el `sb a0, 0(s0)` reexecutat escriu a `0x00000000` i RARS avorta
amb «`address out of range 0x00000000`».

#### Reordenació de `_start` a `#exr-depuracio` — autoritzada i executada

L'exclusió d'aquest bloc es va revocar: la posició de `_start` havia deixat
de ser una decisió oberta, perquè la regla «`_start` ha de ser la primera
etiqueta de `.text`» és a `13_contrib.qmd` des del 19/09. Reordenació
mecànica, i el text de L3-4 en depenia.

**Descoberta durant la verificació**: amb l'ordre antic (`g`, `codifica`,
`_start`), RARS començava a executar per `g` amb `a1 = 0` i avortava a la
primera instrucció del programa. **Cap dels tres errors deliberats no
arribava a manifestar-se**, i el símptoma que descriu l'Error 1 era
inobservable.

Verificat a RARS 1.6 real (`rars1_6.jar`), tres execucions:

| Cas | Resultat |
| :--- | :--- |
| Ordre antic | `line 11` (`lb t0, 0(a1)`, dins de `g`), `at 0x00400000: address out of range 0x00000000` |
| Ordre nou | `line 47` (`sb a0, 0(s0)`), `at 0x00400074: address out of range 0x00000000` — el símptoma de l'Error 1 |
| Control, tres errors corregits | `Program terminated by calling exit` |

#### Verificació post-aplicació

- `make render` complet: **cap warning**; cap `?@` a `_book/`.
- `python3 25_scripts/verifica_laboratoris.py`: **1 error E1**, no 2.
  - ✅ `L3:490` ha desaparegut de la llista d'E1: ara consta com a
    `ASSEMBLA / OK`, amb l'excepció d'execució registrada com a informació
    (`line 47 ... 0x00400074`), que és el comportament esperat d'un exercici
    de depuració amb tres errors deliberats.
  - ⏳ Queda `s3_4_2.s` línia 368 («primera etiqueta després de `.text` és
    `moda:`, no `_start:`»), **fora d'abast per decisió de l'usuari**.

**Nota per a l'auditoria**: el verificador tracta com a E1 el que en un
exercici de depuració és el comportament esperat. En aquest cas s'ha resolt
sol en reordenar, però la qüestió de fons —que el script no distingeix un
programa que falla per disseny d'un que falla per error— queda oberta. No
s'ha tocat el script.

## Exclòs d'aquesta feina (confirmat)

La correcció de l'ordre de `_start` a **`s3_4_2.s` (línia 368)** continua
fora d'abast. **No forma part dels canvis recuperats**: cap hunk dels
extrets de `L3.qmd` hi toca. Va en una tasca a part.

El bloc `L3:490` sí que s'ha corregit (vegeu `b6c8124`), amb autorització
explícita de l'usuari del 2026-09-20.

---

## Pendent — sessió B (grup 3)

Ordre previst (punts 5–10 de l'ordre original):

| Ordre | Xat | Fitxers amb diff |
| :--- | :--- | :--- |
| 5 | `EC_Revisio_interna_de_L4_L3/` | `A4.qmd` (23 lín.); `L4.qmd` (6 lín.) → **B per construcció**, vegeu nota L4/L5 |
| 6 | `baixat_T9-PE_T9_revisio_interna/` | `13_contrib.qmd` (105); `CLAUDE.md` (68); `S_criteris.qmd` (8) |
| 7 | `baixat_EC_A3_E3_S3__revisio_interna/` | `13_contrib.qmd` (10); `S_criteris.qmd` (8) |
| 8 | `baixat_EC_A4_E4_S4_Fable/` | `13_contrib.qmd` (49); `A4.qmd` (342) |
| 9 | `baixat_EC_A1_E1_S1_Fable/` | `12_sigles_simbols.qmd` (327) |
| 10 | `baixat_EC_A5_E5_S5_Fable/` | `A3.qmd` (80); `index.qmd` (69) |
| 10 | `EC_L5_revisio_interna/` | `L5.qmd` (101) → **B per construcció**, vegeu nota L4/L5 |

### Nota L4/L5 (resolta per l'usuari, 2026-09-20)

De L4 i L5 hi ha dues versions a la col·lecció, una d'anterior i una de
posterior a la revisió en tres passades:

- `EC_Revisio_final_L5_tres_passades/L5.qmd` → idèntic al repo (versió nova).
- `EC_L5_revisio_interna/L5.qmd` → 101 lín. (versió **anterior**) ⇒ **categoria B**.
- `baixat_EC_L4_revisio_interna_tres_passades/L4.qmd` → idèntic (versió nova).
- `EC_Revisio_interna_de_L4_L3/L4.qmd` → 6 lín. (versió **anterior**) ⇒ **categoria B**.

No són candidats. Si a la sessió B apareix alguna línia que **no** encaixi en
aquest patró (contingut que la versió nova hagi perdut), cal aturar-se i
consultar-ho.

### Fitxers que apareixen en més d'un xat (comparació creuada obligatòria a la sessió B)

- `13_contrib.qmd`: a `L3_revisio_interna` (13), `L6_revisio_interna` (4),
  `baixat_EC_A3_E3_S3` (10), `baixat_EC_A4_E4_S4` (49), `baixat_T9-PE_T9` (105).
- `12_sigles_simbols.qmd`: a `EC_sigles_i_símbols_T7_T8` (idèntic) i
  `baixat_EC_A1_E1_S1_Fable` (327).
- `A3.qmd`: a `baixat_EC_A3_E3_S3` (idèntic) i `baixat_EC_A5_E5_S5` (80).
- `A4.qmd`: a `baixat_EC_A4_E4_S4` (342) i `EC_Revisio_interna_de_L4_L3` (23).
- `S_criteris.qmd`: a `baixat_EC_A3_E3_S3` (8) i `baixat_T9-PE_T9` (8).
- `CLAUDE.md`: a `L3_revisio_interna` (2) i `baixat_T9-PE_T9` (68).

### Cap pendent de procedència

`baixat_S_criteris_seleccio.qmd` és un fitxer solt a l'arrel d'`extrets/`, sense
subdirectori de xat. Cal determinar-ne l'origen abans de classificar-lo.

---

## ⚠️ SEGON MODE DE FALLADA — per a l'auditoria posterior

**No investigar ara.** Entrada oberta el 2026-09-20 arran del cas del 12/07.

Aquest pipeline de recuperació busca **un sol** mode de fallada:

> **Mode 1 — feina mai integrada.** Un xat produeix un deliverable i ningú no
> el porta al repositori. Es detecta comparant els extrets amb el repositori:
> el contingut és als extrets i no hi és al repo.

El cas del 12/07 n'exhibeix un de **diferent**, que el pipeline no busca i que
no hauria trobat si no fos que en teníem els extrets:

> **Mode 2 — feina integrada i després esborrada en silenci.** Un commit
> posterior arrossega una còpia vella d'un fitxer que **no és l'objecte del
> commit** i en revessa canvis ja integrats. No hi ha conflicte, ni error, ni
> rastre al missatge del commit: la feina simplement desapareix.

Característiques del cas documentat (`4f973d5`, 12/07):

- El missatge del commit parla de `12_sigles_simbols.qmd`; la víctima és
  `13_contrib.qmd`, que no s'hi esmenta.
- Relació insercions/supressions anòmala en el fitxer víctima: +38 / −58,
  quan el commit és nominalment d'addició de contingut en un **altre** fitxer.
- El commit arrossega fitxers de treball (`A3.qmd_`, 2110 línies), senyal d'un
  `git add` massa ampli des d'un directori de treball desincronitzat.
- Va sobreviure 2 mesos sense detectar-se perquè no trenca el render: el
  llibre compila igual amb les convencions incompletes.

### Proposta de detecció (per executar a l'auditoria)

L'objectiu és trobar altres commits amb el mateix patró, **incloent-hi xats
dels quals no tenim extrets** (on el mode 2 és invisible per comparació).

1. **Commits amb supressions grans en fitxers que el missatge no esmenta.**
   Per a cada commit, comparar la llista de fitxers amb supressions
   significatives (p. ex. > 20 línies o > 25 % del fitxer) contra els noms de
   fitxer citats al missatge. Els que no hi apareixen són candidats.

   ```bash
   git log --format='%H%n%s%n%b' --numstat -- '*.qmd' '*.md'
   ```

2. **Commits amb relació anòmala insercions/supressions** en un fitxer que no
   és l'objecte declarat del commit (com aquí: +38 / −58 a `13_contrib.qmd`
   en un commit sobre `12_sigles_simbols.qmd`).

3. **Commits que arrosseguen fitxers de treball** (`*_`, `*.orig`, `*.bak`,
   `*.qmd_`, còpies numerades): indici d'un `git add` massa ampli, i per tant
   de possible reversió col·lateral.

4. **Verificació creuada amb els missatges de commit que declaren
   correccions**: `614f576` enumerava explícitament les seves correccions
   («bibliografia.qmd→15_bibliografia.bib»). Comprovar que cada correcció
   declarada en un missatge de commit **segueix viva** al fitxer avui és una
   prova barata i d'alt rendiment. Es pot automatitzar parcialment extraient
   els patrons `X→Y` dels missatges i comprovant que `Y` hi és i `X` no.

5. **Remissions penjades**: tot `§Nom de secció` citat des de `CLAUDE.md` o
   `13_contrib.qmd` ha de correspondre a una capçalera existent al fitxer
   destí. Va ser el símptoma que va destapar aquest cas
   (`CLAUDE.md:93` → secció inexistent).

**Abast**: el mode 2 pot haver afectat qualsevol fitxer, no només els que
tenim als extrets. Els punts 1–3 són purament històrics (només `git log`) i
els 4–5 comproven l'estat actual; cap no depèn de tenir els deliverables
originals.

---

## Fitxers de REGISTRE (no comparats; només evidència)

`TODO.md` (×6), `*_tasques.md` (`T1_P`, `T3_P`, `T4_P`, `T2_P`, `A9_P`, `L5_tasques`
×2, `L6_tasques`), `L2__revisio_interna.md`, `L3__revisio_interna.md`,
`Lx__revisio_interna__plantilla.md`, `saneja_tasques.md`,
`substantiu_adjectiu.md`, `sigles_simbols__tasques.qmd`.

---

## Regles vigents en aquesta recuperació

- Cap canvi sense confirmació explícita, un a un.
- No aplicar diffs a cegues: la majoria de diferències del grup 3 són feina
  posterior.
- Discriminador obligatori per a tot hunk A dels grups 2 i 3:
  `git log -S'<fragment>' --oneline -- <fitxer>`.
- **Exclòs d'aquesta feina**: la correcció de l'ordre de `_start` a L3
  (Decisió 1 d'aquell xat, mai resposta, no present als canvis recuperats).
