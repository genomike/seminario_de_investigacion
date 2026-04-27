#!/usr/bin/env python3
"""Plantilla para correcciones masivas idempotentes del manuscrito.

Copiar este archivo como `fix_<patron>_v<N>.py`, completar los reemplazos y
ejecutar desde la raiz del repositorio. No guardar aqui texto propio de una
tesis concreta despues de consolidar el cambio.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
DOC = REPO_ROOT / "content" / "manuscript" / "Documento_Tesis.md"


def replace_once(text: str, old: str, new: str, label: str) -> tuple[str, int, int]:
    """Reemplaza un ancla unica y reporta (texto, cambios, errores)."""
    if old not in text:
        if new in text:
            print(f"  . ya aplicado: {label}")
            return text, 0, 0
        print(f"  x NO ENCONTRADO: {label}", file=sys.stderr)
        return text, 0, 1

    count = text.count(old)
    if count > 1:
        print(f"  x AMBIGUO ({count} matches): {label}", file=sys.stderr)
        return text, 0, 1

    print(f"  ok {label}")
    return text.replace(old, new, 1), 1, 0


def main() -> int:
    if not DOC.exists():
        print(f"No existe {DOC}", file=sys.stderr)
        return 1

    text = DOC.read_text(encoding="utf-8")
    changes = 0
    errors = 0

    replacements: list[tuple[str, str, str]] = [
        # (old, new, label)
        # ("texto exacto antiguo", "texto exacto nuevo", "descripcion"),
    ]

    for old, new, label in replacements:
        text, delta, err = replace_once(text, old, new, label)
        changes += delta
        errors += err

    if errors:
        print(f"\n{errors} error(es); no se escribio el archivo.", file=sys.stderr)
        return 1
    if changes:
        DOC.write_text(text, encoding="utf-8")
        print(f"\n{changes} cambio(s) aplicado(s).")
    else:
        print("\nNada que cambiar.")
    return 0


if __name__ == "__main__":
    sys.exit(main())