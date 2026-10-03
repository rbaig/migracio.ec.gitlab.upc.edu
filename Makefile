taules:
	25_scripts/gen_taules_auto.py 24_specs/taules_fusio.toml 21_riscv --output-dir=auto_riscv/

render: taules          # bucle diari: només HTML (segons)
	quarto render --to html

render-complet: taules  # HTML + PDF (~5 min aquí, ~7 al CI)
	quarto render

inventari:              # inventari de figures (24_specs/figures.md)
	python3 25_scripts/inventari_figures.py

clean:
	rm -rf _book *_files
	rm -f *.html *.log Estructura-de-computadors.tex

.PHONY: render render-complet taules inventari clean
