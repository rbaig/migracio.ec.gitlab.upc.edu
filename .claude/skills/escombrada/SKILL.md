---
name: escombrada
description: Mesura el corpus d'EC (comptes, repartiments per fitxer, afirmacions «no n'hi ha cap» o «és l'únic») amb 25_scripts/escombrada.sh. Carrega-la abans de publicar qualsevol xifra o afirmació d'absència o d'unicitat sobre el repositori —al TODO.md, a 13_contrib.qmd, al registre de decisions, en un missatge de commit o en un informe— i abans de retirar una entrada del TODO.md perquè «ja no hi és».
---

# Escombrada del corpus

Les regles són a `regles.md`, en aquest mateix directori, i cadascuna porta el cas que la va originar. **Llegeix-lo sencer abans de la primera escombrada de la sessió.** Aquest fitxer no les copia: una còpia paral·lela divergiria en silenci.

## L'ordre

```bash
25_scripts/escombrada.sh [--cas] [-F] [-w] [--commit <c>] [--tot] <patró> [-- <pathspec>...]
```

`25_scripts/escombrada.sh --help` en dona el detall. Cada execució escriu:

- el commit i la data de la mesura, i si l'arbre de treball tenia canvis no confirmats;
- quins fitxers exclou i per què;
- el repartiment per fitxer, amb la comprovació que suma el total;
- l'ordre `git grep … | wc -l` que ho reprodueix.

Mecanitza les regles **1, 4, 10, 11, 12 i 12 bis**. Per defecte no distingeix majúscules, cobreix tots els tipus de fitxer versionats i exclou els fitxers que documenten els casos (regla 12): `TODO.md`, `13_contrib.qmd`, `24_specs/registre_de_decisions.md` i `.claude/`. Les opcions ho canvien i la capçalera de la sortida ho diu.

## En publicar una xifra

Copia-hi la línia `Ordre:` i la data o el commit de la línia `# Mesura:`. Una xifra sense l'ordre que la sosté no es pot verificar, només reproduir (regla 11).

- Si l'script acaba amb `✗` (el repartiment no suma el total), atura't: no publiquis cap de les dues xifres.
- Si una xifra no coincideix amb una de publicada, la primera pregunta és **quan**: torna-la a mesurar amb `--commit` al commit on es va publicar.
- Si trobes ocurrències als fitxers exclosos que no són cites, l'afirmació és la que està malament, no l'exclusió (regla 12, ⚠️).

## El que l'script no fa

Les regles **2, 3, 5, 6, 7, 8, 9 i 13** demanen judici i continuen sent teves: tria del patró, lectura del bloc sencer, preguntes a l'historial, fitxers comentats a `_quarto.yml`, còpies dels marcadors, contrast amb la llista de canvis aprovats i branques de cada remot. Llegeix-les a `regles.md` abans d'afirmar res que en depengui.
