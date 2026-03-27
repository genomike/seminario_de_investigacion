# Problema unificado de investigación

## Título propuesto

Modelo híbrido de diagnóstico e implementación de interoperabilidad basado en HL7 FHIR para la mejora de la gestión de historias clínicas de pacientes que tienen SIS en centros de salud MINSA en Lima.

## Resumen ejecutivo

Esta investigación adopta un **enfoque híbrido de tres fases** (diagnóstico → implementación → evaluación) para abordar las deficiencias de interoperabilidad en centros de salud MINSA del ámbito SIS en Lima. Aunque el Perú cuenta con un marco normativo que define arquitectura (RNIEDS/PIDESALUD), estándares de intercambio (HL7, DICOM), codificación (CIE-10, CPMS) y catálogos IEDS, persiste una brecha entre norma y ejecución que se manifiesta en historias clínicas fragmentadas, duplicidad de registros y exámenes, demoras en validación administrativa y riesgos de error clínico.

El modelo híbrido supera las limitaciones de un enfoque puramente diagnóstico (que describe la brecha pero no la cierra) o puramente implementador (que carece de línea base para medir impacto). Al integrar ambos, la investigación: (1) diagnostica las brechas reales de interoperabilidad, (2) diseña e implementa una capa piloto de integración HL7 FHIR que atiende las brechas críticas, y (3) evalúa cuantitativamente el impacto pre/post en la calidad de gestión de historias clínicas.

## Formulación integrada del problema

Los centros de salud del MINSA presentan deficiencias en la interoperabilidad de sus sistemas de información y en la gestión de historias clínicas de pacientes afiliados al SIS, pese a la existencia del marco normativo RM N° 1104-2018-MINSA, RM N° 464-2019-MINSA y RM N° 1193-2019-MINSA. La persistencia de sistemas heredados, la implementación parcial de estándares de comunicación e integración (HL7, DICOM), el uso inconsistente de codificación clínica (CIE-10, CPMS), las brechas de conexión a PIDESALUD, las debilidades de gobernanza y normalización de datos (IEDS), y las limitaciones de infraestructura, talento y presupuesto ocasionan fragmentación y pérdida de información clínica, duplicidad de registros y exámenes, demoras asistenciales, dificultades en la validación administrativa y facturación SIS, mayor riesgo de errores médicos e insatisfacción del paciente.

Ante esta situación, se requiere un modelo híbrido que no solo diagnostique las brechas existentes, sino que proponga e implemente una solución tecnológica concreta — una capa de integración basada en HL7 FHIR — y mida su efecto real en la calidad de gestión de las historias clínicas, generando evidencia para su escalamiento a nivel sectorial.

## Pregunta general de investigación

¿De qué manera un modelo híbrido que integre el diagnóstico de brechas de interoperabilidad y la implementación piloto de una capa de integración basada en HL7 FHIR permitirá mejorar la gestión de historias clínicas de pacientes SIS en centros de salud del MINSA en Lima?

## Preguntas específicas de investigación

1. **Fase diagnóstica:** ¿Cuál es el nivel actual de cumplimiento de los estándares de interoperabilidad (RNIEDS, PIDESALUD, HL7, CIE-10, CPMS) en centros de salud MINSA del ámbito SIS en Lima y qué brechas críticas existen en la gestión de historias clínicas?
2. **Fase de implementación:** ¿Cómo diseñar e implementar una capa de integración basada en HL7 FHIR que atienda las brechas de interoperabilidad identificadas en el diagnóstico?
3. **Fase de evaluación:** ¿En qué medida la implementación piloto de la capa de integración FHIR mejora la integridad, continuidad y calidad de las historias clínicas de pacientes SIS respecto a la línea base diagnóstica?

## Objetivo general

Mejorar la gestión de historias clínicas de pacientes SIS en centros de salud MINSA en Lima mediante un modelo híbrido que diagnostique las brechas de interoperabilidad e implemente una capa piloto de integración basada en HL7 FHIR.

## Objetivos específicos

