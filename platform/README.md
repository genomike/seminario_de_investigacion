# `platform/` — Motor reusable de generación

Capa **estable** del repositorio. **No depende del tema** de la tesis.

## Subcarpetas

- **`scripts/build/`** — pipeline principal:
  - `build_thesis.py` — genera `build/tesis.docx` desde `content/manuscript/`.
  - `build_diagrams.py` — renderiza un set fijo de diagramas inline
    (`*.puml`) a `content/media/figures/*.png`.
- **`scripts/fixes/`** — correcciones idempotentes one-off del manuscrito
  (referencias, conectores, casing). Ejecutar con cuidado; siempre revisar
  diff después.
- **`scripts/downloads/`** — descarga masiva de fuentes (PowerShell).
- **`scripts/cleanup/`** — `reset_for_new_thesis.py` para fork limpio.
- **`templates/styles/`** — DOCX que controlan estilos APA + carátula.
- **`templates/guides/`** — guías universitarias APA 7, EPG, metodología.
- **`templates/examples/`** — plantillas de ejemplo llenadas.
- **`tools/`** — binarios externos (`plantuml.jar`).

## Reglas

- **No** importar nada de `content/`. Tomar paths como datos.
- **No** hardcodear texto del tema (palabras como "FHIR", "MINSA",
  "interoperabilidad" no deben aparecer en `platform/scripts/build/`).
- Toda ruta a `content/` o `build/` se calcula desde `REPO_ROOT` en cada
  script: `REPO_ROOT = Path(__file__).resolve().parents[N]`.
- Idempotencia: scripts de `fixes/` deben poder ejecutarse N veces sin
  efecto adicional.
