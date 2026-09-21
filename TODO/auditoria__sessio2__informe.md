# Auditoria — informe de la sessió 2 (executar)

Fitxer **transitori**. S'esborra en tancar l'auditoria.

Sessió 2026-09-21. Model: Opus 5. Base: `c295b8b`.
Commits de la sessió: `c2a9171`, `cef40b1`, `4031179`.

**Aquesta és la primera sessió que esborra contingut del corpus.** 92 línies
eliminades en 5 fitxers, totes autoritzades una a una i totes precedides de la
seva llista de comprovacions.

---

## El mètode que ha salvat la sessió, primer

L'encàrrec afirmava, sobre D4:

> `.space NF*NC*4` és una expressió aritmètica a l'operand i RARS no
> l'assembla. Ho he verificat: és l'únic cas que queda a tot el corpus.

**Era fals**, i l'informe de la sessió 1 ja ho deia a §1c D4 («`A4.qmd`
❌ **Intacte: 20 línies**»). L'encàrrec i l'informe es contradeien, i l'informe
tenia raó: hi ha **20 línies vives a A4 i 5 a S4**, comprovades una a una i
totes fora de comentari HTML.

El que ho va aturar va ser **llegir l'informe contra l'encàrrec en comptes
d'executar l'encàrrec**. Si s'hagués corregit només `:529`, el fitxer hauria
quedat amb un literal enmig de 24 expressions supervivents: més incoherent que
abans de tocar-lo.

> ⭐ **Regla nova.** Quan l'encàrrec afirma un fet verificable del corpus
> («és l'únic», «no n'hi ha cap»), **es verifica abans d'executar-lo**, encara
> que vingui amb la mesura al costat. Una mesura pot no mesurar el que afirma:
> aquí el patró de cerca només podia trobar `.space` i se'n va concloure «cap
> altre cas a tot el corpus».

I una segona, de la mateixa parada: **les meves tres opcions de sortida també
partien d'una premissa falsa.** Proposaven literalitzar `la t3, mat + 72`, i
això tampoc no assembla — `#cau-rars-la-offset` (`L2.qmd:343`) documenta que
RARS no suporta `la rd, etiqueta+desplaçament` en cap forma. Qui va detectar
l'error de les opcions va ser l'usuari, amb el mateix procediment: contrastar
la proposta contra el que el corpus ja tenia escrit.

---

# Les 🔴

## D4 — reduïda a una sola acció

**Decisió de l'usuari**: l'exempció teoria/laboratori que `#cau-rars-la-offset`
ja estableix per a `la` **s'estén a l'aritmètica als operands**. A4 i S4 són
teoria; les seves expressions són notació d'adreçament i la secció ensenya
precisament que `NC*4` és un invariant.

| Element | Acció |
| :--- | :--- |
| 20 línies `li tX, NC*4` / `NC*2` d'A4 i les de S4 | **No es toquen** |
| Línies `la` amb desplaçament (A4, S4) | **No es toquen** (`#cau-rars-la-offset`) |
| `A4.qmd:529` (`.space NF*NC*4`) | **No es toca** — vegeu sota |
| Remissió a `@nte-rars-operands-literals` | **Afegida** a A4 i a S4 |

### Per què `A4.qmd:529` tampoc no canvia

L'encàrrec demanava fer-lo convergir amb `A2.qmd:465` (`.space 120`). Dos fets
del fitxer ho impedeixen, i tots dos es van comprovar abans de proposar res:

1. **A4 no defineix `NF` ni `NC` enlloc.** L'única menció d'`.eqv` al fitxer és
   `@imp-eqv-dimensions`, que **recomana** definir-les sense fer-ho. No hi ha
   cap literal a escriure sense inventar valors.
2. **El bloc és la traducció d'`int mat1[NF][NC];`** (`A4.qmd:504`), que tampoc
   no compila sense dimensions. Declarar trencat l'assemblador i sana la C,
   tres línies més amunt, seria incoherent.