1. **OE1 (Diagnóstico):** Determinar el nivel de cumplimiento de los estándares de interoperabilidad (RNIEDS, PIDESALUD, HL7, CIE-10, CPMS) y levantar una línea base de calidad de gestión de HCE en los establecimientos seleccionados.
2. **OE2 (Implementación):** Diseñar e implementar una capa piloto de integración basada en HL7 FHIR que atienda las brechas críticas identificadas en el diagnóstico.
3. **OE3 (Evaluación):** Evaluar el impacto de la implementación piloto comparando los indicadores de calidad de gestión de HCE antes y después de la intervención.
4. **OE4 (Escalabilidad):** Formular lineamientos y lecciones aprendidas para el escalamiento del modelo a otros establecimientos MINSA.

## Hipótesis de trabajo

**Hipótesis general:** La implementación piloto de una capa de integración basada en HL7 FHIR, diseñada a partir del diagnóstico de brechas de interoperabilidad, mejora significativamente la calidad de gestión de historias clínicas de pacientes SIS en centros de salud MINSA en Lima.

**Hipótesis específicas:**

1. **H1:** Los centros de salud MINSA del ámbito SIS en Lima presentan un nivel de cumplimiento inferior al 50 % en al menos tres de las cinco dimensiones de interoperabilidad evaluadas.
2. **H2:** La capa de integración FHIR piloto es técnicamente viable de implementar con los recursos disponibles en establecimientos MINSA de nivel I y II.
3. **H3:** Después de la implementación piloto, los indicadores de completitud, codificación correcta y continuidad de atención de las HCE mejoran en al menos un 20 % respecto a la línea base.

## Base normativa nacional consolidada

### Resolución Ministerial N° 1104-2018-MINSA

- Rol: crea la infraestructura base de interoperabilidad sectorial.
- Componentes clave: RNIEDS y PIDESALUD.
- Contribución al problema: define el soporte estructural para intercambio de datos y consulta de catálogos estándar.

### Resolución Ministerial N° 464-2019-MINSA

- Rol: regula la interoperabilidad en sistemas de información asistenciales.
- Instrumento técnico: Directiva Administrativa N° 266-MINSA/2019/OGTI.
- Alcance: entidades públicas y privadas vinculadas al sistema de salud, según la directiva.
- Contribución al problema: convierte los requisitos técnicos y de proceso en obligaciones de implementación.

### Resolución Ministerial N° 1193-2019-MINSA

- Rol: aprueba catálogos IEDS para estandarización semántica.
- Componentes críticos: identificación de persona, establecimiento, procedimientos y medicamentos.
- Contribución al problema: reduce ambiguedad semántica, error de codificación y no comparabilidad de datos.

## Arquitectura funcional del modelo normativo

### RNIEDS (repositorio maestro semántico)

- Función: repositorio de identificaciones estándar para uniformizar vocabulario clínico-administrativo.
- Resultado esperado: consistencia semántica en captura, transmisión y consumo de datos.

### PIDESALUD (plataforma de intercambio)

- Función: habilitar interoperabilidad entre instituciones mediante servicios de intercambio/consulta.
- Resultado esperado: circulación oportuna y segura de información clínica relevante.

### Relación operativa entre componentes

- RNIEDS aporta el contenido estandarizado (catálogos, identificadores).
- PIDESALUD aporta el mecanismo de intercambio entre sistemas heterogéneos.
- La combinación de ambos habilita continuidad de atención y trazabilidad clínica-administrativa.

## Niveles de interoperabilidad y su traducción operativa

### Interoperabilidad organizativa

- Alineación de procesos asistenciales y administrativos entre instituciones.
- Necesidad de gobernanza, roles claros y acuerdos de intercambio.

### Interoperabilidad de comunicación

- Uso de estándares de intercambio de información clínica.
- Estándares mencionados en el marco trabajado: HL7 para mensajería y DICOM para imágenes.

### Interoperabilidad semántica (codificación)

- Uso de catálogos y codificaciones para que el significado del dato se conserve entre sistemas.
- Elementos centrales: CIE-10 para diagnósticos y CPMS para procedimientos.

### Interoperabilidad de proceso y seguridad

- Reglas de acceso, privacidad, trazabilidad y control de tratamiento de datos personales.
- Vinculación con normativa nacional de protección de datos y seguridad de la información.

### Interoperabilidad de dispositivo

