# Guía de Aplicación APA 7.ª Edición — Documento de Tesis

> **Propósito:** Este documento sirve como instrucción de referencia para alinear `Documento_Tesis.md` con las normas APA 7.ª edición cada vez que se modifique o amplíe la tesis. Basado en el análisis cruzado entre la Guía Normas APA 7.ª edición (normas-apa.org) y el estado actual del documento.

---

## 1. Formato general del documento

### 1.1. Tamaño de papel y márgenes

| Elemento | Norma APA 7 | Estado actual | Acción requerida |
|---|---|---|---|
| Tamaño de papel | Carta (21.59 × 27.94 cm) | Definido en `reference.docx` | Verificar en plantilla DOCX |
| Márgenes | 2.54 cm (1 pulgada) todos los lados | Definido en `reference.docx` | Verificar en plantilla DOCX |

### 1.2. Tipografía

| Elemento | Norma APA 7 | Recomendación |
|---|---|---|
| Fuente con serifas | Times New Roman 12 pt | La tesis usa Times New Roman 12 pt ✅ |
| Fuente sin serifas | Calibri 11 pt / Arial 11 pt | Alternativa válida |
| Notas al pie | Fuente más pequeña (ej. 10 pt) | Aplicar si se usan notas al pie |
| Notas de figuras/tablas | Puede ser más pequeña (10 pt) | Actualmente en 10 pt vía `formatear_notas_fuente()` ✅ |

### 1.3. Interlineado

| Elemento | Norma APA 7 | Acción requerida |
|---|---|---|
| Texto general | Doble espacio (2.0) | Configurar en `reference.docx` |
| Resumen | Doble espacio | Aplicar |
| Referencias | Doble espacio | Aplicar |
| Títulos y subtítulos | Doble espacio (sin espacio extra antes/después) | No agregar espacio de párrafo adicional |
| Citas en bloque (>40 palabras) | Doble espacio | Aplicar |
| **Excepciones** | | |
| Portada | Línea extra en blanco entre título y autores | Verificar |
| Cuerpo de tablas | Sencillo, 1.5 o doble (a elección) | El más efectivo |
| Notas de figuras/tablas | Doble espacio en número y título | Aplicar |

### 1.4. Sangría de párrafo

| Elemento | Norma APA 7 | Acción requerida |
|---|---|---|
| Primera línea de cada párrafo | Sangría de 1.27 cm (½ pulgada) | Configurar en `reference.docx` con estilo Normal |
| Excepciones (sin sangría) | Resumen, títulos de tabla/figura, etiquetas de apéndice, títulos de sección centrados | Verificar |
| Lista de referencias | Sangría francesa de 1.27 cm | Configurar estilo en `reference.docx` |
| Citas en bloque | Sangría izquierda de 1.27 cm en todo el bloque | Pandoc lo genera con `>` o bloques indentados |

### 1.5. Numeración de páginas

| Elemento | Norma APA 7 | Acción requerida |
|---|---|---|
| Posición | Esquina superior derecha | Configurar encabezado en `reference.docx` |
| Portada | Lleva el número 1 | Verificar que la portada tenga número de página |
| Todas las páginas | Numeración continua | Asegurar continuidad |

### 1.6. Encabezado (running head)

| Tipo de trabajo | Norma APA 7 |
|---|---|
| Estudiantes | Solo número de página (sin running head) |
| Profesional | Título abreviado en mayúsculas + número de página |

> **Para esta tesis (estudiantes de maestría):** Solo número de página en el encabezado. No incluir running head salvo que la universidad lo requiera.

---

## 2. Títulos y subtítulos (niveles de encabezado)

APA 7 define 5 niveles de encabezado:

