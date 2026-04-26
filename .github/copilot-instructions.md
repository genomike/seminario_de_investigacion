# Copilot — instrucciones del repositorio

Este repositorio produce **un proyecto de tesis** (Markdown único →
Pandoc → DOCX con postproceso `python-docx`). El asistente debe
trabajar siempre desde el archivo fuente
[content/manuscript/Documento_Tesis.md](../content/manuscript/Documento_Tesis.md),
nunca editando el DOCX de salida.

## Arquitectura del repo (3 capas)

```
content/    ← contenido del tema (volátil)
platform/   ← motor reusable (estable, no toca el tema)
build/      ← salidas (efímero, gitignored)
```

Ver [docs/ARCHITECTURE.md](../docs/ARCHITECTURE.md) para el detalle.

**Reglas de oro**:

1. `platform/` no importa de `content/`, ni hardcodea texto del tema.
2. `content/` no contiene `.py` ejecutable.
3. El output va siempre a `build/tesis.docx` (no a la raíz).

## Tema actual

> Modelo de interoperabilidad basado en HL7 FHIR para mejorar el
> intercambio de información clínica en centros de salud del MINSA — Perú.
>
> Para forkear sobre otro tema: ejecutar
> `python platform/scripts/cleanup/reset_for_new_thesis.py --apply`,
> reemplazar la línea de tema y cambiar el skill de dominio.

## Stack

- **Pandoc** ≥ 3.0
- **Python** 3.10+ (`python-docx`, `lxml`, `pytest`)
- **Java** + `platform/tools/plantuml.jar` (diagramas)
- Entorno: Windows + PowerShell
- Idioma de toda la conversación y los entregables: **español**

## Comandos canónicos

```powershell
# Build completo
python platform/scripts/build/build_thesis.py        # -> build/tesis.docx

# Regenerar solo diagramas (paso separado)
python platform/scripts/build/build_diagrams.py      # -> content/media/figures/

# Tests del motor
python -m pytest tests/ -q

# Reset para nueva tesis
python platform/scripts/cleanup/reset_for_new_thesis.py            # dry-run
python platform/scripts/cleanup/reset_for_new_thesis.py --apply    # aplicar
```

## Ruta de skills

Todos los flujos están documentados en [.github/skills/](skills/README.md).
**Antes de actuar**, cargar el `SKILL.md` correspondiente:

| Si la solicitud es sobre…              | Cargar                                              |
|----------------------------------------|-----------------------------------------------------|
| algo ambiguo o multi-etapa             | `skills/thesis-orchestrator/SKILL.md`               |
| estructura / capítulos / numeración    | `skills/thesis-structure-epg/SKILL.md`              |
| portada / carátula                     | `skills/thesis-portada/SKILL.md`                    |
| buscar o descargar fuentes (genérico)  | `skills/thesis-fuentes/SKILL.md`                    |
| fuentes para tesis de **Derecho**      | `skills/thesis-fuentes-derecho/SKILL.md`            |
| antecedentes                           | `skills/thesis-antecedentes/SKILL.md`               |
| tablas                                 | `skills/thesis-tablas-apa/SKILL.md`                 |
| figuras / diagramas                    | `skills/thesis-figuras-plantuml/SKILL.md`           |
| citas o referencias                    | `skills/thesis-citas-apa7/SKILL.md`                 |
| estilos Word / reference-doc           | `skills/thesis-estilos-docx/SKILL.md`               |
| generar el DOCX                        | `skills/thesis-pipeline-build/SKILL.md`             |
| comentarios del asesor                 | `skills/thesis-observaciones-asesor/SKILL.md`       |
| corrección masiva del MD               | `skills/thesis-scripts-fix/SKILL.md`                |
| reusar el repo para otra tesis         | `skills/thesis-fork-new-topic/SKILL.md`             |
| dominio: interoperabilidad / HL7 FHIR  | `skills/thesis-dominio-interoperabilidad/SKILL.md`  |
| dominio: **Derecho** (jurídico)        | `skills/thesis-dominio-derecho/SKILL.md`            |

## Convenciones rápidas

- Una sola fuente de verdad: `content/manuscript/Documento_Tesis.md`.
- Saltos de página = `\newpage` (no HTML).
- Tablas = pipe tables Markdown con caption `: Tabla N. … {#tbl:slug}`.
- Figuras = `![Caption](../media/figures/diagrama-x.png)` (path relativo
  desde `manuscript/`); nunca screenshots.
- Diagramas fuente: `content/media/diagrams/*.puml`; renderizados a
  `content/media/figures/*.png`.
- Acentos en `.puml` = placeholders `{a1}{e1}{i1}{o1}{u1}{n1}`.
- Correcciones masivas (>3 ediciones del mismo patrón): script Python
  idempotente en `platform/scripts/fixes/`.
- Antes de hacer build, cerrar Word; el script intenta matarlo, pero
  procesos colgados pueden bloquear el `.docx`.

## Tests obligatorios al refactorizar

Cualquier cambio en `platform/` debe pasar:

```powershell
python -m pytest tests/ -q
```

Tests cubren: rutas, arquitectura por capas, validación del MD, filtrado
de secciones excluidas.

## Reglas de comunicación

- Responder en español.
- Confirmar el plan en 1-3 viñetas antes de cambios > 3 archivos.
- Usar las skills aunque parezcan obvias: contienen anti-patrones
  específicos que ya costaron tiempo descubrir.
