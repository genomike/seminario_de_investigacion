# `content/` — Contenido específico de la tesis

Todo lo que **cambia con la tesis** vive aquí.

## Subcarpetas

- **`manuscript/`** — el archivo Markdown único (`Documento_Tesis.md`).
  Es la **fuente de verdad** del documento.
- **`sources/`** — bibliografía descargada.
  - `international/` — fuentes Q1/SciELO/internacionales.
  - `national/` — fuentes nacionales, normativa MINSA/Estado peruano.
- **`media/`**
  - `diagrams/` — `*.puml` (fuente PlantUML).
  - `figures/` — `*.png` (renderizadas + imágenes externas).
- **`observations/`** — feedback del asesor, checklists del tema.
- **`drafts/`** — borradores de capítulos, notas de refinamiento.

## Reglas

- **No** poner código `.py` aquí.
- **No** poner archivos generados sin fuente (PNG sin su `.puml` de origen,
  salvo imágenes externas claramente identificadas).
- Los paths a imágenes desde el MD son relativos: `../media/figures/x.png`.
- Para reusar el repo en otra tesis, esta carpeta se vacía con
  `python platform/scripts/cleanup/reset_for_new_thesis.py --apply`.
