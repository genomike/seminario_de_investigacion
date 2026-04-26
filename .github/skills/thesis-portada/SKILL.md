---
name: thesis-portada
description: Construir o editar la portada (carátula) del proyecto de tesis. Usar cuando el usuario pide cambiar título, autores, año, sede, grado, o cuando reporta que la portada no se ve centrada o pierde formato.
---

# Carátula / Portada

## Dos modos soportados

El pipeline acepta **uno** de estos modos (excluyentes):

1. **Carátula manual pre-armada en Word** (recomendado).
   Existe `platform/templates/styles/caratula.docx` en la raíz; `platform/scripts/build/build_thesis.py` lo concatena al inicio
   del DOCX final. **Si está**, no se renderiza la portada del Markdown.
2. **Carátula desde el Markdown** vía divs con `custom-style="Portada-Centrado"`.
   Aplica si se borra `platform/templates/styles/caratula.docx`.

> Verificar siempre `Test-Path caratula.docx` antes de tocar la portada del MD.

## Plantilla del modo Markdown (referencia)

```markdown
::: {custom-style="Portada-Centrado"}
![](media/image1.png){height=2.8cm}
:::

::: {custom-style="Portada-Centrado"}
**MAESTRÍA EN INGENIERÍA DE SOFTWARE**
:::

::: {custom-style="Portada-Centrado"}
**PROYECTO DE TESIS**
:::

::: {custom-style="Portada-Centrado"}
&nbsp;
:::

::: {custom-style="Portada-Centrado"}
**"TÍTULO EN MAYÚSCULAS Y NEGRITA ENTRE COMILLAS TIPOGRÁFICAS"**
:::

::: {custom-style="Portada-Centrado"}
PRESENTADO POR:
:::

::: {custom-style="Portada-Centrado"}
**Bach. Apellido Apellido Nombres**
:::

::: {custom-style="Portada-Centrado"}
PARA OPTAR EL GRADO ACADÉMICO DE:
:::

::: {custom-style="Portada-Centrado"}
**MAESTRO(A) EN INGENIERÍA DE SOFTWARE**
:::

::: {custom-style="Portada-Centrado"}
**LIMA**

**AÑO**
:::

\newpage
```

## Reglas estrictas

- Cada línea de la portada va dentro de su propio bloque `::: {custom-style="Portada-Centrado"} ... :::`. No agrupar varias líneas en un mismo bloque salvo que se quieran como un único párrafo (LIMA / AÑO sí van juntos).
- El estilo `Portada-Centrado` está definido en `platform/templates/styles/plantilla_estilos.docx` por `generar_tesis.preparar_reference_doc()`. **No renombrarlo.**
- Para crear espacio vertical entre bloques, usar un bloque con `&nbsp;` (no líneas en blanco; Pandoc las colapsa).
- El logo es `media/image1.png` y se ancla con `{height=2.8cm}`.
- El título va en **mayúsculas, negrita y entre comillas tipográficas curvas** (`"…"`), no comillas rectas.

## Cuándo cambiar a `platform/templates/styles/caratula.docx` manual

- Cuando el reglamento exige una imagen específica (recibo de caja, sello), márgenes especiales o tipografía no replicable con estilos de Pandoc.
- Cuando hay logo + texto en disposición compleja (dos columnas, recuadros).

Para regenerar la portada manual: abrir `documentos_apoyo/Plantilla de informe de tesis maestría-llenada.docx`, copiar la primera página y guardar como `platform/templates/styles/caratula.docx` en la raíz.

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
