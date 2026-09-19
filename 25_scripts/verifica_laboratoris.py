#!/usr/bin/env python3
"""Arnès de verificació empírica dels programes d'assemblador dels laboratoris.

Extreu els blocs ```{.s filename="*.s"} de 04_laboratori/L1.qmd-L6.qmd, els
escriu a fitxers i els assembla/executa amb RARS 1.6 en mode línia de
comandes. Genera un informe amb el resultat (assembla/executa) i, per als
programes que executen, el bolcat de .data i dels registres finals.

Ús:
    python3 25_scripts/verifica_laboratoris.py [--rars /ruta/a/rars1_6.jar]

No forma part del pre-render de Quarto: és una eina d'auditoria a demanda.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LAB_DIR = REPO_ROOT / "04_laboratori"
OUT_DIR = REPO_ROOT / "25_scripts" / "out_verifica_laboratoris"
DEFAULT_RARS = Path("/home/roger/backup/uni/UPC/EC/RISC_V/RARS/rars1_6.jar")

MAX_STEPS = 200000

BLOCK_RE = re.compile(r'```\{\.s filename="([^"]+)"\}\n(.*?)\n```', re.S)

# Registres a bolcar sempre (arguments/retorn + temporals + segurs habituals).
REGS = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7",
        "t0", "t1", "t2", "t3", "t4", "t5", "t6",
        "s0", "s1", "s2", "s3", "s4", "s5", "ra", "sp"]

# Noms de filename que no són fitxers .s reals (fragments il·lustratius).
FRAGMENT_NAMES = {"RV32I", "C", "..."}

# Casos especials de compilació conjunta: (laboratori, [noms de bloc en ordre
# d'aparició al .qmd]) -> llista de filenames .s a assemblar junts.
# Els noms de bloc identifiquen el bloc pel seu filename i número d'ordre
# d'aparició (1-indexat) dins del fitxer, per desambiguar filenames repetits.
JOINT_COMPILATION = {
    # s5_1_2.s conté _start i ha d'anar primer (vegeu wrn-arrencada-rars).
    ("L5", "s5_1_1.s#1"): ["s5_1_2.s#1", "s5_1_1.s#1"],
    ("L5", "s5_1_2.s#1"): ["s5_1_2.s#1", "s5_1_1.s#1"],
    # s5_3_1.s (versió final, #sol-compon) crida descompon, definida a
    # s5_2_1.s: no és el cas de compilació separada explícit de l'enunciat
    # (§3), però estructuralment en depèn igual per assemblar. s5_3_1.s ha
    # d'anar primer a la línia de comandes: conté _start i RARS arrenca a la
    # primera instrucció del primer fitxer assemblat (vegeu wrn-arrencada-rars).
    ("L5", "s5_2_1.s#1"): ["s5_3_1.s#2", "s5_2_1.s#1"],
    ("L5", "s5_3_1.s#2"): ["s5_3_1.s#2", "s5_2_1.s#1"],
}

# Blocs a ignorar completament (no representen cap lliurament: són versions
# provisionals substituïdes explícitament per un bloc posterior al mateix
# fitxer). Identificats per (laboratori, filename, ordre d'aparició 1-indexat).
SUPERSEDED = {
    ("L5", "s5_3_1.s", 1),  # _start provisional dins callout de comprovació;
                            # substituït pel programa complet a l'ordre 2.
}

# Blocs "incomplets per disseny": depenen d'una subrutina que l'enunciat
# demana escriure a l'alumne i que no és present al bloc. Es couen soles:
# no compten com a fallada.
INCOMPLETE_BY_DESIGN = {
    ("L3", "s3_4_2.s", 1): "conté el comentari `# update: vegeu @sol-update "
                            "(inseriu el codi aquí)` — la subrutina update "
                            "l'ha d'enganxar l'alumne.",
    ("L3", "s3_5_1.s", 1): "és només la subrutina `codifica` corregida "
                            "(extracte de la solució de depuració, exr-depuracio); "
                            "no inclou `g`, `.data` ni `_start` i per tant no "
                            "és un programa autònom.",
}

# Verificació empírica addicional, només per contrastar la predicció que
# _start col·locat després de subrutines a .text fa que RARS comenci a
# executar a la primera instrucció del fitxer (no a _start). S'omple el
# placeholder d'un bloc "incomplet per disseny" amb una subrutina ja
# verificada independentment, NOMÉS per comprovar aquest efecte d'arrencada;
# no valida la resta del contingut del bloc.
STARTUP_ORDER_CHECKS = {
    ("L3", "s3_4_2.s", 1): {
        "placeholder": "# update: vegeu @sol-update (inseriu el codi aquí)",
        "source_block": ("L3", "s3_4_1.s", 1),
        "note": "update (de s3_4_1.s, ja verificada) enganxada al placeholder "
                "només per comprovar l'ordre d'arrencada; _start és després "
                "de moda/update a .text.",
    },
}

# s3_5_1.s (exr-depuracio) només conté la subrutina `codifica` corregida.
# El programa complet (g + .data + _start) és al bloc sense filename= de
# l'enunciat (L3.qmd:490-553, versió amb els 3 errors originals). Es
# reconstrueix aquí, amb els 3 errors ja esmenats, únicament per contrastar
# la predicció d'ordre d'arrencada (_start és després de codifica a .text).
S3_5_1_FULL_PROGRAM_TEMPLATE = """\
.globl _start

