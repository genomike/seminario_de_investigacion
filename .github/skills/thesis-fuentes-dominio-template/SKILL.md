---
name: thesis-fuentes-dominio-template
description: Plantilla para crear un skill de fuentes especializadas por dominio. Usar cuando una tesis nueva requiere portales, bases de datos, repositorios, normativa o literatura gris que no estan cubiertos por el skill generico thesis-fuentes.
---

# Plantilla de fuentes especializadas por dominio

Este skill es un **molde**. Copialo como `thesis-fuentes-<dominio>` cuando el
tema exija fuentes especializadas. No debe contener ejemplos reales hasta que
exista un dominio definido en el fork.

## Jerarquia de fuentes

Ordenar las fuentes del campo segun su fuerza academica o normativa.

| Prioridad | Tipo de fuente | Criterio de aceptacion |
|---|---|---|
| 1 | `<fuente primaria / indexada / oficial>` | `<criterio>` |
| 2 | `<fuente secundaria especializada>` | `<criterio>` |
| 3 | `<literatura gris o repositorio>` | `<criterio>` |

## Bases y portales recomendados

| Recurso | URL base | Que buscar | Observaciones |
|---|---|---|---|
| `<nombre>` | `<url>` | `<tipo de documento>` | `<restricciones>` |

## Query matrix

Construir combinaciones de busqueda antes de descargar documentos.

| Bloque | Terminos principales | Sinonimos / equivalentes |
|---|---|---|
| Tema | `<termino 1>` | `<sinonimos>` |
| Poblacion / unidad | `<termino 2>` | `<sinonimos>` |
| Contexto | `<termino 3>` | `<sinonimos>` |
| Metodo / variable | `<termino 4>` | `<sinonimos>` |

## Criterios de inclusion

- Rango temporal: `<anos>`.
- Idiomas: `<idiomas>`.
- Tipo de documento: `<articulos, tesis, normas, reportes, datasets>`.
- Calidad minima: `<indexacion, revision por pares, fuente oficial, etc.>`.
- Pertinencia directa con problema, objetivos o variables/categorias.

## Criterios de exclusion

- Documentos sin autor o institucion verificable.
- Fuentes sin fecha cuando la vigencia sea importante.
- Material divulgativo sin respaldo metodologico, salvo que se use como
  contexto no academico.
- Duplicados o versiones no oficiales cuando exista version primaria.

## Catalogacion local

Guardar fuentes en:

```
content/sources/international/
content/sources/national/
```

Formato sugerido de nombre:

```
NN_ApellidoAutor_Ano_TituloCorto.pdf
NN_ApellidoAutor_Ano_TituloCorto.txt
```

## Ficha minima por fuente

| Campo | Valor |
|---|---|
| Referencia APA preliminar | `<referencia>` |
| DOI / URL / identificador | `<enlace>` |
| Tipo de fuente | `<tipo>` |
| Aporte al tema | `<aporte>` |
| Uso probable | `<antecedente / teoria / metodo / normativa>` |
| Limitaciones | `<limitacion>` |

## Validaciones

- Verificar que los PDFs abren y corresponden al titulo registrado.
- Confirmar DOI/URL y fecha de acceso cuando aplique.
- Separar fuentes academicas, normativas y tecnicas si el dominio lo exige.
- No descargar material masivo sin catalogarlo: fuente no catalogada se pierde.