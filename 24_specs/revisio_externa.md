# Revisió externa d'A1–A8: nota per als equips

> **Esborrany del 2026-10-12** (fase 8 de `CLAUDE.md §Pla de treball`), pendent que l'editor el revisi abans d'enviar-lo. Els equips i el calendari els decideix l'editor.

## Abans de començar

- **Partiu de `main` d'avui.** Des del 2026-10-06, quan es va declarar l'abast de la revisió (A1–A8), tots els fitxers han canviat (taula de sota). Una còpia d'abans no serveix de base.
- **Una branca per equip**: `revisio/<grup>-t<N>-t<M>`, creada des de `main` i actualitzada amb `main` periòdicament (`13_contrib.qmd §Convenció de noms de branques`). Al final, una *Merge Request* a `main`. El push directe a `main` és només per a l'editor (`§Push directe a `main``).
- **Les regles són a `13_contrib.qmd`** (el capítol «Contribueix-hi» del llibre), curtes i sense historial. El perquè de cadascuna, i qui la va decidir, és a `24_specs/registre_de_decisions.md`: abans de proposar de canviar una regla, llegiu-ne l'entrada.
- **Abans de cada commit, `make comprova`** (`§Comprovacions per nivells`): mira el que heu canviat i, si cal, renderitza. Els hooks de git opcionals ho fan sols (`make instal·la-hooks`). Cada push d'una branca passa `make comprova-branca` al mirall de GitHub (`§Les branques, al mirall de GitHub`).
- **No editeu a mà el que es genera**: `auto_figs/`, `auto_riscv/`, `_book/`, les variants `_dark.svg` de les figures, la secció «Termes» de `12_sigles_simbols.qmd` (`make glossari`) i els SVG dels generadors de model (a) (`make registres`).
- **Una errada del material publicat**: una *issue* amb l'etiqueta `errada` (`§Errades del material publicat`, D-96).

## Convencions noves des del 2026-10-06

Totes són a `13_contrib.qmd`; aquí només hi ha la llista, perquè sapigueu què ha canviat. Entre parèntesis, l'entrada del registre.

- **Llenguatge**: les sigles, sense plural (D-79), amb l'article segons com es llegeixen (D-80), i expandides només a la primera aparició del llibre (D-89); un espai que no es parteix entre el nombre i la unitat o el % (D-87); el lèxic anglès–català, el del glossari de termes, que n'és l'única font (D-88, D-100, D-108); formes que no s'han de fer servir, que `make comprova` atura (D-105, D-106); noms de persona (D-107); adjectius darrere del nom (D-72); «imbricat», «lectura/escriptura», «ròssec», «coma flotant», «farciment», «multinucli» (D-34 a D-38).
- **Codi**: els comentaris del C, amb `//` i línia per línia (D-83); l'operand de memòria, sempre `desplaçament(base)` (D-84); cap etiqueta ni constant `b` o `B` (D-111); les taules de pseudoinstruccions, amb un sol esquema (D-66); els formats d'instrucció, on es presenta cadascun (D-5); Zifencei, fora d'EC (D-77); les convencions d'EC no penalitzen a l'avaluació (D-85).
- **Format**: cap callout dins d'un altre (D-110); una taula amb `#tbl-` porta peu (D-102); els punters cap endavant permesos (D-70, D-78).
- **Figures**: el nom, pel fitxer que la consumeix (`A<N>_`, D-76); el `<desc>` és el text alternatiu (D-51); les vores entre zones, per dins (D-99); els originals substituïts es conserven a `22_figs_originals/conservats/` (D-68).

## Estat de cada fitxer

Revisió interna: tancada per a tot A1–A8 el 2026-09-23 (l'editor). Canvis des del 2026-10-06, mesurats el 2026-10-12 sobre `main`:

```bash
for n in 1 2 3 4 5 6 7 8; do echo "A$n $(git log --since=2026-10-06 --oneline -- 01_apunts/A$n.qmd | wc -l) $(git diff --shortstat 7ac2fc9 HEAD -- 01_apunts/A$n.qmd)"; done
```

| Fitxer | Revisió externa anterior | Canvis des del 2026-10-06 | Punts oberts que el toquen (`TODO.md`) |
| :--- | :--- | :--- | :--- |
| A1 | — | 17 commits; +151 −133 | Exemples plegables a l'HTML: A1 n'és el pilot (D-90) |
| A2 | — | 35 commits; +456 −433 | §T2: `#sec-punters` i `#sec-vectors`, el que la revisió del 2026-10-12 no va aplicar (decisió de l'editor); remissions `@lst-` (3) |
| A3 | `!5` (T3), a `main` el 2026-10-01 | 20 commits; +272 −308 | la figura `A3_deps_exemple.svg` (retoc de l'editor); remissions `@lst-` (3) |
| A4 | `!7` (T4–T6), a `main` el 2026-10-01 | 13 commits; +68 −68 | — |
| A5 | `!7` | 20 commits; +102 −97 | Rectes de T5 en una sola figura (prioritat baixa) |
| A6 | `!7` | 17 commits; +57 −57 | La pregunta de productivitat de dos exemples (reunió del 2 de novembre) |
| A7 | — | 17 commits; +234 −238 | — |
| A8 | `!8` (T8), a `main` el 2026-10-06, fins a §8.7 exclosa | 9 commits; +113 −109 | Per al revisor de T8: la condició VIPT de `#sec-mv-vipt`; la branca `tema8` es conserva perquè hi pugui continuar, i li convé incorporar-hi `main` abans |

Afecten tots els fitxers, i encara són oberts: la revisió completa de la norma de lèxic anglès/català i la reducció de la paleta de colors de les figures.
