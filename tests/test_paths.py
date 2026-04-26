"""Tests para constantes de rutas en build_thesis y build_diagrams."""
from pathlib import Path
import importlib.util
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]


def _load(modname: str, relpath: str):
    spec = importlib.util.spec_from_file_location(modname, REPO_ROOT / relpath)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    sys.modules[modname] = mod
    spec.loader.exec_module(mod)
    return mod


def test_build_thesis_paths_resolve_under_repo():
    bt = _load("bt", "platform/scripts/build/build_thesis.py")
    assert bt.REPO_ROOT == REPO_ROOT
    assert bt.PLANTILLA == REPO_ROOT / "platform" / "templates" / "styles" / "plantilla_estilos.docx"
    assert bt.CARATULA_MANUAL == REPO_ROOT / "platform" / "templates" / "styles" / "caratula.docx"
    assert bt.ENTRADA == REPO_ROOT / "content" / "manuscript" / "Documento_Tesis.md"
    assert bt.SALIDA == REPO_ROOT / "build" / "tesis.docx"
    assert bt.REFERENCE == REPO_ROOT / "build" / "_reference.docx"
    assert bt.CUERPO_TEMP == REPO_ROOT / "build" / "_cuerpo_tesis_temp.docx"


def test_build_thesis_required_files_exist():
    bt = _load("bt2", "platform/scripts/build/build_thesis.py")
    assert bt.PLANTILLA.exists(), f"Falta {bt.PLANTILLA}"
    assert bt.CARATULA_MANUAL.exists(), f"Falta {bt.CARATULA_MANUAL}"
    assert bt.ENTRADA.exists(), f"Falta {bt.ENTRADA}"


def test_build_diagrams_paths():
    bd = _load("bd", "platform/scripts/build/build_diagrams.py")
    assert bd.REPO_ROOT == REPO_ROOT
    assert bd.DIAGRAMS_DIR == REPO_ROOT / "content" / "media" / "diagrams"
    assert bd.FIGURES_DIR == REPO_ROOT / "content" / "media" / "figures"
    assert bd.PLANTUML_JAR == REPO_ROOT / "platform" / "tools" / "plantuml.jar"
    assert bd.PLANTUML_JAR.exists(), "plantuml.jar debe existir en platform/tools/"
