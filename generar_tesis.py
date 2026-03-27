"""
Genera Documento_Tesis.docx desde Documento_Tesis.md usando pandoc.

Pasos:
  1. Crea 'reference_portada.docx' basado en la plantilla, añadiendo el
     estilo 'Portada-Centrado' (centrado, sin salto automático de página).
    2. Ejecuta pandoc con ese reference-doc para generar el .docx base.
    3. Postprocesa el .docx para aplicar:
         - índice automático con formato Word,
         - índice de tablas e índice de figuras,
         - saltos de página en secciones preliminares,
         - numeración de títulos de nivel 2 y 3 por capítulo.

Uso:
  python generar_tesis.py
"""

# pyright: reportPrivateUsage=false
# pylint: disable=protected-access

import re
import locale
import subprocess
import sys
from pathlib import Path

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

BASE = Path(__file__).parent
PLANTILLA = BASE / "Plantilla de informe de tesis maestría.docx"
REFERENCE = BASE / "reference_portada.docx"
ENTRADA = BASE / "Documento_Tesis.md"
SALIDA = BASE / "Documento_Tesis_salida.docx"
SALIDA_ALT = BASE / "Documento_Tesis_salida_nueva.docx"


def crear_reference_doc():
    """Añade el estilo 'Portada-Centrado' a la plantilla y guarda como referencia."""
    doc = Document(str(PLANTILLA))

    # Evitar duplicar el estilo si ya existe
    nombres_estilos = [s.name for s in doc.styles]

    if "Portada-Centrado" not in nombres_estilos:
        estilo = doc.styles.add_style("Portada-Centrado", WD_STYLE_TYPE.PARAGRAPH)
        estilo.base_style = doc.styles["Normal"]
        fmt = estilo.paragraph_format
        fmt.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fmt.space_before = Pt(6)
        fmt.space_after = Pt(6)
        fmt.keep_with_next = False
        # Hereda la fuente de Normal; solo ajustamos que NO sea Heading
        print("  Estilo 'Portada-Centrado' creado.")
    else:
        print("  Estilo 'Portada-Centrado' ya existe en la plantilla.")

    doc.save(str(REFERENCE))
    print(f"  Reference doc guardado: {REFERENCE.name}")


def ejecutar_pandoc(destino):
    """Llama a pandoc para convertir el markdown al docx."""
    cmd = [
        "pandoc",
        str(ENTRADA),
        f"--reference-doc={REFERENCE}",
        "--from", "markdown+fenced_divs+raw_tex+pipe_tables+table_captions",
        "--to", "docx",
        "-o", str(destino),
    ]
    print(f"\nEjecutando: {' '.join(cmd)}\n")
    resultado = subprocess.run(cmd, capture_output=True, text=False, check=False)
    preferida = locale.getpreferredencoding(False) or "utf-8"
    try:
        stdout = resultado.stdout.decode("utf-8")
    except UnicodeDecodeError:
        stdout = resultado.stdout.decode(preferida, errors="replace")
    try:
        stderr = resultado.stderr.decode("utf-8")
    except UnicodeDecodeError:
        stderr = resultado.stderr.decode(preferida, errors="replace")

    if resultado.returncode != 0:
        print("ERROR de pandoc:")
        print(stderr)
        return False
    else:
        if stderr:
            print("Advertencias pandoc:", stderr)
        if stdout:
            print(stdout)
        print(f"\nDocumento generado correctamente: {destino.name}")
        return True


def insertar_parrafo_despues(parrafo, texto=""):
    """Inserta un párrafo nuevo justo después del párrafo recibido."""
    nuevo_p = OxmlElement("w:p")
    parrafo._p.addnext(nuevo_p)  # pyright: ignore[reportPrivateUsage]
    nuevo = parrafo._parent.add_paragraph()  # pyright: ignore[reportPrivateUsage]
    nuevo._p.getparent().remove(nuevo._p)  # pyright: ignore[reportPrivateUsage]
    nuevo._p = nuevo_p  # pyright: ignore[reportPrivateUsage]
    if texto:
        nuevo.add_run(texto)
    return nuevo