- Condiciones tecnológicas de captura en punto de atención (equipos, conectividad, periféricos).
- Implica capacidad real de registrar datos completos y oportunos en campo.

## Catálogos IEDS críticos para historia clínica SIS-MINSA

### Identificación de paciente

- Claves: DNI o Carnet de Extranjeria.
- Integraciones esperadas: validación con fuentes oficiales (RENIEC/Migraciones).
- Riesgo de no cumplimiento: duplicidad de identidad y errores en continuidad clínica.

### Identificación de establecimiento

- Clave: código de establecimiento (RENAES).
- Riesgo de no cumplimiento: trazabilidad institucional débil y problemas de referencia/contrarreferencia.

### Procedimientos médicos

- Clave: codificación CPMS.
- Riesgo de no cumplimiento: inconsistencia de registro y observaciones en procesos SIS.

### Medicamentos

- Clave: códigos alineados al marco de DIGEMID.
- Riesgo de no cumplimiento: errores de prescripción, dispensación y seguimiento farmacoterapéutico.

## Actores y responsabilidades esperadas

### MINSA (OGTI)

- Conducción técnica de interoperabilidad.
- Definición de lineamientos, catálogos y coordinación sectorial.

### SUSALUD

- Rol de supervisión y protección de derechos en salud.
- Relevancia para el estudio: componente de vigilancia de cumplimiento y efectos en derechos del paciente.

### IPRESS y UGIPRESS

- Implementación efectiva de estándares, catálogos y seguridad del dato.
- Punto crítico de estudio: distancia entre obligación normativa y capacidad operativa local.

## Causa-efecto del problema unificado

### Causas estructurales

- Sistemas heredados con baja capacidad de integración.
- Implementación parcial de HL7/DICOM.
- Uso inconsistente de CIE-10/CPMS/IEDS.
- Brechas de conectividad para operación sostenida.
- Insuficiente gobernanza y control de calidad de datos.
- Capacitación insuficiente y alta rotación de personal.
- Restricciones presupuestales para modernización.

### Efectos en la operación SIS-MINSA

- Fragmentación de historia clínica.
- Duplicidad de exámenes y procedimientos.
- Demoras en diagnóstico, tratamiento y validación administrativa.
- Riesgo de errores médicos por información incompleta.
- Sobrecostos por ineficiencia y baja trazabilidad.
- Insatisfacción del paciente y potencial afectación de derechos en salud.

## Variables y operacionalización

### Variable independiente

Modelo híbrido de interoperabilidad (diagnóstico + implementación FHIR).

### Dimensiones de la variable independiente

#### Fase 1 — Diagnóstico

| Dimensión | Indicador | Escala | Instrumento |
|---|---|---|---|
| Arquitectura RNIEDS-PIDESALUD | % de componentes implementados operativamente | Razón (0-100 %) | Checklist normativo |
| Estándares de intercambio | Nivel de adopción de HL7/FHIR y DICOM | Ordinal (nulo/parcial/completo) | Ficha técnica |
| Codificación clínica | % cumplimiento CIE-10, CPMS, catálogos IEDS | Razón (0-100 %) | Auditoría de registros |
| Seguridad y trazabilidad | Existencia de políticas y logs de acceso | Nominal (sí/no) + ordinal | Revisión documental |
| Infraestructura y conectividad | Disponibilidad de conexión operativa | Nominal (sí/no) + razón (% uptime) | Monitoreo técnico |

#### Fase 2 — Implementación piloto

| Componente | Indicador | Escala | Instrumento |
|---|---|---|---|
| Perfiles FHIR definidos | Número de recursos FHIR mapeados | Razón | Documentación técnica |
| Mapeo de datos | % de campos locales mapeados a FHIR | Razón (0-100 %) | Matriz de mapeo |
| Servicio desplegado | Disponibilidad del endpoint FHIR | Nominal (operativo/no operativo) | Pruebas de integración |
| Capacitación | % de personal capacitado | Razón (0-100 %) | Registro de asistencia |

#### Fase 3 — Evaluación de impacto

- Comparación pre/post de todos los indicadores de la variable dependiente.

### Variable dependiente

Calidad de gestión de historias clínicas de pacientes SIS.

### Indicadores de la variable dependiente (medidos pre y post implementación)

