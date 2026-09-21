# L2 — aplicació de cinc decisions preses

Fitxer **transitori**. S'esborra en tancar aquesta feina.

Sessió 2026-09-21. Model: Opus 5. Base: `3df456d` (tancament de la Passada 1
de la recuperació de diffs).

Regles heretades de `recuperacio_diff__informe.md §Regles vigents`, aplicades
aquí: cap canvi sense confirmació explícita; no aplicar res a cegues; la
**invariant de verificació** (la comprovació final es fa contra la llista de
decisions i sobre l'arbre de treball, mai contra un fitxer extret ni contra el
commit que va introduir un canvi).

---

## ✅ TANCADA. Les cinc decisions aplicades

| # | Decisió | Commit |
| :--- | :--- | :--- |
| 1 | **D3** — treure els blocs plantilla `.markdown` | `733b408` |
| 2 | **D1** — renumerar els lliuraments | `4ab25cb` |
| 3 | **P3** — regla dels tres usos per a `filename` | `608056f` |
| 4 | **P1** — partir els cinc callouts «Comprovació pràctica» | `cf2dd43` |
| 5 | **D2** — esquelet a `s2_1_1.s` | `2103579` |

L'ordre era deliberat i es va respectar: D3 primer (menys blocs a renumerar),
D1 abans que P3 (P3 treballa amb els noms definitius), i la renumeració de més
alt a més baix.

---

## Pas 0 — inventari (la part que va evitar una errada)

L'encàrrec demanava derivar la correspondència secció↔lliurament **del fitxer
actual, no del registre de juliol**. Es va fer, i el resultat va coincidir amb
D1 — però verificat, no heretat. La secció `la`/`li` ja era al fitxer
(`L2.qmd:356`), que és precisament la causa del desfasament: els noms
corresponien a la numeració anterior a la seva inserció.

