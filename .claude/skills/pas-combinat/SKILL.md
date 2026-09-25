---
name: pas-combinat
description: Pas combinat d'un fitxer d'enunciats o de solucions d'EC (Ex.qmd o Sx.qmd) —adaptació als Ax.qmd resultants de la revisió interna i revisió interna pròpia—, per fases amb aturades.
argument-hint: "<E1–E9 | S1–S9>"
disable-model-invocation: true
---

# Pas combinat de `$ARGUMENTS`

- `E<x>` → `02_exercicis/E<x>.qmd`; `S<x>` → `03_solucions/S<x>.qmd`.
- Referències: la parella del mateix tema (l'enunciat o la solució) i `01_apunts/A<x>.qmd`.

Si l'argument no és un d'aquests, o si `CLAUDE.md §Estat dels materials` no llista el fitxer com a pendent del pas combinat, atura't i digues-ho. `E3.qmd` i `S3.qmd` ja estan fets.

⚠️ **T4, T5 i T6 són en revisió externa** a la branca `temes456` (`CLAUDE.md §Estat dels materials`). Abans de tocar `E4`–`E6` o `S4`–`S6`, pregunta com s'ha de coordinar amb el grup de treball.

## Procediment

Segueix `26_prompts/Ax_Ex_Px__revisio_interna__plantilla.md`. Els **aspectes a revisar** i les **fases A, B i C, amb les seves aturades**, valen tal com hi són escrits, llegint `L{N}.qmd` com el fitxer d'aquest pas. La plantilla és per a claude.ai, i aquí en canvien cinc coses:

1. **Fitxers**: llegeix-los del repositori local. No els baixis de `raw.githubusercontent.com`: el mirall va uns minuts endarrerit i no té els canvis que no s'han pujat.
2. **Configuració**: no hi ha cap interruptor de *Thinking*. El model i l'effort de cada fase surten de `CLAUDE.md §Model i effortness`; si la configuració activa no hi correspon, atura't i digues quina cal. Les verificacions de xifres i les escombrades de la Fase B es poden delegar a l'agent `auditor-xifres`, i la revisió lingüística a `revisor-linguistic`: cadascun porta el model de la seva fila de la taula.
3. **Llista de tasques de la Fase B**: no s'ofereix per descarregar. Presenta-la a l'aturada i, si s'ha de desar, pregunta on: el directori `TODO/` no ha de tornar (vegeu la capçalera del `TODO.md`).
4. **Canvis**: no s'ofereixen fitxers. Un commit per bloc confirmat, amb push a `origin`, en el format de `13_contrib.qmd §Commits` (`CLAUDE.md §Flux de treball`).
5. **Exhauriment del xat**: la secció final de la plantilla no s'aplica. El punt de represa és l'últim informe d'aturada i l'últim commit.

El bloc «Estat de la Revisió interna» i les preguntes 1 i 5 de la plantilla (configuració activa) són una instantània antiga: l'estat vigent és a `CLAUDE.md §Estat dels materials` i al `TODO.md`.

## Tancament

Les preguntes 2–4 de la plantilla —si es dona per tancada la revisió pedagògica, la tècnica i la lingüística— es fan en acabar la Fase C. La resposta és una **declaració de l'usuari**: es registra tal com la fa, no es verifica (`CLAUDE.md §Estat dels materials`).
