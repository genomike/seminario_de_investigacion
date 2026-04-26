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
platform/scripts/build/build_thesis.py
platform/scripts/build/build_diagrams.py
plantuml.jar
plantilla_estilos.docx
documentos_apoyo/                 (la guía EPG y el template universidad)
guia-apa7-tesis.md
.github/skills/                   (este conjunto de skills)
.github/copilot-instructions.md   (bootstrap del asistente)
scripts/                          (scripts de fix como esqueletos)
```

## Qué se vacía

```
Documento_Tesis.md                → dejar solo portada + esqueleto de capítulos
fuentes/internacionales/*         → vaciar
fuentes/nacionales/*              → vaciar
media/*.png  + media/*.puml       → vaciar (excepto image1.png si se reusa logo)
diagramas/*.puml                  → vaciar
observaciones/*                   → vaciar
tesis/*                           → vaciar (es trabajo en curso)
caratula.docx                     → reemplazar con portada del nuevo tema
```

## Qué hay que **adaptar** al nuevo tema

1. **`thesis-portada`** — actualizar título, autores, año.
2. **`thesis-dominio-*`** — eliminar el skill
   `thesis-dominio-interoperabilidad` y crear uno nuevo
   (`thesis-dominio-<tu-tema>`) con:
   - vocabulario / siglas del nuevo dominio,
   - normativa aplicable,
   - métricas y datasets típicos,
   - bases de datos académicas más fuertes para el tema.
3. **`README.md` raíz** (si lo hay) — sustituir descripción por la del nuevo tema.
4. **`.github/copilot-instructions.md`** — actualizar las dos líneas que
   dicen el tema y el contexto.
5. **`tesis/Elaboración_Tesis.md`** — recrear los pasos de keywords →
   búsqueda → fuentes finales → título para el nuevo tema.

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
- [ ] Reescribir el skill de dominio.
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
- No actualizar el skill de dominio: el orquestador termina cargando el del tema viejo.
- Cambiar la estructura "porque ahora es cualitativa" — la guía EPG
  acepta cualitativa con los mismos capítulos, solo cambia Cap. III a
  "Supuestos y categorías".
