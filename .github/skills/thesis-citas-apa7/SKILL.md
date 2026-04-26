---
name: thesis-citas-apa7
description: Reglas de citas en texto y de la lista de referencias en formato APA 7 aplicadas a esta tesis. Usar siempre que se inserte una cita nueva, se agregue una entrada a "# Referencias", o se detecte una inconsistencia (autores duplicados, DOI sin URL, et al. mal aplicado, etc.).
---

# Citas y referencias APA 7

## Fuente de autoridad del repo

[guia-apa7-tesis.md](../../../guia-apa7-tesis.md). Este SKILL.md resume las
reglas más usadas y los errores más frecuentes; ante duda, abrir la guía.

## Citas en el texto

| Caso | Forma narrativa | Forma parentética |
|---|---|---|
| 1 autor | Apellido (Año) afirma… | (Apellido, Año) |
| 2 autores | Apellido1 y Apellido2 (Año) | (Apellido1 y Apellido2, Año) |
| 3+ autores (1.ª y siguientes) | Apellido1 et al. (Año) | (Apellido1 et al., Año) |
| Cita textual con página | Apellido1 y Apellido2 (Año, p. NN) | (Apellido1 y Apellido2, Año, p. NN) |
| Múltiples fuentes | (Apellido1 et al., Año; Apellido2 et al., Año; Apellido3 et al., Año) — orden alfabético separado por `;` |
| Institución (1.ª vez) | Nombre Completo de la Institución (SIGLA, Año) | (Nombre Completo de la Institución [SIGLA], Año) |
| Institución (siguientes) | SIGLA (Año) | (SIGLA, Año) |

**Reglas:**

- `et al.` desde la **primera mención** cuando hay 3+ autores (APA 7,
  cambio respecto a APA 6).
- En español usar `y` (no `&`) para unir dos autores en el cuerpo del texto.
- Punto **después** del paréntesis: `…en el contexto estudiado
  (Apellido et al., Año).`
- Citas textuales > 40 palabras: bloque sangrado, sin comillas, cita al final.

## Lista de referencias

Sección **`# Referencias`** al final del documento, antes de Anexos.
Reglas globales:

- Orden **alfabético por apellido del primer autor**, luego por año
  ascendente (más antigua primero) si hay varias del mismo autor.
- **Sangría francesa** (la maneja el estilo `Bibliography` del
  reference-doc; no usar bullets ni numeración).
- DOI **siempre como URL**: `https://doi.org/10.xxxx/yyyy`. Sin "DOI:"
  delante. Sin punto final después de la URL.
- Nombres de revistas en *cursiva*; volumen también en *cursiva*.
- Títulos de artículos: solo capitalizar la primera palabra y nombres propios.
- Hasta 20 autores listados; entre el 19.º y el último, `…` (puntos
  suspensivos) y luego el último autor.

## Plantillas

### Artículo de revista con DOI

```markdown
Apellido1, A. B., Apellido2, C. D., Apellido3, E. F., y Apellido4, G. H. (Año).
Título del artículo en minúsculas salvo nombres propios. *Nombre de la
Revista en Cursiva*, *vol*(núm), ppágina-inicio-ppágina-fin.
https://doi.org/10.xxxx/yyyy
```

### Artículo sin DOI (con URL)

```markdown
Apellido, X. Y. (Año). Título del artículo. *Revista*, *vol*(núm), pp-pp.
https://www.example.org/path
```

### Tesis de maestría / doctorado

```markdown
Apellido, X. Y. (Año). *Título de la tesis* [Tesis de maestría,
Nombre de la Universidad]. Nombre del Repositorio Institucional.
https://hdl.handle.net/<handle>
```

### Libro

```markdown
Hernández-Sampieri, R., y Mendoza Torres, C. P. (2018). *Metodología de
la investigación: las rutas cuantitativa, cualitativa y mixta*. McGraw-Hill.
```

### Capítulo de libro

```markdown
Apellido, A. A. (Año). Título del capítulo. En B. B. Editor (Ed.),
*Título del libro* (pp. 100-120). Editorial. https://doi.org/...
```

### Informe institucional

```markdown
Nombre Completo de la Institución. (Año). *Título del informe o norma*
(Número o código si aplica). https://<dominio-oficial>/<ruta>
```

### Página web (informe en línea de organismo)

```markdown
Nombre Completo de la Institución. (Año). *Título del documento en línea*.
https://<dominio-oficial>/<ruta>
```

## Resumen y Abstract

- Bloque `*Palabras clave:*` (cursiva, sin "s" final, dos puntos), seguido
  de 3-5 términos separados por `;`. Ejemplo genérico:

  ```markdown
  *Palabras clave:* <término1>; <término2>; <término3>; <término4>
  ```

- En inglés, equivalente: `*Keywords:* <term1>; <term2>; <term3>; <term4>`.

## Validaciones rápidas

```powershell
# Citas dentro del texto que aún tienen "&" (deben ser "y" en español):
Select-String Documento_Tesis.md -Pattern '\(\w+ & \w+,'

# DOIs sin protocolo:
Select-String Documento_Tesis.md -Pattern '(?<![:/])10\.\d{4,9}/\S+' -CaseSensitive

# "et al" sin punto:
Select-String Documento_Tesis.md -Pattern 'et al\b(?!\.)'
```

## Anti-patrones

- "Et al." en mayúscula a media frase (solo va con mayúscula al inicio
  de una oración; en MAYÚSCULAS solo en los antecedentes — ver
  `thesis-antecedentes`).
- Listar 4 autores en el texto en vez de "et al.".
- DOI con `dx.doi.org` (formato antiguo) → cambiar a `doi.org`.
- Doble punto después de URL.
- Bullets en la lista de referencias.
- Mezclar idiomas en una misma referencia (ej. "y" en cita inglesa).
