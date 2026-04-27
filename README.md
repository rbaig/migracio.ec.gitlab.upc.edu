# README

Material escrit d'Estructura de Computadors (EC)
Segon quadrimestre (Q2) del Grau en enginyeria Informàtica (GEI)
Facultat d'informàtica de Barcelona (FIB)
Universitat politècnica de Catalunya (UPC)

## Quarto

### Ús

* Directori de treball
```
cd ~/git/EC.qmd
```

* Renderitzat HTML
```bash
quarto render --to html
```
* Renderitzat PDF
quarto render --to pdf --output-dir .

* Netejar a fons
```bash
rm *.html *.log *.tex
rm -rf *_files
```

* VS Code Terminal (rerenderitza a casa guardada):
```
quarto preview
```

### Installation Debian
https://quarto.org/docs/download/

```bash
wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.9.36/quarto-1.9.36-linux-amd64.deb
sudo dpkg -i quarto-1.9.36-linux-amd64.deb
quarto --version
```
* Si no hi ha el navegador Chrome instal·lat (e.g., server)
```bash
quarto install chrome-headless-shell
```
* Per renderitzar PDF fer-ho amb TinyTex estalvia maldecaps:
```bash
quarto install tinytex
```
* Per status
```bash
quarto check
```

### Contribueix-hi

Vegeu el fitxer `contrib.qmd`
