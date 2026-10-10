# Les ordres del projecte: `make help` les llista. Les tres de cada dia són
# `make render` (mentre s'edita), `make comprova` (abans del commit) i
# `make comprova-tot` (abans d'obrir una MR o de publicar), i es descriuen a
# 13_contrib.qmd §Comprovacions per nivells.
#
# Dos renders del mateix worktree no es poden fer alhora (el pre-render esborra
# auto_figs/): el segon espera que acabi el primer, fins a 15 min (flock, amb
# el fitxer de bloqueig al directori de git del worktree; D-103). On no hi ha
# flock (macOS), no hi ha bloqueig.

TAULES   = 25_scripts/gen_taules_auto.py 24_specs/taules_fusio.toml 21_riscv --output-dir=auto_riscv/
BLOQUEIG = $(shell git rev-parse --git-path ec-render.lock 2>/dev/null)
FLOCK    = $(if $(shell command -v flock 2>/dev/null),flock -w 900 -E 75 "$(BLOQUEIG)",)
ESPERA   = if [ -n '$(FLOCK)' ] && ! flock -n "$(BLOQUEIG)" true; then echo "[render] Hi ha un altre render en marxa en aquest worktree: s'espera que acabi (fins a 15 min)." >&2; fi
ESGOTAT  = if [ $$rc -eq 75 ]; then echo "[render] L'altre render no ha acabat en 15 min, i aquest no s'ha fet." >&2; fi; exit $$rc

help:                   ## aquesta llista
	@awk -F':.*## ' '/^[^ \t#=][^:=]*:.*## /{printf "  make %-16s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

render:                 ## taules fusionades i HTML (1–3 min): el bucle diari
	@$(ESPERA)
	@$(FLOCK) sh -c '$(TAULES) && quarto render --to html'; rc=$$?; $(ESGOTAT)

render-complet:         ## taules fusionades, HTML i PDF (4–8 min)
	@$(ESPERA)
	@$(FLOCK) sh -c '$(TAULES) && quarto render'; rc=$$?; $(ESGOTAT)

comprova:               ## les comprovacions del nivell dels canvis respecte d'HEAD: abans del commit
	@python3 25_scripts/comprova.py || [ $$? -eq 1 ]

comprova-branca:        ## les de la branca sencera respecte d'origin/main: abans del push
	@python3 25_scripts/comprova.py --base origin/main || [ $$? -eq 1 ]

comprova-tot:           ## totes, sobre el corpus sencer, amb el PDF i RARS (5–10 min): abans d'una MR o de publicar
	@python3 25_scripts/comprova.py --tot || [ $$? -eq 1 ]

registres:              ## regenera els registres versionats: glossari, SVG de model (a) i taules de la guia
	python3 25_scripts/gen_glossari.py
	python3 25_scripts/gen_T4_sumador.py
	python3 25_scripts/gen_T7.py
	python3 25_scripts/gen_T8.py
	python3 25_scripts/comprova.py --taula

glossari:               ## només la secció «Termes» de 12_sigles_simbols.qmd, des del corpus
	python3 25_scripts/gen_glossari.py

inventari:              ## l'inventari de figures, a demanda (25_scripts/out_inventari_figures/figures.md)
	python3 25_scripts/inventari_figures.py

taules:                 ## només les taules fusionades (auto_riscv/), sense renderitzar
	$(TAULES)

instal·la-hooks:        ## activa els hooks de git (.githooks/): les ràpides abans del commit, la branca abans del push
	git config core.hooksPath .githooks
	@echo "Hooks de git activats. Per desactivar-los: git config --unset core.hooksPath"

clean:                  ## esborra els artefactes del render, sense tocar cap font
	rm -rf _book *_files
	rm -f $(filter-out $(shell git ls-files '*.html'),$(wildcard *.html)) *.log Estructura-de-computadors.tex

.PHONY: help render render-complet comprova comprova-branca comprova-tot registres glossari inventari taules instal·la-hooks clean
