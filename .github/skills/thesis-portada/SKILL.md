---
name: thesis-portada
description: Construir o editar la portada (carátula) del proyecto de tesis. Usar cuando el usuario pide cambiar título, autores, año, sede, grado, o cuando reporta que la portada no se ve centrada o pierde formato.
---

# Carátula / Portada

## Modo soportado

La fuente de verdad de los datos de portada es
`content/manuscript/Documento_Tesis.md`.

`platform/templates/styles/caratula.docx` es una plantilla genérica con
placeholders. Durante el build, `platform/scripts/build/build_thesis.py` lee la
portada Markdown, rellena esos placeholders en `build/_caratula_temp.docx` y
concatena esa carátula generada al DOCX final.

No guardar títulos, autores, instituciones o datos de un tema concreto dentro
de `platform/templates/styles/caratula.docx`.

## Plantilla del modo Markdown (referencia)

```markdown
::: {custom-style="Portada-Centrado"}
![](../media/figures/logo-institucional.png){height=2.8cm}
:::

::: {custom-style="Portada-Centrado"}
**<PROGRAMA DE POSGRADO>**
:::

::: {custom-style="Portada-Centrado"}
**PROYECTO DE TESIS**
:::

::: {custom-style="Portada-Centrado"}
&nbsp;
:::

::: {custom-style="Portada-Centrado"}
**"<TÍTULO DE LA TESIS EN MAYÚSCULAS>"**
:::

::: {custom-style="Portada-Centrado"}
PRESENTADO POR:
:::

::: {custom-style="Portada-Centrado"}
**Bach. <APELLIDOS Y NOMBRES>**
:::

::: {custom-style="Portada-Centrado"}
PARA OPTAR EL GRADO ACADÉMICO DE:
:::

::: {custom-style="Portada-Centrado"}
**<GRADO ACADÉMICO>**
:::

::: {custom-style="Portada-Centrado"}
**<CIUDAD>**

**AÑO**
:::

\newpage
```

## Reglas estrictas

- Cada línea de la portada va dentro de su propio bloque `::: {custom-style="Portada-Centrado"} ... :::`. No agrupar varias líneas en un mismo bloque salvo que se quieran como un único párrafo (`<CIUDAD>` / `<AÑO>` sí pueden ir juntos).
- El estilo `Portada-Centrado` está definido en `platform/templates/styles/plantilla_estilos.docx` y lo usa `platform/scripts/build/build_thesis.py`. **No renombrarlo.**
- Para crear espacio vertical entre bloques, usar un bloque con `&nbsp;` (no líneas en blanco; Pandoc las colapsa).
- El logo debe vivir en `content/media/figures/` y se ancla con `{height=2.8cm}`.
- El título va en **mayúsculas, negrita y entre comillas tipográficas curvas** (`"…"`), no comillas rectas.

## Cuándo cambiar la plantilla DOCX

- Cuando el reglamento exige una imagen específica (recibo de caja, sello), márgenes especiales o tipografía no replicable con estilos de Pandoc.
- Cuando hay logo + texto en disposición compleja (dos columnas, recuadros).

Para regenerar la plantilla: partir de una carátula institucional, reemplazar
todo dato concreto por placeholders (`<TITULO DE LA TESIS>`, `<AUTOR 1>`, etc.)
y guardar solo la primera página como `platform/templates/styles/caratula.docx`.

## Datos a verificar siempre antes de cerrar la versión

- [ ] Título exacto (con cambios sugeridos por asesor).
- [ ] Nombres completos en orden alfabético por apellido.
- [ ] Grado al que se opta concuerda con el programa.
- [ ] Año = año de sustentación, no de inicio.
- [ ] Sede correcta.

## Anti-patrones

- Insertar `<center>...</center>` HTML: no se aplica.
- Usar `# Portada` como heading 1: produce entrada en el índice.
- Olvidar el `\newpage` final: el Índice queda pegado a la portada.
