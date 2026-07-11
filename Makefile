render:
	25_scripts/gen_taules_auto.py 24_specs/taules_fusio.toml 21_riscv --output-dir=auto_riscv/
	quarto render

clean:
	rm -rf _book *_files
	rm -f *.html *.log Estructura-de-computadors.tex

.PHONY: render clean