def insertar_campo_word(parrafo, instruccion, texto_placeholder="Actualice campos (F9)"):
    """Inserta un campo de Word (TOC, lista de tablas, lista de figuras)."""
    run = parrafo.add_run()
    r = run._r  # pyright: ignore[reportPrivateUsage]

    fld_char_begin = OxmlElement("w:fldChar")
    fld_char_begin.set(qn("w:fldCharType"), "begin")

    instr_text = OxmlElement("w:instrText")
    instr_text.set(qn("xml:space"), "preserve")
    instr_text.text = instruccion

    fld_char_sep = OxmlElement("w:fldChar")
    fld_char_sep.set(qn("w:fldCharType"), "separate")

    text = OxmlElement("w:t")
    text.text = texto_placeholder

    fld_char_end = OxmlElement("w:fldChar")
    fld_char_end.set(qn("w:fldCharType"), "end")

    r.append(fld_char_begin)
    r.append(instr_text)
    r.append(fld_char_sep)
    r.append(text)
    r.append(fld_char_end)


def activar_actualizacion_campos(doc):
    """Hace que Word actualice TOC/campos al abrir el documento."""
    settings = doc.settings.element
    update_fields = settings.find(qn("w:updateFields"))
    if update_fields is None:
        update_fields = OxmlElement("w:updateFields")
        settings.append(update_fields)
    update_fields.set(qn("w:val"), "true")


def aplicar_saltos_pagina_encabezados(doc):
    """Aplica salto de página antes de los encabezados clave."""
    objetivos = {
        "Agradecimiento",
        "Índice",
        "Índice de tablas",
        "Índice de figuras",
        "Resumen",
        "Abstract",
        "Introducción",
        "Referencias",
        "Anexos",
    }
    for p in doc.paragraphs:
        texto = p.text.strip()
        estilo = p.style.name if p.style is not None else ""

        if texto in objetivos:
            p.paragraph_format.page_break_before = True
        elif estilo == "Heading 1" and texto.startswith("Capítulo "):
            p.paragraph_format.page_break_before = True


def aplicar_numeracion_titulos(doc):
    """Numera Heading 2/3 por capítulo para aproximar el formato solicitado."""
    capitulo_actual = 0
    nivel2 = 0
    nivel3 = 0
    dentro_de_capitulo = False

    for p in doc.paragraphs:
        estilo = p.style.name if p.style is not None else ""
        texto = p.text.strip()

        if estilo == "Heading 1":
            if texto.startswith("Capítulo "):
                capitulo_actual += 1
                nivel2 = 0
                nivel3 = 0
                dentro_de_capitulo = True
                if ": " in texto:
                    p.text = texto.replace(": ", ".- ", 1)
            else:
                dentro_de_capitulo = False

        elif dentro_de_capitulo and estilo == "Heading 2":
            nivel2 += 1
            nivel3 = 0
            limpio = re.sub(r"^\d+\.\d+\.?\s*(->\s*)?", "", texto)
            p.text = f"{capitulo_actual}.{nivel2}. -> {limpio}"

        elif dentro_de_capitulo and estilo == "Heading 3":
            nivel3 += 1
            limpio = re.sub(r"^\d+\.\d+\.\d+\.?\s*(->\s*)?", "", texto)
            p.text = f"{capitulo_actual}.{nivel2}.{nivel3}. -> {limpio}"


def _ajustar_fuente_runs(parrafo, tamano_pt, negrita=None):
    """Ajusta tamaño (y opcionalmente negrita) en runs no vacíos."""
    for run in parrafo.runs:
        if run.text and run.text.strip():
            run.font.size = Pt(tamano_pt)
            if negrita is not None:
                run.bold = negrita


