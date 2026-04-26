"""Resetea el repositorio para una nueva tesis (fork limpio).

Vacía el contenido específico del tema actual, dejando intactas las capas
estables (`platform/`, `.github/`, `docs/`, `tests/`).

Uso:
    python platform/scripts/cleanup/reset_for_new_thesis.py            # dry-run
    python platform/scripts/cleanup/reset_for_new_thesis.py --apply    # ejecuta
    python platform/scripts/cleanup/reset_for_new_thesis.py --apply --keep-templates

Diseño:
- **Idempotente**: ejecutar N veces no rompe nada.
- **Reversible**: por defecto solo lista lo que borraría (`--dry-run`).
- **Conservador**: no toca `platform/`, `.git/`, `.github/`, `docs/`, `tests/`.
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


def collect_targets(keep_templates: bool) -> tuple[list[Path], list[Path]]:
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply", action="store_true",
        help="Ejecuta los borrados. Sin esta flag corre en modo dry-run.",
    )
    parser.add_argument(
        "--keep-templates", action="store_true",
        help="Conserva platform/templates/* (solo afecta al print informativo).",
    )
    args = parser.parse_args()
    dry_run = not args.apply

    print(f"=== reset_for_new_thesis ({'DRY-RUN' if dry_run else 'APPLY'}) ===")
    print(f"REPO_ROOT = {REPO_ROOT}")
    print()

    files, dirs = collect_targets(keep_templates=args.keep_templates)

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

    print()
    if dry_run:
        print("Dry-run completado. Re-ejecutar con --apply para borrar.")
    else:
        print("Reset completado. Próximos pasos:")
        print("  1. Editar content/manuscript/Documento_Tesis.md con el nuevo título y autor.")
        print("  2. Editar platform/templates/styles/caratula.docx con la nueva carátula.")
        print("  3. Actualizar el tema en .github/copilot-instructions.md.")
        print("  4. (Opcional) Crear/cargar skill de dominio nuevo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
