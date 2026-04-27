---
name: thesis-dominio-template
description: Plantilla para crear un skill de dominio de una tesis nueva. Usar al iniciar un fork o al cambiar de tema para definir vocabulario, marco normativo, teorias, variables, indicadores, fuentes y anti-patrones del nuevo campo sin contaminar los skills genericos.
---

# Plantilla de skill de dominio

Este skill es un **molde**. No describe un tema real. Al iniciar una tesis
nueva, copia esta carpeta como `thesis-dominio-<tema>` y reemplaza todos los
placeholders por conocimiento del dominio elegido.

Los skills genericos deben permanecer agnosticos. Todo vocabulario, norma,
institucion, tecnologia, corriente teorica o base de datos especializada vive
solo en el skill de dominio del fork.

## Ficha del dominio

| Campo | Contenido a completar |
|---|---|
| Tema de tesis | `<tema exacto>` |
| Area / programa | `<area academica>` |
| Objeto de estudio | `<fenomeno, proceso, poblacion, sistema o institucion>` |
| Unidad de analisis | `<persona, documento, expediente, organizacion, sistema, caso, etc.>` |
| Alcance geografico | `<pais, region, ciudad, institucion o entorno>` |
| Horizonte temporal | `<periodo de analisis>` |

## Vocabulario controlado

Completar una tabla con terminos que deben usarse de forma consistente.

| Termino / sigla | Definicion operativa | Uso recomendado |
|---|---|---|
| `<termino>` | `<definicion breve>` | `<forma preferida en la tesis>` |

Reglas:

- Definir siglas en la primera mencion.
- Mantener una sola traduccion o equivalencia para terminos tecnicos.
- Registrar sinonimos que deben evitarse si generan ambiguedad.

## Marco teorico sugerido

Identificar teorias, modelos, enfoques o escuelas pertinentes.

| Enfoque | Autor base | Para que sirve en la tesis |
|---|---|---|
| `<teoria o modelo>` | `<autor, ano>` | `<relacion con variables/categorias>` |

## Marco normativo o institucional

Usar solo si el tema lo requiere. Puede incluir leyes, reglamentos, politicas,
protocolos, estandares tecnicos, lineamientos institucionales o acuerdos.

| Tipo | Documento | Relevancia |
|---|---|---|
| `<ley / norma / politica / estandar>` | `<nombre y ano>` | `<por que afecta al problema>` |

## Variables, categorias e indicadores

Para tesis cuantitativas, completar variables e indicadores. Para cualitativas,
usar categorias/subcategorias y evidencias esperadas.

| Elemento | Definicion operativa | Indicador / evidencia | Fuente de datos |
|---|---|---|---|
| `<variable o categoria>` | `<definicion>` | `<indicador o evidencia>` | `<instrumento / fuente>` |

## Fuentes prioritarias del dominio

Listar bases de datos, repositorios, portales normativos o colecciones
especializadas. No duplicar reglas genericas de `thesis-fuentes`; aqui solo va
lo particular del campo.

| Fuente | Tipo de material | Criterio de uso |
|---|---|---|
| `<base o portal>` | `<articulos / tesis / normas / datasets>` | `<cuando usarla>` |

## Antecedentes modelo

Registrar 3-5 autores o estudios semilla una vez que el tema este definido.
Cada entrada debe indicar por que sirve a la tesis, no solo su titulo.

| Autor (ano) | Aporte | Posible uso en la tesis |
|---|---|---|
| `<autor>` | `<aporte principal>` | `<antecedente / teoria / metodo / indicador>` |

## Diagramas utiles para este dominio

Proponer diagramas conceptuales, metodologicos o de proceso que ayuden al
lector. Los archivos concretos deben vivir en `content/media/diagrams/`.

| Diagrama | Proposito | Seccion sugerida |
|---|---|---|
| `<nombre conceptual>` | `<que aclara>` | `<capitulo/seccion>` |

## Anti-patrones del dominio

- Confundir `<concepto A>` con `<concepto B>`.
- Usar afirmaciones normativas sin fuente.
- Mezclar niveles de analisis incompatibles.
- Generalizar hallazgos fuera del alcance declarado.

## Checklist antes de redactar

- [ ] Tema, problema y objetivos usan el mismo vocabulario.
- [ ] Las variables/categorias se pueden observar o medir.
- [ ] Las fuentes prioritarias son accesibles.
- [ ] Las normas o documentos institucionales estan vigentes.
- [ ] Las limitaciones del dominio estan declaradas.