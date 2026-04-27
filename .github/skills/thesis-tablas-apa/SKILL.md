---
name: thesis-tablas-apa
description: Crear, editar o uniformar tablas para que rendericen como tabla APA real en el DOCX final. Usar cuando el usuario pide "agregar una tabla", "convertir esta lista a tabla", "la tabla N salió desordenada en Word", o cuando se inserta una tabla nueva en el Markdown.
---

# Tablas en formato APA (Pandoc → DOCX)

## Regla número 1

**Solo Markdown pipe tables.** Nada de HTML (`<table>`), nada de tablas
"grid" Pandoc, nada de tablas embebidas como imagen.

Toda modificación de tablas se realiza en
`content/manuscript/Documento_Tesis.md`; no se corrigen tablas editando
`build/tesis.docx`.

Razón: solo las pipe tables con caption se postprocesan correctamente para
quedar con el estilo APA (número en negrita arriba, título en cursiva
abajo, solo bordes horizontales, ancho fijo).

## Plantilla canónica

```markdown

: Tabla 7. <Título descriptivo de la tabla> {#tbl:slug-unico}

| <Columna 1> | <Columna 2> | <Columna 3> | <Columna 4> |
|-------------|-------------|-------------|-------------|
| <Valor>     | <Valor>     | <Valor>     | <Valor>     |
| <Valor>     | <Valor>     | <Valor>     | <Valor>     |
| <Valor>     | <Valor>     | <Valor>     | <Valor>     |

Nota. Elaboración propia con base en <Autor1> (<Año>) y <Autor2> (<Año>).

```

> Reemplaza los placeholders `<...>` por el contenido real del dominio
> de tu tesis. El `slug` del caption debe ser kebab-case y único en
> todo el documento (p. ej. `tbl:metodos-comparados`, `tbl:variables-op`).


Detalles obligatorios:

- **Caption en su propia línea**, comenzando con `: Tabla N. <Título>`,
  seguida de `{#tbl:slug}` (slug en kebab-case, único en todo el documento).
- **Una línea en blanco** antes y después del caption y de la tabla.
- **Pipes alineados** (no es obligatorio para Pandoc, pero ayuda al diff).
- **Encabezado de columna** siempre presente (no tablas sin header).
- **Nota debajo** de la tabla en formato `Nota. <texto>` (con punto). Esto
  no requiere `custom-style`; el postproceso lo detecta.

## Numeración

- La numeración `Tabla N.` es **manual y consecutiva** en orden de aparición.
- Cuando se inserta una tabla nueva en medio del documento, **renumerar
  todas las posteriores** y actualizar las referencias en texto.
- Para evitar inconsistencias, usar `thesis-scripts-fix` para renumerar
  con un script (no a mano si hay > 5 tablas afectadas).

## Referencias en texto

Toda tabla **debe ser referenciada** en el cuerpo al menos una vez, con
la forma explícita `**La Tabla N** <verbo>` (no "la tabla siguiente", no
"como se ve a continuación"):

> La Tabla 7 sintetiza <breve descripción de lo que la tabla compara o
> resume>.

Si una tabla queda sin referencia en texto, el asesor la marca como
huérfana. Validar con:

```powershell
Select-String -Path Documento_Tesis.md -Pattern "siguiente tabla" -SimpleMatch
```

## Postproceso aplicado por `platform/scripts/build/build_thesis.py`

- Inserta el número en negrita en la línea superior.
- Pone el título en cursiva.
- Limpia bordes verticales (solo bordes horizontales: arriba, debajo del
  encabezado, abajo).
- Aplica fuente Times New Roman 11 al contenido y 12 al título.
- Quita relleno de color de filas alternadas si pandoc las introduce.

Si una tabla **no se postprocesa** (sigue con bordes completos), suele ser
porque:

- Falta el caption con `:` al inicio.
- El caption está pegado a la tabla sin línea en blanco.
- Hay HTML mezclado dentro de las celdas.

## Tablas multipágina

- Pandoc no soporta repetir el encabezado en cada página automáticamente
  desde Markdown. Si una tabla pasa de una página, después de generar el
  DOCX:
  1. Abrir Word, usar el menú contextual en la fila de encabezado → *Repetir como
     fila de encabezado*.
  2. Anotar este paso manual en el changelog para no olvidarlo en la
     próxima regeneración.

## Tablas comparativas de antecedentes

La columna `Aporte a la tesis` debe ser la última y debe coincidir con la
frase usada en `**En relación con esta tesis,**` del antecedente
(ver `thesis-antecedentes`).

## Anti-patrones

- Doble numeración (`Tabla 13. Tabla 4.`): pasa cuando un caption interno
  duplica el "Tabla N" manual; revisar la columna `caption` del Markdown.
- Captions como `**Tabla 7.** *Título*` en negrita+cursiva manual: no.
  La negrita la pone el postproceso.
- Bordes verticales: si aparecen en el DOCX, regenerar; no editar a mano
  el `.docx`.
- Tablas con celdas multilinea separadas por `<br>`: usar pipe tables
  con texto plano y un `; ` como separador, o partir en dos filas.
- Anidar tablas: no soportado en Pandoc → DOCX.
