# Arquitectura del sistema de generación de tesis

## 1. Decisión arquitectónica

Aplicamos **Clean Architecture** y el principio de **separación por
estabilidad** (Stable Dependencies Principle, SDP) al repositorio:

> *Las dependencias deben apuntar hacia componentes más estables.*

Esto se traduce en tres capas concéntricas:

```
┌──────────────────────────────────────────────────────────┐
│  build/         (efímero)        ← genera y descarta     │
│  ┌────────────────────────────────────────────────────┐  │
│  │  content/   (volátil, específico del tema)         │  │
│  │  ┌──────────────────────────────────────────────┐  │  │
│  │  │  platform/   (estable, reusable entre tesis) │  │  │
│  │  └──────────────────────────────────────────────┘  │  │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
        ↑                ↑                  ↑
  cambia por        cambia por           cambia por
  ejecución         redacción            mejora del motor
```

Reglas:

1. `platform/` **no** importa nada de `content/`. Toma rutas como datos.
2. `content/` **no** contiene código ejecutable.
3. `build/` es siempre **regenerable**; está en `.gitignore`.
4. La interfaz entre capas es el filesystem (paths conocidos vía constantes
   en `platform/scripts/build/build_thesis.py`).

## 2. Mapeo de carpetas

| Carpeta                         | Propósito                                         |
|---------------------------------|---------------------------------------------------|
| `content/manuscript/`           | Markdown único (`Documento_Tesis.md`)             |
| `content/sources/{international,national}/` | PDFs y extractos de fuentes bibliográficas |
| `content/media/diagrams/`       | Archivos PlantUML (`*.puml`) — fuente             |
| `content/media/figures/`        | Imágenes finales (`*.png`) — generadas o externas |
| `content/observations/`         | Feedback del asesor, checklists del tema          |
| `content/drafts/`               | Borradores y refinamientos en proceso             |
| `platform/scripts/build/`       | Scripts principales del pipeline                  |
| `platform/scripts/fixes/`       | Correcciones idempotentes one-off del MD          |
| `platform/scripts/downloads/`   | Descarga masiva de fuentes                        |
| `platform/scripts/cleanup/`     | Reset del repo para una nueva tesis               |
| `platform/templates/styles/`    | `plantilla_estilos.docx`, `caratula.docx`         |
| `platform/templates/guides/`    | Guías universitarias (APA 7, EPG)                 |
| `platform/templates/examples/`  | Plantillas de ejemplo llenadas                    |
| `platform/tools/`               | Binarios externos (`plantuml.jar`)                |
| `build/`                        | DOCX final + intermedios (gitignored)             |
| `tests/`                        | Tests unitarios del pipeline                      |

## 3. Pipeline de generación

```
                ┌─────────────────────────┐
                │ content/manuscript/     │
                │   Documento_Tesis.md    │
                └────────────┬────────────┘
                             │
       ┌─────────────────────┼─────────────────────┐
       │                     │                     │
       ▼                     ▼                     ▼
  extraer_cuerpo      filtrar_secciones      ../media/figures/*.png
  (sin portada)       (excluir Resumen,         (resource-path)
                       Abstract, Intro)
       │                     │                     │
       └──────────┬──────────┘                     │
                  ▼                                │
         pandoc + reference-doc ◄─ platform/templates/styles/
                  │                                │
                  ▼                                │
         build/_cuerpo_tesis_temp.docx             │
                  │                                │
                  ▼                                │
       combinar con caratula.docx ◄────────────────┘
                  │
                  ▼
         postprocesar_docx
         (TOC, LOT, LOF, numeración H2/H3,
          bordes APA, fuente Calibri, bullets)
                  │
                  ▼
            build/tesis.docx
```

## 4. Convenciones críticas

- **Una sola fuente de verdad**: `content/manuscript/Documento_Tesis.md`.
- **Salto de página**: `\newpage` (LaTeX raw), nunca HTML.
- **Imágenes en MD**: paths relativos al MD → `../media/figures/<nombre>.png`.
- **Tablas**: pipe tables Markdown con caption `: Tabla N. … {#tbl:slug}`.
- **Diagramas**: `.puml` en `content/media/diagrams/` con placeholders
  `{a1}{e1}{i1}{o1}{u1}{n1}` para acentos; `.png` se genera a `figures/`.
- **Correcciones masivas** (>3 ediciones del mismo patrón): script Python
  idempotente en `platform/scripts/fixes/`.
- **Antes de build**: cerrar Word; el script intenta liberar bloqueos pero
  procesos colgados pueden persistir.

## 5. Reglas de dependencia (verificables por test)

```python
# tests/test_architecture.py debe garantizar:
# - platform/* nunca importa de content/
# - platform/* nunca hardcodea texto de un tema concreto
# - content/* no contiene .py ejecutable
```

## 6. ADRs (Architectural Decision Records)

### ADR-001 — Salida en `build/` con nombre canónico

**Decisión**: el output va a `build/tesis.docx` (no a la raíz, no con sufijos
`_salida` / `_validacion` / `_nueva`).

**Motivo**: `build/` está en `.gitignore`, por lo que cualquier archivo de
salida desaparece del repo automáticamente. Naming canónico evita
confusión sobre cuál es el "bueno".

### ADR-002 — Reference-doc como artefacto intermedio en `build/`

**Decisión**: `document_reference.docx` se genera en `build/_reference.docx`
(prefijo `_` indica intermedio).

**Motivo**: era un build artifact que vivía en la raíz; ahora se elimina
junto con el resto al hacer clean.

### ADR-003 — `--resource-path` apunta al directorio del MD

**Decisión**: pasamos `--resource-path={ENTRADA.parent}` a pandoc para que
las referencias `../media/figures/foo.png` sean resolvibles desde el MD.

**Motivo**: paths del MD son relativos al propio MD, no al working dir.
