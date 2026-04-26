"""Linter del manuscrito Markdown."""
from pathlib import Path
import re

REPO_ROOT = Path(__file__).resolve().parents[1]
MD = REPO_ROOT / "content" / "manuscript" / "Documento_Tesis.md"


def test_manuscript_exists():
    assert MD.exists(), f"Falta el manuscrito: {MD}"


def test_image_paths_resolve():
    """Toda imagen referenciada debe existir físicamente."""
    text = MD.read_text(encoding="utf-8")
    pattern = re.compile(r"!\[[^\]]*\]\(([^)]+\.(?:png|jpg|jpeg|svg))\)", re.IGNORECASE)
    md_dir = MD.parent
    missing = []
    for m in pattern.finditer(text):
        ref = m.group(1).split(" ")[0]
        # Solo paths relativos (no http/https)
        if ref.startswith(("http://", "https://")):
            continue
        target = (md_dir / ref).resolve()
        if not target.exists():
            missing.append(ref)
    assert not missing, f"Imágenes referenciadas que no existen: {missing}"


def test_no_html_pagebreak():
    """Saltos de página deben ser \\newpage, no <div style=...>."""
    text = MD.read_text(encoding="utf-8")
    assert "page-break-after" not in text, "Usar \\newpage en vez de CSS"
    assert "<br" not in text.lower() or text.lower().count("<br") < 5, \
        "Demasiados <br>; preferir saltos Markdown"


def test_no_lazy_phrases():
    """Frases prohibidas que generan ambigüedad referencial."""
    text = MD.read_text(encoding="utf-8").lower()
    forbidden = ["siguiente figura", "siguiente tabla", "tabla anterior", "figura anterior"]
    found = [p for p in forbidden if p in text]
    assert not found, f"Frases ambiguas (usar referencia explícita @fig:/@tbl:): {found}"
