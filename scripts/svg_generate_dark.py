#!/usr/bin/env python3
"""
svg_generate_dark.py
====================
Script de pre-render de Quarto. Genera automàticament les variants dark de
totes les figures SVG light del projecte EC.

Execució automàtica via _quarto.yml:
    project:
      pre-render: scripts/svg_generate_dark.py

La taula de substitució de colors és la font de veritat única definida a
svg_specs.md, dins el bloc etiquetat `#svg-dark-replacements`.
Per modificar la paleta dark, editeu només aquell bloc.

Lògica de regeneració
---------------------
Per a cada `figures/*_light.svg`:
  1. Si el nom base és a `dark_exclusions.txt` → SALTA (dark manual).
  2. Si la dark ja existeix i és més nova que la light → SALTA (vigent).
  3. En cas contrari → GENERA la dark aplicant la taula de substitució.

Fitxer d'exclusions
-------------------
`dark_exclusions.txt`: un nom de fitxer per línia (sense ruta).
Les línies que comencen per `#` s'ignoren (comentaris).
"""

import ast
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Lectura de la taula de substitució des de svg_specs.md
# ---------------------------------------------------------------------------

def _load_replacements(specs_file: Path) -> list[tuple[str, str]]:
    """
    Extreu la variable REPLACEMENTS del bloc `{.python #svg-dark-replacements}`
    de svg_specs.md i la retorna com a llista de tuples (light, dark).

    Llança ValueError si el bloc no es troba o no es pot parsejar.
    """
    content = specs_file.read_text(encoding='utf-8')

    # Localitza el bloc: ```{.python #svg-dark-replacements} ... ```
    pattern = re.compile(
        r'```\{\.python\s+#svg-dark-replacements\}(.*?)```',
        re.DOTALL,
    )
    match = pattern.search(content)
    if not match:
        raise ValueError(
            f"Bloc '#svg-dark-replacements' no trobat a {specs_file}.\n"
            "Afegiu un bloc ```{.python #svg-dark-replacements} amb REPLACEMENTS = [...]"
        )

    block = match.group(1).strip()

    # Parsejem amb ast per evitar eval() arbitrari
    try:
        tree = ast.parse(block, mode='exec')
    except SyntaxError as exc:
        raise ValueError(f"Error de sintaxi al bloc de substitució: {exc}") from exc

    # Busquem l'assignació REPLACEMENTS = [...]
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(t, ast.Name) and t.id == 'REPLACEMENTS'
                for t in node.targets
            )
        ):
            try:
                replacements = ast.literal_eval(node.value)
            except ValueError as exc:
                raise ValueError(
                    f"No s'ha pogut avaluar REPLACEMENTS: {exc}"
                ) from exc
            if not isinstance(replacements, list):
                raise ValueError("REPLACEMENTS ha de ser una llista.")
            return [(str(a), str(b)) for a, b in replacements]

    raise ValueError(
        f"Variable REPLACEMENTS no trobada al bloc '#svg-dark-replacements' de {specs_file}."
    )


# ---------------------------------------------------------------------------
# Substitució de colors
# ---------------------------------------------------------------------------

def _build_substituter(replacements: list[tuple[str, str]]):
    """Retorna una funció de substitució compilada per a la taula donada."""
    pattern = re.compile(
        '|'.join(re.escape(src) for src, _ in replacements),
        flags=re.IGNORECASE,
    )
    mapping = {src.lower(): dst for src, dst in replacements}
    return lambda content: pattern.sub(
        lambda m: mapping[m.group(0).lower()], content
    )


# ---------------------------------------------------------------------------
# Fitxer d'exclusions
# ---------------------------------------------------------------------------

def _load_exclusions(exclusions_file: Path) -> list[re.Pattern]:
    """Carrega els patrons d'exclusió com a expressions regulars compilades."""
    if not exclusions_file.exists():
        return []
    lines = exclusions_file.read_text(encoding='utf-8').splitlines()
    patterns = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        try:
            patterns.append(re.compile(line))
        except re.error as exc:
            print(f'[dark-svg] AVÍS: patró d\'exclusió invàlid {line!r}: {exc}', file=sys.stderr)
    return patterns


def _is_excluded(dark_name: str, exclusions: list[re.Pattern]) -> bool:
    return any(p.search(dark_name) for p in exclusions)


# ---------------------------------------------------------------------------
# Lògica principal
# ---------------------------------------------------------------------------

def generate_dark_svgs(
    figures_dir: Path,
    specs_file: Path,
    exclusions_file: Path,
    verbose: bool = True,
) -> None:

    # Carrega la taula des de svg_specs.md
    try:
        replacements = _load_replacements(specs_file)
    except ValueError as exc:
        print(f'[dark-svg] ERROR carregant taula de substitució: {exc}', file=sys.stderr)
        sys.exit(1)

    if verbose:
        print(f'[dark-svg] Taula carregada des de {specs_file} ({len(replacements)} substitucions)')

    apply_dark = _build_substituter(replacements)

    light_files = sorted(figures_dir.glob('*_light.svg'))
    if not light_files:
        if verbose:
            print(f'[dark-svg] Cap fitxer *_light.svg trobat a {figures_dir}')
        return

    exclusions = _load_exclusions(exclusions_file)
    if verbose and exclusions:
        print(f'[dark-svg] Exclusions ({len(exclusions)} patrons): {[p.pattern for p in exclusions]}')

    generated = skipped_manual = skipped_fresh = errors = 0

    for light_path in light_files:
        dark_name = light_path.name.replace('_light.svg', '_dark.svg')
        dark_path = light_path.parent / dark_name

        # 1. Exclusió manual (regex)
        if _is_excluded(dark_name, exclusions):
            if verbose:
                print(f'[dark-svg] SALTA (manual)  {dark_name}')
            skipped_manual += 1
            continue

        # 2. Dark vigent (més nova que light)
        if (
            dark_path.exists()
            and dark_path.stat().st_mtime > light_path.stat().st_mtime
        ):
            if verbose:
                print(f'[dark-svg] SALTA (vigent)  {dark_name}')
            skipped_fresh += 1
            continue

        # 3. Generació
        try:
            content = light_path.read_text(encoding='utf-8')
            dark_path.write_text(apply_dark(content), encoding='utf-8')
            if verbose:
                print(f'[dark-svg] GENERAT         {dark_name}')
            generated += 1
        except Exception as exc:  # noqa: BLE001
            print(f'[dark-svg] ERROR  {dark_name}: {exc}', file=sys.stderr)
            errors += 1

    if verbose:
        print(
            f'[dark-svg] Resum: {generated} generats, '
            f'{skipped_fresh} vigents, '
            f'{skipped_manual} manuals, '
            f'{errors} errors.'
        )

    if errors:
        sys.exit(1)


# ---------------------------------------------------------------------------
# Punt d'entrada
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    root = Path.cwd()
    generate_dark_svgs(
        figures_dir=root / 'figures',
        specs_file=root / 'svg_specs.md',
        exclusions_file=root / 'dark_exclusions.txt',
        verbose=True,
    )
