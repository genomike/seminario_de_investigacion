# Tesis — Sistema de Generación Automatizada

Repositorio para la elaboración de una tesis de maestría en formato APA 7 / EPG,
con generación automatizada del DOCX final desde un único archivo Markdown
fuente, mediante **Pandoc** + postproceso con **python-docx**.

## Estructura (Clean Architecture)

```
.
├── content/        # CONTENIDO específico de la tesis (volátil)
├── platform/       # MOTOR de generación reusable (estable)
├── build/          # SALIDAS generadas (gitignored)
├── tests/          # Pruebas unitarias del motor
├── docs/           # Documentación interna del sistema
└── .github/        # Skills + instrucciones para Copilot
```

Tres capas separadas por **estabilidad**:

| Capa       | Cambia cada… | Ejemplos                                      |
|------------|--------------|-----------------------------------------------|
| `content/` | edición      | manuscrito, fuentes bibliográficas, diagramas |
| `platform/`| feature      | scripts de build, plantillas DOCX, plantuml   |
| `build/`   | corrida      | `tesis.docx`, intermedios                     |

Ver [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) para el detalle.

## Requisitos

- **Python** 3.10+ con `python-docx` y `lxml`
- **Pandoc** ≥ 3.0 en el `PATH`
- **Java** (para `platform/tools/plantuml.jar`)
- **Windows + PowerShell** (probado); el código es portable

## Comandos principales

```powershell
# Generar el DOCX final  -> build/tesis.docx
python platform/scripts/build/build_thesis.py

# Regenerar diagramas PNG desde .puml (paso separado)
python platform/scripts/build/build_diagrams.py

# Ejecutar tests
python -m pytest tests/

# Resetear el repo para una nueva tesis (limpia content/, build/)
python platform/scripts/cleanup/reset_for_new_thesis.py --dry-run
python platform/scripts/cleanup/reset_for_new_thesis.py --apply
```

## Tema actual

> **Modelo de interoperabilidad basado en HL7 FHIR para mejorar el intercambio
> de información clínica en centros de salud del MINSA — Perú.**

Para reusar este repositorio en **otra tesis** (p. ej. Derecho), seguir
[.github/skills/thesis-fork-new-topic/SKILL.md](.github/skills/thesis-fork-new-topic/SKILL.md).

## Skills (Copilot)

Las convenciones del proyecto están documentadas como *skills* en
[.github/skills/](.github/skills/). El asistente debe cargar el skill
relevante antes de actuar.
