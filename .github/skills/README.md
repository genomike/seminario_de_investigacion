# Skills de elaboración de tesis (EPG)

Conjunto de skills reutilizables destilados de las sesiones que produjeron
[Documento_Tesis.md](../../content/manuscript/Documento_Tesis.md) y su salida
[build/tesis.docx](../../build/tesis.docx).

Están pensados para ser **portables a cualquier fork** que reutilice este
mismo pipeline (Markdown único + Pandoc + reference-doc DOCX +
postproceso `python-docx` + diagramas PlantUML), aunque el tema sea distinto.

## Cómo invocarlos

Cada skill vive en su propia carpeta con un `SKILL.md`. Los archivos `SKILL.md`
están escritos para ser **leídos al inicio de la tarea relevante**: si el
usuario pide algo que cae en el dominio de un skill, hay que abrir su
`SKILL.md` antes de actuar.

> Regla de oro: **leer el SKILL.md antes de tocar el archivo objetivo**.
> No basta con "recordar" el patrón; los detalles (conectores, captions,
> rutas, scripts de postproceso) cambian entre forks.

## Mapa de skills

| Skill | Cuándo usarlo |
|---|---|
| [thesis-orchestrator](thesis-orchestrator/SKILL.md) | Punto de entrada. Orquesta el resto del pipeline. |
| [thesis-structure-epg](thesis-structure-epg/SKILL.md) | Antes de crear capítulos/secciones (orden EPG y numeración). |
| [thesis-portada](thesis-portada/SKILL.md) | Editar/regenerar la carátula. |
| [thesis-fuentes](thesis-fuentes/SKILL.md) | Buscar, descargar y catalogar fuentes académicas. |
| [thesis-antecedentes](thesis-antecedentes/SKILL.md) | Redactar o reformatear antecedentes (patrón de conectores). |
| [thesis-tablas-apa](thesis-tablas-apa/SKILL.md) | Crear/editar tablas para que rendericen como tabla real APA en DOCX. |
| [thesis-figuras-plantuml](thesis-figuras-plantuml/SKILL.md) | Crear o regenerar diagramas/figuras. |
| [thesis-citas-apa7](thesis-citas-apa7/SKILL.md) | Citas en texto y lista de referencias. |
| [thesis-estilos-docx](thesis-estilos-docx/SKILL.md) | Tocar `platform/templates/styles/plantilla_estilos.docx`/`reference-doc` (estilos Word). |
| [thesis-pipeline-build](thesis-pipeline-build/SKILL.md) | Ejecutar `platform/scripts/build/build_thesis.py` y depurar la salida DOCX. |
| [thesis-observaciones-asesor](thesis-observaciones-asesor/SKILL.md) | Procesar comentarios del asesor (formales y de fondo). |
| [thesis-scripts-fix](thesis-scripts-fix/SKILL.md) | Escribir scripts idempotentes de corrección masiva del Markdown. |
| [thesis-fork-new-topic](thesis-fork-new-topic/SKILL.md) | Reusar este repo como base para una tesis sobre otro tema. |
| [thesis-dominio-interoperabilidad](thesis-dominio-interoperabilidad/SKILL.md) | Skill de dominio de **ejemplo** (interoperabilidad clínica/HL7 FHIR). Reemplázalo en cada fork por `thesis-dominio-<tu-tema>`. |
| [thesis-dominio-derecho](thesis-dominio-derecho/SKILL.md) | Solo aplicable a tesis de **Derecho** (jurídica). |
| [thesis-fuentes-derecho](thesis-fuentes-derecho/SKILL.md) | Fuentes especializadas para tesis de Derecho (SPIJ, TC, vLex, etc.). |

## Pipeline canónico (resumen ejecutivo)

```
1. Definir título, problema, objetivos      → thesis-structure-epg
2. Carátula                                  → thesis-portada
3. Búsqueda y descarga de fuentes            → thesis-fuentes
4. Redacción capítulos (Marco, Antecedentes) → thesis-antecedentes / thesis-citas-apa7
5. Tablas y figuras                          → thesis-tablas-apa / thesis-figuras-plantuml
6. Build a DOCX                              → thesis-pipeline-build
7. Aplicar correcciones del asesor           → thesis-observaciones-asesor
8. Refinar APA y consistencia                → thesis-citas-apa7 / thesis-scripts-fix
```

## Convenciones globales del repo

- **Un único** `content/manuscript/Documento_Tesis.md` como fuente de verdad. Nada de partir el cuerpo en múltiples `.md`. (Los `.md` en `content/drafts/`, `platform/templates/guides/` son insumos de trabajo, no entradas del build.)
- Toda corrección solicitada por el usuario se aplica primero en esa fuente de verdad (MD), no en el DOCX final.
- Saltos de página se controlan con `\newpage` (no con HTML ni con CSS).
- Tablas: **siempre** Markdown pipe tables con caption `: Tabla N. ... {#tbl:slug}`. Nunca HTML.
- Figuras: `![Caption](../media/figures/diagrama-x.png)`; los `.puml` viven en `content/media/figures/` o `content/media/diagrams/` y se renderizan con `platform/tools/plantuml.jar`.
- Para cambios de figuras: actualizar `.puml` -> regenerar `.png` -> verificar embed en `content/manuscript/Documento_Tesis.md`.
- Encoding UTF-8. Acentos directamente en el texto del Markdown (en PlantUML usar placeholders `{a1},{e1},{i1},{o1},{u1},{n1}`).
- Comandos largos y here-strings en PowerShell se rompen con PSReadLine: para tareas largas crear un `.py` temporal y ejecutarlo con `python archivo.py`.

## Método alternativo recomendado para un nuevo fork

Para una tesis nueva sobre **otro tema** (mismo asesor / misma EPG / mismo
formato), el camino más corto es:

1. Hacer fork de este repo y ejecutar
   `python platform/scripts/cleanup/reset_for_new_thesis.py --apply`
   (resetea `content/manuscript/Documento_Tesis.md` a esqueleto y vacía
   `content/sources/`, `content/media/`, `content/observations/`,
   `content/drafts/`, `build/`).
2. (Si la limpieza manual hace falta): vaciar también subcarpetas extra
   en `content/`.
3. Conservar tal cual: todo `platform/`, `tests/`, `docs/`,
   `.github/skills/`, `.github/copilot-instructions.md`.
4. Adaptar `thesis-portada` (datos del autor/título), `thesis-dominio-*`
   (reemplazar por el dominio del nuevo tema) y arrancar por
   `thesis-orchestrator`. Para tesis de Derecho, cargar
   `thesis-dominio-derecho` y `thesis-fuentes-derecho`.
