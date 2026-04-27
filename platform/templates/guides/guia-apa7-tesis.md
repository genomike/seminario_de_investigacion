# Guia de aplicacion APA 7 para tesis

> Proposito: servir como referencia rapida y agnostica para mantener el
> manuscrito en formato APA 7 y compatible con el pipeline Markdown -> Pandoc
> -> DOCX. Los ejemplos usan placeholders; reemplazarlos por datos reales del
> tema de cada tesis.

---

## 1. Formato general

| Elemento | Regla APA 7 | Aplicacion en el repo |
|---|---|---|
| Papel | Carta o el formato exigido por la universidad | Validar en `platform/templates/styles/plantilla_estilos.docx` |
| Margenes | 2.54 cm como base APA | Ajustar solo en el reference-doc |
| Fuente | Times New Roman 12 pt o fuente APA permitida | Mantener consistencia en todo el DOCX |
| Interlineado | Doble en texto academico | Tablas pueden usar sencillo o 1.5 si la legibilidad lo exige |
| Sangria | Primera linea 1.27 cm | Configurar en estilo Normal |
| Referencias | Sangria francesa 1.27 cm | Configurar en estilo Bibliography |
| Paginas | Numeracion continua | Encabezado en la zona superior externa salvo norma institucional distinta |

## 2. Estructura base de tesis

Orden recomendado para este pipeline:

1. Portada.
2. Agradecimiento o dedicatoria, si aplica.
3. Indice general.
4. Indice de tablas.
5. Indice de figuras.
6. Resumen.
7. Abstract.
8. Introduccion.
9. Capitulos de la escuela o programa.
10. Referencias.
11. Anexos.

La estructura institucional prevalece sobre la estructura APA estandar cuando
la universidad exige un orden especifico.

## 3. Titulos y subtitulos

| Nivel APA | Markdown | Formato esperado |
|---|---|---|
| Nivel 1 | `# Capitulo I: Titulo` | Centrado, negrita |
| Nivel 2 | `## 1.1. Titulo` | Alineado izquierda, negrita |
| Nivel 3 | `### 1.1.1. Titulo` | Alineado izquierda, negrita cursiva |

Reglas:

- No usar marcadores como `->` o `.-` en numeracion.
- No dejar dos titulos consecutivos sin texto entre ellos.
- Mantener el mismo criterio de mayusculas en todos los capitulos.

## 4. Citas en texto

| Caso | Forma narrativa | Forma parentetica |
|---|---|---|
| 1 autor | Apellido (Ano) sostiene... | (Apellido, Ano) |
| 2 autores | Apellido1 y Apellido2 (Ano) | (Apellido1 y Apellido2, Ano) |
| 3+ autores | Apellido1 et al. (Ano) | (Apellido1 et al., Ano) |
| Institucion primera vez | Nombre Completo (SIGLA, Ano) | (Nombre Completo [SIGLA], Ano) |
| Institucion siguientes | SIGLA (Ano) | (SIGLA, Ano) |
| Cita textual | Apellido (Ano, p. NN) | (Apellido, Ano, p. NN) |

Reglas:

- Usar `et al.` desde la primera cita cuando hay tres o mas autores.
- En espanol, unir dos autores con `y`, no con `&`, dentro del texto.
- En citas multiples, ordenar alfabeticamente y separar con `;`.
- El punto va despues del parentesis: `... (Apellido, Ano).`
- Citas textuales de 40 palabras o mas van en bloque con sangria, sin comillas.

## 5. Lista de referencias

Seccion `# Referencias`, sin vinetas ni numeracion. Orden alfabetico por el
apellido del primer autor.

### Articulo con DOI

```markdown
Apellido, A. A., Apellido, B. B., y Apellido, C. C. (Ano). Titulo del
articulo en sentence case. *Nombre de la Revista*, *volumen*(numero),
pp-pp. https://doi.org/10.xxxx/yyyy
```

### Articulo sin DOI con URL

```markdown
Apellido, A. A. (Ano). Titulo del articulo. *Nombre de la Revista*,
*volumen*(numero), pp-pp. https://url
```

### Tesis o trabajo academico

```markdown
Apellido, A. A. (Ano). *Titulo de la tesis* [Tesis de maestria,
Nombre de la Universidad]. Nombre del Repositorio. https://url
```

