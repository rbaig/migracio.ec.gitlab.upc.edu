#!/usr/bin/env bash
# Escombrada del corpus: compte, repartiment per fitxer i l'ordre que ho reprodueix.
# Les regles són a 13_contrib.qmd §Escombrades i verificació del corpus; aquest
# script mecanitza les regles 1, 4, 10, 11, 12 i 12 bis. La resta demanen judici.
#
# Ús: 25_scripts/escombrada.sh [opcions] <patró> [-- <pathspec>...]
#   --cas          distingeix majúscules (per defecte no; regla 4)
#   -F             patró literal (per defecte, expressió regular estesa)
#   -w             només paraules senceres
#   --commit <c>   mesura en un commit en lloc de l'arbre de treball (regla 11)
#   --tot          no exclou TODO.md ni 13_contrib.qmd (regla 12)
# Sense pathspec, cobreix tot el repositori versionat, amb tots els tipus de fitxer (regla 4).
set -uo pipefail
cd "$(git rev-parse --show-toplevel)" || exit 1

cas=-i; mode=-E; paraula=; commit=; exclou=1
while [ $# -gt 0 ]; do
  case $1 in
    --cas) cas=; shift ;;
    -F) mode=-F; shift ;;
    -w) paraula=-w; shift ;;
    --commit) commit=${2:?Falta el commit}; shift 2 ;;
    --tot) exclou=0; shift ;;
    -h|--help) sed -n '2,12p' "$0" | sed -E 's/^# ?//'; exit 0 ;;
    --) shift; break ;;
    -*) echo "Opció desconeguda: $1 (vegeu --help)" >&2; exit 64 ;;
    *) break ;;
  esac
done
[ $# -ge 1 ] || { echo "Falta el patró (vegeu --help)" >&2; exit 64; }
patro=$1; shift
[ "${1:-}" = "--" ] && shift
pathspec=("$@")
[ ${#pathspec[@]} -eq 0 ] && pathspec=(.)
[ $exclou -eq 1 ] && pathspec+=(':!TODO.md' ':!13_contrib.qmd')

ordre=(git grep -o -I "$mode")
[ -n "$cas" ] && ordre+=("$cas")
[ -n "$paraula" ] && ordre+=("$paraula")
ordre+=(-e "$patro")
[ -n "$commit" ] && ordre+=("$commit")
ordre+=(-- "${pathspec[@]}")

# Cita un argument perquè l'ordre publicada es pugui copiar i enganxar.
cita() {
  case $1 in
    *[!A-Za-z0-9_./=-]*) printf "'%s'" "${1//\'/\'\\\'\'}" ;;
    *) printf '%s' "$1" ;;
  esac
}
publicada=$(for a in "${ordre[@]}"; do cita "$a"; printf ' '; done)

sortida=$("${ordre[@]}"); rc=$?
if [ $rc -gt 1 ]; then
  echo "git grep ha fallat (codi $rc): $publicada" >&2
  exit $rc
fi

# Regla 11: una xifra només és certa respecte del commit on es va mesurar.
if [ -n "$commit" ]; then
  mesura="commit $(git rev-parse --short "$commit") ($(git log -1 --format=%cs "$commit"))"
else
  mesura="arbre de treball sobre $(git rev-parse --short HEAD) ($(date +%F))"
  [ -n "$(git status --porcelain --untracked-files=no)" ] && mesura+=", amb canvis no confirmats"
fi
echo "# Mesura: $mesura"
[ $exclou -eq 1 ] && echo "# Exclou TODO.md (hi registra la tasca) i 13_contrib.qmd (hi escriu la lliçó): regla 12. Per incloure'ls, --tot."

total=0
[ -n "$sortida" ] && total=$(printf '%s\n' "$sortida" | wc -l)
if [ "$total" -eq 0 ]; then
  echo "total: 0 (cap coincidència)"
else
  # Amb un commit, git grep escriu <commit>:<ruta>:<coincidència> i la ruta és el segon camp.
  repartiment=$(printf '%s\n' "$sortida" \
    | awk -v c="$commit" '{ if (c != "") sub(/^[^:]*:/, ""); print substr($0, 1, index($0, ":") - 1) }' \
    | sort | uniq -c | sort -rn)
  printf '%s\n' "$repartiment"
  suma=$(printf '%s\n' "$repartiment" | awk '{ s += $1 } END { print s }')
  # Regla 12 bis: el repartiment ha de sumar el total que acompanya.
  if [ "$suma" -eq "$total" ]; then
    echo "total: $total (el repartiment suma $suma ✓)"
  else
    echo "total: $total, però el repartiment suma $suma ✗" >&2
    echo "Ordre: $publicada| wc -l"
    exit 1
  fi
fi
echo "Ordre: $publicada| wc -l"