| Indicador | Fórmula / operacionalización | Escala | Fuente |
|---|---|---|---|
| Completitud de HCE | % de campos obligatorios completos | Razón (0-100 %) | Auditoría de registros |
| Codificación CIE-10 | % de diagnósticos correctamente codificados | Razón (0-100 %) | Muestra de atenciones |
| Codificación CPMS | % de procedimientos correctamente codificados | Razón (0-100 %) | Muestra de atenciones |
| Duplicidad de pacientes | Tasa de duplicados por cada 1 000 atenciones | Razón | Base de datos HIS |
| Duplicidad de exámenes | Tasa de exámenes duplicados por cada 1 000 atenciones | Razón | Base de datos HIS |
| Tiempo de validación SIS | Tiempo promedio en horas | Razón | Registros SIS |
| Continuidad de atención | % de HCE con trazabilidad entre establecimientos | Razón (0-100 %) | Cruce de registros |
| Trazabilidad de accesos | % de registros con log completo | Razón (0-100 %) | Logs del sistema |

## Diseño metodológico

### Enfoque

Mixto (cuantitativo predominante + cualitativo complementario).

### Tipo de estudio

- **Aplicado:** propone e implementa una solución concreta (capa FHIR).
- **Pre-experimental o cuasi-experimental:** diseño pre-test / post-test (con grupo único o con grupo control si la muestra lo permite).
- **Alcance:** explicativo-propositivo.

### Fases del diseño

| Fase | Actividad | Técnica / instrumento | Producto |
|---|---|---|---|
| 1. Diagnóstico | Evaluar cumplimiento normativo-técnico | Checklist (RM 1104, 464, 1193), auditoría de registros, entrevistas | Línea base + mapa de brechas |
| 2. Implementación | Diseñar y desplegar capa FHIR piloto | Diseño de perfiles FHIR, mapeo de datos, despliegue, capacitación | Servicio piloto operativo |
| 3. Evaluación | Medir indicadores post y comparar con línea base | Auditoría post, prueba estadística pareada (Wilcoxon / t-test) | Evidencia de impacto |

### Unidades de análisis

- Establecimientos de salud MINSA del ámbito SIS en Lima (mínimo 2-3 niveles de complejidad).
- Historias clínicas electrónicas (muestra de registros por establecimiento).
- Procesos de registro, codificación, intercambio y validación administrativa.

### Técnicas e instrumentos

- Revisión documental normativa y técnica.
- Lista de chequeo de cumplimiento de interoperabilidad (ver archivo de checklist).
- Auditoría de registros clínico-administrativos (pre y post).
- Entrevistas semiestructuradas a responsables TI, estadística y jefaturas asistenciales.
- Pruebas de integración técnica (validación de endpoints FHIR).

### Estrategia de análisis

- Índice compuesto de cumplimiento de interoperabilidad (Fase 1).
- Prueba de diferencias pareadas (Wilcoxon o t-test según normalidad) para comparar indicadores pre/post (Fase 3).
- Análisis cualitativo de lecciones aprendidas y barreras de implementación.
- Priorización de brechas con matriz impacto-viabilidad.

## Brechas críticas observadas hasta ahora

1. Cumplimiento formal de la norma, pero ejecución técnica desigual entre establecimientos.
2. Integración parcial a plataformas y catálogos en sedes con limitaciones de conectividad.
3. Dependencia de procesos manuales para conciliación de datos clínicos y administrativos.
4. Débil trazabilidad de cambios en el dato clínico y baja madurez de auditoría.
5. Diferencias de capacidad técnica entre nivel central y periferia operativa.

## Hallazgos de investigación web incorporables al marco teórico

### HL7 (fuente institucional)

- HL7 International se define como organización acreditada ANSI para estándares de intercambio e integración de información de salud.
- Relevancia para la tesis: respalda el fundamento técnico de interoperabilidad por estándares abiertos y perfiles de implementación.

### DICOM (fuente institucional)

- DICOM es el estándar internacional para imágenes médicas y su información asociada.
- Es reconocido por ISO como ISO 12052.
- Relevancia para la tesis: sustenta interoperabilidad de imágenes diagnósticas y continuidad de información radiológica.

