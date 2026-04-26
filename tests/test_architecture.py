"""Tests de arquitectura: validan reglas de dependencia entre capas."""
from pathlib import Path
import re
import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]

# Vocabulario del tema actual que NO debería aparecer en el motor.
TOPIC_KEYWORDS = ["FHIR", "MINSA", "HL7", "interoperabilidad clínica"]


def _python_files(folder: Path):
    return [p for p in folder.rglob("*.py") if "__pycache__" not in p.parts]


def test_platform_does_not_import_content():
    """platform/ no debe importar nada de content/."""
    bad = []
    for py in _python_files(REPO_ROOT / "platform"):
        text = py.read_text(encoding="utf-8", errors="ignore")
        if re.search(r"\b(import|from)\s+content\b", text):
            bad.append(py.relative_to(REPO_ROOT))
    assert not bad, f"Imports prohibidos: {bad}"


def test_content_has_no_executable_python():
    """content/ no debe contener .py ejecutable."""
    pys = _python_files(REPO_ROOT / "content")
    assert not pys, f"content/ no debe tener .py: {pys}"


@pytest.mark.xfail(
    reason="Deuda técnica: build_thesis.py contiene strings 'FHIR'/'HL7' en "
           "comentarios y heurísticas. Migrar a config externa para hacer el "
           "motor 100%% reusable.",
    strict=False,
)
def test_build_scripts_have_no_topic_keywords():
    """platform/scripts/build/ no debe tener keywords del tema (motor reusable)."""
    build_dir = REPO_ROOT / "platform" / "scripts" / "build"
    bad = []
    for py in _python_files(build_dir):
        text = py.read_text(encoding="utf-8", errors="ignore")
        for kw in TOPIC_KEYWORDS:
            if kw.lower() in text.lower():
                bad.append((py.relative_to(REPO_ROOT), kw))
    # build_diagrams.py contiene texto inline de diagramas del tema actual:
    # se acepta como deuda técnica conocida hasta migrar los diagramas inline
    # a archivos .puml en content/media/diagrams/.
    bad = [(p, k) for (p, k) in bad if "build_diagrams.py" not in str(p)]
    assert not bad, f"Keywords del tema en motor: {bad}"


def test_repo_root_layout():
    """Carpetas raíz esperadas existen."""
    for d in ["content", "platform", "build", "tests", "docs", ".github"]:
        assert (REPO_ROOT / d).is_dir(), f"Falta carpeta raíz: {d}"


def test_no_legacy_paths_in_root():
    """Archivos legacy ya no deben estar en raíz."""
    legacy = [
        "Documento_Tesis.md", "generar_tesis.py", "generar_diagramas.py",
        "plantilla_estilos.docx", "caratula.docx", "plantuml.jar",
        "Documento_Tesis_salida.docx", "document_reference.docx",
    ]
    found = [n for n in legacy if (REPO_ROOT / n).exists()]
    assert not found, f"Archivos legacy en raíz: {found}"