| Nivel | Formato APA 7 | Equivalente Markdown | Uso en la tesis |
|---|---|---|---|
| **Nivel 1** | Centrado, **Negrita**, Cada Palabra en Mayúscula. Texto en nuevo párrafo. | `# Título` | Capítulos principales: `# Capítulo I: Planteamiento del estudio` |
| **Nivel 2** | Alineado a la izquierda, **Negrita**, Cada Palabra en Mayúscula. Texto en nuevo párrafo. | `## Subtítulo` | Secciones: `## 1.1. -> Planteamiento y formulación del problema` |
| **Nivel 3** | Alineado a la izquierda, **_Negrita cursiva_**, Cada Palabra en Mayúscula. Texto en nuevo párrafo. | `### Subtítulo` | Subsecciones: `### 1.1.1.- Planteamiento del problema` |
| **Nivel 4** | Con sangría ½ pulg., **Negrita**, Cada Palabra en Mayúscula, con punto final. Texto continúa en la misma línea. | N/A directo en Markdown | No usado actualmente |
| **Nivel 5** | Con sangría ½ pulg., **_Negrita cursiva_**, Cada Palabra en Mayúscula, punto final. Texto continúa en la misma línea. | N/A directo en Markdown | No usado actualmente |

### Reglas de capitalización para títulos

- **Title Case (Niveles 1-5):** Cada Palabra Inicia en Mayúscula, excepto artículos (el, la, los, un), preposiciones cortas (de, en, con, por) y conjunciones (y, o, ni), a menos que sean la primera palabra.
- En español, la convención APA admite capitalización de la primera palabra y nombres propios solamente. **Recomendación:** mantener consistencia interna; la tesis actualmente usa estilo mixto.

### Hallazgos en el documento actual

| Problema | Ejemplo | Corrección requerida |
|---|---|---|
| El marcador `->` en Heading 2 no es APA | `## 1.1. -> Planteamiento` | Eliminar `->` o reemplazar por punto o espacio |
| El marcador `.-` en Heading 3 no es APA | `### 1.1.1.- Planteamiento` | Usar `### 1.1.1. Planteamiento` (punto sin guion) |
| Antecedentes usan `**NEGRITA MAYÚSCULAS**` para autores | `**ADELUSI ET AL. (2025)**` | APA no usa mayúsculas completas en subtítulos de texto |

---

## 3. Citas en el texto

### 3.1. Formatos básicos

APA 7 tiene dos formatos de cita en texto:

| Tipo | Formato | Ejemplo |
|---|---|---|
| **Cita en paréntesis** | (Autor, año) | (Torab-Miandoab et al., 2023) |
| **Cita narrativa** | Autor (año) | Torab-Miandoab et al. (2023) señalan que... |

### 3.2. Reglas según número de autores

| N.° de autores | Primera cita | Citas subsiguientes |
|---|---|---|
| 1 autor | (Bayona, 2019) | (Bayona, 2019) |
| 2 autores | (Arrué Pajares y Vargas Rioja, 2022) | (Arrué Pajares y Vargas Rioja, 2022) |
| 3+ autores | (Torab-Miandoab et al., 2023) | (Torab-Miandoab et al., 2023) |

> **Nota APA 7:** A partir de 3 autores se usa "et al." desde la primera citación. Esto cambió respecto a APA 6, donde se listaban hasta 5 autores la primera vez.

### 3.3. Citas de organizaciones/instituciones

| Primera cita | Citas subsiguientes |
|---|---|
| Organización Panamericana de la Salud (OPS, 2024) | OPS (2024) |
| Ministerio de Salud (MINSA, 2018) | MINSA (2018) |

> **Regla:** Solo abreviar si la abreviatura es muy conocida. En la primera mención, escribir el nombre completo seguido de la abreviatura entre paréntesis.

### 3.4. Citas textuales (directas)

| Tipo | Formato |
|---|---|
| **Menos de 40 palabras** | Integrada en el texto entre "comillas", con (Autor, año, p. XX) al final. El punto va **después** del paréntesis. |
| **40 o más palabras** | En bloque con sangría izquierda de 1.27 cm, sin comillas, sin cursiva, interlineado doble. El punto va **antes** de la cita parentética. |

> **Estado actual:** La tesis no contiene citas textuales directas extensas. Si se agregan, aplicar el formato correspondiente.

### 3.5. Citas parafraseadas

- **Siempre** incluir autor y año.
- El **número de página** es recomendado pero no obligatorio en paráfrasis.
- Si el parafraseo abarca varias oraciones, citar en la primera mención; no es necesario repetir mientras la fuente permanezca clara.