### Clasificación internacional de enfermedades (OMS)

- La OMS define ICD como base global para comparabilidad de morbilidad y mortalidad.
- ICD-11 esta oficialmente en vigor desde 2022 a nivel OMS.
- Relevancia para la tesis: refuerza la importancia de codificación estandarizada para calidad de dato, comparabilidad y gestión sanitaria.

## Estado de validación de fuentes normativas en línea

- El detalle normativo principal de las RM 1104-2018, 464-2019 y 1193-2019 ya fue incorporado desde tu extracción documental previa.
- La consulta web automatizada a enlaces de gob.pe devolvió contenido cruzado en algunos casos, por lo que las URL finales de cada resolución deben confirmarse manualmente desde el buscador oficial de MINSA o El Peruano.
- Esta nota se incluye para mantener trazabilidad metodológica y evitar citas incorrectas.

## Supuestos y delimitaciones

- Se asume que la muestra de establecimientos representa variabilidad territorial (urbano/periférico).
- Se delimita el análisis al proceso de historia clínica y su vínculo operativo con el SIS.
- No se evalúa todo el ecosistema nacional de salud digital, solo el segmento pertinente al problema.

## Riesgos metodológicos y mitigación

1. Riesgo de subregistro en fuentes internas.
   Mitigación: triangulación entre registros, entrevistas y evidencia de sistema.
2. Riesgo de sesgo por autoevaluación institucional.
   Mitigación: aplicar verificación documental y prueba de casos trazadores.
3. Riesgo de baja disponibilidad de logs históricos.
   Mitigación: usar periodo de observación acotado y trazas disponibles.

## Estructura sugerida de capítulos de tesis

1. **Planteamiento del problema** — contexto, formulación, preguntas, objetivos, hipótesis, justificación.
2. **Marco teórico y normativo** — interoperabilidad en salud, estándares (HL7/FHIR, DICOM, CIE-10), marco normativo peruano (RM 1104, 464, 1193), antecedentes internacionales y nacionales.
3. **Metodología** — diseño pre-experimental, población/muestra, operacionalización de variables, instrumentos, procedimiento por fases.
4. **Fase 1: Diagnóstico** — resultados del levantamiento de línea base, mapa de brechas, priorización.
5. **Fase 2: Implementación piloto** — diseño de la capa FHIR, arquitectura, mapeo de datos, despliegue, capacitación.
6. **Fase 3: Evaluación de impacto** — comparación pre/post, pruebas estadísticas, análisis de resultados.
7. **Discusión** — contraste con antecedentes, implicancias, limitaciones.
8. **Conclusiones y recomendaciones** — hallazgos principales, lineamientos de escalabilidad, trabajo futuro.

## Lógica de la fusión (trazabilidad conceptual)

- **Problema macro original:** limitaciones de interoperabilidad de sistemas de salud.
- **Problema aplicado original:** deficiencias de gestión de historias clínicas SIS-MINSA.
- **Problema unificado:** brecha de cumplimiento e implementación de interoperabilidad que impacta la continuidad clínica y la eficiencia administrativa.
- **Enfoque híbrido (evolución):** el diagnóstico identifica las brechas, la implementación FHIR las atiende, y la evaluación pre/post genera evidencia de mejora. Esto supera el enfoque diagnóstico-predictivo anterior (que solo estimaba riesgo de fragmentación sin cerrar la brecha).

## Siguientes pasos - ejecución

1. **Selección de establecimientos:** definir la muestra de IPRESS en Lima (mínimo 2-3 niveles de complejidad).
2. **Validación de instrumentos:** someter el checklist diagnóstico y la ficha de auditoría a juicio de expertos.
3. **Ejecución del diagnóstico (Fase 1):** levantar línea base en los establecimientos seleccionados.
4. **Diseño FHIR (Fase 2):** definir perfiles de recursos, terminologías y arquitectura del servicio piloto.
5. **Implementación y capacitación (Fase 2):** desplegar la capa piloto y formar al personal operativo.
6. **Medición post y análisis (Fase 3):** recoger indicadores post-implementación y ejecutar pruebas estadísticas.
7. **Redacción de tesis:** escribir capítulos con base en los resultados obtenidos.