render:                 # bucle diari: només HTML (segons)
	25_scripts/gen_taules_auto.py 24_specs/taules_fusio.toml 21_riscv --output-dir=auto_riscv/
	quarto render --to html

render-complet:         # HTML + PDF (~7 min, compilació LaTeX)
	25_scripts/gen_taules_auto.py 24_specs/taules_fusio.toml 21_riscv --output-dir=auto_riscv/
	quarto render

clean:
	rm -rf _book *_files
	rm -f *.html *.log Estructura-de-computadors.tex

.PHONY: render render-complet clean
