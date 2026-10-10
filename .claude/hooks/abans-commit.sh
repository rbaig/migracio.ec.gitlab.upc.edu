#!/usr/bin/env bash
# PreToolUse (Bash): abans de cada `git commit`, les comprovacions del nivell del
# canvi (25_scripts/comprova.py; 13_contrib.qmd §Comprovacions per nivells, D-103).
# El nivell es dedueix dels fitxers canviats: als nivells 0 i 1 no hi ha render;
# al 2, `make render`; als 3 i 4, `make render-complet`.
#   - Si alguna comprovació atura el commit (comprova.py surt amb 2: el render
#     falla o dona cap WARNING, un registre desactualitzat, una forma no admesa…),
#     el hook surt amb 2 i el commit no es fa.
#   - Els avisos i els recordatoris (sortida 1) no l'aturen ni pregunten: arriben
#     a Claude (additionalContext) i a l'usuari, a la pantalla (systemMessage) (D-61).
# Les persones que no fan servir Claude Code tenen el mateix amb els hooks de git
# de `.githooks/` (`make instal·la-hooks`).
#
# Es mira l'arbre de treball sencer respecte d'HEAD (més els fitxers nous no
# versionats), no només el que ja és a l'índex: el hook s'executa abans de
# l'ordre, i en un `git add … && git commit` l'índex encara no s'ha actualitzat.

entrada=$(cat)
cmd=$(jq -r '.tool_input.command // ""' <<<"$entrada")

printf '%s\n' "$cmd" | sed -E 's/(&&|\|\||;|\|)/\n/g' \
  | grep -qE '^[[:space:]]*git([[:space:]]+-[cC][[:space:]]+[^[:space:]]+)*[[:space:]]+commit([[:space:]]|$)' \
  || exit 0

dir=$(jq -r '.cwd // empty' <<<"$entrada")
arrel=$(git -C "${dir:-.}" rev-parse --show-toplevel 2>/dev/null) || exit 0
[ -f "$arrel/_quarto.yml" ] && [ -f "$arrel/25_scripts/comprova.py" ] || exit 0
cd "$arrel" || exit 0

sortida=$(python3 25_scripts/comprova.py 2>&1); rc=$?

if [ $rc -eq 2 ]; then
  {
    echo "Les comprovacions aturen el commit (25_scripts/comprova.py; 13_contrib.qmd §Comprovacions per nivells):"
    printf '%s\n' "$sortida" | tail -n 80
  } >&2
  exit 2
fi

if [ $rc -ne 0 ]; then
  jq -n --arg r "$sortida" \
    '{systemMessage: ("Avisos d'"'"'abans del commit:\n" + $r), hookSpecificOutput: {hookEventName: "PreToolUse", additionalContext: $r}}'
fi
exit 0
