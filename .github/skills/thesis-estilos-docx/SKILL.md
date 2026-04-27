---
name: thesis-estilos-docx
description: Modificar el reference-doc DOCX (estilos Word) que Pandoc usa para renderizar la tesis. Usar cuando hay que ajustar fuente, márgenes, sangría, interlineado, encabezados, numeración Word, o crear/editar custom-styles como "Portada-Centrado".
---

# Reference-doc DOCX y custom-styles

## Archivos involucrados

- `platform/templates/styles/plantilla_estilos.docx` — fuente principal de estilos (en repo).
- `build/_reference.docx` — copia preparada por
  `build_thesis.preparar_reference_doc()` (no editar a mano; se
  regenera en cada build).
- `platform/templates/styles/caratula.docx` — opcional; si existe se concatena al inicio.

## Especificaciones APA 7 que viven en `platform/templates/styles/plantilla_estilos.docx`

| Aspecto | Valor |
|---|---|
| Fuente | Times New Roman |
| Tamaño cuerpo | 12 pt |
| Interlineado | 2.0 (doble) |
| Márgenes | 2.54 cm (1") en los 4 lados |
| Sangría primera línea | 1.27 cm (0.5") |
| Alineación cuerpo | Izquierda (no justificado) |
| Espacio antes/después de párrafo | 0 |
| Numeración de página | Arábiga, esquina superior derecha; preliminares en romanos |
| Encabezados (`Heading 1`) | TNR 12 pt, negrita, centrado |
| `Heading 2`, `Heading 3` | TNR 12 pt, negrita, alineados a la izquierda |
| Bibliografía (`Bibliography`) | Sangría francesa de 1.27 cm; sin viñetas |
| `Caption` | TNR 11 pt, cursiva |
| `Quote` (cita en bloque) | Sangría izquierda 1.27 cm; sin comillas |

## Custom-styles definidos

| Style | Uso |
|---|---|
| `Portada-Centrado` | Cada línea de la portada cuando se construye desde Markdown (ver `thesis-portada`). |
| `toc 1`, `toc 2`, `toc 3` | Entradas del índice (Pandoc/Word los genera). |
| `table of figures` | Entradas del índice de tablas e índice de figuras. |
| `Bibliography` | Lista de referencias (sangría francesa, sin viñetas). |
| `Caption` | Captions de tablas y figuras. |

> **No** renombrar estos estilos. `platform/scripts/build/build_thesis.py` y los divs
> `::: {custom-style="…"}` en el Markdown los referencian por nombre.

## Cómo editar `platform/templates/styles/plantilla_estilos.docx`

1. Cerrar Word para evitar bloqueos.
2. Abrir `platform/templates/styles/plantilla_estilos.docx`.
3. Modificar el estilo en *Inicio → Estilos → modificar*. Confirmar
   que el cambio quede a nivel de **estilo**, no de párrafo.
4. Guardar y cerrar.
5. Borrar `build/_reference.docx` para forzar regeneración.
6. Ejecutar `python platform/scripts/build/build_thesis.py` y validar el DOCX resultante.

## Cuando los cambios "no se ven"

Causas frecuentes:

- Word tiene el archivo abierto → `_cerrar_procesos_bloqueando_docx()`
  intenta matar `WINWORD/SOFFICE/WPS`, pero a veces hay procesos
  fantasma. Verificar con `Get-Process | Where-Object Name -in
  WINWORD,soffice,wps`.
- El estilo se cambió a nivel de párrafo y no de definición de estilo.
- El cuerpo del Markdown está aplicando un override (ej. `<span
  style="…">`) que pisa el estilo.
- `build/_reference.docx` quedó del build anterior — borrar y
  regenerar.

## Postproceso adicional vía `python-docx`

`platform/scripts/build/build_thesis.py` realiza ajustes que **no** se hacen vía estilos:

- Inserta los campos `TOC`, `LOT` (lista de tablas) y `LOF` (lista de
  figuras) usando `OxmlElement`.
- Numera `Heading 2` como `N.M.` y `Heading 3` como `N.M.K.` por
  capítulo (no global).
- Aplica bordes solo horizontales a tablas con caption `Tabla N.`.
- Crea un `abstractNum` único de tipo bullet y reasigna `numId`
  huérfanos (efecto: que las viñetas se vean como `•` en vez de
  numeración decimal arbitraria).
- Inserta el número en negrita y el título en cursiva sobre cada
  tabla/figura.

Si se necesita otro ajuste estructural, **agregarlo a `platform/scripts/build/build_thesis.py`**,
no editar el DOCX a mano.

## Anti-patrones

- Editar `document_reference.docx` directamente (se sobrescribe).
- Cambiar la fuente del cuerpo a Calibri/Arial: APA exige TNR (o equivalente
  serif: Liberation Serif, Cambria 12).
- Usar `<style>` HTML en el Markdown para forzar formato puntual.
- Crear nuevos custom-styles sin actualizar `preparar_reference_doc()`.
