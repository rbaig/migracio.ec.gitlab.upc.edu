# Regles de les escombrades

Una **escombrada** és tota cerca que pretén mesurar el corpus sencer: comptar
ocurrències d'una forma, localitzar tots els casos d'una convenció o sostenir
una afirmació sobre el conjunt. `25_scripts/escombrada.sh` aplica les regles
que no demanen judici (`--help` diu quines). Cada regla porta el cas que la va
originar, en una línia; el relat sencer és a git (`git show
arxiu/pre-neteja-2026-10-14:.claude/skills/escombrada/regles.md`).

**1. `git grep`, mai `grep -r`**, amb el pathspec `':!TODO.md'`, o la mesura
s'inclou a si mateixa. `git grep` només veu fitxers versionats i exclou els
generats (`auto_riscv/`, `_book/`) sense haver-hi de pensar. **`git grep -c`
compta línies, no ocurrències**: per comptar, `git grep -o … | wc -l`. Una
exclusió per ruta caduca amb la ruta: quan un fitxer es mou, les mesures que
l'excloïen s'han de migrar. Cas: l'escombrada de `desplacament-arithmetic`, amb
`grep -r` a dues carpetes, va deixar la quarta ocurrència a `11_riscv.qmd`
(`953edca`).

**2. Mesureu per forma, no per nom.** Cas: el que RARS rebutja és l'expressió
aritmètica a l'operand, no `NC*4`; el patró pels noms donava 20 i 5 línies, i
per forma eren 11 i 27, amb una secció sencera de `S4.qmd` fora (`c2a9171`,
`45f6cc2`).

**3. Cap afirmació «és l'únic» o «no n'hi ha cap» sense l'ordre exacta que la
sosté** i sense haver llegit el fitxer o el bloc sencer, tampoc si arriba ja
mesurada d'un encàrrec o d'un registre.

**4. El patró ha de cobrir totes les formes i tots els tipus de fitxer**:
majúscules incloses (`-i`), i no només els `.qmd`. Cas: «simple precisió» va
deixar sis capçaleres en majúscula a `A5.qmd` i `S5.qmd`, i nou ocurrències als
SVG i a `24_specs/registres.toml`.

**5. Per afirmar res sobre l'historial, pregunteu a l'historial**, no a l'arbre
de treball: `git log -S'<fragment>' -- <fitxer>` (qui el va treure i per què),
`git log --all -- <ruta>` (si hi va ser mai) i `git show <commit>~1:<fitxer>`
(si una còpia antiga és l'estat previ a un commit: si coincideix byte a byte,
totes les diferències són aquell commit). Cas: una línia sobre `fcvt.w.s` que
semblava una millora era una correcció retirada a posta perquè era incorrecta
(`92345e4`); i `rars1_6.jar`, que «no hi havia estat mai», va ser al repositori
fins a `fbf7c3d`. Dels registres de revisió d'abans del 2026-09-22
(`git show a211bbf:<ruta>`), no en citeu cap resum: citeu la secció de l'ítem i
comproveu-la al corpus.

**6. Quan trobeu un cas d'una forma, escombreu la forma**, no el nom ni la línia.
Cas: l'escombrada de `startup.s` pel nom no va veure el bloc `.globl main` /
`main:` / `ret` del callout de bones pràctiques, que no diu «startup»
(`c2a9171`).

**7. Abans d'afirmar que una línia arriba a l'alumne, comproveu `_quarto.yml`**,
i escombreu sempre el font, no la sortida: un fitxer comentat als `chapters:` és
del projecte (`CLAUDE.md §Abast del projecte`), i `13_contrib.qmd` és només HTML.
Cas: l'únic «TODO» escrit com a text de llibre era a un fitxer no renderitzat,
i cap escombrada del `_book/` no el veia.

**8. Un marcador dins del corpus és una còpia.** Abans de fer-lo desaparèixer, o
de retirar una entrada del `TODO.md`, comproveu on en queda còpia i digueu-ho; si
no n'hi ha cap, copieu-lo abans, al mateix commit. Cas: el bloc comentat d'`A2.qmd`
amb un bolcat de RARS que no era enlloc més (`cef40b1`).

**9. Verifiqueu contra la llista de canvis aprovats i sobre l'arbre de
treball**, mai contra el fitxer d'on heu copiat: si s'ha acordat un afegit que
no és a la font, la igualtat amb la font és una alarma. Cas: un paràgraf aprovat
el mateix dia, esborrat en aplicar un extret i restaurat (`f136762`, `7f0703c`,
`8b9f82d`).

**10. Una escombrada amb la sortida truncada no sosté cap negació.** `| head`,
`-m N` o qualsevol límit donen una mostra («n'hi ha almenys N»); una negació
demana l'ordre sencera, comptada amb `| wc -l`. Cas: un `| head -5` va fer
concloure que `#wrn-mul-modul-2n` no existia, i era a `A4.qmd`, més avall.

**11. Una xifra només és certa respecte del commit on es va mesurar**: dateu les
que publiqueu, i quan dues lectures discrepen, la primera pregunta és **quan**
(`git show <commit>:<ruta>`). Cas: 19 i 26 pathspecs al `TODO.md`, totes dues
certes, amb un bloc de feina entremig.

**12. Una afirmació d'absència ha d'excloure els fitxers que documenten el
cas**, que en contenen cites, no ocurrències: `TODO.md`, `13_contrib.qmd`,
`24_specs/registre_de_decisions.md` i `.claude/`. L'exclusió s'explica, no
s'amaga: si l'ordre amb l'exclusió encara no reprodueix la xifra, el que s'ha de
corregir és l'afirmació, no el pathspec. Cas: `00c000ef`, l'única ocurrència
que en quedava era l'ordre que en comprovava l'absència.

```bash
git grep -c "00c000ef" -- . ':!TODO.md' ':!13_contrib.qmd' ':!24_specs/registre_de_decisions.md' ':!.claude/'
```

**12 bis. Un desglossament s'ha de poder sumar al total que acompanya**, i porta
l'ordre que el reprodueix, com el total. Un total correcte no avala les parts.
Cas: el repartiment de `_start` sumava 91 contra un total de 104, amb quatre
valors dolents, i el total sí que reproduïa (2026-09-23).

**13. Una afirmació sobre branques diu de quin remot parla i es mesura amb
`git ls-remote`**: `git branch -r` és la vista guardada del clon, i GitLab
(`origin`) i el mirall de GitHub (`mirror`, amb la branca `build` del CI) no
tenen les mateixes branques. Una referència obsoleta es poda
(`git fetch --prune`), no es registra. Cas: `build` declarada inexistent mirant
només GitLab, i dues branques declarades existents des de referències obsoletes.
