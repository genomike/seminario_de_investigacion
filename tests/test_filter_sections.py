"""Tests para _filtrar_secciones_excluidas en build_thesis.py."""
from pathlib import Path
import importlib.util
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]


def _load_bt():
    spec = importlib.util.spec_from_file_location(
        "bt_filter", REPO_ROOT / "platform" / "scripts" / "build" / "build_thesis.py"
    )
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    sys.modules["bt_filter"] = mod
    spec.loader.exec_module(mod)
    return mod


def test_filter_excludes_section():
    bt = _load_bt()
    # Asegurar que SECCIONES_EXCLUIDAS contiene "Resumen"
    assert "Resumen" in bt.SECCIONES_EXCLUIDAS

    md = "\\newpage\n\n# Resumen\n\nContenido del resumen.\n\n\\newpage\n\n# Capítulo I\n\nTexto.\n"
    out = bt._filtrar_secciones_excluidas(md)
    assert "Resumen" not in out
    assert "Capítulo I" in out
    assert "Texto." in out


def test_filter_idempotent():
    bt = _load_bt()
    md = "# Capítulo I\n\nTexto.\n"
    assert bt._filtrar_secciones_excluidas(md) == md


def test_filter_preserves_subheadings_with_same_name():
    """Un H2 llamado 'Resumen' (## Resumen) NO debe excluirse, solo H1."""
    bt = _load_bt()
    md = "# Capítulo I\n\n## Resumen\n\nResumen del capítulo.\n"
    out = bt._filtrar_secciones_excluidas(md)
    assert "## Resumen" in out
    assert "Resumen del capítulo." in out