.data
alfabet: .asciz "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
w1:      .asciz "ARQUITECTURA"
w2:      .space 16

.text

g:
        lb   t0, 0(a1)          # t0 = *pfrase
        li   t1, 'A'
        sub  t0, t0, t1         # t0 = *pfrase - 'A'
        li   t1, 25
        sub  t0, t1, t0         # t0 = 25 - (*pfrase - 'A')
        add  t0, a0, t0         # t0 = &alfa[25 - ...]
        lb   a0, 0(t0)          # a0 = alfa[25 - ...]
        ret

{codifica}

_start:
        la   a0, w1
        la   a1, w2
        jal  ra, codifica

        li   a7, 93
        li   a0, 0
        ecall
"""


class Block:
    def __init__(self, lab, filename, order, body, line):
        self.lab = lab
        self.filename = filename
        self.order = order
        self.body = body
        self.line = line
        self.key = f"{filename}#{order}"

    @property
    def is_fragment(self):
        return self.filename in FRAGMENT_NAMES

    @property
    def is_complete_program(self):
        return "_start:" in self.body

    @property
    def superseded(self):
        return (self.lab, self.filename, self.order) in SUPERSEDED

    @property
    def incomplete_reason(self):
        return INCOMPLETE_BY_DESIGN.get((self.lab, self.filename, self.order))


# ---------------------------------------------------------------------------
# Comprovacions ESTÀTIQUES (text, no depenen d'assemblar ni executar).
# S'apliquen a TOTS els blocs .s, inclosos els que RARS no pot processar sol
# (incomplets per disseny, sense _start, substituïts).
# ---------------------------------------------------------------------------

LABEL_RE = re.compile(r'^([A-Za-z_.][\w.]*)\s*:', re.M)
TEXT_DIRECTIVE_RE = re.compile(r'^\s*\.text\b', re.M)

# Directives/instruccions l'operand de les quals no admet cap expressió
# aritmètica a RARS: cal el literal ja calculat.
ARITH_OPERAND_RE = re.compile(
    r'^\s*(?:\.space|li|la)\s+(?:[A-Za-z_][\w]*\s*,\s*)?'
    r'([A-Za-z_][\w]*|\d+)\s*([+\-*])\s*([A-Za-z0-9_]+(?:\s*[+\-*]\s*[A-Za-z0-9_]+)*)',
    re.M,
)

RA_SPILL_RE = re.compile(r'^\s*(?:sw|lw)\s+ra\s*,', re.M)


def strip_comment(line):
    """Retorna la línia sense el comentari `#` final (no toca strings)."""
    idx = line.find('#')
    return line if idx == -1 else line[:idx]


def line_at(body, pos):
    """Número de línia (1-indexat, relatiu al bloc) del caràcter a `pos`."""
    return body.count("\n", 0, pos) + 1


def check_e1_start_order(block):
    """E1 — quan el bloc conté una etiqueta `_start:`, ha de ser la primera
    etiqueta després de `.text` (o, si el bloc és incomplet per disseny i no
    en conté cap, ERROR pel mateix motiu: RARS no pot determinar el punt
    d'entrada). Un fitxer amb `.text` però sense cap `_start:` (subrutines
    de compilació separada, p. ex. L5 §1/§3) no és, per si sol, un error E1:
    la comprovació d'ordre d'arrencada s'aplica al fitxer que sí conté
    `_start`."""
    findings = []
    m = TEXT_DIRECTIVE_RE.search(block.body)
    if m and "_start:" in block.body:
        after = block.body[m.end():]
        lm = LABEL_RE.search(after)
        if lm and lm.group(1) != "_start":
            findings.append((
                "ERROR", "E1",
                line_at(block.body, m.end() + lm.start()),
                f"primera etiqueta després de `.text` és `{lm.group(1)}:`, "
                f"no `_start:` — RARS inicia el PC a la primera instrucció "
                f"de `.text` i el programa no s'executarà com l'enunciat diu.",
            ))
        return findings

    if block.incomplete_reason and "_start:" not in block.body:
        findings.append((
            "ERROR", "E1",
            1,
            "el bloc no conté cap `.text` ni `_start:` — és incomplet per "
            "disseny, però pel mateix motiu (RARS no pot determinar el punt "
            "d'entrada) es reporta com a E1.",
        ))
    return findings


def check_e2_arith_operands(block):
    """E2 — cap operand de .space/li/la amb expressió aritmètica; cal el
    literal ja calculat (l'expressió va al comentari)."""
    findings = []
    for lineno, raw_line in enumerate(block.body.splitlines(), start=1):
        code = strip_comment(raw_line)
        m = ARITH_OPERAND_RE.search(code)
        if m:
            findings.append((
                "ERROR", "E2", lineno,
                f"operand amb expressió aritmètica (`{m.group(0).strip()}`) "
                f"— RARS no avalua expressions als operands; cal el literal "
                f"ja calculat, amb l'expressió al comentari.",
            ))
    return findings


def check_e3_start_prolog(block):
    """E3 — _start no és callee de ningú: cap desat/restauració de ra."""
    findings = []
    m = re.search(r'^_start\s*:', block.body, re.M)
    if not m:
        return findings
    after = block.body[m.end():]
    # Talla a la següent etiqueta de primer nivell (fi de _start), si n'hi ha.
    nm = LABEL_RE.search(after)
    scope = after[:nm.start()] if nm else after
    base_line = line_at(block.body, m.end())
    for rel_line, raw_line in enumerate(scope.splitlines(), start=0):
        code = strip_comment(raw_line)
        if RA_SPILL_RE.search(code):
            findings.append((
                "AVÍS", "E3", base_line + rel_line,
                "desat/restauració de `ra` dins `_start` — `_start` no és "
                "callee de ningú i acaba amb `li a7, 93` + `ecall`; no ha de "
                "tenir pròleg ni epíleg.",
            ))
    return findings


def static_checks(block):
    """Totes les comprovacions estàtiques per a un bloc. Retorna una llista
    de (nivell, regla, línia_relativa_al_bloc, missatge)."""
    findings = []
    findings += check_e1_start_order(block)
    findings += check_e2_arith_operands(block)
    findings += check_e3_start_prolog(block)
    return findings


def extract_blocks():
    blocks = []
    for path in sorted(LAB_DIR.glob("L*.qmd")):
        lab = path.stem
        text = path.read_text(encoding="utf-8")
        counts = {}
        for m in BLOCK_RE.finditer(text):
            filename, body = m.group(1), m.group(2)
            counts[filename] = counts.get(filename, 0) + 1
            order = counts[filename]
            line = text[:m.start()].count("\n") + 1
            blocks.append(Block(lab, filename, order, body, line))
    return blocks


def write_block_file(block, dest_dir):
    dest_dir.mkdir(parents=True, exist_ok=True)
    path = dest_dir / block.filename
    path.write_text(block.body + "\n", encoding="utf-8")
    return path


def run_rars(rars_jar, files, dump_path):
    cmd = ["java", "-jar", str(rars_jar), "nc", "b", str(MAX_STEPS)]
    cmd += REGS
    cmd += ["dump", ".data", "HexText", str(dump_path)]
    cmd += [str(f) for f in files]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    except subprocess.TimeoutExpired:
        return {"stdout": "", "stderr": "TIMEOUT (>60s)", "timed_out": True}
    return {"stdout": proc.stdout, "stderr": proc.stderr, "timed_out": False}


def classify(result):
    out = result["stdout"] + result["stderr"]
    if result.get("timed_out"):
        return "NO ASSEMBLA", "TIMEOUT", None
    # Un "Error in <fitxer> line N" que NO sigui una excepció d'execució en
    # temps real (RARS l'anomena "Runtime exception") és un error
    # d'assemblatge: el programa no arriba a simular-se.
    is_runtime = "Runtime exception" in out or "Simulation terminated due to errors" in out
    if not is_runtime and (re.search(r"Error in .* line \d+", out) or "not a recognized operator" in out):
        msg = next((l for l in out.splitlines() if l.startswith("Error in")), out.strip())
        return "NO ASSEMBLA", msg, None
    if "Processing terminated due to errors" in out:
        msg = next((l for l in out.splitlines() if l.strip()), out.strip())
        return "NO ASSEMBLA", msg, None
    # RARS només mostra "Program terminated by calling exit" quan el
    # programa no ha escrit res per syscall a stdout; si n'hi ha, aquest
    # missatge no apareix encara que l'execució hagi acabat correctament.
    # Per tant, l'absència de qualsevol patró d'error és el senyal de succés.
    if re.search(r"error|exception|terminated due to errors", out, re.I):
        first = next((l for l in out.splitlines() if l.strip()), out.strip())
        return "ASSEMBLA", f"EXCEPCIÓ: {first}", out
    return "ASSEMBLA", "EXECUTA FINS AL FINAL", out


def trim_data_dump(dump_path):
    if not dump_path.exists():
        return []
    words = dump_path.read_text().splitlines()
    last_nonzero = -1
    for i, w in enumerate(words):
        if w.strip("0") != "":
            last_nonzero = i
    return words[: last_nonzero + 1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rars", type=Path, default=DEFAULT_RARS)
    args = ap.parse_args()

    if not args.rars.exists():
        print(f"ERROR: no s'ha trobat rars1_6.jar a {args.rars}", file=sys.stderr)
        sys.exit(1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    src_dir = OUT_DIR / "fitxers_extrets"

    blocks = extract_blocks()
    by_key = {(b.lab, b.key): b for b in blocks}

    rows = []
    details = []
    static_findings = []  # (lab, filename, order, línia_absoluta, nivell, regla, missatge)
    handled = set()

    def static_summary(b):
        findings = static_checks(b)
        for nivell, regla, rel_line, msg in findings:
            static_findings.append((b.lab, b.filename, b.order, b.line + rel_line - 1,
                                     nivell, regla, msg))
        n_err = sum(1 for f in findings if f[0] == "ERROR")
        n_avis = sum(1 for f in findings if f[0] == "AVÍS")
        if n_err == 0 and n_avis == 0:
            return "OK"
        parts = []
        if n_err:
            parts.append(f"{n_err} error{'s' if n_err != 1 else ''}")
        if n_avis:
            parts.append(f"{n_avis} avís{'os' if n_avis != 1 else ''}")
        return ", ".join(parts)

    for b in blocks:
        rowkey = (b.lab, b.key)
        if rowkey in handled:
            continue

        estatic = static_summary(b)

        if b.is_fragment:
            rows.append((b.lab, b.filename, b.order, b.line, "—", "FRAGMENT (no assemblable)", "", estatic))
            handled.add(rowkey)
            continue

        if b.superseded:
            rows.append((b.lab, b.filename, b.order, b.line, "—", "SUBSTITUÏT (vegeu bloc posterior)", "", estatic))
            handled.add(rowkey)
            continue

        reason = b.incomplete_reason
        if reason:
            rows.append((b.lab, b.filename, b.order, b.line, "—", "INCOMPLET PER DISSENY", reason, estatic))
            handled.add(rowkey)
            check = STARTUP_ORDER_CHECKS.get((b.lab, b.filename, b.order))
            if check:
                src = by_key.get((check["source_block"][0], f"{check['source_block'][1]}#{check['source_block'][2]}"))
                spliced = b.body.replace(check["placeholder"], src.body)
                dest_dir = src_dir / b.lab / f"{b.filename}_{b.order}_ordre_arrencada"
                dest_dir.mkdir(parents=True, exist_ok=True)
                path = dest_dir / b.filename
                path.write_text(spliced + "\n", encoding="utf-8")
                dump_path = dest_dir / "dump_data.txt"
                result = run_rars(args.rars, [path], dump_path)
                assembla, estat, raw = classify(result)
                details.append((b.lab, f"{b.filename} [comprovació ordre d'arrencada, {check['note']}]",
                                 assembla, estat, raw, trim_data_dump(dump_path)))
            if (b.lab, b.filename, b.order) == ("L3", "s3_5_1.s", 1):
                spliced = S3_5_1_FULL_PROGRAM_TEMPLATE.format(codifica=b.body)
                dest_dir = src_dir / b.lab / f"{b.filename}_{b.order}_ordre_arrencada"
                dest_dir.mkdir(parents=True, exist_ok=True)
                path = dest_dir / b.filename
                path.write_text(spliced, encoding="utf-8")
                dump_path = dest_dir / "dump_data.txt"
                result = run_rars(args.rars, [path], dump_path)
                assembla, estat, raw = classify(result)
                note = ("codifica corregida reconstruïda amb g/.data/_start del "
                        "bloc enunciat (exr-depuracio, L3.qmd:490-553), només per "
                        "comprovar l'ordre d'arrencada; _start és després de "
                        "codifica a .text.")
                details.append((b.lab, f"{b.filename} [comprovació ordre d'arrencada, {note}]",
                                 assembla, estat, raw, trim_data_dump(dump_path)))
            continue

        # Compilació conjunta?
        joint = JOINT_COMPILATION.get((b.lab, b.key))
        if joint:
            group_blocks = [by_key[(b.lab, k)] for k in joint if (b.lab, k) in by_key]
            for gb in group_blocks:
                handled.add((gb.lab, gb.key))
            estatics = [estatic] + [static_summary(gb) for gb in group_blocks if gb is not b]
            dest_dir = src_dir / b.lab / f"conjunt_{'_'.join(g.filename for g in group_blocks)}"
            paths = [write_block_file(gb, dest_dir) for gb in group_blocks]
            dump_path = dest_dir / "dump_data.txt"
            result = run_rars(args.rars, paths, dump_path)
            assembla, estat, raw = classify(result)
            label = " + ".join(g.filename for g in group_blocks)
            estatic_joint = "OK" if all(e == "OK" for e in estatics) else " / ".join(estatics)
            rows.append((b.lab, label, "-", "/".join(str(g.line) for g in group_blocks),
                         assembla, estat, "", estatic_joint))
            details.append((b.lab, label, assembla, estat, raw, trim_data_dump(dump_path)))
            continue

        if not b.is_complete_program:
            rows.append((b.lab, b.filename, b.order, b.line, "—",
                         "SENSE _start (no verificable sol)", "", estatic))
            handled.add(rowkey)
            continue

        dest_dir = src_dir / b.lab / f"{b.filename}_{b.order}"
        path = write_block_file(b, dest_dir)
        dump_path = dest_dir / "dump_data.txt"
        result = run_rars(args.rars, [path], dump_path)
        assembla, estat, raw = classify(result)
        rows.append((b.lab, b.filename, b.order, b.line, assembla, estat, "", estatic))
        details.append((b.lab, b.filename, assembla, estat, raw, trim_data_dump(dump_path)))
        handled.add(rowkey)

    write_report(rows, details, static_findings)


def write_report(rows, details, static_findings):
    report_path = OUT_DIR / "informe.md"
    lines = []
    lines.append("# Informe de verificació empírica dels laboratoris (RARS 1.6)\n")
    lines.append("| Laboratori | Fitxer | Ordre | Línia .qmd | Assembla | Executa | Estàtic |")
    lines.append("| :--- | :--- | :---: | :---: | :--- | :--- | :--- |")
    for lab, filename, order, line, assembla, estat, _, estatic in rows:
        lines.append(f"| {lab} | `{filename}` | {order} | {line} | {assembla} | {estat} | {estatic} |")

    lines.append("\n---\n\n## Detall\n")
    for lab, filename, assembla, estat, raw, data_dump in details:
        lines.append(f"### {lab} — `{filename}`\n")
        lines.append(f"- **Assembla**: {assembla}")
        lines.append(f"- **Execució**: {estat}\n")
        if raw:
            lines.append("```")
            lines.append(raw.strip())
            lines.append("```\n")
        if data_dump:
            lines.append("**Bolcat `.data` (paraules no nul·les, HexText):**\n")
            lines.append("```")
            lines.extend(data_dump)
            lines.append("```\n")

    lines.append("\n---\n\n## Comprovacions estàtiques — detall\n")
    if not static_findings:
        lines.append("Cap troballa.\n")
    else:
        lines.append("| Laboratori | Fitxer | Línia .qmd | Nivell | Regla | Missatge |")
        lines.append("| :--- | :--- | :---: | :---: | :---: | :--- |")
        for lab, filename, order, line, nivell, regla, msg in static_findings:
            fitxer = f"{filename}" if order == 1 else f"{filename} (#{order})"
            lines.append(f"| {lab} | `{fitxer}` | {line} | {nivell} | {regla} | {msg} |")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Informe escrit a {report_path}")


if __name__ == "__main__":
    main()