### 3.6. Citas secundarias

- Formato: (Autor original, año, como se citó en Autor secundario, año).
- Usar solo cuando el original no sea accesible.
- En la lista de referencias solo se incluye la fuente secundaria.

> **Estado actual:** La tesis tiene citas secundarias como "HIMSS, citado en Amar et al. (2024)". Verificar formato: debería ser "(HIMSS, como se citó en Amar et al., 2024)" o bien usar la referencia de Amar et al. directamente.

### Hallazgos en el documento actual

| Problema | Ejemplo | Corrección |
|---|---|---|
| Cita de OPS sin nombre completo en primera mención | "La OPS (2024) define..." | Primera mención: "La Organización Panamericana de la Salud (OPS, 2024) define..." — luego "OPS (2024)" |
| "Bayona Castañeda (2019)" usa nombre + apellido | Consistente en el documento | APA usa solo apellido: "Bayona (2019)" — a menos que haya ambigüedad con otro autor Bayona |
| Cita con "et al.°" (grado) | "Mauricio et al.°(2024)" | Quitar el símbolo °: "Mauricio et al. (2024)" |
| Uso de punto y coma en citas múltiples | (Torab-Miandoab et al., 2023; Holmgren et al., 2023) | Correcto ✅ — en APA 7 las citas múltiples se separan con `;` y van en orden alfabético |

---

## 4. Lista de referencias

### 4.1. Principios generales

- **Toda fuente citada** en el texto debe aparecer en la lista de referencias.
- **Toda entrada** en la lista de referencias debe estar citada en el texto.
- Ordenar **alfabéticamente** por el apellido del primer autor.
- **Sangría francesa** de 1.27 cm (½ pulgada).
- **Interlineado doble**.
- No numerar las entradas.

### 4.2. Elementos de una referencia (4 componentes)

```
Autor(es). (Año). Título del trabajo. Fuente.
```

| Componente | Descripción |
|---|---|
| **Autor** | Apellido, Inicial(es). Separar múltiples autores con `,` y usar `&` antes del último. Hasta 20 autores se listan todos; más de 20: primeros 19, `...`, último. |
| **Fecha** | (Año). Si no hay fecha: (s.f.). |
| **Título** | *En cursiva* para obras independientes (libros, informes, tesis). Sin cursiva para partes de obras (artículos, capítulos). |
| **Fuente** | Revista + volumen + número + páginas + DOI/URL. Para libros: editorial + DOI/URL. |

### 4.3. Formatos comunes para esta tesis

#### Artículo de revista científica
```
Apellido, A. A., Apellido, B. B., & Apellido, C. C. (Año). Título del artículo.
    Nombre de la Revista, Volumen(Número), páginas. https://doi.org/xx.xxxx
```

**Ejemplo correcto (de la tesis):**
```
Adelusi, B. S., Osamika, D., Chinyeaka Kelvin-Agwu, M., Mustapha, A. Y.,
    Forkuo, A. Y., & Ikhalea, N. (2025). A Federated Interoperability Framework
    for Seamless Health Data Exchange Using FHIR Standards Across Multi-Hospital
    Systems. Engineering and Technology Journal, 10(05).
    https://doi.org/10.47191/etj/v10i05.03
```

> **Reglas del título del artículo:** Solo primera palabra y nombres propios en mayúscula ("sentence case"). Nombre de la revista en *cursiva* y Title Case.

#### Tesis o disertación
```
Apellido, A. A. (Año). Título de la tesis [Tesis de maestría/doctoral,
    Nombre de la Universidad]. Nombre del Repositorio.
    https://url-del-repositorio
```

**Ejemplo correcto (de la tesis):**
```
Porras Gamarra, H. J. (2024). Implementación de un sistema de interoperabilidad
    de información clínica basado en los estándares internacionales HL7 FHIR y
    openEHR [Trabajo de suficiencia profesional, Universidad Nacional Federico
    Villarreal]. Repositorio UNFV.
```

#### Libro
```
Apellido, A. A. (Año). Título del libro (N.ª ed.). Editorial.
    https://doi.org/xx.xxxx
```

