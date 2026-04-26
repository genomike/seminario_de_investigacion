---
name: thesis-dominio-derecho
description: |
  Carga este skill cuando la tesis sea de **Derecho** (en lugar de
  ingeniería de software). Establece criterios de investigación
  jurídica, taxonomía de fuentes, jerarquía normativa y vocabulario
  técnico-legal aplicable a tesis peruanas.
---

# Skill: dominio Derecho

Este skill REEMPLAZA a `thesis-dominio-interoperabilidad` cuando se
forkea el repositorio para una tesis de Derecho. Definir el tema
concreto en la línea "Tema actual" de `.github/copilot-instructions.md`.

## 1. Tipos de investigación jurídica

| Tipo                | Pregunta que responde                                | Fuentes principales              |
|---------------------|------------------------------------------------------|-----------------------------------|
| **Dogmática**       | ¿Qué dice y cómo se interpreta la norma?             | Doctrina, jurisprudencia, ley     |
| **Histórico-jurídica** | ¿Cómo evolucionó la institución?                  | Códigos derogados, exposiciones de motivos |
| **Comparada**       | ¿Cómo regulan otros ordenamientos lo mismo?          | Legislación extranjera, tratados  |
| **Sociojurídica / empírica** | ¿Cómo opera el derecho en la realidad social?| Estadísticas, expedientes, encuestas |
| **Filosófica / iusfilosófica** | ¿Qué fundamento ético/político tiene?      | Doctrina iusfilosófica            |

La tesis debe declarar **explícitamente** el tipo de investigación en
el capítulo metodológico (no es lo mismo dogmática que empírica).

## 2. Jerarquía normativa peruana (orden de citación)

```
1. Constitución Política del Perú (1993, con reformas)
2. Tratados internacionales ratificados (DDHH y otros)
3. Leyes orgánicas
4. Leyes ordinarias / Decretos legislativos / Decretos de urgencia
5. Decretos supremos (reglamentos)
6. Resoluciones supremas / ministeriales / directorales
7. Ordenanzas regionales y municipales
8. Jurisprudencia vinculante (TC, Corte Suprema – plenos casatorios)
9. Doctrina
```

## 3. Tipos de fuentes y prioridad

### Fuentes primarias (obligatorias)
- **Legislación**: SPIJ (`spij.minjus.gob.pe`), Diario Oficial El Peruano.
- **Jurisprudencia**:
  - Tribunal Constitucional (`tc.gob.pe`) — sentencias y precedentes
    vinculantes.
  - Corte Suprema (`pj.gob.pe`) — Plenos Casatorios Civiles, Penales.
  - Corte IDH (`corteidh.or.cr`) — opiniones consultivas y sentencias.
- **Tratados**: Cancillería (`rree.gob.pe`), ONU treaty collection.

### Fuentes secundarias (doctrinales)
- **Repositorios académicos peruanos**:
  - PUCP — `tesis.pucp.edu.pe`, revistas `revistas.pucp.edu.pe`
    (Derecho PUCP, Pensamiento Constitucional, Themis).
  - UNMSM — `cybertesis.unmsm.edu.pe`.
  - UPC, USMP, U. de Lima, UDEP.
- **Bases especializadas**:
  - **vLex Perú** (`vlex.com.pe`) — jurisprudencia + doctrina.
  - **La Ley** (`laley.pe`) — Gaceta Jurídica.
  - **Actualidad Jurídica** (Gaceta Jurídica).
  - **Dialnet** (`dialnet.unirioja.es`) — doctrina hispanoamericana.
  - **SciELO Derecho** (`scielo.org`, área Ciencias Sociales).
- **Internacionales**:
  - HeinOnline, JSTOR Law, Westlaw (si la universidad da acceso).
  - SSRN Legal Scholarship Network.
  - Repositorios de revistas indexadas en Scopus / Web of Science
    categoría Law.

### Criterios de selección
- **Vigencia normativa**: verificar siempre si la ley citada está
  vigente, modificada o derogada (SPIJ permite filtrar por estado).
- **Pertinencia**: misma rama del Derecho que la tesis (civil, penal,
  constitucional, administrativo, laboral, etc.).
- **Recencia**: doctrina de últimos 10 años; clásicos (>10 años) solo
  cuando son fundacionales (p. ej. Kelsen, Hart, Rubio Correa).
