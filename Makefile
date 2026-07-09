render:
	22_scripts/gen_taules_auto.py 21_specs/taules_fusio.toml 11_riscv --output-dir=11_riscv_auto/
	quarto render

clean:
	rm -rf _book *_files
	rm -f *.html *.log Estructura-de-computadors.tex

.PHONY: render clean
