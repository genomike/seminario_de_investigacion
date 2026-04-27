---
name: thesis-structure-epg
description: Estructura obligatoria, orden de secciones y numeración de capítulos para la tesis EPG (Escuela de Posgrado). Usar antes de crear o renombrar cualquier sección de nivel 1/2/3, o cuando el usuario habla de "capítulo I/II/III/IV/V", "índice", "preliminares", "anexos", "operacionalización".
---

# Estructura del proyecto de tesis (EPG)

## Fuente de autoridad

[platform/templates/guides/Guía metodológica para la elaboración del proyecto de tesis.pdf](../../../platform/templates/guides/).
Cualquier divergencia con APA 7 se resuelve a favor de la guía institucional
(la EPG manda sobre APA en estructura).

## Orden obligatorio (preliminares → cuerpo → finales)

```text
Portada                       (sin número visible)
Índice                        \newpage antes
Índice de tablas              \newpage antes
Índice de figuras             \newpage antes
Resumen + Palabras clave      \newpage antes
Abstract + Keywords           \newpage antes
Introducción                  \newpage antes
Capítulo I.   Planteamiento del estudio
  1.1. Planteamiento y formulación del problema
    1.1.1. Planteamiento del problema
    1.1.2. Formulación del problema
  1.2. Determinación de objetivos
    1.2.1. Objetivo general
    1.2.2. Objetivos específicos
  1.3. Justificación e importancia del estudio
    1.3.1. Justificación teórica
    1.3.2. Justificación metodológica
    1.3.3. Justificación social
  1.4. Limitaciones de la presente investigación
Capítulo II.  Marco teórico
  2.1. Antecedentes del problema (Internacionales / Nacionales / Síntesis crítica)
  2.2. Bases teóricas (Desarrollo histórico / Fundamentación teórica / Marco conceptual)
  2.3. Definición de términos básicos
Capítulo III. Hipótesis y variables  (o Supuestos y categorías si es cualitativo)
  3.1. Hipótesis (general / específicas / fundamentación / trazabilidad)
  3.2. Operacionalización de variables
  3.3. Matriz de operacionalización de variables
Capítulo IV.  Metodología del estudio
  4.1. Enfoque, tipo y alcance
  4.2. Diseño de la investigación
  4.3. Población y muestra
  4.4. Técnicas e instrumentos de recolección de datos
  4.5. Técnicas de análisis de datos
Capítulo V.   Aspectos administrativos
  5.1. Presupuesto
  5.2. Cronograma de actividades
Referencias                   \newpage antes
Anexos                        \newpage antes
```

## Numeración de títulos en Markdown

- `# Capítulo I: Planteamiento del estudio` (Heading 1)
- `## 1.1. Planteamiento y formulación del problema` (Heading 2)
- `### 1.1.1. Planteamiento del problema` (Heading 3)

**Reglas:**
- Numerar manualmente en el texto del título (`platform/scripts/build/build_thesis.py` confía en eso para construir la tabla de contenido).
- **No** usar `->` ni `.-` después del número. Solo punto y espacio: `1.1. ` (no `1.1.- ` ni `1.1.->`).
- Una sola "frase" por título; sin punto final.
- Title Case en español APA: capitalizar la primera palabra y nombres propios; el resto en minúscula.

## Saltos de página

- `\newpage` (línea propia, en blanco antes y después) entre cada preliminar y antes de Referencias y Anexos.
- **No** insertar `\newpage` entre subsecciones del cuerpo: el flujo de Word lo decide.

## Resumen y Abstract

- Extensión 150-250 palabras.
- Etiquetas en cursiva, no en negrita: `*Palabras clave:* …` y `*Keywords:* …`.
- "Palabras clave" sin "s" final.

## Cosas que NO van en el cuerpo del Markdown

- Tabla de contenido literal (la genera `platform/scripts/build/build_thesis.py` con campos Word).
- Lista de tablas y figuras (idem).
- Numeración de páginas, encabezados/pies (lo aporta el `reference-doc`).

## Cuando el tema cambia (fork)

La estructura no cambia: cambia solo el contenido. Conservar literal los
nombres de los capítulos y el orden. Ajustar `Capítulo III` a "Supuestos
y categorías" únicamente si el enfoque es cualitativo.
