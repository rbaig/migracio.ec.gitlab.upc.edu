#!/usr/bin/env bash
# PreToolUse (Edit|Write): els fitxers que genera el render o un script no s'editen
# a mà, perquè el pròxim render o la pròxima execució del generador desfà el retoc
# en silenci (13_contrib.qmd §Paleta de colors, §Renderitzar el projecte).
#   - auto_figs/, auto_riscv/ i _book/: el pre-render i el render; auto_termes/, gen_glossari.py.
#   - *_dark.svg: gen_dark.py, sempre.
# Sortir amb 2 bloqueja l'edició, i el text d'stderr arriba a Claude com a motiu.

f=$(jq -r '.tool_input.file_path // ""')
[ -n "$f" ] || exit 0
arrel=$(git -C "$(dirname "$f")" rev-parse --show-toplevel 2>/dev/null) || exit 0
rel=${f#"$arrel"/}

case "$rel" in
  auto_figs/*|*_dark.svg)
    echo "Bloquejat: $rel el genera el pre-render (gen_dark.py, els gen_*.py o norm_font.py). Canvieu-ne el font: l'SVG de 22_figs_originals/, el .toml de 24_specs/ o el generador (13_contrib.qmd §Figures i material gràfic)." >&2
    exit 2 ;;
  auto_riscv/*)
    echo "Bloquejat: $rel el genera gen_taules_auto.py a partir de 21_riscv/ i 24_specs/taules_fusio.toml. Canvieu-ne els fragments." >&2
    exit 2 ;;
  auto_termes/*)
    echo "Bloquejat: $rel el genera gen_glossari.py a partir de 24_specs/termes.toml. Canvieu-ne el terme allà." >&2
    exit 2 ;;
  _book/*)
    echo "Bloquejat: $rel és la sortida del render. Canvieu-ne el .qmd." >&2
    exit 2 ;;
esac
exit 0
