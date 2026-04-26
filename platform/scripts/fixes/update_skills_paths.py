"""Actualiza paths legacy en .github/skills/*.md tras la reestructuración."""
from pathlib import Path
import re

REPO = Path(__file__).resolve().parents[1]
SKILLS = REPO / ".github" / "skills"

REPLACEMENTS = [
    # (regex, replacement)
    (r"\bgenerar_tesis\.py\b", "platform/scripts/build/build_thesis.py"),
    (r"\bgenerar_diagramas\.py\b", "platform/scripts/build/build_diagrams.py"),
    (r"\(\.\./\.\./Documento_Tesis\.md\)", "(../../content/manuscript/Documento_Tesis.md)"),
    (r"\(\.\./\.\./Documento_Tesis_salida\.docx\)", "(../../build/tesis.docx)"),
    (r"`Documento_Tesis_salida\.docx`", "`build/tesis.docx`"),
    (r"`Documento_Tesis\.md`", "`content/manuscript/Documento_Tesis.md`"),
    (r"`plantilla_estilos\.docx`", "`platform/templates/styles/plantilla_estilos.docx`"),
    (r"`caratula\.docx`", "`platform/templates/styles/caratula.docx`"),
    (r"`plantuml\.jar`", "`platform/tools/plantuml.jar`"),
    (r"`guia-apa7-tesis\.md`", "`platform/templates/guides/guia-apa7-tesis.md`"),
    (r"`documentos_apoyo/`", "`platform/templates/guides/`"),
    (r"\(\.\./\.\./\.\./observaciones/\)", "(../../../content/observations/)"),
    (r"`fuentes/`", "`content/sources/`"),
    (r"`fuentes/internacionales/`", "`content/sources/international/`"),
    (r"`fuentes/nacionales/`", "`content/sources/national/`"),
    (r"`media/`", "`content/media/figures/`"),
    (r"`diagramas/`", "`content/media/diagrams/`"),
    (r"`observaciones/`", "`content/observations/`"),
    (r"`tesis/`", "`content/drafts/`"),
    (r"!\[Caption\]\(media/diagrama-x\.png\)", "![Caption](../media/figures/diagrama-x.png)"),
    (r"`scripts/`", "`platform/scripts/fixes/`"),
    (r"`scripts/fix_", "`platform/scripts/fixes/fix_"),
    (r"`scripts/add_", "`platform/scripts/fixes/add_"),
    (r"`scripts/download_", "`platform/scripts/downloads/download_"),
    (r"`scripts/retry_", "`platform/scripts/downloads/retry_"),
]

count = 0
for f in SKILLS.rglob("*.md"):
    orig = f.read_text(encoding="utf-8")
    new = orig
    for pat, repl in REPLACEMENTS:
        new = re.sub(pat, repl, new)
    if new != orig:
        f.write_text(new, encoding="utf-8")
        print(f"  upd: {f.relative_to(REPO)}")
        count += 1
print(f"Total actualizados: {count}")