def _eliminar_parrafo(parrafo):
    """Elimina un párrafo del documento."""
    elemento = parrafo._element  # pyright: ignore[reportPrivateUsage]
    padre = elemento.getparent()
    if padre is not None:
        padre.remove(elemento)


def ajustar_caratula(doc):
    """Aproxima la carátula al formato esperado (logo, jerarquía y espaciado)."""
    # Reducir altura del logo para acercarse a la plantilla objetivo.
    if doc.inline_shapes:
        doc.inline_shapes[0].width = Inches(2.9)
        doc.inline_shapes[0].height = Inches(0.95)

    # Ubicar fin de carátula usando el año.
    fin = None
    for idx, p in enumerate(doc.paragraphs):
        if p.text.strip() == "2026":
            fin = idx
            break
    if fin is None:
        return

    # Limpiar líneas vacías de la portada (excepto el párrafo del logo).
    for p in list(doc.paragraphs[: fin + 1]):
        texto = p.text.strip()
        tiene_logo = "w:drawing" in p._p.xml
        if not texto and not tiene_logo:
            _eliminar_parrafo(p)

    # Recalcular fin de portada tras limpieza.
    fin = None
    for idx, p in enumerate(doc.paragraphs):
        if p.text.strip() == "2026":
            fin = idx
            break
    if fin is None:
        return

    # Espaciado adaptativo: si la carátula creciera demasiado, compacta.
    texto_portada = " ".join(p.text.strip() for p in doc.paragraphs[: fin + 1] if p.text.strip())
    modo_compacto = len(texto_portada) > 650
    factor = 0.82 if modo_compacto else 1.0

    for idx, p in enumerate(doc.paragraphs[: fin + 1]):
        texto = p.text.strip()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.15

        # Párrafo del logo (sin texto, con drawing embebido).
        if not texto and "w:drawing" in p._p.xml:
            p.paragraph_format.space_before = Pt(18 * factor)
            p.paragraph_format.space_after = Pt(22 * factor)
            continue

        if texto == "MAESTRÍA EN INGENIERÍA DE SOFTWARE":
            _ajustar_fuente_runs(p, 17, True)
            p.paragraph_format.space_after = Pt(14 * factor)
        elif texto == "PROYECTO DE TESIS":
            _ajustar_fuente_runs(p, 16, True)
            p.paragraph_format.space_after = Pt(18 * factor)
        elif "MODELO DE INTEROPERABILIDAD BASADO EN HL7 FHIR" in texto:
            _ajustar_fuente_runs(p, 15, True)
            p.paragraph_format.space_after = Pt(18 * factor)
        elif texto == "PRESENTADO POR:":
            _ajustar_fuente_runs(p, 14, False)
            p.paragraph_format.space_after = Pt(12 * factor)
        elif texto.startswith("Bach."):
            _ajustar_fuente_runs(p, 14, True)
            p.paragraph_format.space_after = Pt(7 * factor)
        elif texto == "PARA OPTAR EL GRADO ACADÉMICO DE:":
            _ajustar_fuente_runs(p, 14, False)
            p.paragraph_format.space_before = Pt(10 * factor)
            p.paragraph_format.space_after = Pt(12 * factor)
        elif texto == "MAESTRO(A) EN INGENIERÍA DE SOFTWARE":
            _ajustar_fuente_runs(p, 16, True)
            p.paragraph_format.space_after = Pt(10 * factor)
        elif texto == "LIMA":
            _ajustar_fuente_runs(p, 13, False)
            p.paragraph_format.space_after = Pt(6 * factor)
        elif texto == "2026":
            _ajustar_fuente_runs(p, 13, False)


def excluir_preliminares_del_toc(doc):
    """Quita Agradecimiento del TOC cambiando su estilo a Normal."""
    excluir = {"Agradecimiento"}
    for p in doc.paragraphs:
        if p.text.strip() in excluir:
            p.style = doc.styles["Normal"]
            _ajustar_fuente_runs(p, 16, True)


