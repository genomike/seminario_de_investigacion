"""Tests de arquitectura: validan reglas de dependencia entre capas."""
from pathlib import Path
import re

REPO_ROOT = Path(__file__).resolve().parents[1]


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


def test_build_scripts_do_not_embed_topic_content():
    """platform/scripts/build/ no debe traer contenido de una tesis concreta."""
    build_dir = REPO_ROOT / "platform" / "scripts" / "build"
    bad = []
    for py in _python_files(build_dir):
        text = py.read_text(encoding="utf-8", errors="ignore")
        if "@startuml" in text or "@startgantt" in text:
            bad.append(py.relative_to(REPO_ROOT))
    assert not bad, f"Diagramas hardcodeados en motor: {bad}"


def test_platform_scripts_do_not_embed_external_source_urls():
    """Las URLs de fuentes pertenecen a content/, no al motor reusable."""
    allowed_technical_hosts = [
        "schemas.openxmlformats.org",
        "purl.oclc.org",
        "www.w3.org",
    ]
    script_dirs = [
        REPO_ROOT / "platform" / "scripts" / "build",
        REPO_ROOT / "platform" / "scripts" / "fixes",
        REPO_ROOT / "platform" / "scripts" / "downloads",
    ]
    bad = []
    for folder in script_dirs:
        for script in list(folder.rglob("*.py")) + list(folder.rglob("*.ps1")):
            text = script.read_text(encoding="utf-8", errors="ignore")
            urls = re.findall(r"https?://[^\"'\s<>]+", text)
            external_urls = [
                url for url in urls
                if not any(host in url for host in allowed_technical_hosts)
            ]
            if external_urls:
                bad.append((script.relative_to(REPO_ROOT), external_urls))
    assert not bad, f"URLs de fuentes hardcodeadas en platform/: {bad}"


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
