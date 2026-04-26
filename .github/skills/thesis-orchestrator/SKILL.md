---
name: thesis-orchestrator
description: Punto de entrada para cualquier trabajo sobre la tesis. Usar cuando el usuario pide "trabajar en la tesis", "agregar un capítulo", "generar el documento", "revisar comentarios del asesor" o cualquier tarea que combine varios pasos. Decide qué otros skills cargar.
---

# Orquestador del trabajo de tesis

## Cuándo usar este skill

Carga este SKILL.md primero cuando la solicitud del usuario:

- Es ambigua respecto a qué etapa de la tesis hay que tocar.
- Implica varios pasos del pipeline (p. ej. "agrega este antecedente, regenera el DOCX y revisa que la tabla salga bien").
- Es una sesión nueva donde no hay contexto previo cargado.

## Pasos obligatorios

1. **Identificar la etapa** del pipeline a la que pertenece la solicitud:
   - Definir/cambiar tema, problema, objetivos → `thesis-structure-epg`
   - Carátula / datos del autor → `thesis-portada`
   - Buscar/descargar/catalogar fuentes → `thesis-fuentes`
   - Redactar antecedentes → `thesis-antecedentes`
   - Tablas → `thesis-tablas-apa`
   - Figuras / diagramas → `thesis-figuras-plantuml`
   - Citas o lista de referencias → `thesis-citas-apa7`
   - Estilos del DOCX (fuente, márgenes, sangría, numeración) → `thesis-estilos-docx`
   - Generar el DOCX final → `thesis-pipeline-build`
   - Comentarios del asesor → `thesis-observaciones-asesor`
   - Corrección masiva del Markdown → `thesis-scripts-fix`
   - Reusar el repo para otra tesis → `thesis-fork-new-topic`

2. **Cargar el `SKILL.md` correspondiente con `read_file`** antes de actuar.
   Si la tarea cruza dominios (ej. "agrega esta tabla con su cita"), cargar
   ambos en paralelo.

3. **Respetar el orden del pipeline** cuando hay dependencias:
   - No generar DOCX si hay diagramas `.puml` modificados sin renderizar.
   - No "ajustar APA" si la sección aún se está escribiendo.
   - No tocar `platform/templates/styles/plantilla_estilos.docx` si solo cambia el contenido del MD.

4. **Confirmar al usuario el plan** en 1-3 viñetas antes de ejecutar
   cambios grandes (más de 3 archivos o cambios al pipeline).

## Estado canónico del repo

- Fuente de verdad del cuerpo: [content/manuscript/Documento_Tesis.md](../../../content/manuscript/Documento_Tesis.md).
- Generador: [platform/scripts/build/build_thesis.py](../../../platform/scripts/build/build_thesis.py).
- Render de diagramas: [platform/scripts/build/build_diagrams.py](../../../platform/scripts/build/build_diagrams.py).
- Estilos Word: [platform/templates/styles/plantilla_estilos.docx](../../../platform/templates/styles/plantilla_estilos.docx).
- Carátula opcional pre-armada: `platform/templates/styles/caratula.docx` (se concatena si existe).
- Diagramas: PlantUML en `content/media/diagrams/*.puml`, renderizados a `content/media/figures/*.png`.
- Guía APA del repo: [platform/templates/guides/guia-apa7-tesis.md](../../../platform/templates/guides/guia-apa7-tesis.md) (autoridad
  para dudas de formato APA específicas a esta tesis).
- Guía oficial EPG: [platform/templates/guides/Guía metodológica para la elaboración del proyecto de tesis.pdf](../../../platform/templates/guides/Guía metodológica para la elaboración del proyecto de tesis.pdf) (autoridad
  para estructura institucional).

## Política de actualización obligatoria

- Todo cambio solicitado por el usuario se consolida en [content/manuscript/Documento_Tesis.md](../../../content/manuscript/Documento_Tesis.md) como fuente de verdad.
- Si el cambio involucra una figura, actualizar el `.puml` en `content/media/diagrams/`, regenerar su `.png` en `content/media/figures/` y verificar/actualizar el embed en el Markdown.
- Si el cambio involucra tablas, actualizar la tabla en Markdown (pipe table + caption), nunca en el DOCX.
- No editar `build/tesis.docx` como mecanismo de corrección: cualquier corrección se hace en insumos (`content/` o `platform/`) y luego se recompila.

## Anti-patrones registrados

- **No** crear archivos `.md` paralelos para "documentar el cambio" salvo
  que el usuario lo pida explícitamente.
- **No** introducir HTML inline en `content/manuscript/Documento_Tesis.md` para tablas o saltos
  de página: Pandoc no las convierte bien a DOCX.
- **No** ejecutar `dotnet`, `npm`, `vite`… (este repo no tiene stack de app).
  El único stack es Python + Pandoc + Java (PlantUML).
- **No** pelear con PSReadLine en here-strings largos: si el bloque pasa
  de ~30 líneas, escribir un `.py` y ejecutarlo.
- **No** asumir que la portada se construye desde Markdown pleno: usa
  divs `::: {custom-style="Portada-Centrado"}` (ver `thesis-portada`).

## Lecciones aprendidas (cross-cutting)

- Cualquier cambio en `content/manuscript/Documento_Tesis.md` requiere **regenerar el DOCX**
  y validar visualmente: la diferencia "se ve bien en MD" ≠ "se ve bien en
  Word" es enorme (numeración, bullets, tablas, captions).
- Los scripts de fix masivo deben ser **idempotentes**: si encuentran el
  patrón ya corregido, no deben romper nada (`thesis-scripts-fix`).
- Las observaciones del asesor llegan como capturas (PNG) y como cambios
  en Word; ambos formatos deben extraerse a viñetas accionables antes de
  modificar el Markdown.