- **Autoridad**: priorizar autores referenciados en plenos casatorios o
  sentencias del TC.

## 4. Citación APA 7 para fuentes legales

APA 7 admite formato propio para legislación. Convención sugerida en este
repositorio (consistente, en español):

### Constitución y leyes
```
Constitución Política del Perú [Const.]. (1993). Lima: Congreso Constituyente
    Democrático.

Ley N.º 27444, Ley del Procedimiento Administrativo General. (11 de abril
    de 2001). Diario Oficial El Peruano.

Decreto Legislativo N.º 1252, que crea el Sistema Nacional de Programación
    Multianual y Gestión de Inversiones. (1 de diciembre de 2016). Diario
    Oficial El Peruano.
```

### Jurisprudencia
```
Tribunal Constitucional del Perú. (15 de marzo de 2004). Sentencia recaída
    en el Expediente N.º 0008-2003-AI/TC.

Corte Suprema de Justicia de la República, Sala Civil Permanente. (19 de
    enero de 2017). Casación N.º 4442-2015 Moquegua [V Pleno Casatorio Civil].

Corte Interamericana de Derechos Humanos. (2001). Caso Barrios Altos vs.
    Perú. Sentencia de 14 de marzo de 2001 (Fondo). Serie C N.º 75.
```

### Citas en texto
- `(Const., 1993, art. 2)` para artículos constitucionales.
- `(Ley N.º 27444, 2001, art. 4)` para leyes.
- `(STC 0008-2003-AI/TC, 2004, fundamento 25)` para jurisprudencia
  constitucional.
- `(Casación N.º 4442-2015 Moquegua, 2017, considerando 12)`.

## 5. Vocabulario técnico (no usar como sinónimos)

| Correcto                     | Error frecuente                  |
|------------------------------|-----------------------------------|
| principio / regla            | "ley" para todo                   |
| precepto / disposición       | "artículo" (es la unidad textual) |
| supuesto de hecho / consecuencia jurídica | "causa / efecto"     |
| imputación / atribución      | "culpa" (en sentido coloquial)    |
| derogación expresa / tácita  | "anulación"                       |
| inconstitucionalidad         | "ilegalidad"                      |
| nulidad / anulabilidad / inexistencia | "invalidez" genérica     |
| prescripción / caducidad     | confusión entre ambas             |
| obiter dicta / ratio decidendi | "fundamento" sin distinción     |

## 6. Estructura típica de tesis de Derecho (EPG)

```
Capítulo I  – Planteamiento del problema (problema jurídico)
Capítulo II – Marco teórico (doctrina + marco normativo + jurisprudencia)
   2.1 Antecedentes (tesis previas + doctrina)
   2.2 Bases teóricas (instituciones jurídicas)
   2.3 Marco normativo (leyes vigentes ordenadas jerárquicamente)
   2.4 Marco jurisprudencial (sentencias relevantes analizadas)
   2.5 Derecho comparado (si aplica)
Capítulo III – Metodología (dogmática / empírica / mixta)
Capítulo IV – Análisis y discusión (no "resultados" si es dogmática)
Capítulo V  – Propuesta normativa o de lege ferenda (si aplica)
Conclusiones
Recomendaciones
Referencias (separar: Legislación, Jurisprudencia, Doctrina)
```

> **Nota**: en tesis dogmática NO suele haber "resultados experimentales".
> Renombrar a "Análisis jurídico" o "Discusión doctrinaria".

## 7. Reglas específicas de este repositorio para Derecho

- En `content/sources/`, sustituir subcarpetas por:
  - `legislacion/` — DOC/PDF de leyes y decretos.
  - `jurisprudencia/` — sentencias TC, Casaciones, Corte IDH.
  - `doctrina/nacional/` y `doctrina/internacional/`.
- En `content/observations/`, mantener checklist de la EPG correspondiente
  a la facultad de Derecho.
- Las tablas comparativas de derecho comparado son frecuentes: usar el
  patrón APA del skill `thesis-tablas-apa`.
- Diagramas: limitar a `media/diagrams/` solo cuando aporten (p. ej.
  línea de tiempo normativa, jerarquía de fuentes, flujograma procesal).
  Evitar diagramas decorativos.
