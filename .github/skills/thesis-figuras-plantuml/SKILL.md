---
name: thesis-figuras-plantuml
description: Crear o regenerar figuras y diagramas (PlantUML → PNG → embed en MD). Usar cuando el usuario pide agregar, modificar o regenerar un diagrama, cuando una figura sale pixelada/recortada, o cuando hay que renumerar figuras.
---

# Figuras y diagramas

## Pipeline

```
content/media/diagrams/diagrama-x.puml  →  java -jar plantuml.jar  →  content/media/figures/diagrama-x.png
                                                                      ↓
                                     ![Caption](../media/figures/diagrama-x.png) en content/manuscript/Documento_Tesis.md
```

Renderizado batch: [platform/scripts/build/build_diagrams.py](../../../platform/scripts/build/build_diagrams.py).
Compilación DOCX separada: [platform/scripts/build/build_thesis.py](../../../platform/scripts/build/build_thesis.py)
usa las imágenes ya renderizadas desde el Markdown.

Regla operativa: cuando una solicitud implique cambios de figura,
el flujo es siempre `editar .puml -> regenerar .png -> verificar/actualizar
embed en content/manuscript/Documento_Tesis.md`.

## Convenciones del `.puml`

```plantuml
@startuml
!theme plain
skinparam dpi 150
skinparam defaultFontName "Calibri"
scale max 1900 width

title <Título corto opcional>

' ... contenido ...

@enduml
```

**Reglas estrictas:**

- `!theme plain` (sin colores corporativos por defecto).
- `scale max 1900 width` **siempre**: imágenes con ancho > 2000 px revientan
  el flujo de chat al revisarlas y suelen exceder el ancho de página en
  Word.
- DPI 150 es el equilibrio nitidez/peso.
- Paleta pastel sobria; evitar rojos/verdes saturados (no se ven bien
  impresos en B/N).
- **Acentos**: PlantUML rompe acentos en algunos componentes (notas,
  títulos largos). Usar placeholders `{a1}{e1}{i1}{o1}{u1}{n1}{N1}` y
  reemplazarlos en `platform/scripts/build/build_diagrams.py`. Ver bloque `_accent()` en
  ese script.

## Embed en Markdown

```markdown

![<Título descriptivo de la figura>](../media/figures/diagrama-<slug>.png)

```

- Una **línea en blanco** antes y después.
- Caption en el alt-text (Pandoc lo usa como "title" de la figura).
- Sin `{width=...}` salvo que se necesite forzar tamaño; Pandoc usa el
  ancho real de la imagen y lo recorta al área de texto.

## Numeración y referencias en texto

- Número manual y consecutivo: el caption en el Markdown **no lleva**
  "Figura N." (lo añade el postproceso al insertarlo en el DOCX). Lo que
  va en el alt-text es solo el título.
- Toda figura debe referenciarse en texto con la forma explícita:
  `**La Figura N** <verbo>` (no "la siguiente figura", no "como se ve
  abajo").

Validación:

```powershell
Select-String -Path Documento_Tesis.md -Pattern "siguiente figura" -SimpleMatch
```

Cuando hay > 3 figuras sin referencia, escribir un script tipo
[platform/scripts/fixes/fix_referencias_v3.py](../../../platform/scripts/fixes/fix_referencias_v3.py) en
vez de editar a mano.

## Tipos de diagrama soportados

| Tipo | Cuándo |
|---|---|
| Diagrama de bloques / componentes | Arquitecturas, capas |
| Mapa mental | Marco conceptual, fundamentación teórica |
| Diagrama de flujo | Procesos metodológicos, fases |
| Diagrama de Gantt | Cronograma |
| Diagrama de clases | Modelo de datos / entidades del dominio |
| Diagrama de despliegue | Infraestructura |

Para el cronograma, PlantUML soporta `@startgantt`. Mantener nombres de
tareas cortos (≤ 40 caracteres) para que entren en el ancho de página.

## Anti-patrones

- Subir el PNG sin el `.puml` fuente: irreproducible.
- Usar capturas de pantalla de herramientas externas como "diagrama":
  pierden calidad y no se pueden editar.
- Diagramas con > 25 nodos: dividir en dos figuras.
- Olvidar `scale max 1900 width` y producir un PNG de 4000 px que no
  cabe en el área de texto.
- Editar el PNG a mano: la próxima regeneración lo sobrescribe.

## Lecciones aprendidas

- En chats con muchas imágenes, si algún PNG > 2000 px en alguna
  dimensión la solicitud falla con `many-image requests`. Por eso el
  `scale max 1900 width` es regla y no recomendación.
- Para revisar muchas figuras, hacerlo de una en una; no en lote.
