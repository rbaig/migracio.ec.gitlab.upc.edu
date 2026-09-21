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

### Un ús que `13_contrib.qmd` no preveu — decisió pendent

Els marcadors `⚠️ codi_erroni__*.c ⚠️` i
`⚠️codi_erroni__alineacio_incorrecte.s⚠️` **no són ni llenguatge ni context**:
són una marca semàntica de «codi deliberadament incorrecte». La taula de
`13_contrib.qmd §Blocs de codi` no en preveu la categoria.

**Cal decidir si mereixen fila pròpia.** No s'ha tocat res.
