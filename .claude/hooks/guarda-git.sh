#!/usr/bin/env bash
# PreToolUse (Bash): dues regles de CLAUDE.md §Flux de treball que no han de
# dependre de la memòria del model.
#   - El mirall de GitHub s'actualitza sol des de GitLab: no s'hi empeny a mà.
#   - Fix-forward: no es reescriu l'historial.
# Sortir amb 2 bloqueja l'ordre, i el text d'stderr arriba a Claude com a motiu.

cmd=$(jq -r '.tool_input.command // ""')

# Cada ordre d'una cadena (&&, ||, ;, |) en una línia pròpia, perquè el patró
# només casi amb ordres que comencen per `git` i no amb el text d'un missatge.
segments=$(printf '%s\n' "$cmd" | sed -E 's/(&&|\|\||;|\|)/\n/g')
git_re='^[[:space:]]*git([[:space:]]+-[cC][[:space:]]+[^[:space:]]+)*[[:space:]]+'

if grep -qE "${git_re}push([[:space:]].*)?[[:space:]]mirror([[:space:]:]|$)" <<<"$segments"; then
  echo "Bloquejat: el mirall de GitHub s'actualitza sol des de GitLab i no s'hi empeny a mà (CLAUDE.md §Flux de treball)." >&2
  exit 2
fi

if grep -qE "${git_re}(push([[:space:]].*)?[[:space:]](--force|--force-with-lease|-f|\+[^[:space:]]+)([[:space:]=]|$)|rebase([[:space:]]|$)|commit([[:space:]].*)?[[:space:]]--amend([[:space:]]|$)|reset([[:space:]].*)?[[:space:]]--hard([[:space:]]|$)|filter-(branch|repo)([[:space:]]|$))" <<<"$segments"; then
  echo "Bloquejat: fix-forward, no es reescriu l'historial (CLAUDE.md §Flux de treball). Corregiu-ho amb un commit nou." >&2
  exit 2
fi

exit 0
