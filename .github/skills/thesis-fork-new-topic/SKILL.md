---
name: thesis-fork-new-topic
description: Reusar este repo como base para una tesis nueva sobre OTRO tema (manteniendo asesor / EPG / pipeline). Usar cuando el usuario dice "voy a hacer otra tesis", "reusemos esto para…", "fork", o cuando se detecta que el repo está clonado y el contenido del MD ya no corresponde al tema original.
---

# Forkear este repo para una tesis nueva

## Objetivo

Aprovechar el pipeline (Pandoc + postproceso + skills + estilos APA + scripts
de fix) para escribir otra tesis sobre cualquier tema, sin reinventar la
infraestructura.

## Qué se conserva tal cual

```
platform/                          # motor reusable (build, fixes, cleanup, tests)
  scripts/build/build_thesis.py
  scripts/build/build_diagrams.py
  scripts/cleanup/reset_for_new_thesis.py
  scripts/fixes/                   # esqueletos de scripts de corrección masiva
  templates/styles/plantilla_estilos.docx
  templates/portada/caratula.docx
  templates/guides/                # guía EPG, guía APA7
  tools/plantuml.jar
tests/
docs/ARCHITECTURE.md
.github/skills/                    # este conjunto de skills
.github/copilot-instructions.md    # bootstrap del asistente
```

## Qué se vacía

Lo más fácil es delegar en el script:

```powershell
python platform/scripts/cleanup/reset_for_new_thesis.py            # dry-run
python platform/scripts/cleanup/reset_for_new_thesis.py --apply    # aplicar
```

Equivalente manual (no recomendado):

```
content/manuscript/Documento_Tesis.md  → reset al esqueleto base
content/sources/international/*        → vaciar
content/sources/national/*             → vaciar
content/media/diagrams/*.puml          → vaciar
content/media/figures/*.png            → vaciar
content/observations/*                 → vaciar
content/drafts/*                       → vaciar
build/*                                → vaciar (regenerable)
```

## Qué hay que **adaptar** al nuevo tema

1. **`thesis-portada`** — actualizar título, autores, año.
2. **`thesis-dominio-*`** — copiar `thesis-dominio-template` como
  `thesis-dominio-<tu-tema>` y completarlo con:
   - vocabulario / siglas del nuevo dominio,
   - normativa aplicable,
   - métricas y datasets típicos,
   - bases de datos académicas más fuertes para el tema.
  Si el tema necesita fuentes especializadas, copiar también
  `thesis-fuentes-dominio-template` como `thesis-fuentes-<tu-tema>`.
3. **`README.md` raíz** (si lo hay) — sustituir descripción por la del nuevo tema.
4. **`.github/copilot-instructions.md`** — mantenerlo agnóstico. No colocar
  el tema completo ahí; el tema vive en `content/manuscript/Documento_Tesis.md`
  y, si existe, en el skill de dominio del fork.
5. **`content/drafts/`** — recrear los pasos de keywords → búsqueda
   → fuentes finales → título para el nuevo tema.

## Qué **NO** hay que cambiar

- Estructura EPG (`thesis-structure-epg`).
- Patrón de antecedentes (`thesis-antecedentes`) — el asesor lo exige
  igual sin importar el tema.
- Reglas APA (`thesis-citas-apa7`).
- Estilos del DOCX (`thesis-estilos-docx`).
- Pipeline (`thesis-pipeline-build`).
- Observaciones del asesor (`thesis-observaciones-asesor`) — el patrón
  para procesar feedback es independiente del tema.

## Checklist del fork (en orden)

- [ ] Crear branch `tema-<nuevo-tema>` o repo nuevo desde el fork.
- [ ] Vaciar carpetas listadas arriba.
- [ ] Verificar que `python platform/scripts/build/build_thesis.py` aún corre (debería dejar
      un DOCX casi vacío, pero sin errores).
- [ ] Cargar `thesis-orchestrator` y arrancar el flujo:
      `thesis-fuentes` → primera batch de fuentes → `thesis-antecedentes`.
- [ ] Crear el skill de dominio a partir de `thesis-dominio-template`.
- [ ] Hacer commit "chore: scaffold para tesis sobre <tema>".

## Sugerencias de mejora opcionales para el fork

Estas son alternativas que el equipo no llegó a aplicar pero que vale la
pena considerar al iniciar de cero:

- **BibTeX + CSL**: usar `--citeproc` con un `references.bib` y
  `apa.csl`. Elimina el riesgo de inconsistencia en formatos de cita
  y libera la sección `# Referencias` (Pandoc la genera). Costo de
  migración: medio (hay que volcar las referencias actuales a `.bib`).
- **Quarto** en vez de Pandoc raw: Quarto absorbe el postproceso de
  TOC/LOT/LOF y maneja referencias cruzadas (`@fig-xxx`, `@tbl-xxx`)
  de forma nativa.
- **GitHub Actions** que en cada push genere el DOCX y lo publique como
  artifact: evita el "se ve bien en mi máquina".
- **pre-commit hook** que corra las validaciones de
  `thesis-scripts-fix` (sin escribir, solo reportar) para pillar
  problemas antes del PR.
- **Diccionario `cspell`** en `.cspell.json` con el vocabulario del
  dominio: marca errores tipográficos sin marcar todas las siglas.

## Anti-patrones del fork

- Mantener fuentes del tema viejo "por si sirven": confunden al asesor y al lector.
- Dejar vocabulario del tema viejo en `.github/skills/`, `platform/`,
  `tests/`, `docs/` o README: contamina los siguientes forks.
- Cambiar la estructura "porque ahora es cualitativa" — la guía EPG
  acepta cualitativa con los mismos capítulos, solo cambia Cap. III a
  "Supuestos y categorías".
