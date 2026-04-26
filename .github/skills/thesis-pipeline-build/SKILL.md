---
name: thesis-pipeline-build
description: Ejecutar el build de la tesis (Markdown → DOCX) con `platform/scripts/build/build_thesis.py` y depurar problemas de la salida. Usar cuando el usuario pide "generar el documento", "exportar a Word", "compilar la tesis", o cuando reporta un problema visible solo en el DOCX (índices vacíos, numeración rota, tabla sin formato, viñetas como números, etc.).
---

# Build de la tesis

## Comando estándar

```powershell
# desde la raíz del repo
python platform/scripts/build/build_thesis.py
```

Salida esperada: `build/tesis.docx` en la raíz, listo para
abrir en Word.

## Dependencias

- **Pandoc** ≥ 3.0 en el `PATH`.
- **Python** 3.10+ con `python-docx` y `lxml` instalados.
- **Java** (JRE 8+) para PlantUML, **solo** si hay diagramas a regenerar.
- `platform/tools/plantuml.jar` en la raíz (ya versionado).
- `pandoc-crossref` **opcional**; si se usa, las referencias `@tbl:slug`
  funcionan; si no, mantener referencias manuales `Tabla N`.

Verificación rápida:

```powershell
pandoc --version | Select-Object -First 1
python -c "import docx, lxml; print('ok')"
```

## Pasos internos del script (resumen)

1. `preparar_reference_doc()` — copia `platform/templates/styles/plantilla_estilos.docx` a
   `document_reference.docx` y le inyecta los custom-styles que faltan.
2. `_filtrar_secciones_excluidas()` — quita Resumen/Abstract/Introducción
   del cuerpo principal porque ya van en preliminares.
3. `_cerrar_procesos_bloqueando_docx()` — intenta cerrar Word/LibreOffice/WPS
   si tienen el DOCX bloqueado.
4. `ejecutar_pandoc()` — invoca:

   ```text
   pandoc Documento_Tesis.md
     --from markdown+fenced_divs+raw_tex+pipe_tables+table_captions
     --reference-doc=document_reference.docx
     --output=build/tesis.docx
   ```

5. Postproceso (`python-docx`):
   - Inserta TOC / LOT / LOF.
   - Numera Heading 2/3 por capítulo.
   - Aplica bordes horizontales a tablas con caption `Tabla N.`.
   - `convertir_listas_a_bullets()` arregla numIds huérfanos.
   - Concatena `platform/templates/styles/caratula.docx` al inicio si existe.

## Diagrama de flujo de troubleshooting

| Síntoma en el DOCX | Causa probable | Acción |
|---|---|---|
| Documento no se genera, error de bloqueo | Word abierto | Cerrar Word; reintentar |
| Índice vacío | Word no actualiza campos al abrir | En Word: Ctrl+A → F9 |
| Numeración 1.1, 1.2 reinicia mal | Heading 2 fuera del Capítulo correcto | Verificar jerarquía Heading 1 → 2 |
| Tabla con bordes verticales | Caption mal formado o pegado a la tabla | Ver `thesis-tablas-apa` |
| Viñetas son números (1, 2, 3) en vez de `•` | numId huérfano de Pandoc | Confirmar que `convertir_listas_a_bullets()` corrió |
| Imagen pixelada | PNG renderizado a baja resolución | Regenerar diagrama con `dpi 150` |
| Diagrama acentos rotos (`Â`) | UTF-8 mal en `.puml` | Usar placeholders `{a1}{e1}…` |
| Portada descuadrada | Falta `platform/templates/styles/caratula.docx` y los divs `Portada-Centrado` no están en el MD | Ver `thesis-portada` |
| Resumen aparece dos veces | No se filtró del cuerpo | Verificar que la sección esté entre los headings de preliminares |
| Caption de tabla aparece debajo y no arriba | Caption posicionado mal en pipe table | Caption va **antes** de la tabla con `: Tabla N. Título` |

## Regenerar diagramas antes del build

```powershell
python platform/scripts/build/build_diagrams.py        # .puml -> .png
python platform/scripts/build/build_thesis.py
```

`build_thesis.py` no debe modificar `.puml` ni regenerar figuras.
Su responsabilidad es construir el DOCX a partir del Markdown de entrada
y los recursos ya existentes.

## Validaciones manuales obligatorias antes de entregar

- [ ] Abrir el DOCX en Word, hacer Ctrl+A y F9 para refrescar todos los campos
  (TOC, LOT, LOF, números de página).
- [ ] Recorrer el documento mirando: portada, índice, primer capítulo,
  cada tabla y figura, referencias.
- [ ] Validar que ninguna tabla quede partida horriblemente entre páginas
  (si pasa, en Word: *Repetir como fila de encabezado*).
- [ ] Buscar `siguiente figura` y `siguiente tabla` con Ctrl+F (deben ser 0).

## Anti-patrones

- Ejecutar `pandoc` directamente sin pasar por `platform/scripts/build/build_thesis.py` (pierde
  el postproceso → tablas, índices, numeración salen mal).
- Editar `build/tesis.docx` y commitearlo: es output, no input.
- Hacer commit del `document_reference.docx`: idem.
- Cambiar el flag de Pandoc a `--from markdown` (sin las extensiones):
  rompe pipe tables con caption.
