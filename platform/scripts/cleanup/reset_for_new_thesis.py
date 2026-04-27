"""Resetea el repositorio para una nueva tesis (fork limpio).

Vacía el contenido específico del tema actual, dejando intactas las capas
estables (`platform/`, `.github/`, `docs/`, `tests/`).

Uso:
    python platform/scripts/cleanup/reset_for_new_thesis.py            # dry-run
    python platform/scripts/cleanup/reset_for_new_thesis.py --apply    # ejecuta
    python platform/scripts/cleanup/reset_for_new_thesis.py --apply --scan-term "termino viejo"

Diseño:
- **Idempotente**: ejecutar N veces no rompe nada.
- **Reversible**: por defecto solo lista lo que borraría (modo dry-run).
- **Conservador**: no toca `platform/`, `.git/`, `.github/`, `docs/`, `tests/`.
    Esas carpetas deben ser agnósticas antes de ejecutar este script.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]

# Carpetas cuyo contenido se vacía (preservando la carpeta y su README.md).
DIRS_TO_EMPTY: list[Path] = [
    REPO_ROOT / "content" / "sources" / "international",
    REPO_ROOT / "content" / "sources" / "national",
    REPO_ROOT / "content" / "media" / "diagrams",
    REPO_ROOT / "content" / "media" / "figures",
    REPO_ROOT / "content" / "observations",
    REPO_ROOT / "content" / "drafts",
    REPO_ROOT / "build",
]

# Archivos individuales a resetear con un esqueleto mínimo.
MANUSCRIPT = REPO_ROOT / "content" / "manuscript" / "Documento_Tesis.md"

TEXT_SUFFIXES = {
    ".md", ".txt", ".py", ".ps1", ".json", ".yaml", ".yml",
    ".toml", ".ini", ".cfg", ".csv", ".puml",
}
SCAN_EXCLUDED_PARTS = {".git", ".pytest_cache", "__pycache__", "build"}

MANUSCRIPT_SKELETON = """\
---
title: "Título de la nueva tesis"
author: "Autor"
---

# Resumen

\\newpage

# Abstract

\\newpage

# Introducción

\\newpage

# Capítulo I: Planteamiento del problema

\\newpage

# Capítulo II: Marco teórico

\\newpage

# Capítulo III: Metodología

\\newpage

# Capítulo IV: Resultados

\\newpage

# Capítulo V: Discusión

\\newpage

# Conclusiones

\\newpage

# Recomendaciones

\\newpage

# Referencias

\\newpage

