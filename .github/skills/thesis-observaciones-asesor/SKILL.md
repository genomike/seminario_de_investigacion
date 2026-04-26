---
name: thesis-observaciones-asesor
description: Procesar observaciones del asesor (capturas en `content/observations/` o cambios trackeados en Word) y traducirlas a cambios concretos en `content/manuscript/Documento_Tesis.md`. Usar siempre que el usuario diga "el asesor observó…", "revisar comentarios", "aplicar feedback", o cuando aparezcan archivos nuevos en `content/observations/`.
---

# Procesamiento de observaciones del asesor

## Inputs típicos

- **Capturas PNG** con marcas en colores (rojo = corregir; amarillo =
  reformular; verde = ok / referencia). Viven en `content/observations/`.
- **DOCX con control de cambios**: el asesor edita el `.docx` y devuelve
  un archivo con sufijo `_revisado.docx` o similar.
- **Mensajes en chat / correo** con bullets.

## Workflow obligatorio

1. **Inventariar** las observaciones en una lista numerada antes de tocar
   nada. Para cada una:

   ```text
   #N | sección | tipo (forma|fondo) | descripción breve | acción propuesta
   ```

2. **Validar el inventario con el usuario** (al menos confirmación
   tácita) cuando hay > 5 cambios o cualquiera afecta estructura/título/objetivos.

3. **Clasificar** por categoría:

   | Categoría | Ejemplos | Skill que se carga |
   |---|---|---|
   | Estructura | falta sección, mover apartado | `thesis-structure-epg` |
   | Antecedentes | reformular conector, falta porte | `thesis-antecedentes` |
   | Tablas/Figuras | numerar, referenciar, agregar nota | `thesis-tablas-apa` / `thesis-figuras-plantuml` |
   | Citas | autor mal, et al. mal, DOI faltante | `thesis-citas-apa7` |
   | Estilo Word | sangría, fuente, encabezado | `thesis-estilos-docx` |
   | Contenido | datos faltantes, métricas | abrir el PDF de la fuente, citar correctamente |

4. **Decidir scope** del cambio:
   - **Cambio puntual** (1-3 ediciones): `replace_string_in_file` directo.
   - **Cambio masivo** (mismo patrón en > 3 lugares): escribir un script
     de fix idempotente (ver `thesis-scripts-fix`).
   - **Cambio estructural** (renombrar capítulo, mover sección):
     diff manual, validar índice + referencias internas.

5. **Aplicar y rebuild** el DOCX (`thesis-pipeline-build`) y verificar
   visualmente las observaciones marcadas.

6. **Anotar en el changelog** (`observaciones/<fecha>_resuelto.md`) qué se
   aplicó y qué quedó pendiente, con el número de la observación.

## Patrón clave aprendido (asesor de esta tesis)

La observación más recurrente fue **antecedentes inconsistentes**: cada
estudio escrito con conectores distintos. Solución general que se
estandarizó: el patrón en `thesis-antecedentes` (porte / problema /
objetivo / metodología / métricas / resultados / limitaciones / vínculo).
Ese patrón **no es opcional** y se aplica de forma universal a futuros
antecedentes y a forks.

Otras recurrentes:

- "Referencia explícita a tablas y figuras". Reemplazar siempre `la
  siguiente figura/tabla` por `La Figura N / La Tabla N`.
- "Justificar la cita". Cuando se cita un dato (porcentaje, métrica),
  añadir el contexto del estudio antes de la cita, no solo `(Autor, Año)`.
- "No usar negritas decorativas". Solo van en negrita: títulos,
  conectores del patrón de antecedentes, los encabezados de los términos
  básicos. Nada más.
- "Síntesis crítica". Cada bloque de antecedentes (internacionales,
  nacionales) cierra con una síntesis crítica que identifique vacíos.

## Capturas → texto

Cuando la observación llega como PNG con highlights:

1. Abrir la imagen y describir lo marcado en bullets:
   - color rojo → "corregir X"
   - color amarillo → "revisar Y"
   - llaves laterales → "agregar componente Z"
2. **Limitar a 1-2 imágenes por turno**: en chats con muchas imágenes
   grandes, la solicitud puede fallar.
3. Si la captura tiene > 2000 px en alguna dimensión, redimensionarla
   antes de enviarla a revisión (usar `content/media/figures/` para no contaminar
   `content/observations/`).

## Anti-patrones

- Aplicar cambios "del aire" sin inventariar primero (se pierden
  observaciones).
- Editar el DOCX revisado por el asesor en vez del Markdown fuente
  (el siguiente build los borra todos).
- Tomar decisiones de fondo (mover capítulos, cambiar título) sin
  confirmación explícita.
- Mezclar varios tipos de observación en un solo commit.
