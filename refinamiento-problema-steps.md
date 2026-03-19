# Refinamiento del problema: paso a paso

## Problema base

Deficiencias en la interoperabilidad y en la gestión de historias clínicas de pacientes SIS en centros de salud del MINSA.

## Paso 1. Definición de palabras clave

### Palabras clave núcleo (español)

- interoperabilidad en salud
- historia clínica electrónica
- sistemas de información asistenciales
- SIS
- MINSA
- RNIEDS
- PIDESALUD
- IEDS
- CIE-10
- CPMS
- calidad de dato clínico
- continuidad de atención

### Palabras clave equivalentes (inglés)

- health information interoperability
- electronic health record interoperability
- EHR interoperability
- HL7 FHIR
- DICOM
- semantic interoperability
- health information exchange (HIE)
- patient record continuity
- clinical coding quality
- health data standards

### Combinaciones sugeridas para búsqueda

1. "health information interoperability" AND "electronic health record" AND (HL7 OR FHIR)
2. "semantic interoperability" AND "clinical data" AND (CIE-10 OR coding)
3. "health information exchange" AND "hospital interoperability" AND "patient continuity"
4. "Peru" AND "electronic health record interoperability"
5. "interoperability" AND "SIS" AND "MINSA" (para literatura local y gris)

## Paso 2. Búsqueda en web

### Criterios aplicados

- ventana temporal: 2023-2025
- tipo de documento: journal article
- idioma: inglés preferente (y español cuando aporte contexto local)
- foco temático: interoperabilidad técnica, semántica y operativa de historias clínicas

### Fuentes usadas

- Crossref API (extracción de metadatos y DOI)
- Páginas institucionales de estándares (HL7, DICOM, OMS)

### Nota metodológica

El criterio de cuartil Q1/Q2 no se puede confirmar al 100% solo con Crossref; para defensa formal se recomienda validar cada revista en Scopus/SCImago o Web of Science.

## Paso 3. Artículos encontrados (selección final)

Se consolidó una muestra útil de 10 artículos recientes con DOI verificable.

| Año | Artículo | Revista | DOI |
|---|---|---|---|
| 2025 | Assessing the value of health information exchange organizations to hospital interoperability | Health Affairs Scholar | 10.1093/haschl/qxaf133 |
| 2024 | State-of-the-Art Fast Healthcare Interoperability Resources (FHIR)-Based Data Model and Structure Implementations: Systematic Scoping Review | JMIR Medical Informatics | 10.2196/58445 |
| 2024 | Electronic Health Record and Semantic Issues Using Fast Healthcare Interoperability Resources: Systematic Mapping Review | Journal of Medical Internet Research | 10.2196/45209 |
| 2024 | Interoperability of health data using FHIR Mapping Language: transforming HL7 CDA to FHIR with reusable visual components | Frontiers in Digital Health | 10.3389/fdgth.2024.1480600 |
| 2024 | Electronic Health Record Interoperability System in Peru Using Blockchain | International Journal of Online and Biomedical Engineering (iJOE) | 10.3991/ijoe.v20i03.44507 |
| 2023 | Interoperability of heterogeneous health information systems: a systematic literature review | BMC Medical Informatics and Decision Making | 10.1186/s12911-023-02115-5 |
| 2023 | Interoperability with multiple Fast Healthcare Interoperability Resources (FHIR) profiles and versions | JAMIA Open | 10.1093/jamiaopen/ooad001 |
| 2023 | Federated electronic health records for the European Health Data Space | The Lancet Digital Health | 10.1016/S2589-7500(23)00156-5 |
| 2023 | Electronic health record interoperability using FHIR and blockchain: A bibliometric analysis and future perspective | Perspectives in Clinical Research | 10.4103/picr.picr_272_22 |
| 2023 | Interoperability of Clinical Data through FHIR: A review | Procedia Computer Science | 10.1016/j.procs.2023.03.115 |

Archivos de soporte generados:

- articulos-seleccionados.csv
- articulos-seleccionados.json

### Síntesis por categorías (según los artículos)