I la clau que ho tanca: **el que fa canònic el bloc d'A2 no és el `120`, sinó
que el `120` hi és derivable**, perquè les `.eqv NF, 5` / `.eqv NC, 6` són a
sobre. A A4 un literal seria un número sense procedència, just abans d'un
callout que recomana les constants que el bloc no té.

**Les remissions afegides:**

- `A4.qmd` — dins `@imp-eqv-dimensions`, que és l'ancoratge natural: és el
  callout que recomana les constants la aritmètica de les quals RARS rebutja.
- `S4.qmd` — al capdamunt de `## Matrius`, seguint el patró que `S2.qmd:631` ja
  havia establert per al mateix problema.

Àncores verificades: `@nte-rars-operands-literals` (`A2:451`) i
`@imp-ec-la-offset` (`A2:600`). Abans d'aquesta sessió el callout només es
referenciava des de `L4.qmd:94`; ara també des de la teoria i el solucionari,
que és el forat que el `TODO.md` preveia des del principi.

## D1 — la contradicció de `13_contrib.qmd:204`, retirada

La nota deia «pendent d'aplicar a L3» al costat de la regla mateixa.

**Verificació pròpia, no heretada.** Es va comprovar programàticament l'ordre
de les etiquetes a **tot el laboratori**, no només a L3:

```
Blocs amb .text i _start a L1–L6: 25
Infraccions: 0
```

Tres blocs de `.text` **sense** `_start` (`L2:511`, `L5:106`, `L5:239`) van
aparèixer al primer escombrat i **no són excepcions**: són fragments o fitxers
de subrutina sola (`abs`, `descompon`). La regla és d'ordre intern i no els
aplica. Anotat, perquè el proper que faci l'escombrada els tornarà a trobar.

Retirada als tres llocs: `13_contrib.qmd:204`, `TODO.md:115`,
`L5_tasques.md:99`.

**Una troballa de passada:** el caveat de l'informe deia que `L3:357` continua
sent l'únic `ERROR E1` del verificador. **Ja no ho és.** El verificador dona
exit 0 i el classifica com a `INCOMPLET PER DISSENY | OK`. El caveat també
havia caducat.

## Els quatre blocs de `startup.s`

Decisió del 19/07 (assignatura, tots els professors), mai executada.

### Llista de comprovacions de supressió, bloc a bloc

**Ancoratges.** Cap dels que desapareixen tenia cap remissió viva:

| Ancoratge | Remissions | On eren |
| :--- | ---: | :--- |
| `#imp-programa-esquelet` | 0 | — |
| `#wrn-so-start` | 0 | — |
| `#tip-rars-main-multinivell` | 0 | — |
| `#imp-exception-handler` | 3 | **Totes dins dels blocs eliminats** (A1:40, A2:770, A3:1541, index:147/160) |

`#nte-programa-esquelet` estava **duplicat**: la còpia comentada (`:746`) va
desaparèixer amb el bloc i **el viu de `:730` queda**, amb les seves 6
referències intactes (A3, A9, S9, L1×2, L2). Confirmat com demanava l'encàrrec.

**Dades.** Bloc a bloc, el que contenien que no fos la instrucció obsoleta:

| Bloc | Dades | Existeix enlloc més? |
| :--- | :--- | :--- |
| `A1:39-40` | cap | — |
| `A3:1541-1550` | La regla de preservar `ra` a les multinivell | ✅ **Sí** — `A3:1552`, viva, just a sota del bloc |
| `index:147-151`, `:160-167` | Passos de configuració de l'*Exception Handler* | Únics, però són instruccions d'ús del mecanisme exclòs |
| **`A2:744-810`** | **Bolcat de codi màquina** (`0x00c000ef`, `0x00a00893`, `0x00000073` + desassemblat), flux `_start → main → exit → _exit`, codi de `startup.s` | ❌ **NO** — `git grep -c "00c000ef" -- . ':!TODO/'` → només A2 |

