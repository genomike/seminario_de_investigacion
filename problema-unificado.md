# Problema unificado de investigación

## Título propuesto

Deficiencias en la interoperabilidad y en la gestión de historias clínicas de pacientes SIS en centros de salud del MINSA.

## Resumen ejecutivo

El problema de investigación integra dos niveles: un nivel estructural (interoperabilidad de sistemas de información en salud) y un nivel operativo (gestión real de la historia clínica de pacientes SIS en centros MINSA). Aunque el Perú cuenta con un marco normativo que define arquitectura, reglas técnicas y catálogos estandarizados, persiste una brecha entre norma y ejecución. Esta brecha se manifiesta en historias clínicas fragmentadas, duplicidad de registros y exámenes, demoras en validación administrativa, riesgos de error clínico y sobrecostos para el sistema.

## Formulación integrada del problema

Los centros de salud del MINSA presentan deficiencias en la interoperabilidad de sus sistemas de información y en la gestión de historias clínicas de pacientes afiliados al SIS, pese a la existencia del marco normativo RM N° 1104-2018-MINSA, RM N° 464-2019-MINSA y RM N° 1193-2019-MINSA. La persistencia de sistemas heredados, la implementación parcial de estándares de comunicación e integración (HL7, DICOM), el uso inconsistente de codificación clínica (CIE-10, CPMS), las brechas de conexión a PIDESALUD, las debilidades de gobernanza y normalización de datos (IEDS), y las limitaciones de infraestructura, talento y presupuesto ocasionan fragmentación y pérdida de información clínica, duplicidad de registros y exámenes, demoras asistenciales, dificultades en la validación administrativa y facturación SIS, mayor riesgo de errores médicos e insatisfacción del paciente.

## Pregunta general de investigación

¿En qué medida el nivel de cumplimiento de las exigencias técnicas y organizativas establecidas por las RM N° 1104-2018-MINSA, N° 464-2019-MINSA y N° 1193-2019-MINSA influye en la integridad, disponibilidad y continuidad de la historia clínica electrónica de pacientes SIS en los centros de salud del MINSA?

## Preguntas específicas sugeridas

1. ¿Cuál es el nivel de adopción operativa de la arquitectura RNIEDS-PIDESALUD en IPRESS del ámbito SIS-MINSA?
2. ¿Qué grado de cumplimiento existe en el uso de estándares de intercambio (HL7, DICOM) y codificación (CIE-10, CPMS)?
3. ¿Qué brechas de calidad de dato (identidad de paciente, códigos de establecimiento, medicamentos y procedimientos) afectan la continuidad de atención?
4. ¿Cómo impactan las brechas de interoperabilidad en tiempos de atención, duplicidad de exámenes y validación administrativa SIS?
5. ¿Qué factores organizacionales y presupuestales explican el incumplimiento parcial en establecimientos periféricos?

## Objetivo general

Evaluar el nivel de cumplimiento normativo y técnico de interoperabilidad en centros de salud del MINSA y su efecto en la gestión de historias clínicas de pacientes SIS.

## Objetivos específicos sugeridos

1. Identificar el grado de implementación de componentes de interoperabilidad (RNIEDS, PIDESALUD) en establecimientos seleccionados.
2. Medir el cumplimiento de estándares de comunicación y codificación clínica exigidos por la normativa.
3. Analizar la calidad semántica del dato mediante catálogos IEDS críticos.
4. Estimar el efecto de las brechas técnicas sobre continuidad asistencial, eficiencia operativa y riesgo clínico-administrativo.
5. Proponer lineamientos de mejora priorizados para cerrar la brecha entre norma y práctica.

## Hipótesis de trabajo

Un mayor cumplimiento de los componentes normativos y técnicos de interoperabilidad definidos en las RM N° 1104-2018-MINSA, N° 464-2019-MINSA y N° 1193-2019-MINSA se asocia con una mejora significativa en la gestión de historias clínicas de pacientes SIS, expresada en mayor continuidad asistencial, menor duplicidad de procedimientos y menor riesgo de errores clínico-administrativos.

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

## Variables y operacionalización inicial

### Variable independiente

Nivel de cumplimiento normativo y técnico de interoperabilidad.

### Dimensiones de la variable independiente

1. Implementación de arquitectura RNIEDS-PIDESALUD.
2. Cumplimiento de estándares de intercambio (HL7, DICOM).
3. Cumplimiento de codificación y catálogos IEDS (CIE-10, CPMS, RENAES, DIGEMID, identidad paciente).
4. Seguridad, privacidad y trazabilidad de acceso/uso de datos.

### Variable dependiente

Calidad de gestión de historia clínica de pacientes SIS-MINSA.

### Indicadores sugeridos

- Porcentaje de establecimientos con conexión operativa a PIDESALUD.
- Porcentaje de transacciones validadas bajo estándar de intercambio definido.
- Porcentaje de diagnósticos correctamente codificados en CIE-10.
- Porcentaje de procedimientos correctamente codificados en CPMS.
- Tasa de duplicidad de pacientes y exámenes por cada 1000 atenciones.
- Tiempo promedio de validación administrativa SIS.
- Porcentaje de registros con trazabilidad completa de acceso y modificación.

## Diseño metodológico sugerido para tesis

### Enfoque

Mixto (cuantitativo + cualitativo) con predominio explicativo.

### Tipo de estudio

- Aplicado, no experimental, transversal.
- Alcance correlacional-explicativo.

### Unidades de análisis

- Establecimientos de salud MINSA del ambito SIS.
- Procesos de registro, codificación, intercambio y validación administrativa.

### Técnicas e instrumentos

- Revisión documental normativa y técnica.
- Lista de chequeo de cumplimiento (ver archivo de checklist).
- Auditoria de registros clínico-administrativos.
- Entrevistas semiestructuradas a responsables TI, estadística y jefaturas asistenciales.

### Estrategia de análisis

- Indice compuesto de cumplimiento de interoperabilidad.
- Análisis de asociación entre cumplimiento y resultados operativos.
- Priorización de brechas con matriz impacto-probabilidad.

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

## Estructura sugerida de capítulo de tesis

1. Problema y contexto de interoperabilidad en salud.
2. Marco normativo y técnico nacional (RM 1104, 464, 1193).
3. Marco internacional de estandarización (HL7, DICOM, clasificaciones OMS).
4. Brecha norma-practica en IPRESS del ambito SIS-MINSA.
5. Modelo de variables e indicadores.
6. Resultados, brechas priorizadas y propuesta de mejora.

## Lógica de la fusión (trazabilidad conceptual)

- Problema macro original: limitaciones de interoperabilidad de sistemas de salud.
- Problema aplicado original: deficiencias de gestión de historias clínicas SIS-MINSA.
- Problema unificado: brecha de cumplimiento e implementación de interoperabilidad que impacta la continuidad clínica y la eficiencia administrativa.

## Próxima ampliación recomendada

Para una versión final de grado tesis, el siguiente bloque a construir es una matriz de operacionalización completa con escala de medición, fuente de verificación por indicador y ficha de instrumento para trabajo de campo.