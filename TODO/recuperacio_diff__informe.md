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

*(pendent en aquesta sessió — vegeu «Pendent immediat»)*

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
| `L3_revisio_interna/` | `L3.qmd` | ⏳ pendent de classificar |
| `L3_revisio_interna/` | `CLAUDE.md` | ⏳ pendent de classificar |
| `L3_revisio_interna/` | `13_contrib.qmd` | ⏳ pendent (classificació sencera A/B/C/D) |
| `L6_revisio_interna/` | `L6.qmd` | ✅ tancat: idèntic (control superat) |
| `L6_revisio_interna/` | `A7.qmd` | ✅ tancat: idèntic |
| `L6_revisio_interna/` | `13_contrib.qmd` | ⏳ pendent (classificació sencera) |
| `EC_sigles_i_símbols_T7_T8/` | `12_sigles_simbols.qmd` | ✅ tancat: idèntic |

## Pendent immediat (resta de la sessió A)

1. `L3_revisio_interna/L3.qmd` (22 lín.) — grup 1, categoria A per premissa.
2. `L3_revisio_interna/CLAUDE.md` (2 lín.) — grup 1, categoria A per premissa.
3. `L3_revisio_interna/13_contrib.qmd` (13 lín.) — **classificació sencera A/B/C/D**
   (el fitxer va rebre feina el 19/09 i ha divergit).
4. `L6_revisio_interna/13_contrib.qmd` (4 lín.) — classificació sencera.
5. `L6_revisio_interna/A7.qmd` — idèntic, tancat.
6. `L6_revisio_interna/L6.qmd` — idèntic, control superat, tancat.

**Recordatori explícit**: si a `L6.qmd` hi apareguessin candidats A, NO
s'apliquen — voldria dir que falla la classificació. No és el cas: és idèntic.

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
