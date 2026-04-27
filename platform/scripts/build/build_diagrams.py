"""Renderiza diagramas PlantUML del repositorio (`*.puml` -> `*.png`).

Motor agnostico al tema: descubre los archivos `.puml` ubicados en
`content/media/diagrams/` y los renderiza con `platform/tools/plantuml.jar`,
dejando los PNG en `content/media/figures/`.

Uso:
    python platform/scripts/build/build_diagrams.py
"""
from __future__ import annotations

from pathlib import Path
import subprocess
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
DIAGRAMS_DIR = REPO_ROOT / "content" / "media" / "diagrams"
FIGURES_DIR = REPO_ROOT / "content" / "media" / "figures"
PLANTUML_JAR = REPO_ROOT / "platform" / "tools" / "plantuml.jar"


def render_all() -> int:
    DIAGRAMS_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    if not PLANTUML_JAR.exists():
        print(f"ERROR: no se encontro {PLANTUML_JAR}", file=sys.stderr)
        return 2

    puml_files = sorted(DIAGRAMS_DIR.glob("*.puml"))
    if not puml_files:
        print(f"(sin diagramas) No hay archivos .puml en {DIAGRAMS_DIR}")
        return 0

    print(f"Renderizando {len(puml_files)} diagrama(s) en {FIGURES_DIR}")
    command = [
        "java",
        "-jar",
        str(PLANTUML_JAR),
        "-tpng",
        "-o",
        str(FIGURES_DIR),
        *[str(path) for path in puml_files],
    ]
    result = subprocess.run(command, check=False)
    if result.returncode != 0:
        print(f"ERROR: plantuml retorno {result.returncode}", file=sys.stderr)
        return result.returncode

    print("OK.")
    return 0


if __name__ == "__main__":
    sys.exit(render_all())