**El bloc d'A2 era el cas que la regla nova preveia.** Les dades es van copiar
a `TODO.md §Decisions obertes`, a l'entrada de la decisió que les exclou, abans
d'eliminar res. Verificat després: les 7 cadenes úniques hi són totes.

Un detall que l'inventari va destapar: l'enllaç d'`index.qmd` apuntava a
`04_laboratori/startup.s`, **que no existeix al repositori**. Si algú hagués
reactivat el bloc, l'enllaç hauria estat trencat.

---

# Les 🟠 i 🟡

| # | Acció | Resultat |
| ---: | :--- | :--- |
| 1 | `A2:717-721` — `main:`→`suma:`, `.globl main`→`.globl suma`, `add t0`→`add a0` | ✅ Convergeix amb `A1:205-208` |
| 3 | `E9:72` i `S9:201` → `li a7, 93` | ✅ A S9 s'hi ha afegit `li a0, 0`, que `exit2` demana |
| 5 | `S_criteris_seleccio.qmd:19` | ✅ Nota neutra; era l'únic «TODO» escrit com a contingut |
| 6 | `A9:575` — addició al catàleg | ✅ El servei 10 es queda documentat; s'hi afegeix que a EC la sortida es fa amb `exit2` |
| 8 | `A3:2053` — callout `#cau-carrega-ec` | ✅ **Reescrit** — vegeu sota |
| 11 | `13_contrib.qmd:189` — «del hardware» → «del maquinari» | ✅ |
| 14 | $V^2$ (A7) vs. $V_{CC}^2$ (A6) | ✅ **Verificat i corregit a A7; S6 registrat** — vegeu sota |
| 16 | `A2:1720` — remissió pendent | ✅ Ara remet a `@sec-memoria-t2` |
| 15 | `#nte-programa-esquelet` duplicat | ✅ Resolt sol amb la supressió del bloc 2 |
| 17 | `T4_multiplicador_sequencial.png` | 📋 Registrat, no eliminat (binari, fora d'abast) |

## El callout d'A3, reescrit a mitja sessió

La redacció de l'informe deia que a EC els programes «no s'inicien per una
crida a `main`». **L'usuari va detectar que xoca amb el `void main()` que EC
usa a tots els programes en C.** Tenia raó, i la solució era al corpus mateix:
`#cau-void-main` (`A2:2022`) diu que aquell `main` és **notació**, no codi que
es compili.

El callout final té dos paràgrafs: el primer manté la negació (sense la frase
del `main`), i el segon la resol explícitament remetent a `@cau-void-main`.
Així els dos callouts es reforcen en lloc de contradir-se.

## La $V$ de la potència dinàmica: verificat, i la troballa és més gran

L'informe deixava el punt sense verificar. Fet:

| Lloc | Notació | Acció |
| :--- | :--- | :--- |
| `A6.qmd:278` (`@eq-potencia-dinamica`) | $V_{CC}^{2}$ | Font de veritat |
| `E6.qmd:192` | $V_{CC}$ | Concorda amb A6 |
| `A7.qmd:113` | $V^2$ | ✅ **Corregit** |
| **`S6.qmd:324`** | $V^2$ | ❌ **No tocat** — vegeu sota |

L'escombrada va destapar un tercer cas que l'informe no citava: `S6.qmd:324`.
**No s'ha harmonitzat**, i el motiu és el mateix criteri que va aturar D4:
S6 usa $V$ **de manera consistent dins de tota la seva derivació**
($C = P_{din}/(V^2 \cdot f)$, $V_A^2$, els dos càlculs de $C_A$ i $C_B$).
Canviar-hi només la línia que cita l'equació el deixaria incoherent amb el seu
propi desenvolupament: l'harmonització de S6 s'ha de fer **sencera o no
fer-se**, i això fa que la parella E6/S6 no concordi. Registrat a `TODO.md §T6`.

A `A7:113` també s'hi ha canviat la remissió: citava `@sec-potencia-dinamica`
(la secció) i ara cita `@eq-potencia-dinamica` (l'equació), com ja fa `A6:354`.

---

# Verificació

| Comprovació | Resultat |
| :--- | :--- |
| `make render` | **Cap warning** |
| `?@` recursiu a `_book/` (39 fitxers HTML) | **0** |
| `?@` a `Estructura-de-computadors.tex` | **0** |
| `?@` al PDF | **0** |
| Formes `?sec-`/`?fig-`/`?tbl-` sense arrova | **0** |
| `verifica_laboratoris.py` | **exit 0**, 0 `ERROR` |
| Ancoratges penjats després de les supressions | **cap** |
| Dades úniques del bloc d'A2 preservades | **7/7 al `TODO.md`** |

**Escombrada de pèrdues** sobre els commits de la sessió: 36 línies eliminades
de ≥ 25 caràcters sense rastre a l'arbre. **Totes** pertanyen als quatre blocs
autoritzats o als marcadors eliminats amb permís; **cap no conté dades**. Les
dades úniques que hi havia són al `TODO.md`, i la comprovació ho confirma
cadena a cadena.

**Marcadors al corpus: 38 → 29.** Els 29 que queden són els 9 falsos positius
de `13_contrib.qmd` (metavariables, remissions i la regla de commit), les
decisions vives que no pot prendre Claude Code i els pendents ja registrats.

---

# El que queda obert per a la sessió 3

**Decisions vives registrades aquesta sessió** (no es podien executar):

| Entrada | Lloc |
| :--- | :--- |
| Verificació de la taula d'alineació contra l'ABI `ilp32` i el BA | `TODO.md §T2` (nova) |
| Decisió de contingut a `#cau-boolea-c` | `TODO.md §T3` |
| Harmonització de $V$/$V_{CC}$ a S6, i la parella E6/S6 | `TODO.md §T6` |
| `T4_multiplicador_sequencial.png` (63 KB, no referenciat) | `TODO.md §SVG` |

**Entrada marcada com a caduca**: `TODO.md §T3` demanava revisar la remissió
`@imp-exception-handler` del callout `#tip-rars-main-multinivell`. El callout
ja no existeix.

**Punt 10 (l'alineació de `.dword` a RARS, `L2.qmd:156-166`) no s'ha tocat.**
És una decisió viva, no una instrucció obsoleta, i el seu bolcat comparatiu
MARS/RARS segueix sent l'única còpia d'aquelles dades al corpus. Quan la
sessió 3 el resolgui, **les línies `:164-166` s'han de preservar**, igual que
s'ha fet amb el bolcat d'A2.

La sessió 3 reescriu el `TODO.md` a partir del que queda.

---

## Les regles que aquesta sessió deixa escrites

1. ⭐ **Un fet verificable afirmat a l'encàrrec es verifica abans d'executar-lo**,
   encara que vingui amb la mesura al costat. Una mesura pot no mesurar el que
   afirma. (D4: el patró només trobava `.space` i se'n va concloure «l'únic cas
   de tot el corpus»; n'hi havia 25.)
2. **Quan la correcció d'una incoherència en crearia una altra, no es fa a
   mitges.** S6 usa $V$ en tota la seva derivació: harmonitzar-ne una sola
   línia seria pitjor que deixar-lo. Val igual per a A4 amb les `.eqv`.
3. **Abans d'eliminar un bloc, l'inventari del que conté va a l'informe**, i el
   que no existeixi enlloc més es preserva **abans** de la supressió, no
   després. (El bolcat d'A2 no existia enlloc més.)
4. **Un ancoratge amb remissions no bloqueja la supressió si les remissions són
   dins dels blocs que també s'eliminen.** `#imp-exception-handler` en tenia 3 i
   totes tres van desaparèixer amb els seus blocs; calia comprovar-ho una a una.
