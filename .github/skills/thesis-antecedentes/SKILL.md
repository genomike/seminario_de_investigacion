---
name: thesis-antecedentes
description: Redactar o reformatear antecedentes (internacionales y nacionales) siguiendo el patrón de conectores en negrita exigido por el asesor. Usar siempre que el usuario pida agregar, reescribir o uniformar un antecedente, o cuando se detecte un antecedente que no respete el patrón.
---

# Patrón canónico de antecedentes

## Origen

Este patrón se construyó a partir de las observaciones del asesor (capturas en
[observaciones/](../../../content/observations/), particularmente
`marco_teorico.png`), que resaltó en colores los componentes obligatorios:
**porte**, **problema**, **objetivo**, **metodología**, **métricas**,
**resultados**, **limitaciones** y **vínculo con la tesis**.

## Plantilla obligatoria

Cada antecedente es **un solo bloque de 1 a 2 párrafos** con todos estos
conectores **en negrita** y en este orden:

```markdown
**APELLIDO[S] ET AL. (AÑO)** <verbo de aporte: proponen / desarrollan /
analizan / sistematizan / evalúan> <objeto del aporte>, <complemento breve>.
**En cuanto al porte,** <alcance del estudio: tipo, n, ámbito, revista en
*cursiva*>. **En ese marco,** el problema se centró en <enunciado del
problema reportado>. **A partir de ello,** el objetivo se orientó a <enunciado
del objetivo>.

**Para abordarlo, se empleó la siguiente metodología:** <diseño / técnicas
/ instrumentos>. **Para la evaluación,** <entorno y procedimiento>. **Como
métricas o indicadores de desempeño,** <lista de indicadores>. **En términos
de resultados,** <hallazgos cuantitativos cuando existan>. **No obstante,**
<limitaciones declaradas y/o trabajo futuro>. **En relación con esta tesis,**
<aporte específico al diseño, métricas o validación de la presente
investigación>.
```

## Reglas estrictas

1. **Apellido del primer autor en MAYÚSCULAS** seguido de `ET AL.` cuando
   son 3+ autores; si son 1 o 2, listarlos en MAYÚSCULAS unidos por `Y`.
   Ejemplo: `**ADELUSI ET AL. (2025)**`, `**MAURICIO Y PÉREZ (2024)**`.
2. **Año entre paréntesis**, sin coma antes.
3. Los **conectores van en negrita exactamente** como aparecen arriba
   (incluyendo la coma final cuando aplica). No traducirlos, no
   parafrasearlos, no quitarles la coma.
4. La **revista** o repositorio va en cursiva: `*JMIR Medical Informatics*`,
   `*Frontiers in Digital Health*`, `*Repositorio UNFV*`.
5. Cada antecedente debe **terminar con `**En relación con esta tesis,**`**.
   Sin esa frase, el asesor lo marca como incompleto.
6. Cuando una pieza no aplica (ej. estudio cualitativo sin métricas), **no
   omitir el conector**: usar `**Como métricas o indicadores de desempeño,**
   no se reportaron indicadores cuantitativos; el estudio prioriza
   categorías cualitativas X, Y y Z.`
7. **Una cita por antecedente**. Si se quiere combinar dos estudios, son
   dos antecedentes consecutivos, no un solo bloque.

## Variantes aceptadas de los conectores

Solo cuando el flujo lo exija; conservar la negrita y la coma:

| Slot | Variante alternativa permitida |
|---|---|
| `**Para abordarlo, se empleó la siguiente metodología:**` | `**Metodológicamente,**` (solo si el slot anterior ya describió método) |
| `**Para la evaluación,**` | `**Para la validación,**` |
| `**No obstante,**` | `**Entre las limitaciones,**` |
| `**En relación con esta tesis,**` | `**Su aporte a la presente investigación radica en**` |

## Cita en el texto

Al final del bloque (o de la cita textual interna), va la cita APA en
formato narrativo o parentético:

- Narrativo (preferido cuando el autor abre el bloque): el "(AÑO)" del
  encabezado **ya cuenta** como cita; añadir solo si hay paráfrasis directa
  con número de página.
- Parentético adicional cuando se cita una métrica concreta: `(Adelusi
  et al., 2025, p. 7)`.

## Ejemplo canónico (forma corta)

> **HERYAWAN ET AL. (2025)** caracterizan barreras reales de implementación
> FHIR en la plataforma nacional Satusehat de Indonesia, primer despliegue
> masivo de interoperabilidad basada en FHIR en el sudeste asiático. **En
> cuanto al porte,** el estudio abarca el primer análisis cualitativo a
> escala de ecosistema nacional de adopción FHIR en el sudeste asiático,
> con 107 incidencias documentadas en el *Developer Hub* de la plataforma
> Satusehat de Indonesia. **En ese marco,** el problema se centró en
> dificultades técnicas recurrentes en el uso de servidores, perfiles y
> mapeo semántico de datos durante la adopción nacional de FHIR. **A
> partir de ello,** el objetivo se orientó a identificar puntos críticos
> de adopción e integración para mejorar el despliegue interoperable
> nacional. **Para abordarlo,** se empleó la siguiente metodología:
> análisis de contenido cualitativo de interacciones del grupo Telegram
> del Developer Hub de Satusehat y de la documentación técnica oficial
> (*JMIR Formative Research*).
> ...
> **En relación con esta tesis,** … (cómo conecta con la presente
> investigación).

## Tabla comparativa al final de cada bloque

Después del último antecedente (internacional / nacional), incluir
una **tabla síntesis** con columnas estándar: `Autor (Año)`, `Porte`,
`Problema`, `Objetivo`, `Metodología`, `Resultados`, `Aporte a la tesis`.
Ver `thesis-tablas-apa` para el formato.

## Síntesis crítica

Cerrar la sección de antecedentes con una **subsección 2.1.3. Síntesis
crítica** que:

- Identifica el patrón común (tendencias / consensos).
- Identifica el vacío (lo que esta tesis cubre y nadie más).
- Conecta con los objetivos específicos del Cap. I.

## Operacionalización del patrón

Cuando hay que aplicar el patrón a varios antecedentes ya escritos sin él,
**no editar a mano**: escribir un script de fix idempotente
(ver `thesis-scripts-fix`) imitando
[platform/scripts/fixes/add_porte_conectores.py](../../../platform/scripts/fixes/add_porte_conectores.py).
Ese script:

1. Define una lista de tuplas `(fragmento_único_antes_del_split,
   descripción_porte, log_id)`.
2. Inserta `**En cuanto al porte,** <descripción>. ` justo antes del
   conector `**En ese marco,**`.
3. Reporta cada reemplazo y aborta si no encuentra el ancla (no usa
   reemplazo aproximado).

## Anti-patrones

- Conectores **sin negrita** o **sin la coma**: el asesor los marca.
- Apellido en minúsculas o sin `ET AL.`.
- Mezclar dos estudios en el mismo bloque ("Adelusi et al. (2025) y
  Heryawan et al. (2025) coinciden en…").
- Saltarse `**En cuanto al porte,**` o `**En relación con esta tesis,**`.
- Bullets dentro del antecedente: debe ser prosa.