#### Informe / documento institucional
```
Nombre de la Organización. (Año). Título del documento. Editorial/Organización.
    https://url
```

**Ejemplo:**
```
Organización Panamericana de la Salud (OPS). (2024). Guía de implementación de
    interoperabilidad de sistemas de información en salud. OPS.
```

#### Página web
```
Autor. (Fecha). Título de la página. Nombre del Sitio Web.
    https://url
```

### 4.4. Reglas de DOI y URL

| Regla | Detalle |
|---|---|
| **Formato DOI** | Siempre como URL: `https://doi.org/10.xxxx/yyyy` |
| **No insertar saltos de línea** en URLs | Las quiebras automáticas del procesador son aceptables |
| **DOI disponible** | Siempre incluirlo; prevalece sobre la URL |
| **Sin DOI + online** | Incluir URL directa del contenido |
| **Sin DOI + impreso** | No incluir URL |
| **No escribir** "Recuperado de" ni "Disponible en" | Colocar la URL directamente |

> **Excepción:** Para contenidos que cambian con el tiempo, usar: "Recuperado el [fecha], de [URL]".

### Hallazgos en la lista de referencias actual

| Problema | Ejemplo | Corrección |
|---|---|---|
| Referencias con viñeta `-` | `- Adelusi, B. S., ...` | APA no numera ni usa viñetas en referencias. Eliminar `-` y usar sangría francesa. |
| Título de artículo en cursiva | Algunos usos inconsistentes | Solo el nombre de la revista va en cursiva, no el título del artículo |
| Falta cursiva en nombre de revista | Verificar todos | Nombre de la revista siempre en *cursiva* |
| Tesis sin tipo entre corchetes | Algunas tesis carecen de `[Tesis de maestría, ...]` | Incluir tipo y universidad entre corchetes |
| URLs sin hipervínculo funcional | Verificar en DOCX generado | Asegurar que los enlaces sean funcionales |

---

## 5. Tablas

### 5.1. Componentes APA 7 de una tabla

| Componente | Formato |
|---|---|
| **Número** | "Tabla 1", "Tabla 2"... en **negrita**, sobre el título |
| **Título** | En línea siguiente, *cursiva*, interlineado doble, descriptivo y breve |
| **Encabezados** | Centrados o alineados, separados por líneas horizontales |
| **Cuerpo** | Interlineado sencillo, 1.5 o doble |
| **Notas** | Debajo de la tabla. Tres tipos: general, específica, de probabilidad |
| **Líneas** | Solo bordes horizontales (superior, bajo encabezado, inferior). Sin bordes verticales ni cuadrícula completa. |

### 5.2. Citación de tablas en el texto

- Referirse siempre por su número: "como se muestra en la Tabla 1" o "(ver Tabla 1)".
- **Nunca** referirse por posición: "la tabla anterior" o "la tabla de la página 12".

### Hallazgos en el documento actual

| Problema | Ejemplo | Corrección |
|---|---|---|
| Las tablas usan Markdown con caption al final | `: Tabla 1. Matriz de operacionalización` | APA requiere número en negrita encima, título en cursiva debajo. Verificar renderizado en DOCX. |
| Tabla de operacionalización de variables muy ancha | Variable repetida en múltiples filas | El formato es aceptable para tabla extensa; verificar que el renderizado DOCX mantenga legibilidad |
| Bordes de tabla | `aplicar_bordes_tablas()` en `generar_tesis.py` | Verificar que solo aplique bordes horizontales (APA 7: sin bordes verticales) |

---

## 6. Figuras

### 6.1. Componentes APA 7 de una figura

| Componente | Formato |
|---|---|
| **Número** | "Figura 1", "Figura 2"... en **negrita**, sobre la imagen |
| **Título** | En línea siguiente, *cursiva*, descriptivo, interlineado doble |
| **Imagen** | La figura propiamente dicha |
| **Leyenda** | Dentro de la figura si es necesario |
| **Nota** | Debajo de la figura. Para atribución, usar nota general. |

### 6.2. Notas de figuras

| Tipo de nota | Uso | Formato |
|---|---|---|
| **General** | Explicación general, fuente | *Nota.* Texto de la nota. |
| **Específica** | Señalar elementos puntuales | Letras superíndice. |
| **De probabilidad** | Significancia estadística | Asteriscos: *p < .05 |

