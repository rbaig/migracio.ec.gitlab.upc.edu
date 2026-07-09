#!/usr/bin/env python3
"""
gen_taules_auto.py — Fusiona fragments de taula de 11_riscv/ per a 05_riscv.qmd.

Motiu: Quarto no permet encadenar dos {{< include >}} consecutius dins d'una
mateixa taula pipe (el primer tanca la taula; la resta cau a text cru). La
solució és fusionar físicament els fitxers font en un de sol i incloure'l amb
un únic {{< include >}}. Vegeu 21_specs/taules_fusio.toml i 07_contrib.qmd
§Fitxer de referència tècnica.

IMPORTANT: a diferència dels altres scripts de 22_scripts/, aquest NO es crida
des del `pre-render` de _quarto.yml. Quarto resol els {{< include >}} dels
capítols en un escaneig de configuració que s'executa ABANS del pre-render, de
manera que el fitxer fusionat ha d'existir al disc abans d'invocar `quarto`.
Cal executar aquest script manualment (README.md):

    python3 22_scripts/gen_taules_auto.py 21_specs/taules_fusio.toml 11_riscv --output-dir="11_riscv_auto/"

- El primer cop (checkout nou) i sempre que `quarto render` avorti per manca
  d'un fitxer a 11_riscv_auto/.
- Sempre que editeu un fitxer de 11_riscv/ que aparegui a
  21_specs/taules_fusio.toml (si no, 11_riscv_auto/ queda desactualitzat en
  silenci: `quarto render` no fallarà, però la taula final no reflectirà el
  canvi).

Ús manual complet:
    python3 22_scripts/gen_taules_auto.py <specs_file> <fonts_dir> [--output-dir DIR] [--force] [--verbosity N]

Arguments posicionals:
    specs_file      Manifest de fusions (p. ex. 21_specs/taules_fusio.toml).
    fonts_dir       Directori on es troben els fitxers font (p. ex. 11_riscv/).

Arguments opcionals:
    --output-dir    Directori on es desen els fitxers fusionats (per defecte: 11_riscv_auto/).
    --force         Regenera tots els fitxers ignorant timestamps.
    --verbosity 0|1|2
                    Nivell de detall del log (per defecte: 1).
                      0  Només errors i resum final.
                      1  Errors + avisos + resum.
                      2  Tot l'anterior + una línia per fitxer processat.

No editeu els fitxers generats a l'output-dir: editeu 21_specs/taules_fusio.toml
i els fitxers font a 11_riscv/.
"""

import tomllib
import sys
from pathlib import Path


def _load_manifest(specs_path: Path) -> list[dict]:
    if not specs_path.exists():
        print(f'[gen-taules-auto] ERROR: no es troba {specs_path}', file=sys.stderr)
        sys.exit(1)
    try:
        with open(specs_path, 'rb') as f:
            data = tomllib.load(f)
    except tomllib.TOMLDecodeError as exc:
        print(f'[gen-taules-auto] ERROR parsejant {specs_path}: {exc}', file=sys.stderr)
        sys.exit(1)

    if 'fusio' not in data:
        print(
            f'[gen-taules-auto] ERROR: {specs_path} no conté cap entrada [[fusio]].',
            file=sys.stderr,
        )
        sys.exit(1)

    return data['fusio']


def _validate(manifest: list[dict], fonts_dir: Path) -> list[str]:
    errors = []
    noms = set()
    for entry in manifest:
        sortida = entry.get('sortida')
        fonts = entry.get('fonts')
        if not sortida or not fonts:
            errors.append(f'  entrada incompleta (falta "sortida" o "fonts"): {entry}')
            continue
        if sortida in noms:
            errors.append(f'  "sortida" duplicada: {sortida}')
        noms.add(sortida)
        if len(fonts) < 2:
            errors.append(f'  {sortida}: cal almenys 2 fonts, en té {len(fonts)}')
        for fname in fonts:
            if not (fonts_dir / fname).exists():
                errors.append(f'  {sortida}: font no trobada: {fonts_dir / fname}')
    return errors


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description='Fusiona fragments de taula de 11_riscv/ per a 05_riscv.qmd.'
    )
    parser.add_argument('specs_file', type=Path, help='Manifest de fusions (p. ex. 21_specs/taules_fusio.toml)')
    parser.add_argument('fonts_dir', type=Path, help='Directori dels fitxers font (p. ex. 11_riscv/)')
    parser.add_argument(
        '--output-dir',
        type=Path,
        default=Path('11_riscv_auto'),
        metavar='DIR',
        help='Directori de sortida (per defecte: 11_riscv_auto/).',
    )
    parser.add_argument('--force', action='store_true', help='Regenera tots els fitxers ignorant timestamps.')
    parser.add_argument(
        '--verbosity',
        type=int,
        default=1,
        choices=[0, 1, 2],
        metavar='N',
        help="Nivell de detall del log (per defecte: 1).",
    )
    args = parser.parse_args()

    specs_path = args.specs_file
    fonts_dir  = args.fonts_dir
    output_dir = args.output_dir
    verbosity  = args.verbosity

    manifest = _load_manifest(specs_path)

    errors_val = _validate(manifest, fonts_dir)
    if errors_val:
        print('[gen-taules-auto] ERRORS DE VALIDACIÓ:', file=sys.stderr)
        for e in errors_val:
            print(e, file=sys.stderr)
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)
    script_mtime = Path(__file__).stat().st_mtime

    generated = skipped = errors = 0
    for entry in manifest:
        sortida = entry['sortida']
        fonts   = [fonts_dir / f for f in entry['fonts']]
        out_path = output_dir / f'{sortida}.qmd'

        if not args.force and out_path.exists():
            newest_font_mtime = max(f.stat().st_mtime for f in fonts)
            if out_path.stat().st_mtime > script_mtime and out_path.stat().st_mtime > newest_font_mtime:
                if verbosity >= 2:
                    print(f'[gen-taules-auto] SALTA (vigent)  {out_path.name}')
                skipped += 1
                continue

        try:
            parts = [f.read_text(encoding='utf-8').rstrip('\n') for f in fonts]
            content = '\n'.join(parts) + '\n'
            out_path.write_text(content, encoding='utf-8')
            generated += 1
            if verbosity >= 2:
                print(f'[gen-taules-auto] GENERAT  {out_path.name}')
        except Exception as exc:  # noqa: BLE001
            print(f'[gen-taules-auto] ERROR {out_path.name}: {exc}', file=sys.stderr)
            errors += 1

    if verbosity >= 1:
        print(
            f'[gen-taules-auto] Resum: {generated} generats, {skipped} vigents, {errors} errors. '
            f'Directori: {output_dir}'
        )

    if errors:
        sys.exit(1)


if __name__ == '__main__':
    main()