def insertar_indices_automaticos(doc):
    """Inserta TOC y listas automáticas en sus respectivas secciones."""
    for p in list(doc.paragraphs):
        titulo = p.text.strip()
        if titulo == "Índice":
            destino = insertar_parrafo_despues(p)
            insertar_campo_word(destino, 'TOC \\o "1-3" \\h \\z \\u')
        elif titulo == "Índice de tablas":
            destino = insertar_parrafo_despues(p)
            insertar_campo_word(destino, 'TOC \\h \\z \\c "Table"')
        elif titulo == "Índice de figuras":
            destino = insertar_parrafo_despues(p)
            insertar_campo_word(destino, 'TOC \\h \\z \\c "Figure"')


def aplicar_bordes_tablas(doc):
    """Fuerza bordes visibles en todas las tablas."""
    for tabla in doc.tables:
        tabla.style = "Table Grid"

        tbl = tabla._tbl  # pyright: ignore[reportPrivateUsage]
        tbl_pr = tbl.tblPr

        bordes = tbl_pr.find(qn("w:tblBorders"))
        if bordes is not None:
            tbl_pr.remove(bordes)

        bordes = OxmlElement("w:tblBorders")
        for borde in ("top", "left", "bottom", "right", "insideH", "insideV"):
            el = OxmlElement(f"w:{borde}")
            el.set(qn("w:val"), "single")
            el.set(qn("w:sz"), "8")
            el.set(qn("w:space"), "0")
            el.set(qn("w:color"), "000000")
            bordes.append(el)

        tbl_pr.append(bordes)


def actualizar_campos_con_word(destino):
    """Actualiza TOC/índices y campos usando Word COM para guardar números finales."""
    path = str(destino).replace("'", "''")
    script = rf"""
$ErrorActionPreference = 'Stop'
$path = '{path}'
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
$doc = $word.Documents.Open($path)
$doc.Repaginate() | Out-Null
foreach ($toc in $doc.TablesOfContents) {{ $toc.Update() }}
foreach ($tof in $doc.TablesOfFigures) {{ $tof.Update() }}
$doc.Fields.Update() | Out-Null
$doc.Save()
$doc.Close()
$word.Quit()
"""
    resultado = subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", script],
        capture_output=True,
        text=True,
        check=False,
    )
    if resultado.returncode == 0:
        print("Campos de Word actualizados automáticamente (TOC/índices).")
    else:
        print("No se pudo actualizar campos con Word automáticamente.")
        if resultado.stderr:
            print(resultado.stderr)


def postprocesar_docx(destino):
    """Aplica formato y campos Word después de la conversión de pandoc."""
    doc = Document(str(destino))
    ajustar_caratula(doc)
    excluir_preliminares_del_toc(doc)
    aplicar_numeracion_titulos(doc)
    aplicar_saltos_pagina_encabezados(doc)
    insertar_indices_automaticos(doc)
    aplicar_bordes_tablas(doc)
    activar_actualizacion_campos(doc)
    doc.save(str(destino))
    actualizar_campos_con_word(destino)
    print("Postproceso DOCX completado (índices, saltos y numeración).")


if __name__ == "__main__":
    print("=== Preparando reference doc con estilos de portada ===")
    crear_reference_doc()
    print("\n=== Ejecutando pandoc ===")
    salida_objetivo = SALIDA
    exito = ejecutar_pandoc(salida_objetivo)
    if not exito:
        print("\nEl archivo principal parece estar bloqueado. Se generará salida alternativa.")
        salida_objetivo = SALIDA_ALT
        if not ejecutar_pandoc(salida_objetivo):
            sys.exit(1)
    print("\n=== Aplicando postproceso DOCX ===")
    postprocesar_docx(salida_objetivo)