#### Modelos identificados

- modelos de arquitectura federada para intercambio clínico
- modelos de mapeo semántico CDA-FHIR
- modelos de interoperabilidad con blockchain + FHIR
- modelos organizacionales de HIE/HIO para interoperabilidad hospitalaria
- modelos de evaluación de compatibilidad de perfiles FHIR

#### Metodologías predominantes

- revisiones sistemáticas
- scoping reviews
- systematic mapping reviews
- análisis bibliométrico
- estudios de implementación/prototipo

#### Métodos recurrentes

- mapeo terminológico y semántico
- transformación de estructuras clínicas a FHIR
- diseño de arquitectura interoperable
- evaluación de intercambio entre perfiles/servidores
- medición de adopción institucional de intercambio

#### Técnicas

- HL7 FHIR profiles/resources
- CDA to FHIR mapping
- terminología clínica estandarizada
- APIs de interoperabilidad
- trazabilidad y control de acceso

#### Frameworks/estándares más citados

- HL7 FHIR
- HL7 CDA
- DICOM (en integración de imágenes)
- marcos de HIE/HIO

## Paso 4. Título refinado (formato solicitado)

Formato: Aporte/Propuesta + Técnica + Problema + Escenario

Título propuesto:

Modelo de evaluación y predicción del riesgo de fragmentación de historias clínicas basado en estándares de interoperabilidad y aprendizaje automático en centros de salud MINSA del ámbito SIS en Lima.

Desglose del formato:

- Aporte/Propuesta: Modelo de evaluación y predicción del riesgo de fragmentación.
- Técnica: Estándares de interoperabilidad + aprendizaje automático supervisado.
- Problema: Deficiencias de interoperabilidad y gestión de historia clínica SIS.
- Escenario: Centros de salud MINSA (Lima, con posibilidad de escalar a otras regiones).

## Paso 5. Problema general refinado

¿De qué manera un modelo de evaluación y predicción, basado en indicadores de interoperabilidad técnica y semántica, permitirá estimar el riesgo de fragmentación de historias clínicas de pacientes SIS en centros de salud del MINSA en Lima?

## Paso 6. Problemas específicos (alineados al esquema de clase)

1. ¿Qué variables de entrada (técnicas, semánticas, organizacionales y de proceso) influyen de forma significativa en la fragmentación de historias clínicas de pacientes SIS?
2. ¿Qué técnicas o algoritmos permiten estimar con mayor confiabilidad la probabilidad de fragmentación e inconsistencia del dato clínico?
3. ¿Qué nivel de desempeño (AUC-ROC, F1, precisión, sensibilidad) demuestra capacidad predictiva suficiente para apoyar decisiones de mejora en interoperabilidad?

## Paso 7. Variables para el modelo específico

### Variables de entrada sugeridas

- porcentaje de campos obligatorios completos
- porcentaje de diagnósticos codificados en CIE-10 válidos
- porcentaje de procedimientos codificados en CPMS válidos
- sincronización de catálogos IEDS (sí/no y frecuencia)
- disponibilidad de conexión operativa a PIDESALUD
- número de duplicados por paciente/atención
- tiempo de validación administrativa SIS
- disponibilidad de trazabilidad/auditoría de accesos

### Variable objetivo (target)

- riesgo de fragmentación de historia clínica: bajo, medio, alto

### Métricas sugeridas

- AUC-ROC
- F1-score
- precisión
- sensibilidad/recall
- matriz de confusión

## Paso 8. Lista de trabajo para continuar

1. Definir muestra de establecimientos (mínimo 3 niveles de complejidad).
2. Construir ficha de levantamiento de datos por establecimiento.
3. Operacionalizar cada variable con fórmula y fuente.
4. Ejecutar prueba piloto de calidad de datos.
5. Entrenar y comparar 2-4 algoritmos base (ejemplo: regresión logística, random forest, XGBoost, árbol de decisión).
6. Validar desempeño y seleccionar modelo final.

## Entregable de diagrama

Se creó el diagrama específico del problema en:

- diagrama-problema-especifico.puml