# Anexos
"""


def is_protected(path: Path) -> bool:
    """`README.md` y `.gitkeep` se preservan al vaciar carpetas."""
    return path.name in {"README.md", ".gitkeep"}


def collect_targets() -> tuple[list[Path], list[Path]]:
    """Devuelve (archivos_a_borrar, dirs_a_borrar)."""
    files: list[Path] = []
    dirs: list[Path] = []
    for d in DIRS_TO_EMPTY:
        if not d.exists():
            continue
        for child in d.iterdir():
            if is_protected(child):
                continue
            if child.is_file():
                files.append(child)
            elif child.is_dir():
                dirs.append(child)
    return files, dirs


def reset_manuscript(dry_run: bool) -> bool:
    """Reescribe el manuscrito al esqueleto. Devuelve True si lo modificaría."""
    if not MANUSCRIPT.exists():
        if dry_run:
            print(f"  [crear] {MANUSCRIPT.relative_to(REPO_ROOT)}")
        else:
            MANUSCRIPT.parent.mkdir(parents=True, exist_ok=True)
            MANUSCRIPT.write_text(MANUSCRIPT_SKELETON, encoding="utf-8")
        return True

    current = MANUSCRIPT.read_text(encoding="utf-8")
    if current == MANUSCRIPT_SKELETON:
        return False

    if dry_run:
        print(f"  [reset] {MANUSCRIPT.relative_to(REPO_ROOT)}  ({len(current)} bytes -> {len(MANUSCRIPT_SKELETON)} bytes)")
    else:
        MANUSCRIPT.write_text(MANUSCRIPT_SKELETON, encoding="utf-8")
    return True


def load_scan_terms(raw_terms: list[str], scan_file: Path | None) -> list[str]:
    """Combina terminos de CLI y archivo, preservando orden y unicidad."""
    terms: list[str] = []
    for term in raw_terms:
        clean = term.strip()
        if clean and clean not in terms:
            terms.append(clean)
    if scan_file:
        for line in scan_file.read_text(encoding="utf-8").splitlines():
            clean = line.strip()
            if clean and not clean.startswith("#") and clean not in terms:
                terms.append(clean)
    return terms


def scan_residual_terms(terms: list[str]) -> list[tuple[Path, str]]:
    """Busca terminos residuales en archivos de texto del repo."""
    hits: list[tuple[Path, str]] = []
    lowered = [(term, term.lower()) for term in terms]
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SCAN_EXCLUDED_PARTS for part in path.parts):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
        for original, term in lowered:
            if term in text:
                hits.append((path.relative_to(REPO_ROOT), original))
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply", action="store_true",
        help="Ejecuta los borrados. Sin esta flag corre en modo dry-run.",
    )
    parser.add_argument(
        "--scan-term", action="append", default=[], metavar="TERM",
        help="Termino del tema anterior que no debe quedar tras el reset. Puede repetirse.",
    )
    parser.add_argument(
        "--scan-file", type=Path,
        help="Archivo UTF-8 con terminos a buscar (uno por linea, # para comentarios).",
    )
    args = parser.parse_args()
    dry_run = not args.apply

    print(f"=== reset_for_new_thesis ({'DRY-RUN' if dry_run else 'APPLY'}) ===")
    print(f"REPO_ROOT = {REPO_ROOT}")
    print()

    files, dirs = collect_targets()

    print(f"-- Archivos a borrar: {len(files)}")
    for f in sorted(files):
        try:
            rel = f.relative_to(REPO_ROOT)
        except ValueError:
            rel = f
        print(f"  [del] {rel}")
        if not dry_run:
            try:
                f.unlink()
            except OSError as e:
                print(f"        ERROR: {e}")

    print(f"\n-- Directorios a borrar: {len(dirs)}")
    for d in sorted(dirs):
        try:
            rel = d.relative_to(REPO_ROOT)
        except ValueError:
            rel = d
        print(f"  [rmtree] {rel}")
        if not dry_run:
            shutil.rmtree(d, ignore_errors=True)

    print("\n-- Manuscrito:")
    changed = reset_manuscript(dry_run)
    if not changed:
        print("  (ya está en estado de esqueleto)")

    terms = load_scan_terms(args.scan_term, args.scan_file)
    if terms:
        print("\n-- Verificación de términos residuales:")
        if dry_run:
            print("  (omitida en dry-run; ejecutar con --apply para verificar el repo limpio)")
        else:
            hits = scan_residual_terms(terms)
            if hits:
                for rel, term in hits:
                    print(f"  [hit] {rel} :: {term}")
                print("\nERROR: quedan términos del tema anterior. Revisar los hits anteriores.", file=sys.stderr)
                return 1
            print("  OK: no se encontraron términos residuales configurados.")

    print()
    if dry_run:
        print("Dry-run completado. Re-ejecutar con --apply para borrar.")
    else:
        print("Reset completado. Próximos pasos:")
        print("  1. Editar content/manuscript/Documento_Tesis.md con el nuevo título y autor.")
        print("  2. Editar platform/templates/styles/caratula.docx con la nueva carátula.")
        print("  3. Si hace falta, crear un skill de dominio copiando thesis-dominio-template.")
        print("  4. Buscar términos del tema anterior fuera de content/ y corregir cualquier fuga.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
