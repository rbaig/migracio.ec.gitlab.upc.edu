# Lèxic: l'anàlisi del 2026-10-12 i les eines de consulta

Aquest directori es conserva sencer ([D-122](../registre_de_decisions.md#d-122)): té l'anàlisi del lèxic anglès–català del llibre que va donar [D-115](../registre_de_decisions.md#d-115) i [D-116](../registre_de_decisions.md#d-116), i els scripts amb què es va fer. Uns quants serveixen per consultar les fonts d'un terme nou; la resta són el registre del mètode.

## Els criteris del lèxic

No són aquí: aquest directori no en té cap còpia.

- **Les regles**: `13_contrib.qmd`, §Referència normativa (les fonts lèxiques, per ordre de precedència: DIEC2, Termcat, Optimot, Softcatalà i Viquipèdia) i §Anglicismes i terminologia obligatòria (el sintagma transparent, quan es fa servir l'anglès, la presentació i la cursiva).
- **El perquè**: D-115 (el fitxer de termes mana i el text s'hi comprova) i D-116 (les fonts, el sintagma transparent i l'anglès sempre en cursiva).
- **Les formes**: `24_specs/termes.toml`, amb les fonts de cada terme al camp `fonts`. En surten el glossari de termes i la taula de formes que no s'han de fer servir (`12_sigles_simbols.qmd`, `13_contrib.qmd`), i les comprovacions de `comprova.py` hi contrasten el text.

## L'anàlisi del 2026-10-12

`revisio_2026-10-12.md` és la fotografia del lèxic de `2a4199f`: 193 entrades consultades al Cercaterm, a l'Optimot i a Softcatalà, amb les propostes de canvi i els dubtes de llavors. **Es llegeix com a història**:

- el criteri que hi apareix és el de D-88, que D-116 ha substituït;
- les decisions que en van sortir ja són a `termes.toml` i al text (D-116);
- `24_specs/glossari.toml`, que hi apareix, ja no existeix: el va substituir `termes.toml` (D-115);
- els números de línia són els de `2a4199f`.

## Consultar les fonts d'un terme nou

Els scripts de consulta cobreixen el Termcat, l'Optimot i Softcatalà. El DIEC2 i la Viquipèdia es consulten a mà. Executeu-los des d'un directori temporal, no des del repositori: escriuen els resultats (JSON) al directori de treball. A `termes.txt` hi va un terme anglès per línia. Les consultes es reprenen: un terme que ja és al JSON de sortida no es torna a demanar.

```bash
cd "$(mktemp -d)"
printf 'buffer\nstride\n' > termes.txt
S=<clon>/24_specs/lexic/scripts
python3 $S/lot_http.py              # softcatala.json i optimot.json
python3 $S/optimot_detall.py        # optimot_detall.json: les fitxes del Termcat de l'àrea TIC (i les d'altres fonts), amb les denominacions ca/en
python3 $S/cercaterm.py termes.txt  # cercaterm.json: el Cercaterm, amb l'àrea TIC i sense
```

- `cercaterm.py` fa servir Playwright amb el Chrome del sistema (`/usr/bin/google-chrome`), perquè la web del Termcat posa un repte (Anubis) que una petició simple no passa. Arguments opcionals: el fitxer de sortida i la llengua del terme (`en`, per defecte, o `ca`).
- `softcatala.py` i `optimot.py` són els mòduls que fa servir `lot_http.py`; també es poden importar sols (`cerca(terme)`).
- Una fitxa és del concepte si és de l'àrea TIC, o d'una àrea informàtica de la Neoloteca. Una fitxa d'una altra àrea (*stride*, «gambada», és d'esport) no compta (D-116).
- Provats el 2026-10-14 amb *buffer* i *stride*: les tres consultes responen.

Amb el resultat, el terme entra a `termes.toml` amb la forma i el camp `fonts`, i el text el presenta com diu la guia.

## Els scripts de l'anàlisi

Els tres primers encara funcionen, des d'un directori temporal i en aquest ordre (provat el 2026-10-14): `italiques.py <clon> > italiques.tsv`, i després `classifica.py` i `context.py`, que llegeixen `italiques.tsv`. `context.py` llegeix els `.qmd` del clon principal, el camí escrit al codi. La resta no es poden tornar a executar: llegeixen fitxers intermedis que no es van versionar (`prosa.tsv`, `glossari.json`, `taules.json`…), alguns duen escrit el camí d'un directori temporal que ja no existeix, i `24_specs/glossari.toml` tampoc no hi és. Es conserven com a registre del mètode.

| Script | Què feia |
| :--- | :--- |
| `italiques.py` | Extreu les cursives de la prosa dels `.qmd` (fora del codi i de les fórmules), amb el fitxer i la línia |
| `classifica.py` | Classifica les cursives en anglès o en català amb hunspell, amb el nombre d'ocurrències |
| `context.py` | El context de cada cursiva al seu fitxer |
| `comptes.py` | Compta les ocurrències de cada terme, en cursiva i en pla, i de la forma catalana |
| `termes_c.py` | Els anglicismes del corpus que no eren al glossari |
| `pass2_termes.py`, `pass2.py` | La segona passada: les variants angleses i les formes catalanes, a l'Optimot i a Softcatalà |
| `digest.py`, `digest2.py` | El resum de les fonts per a cada terme |
| `files.py` | Les files de les taules, amb la valoració de cada terme |
| `gen_lexic.py`, `assemble.py` | Generen les taules i munten `revisio_2026-10-12.md` |