### Libro

```markdown
Apellido, A. A., y Apellido, B. B. (Ano). *Titulo del libro* (edicion si
aplica). Editorial. https://doi.org/10.xxxx/yyyy
```

### Informe institucional o norma

```markdown
Nombre Completo de la Institucion. (Ano). *Titulo del documento* (codigo o
numero si aplica). https://url-oficial
```

## 6. Tablas

Usar siempre Markdown pipe tables con caption Pandoc:

```markdown
: Tabla N. Titulo breve y descriptivo {#tbl:slug-unico}

| Columna 1 | Columna 2 | Columna 3 |
|---|---|---|
| Valor | Valor | Valor |

Nota. Elaboracion propia con base en Apellido (Ano).
```

Reglas:

- El caption debe iniciar con `: Tabla N.` y tener identificador unico.
- Toda tabla debe citarse en el texto como `La Tabla N ...`.
- No usar HTML ni imagenes para tablas.
- Solo bordes horizontales en el DOCX final.

## 7. Figuras

Embed canonico:

```markdown
![Titulo descriptivo de la figura](../media/figures/diagrama-slug.png)
```

Reglas:

- El alt-text funciona como titulo de la figura.
- El numero `Figura N` lo agrega el postproceso.
- Toda figura debe citarse en el texto como `La Figura N ...`.
- Si la figura se adapta de otra fuente, agregar nota de atribucion.
- Si es elaboracion propia, la nota es opcional salvo exigencia institucional.

## 8. Resumen y Abstract

| Elemento | Regla |
|---|---|
| Extension | 150-250 palabras, o lo que exija la universidad |
| Parrafo | Sin sangria |
| Palabras clave | `*Palabras clave:* termino1; termino2; termino3` |
| Keywords | `*Keywords:* term1; term2; term3` |

## 9. Uso de cursiva y negrita

Usar cursiva para:

- Titulos de libros, revistas e informes.
- Terminos extranjeros no asimilados, en su primera aparicion.
- Simbolos estadisticos como *p*, *M*, *DE*.

Usar negrita para:

- Titulos segun nivel.
- Etiquetas `Tabla N` y `Figura N` cuando el postproceso las genere.

No usar negrita para resaltar frases completas de forma decorativa.

## 10. Numeros y estadistica

| Caso | Regla |
|---|---|
| 0-9 | En letras, salvo excepciones |
| 10 o mas | En cifras |
| Unidades de medida | Siempre en cifras |
| Porcentajes | En cifras y con criterio consistente |
| Estadisticos | Formato APA: *p* < .05, *n* = 30 |

## 11. Checklist de verificacion

### Formato

- [ ] Margenes y fuente consistentes en el reference-doc.
- [ ] Interlineado y sangrias revisados en DOCX.
- [ ] Numeracion de paginas continua.

### Citas y referencias

- [ ] Toda cita tiene entrada en referencias.
- [ ] Toda referencia esta citada en el texto.
- [ ] DOI como URL `https://doi.org/...`.
- [ ] Sin vinetas en referencias.
- [ ] Instituciones con nombre completo en primera mencion.

### Tablas y figuras

- [ ] Cada tabla y figura se menciona en el texto.
- [ ] Captions de tablas con `: Tabla N. ... {#tbl:...}`.
- [ ] Figuras con ruta relativa desde `content/manuscript/`.
- [ ] Notas de fuente cuando no sean elaboracion propia.

### Resumen

- [ ] `*Palabras clave:*` en cursiva, sin pluralizar `clave`.
- [ ] `*Keywords:*` en cursiva.

## 12. Validaciones rapidas

```powershell
# Marcadores de titulo no deseados
Select-String content/manuscript/Documento_Tesis.md -Pattern '->|\. -|\. -'

# DOI sin URL completa
Select-String content/manuscript/Documento_Tesis.md -Pattern '(?<![:/])10\.\d{4,9}/\S+'

# et al sin punto
Select-String content/manuscript/Documento_Tesis.md -Pattern 'et al\b(?!\.)'
```

## 13. Fuente base

American Psychological Association. (2020). *Publication manual of the
American Psychological Association* (7th ed.). https://doi.org/10.1037/0000165-000