**Abast real de les referències `s2_*`** (escombrada de tot l'arbre, sense
filtre d'extensió): només **dos** fitxers.

| Fitxer | Naturalesa |
| :--- | :--- |
| `04_laboratori/L2.qmd` | L'únic fitxer de contingut. |
| `TODO/L2_tasques.md` | Registre transitori de juliol; descriu l'estat *previ*. No s'ha tocat: com a registre històric és correcte tal com està. |

`E2.qmd`, `S2.qmd`, `A2.qmd`, `_quarto.yml`, `25_scripts/verifica_laboratoris.py`
i `TODO/laboratori/L2/`: **cap ocurrència**. La renumeració no tenia radi
d'acció fora de `L2.qmd`.

**`§2.x` escrits a mà**: cap a `L2.qmd` ni a cap `.qmd`. Les referències
internes són totes `@sec-`/`@exr-`/`@cau-`, que Quarto resol sol. Els únics
`§N.x` del corpus són a `13_contrib.qmd:125` i a fitxers `TODO/`, fora d'abast.

**Xoc de renumeració confirmat**: `s2_3_1`, `s2_3_2` i `s2_4_1` existien alhora
com a noms d'origen i de destinació. L'ordre descendent era obligatori, no una
precaució.

---

## Correccions rebudes durant l'execució

Dues, totes dues de l'usuari i totes dues correctes. Es registren perquè
canvien criteri, no només aquest fitxer.

### 1. P3 no era una regla nova

La regla ja era codificada a `13_contrib.qmd:444-455`: el camp `filename`
indica **el llenguatge o el context**, i només un fitxer `.s` específic porta
el seu nom. No hi ha forma per a un `.c` amb nom de lliurament, i no n'hi ha
d'haver. El pas 3, doncs, no introduïa cap criteri: **alineava L2 amb la regla
existent**. L2 era l'únic fitxer del corpus que no la seguia.

Conseqüència operativa: els blocs `.c` **no es van renumerar** al pas 2, perquè
al pas 3 havien de quedar tots com a `C` igualment. Tocar-los dues vegades no
aportava res, i la incoherència entre commits intermedis és irrellevant —
la verificació es fa sobre l'estat final.

### 2. La llista de Fibonacci no barrejava bases

La llista `0, 1, 1, 2, 3, 5, 8, 0xD, 0x15, 0x22` **era tota hexadecimal**. Els
set primers termes s'escriuen igual en totes dues bases i el canvi només es
nota a partir de 13 (`0xD`), 21 (`0x15`) i 34 (`0x22`). Tal com estava, el
lector deduïa que la base canviava a mig camí.

La resposta correcta no era explicar la incoherència sinó **eliminar-la**:
tots deu termes amb prefix, `0x0` … `0x22`. Confirmat empíricament contra el
bolcat de RARS, que és hexadecimal.

### 3. El precedent de la forma de l'oracle existia

Es va proposar un paràgraf en negreta «**Comprovació**: …» dient que no hi
havia precedent. N'hi havia, però **com a prosa, no com a callout**: L3 ja posa
l'oracle al final de l'enunciat amb l'imperatiu «Comproveu…»
(`L3:110`, `L3:331`, `L3:555`). S'ha adoptat aquesta forma.

Que no es trobés és simptomàtic: era pràctica establerta però **no estava
escrita enlloc**. Per això ara es registra (vegeu més avall).

---

## Detall per decisió

### D3 — plantilles `.markdown` (`733b408`)

Tres blocs eliminats: `s2_1_2.md`, `s2_1_3.md`, `s2_2_1.md`. Reproduïen taules
que l'enunciat ja mostra en línia o que la prosa ja descriu.

Motiu: **font única de veritat**. `#cau-format-codi-esquelet` ja fixa
l'esquelet canònic a `A2.qmd §nte-programa-esquelet` i el format a
`#imp-codi-format-criteris`; una plantilla a banda és una còpia més que
divergeix en silenci.

### D1 — renumeració (`4ab25cb`)

`s2_4_1 → s2_5_1`, `s2_3_* → s2_4_*`, `s2_2_* → s2_3_*`, en aquest ordre.
`s2_1_*` sense canvi. Abast: taula de Lliuraments, títols dels `{#exr-}` i
`filename=` dels blocs `.s`.

### P3 — regla dels tres usos (`608056f`)

- 5 blocs `.c` → `filename="C"`.
- El bloc `.s` de `@exr-punters-valors` → `filename="RV32I"`: el lliurament
  d'aquell exercici és un `.md`, de manera que aquell `.s` és la declaració
  que s'ha d'analitzar, no un fitxer a entregar.
- La resta de blocs `.s` corresponen a lliuraments reals i conserven el nom.

### P1 — partició dels cinc callouts (`cf2dd43`)

| # | Exercici | Oracle → enunciat | Callout al `{#sol-}` |
| ---: | :--- | :--- | :--- |
| 1 | `@exr-punters-valors` | 2 words | **Sí** — assemblar sense executar |
| 2 | `@exr-punters-codi` | `s0` + 2 words | **Sí** — dues vistes + pas a pas |
| 3 | `@exr-vectors-declaracio` | `s1`, amb `li s2, 7` | **No** |
| 4 | `@exr-vectors-fibonacci` | 10 termes | **No** |
| 5 | `@exr-strings-ascii` | 2 words | **Sí** — lectura byte a byte |

Motiu: hi haurà una versió del llibre **sense solucions**, i tot això és estudi
previ que es lliura **abans** de la sessió. Un oracle dins d'un `{#sol-}` és
inabastable justament quan fa falta.

Dos principis que en van sortir i que valen per a tot el corpus:

- **Un oracle és una parella (entrada, resultat esperat).** Un valor sense la
  seva precondició no és un test, perquè no es pot reproduir. Per això el
  `li s2, 7` del cas 3 se'n va a l'enunciat amb el resultat.
- **Un callout que només existeix per no deixar el lloc buit és soroll.** Els
  casos 3 i 4 es queden sense, perquè un cop separat l'oracle no els quedava
  tècnica substantiva.

### D2 — esquelet a `s2_1_1.s` (`2103579`)

`.globl _start`, `.text`, `_start:` i sortida amb syscall 93, seguint
`@nte-programa-esquelet` i la forma de `hola.s` (L1). Frase a l'enunciat:
«Afegiu-hi l'esquelet mínim del programa (@nte-programa-esquelet)».

El segment `.data` no canvia, de manera que el bolcat de
`@exr-rars-vista-memoria` continua sent vàlid — comprovat.

---

## Convencions registrades a `13_contrib.qmd`

La regla de «Comprovació pràctica» s'ha reescrit amb la separació
oracle/tècnica (commit `cf2dd43`). Hi consta ara:

- On va l'oracle (final de l'enunciat, prosa, «Comproveu que…») i **per què**
  (la versió sense solucions + l'estudi previ es lliura abans de la sessió).
- Que un oracle és una parella (entrada, resultat esperat).
- On va la tècnica (callout al `{#sol-}`).
- Que si no queda tècnica substantiva, el callout se suprimeix.

Això permet que L3–L6 heretin la convenció quan els toqui la revisió.

---

## Verificació

Feta **sobre l'arbre de treball i contra la llista de cinc decisions**, segons
la invariant heretada.

| Comprovació | Resultat |
| :--- | :--- |
| `make render` complet (HTML + PDF) | **exit 0, cap warning** |
| Referències creuades no resoltes (`?@`) | **cap** a tot el contingut renderitzat |
| `grep -rn 's2_[0-9]_[0-9]'` a tot el corpus | cap nom antic a `L2.qmd` |
| Taula de Lliuraments ↔ cos del document | **igualtat exacta de conjunts** |
| `verifica_laboratoris.py` | **1 error E1**, `L3:357` — l'estat conegut. Cap de nou. |
| Escombrada de pèrdues | **cap pèrdua real** (vegeu sota) |

### Numeració renderitzada (derivada de la sortida, no del codi font)

    29.1 Representació en memòria   →  s2_1_1.s, s2_1_2.md, s2_1_3.md
    29.2 Pseudoinstruccions la i li →  (cap lliurament)
    29.3 Punters                    →  s2_3_1.md, s2_3_2.s
    29.4 Vectors                    →  s2_4_1.md, s2_4_1.s, s2_4_2.s
    29.5 Cadenes de caràcters       →  s2_5_1.s

Cada lliurament cau a la secció que el seu nom declara. §29.2 no en té, que és
tota la raó de la renumeració.

### Oracles verificats contra execució real de RARS

No es van donar per bons: es van contrastar amb el bolcat de
`verifica_laboratoris.py`.

| Cas | Oracle | Bolcat RARS |
| :--- | :--- | :--- |
| 2 | `A[1]`=`0x0000000C`, `punter`=`0x10010008` | `0000000c`, `10010008` ✔ |
| 4 | `0x0` … `0x22` | `0,1,1,2,3,5,8,d,15,22` ✔ (i **tot hex**, confirma la correcció) |
| 5 | `0x36383931`, `0x00000035` | `36383931`, `00000035` ✔ |
| 1 | dump de `s2_1_1.s` inalterat | `fea800fb…` ✔ |

**Efecte lateral mesurable de D2**: `s2_1_1.s` passa de només *ASSEMBLA* a
**EXECUTA FINS AL FINAL / OK** a l'informe del script. És la confirmació
empírica que la decisió era necessària.

### Escombrada de pèrdues

42 línies afegides als 5 commits d'aquesta passada, comprovades contra l'estat
final del fitxer. **1 absent, explicada:**

| Commit | Línia | Explicació |
| :--- | :--- | :--- |
| `4ab25cb` | ` ```{.s filename="s2_3_1.s"} ` | **Supersessió aprovada dins la passada**: D1 la va renomenar i P3 (`608056f`) la va convertir a `RV32I`, que és el cas límit confirmat al pas 0. Verificat amb `git log -S`: el commit que la treu és exactament `608056f`. |

**Cap pèrdua real.** Les altres 41 són a l'arbre de treball.

---

## Per a més endavant — NO tocat en aquesta passada

Anotat a petició de l'usuari, que va comptar el corpus sencer.

### Blocs `.c` amb nom d'estil lliurament — passada C

Xifres de l'usuari, mesurades sobre la base `3df456d`: **139 blocs `.c` ja
feien servir `C`** i **10** portaven nom d'estil lliurament. Verificades i
correctes.

P3 n'ha mogut 5 (els de L2) d'una columna a l'altra, de manera que l'abast
pendent per a la passada C ha canviat i **ara és 5, no 10**:

| Fitxer | Blocs |
| :--- | :--- |
| `L3.qmd` | `s3_2_1.c` (:96), `s3_3_1.c` (:186), `s3_4_2.c` (:306) |
| `L4.qmd` | `s4_2_2.c` (:143), `s4_3_1.c` (:300) |

Recompte comprovat abans/després: 139 → **144** amb `C`; 10 → **5** amb nom
d'estil lliurament. Aquests 5 són **la desviació**, no la norma, i s'alinearan
a la **passada C**, no ara. L2 ja ha quedat alineat com a efecte de P3.

### `CLAUDE.md` — la regla operativa està desfasada (passada C)

Contradicció detectada en arribar al push d'aquesta passada: el protocol de la
feina demana publicar l'informe a cada aturada, però `CLAUDE.md §Regles
operatives` encara diu «Claude Code: fes només canvis locals. L'usuari
actualitza el repositori manualment».

Veredicte de l'usuari: **el desfasat és `CLAUDE.md`**. Aquella regla descriu
com es treballava abans. Ara Claude Code fa commit i push d'allò que l'usuari
confirma, i **l'informe publicat és el mecanisme de revisió**. La salvaguarda
de debò no és no publicar: és **no canviar res sense confirmació**, i es manté
intacta.

**No s'ha arreglat en aquesta passada** (fora d'abast de la passada A). Text de
substitució acordat, per aplicar a la passada C:

> - Claude Code: pots fer commit i `push` a `origin`, però **només de canvis
>   que l'usuari hagi confirmat explícitament**. Fix-forward sempre: no
>   reescriguis l'historial. L'informe de la feina en curs es publica a cada
>   aturada, perquè la revisió es fa llegint el repositori.

### `CLAUDE.md` — taula de «Model i effortness» (passada C)

La taula no preveu el tipus de feina d'aquests dos dies —**classificació i
aplicació de decisions**— i les files que hi ha no s'han fet servir. Cal
revisar-la a la passada C i **proposar una taula nova** quan s'hi arribi.

### `verifica_laboratoris.py` no dedueix el «bloc no autònom» — auditoria (passada B)

Detectat en tancar el punt 4. El script **ja té** la noció de bloc que no ha
d'assemblar sol, però com a **taula codificada a mà**, no com a propietat
derivada del contingut:

```python
INCOMPLETE_BY_DESIGN = {
    ("L3", "s3_4_2.s", 1): "conté el comentari `# update: vegeu @sol-update …`",
}
```

`s3_4_2.s` crida `jal ra, update` i `update:` no hi és definit — és justament
el que l'estudiant ha d'inserir. El bloc no és autònom **per disseny**, i el
`OK` de l'informe surt d'aquesta entrada, no de cap anàlisi del bloc.

Dues conseqüències:

- **La raó ja està desfasada**: la taula cita `@sol-update` i el bloc diu ara
  «vegeu la solució de `s3_4_1.s`». Una taula paral·lela al contingut divergeix
  en silenci — el mateix motiu que va treure les plantilles `.markdown` a D3.
- **`#exr-depuracio` no hi és**, i és el mateix cas per un altre camí: té tres
  errors a posta. Un bloc pot ser no autònom per omissió (falta codi) o per
  incorrecció deliberada (el codi hi és i està malament a propòsit).

Cal una noció de **bloc no autònom** derivada del contingut. **No s'ha tocat
res**: ni el script ni la taula. Fora d'abast de la passada B.

### Un ús que `13_contrib.qmd` no preveu — decisió pendent

Els marcadors `⚠️ codi_erroni__*.c ⚠️` i
`⚠️codi_erroni__alineacio_incorrecte.s⚠️` **no són ni llenguatge ni context**:
són una marca semàntica de «codi deliberadament incorrecte». La taula de
`13_contrib.qmd §Blocs de codi` no en preveu la categoria.

**Cal decidir si mereixen fila pròpia.** No s'ha tocat res.

---
---

# Passada C — escombrades del corpus i convencions

Sessió 2026-09-21 (continuació). Model: Opus 5. Base: `6ee1a8a` (tancament de
la passada B).

## Regla de protocol adoptada en obrir la passada

Quatre errors del mateix tipus a les passades A i B, tots dos interlocutors:
**concloure sobre el conjunt des del tros mirat**. La passada C és tota
escombrades, que és on aquest error fa més mal. Regles vigents:

1. Tota escombrada **declara el seu abast**, i l'abast és el corpus sencer
   tret que hi hagi un motiu escrit per excloure'n res.
2. Tota afirmació de la forma «és l'únic», «no n'hi ha cap» o «no hi ha
   precedent» va acompanyada de **l'ordre exacta que la sosté**.
3. Abans de concloure sobre un bloc, **llegir-lo sencer**.

La regla 1 ha donat fruit immediatament: vegeu 1a.

---

## Bloc 1 — mecànic. Tres commits

### 1a — slug `desplacament-arithmetic` → `-aritmetic` (`953edca`)

**Ordre**: `git grep -n "desplacament-arithmetic" -- .` (tots els fitxers
versionats, sense filtre d'extensió).

| Fitxer | Paper |
| :--- | :--- |
| `01_apunts/A3.qmd:91` | Definició del callout |
| `04_laboratori/L3.qmd:29` | Referència |
| `04_laboratori/L5.qmd:29` | Referència |
| `11_riscv.qmd:91` | Referència — **la que faltava** |
| `TODO/L3_tasques.md:155` | Registre històric; no es toca |

Eren **4 ocurrències de contingut, no 3**. `TODO/L3_tasques.md` deia «tocaria
A3 (definició), L3 i L5» i es va escriure sense escombrar `11_riscv.qmd`.
És el mateix fitxer que ja havia quedat fora d'una escombrada de `∈` a la
passada B: un compendi inclòs per `{{< include >}}`, fàcil d'ometre quan
l'escombrada es limita a `01_apunts/` i `04_laboratori/`.

Sense col·lisió: `#imp-notacio-desplacament-aritmetic` (A3.qmd:85) ja existia i
és un slug diferent de `#nte-instruccions-desplacament-aritmetic`.

### 1b — «de menor pes» → «de menys pes» (`4accc6c`)

**Ordres**: `git grep -o "de menor pes" -- '*.qmd' | wc -l` → 18;
`git grep -n "de menor pes" -- '*.qmd'` per a la llista.

17 de contingut (A2×1, A3×3, A5×2, A8×3, L3×3, L5×5) i 1 a
`TODO/recuperacio_diff__informe.md`, informe tancat, no tocat.

Criteri: **simetria, no majoria**. Mesurat abans de tocar res:

| Forma | Ocurrències |
| :--- | ---: |
| `de més pes` | 28 |
| `de major pes` | **0** |
| `de menys pes` | 32 |
| `de menor pes` | 17 |

El costat alt ja era unànime; «més» aparella amb «menys». Després del canvi,
`de menys pes` = 49 i `de menor pes` = 0.

**Abast deliberadament exclòs**: la resta d'usos de «menor»/«major» al corpus
(`git grep -n "menor\|major" -- '*.qmd'`, ~70 línies) són comparacions
matemàtiques («el menor enter representable»), «row-major order» i «la
majoria». La regla és sobre el **pes dels bits**; no s'hi toca res més.

### 1c — tanca la regla de `filename` (`a29a65b`)

Tres parts, totes sota `13_contrib.qmd §Blocs de codi`.

| Lloc | Abans | Després | Motiu |
| :--- | :--- | :--- | :--- |
| `L4.qmd:143` | `s4_2_2.c` | `C` | El lliurament és `.md`+`.s`; el `.c` és l'enunciat |
| `L4.qmd:300` | `s4_3_1.c` | `C` | Ídem |
| `L3.qmd:463` | `"..."` | `C` | Placeholder literal (ja detectat a `TODO/L3_tasques.md:107`) |
| `L3.qmd:491` | *(cap atribut)* | `s3_5_1.s` | És el lliurament declarat a `L3.qmd:18` |

Amb els dos de L4 s'esgoten els 5 blocs `.c` anotats com a pendents a
l'informe de la passada A.

**Escombrades de tancament**:

- `git grep -n 'filename="\.\.\."' -- '*.qmd'` → queda **només**
  `13_contrib.qmd:151`, on `"..."` és metavariable dins la prosa que descriu
  la convenció. Correcte tal com està.
- `git grep -n '^```{\.s}$' -- '*.qmd'` → **cap** bloc `.s` sense `filename`
  a tot el corpus.

**Efecte lateral mesurat**: en posar-li `filename`, el bloc d'`#exr-depuracio`
entra a l'informe de `verifica_laboratoris.py` i hi surt com a **EXCEPCIÓ**
(`address out of range 0x00000000`) — que és **exactament** el símptoma que
`@sol-depuracio` documenta com a Error 1 (l'epíleg restaura `s0`=0 i
`sb a0, 0(s0)` escriu a l'adreça 0). No és una regressió: les comprovacions
estàtiques segueixen amb «Cap troballa» i l'exit code és 0. La classificació
d'aquest bloc (assembla i falla en execució **a posta**) va a l'auditoria.

### Verificació del bloc 1

| Comprovació | Ordre | Resultat |
| :--- | :--- | :--- |
| Render complet | `make render` | **exit 0**, cap warning |
| Referències no resoltes | `grep -rho '?@[a-z-]*' _book/*.html \| sort -u \| wc -l` | **0** |
| Íd. al PDF | `grep -o "?@[a-z-]*" Estructura-de-computadors.tex` | **cap** |
| Laboratoris | `python3 25_scripts/verifica_laboratoris.py` | **exit 0**, «Cap troballa» a les estàtiques |

---

## Regla d'escombrada — `git grep`, mai `grep -r`

Elevada a regla arran de 1a (l'ocurrència oblidada era a `11_riscv.qmd`).

**Tota escombrada d'aquesta passada i de l'auditoria es fa amb `git grep`.**
Raó: `git grep` només veu fitxers **versionats**, de manera que cobreix l'arrel
i `21_riscv/` i exclou `auto_riscv/` i `_book/` sense haver-hi de pensar.
`grep -r` obliga a enumerar exclusions a mà, que és precisament com es
perden ocurrències.

Família de fitxers de contingut **fora** de `01_apunts/`–`04_laboratori/`, que
és on es perden les escombrades mal delimitades:

| Lloc | Què | Escombrar-hi? |
| :--- | :--- | :--- |
| Arrel | `11_riscv.qmd`, `12_sigles_simbols.qmd`, `13_contrib.qmd`, `14_LICENSE.qmd`, `index.qmd` | **Sí** |
| `21_riscv/` | ~45 fragments inclosos amb `{{< include >}}`, versionats | **Sí** |
| `auto_riscv/` | Generat, a `.gitignore` | **No** — es regenera |
| `_book/`, `auto_figs/` | Sortida del render | **No** |

Corol·lari operatiu: un patró restringit a `'*.qmd'` ja cobreix l'arrel i
`21_riscv/` si l'ordre és `git grep`. El filtre perillós no és l'extensió sinó
el **prefix de directori**.

---

## Bloc 2 — dues llistes per revisar. **CAP CANVI APLICAT**

Estat: llistes presentades a l'usuari, pendents de veredicte. Res tocat al
corpus. Una sessió nova pot reprendre des d'aquí sense reconstruir res.

### 2a — «escriviu un programa» on es demana un fragment

**Ordre**: `git grep -in "escriviu un programa" -- .` → **6 ocurrències**,
que confirma el compte de l'usuari.

Cinc són a `E4.qmd`, no a un fitxer de T5: els slugs són `exr-p5-*` però el
fitxer és `02_exercicis/E4.qmd`.

**Discriminador aplicat** (de l'usuari): si les dades arriben ja en registres
i l'enunciat no demana `.data`, ni `_start`, ni seqüència de sortida, és un
fragment.

| # | Ocurrència | Slug | Dades | Veredicte |
| ---: | :--- | :--- | :--- | :--- |
| 1 | `E4.qmd:58` | `exr-p5-sr-overflow-deteccio-natural` | ja a `t1`,`t2`; surt a `t0`,`t3` | **FRAGMENT** |
| 2 | `E4.qmd:64` | `exr-p5-sr-overflow-deteccio-enter` | ja a `t1`,`t2`; surt a `t0` | **FRAGMENT** |
| 3 | `E4.qmd:105` | `exr-p5-mul-programa` | ja a `t0`,`t2`; surt a `t3`,`t4` | **FRAGMENT** |
| 4 | `E4.qmd:111` | `exr-p5-mul-overflow` | ja a `t1`,`t2`,`t3`; surt a `t0` | **FRAGMENT** |
| 5 | `E4.qmd:556` | `exr-p5-div-programa` | ja a `t3`,`t1`; surt a `t2`,`t3` | **FRAGMENT** |
| 6 | `L3.qmd:184` | `exr-compta-caracter` | `.data` amb `w`, `_start`, syscall 93 | **PROGRAMA — no tocar** |

El cas 6 no era a la llista de l'usuari i és el contraexemple que valida el
discriminador: té `.data`, `_start` i sortida, és el lliurament `s3_3_1.s`
(taula de `L3.qmd:18`) i `verifica_laboratoris.py` el classifica com a
ASSEMBLA / EXECUTA FINS AL FINAL. Els cinc d'E4 no són lliurables ni
executables sols.

**Límits d'instruccions redactats com «menys de N»**: cap als cinc casos.
Ordre: `git grep -in "menys de [0-9]\|com a màxim [0-9]\|no més de [0-9]\|màxim de [0-9]" -- '*.qmd'`.
Els límits del corpus són:

- `E2.qmd:151` «no més de 12 línies» i `E3.qmd:45` «no més de 6 instruccions»
  — forma «no més de N», **inclusiva i correcta**, no és «menys de N».
- `L3.qmd:51` «com a màxim 4 instruccions» — ja convertida a la passada B.
- La resta de resultats són «menys de 32 bits» i «menys de 5 línies»
  (`13_contrib.qmd:849`), que no són límits d'enunciat.

Conclusió: **no hi ha cap «menys de N» a convertir**. La feina de 2a es
redueix a la redacció «programa» → «fragment» als cinc casos d'E4.

### 2b — `void main()` vs. `int main`

**Ordres**: `git grep -oh "int main" -- . | wc -l` → 26;
`git grep -oh "void main" -- . | wc -l` → 23; `git grep -n "int main" -- .`
per a la llista.

Dels 26, **3 no són blocs de codi C a convertir**:

- `13_contrib.qmd:404` — `int main() { return 0; }` dins la prosa que
  exemplifica què va en format codi. No és codi del corpus.
- `TODO/L2_tasques.md:162` i `TODO/T4_P_tasques.md:232-234` — registres.

Queden **23**, que és exactament la xifra de l'usuari.

**Dos casos on el context suggereix que `int main` hi és a posta:**

| Ocurrència | Per què |
| :--- | :--- |
| `A2.qmd:859` | Dins `@tip-forcar-error-tipus`. És **codi C real que es compila de debò**: l'acompanya l'ordre `gcc codi_erroni__gcc_tipus.c -Wall -Wextra -Wpedantic` i la sortida literal del compilador, que cita «In function ‘main’». Té `return 0;`. És `int main(void)`, la forma de l'estàndard. Canviar-lo a `void main()` faria que l'exemple deixés de ser reproduïble amb `-Wpedantic` i contradiria la justificació que el bloc 3 ha de redactar (la qual diu que en C allotjat sí que cal `int main`). |
| `E3.qmd:661` + `S3.qmd:685` | `@exr-p4-compilacio-relocacio`. L'exercici **tracta del flux de compilació**: `a.c`/`b.c`, fitxers `.o`, símbols externs, enllaçat. `int main() { return f(x); }` retorna un valor i el `return` és el que fa visible la referència externa a `f` i a `x`. Aquí el C **no** és notació per traduir a mà: és l'objecte d'estudi. |

Nota: `E3.qmd:661` i `S3.qmd:685` són **el mateix bloc reproduït dues vegades**
(enunciat i solució); si es decideix excloure'l, s'han d'excloure tots dos.

**Comprovació que sosté el criteri**: dels 23, **només aquests 2 blocs
contenen un `return`** dins de `main`. Verificat llegint els 14 restants amb
`awk` sobre les 14 línies següents a cada ocurrència. Els altres 21 són
notació d'un programa que l'alumne tradueix a mà, sense valor de retorn.

**Cas a vigilar**: `E4.qmd:247` i `S4.qmd:351` van ser harmonitzats
**cap a `int main`** per `TODO/T4_P_tasques.md §4.3`, que prenia E2/E3 com a
precedent. Si ara s'unifica cap a `void main()`, aquella decisió es reverteix.
No és contradicció —aleshores no existia la justificació que el bloc 3 ha
d'escriure— però convé que consti.

**Pendent de veredicte de l'usuari**: si els 23 o si 21 (excloent A2 i el
parell E3/S3).
