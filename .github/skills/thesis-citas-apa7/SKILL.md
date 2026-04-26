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
| 1 autor | Adelusi (2025) afirma… | (Adelusi, 2025) |
| 2 autores | Mauricio y Pérez (2024) | (Mauricio y Pérez, 2024) |
| 3+ autores (1.ª y siguientes) | Adelusi et al. (2025) | (Adelusi et al., 2025) |
| Cita textual con página | Bender y Sartipi (2013, p. 326) | (Bender y Sartipi, 2013, p. 326) |
| Múltiples fuentes | (Adelusi et al., 2025; Heryawan et al., 2025; Tabari et al., 2024) — orden alfabético separado por `;` |
| Institución (1.ª vez) | Organización Panamericana de la Salud (OPS, 2023) | (Organización Panamericana de la Salud [OPS], 2023) |
| Institución (siguientes) | OPS (2023) | (OPS, 2023) |

**Reglas:**

- `et al.` desde la **primera mención** cuando hay 3+ autores (APA 7,
  cambio respecto a APA 6).
- En español usar `y` (no `&`) para unir dos autores en el cuerpo del texto.
- Punto **después** del paréntesis: `…en hospitales heterogéneos
  (Adelusi et al., 2025).`
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
Adelusi, B. S., Uzoka, A. C., Hassan, Y. G., y Ojika, F. U. (2025). Building
secure and interoperable health data systems through HL7 FHIR and federated
identity frameworks. *Engineering and Technology Journal*, *10*(7),
4855-4869. https://doi.org/10.47191/etj/v10i7.27
```

### Artículo sin DOI (con URL)

```markdown
Apellido, X. Y. (Año). Título del artículo. *Revista*, *vol*(núm), pp-pp.
https://www.example.org/path
```

### Tesis de maestría / doctorado

```markdown
Esparza Morgan, J. M. (2025). *Título de la tesis* [Tesis de maestría,
Universidad de San Ignacio de Loyola]. Repositorio USIL.
https://hdl.handle.net/20.500.14005/16177
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
Ministerio de Salud del Perú. (2024). *Resolución Ministerial N.º 1104-2024/MINSA*.
https://www.gob.pe/institucion/minsa/normas-legales/...
```

### Página web (informe en línea de organismo)

```markdown
Organización Panamericana de la Salud. (2023). *Estado de la
interoperabilidad en salud en América Latina*. https://www.paho.org/...
```

## Resumen y Abstract

- Bloque `*Palabras clave:*` (cursiva, sin "s" final, dos puntos), seguido
  de 3-5 términos separados por `;`. Ejemplo:

  ```markdown
  *Palabras clave:* interoperabilidad; HL7 FHIR; historia clínica electrónica; Perú
  ```

- En inglés, equivalente: `*Keywords:* interoperability; HL7 FHIR; electronic health record; Peru`.

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
