#!/usr/bin/env bash
# PreToolUse (Bash): les comprovacions de 13_contrib.qmd §Commits abans de cada
# `git commit`.
#   1. `make render` ha d'acabar net; si no, el commit no passa (sortida 2).
#   2. Revisió de prosa de les línies afegides (25_scripts/lint_prosa.py).
#   3. Si el canvi toca el PDF, `make render-complet` és obligatori
#      (13_contrib.qmd §Verificació de l'entorn), i un render HTML no ho exercita.
# Els punts 2 i 3 no bloquegen: demanen confirmació a l'usuari («ask») amb el motiu.
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
[ -f "$arrel/_quarto.yml" ] || exit 0
cd "$arrel" || exit 0

# 1. Render HTML.
if ! sortida=$(make render 2>&1); then
  {
    echo "make render ha fallat i el commit no es fa (13_contrib.qmd §Commits). Darreres línies:"
    printf '%s\n' "$sortida" | tail -n 30
  } >&2
  exit 2
fi

avisos=""

# 2. Prosa de les línies afegides.
if ! prosa=$(python3 25_scripts/lint_prosa.py 2>&1); then
  avisos+="Revisió de prosa (25_scripts/lint_prosa.py), només línies afegides:"$'\n'"$prosa"$'\n\n'
fi

# 3. Canvis que depenen del PDF.
fitxers=$( { git diff HEAD --name-only; git ls-files --others --exclude-standard; } | sort -u)
pdf=""
rutes=$(grep -E '^(preamble\.tex|_quarto\.yml|22_figs_originals/|23_figs_externes/|24_specs/)' <<<"$fitxers")
[ -n "$rutes" ] && pdf+="- fitxers: $(tr '\n' ' ' <<<"$rutes")"$'\n'
qmd=$(grep -E '\.qmd$' <<<"$fitxers")
if [ -n "$qmd" ]; then
  linies=$( { git diff HEAD -U0 --no-color -- '*.qmd' | grep -E '^[+-][^+-]';
              git ls-files --others --exclude-standard -- '*.qmd' | xargs -r cat; } )
  for forma in 'when-format' 'tbl-colwidths' '#fig-' '!\[' '\$'; do
    grep -qE -- "$forma" <<<"$linies" && pdf+="- forma «${forma//\\/}» a les línies canviades"$'\n'
  done
fi
if [ -n "$pdf" ]; then
  avisos+="Aquest canvi pot afectar el PDF, i «make render» no l'exercita. Abans del commit cal «make render-complet» (13_contrib.qmd §Verificació de l'entorn). Motius:"$'\n'"$pdf"
fi

if [ -n "$avisos" ]; then
  jq -n --arg r "$avisos" \
    '{hookSpecificOutput: {hookEventName: "PreToolUse", permissionDecision: "ask", permissionDecisionReason: $r}}'
fi
exit 0