### 6.3. Atribución de fuentes en figuras

| Caso | Acción APA 7 |
|---|---|
| **Elaboración propia** | No es necesario agregar ninguna declaración. APA asume que todo sin cita es del propio autor. Sin embargo, para claridad académica es aceptable incluir "*Nota.* Elaboración propia." |
| **Adaptada de otra fuente** | *Nota.* Adaptado de "Título", por Autor, Año, *Fuente* (DOI/URL). CC BY 4.0. |
| **Reproducida de otra fuente** | *Nota.* De "Título", por Autor, Año, *Fuente* (DOI/URL). Copyright Año por Titular. Reproducido con autorización. |

### 6.4. Citación de figuras en el texto

- Referirse por número: "como se observa en la Figura 1" o "(ver Figura 2)".
- **Nunca** por posición relativa: "la figura de arriba", "la siguiente figura".

### Hallazgos en el documento actual

| Problema | Ejemplo | Corrección |
|---|---|---|
| Las notas de figura dicen "*Nota.* Elaboración propia." | Todas las figuras | Técnicamente innecesario en APA (se asume autoría propia si no hay cita), pero aceptable y recomendable en el contexto de tesis de maestría ✅ |
| Formato del caption en Markdown | `![Título](ruta.png)` | Pandoc genera estilo "ImageCaption"; verificar que se renderice como cursiva debajo de la imagen |
| No se indica "Figura N." en negrita encima | Pandoc + `numerar_captions_figuras()` lo agrega | Verificar que el DOCX resultante tenga: **Figura 1** (en negrita, línea propia), luego *Título en cursiva* |

### Estado actual de figuras

| N.° | Descripción | Nota de fuente |
|---|---|---|
| Figura 1 | Fases del enfoque metodológico | Elaboración propia ✅ |
| Figura 2 | Evolución de estándares de interoperabilidad clínica | Elaboración propia basada en Surisetty (2026) y Amar et al. (2024) ✅ |
| Figura 3 | Enfoques teóricos que sustentan la investigación | Elaboración propia ✅ |
| Figura 4 | Niveles de interoperabilidad en salud según HIMSS | Elaboración propia basada en HIMSS, citado en Amar et al. (2024) y OPS (2024) ✅ |
| Figura 5 | Recursos FHIR principales y sus relaciones | Elaboración propia basada en HL7 International (2019) y Pimenta et al. (2023) ✅ |
| Figura 6 | Marco conceptual de la investigación | Elaboración propia ✅ |

---

## 7. Estructura del documento de tesis

### 7.1. Orden de secciones APA 7

APA 7 define el siguiente orden:

1. Portada
2. Resumen / Abstract
3. Texto principal (cuerpo)
4. Referencias
5. Notas al final (si aplica)
6. Tablas (si van al final)
7. Figuras (si van al final)
8. Apéndices / Anexos

### 7.2. Orden actual de la tesis (adaptado al reglamento universitario)

1. Portada ✅
2. Agradecimiento
3. Índice (Tabla de contenido)
4. Índice de tablas
5. Índice de figuras
6. Resumen ✅
7. Abstract ✅
8. Introducción ✅
9. Capítulo I: Planteamiento del estudio
10. Capítulo II: Marco teórico
11. Capítulo III: Hipótesis y variables
12. Capítulo IV: Metodología del estudio
13. Capítulo V: Aspectos administrativos
14. Referencias ✅
15. Anexos

> **Nota:** La estructura sigue el reglamento de la universidad, que difiere ligeramente de la estructura APA estándar (IMRaD). Esto es correcto; APA 7 permite adaptaciones según los requerimientos institucionales.

---

## 8. Resumen y Abstract

| Elemento | Norma APA 7 | Estado actual |
|---|---|---|
| Extensión | 150-250 palabras | Verificar |
| Nuevo párrafo | Sin sangría (excepción) | Verificar en `reference.docx` |
| Interlineado | Doble | Verificar |
| Palabras clave | En nueva línea, con sangría. Etiqueta en *Cursiva*: "*Palabras clave:*" | Actualmente en **negrita**: `**Palabras claves:**` → cambiar a cursiva: `*Palabras clave:*` |
| Keywords (inglés) | Mismas reglas | Actualmente en **negrita**: `**Keywords:**` → cambiar a cursiva: `*Keywords:*` |

### Hallazgo: "Palabras claves" vs "Palabras clave"

APA 7 en español usa "Palabras clave" (sin "s" final). La forma actual `**Palabras claves:**` debe corregirse a `*Palabras clave:*`.

---

## 9. Uso de cursiva y negrita en el texto

### 9.1. Cuándo usar cursiva

| Uso | Ejemplo |
|---|---|
| Títulos de libros, revistas, informes | *JMIR Medical Informatics* |
| Palabras en otro idioma (primera vez) | *running head* |
| Términos técnicos al introducirlos | *Fast Healthcare Interoperability Resources* |
| Escalas y puntuaciones | *p* < .05 |
| Anclas de escala | de *totalmente en desacuerdo* a *totalmente de acuerdo* |

### 9.2. Cuándo usar negrita

| Uso |
|---|
| Títulos y subtítulos (según nivel) |
| Etiquetas "Tabla 1", "Figura 1" |

### 9.3. Cuándo NO usar cursiva ni negrita

| Caso |
|---|
| Nombres propios de software (SPSS, R, JMeter) |
| Siglas y acrónimos (FHIR, HL7, MINSA) |
| Frases en otro idioma de uso común (*per se*, *versus*) — si ya están integradas al español |

### Hallazgos

| Problema | Ejemplo | Corrección |
|---|---|---|
| Uso excesivo de negrita en antecedentes | `**Aporte:**`, `**Problema:**`, `**Objetivo:**` | El formato estructurado de antecedentes no es APA estricto, pero es aceptable como formato institucional. Mantener consistencia. |
| Nombres de revistas sin cursiva en texto | "publicado en Healthcare, MDPI" | Poner en cursiva: "publicado en *Healthcare*" |

---

## 10. Números y estadísticas

| Regla APA 7 | Ejemplos |
|---|---|
| Números del 0-9 en letras (regla general) | "tres fases", "cinco países" |
| Números ≥ 10 en cifras | "36 estudios", "70 estudios" |
| **Excepciones (siempre en cifras):** | |
| Antes de unidad de medida | "5 cm", "12 pt" |
| Valores estadísticos | "p < .05", "95 %" |
| Porcentajes | "42 %", "95 %" |
| Que representan datos | "n = 36", "N = 2 200" |
| Inicio de oración | Siempre en letras: "Treinta y seis estudios..." |

### Hallazgo

| Problema | Ejemplo | Corrección |
|---|---|---|
| Números pequeños a veces como cifras | "tres fases" (correcto), "cuatro enfoques" (correcto) | Mantener consistencia ✅ |
| Porcentajes | "42 %" con espacio | APA 7 acepta ambas formas (42% o 42 %); mantener consistencia interna |

---

## 11. Listas y viñetas

| Tipo | Uso APA 7 | Formato |
|---|---|---|
| **Lista con viñetas** | Ítems sin orden jerárquico | Guion o bullet, con sangría |
| **Lista numerada** | Ítems en secuencia u orden | 1., 2., 3. |
| **Lista dentro del párrafo** | Enumerar opciones | (a) primero, (b) segundo, (c) tercero |

> **Estado actual:** La tesis usa viñetas con `-` (Markdown) que Pandoc convierte a bullets. Los problemas específicos usan `1.-`, `2.-`. APA usa `1.` sin guion: corregir `1.-` a `1.`.

---

## 12. Checklist de verificación APA 7

Usar esta lista cada vez que se modifique o agregue contenido a la tesis:

### Formato general
- [ ] Márgenes de 2.54 cm en todos los lados
- [ ] Times New Roman 12 pt (o Calibri 11 pt)
- [ ] Interlineado doble en todo el documento
- [ ] Sangría de primera línea 1.27 cm en párrafos
- [ ] Numeración de páginas en esquina superior derecha
- [ ] Sin espacio extra entre párrafos

### Títulos
- [ ] Nivel 1 (H1): Centrado, negrita, Title Case
- [ ] Nivel 2 (H2): Alineado izquierda, negrita, Title Case
- [ ] Nivel 3 (H3): Alineado izquierda, negrita cursiva, Title Case
- [ ] Sin marcadores `->` ni `.-` en numeración de títulos
- [ ] Cada título seguido de texto (nunca dos títulos consecutivos sin texto)

### Citas en texto
- [ ] 1-2 autores: apellidos completos siempre
- [ ] 3+ autores: "et al." desde la primera cita
- [ ] Citas múltiples separadas por `;` en orden alfabético dentro del paréntesis
- [ ] Organizaciones: nombre completo (abreviatura) en primera mención
- [ ] Citas textuales <40 palabras: entre comillas, (autor, año, p. X)
- [ ] Citas textuales ≥40 palabras: bloque con sangría, sin comillas
- [ ] Toda cita tiene referencia y toda referencia tiene cita

### Tablas
- [ ] Número en negrita sobre la tabla
- [ ] Título en cursiva debajo del número
- [ ] Solo bordes horizontales (sin cuadrícula completa)
- [ ] Notas al pie de tabla cuando sea necesario
- [ ] Citada en el texto por número

### Figuras
- [ ] Número en negrita sobre la figura
- [ ] Título en cursiva debajo del número
- [ ] Nota de fuente debajo si no es elaboración propia
- [ ] Citada en el texto por número

### Referencias
- [ ] Orden alfabético por apellido del primer autor
- [ ] Sangría francesa 1.27 cm
- [ ] Interlineado doble
- [ ] Sin viñetas ni numeración
- [ ] DOI con formato https://doi.org/xx.xxxx
- [ ] Nombre de revista en cursiva
- [ ] Título de artículo en sentence case (solo primera palabra en mayúscula)
- [ ] Tesis con [Tipo de tesis, Universidad] entre corchetes
- [ ] Toda entrada citada en el texto (y viceversa)

### Resumen / Abstract
- [ ] 150-250 palabras
- [ ] Sin sangría en el párrafo
- [ ] *Palabras clave:* en cursiva (no negrita)
- [ ] *Keywords:* en cursiva (no negrita)

---

## 13. Correcciones pendientes identificadas

### Alta prioridad

1. **Quitar viñetas `-` en la lista de referencias.** APA usa sangría francesa sin bullets.
2. **Cambiar `**Palabras claves:**` → `*Palabras clave:*`** y `**Keywords:**` → `*Keywords:*`** (cursiva, sin "s").
3. **Eliminar marcadores `->` y `.-`** en títulos de secciones (usar solo `.` o nada).
4. **Verificar que `et al.°` no tenga el símbolo °** en citas (buscar y reemplazar).
5. **Primera mención de OPS:** escribir nombre completo antes de abreviatura.

### Media prioridad

6. **Verificar cursiva en nombres de revistas** en todo el texto narrativo.
7. **Verificar bordes de tablas** en DOCX: solo horizontales (sin verticales).
8. **Formato de figuras:** Confirmar que el DOCX muestra "**Figura N**" en negrita + título en cursiva.
9. **Numeración de problemas/objetivos:** Cambiar `1.-` → `1.` (sin guion).
10. **Bayona Castañeda (2019):** APA usa normalmente solo el primer apellido salvo ambigüedad. Verificar si "Bayona" es suficiente o si la ficha bibliográfica requiere ambos apellidos por ser el formato del autor.

### Baja prioridad

11. **Verificar interlineado doble** en todo el DOCX generado.
12. **Verificar sangría de primera línea** en párrafos del cuerpo.
13. **Verificar encabezado** (solo número de página, sin running head si es formato estudiante).
14. **Consistencia en capitalización** de títulos de sección.

---

## 14. Referencia rápida de la guía APA 7

**Fuente oficial:**
American Psychological Association. (2020). *Publication manual of the American Psychological Association* (7th ed.). https://doi.org/10.1037/0000165-000

**Guía resumida utilizada:**
Guía Normas APA 7.ª edición — Basada en el contenido de https://normas-apa.org/
