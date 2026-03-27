::: {custom-style="Portada-Centrado"}
![](media/image1.png)
:::

::: {custom-style="Portada-Centrado"}
**MAESTRÍA EN INGENIERÍA DE SOFTWARE**
:::

::: {custom-style="Portada-Centrado"}
**PROYECTO DE TESIS**
:::

::: {custom-style="Portada-Centrado"}
**"MODELO DE INTEROPERABILIDAD BASADO EN HL7 FHIR PARA LA MEJORA DE LA GESTIÓN DE HISTORIAS CLÍNICAS EN CENTROS DE SALUD DEL MINSA - PERÚ"**
:::

::: {custom-style="Portada-Centrado"}
PRESENTADO POR:
:::

::: {custom-style="Portada-Centrado"}
**Bach. Cangalaya Carrasco Henry Miguel**

**Bach. Guzmán Vargas Jhessel**

**Bach. Yanqui Rivera Maria de los Angeles**
:::

::: {custom-style="Portada-Centrado"}
**Asesor(a):** [Nombre del Asesor(a)]
:::

::: {custom-style="Portada-Centrado"}
PARA OPTAR EL GRADO ACADÉMICO DE:
:::

::: {custom-style="Portada-Centrado"}
**MAESTRO(A) EN INGENIERÍA DE SOFTWARE**
:::

::: {custom-style="Portada-Centrado"}
LIMA

2026
:::


\newpage

# Agradecimiento

Cuerpo de texto cuerpo de texto cuerpo de texto cuerpo de texto, cuerpo
de texto cuerpo de texto cuerpo de texto cuerpo de texto cuerpo de texto
cuerpo de texto cuerpo de texto cuerpo de texto cuerpo de texto. Cuerpo
de texto cuerpo de texto cuerpo de texto cuerpo de texto, cuerpo de
texto cuerpo de texto cuerpo de texto cuerpo de texto cuerpo de texto
cuerpo de texto cuerpo de texto cuerpo de texto cuerpo de texto cuerpo
de texto cuerpo.


\newpage

# Índice


\newpage

# Índice de tablas


\newpage

# Índice de figuras


\newpage

# Resumen

La presente investigación propone un modelo de interoperabilidad basado en HL7 FHIR para mejorar la gestión de historias clínicas de pacientes SIS en centros de salud del MINSA en Perú. El estudio se estructura en tres fases: diagnóstico de brechas de interoperabilidad, implementación piloto de una capa de integración FHIR y evaluación del impacto mediante comparación pre y post intervención. En la fase diagnóstica se analiza el cumplimiento de estándares y componentes clave (RNIEDS, PIDESALUD, HL7, CIE-10 y CPMS), así como la calidad de los registros clínicos. En la fase de implementación se plantea el diseño y despliegue de servicios de integración orientados a mejorar completitud, codificación, trazabilidad y continuidad de atención. En la fase de evaluación se utilizan indicadores de desempeño para medir cambios en la calidad de gestión de historias clínicas. Los resultados esperados incluyen reducción de duplicidad de registros, mejora en codificación clínica, disminución de tiempos de validación y fortalecimiento de la continuidad asistencial, aportando lineamientos de escalabilidad para otros establecimientos del MINSA.

**Palabras claves:** Interoperabilidad en salud, Historia clínica electrónica, HL7 FHIR, SIS, MINSA

\newpage

# Abstract

This research proposes an interoperability model based on HL7 FHIR to improve the management of electronic health records for SIS-insured patients in MINSA health centers in Peru. The study is structured into three phases: interoperability gap diagnosis, pilot implementation of an FHIR integration layer, and impact evaluation through pre- and post-intervention comparison. The diagnostic phase assesses compliance with key standards and components (RNIEDS, PIDESALUD, HL7, ICD-10, and CPMS), as well as clinical data quality. The implementation phase focuses on the design and deployment of integration services aimed at improving record completeness, coding quality, traceability, and continuity of care. The evaluation phase uses performance indicators to measure changes in health record management quality. Expected outcomes include reduced record duplication, improved clinical coding, shorter administrative validation times, and stronger care continuity, providing scalability guidelines for other MINSA facilities.

**Keywords:** Health interoperability, Electronic health records, HL7 FHIR, SIS, MINSA

\newpage

# Introducción

La interoperabilidad en salud constituye un factor crítico para garantizar la continuidad asistencial, la seguridad del paciente y la eficiencia administrativa en los sistemas públicos de atención. A nivel global, la fragmentación de los sistemas de información sanitarios ha sido identificada como un obstáculo persistente para el intercambio efectivo de datos clínicos (Torab-Miandoab et al., 2023; Holmgren et al., 2023). Según Vorisek et al. (2022), HL7 FHIR se ha consolidado como el estándar de referencia para habilitar la interoperabilidad, con un crecimiento sostenido en su adopción para investigación clínica y gestión de datos de salud.

En el contexto peruano, el Ministerio de Salud (MINSA) ha emitido un marco normativo específico —la Infraestructura de Estándares de Datos en Salud (IEDS), la Red Nacional de Interoperabilidad en Datos de Salud (RNIEDS) y la Plataforma de Interoperabilidad de Datos Estándares de Salud (PIDESALUD)— orientado a estandarizar el intercambio de información entre establecimientos del Seguro Integral de Salud (SIS). Sin embargo, la implementación operativa de estas normativas permanece incompleta y heterogénea, como documentan Mauricio et al. (2024) al señalar que en Perú no existe actualmente un sistema integrado de historias clínicas electrónicas que permita compartir información automáticamente entre establecimientos.

Frente a este escenario, la presente investigación propone un modelo de interoperabilidad basado en HL7 FHIR que integra tres fases secuenciales: diagnóstico de brechas, implementación piloto de una capa de integración y evaluación de impacto mediante indicadores de calidad de gestión de historias clínicas. El estudio se sustenta en evidencia científica reciente —incluyendo revisiones sistemáticas de Amar et al. (2024), Tabari et al. (2024) y Pimenta et al. (2023)— y en experiencias internacionales de implementación en Estonia (Bossenko et al., 2024), Indonesia (Heryawan et al., 2025) y Sri Lanka (Jayathissa y Hewapathrana, 2024).

El documento se estructura en cinco capítulos. El Capítulo I presenta el planteamiento del problema, los objetivos, la justificación y las limitaciones. El Capítulo II desarrolla el marco teórico, incluyendo antecedentes internacionales y nacionales, bases teóricas y la definición de términos. El Capítulo III formula las hipótesis y operacionaliza las variables. El Capítulo IV describe la metodología del estudio. El Capítulo V presenta los aspectos administrativos, incluyendo el presupuesto y el cronograma de actividades.

\newpage

# Capítulo I: Planteamiento del estudio

## Planteamiento y formulación del problema

### Planteamiento del problema

La interoperabilidad de los sistemas de información en salud constituye uno de los desafíos más críticos de la transformación digital sanitaria a nivel mundial. El sector salud es intensivo en datos, con volúmenes masivos de información clínica que se crean, consultan y transfieren diariamente entre múltiples establecimientos y sistemas (Pimenta et al., 2023). Sin embargo, la falta de regulación uniforme permite que cada establecimiento seleccione su sistema de registro electrónico según criterios técnicos, operativos, económicos y legales propios, lo que frecuentemente genera registros de pacientes segregados en sistemas centrados en la institución, produciendo fragmentación de la información (Pimenta et al., 2023). Las consecuencias de esta fragmentación van desde tratamientos ineficaces hasta la ausencia de información crucial en situaciones de emergencia; de hecho, según un informe del BMJ citado por Pimenta et al. (2023), los errores médicos son la tercera causa de muerte, y el 44% de las muertes por error médico son prevenibles.

A nivel global, la revisión sistemática de Torab-Miandoab et al. (2023), que analizó 36 estudios sobre interoperabilidad de sistemas de información sanitarios heterogéneos, concluye que la falta de interoperabilidad reduce la calidad de la atención y desperdicia recursos, existiendo una necesidad urgente de desarrollar mecanismos de integración entre los diversos sistemas de información en salud. Estos autores identificaron que HL7 FHIR, CDA, SNOMED-CT, HIPAA y arquitecturas SOA figuran entre los requisitos más importantes para implementar interoperabilidad, y que la interacción semántica es la alternativa más idónea porque permite que los sistemas reconozcan y procesen información semánticamente similar de forma homogénea.

La revisión sistemática de Vorisek et al. (2022), que incluyó 49 estudios sobre el uso de FHIR en investigación en salud, evidenció que aunque FHIR puede implementarse efectivamente, las limitaciones incluyen cambios en el contenido de los recursos, aspectos de seguridad, cuestiones legales y la necesidad de infraestructura de servidores FHIR. El 73% de los estudios cubrieron investigación clínica, y los usos principales fueron estandarización de datos (41%), captura de datos (29%), reclutamiento (14%), análisis (12%) y gestión de consentimiento (4%).

En el contexto del intercambio de información sanitaria, Holmgren et al. (2023) revisaron los marcos de políticas de cinco países (Estados Unidos, Reino Unido, Alemania, Israel y Portugal) y concluyeron que, si bien todos han adoptado algún nivel de intercambio, existen diferencias significativas en la infraestructura y madurez del intercambio de datos, y cada nación adoptó un enfoque de política diferente. Los autores destacan la importancia de la priorización gubernamental centralizada del intercambio de datos como factor común en los marcos exitosos. Richwine et al. (2025), utilizando datos representativos a nivel nacional de 2.200 hospitales en Estados Unidos, encontraron que la participación hospitalaria en organizaciones de intercambio de información en salud (HIO) se asocia significativamente con un mayor compromiso en intercambio de información clínica, reportes de salud pública e intercambio de datos sobre necesidades sociales relacionadas con la salud.

En la región de América Latina, Bayona Castañeda (2019) documentó que el sistema de salud peruano se encuentra segmentado y fragmentado, con un paciente que puede tener tantas historias clínicas como establecimientos visita — e incluso más de una en un mismo establecimiento —, y que la implementación de la HCE ha sido entorpecida por la inestabilidad política y la falta de integración entre MINSA y EsSalud. Arrué Pajares y Vargas Rioja (2022) confirman que en el Perú se carece de sistemas de información interoperables y que la escasez de estos impide optimizar tiempos de uso de consultorios, camas hospitalarias, salas de operaciones y referencias entre establecimientos. Más recientemente, Mauricio et al. (2024) señalan que en Perú actualmente no existe un sistema integrado de historias clínicas electrónicas que pueda compartirse automáticamente entre establecimientos de salud, lo que genera costos incrementados por exámenes y registros duplicados, así como tiempo adicional necesario para gestionar la información clínica de los pacientes. Estos autores propusieron un sistema de interoperabilidad basado en blockchain y FHIR para sistemas heterogéneos peruanos, demostrando niveles muy altos de adopción y usabilidad. Porras Gamarra (2024), con experiencia directa en la implementación de interoperabilidad HL7 FHIR y openEHR en Europa, señala que durante la pandemia de COVID-19 la diferencia tecnológica fue notoria: mientras en la Unión Europea se discutía sobre el tipo de mensaje HL7 para registros de vacunación, en Perú se intentaba construir sistemas aislados sin planificación ni estándares.

En este contexto nacional, los centros de salud del MINSA presentan deficiencias específicas en la interoperabilidad de sus sistemas de información y en la gestión de historias clínicas de pacientes afiliados al SIS. Estas brechas se manifiestan en: (a) problemas de completitud de registros clínicos, (b) inconsistencias en codificación clínica CIE-10 y CPMS, (c) duplicidad de información de pacientes y exámenes, y (d) limitaciones para la trazabilidad y continuidad de atención entre establecimientos. Aunque existe un marco normativo nacional (RM N° 1104-2018-MINSA, RM N° 464-2019-MINSA, RM N° 1193-2019-MINSA) que define la Infraestructura de Estándares de Datos en Salud (IEDS), la Red Nacional de Interoperabilidad en Datos de Salud (RNIEDS) y la Plataforma de Interoperabilidad de Datos Estándares de Salud (PIDESALUD), su implementación no es uniforme entre establecimientos, perpetuando la fragmentación informacional.

La Organización Panamericana de la Salud (OPS, 2024) define la interoperabilidad como la capacidad de diferentes sistemas de tecnología de la información para comunicar e intercambiar datos con exactitud, efectividad y consistencia, y destaca que para lograrla deben resolverse dos problemas fundamentales: la interoperabilidad técnica (transferencia fiable de datos entre sistemas) y la interoperabilidad semántica (comprensión mutua de la información recibida).

Frente a este panorama, se requiere una propuesta de intervención fundamentada en la evidencia que permita: (1) diagnosticar las brechas de interoperabilidad con instrumentos validados, (2) implementar una capa de integración basada en HL7 FHIR alineada con los estándares internacionales y el marco normativo nacional, y (3) evaluar sus efectos medibles en la calidad de gestión de las historias clínicas. La presente investigación responde a esta necesidad integrando las tres fases en un modelo coherente y replicable.

### Formulación del problema

1.  *Problema general*

¿De qué manera un modelo que integre el diagnóstico de brechas de interoperabilidad y la implementación piloto de una capa de integración basada en HL7 FHIR permitirá mejorar la gestión de historias clínicas de pacientes SIS en centros de salud del MINSA en Perú?

2.  *Problemas específicos*

- ¿Cuál es el nivel actual de cumplimiento de los estándares de interoperabilidad (RNIEDS, PIDESALUD, HL7, CIE-10, CPMS) y qué brechas críticas existen en la gestión de historias clínicas?
- ¿Cómo diseñar e implementar una capa de integración basada en HL7 FHIR que atienda las brechas de interoperabilidad identificadas?
- ¿En qué medida la implementación piloto de la capa de integración FHIR mejora la integridad, continuidad y calidad de las historias clínicas respecto a la línea base diagnóstica?

## Determinación de objetivos

### Objetivo general

Desarrollar e implementar un modelo de interoperabilidad basado en HL7 FHIR que permita mejorar la gestión de historias clínicas de pacientes SIS en centros de salud del MINSA en Perú, mediante un proceso estructurado de diagnóstico, intervención y evaluación de resultados.

### Objetivos específicos

- Identificar y analizar el nivel de cumplimiento de estándares de interoperabilidad (RNIEDS, PIDESALUD, HL7, CIE-10 y CPMS) y las brechas críticas de gestión de historias clínicas en centros de salud MINSA del ámbito SIS.
- Diseñar e implementar una capa piloto de integración basada en HL7 FHIR que responda a las brechas de interoperabilidad identificadas en la fase diagnóstica.
- Evaluar el desempeño e impacto del modelo implementado mediante comparación pre y post intervención, utilizando indicadores de integridad, continuidad y calidad de las historias clínicas.
- Proponer lineamientos técnicos y operativos para la escalabilidad del modelo de interoperabilidad en otros establecimientos de salud del MINSA.

## Justificación e importancia del estudio

### Justificación teórica

La investigación aporta al campo de la interoperabilidad en salud al integrar en un mismo marco analítico los componentes organizativos, semánticos, técnicos y de evaluación de resultados en la gestión de historias clínicas electrónicas. Amar et al. (2024), en su revisión de mapeo sistemático de 70 estudios sobre FHIR e interoperabilidad semántica, identificaron seis categorías de enfoques —mapeo (24,6%), servicios de terminología (14,3%), propuestas basadas en RDF/OWL (19%), anotación (14,3%), aprendizaje automático y procesamiento de lenguaje natural (15,9%) y ontologías (11,9%)— pero señalan la necesidad de marcos integradores que combinen estos enfoques con la evaluación de resultados en contextos operativos reales. Tabari et al. (2024), en su scoping review de modelos de datos FHIR, concluyen que aunque FHIR es un estándar altamente prometedor, los esfuerzos continuos para abordar limitaciones existentes son esenciales para su implementación exitosa. La presente investigación contribuye a cerrar este vacío al articular estándares internacionales (HL7 FHIR, HL7 CDA, DICOM) con el marco normativo peruano (RM N° 1104-2018-MINSA, RM N° 464-2019-MINSA, RM N° 1193-2019-MINSA), generando conocimiento sobre la aplicación efectiva de estos estándares en contextos de atención pública como el SIS-MINSA.

### Justificación metodológica

La propuesta sigue un procedimiento sistemático y replicable en tres fases —diagnóstico de brechas, implementación piloto y evaluación de impacto—, alineándose con las metodologías predominantes en la literatura reciente. Adelusi et al. (2025) demostraron que un framework federado de interoperabilidad basado en FHIR, evaluado mediante métricas de latencia, integridad de datos y escalabilidad, alcanzó más del 95% de precisión en recuperación de datos y una reducción del 38% en latencia respecto a sistemas centralizados convencionales. Liu et al. (2023) validaron la implementación de un sistema EMR en formato FHIR mediante pruebas de rendimiento con Apache JMeter, demostrando que reemplazar gateways con servidores FHIR reduce efectivamente el tiempo y costo de conversión de formatos. La estructura metodológica del presente estudio facilita su reproducción en otros entornos de salud, al definir con claridad instrumentos, variables, métricas e indicadores de desempeño. La comparación pre y post intervención permite generar evidencia objetiva sobre la efectividad del modelo, siguiendo el enfoque de diseño pre-experimental validado en la literatura internacional.

### Justificación social

La mejora de la interoperabilidad impacta directamente en la continuidad y oportunidad de la atención de los pacientes afiliados al SIS. Según Holmgren et al. (2023), una interoperabilidad robusta puede desacelerar el crecimiento de costos médicos mediante la reducción de utilización duplicativa, y puede reducir la carga administrativa de los pacientes al permitir que sus datos los sigan de forma transparente a lo largo del continuo de atención. Pimenta et al. (2023) señalan que el tratamiento adecuado de un paciente solo es posible cuando los profesionales de salud tienen acceso a la colección más actualizada y completa de datos personales y clínicos, siendo la interoperabilidad crítica para alcanzar la excelencia en la atención. La OPS (2024) enfatiza que en el ecosistema de salud, la interoperabilidad permite que los sistemas de información trasciendan los límites de la organización y promuevan una prestación de servicios efectivos, al suministrar la información correcta a los proveedores de atención para comprender y abordar la salud de las personas y las poblaciones. Al disponer de información clínica más íntegra, accesible y trazable, se fortalece la seguridad del paciente, se reduce el riesgo de errores por información incompleta y se favorece una atención más equitativa en el sistema público de salud peruano, especialmente en las poblaciones con mayor vulnerabilidad.

## Limitaciones de la presente investigación

- **Disponibilidad y calidad de los datos:** Los registros clínico-administrativos del MINSA pueden presentar vacíos, inconsistencias o falta de estandarización que limiten la precisión del diagnóstico de brechas. Torab-Miandoab et al. (2023) señalan que los sistemas actualmente en uso son propietarios y pueden diferir de una institución a otra, lo que dificulta la extracción homogénea de datos. *Mitigación:* Se aplicarán criterios de exclusión para registros incompletos y se documentará el porcentaje de datos descartados para transparentar el alcance real de la muestra analizada.

- **Acceso a fuentes de información institucional:** La obtención de autorizaciones para acceder a sistemas de información del MINSA puede retrasarse o restringirse por políticas institucionales de seguridad de datos. Mauricio et al. (2024) reportan que en Perú muchos proveedores de salud, especialmente en áreas rurales, carecen de acceso a sistemas de información de EHR, dificultando la continuidad de atención. *Mitigación:* Se gestionarán los permisos institucionales desde la fase inicial del proyecto y se establecerán acuerdos de confidencialidad. En caso de restricciones, se utilizarán datos anonimizados o sintéticos para las pruebas técnicas, tal como proponen Jayathissa y Hewapathrana (2024) con datasets sintéticos HHIMS.

- **Alcance geográfico:** El estudio se limita a establecimientos de salud MINSA en Lima, lo que restringe la generalización a otras regiones. Holmgren et al. (2023) observan que las diferencias estructurales de los sistemas de salud nacionales hacen difícil identificar estrategias generalizables entre contextos dispares. *Mitigación:* Se seleccionarán establecimientos de al menos 2-3 niveles de complejidad para capturar variabilidad representativa y se documentarán lineamientos de escalabilidad para futuras réplicas en otras regiones.

- **Limitaciones del modelo de interoperabilidad implementado:** Kramer y Moesel (2023) demuestran que aplicaciones que siguen diferentes Guías de Implementación FHIR pueden no ser capaces de interoperar entre sí, y que confirmar la conformidad de dos sistemas con sus respectivas especificaciones no implica que puedan intercambiar datos. Vorisek et al. (2022) identifican como limitaciones el posible cambio en el contenido de los recursos FHIR, aspectos de seguridad y la necesidad de un servidor FHIR. *Mitigación:* Se utilizarán perfiles FHIR alineados con estándares empleados internacionalmente (US Core, International Patient Summary) y se documentarán explícitamente las decisiones de diseño y sus restricciones.

- **Variables no identificadas:** Es posible que factores organizacionales, culturales o técnicos no considerados influyan en los resultados. Heryawan et al. (2025) identificaron que los pain points de implementaciones FHIR incluyen problemas de servidor (57%), mapeo de datos (34%) y selección de perfiles (9%), revelando barreras no siempre anticipadas. *Mitigación:* Se complementará el enfoque cuantitativo con entrevistas cualitativas semiestructuradas para capturar factores emergentes y barreras no previstas.

- **Restricciones de tiempo y recursos:** La implementación piloto es acotada al período académico de la investigación. *Mitigación:* Se priorizarán las brechas de mayor impacto y viabilidad mediante una matriz de priorización, enfocando los recursos en un piloto funcional que pueda ser extendido en fases posteriores.

# Capítulo II: Marco teórico

## Antecedentes del problema

### Internacionales

**Adelusi et al. (2025)** propusieron un Framework Federado de Interoperabilidad basado en FHIR para el intercambio de datos entre múltiples hospitales en Nigeria. El framework fue evaluado mediante simulación con tres sistemas hospitalarios que operaban plataformas EHR diferentes, obteniendo más del 95% de éxito en precisión de recuperación de datos, una reducción del 38% en latencia respecto a sistemas centralizados convencionales y cumplimiento total de protocolos FHIR, sin transferencia de datos crudos entre instituciones.

Este antecedente es directamente relevante para la presente investigación porque valida la viabilidad de un enfoque federado basado en FHIR para integrar sistemas EHR heterogéneos — situación análoga a la del MINSA, donde cada establecimiento opera sistemas de registro independientes. Las métricas de latencia, integridad de datos y escalabilidad empleadas por Adelusi et al. sirven como referente para los indicadores de evaluación propuestos en la Fase 3 del modelo.

**Heryawan et al. (2025)** analizaron el diseño de interoperabilidad FHIR en Indonesia mediante análisis de contenido de la plataforma nacional Satusehat, un sistema que busca integrar datos de salud a escala nacional. Identificaron que los principales problemas reportados por desarrolladores fueron: servidor FHIR (57%), mapeo de datos (34%) y selección de perfiles (9%). Propusieron una arquitectura federada en lugar de centralizada y un sistema de escritor/visor FHIR como solución a las limitaciones encontradas.

La experiencia de Indonesia descrita por Heryawan et al. es particularmente pertinente para el contexto peruano, ya que ambos países comparten características similares: sistemas de salud pública con infraestructura tecnológica heterogénea, múltiples niveles de atención y un proceso de digitalización en curso. Los problemas de mapeo de datos y selección de perfiles identificados anticipan desafíos que el modelo propuesto deberá abordar en la Fase 2 de implementación piloto.

**Amar et al. (2024)** realizaron una revisión de mapeo sistemático de 70 estudios (2012-2022) sobre interoperabilidad semántica utilizando FHIR, publicados en bases de datos especializadas. Clasificaron los enfoques semánticos en seis categorías: mapeo (24,6%), servicios de terminología (14,3%), propuestas basadas en RDF/OWL (19%), anotación (14,3%), aprendizaje automático y procesamiento de lenguaje natural (15,9%) y ontologías (11,9%). La contribución más frecuente fue la propuesta de frameworks o arquitecturas para habilitar la interoperabilidad semántica.

Esta revisión aporta al presente estudio la taxonomía de enfoques semánticos disponibles para implementar interoperabilidad FHIR. La categoría de mapeo — la más frecuente según Amar et al. — es la estrategia central adoptada en la Fase 2 del modelo propuesto, donde los datos locales de los sistemas HIS del MINSA se transforman a recursos FHIR estandarizados.

**Tabari et al. (2024)** publicaron un scoping review sobre modelos de datos y estructuras basadas en FHIR, analizando artículos en PubMed, Scopus, Web of Science, IEEE Xplore, ACM Digital Library y Google Scholar. Identificaron dos temas principales: modelos dinámicos (basados en pipelines de transformación) y modelos estáticos (estructuras de datos predefinidas). Los recursos FHIR más utilizados fueron "Observation", seguido de "Condition" y "Patient". Concluyeron que la implementación de modelado FHIR para datos de EHR facilita la integración, transmisión y análisis de datos.

Los hallazgos de Tabari et al. fundamentan la selección de recursos FHIR para la capa de integración piloto del presente estudio. Los recursos Patient, Encounter, Observation, Condition y Procedure, identificados como los más frecuentes en la literatura, corresponden a los elementos centrales de las historias clínicas del MINSA y serán priorizados en el mapeo de datos.

**Bossenko et al. (2024)** desarrollaron una herramienta y técnicas para la interoperabilidad semántica de datos de salud en Estonia, utilizando FHIR Mapping Language para transformar documentos CDA a recursos FHIR mediante componentes visuales reutilizables. La herramienta fue validada en el contexto de la transición del Sistema Nacional de Información de Salud de Estonia de CDA a FHIR, demostrando alta usabilidad y valor de negocio según la evaluación de expertos del dominio.

La experiencia de Estonia es relevante para el modelo propuesto porque demuestra que la transformación de formatos clínicos heredados a FHIR puede realizarse con herramientas accesibles que permiten la participación de expertos en salud con mínimas habilidades técnicas. Este enfoque puede adaptarse al contexto del MINSA, donde el personal de salud debe apropiarse de los procesos de interoperabilidad sin depender exclusivamente de ingenieros de software.

**Jayathissa y Hewapathrana (2024)** revisaron la implementación técnica de un servidor HAPI-FHIR para mejorar la interoperabilidad entre sistemas de información de atención primaria en Sri Lanka. El estudio abordó desafíos específicos de identidad de pacientes, integración de biometría para autenticación y mecanismos de seguridad de datos en un entorno de recursos limitados, utilizando datasets sintéticos HHIMS para las pruebas de validación.

Sri Lanka comparte con Perú restricciones típicas de países en desarrollo: infraestructura digital desigual, múltiples sistemas no integrados y limitaciones presupuestarias. La solución basada en HAPI-FHIR descrita por Jayathissa y Hewapathrana constituye un precedente técnico para la arquitectura de servidor FHIR que se evaluará en la Fase 2 del presente estudio, particularmente en lo referente a gestión de identidad de pacientes entre establecimientos.

**Torab-Miandoab et al. (2023)** realizaron una revisión sistemática de la literatura sobre interoperabilidad de sistemas de información sanitarios heterogéneos, analizando 36 artículos publicados hasta julio de 2022 en seis bases de datos (PubMed, Web of Science, Scopus, MEDLINE, Cochrane Library y Embase). Encontraron que los proyectos en este campo son mayoritariamente de alcance nacional y orientados a lograr la historia clínica electrónica. Los requisitos más importantes identificados incluyen HL7 FHIR, CDA, HIPAA, SNOMED-CT, SOA, RIM, XML, API, JAVA y SQL. Concluyeron que la interacción semántica es la mejor opción para garantizar el intercambio de datos.

Este antecedente sustenta la selección de HL7 FHIR como estándar central del modelo propuesto, al confirmar que FHIR es el requisito técnico más citado en la literatura sobre interoperabilidad de sistemas heterogéneos. Además, la conclusión sobre la primacía de la interoperabilidad semántica refuerza la necesidad de incorporar codificación estandarizada (CIE-10, CPMS, SNOMED-CT) en la capa de integración del presente estudio.

**Holmgren et al. (2023)** realizaron una revisión narrativa del panorama de políticas de intercambio de información sanitaria (HIE) en cinco países (Estados Unidos, Reino Unido, Alemania, Israel y Portugal), concluyendo que la priorización gubernamental centralizada es un factor común en los marcos exitosos, y que los desafíos de la adopción amplia de HIE incluyen factores técnicos, organizacionales y regulatorios. Los autores destacan que cada nación adoptó un enfoque de política diferente según sus particularidades.

Los hallazgos de Holmgren et al. validan el anclaje normativo del presente estudio al marco regulatorio peruano (IEDS, RNIEDS, PIDESALUD). La conclusión de que la priorización gubernamental centralizada es determinante para el éxito del HIE respalda la pertinencia de articular el modelo propuesto con las políticas del MINSA, y sustenta la recomendación de establecer una gobernanza digital específica para la interoperabilidad.

**Vorisek et al. (2022)** llevaron a cabo una revisión sistemática sobre el uso de FHIR en investigación en salud, incluyendo 49 estudios de las bases PubMed/MEDLINE, Embase, Web of Science, IEEE Xplore y Cochrane Library (2011-2022). El 73% de los estudios cubrió investigación clínica. Los usos principales de FHIR fueron estandarización de datos (41%), captura de datos (29%), reclutamiento (14%), análisis (12%) y gestión de consentimiento (4%). El 63% de los estudios utilizó terminologías adicionales: LOINC (37%), SNOMED-CT (29%), CIE-10 (18%) y OMOP CDM (12%). Solo el 8% utilizó recursos del dominio "Salud Pública e Investigación" de FHIR.

Este estudio aporta el panorama más completo del estado de adopción de FHIR a nivel global, confirmando su consolidación como estándar de referencia. La baja utilización de recursos FHIR en el dominio de salud pública (8%) identificada por Vorisek et al. señala un área de oportunidad directamente relevante para la presente investigación, cuyo ámbito es precisamente el sistema público de salud peruano (MINSA-SIS).

**Gazzarata et al. (2024)** desarrollaron una scoping review sobre el uso de HL7 FHIR en ecosistemas digitales para el manejo de enfermedades crónicas, identificando que FHIR facilita continuidad de atención, integración de datos clínicos longitudinales y articulación entre servicios asistenciales en redes complejas. El estudio destaca que los beneficios de FHIR dependen no solo de la implementación técnica, sino también de mecanismos de gobernanza, estandarización y coordinación organizacional.

Este antecedente fortalece el enfoque de la presente investigación al evidenciar que, para contextos como MINSA-SIS, la adopción de FHIR debe evaluarse de forma integral: arquitectura técnica, calidad semántica de los datos y reglas de gestión interinstitucional.

**Pedrera-Jiménez et al. (2023)** analizaron la coexistencia y complementariedad entre OpenEHR, ISO 13606 y HL7 FHIR, proponiendo un enfoque agnóstico para la selección de estándares en espacios de datos de nueva generación. Sus resultados muestran que los estándares no deben considerarse excluyentes, sino como capas interoperables con funciones diferenciadas para modelado clínico, intercambio y reutilización.

Para este estudio, dicha evidencia es relevante porque respalda una estrategia de implementación pragmática en la que FHIR puede integrarse con activos previos y marcos normativos existentes, reduciendo fricción técnica durante la transición de sistemas heterogéneos.

**Chatterjee et al. (2022)** presentaron una prueba de concepto que combina HL7 FHIR con SNOMED-CT para lograr interoperabilidad estructural y semántica en datos personales de salud, reportando transferencia bidireccional sin pérdida de datos y con consistencia en la representación de conceptos clínicos. El estudio muestra que la codificación semántica mejora la reutilización y la trazabilidad de la información clínica.

Este hallazgo es directamente aplicable al problema de investigación, en especial para reducir inconsistencias en codificación y mejorar la continuidad informacional entre establecimientos del primer nivel de atención.

**Gaudet-Blavignac et al. (2021)** propusieron, en el contexto de la Swiss Personalized Health Network, una estrategia nacional de tres pilares orientada al uso secundario interoperable de datos de salud para investigación. Su aporte combina normalización semántica, lineamientos organizativos y herramientas técnicas para interoperar datos provenientes de múltiples fuentes clínicas.

La pertinencia para el presente trabajo radica en que confirma la necesidad de diseñar simultáneamente componentes técnicos y de gobernanza, particularmente cuando se busca escalar interoperabilidad más allá de una sola institución.

**Mukhiya et al. (2021)** desarrollaron una aproximación de interoperabilidad entre sistemas EHR heterogéneos usando HL7 FHIR y GraphQL, mostrando que una capa de abstracción orientada a APIs puede facilitar consultas flexibles, integración incremental y menor acoplamiento entre plataformas preexistentes.

Este antecedente respalda la decisión metodológica de implementar una capa de integración FHIR en el piloto, priorizando compatibilidad con sistemas heredados y reducción de complejidad de integración.

**Fernandez et al. (2025)** analizaron la interoperabilidad en sistemas de salud universal con evidencia del caso brasileño, resaltando la integración entre datos de atención primaria y hospitalaria como factor crítico para continuidad clínica y gestión poblacional. El estudio subraya que el valor de la interoperabilidad se materializa cuando la red asistencial comparte estándares, procesos y mecanismos de intercambio sostenibles.

Su aporte resulta relevante para la realidad peruana porque ofrece lecciones de implementación en un sistema público de gran escala y heterogeneidad territorial, comparable en complejidad operativa con la red MINSA.

### Nacionales

**Mauricio et al. (2024)** propusieron un sistema de interoperabilidad de historias clínicas electrónicas en Perú basado en blockchain y FHIR HL7. El sistema incluye la homologación de EHR con recursos FHIR para lograr interoperabilidad, y utiliza blockchain para garantizar la seguridad y privacidad de los datos. Fue probado mediante simulación de caso para demostrar interoperabilidad entre clínicas. Una encuesta con 30 pacientes sobre adopción y otra con 10 médicos de un hospital público peruano sobre usabilidad demostraron niveles muy altos en ambas dimensiones. Los autores señalan que en Perú no existe actualmente un sistema integrado de EHR que pueda compartirse automáticamente entre establecimientos, y que su propuesta no requiere alteraciones a los sistemas existentes.

Este antecedente es el más directamente vinculado con la presente investigación, al ser uno de los escasos estudios publicados que aborda la interoperabilidad de EHR con FHIR en el contexto peruano. El diagnóstico de Mauricio et al. sobre la inexistencia de un sistema integrado de historias clínicas electrónicas en Perú confirma la problemática central de este estudio. Sin embargo, a diferencia de su enfoque basado en blockchain, la presente investigación se centra en la implementación de una capa de integración FHIR articulada con el marco normativo del MINSA (IEDS, RNIEDS, PIDESALUD), orientada específicamente a establecimientos SIS.

**Porras Gamarra (2024)** presentó un trabajo de suficiencia profesional en la UNFV sobre la implementación de un sistema de interoperabilidad de información clínica basado en los estándares internacionales HL7 FHIR y openEHR. El trabajo monográfico describe el proyecto M-Connecta, desarrollado para el Departamento de Salud de Cataluña (España), donde se logró el intercambio efectivo de mensajes HL7 FHIR entre plataformas web y sistemas sanitarios, la persistencia de datos clínicos mediante arquetipos openEHR y la descongestión de citas en centros de atención primaria. El autor concluye que la interoperabilidad semántica y sintáctica entre FHIR y openEHR es factible y altamente ventajosa, y recomienda que HL7 FHIR sea implementado en las historias clínicas electrónicas del Perú.

Aunque el proyecto M-Connecta fue ejecutado en el contexto europeo, su autor es un ingeniero peruano que explicita la aplicabilidad de la experiencia al entorno nacional. Porras Gamarra destaca la brecha tecnológica evidenciada durante la pandemia de COVID-19 entre los sistemas de salud europeos — que ya intercambiaban mensajes HL7 para registros de vacunación — y los sistemas peruanos, incapaces de implementar soluciones interoperables en corto plazo. Esta perspectiva comparada refuerza la urgencia de la presente investigación y valida la selección de HL7 FHIR como estándar técnico central del modelo propuesto.

**Arrué Pajares y Vargas Rioja (2022)** desarrollaron como tesis en la PUCP la implementación de un Sistema de Información Hospitalario (HIS) interoperable basado en el estándar HL7 para centros médicos de categoría II-1 o superior. El sistema fue diseñado como plataforma web para gestionar información administrativa (finanzas, recursos humanos, instalaciones, citas, hospitalización) con capacidad de interoperar, mediante el protocolo HL7, con otros módulos del Healthcare Information Management System (HIMS) como Historia Clínica Electrónica, Farmacia, Laboratorio y Radiología. Los autores señalan que en el Perú se carece de sistemas de información interoperables y que el sistema de salud — tanto público (MINSA, EsSalud) como privado — se encuentra fraccionado, con componentes aislados entre sí.

Este antecedente demuestra la viabilidad técnica de construir un HIS interoperable con estándares HL7 en el contexto peruano, aunque basado en HL7 v2 y no en FHIR. La problemática descrita por Arrué Pajares y Vargas Rioja — ausencia de interoperabilidad, fragmentación del sector salud, gestión ineficiente de camas, consultorios y referencias — coincide plenamente con la situación que la presente investigación busca abordar. La evolución de HL7 v2 a FHIR justifica la necesidad de actualizar el enfoque hacia APIs RESTful y recursos FHIR, como propone el modelo de este estudio.

**Bayona Castañeda (2019)** realizó un trabajo de fin de máster en la Universitat Politècnica de València, titulado "Radiografía de la Historia Clínica en Perú", donde analizó la evolución de la implementación de las HCE en el sector salud peruano. La investigación documentó el proceso normativo desde la Ley N° 30024 que crea el Registro Nacional de Historias Clínicas Electrónicas (RENHICE), la plataforma estándar e-Qhali propuesta por el MINSA, y las barreras estructurales del sistema: fragmentación entre MINSA y EsSalud, falta de direccionalidad política, insuficiente conectividad, equipamiento desigual, y la generación de múltiples historias clínicas por paciente. La autora concluye que el objetivo de interoperabilidad del RENHICE se ha visto entorpecido por la falta de integración entre entidades y la inestabilidad política.

El diagnóstico exhaustivo de Bayona Castañeda constituye una línea base cualitativa del estado de la HCE en Perú previo al desarrollo de las normativas IEDS/RNIEDS/PIDESALUD (2018-2019). Sus hallazgos sobre la fragmentación del sistema de salud y la ausencia de interoperabilidad confirman la persistencia de la problemática que motiva la presente investigación. Además, su recomendación de establecer un control y registro de las implementaciones de plataformas en las IPRESS es consistente con el componente de diagnóstico (Fase 1) del modelo propuesto en este estudio.

**Esparza Morgan (2025)** evaluó la influencia de la historia clínica electrónica única en la gestión de la calidad de un hospital de EsSalud, reportando correlaciones positivas entre la madurez de uso de HCE y mejoras en planificación, organización y garantía de servicios. Sus resultados muestran que la digitalización clínica no solo impacta en registro de datos, sino también en desempeño de gestión.

Este antecedente refuerza el enfoque de evaluación del presente estudio, dado que vincula variables de interoperabilidad y calidad operativa, línea central de los indicadores pre y post intervención planteados para centros MINSA.

**Arias Geronimo (2025)** analizó la relación entre confiabilidad de las historias clínicas electrónicas y prestación de servicios de salud preventiva en una microred pública, encontrando asociación positiva moderada y significativa entre ambas dimensiones. El estudio identificó que la precisión de datos mejora la percepción de calidad del servicio, mientras la disponibilidad del sistema y la usabilidad siguen siendo brechas críticas.

La evidencia es pertinente para esta tesis porque confirma que la calidad técnica de la HCE afecta directamente resultados asistenciales en el primer nivel de atención, ámbito prioritario del modelo propuesto.

**Sanchez Calle (2024)** desarrolló una propuesta de arquitectura y requisitos para historia clínica electrónica ocupacional basada en ISO 18308:2011 e ISO 13606:2019, destacando la necesidad de especificaciones técnicas formales para asegurar intercambio estandarizado y sostenibilidad del sistema.

Este antecedente aporta fundamentos normativo-técnicos complementarios a FHIR, útiles para fortalecer el diseño de requisitos funcionales y no funcionales del piloto de interoperabilidad en el contexto peruano.

**Fernández Infanzón y Huarac Cuizano (2021)** propusieron un plan de negocio para integrar IPRESS a una plataforma de HCE apoyada en blockchain, verificación biométrica e interoperabilidad, orientado a articular prestadores privados y públicos bajo iniciativas nacionales como RENHICE. El trabajo identifica barreras de confianza, integridad y trazabilidad de datos, y plantea un esquema de adopción por stakeholders clínicos, administrativos y TI.

Aunque su enfoque es empresarial, su contribución es valiosa para esta investigación al evidenciar condiciones de viabilidad institucional y barreras de implementación que también impactan cualquier despliegue interoperable en el sistema de salud peruano.

**Bran et al. (2024)** examinaron la integración de blockchain, IPFS y HL7 para historias clínicas electrónicas, concluyendo que estas arquitecturas híbridas mejoran inmutabilidad, auditabilidad y confianza en el intercambio de datos clínicos cuando se combinan con marcos de interoperabilidad estandarizados.

Este antecedente contribuye al marco teórico al ampliar la discusión sobre seguridad y gobernanza de datos en escenarios interoperables, especialmente relevantes para redes con múltiples actores y distintos niveles de madurez digital.

**Morales-Camargo y Meneses-Claudio (2023)** realizaron una revisión sistemática sobre el impacto del registro médico electrónico en la atención y la gestión sanitaria, identificando mejoras en acceso a información, soporte a decisiones y eficiencia administrativa, aunque también reportan desafíos de implementación vinculados a capacitación, estandarización y adopción organizacional.

La revisión aporta evidencia transversal que respalda la hipótesis central del estudio: una mejor interoperabilidad y gestión de HCE se asocia con mejoras en desempeño asistencial y administrativo en establecimientos de salud.

A nivel regulatorio, Perú cuenta con el marco normativo específico emitido por el MINSA: la RM N° 1104-2018-MINSA que establece la Infraestructura de Estándares de Datos en Salud (IEDS), la RM N° 464-2019-MINSA que define la Red Nacional de Interoperabilidad en Datos de Salud (RNIEDS), y la RM N° 1193-2019-MINSA que regula la Plataforma de Interoperabilidad de Datos Estándares de Salud (PIDESALUD). Sin embargo, la implementación operativa de estas normativas permanece incompleta y heterogénea entre establecimientos, como lo muestran los diagnósticos nacionales recientes (Bayona Castañeda, 2019; Mauricio et al., 2024; Esparza Morgan, 2025; Arias Geronimo, 2025).

## Bases teóricas

Las bases teóricas del estudio se sustentan en la interoperabilidad en salud, la arquitectura de intercambio de información clínica y la estandarización semántica. La propuesta integra estándares de mensajería e intercambio (HL7/FHIR), estructuración documental clínica (CDA/CCD), codificación clínica (CIE-10, CPMS) y criterios de evaluación de calidad de datos clínicos en entornos de atención pública.

### Desarrollo histórico

La interoperabilidad en salud ha evolucionado progresivamente durante las últimas décadas, desde la digitalización de registros médicos en papel hasta los sistemas de intercambio electrónico basados en estándares. Según Surisetty (2026), las iniciativas de interoperabilidad clínica comenzaron con la mensajería HL7 v2, avanzaron a través de estándares centrados en documentos como CDA y CCD, y más recientemente han migrado hacia la interoperabilidad basada en APIs con HL7 FHIR. Amar et al. (2024) documentan que FHIR fue desarrollado por la organización Health Level Seven International (HL7) con el objetivo de evolucionar los estándares de mensajería para lograr la interoperabilidad semántica, combinando las mejores características de HL7 versión 2, versión 3 y CDA, al tiempo que aprovecha las últimas tecnologías web.

Vorisek et al. (2022) observaron un crecimiento significativo en la adopción de FHIR en años recientes, y un intervalo de cinco años entre la publicación del estándar FHIR y la primera publicación científica de interés al respecto, con Alemania y Estados Unidos liderando el número de publicaciones. En el contexto europeo, Raab et al. (2023) describen cómo la Comisión Europea ha propuesto el European Health Data Space (EHDS) para empoderar a los ciudadanos a acceder a sus datos de salud y compartirlos con médicos. En América Latina, el desarrollo ha sido más reciente; en Perú, Bayona Castañeda (2019) documentó que la implementación de la HCE ha estado marcada por la fragmentación del sistema de salud, la inestabilidad política y la falta de integración entre MINSA y EsSalud, evidenciando que el objetivo de interoperabilidad del RENHICE se encontraba rezagado. Posteriormente, Arrué Pajares y Vargas Rioja (2022) implementaron un HIS interoperable basado en HL7 v2 para centros de categoría II-1, demostrando la viabilidad técnica del estándar en el contexto peruano. Más recientemente, Mauricio et al. (2024) señalan que el acceso al EHR ha aumentado, pero persisten brechas significativas de conectividad e integración entre establecimientos, y Porras Gamarra (2024) recomienda la adopción de FHIR en las HCE del país basándose en su experiencia de implementación de interoperabilidad HL7 FHIR y openEHR en Cataluña.

### Fundamentación teórica

**Niveles de interoperabilidad.** La Healthcare Information and Management Systems Society (HIMSS) propone cuatro niveles de interoperabilidad: (1) fundacional, que establece los requisitos de interconexión para que un sistema envíe datos a otro; (2) estructural, que define el formato y organización del intercambio de datos; (3) semántico, que asegura que los datos intercambiados sean interpretados con el mismo significado por los sistemas emisor y receptor; y (4) organizacional, que incluye políticas, aspectos sociales y legales que facilitan la comunicación segura y oportuna de datos (Amar et al., 2024). La OPS (2024) sintetiza que para lograr la interoperabilidad deben resolverse la interoperabilidad técnica (transferencia fiable) y la interoperabilidad semántica (comprensión mutua).

**HL7 FHIR.** FHIR adopta un enfoque modular donde la información granular se representa como entidades modulares independientes llamadas "Resources" (recursos). Pimenta et al. (2023) describen cada recurso como un "ladrillo Lego®" de información sanitaria: múltiples recursos FHIR se combinan para formar mensajes con datos del paciente o para construir un EHR completo. Estos recursos pueden utilizarse solos, extenderse o acoplarse con otros para cubrir la gran mayoría de casos de uso clínico, superando la impredecibilidad inherente del sector salud sin incrementar costos y complejidad progresivamente. Las APIs RESTful y los servicios web generan, gestionan y distribuyen estos recursos (Pimenta et al., 2023).

**Perfiles e Guías de Implementación FHIR.** FHIR puede adaptarse a diferentes casos de uso mediante la creación de perfiles (profiles), donde los tipos de recursos base se modifican. La descripción general de cómo usar FHIR para un caso de uso se proporciona mediante una Guía de Implementación (IG). Kramer y Moesel (2023) señalan que la comunidad FHIR ha creado cientos de IGs y miles de perfiles, utilizando varias versiones de FHIR, y que aplicaciones que siguen diferentes IGs pueden no ser capaces de interoperar. Estos autores propusieron el método FHIR Interoperability Table (FHIT) para evaluar la interoperabilidad entre clientes y servidores que soportan diferentes recursos, perfiles y versiones.

**Modelos de datos clínicos y FHIR.** Tabari et al. (2024) identificaron que los modelos de datos FHIR se clasifican en dinámicos (basados en pipelines de transformación) y estáticos (estructuras de datos predefinidas). Los casos de uso clínicos cubren enfermedades crónicas, COVID-19 e infecciosas, investigación oncológica, cuidados agudos/intensivos y notas médicas generales. La implementación de modelado FHIR para datos de EHR facilita la integración y transmisión de datos, avanzando en investigación traslacional y fenotipado.

**Intercambio de información en salud (HIE).** Las organizaciones de intercambio de información sanitaria (HIOs) promueven el intercambio seguro de información entre hospitales, proveedores, organizaciones comunitarias y autoridades de salud pública. Richwine et al. (2025) encontraron que la participación en una HIO se asocia significativamente con mayor intercambio clínico, reportes de salud pública e intercambio de datos sobre necesidades sociales. Sin embargo, las HIOs son solo una vía de intercambio entre varias alternativas disponibles.

**Arquitecturas federadas.** Raab et al. (2023) proponen espacios de datos de salud personal federados, una arquitectura que almacena datos de salud en dispositivos personales en lugar de silos de datos centralizados, poniendo al ciudadano en el centro. Adelusi et al. (2025) demostraron que un framework federado basado en FHIR reduce significativamente el riesgo de brechas de datos al no transferir datos crudos. Este enfoque es particularmente relevante para redes de múltiples hospitales con plataformas EHR heterogéneas.

**Blockchain en interoperabilidad de EHR.** Anand y Sadhna (2023), mediante análisis bibliométrico, establecen que la interoperabilidad de datos y el intercambio electrónico de datos se introdujeron en el campo de EHR en 2020, infiriendo que la interoperabilidad de datos es un dominio relativamente nuevo. El mapeo temático sugiere que la “interoperabilidad” de EHR está bien desarrollada y es importante para la estructura del campo de investigación. Mauricio et al. (2024) demostraron la viabilidad de combinar blockchain con FHIR para garantizar seguridad y privacidad en el intercambio de EHR en Perú.

### Marco conceptual

El marco conceptual de la presente investigación articula tres dimensiones complementarias:

**Dimensión normativa-institucional:** Comprende el marco regulatorio peruano (IEDS, RNIEDS, PIDESALUD) que establece los lineamientos técnicos y operativos para la interoperabilidad en el sector salud del MINSA, así como la Ley N° 30024 que crea el RENHICE (Bayona Castañeda, 2019). Se alinea con el contexto internacional descrito por Holmgren et al. (2023), quienes destacan que la priorización gubernamental del intercambio de datos es un factor común en los marcos exitosos.

**Dimensión técnica-semántica:** Integra los estándares de intercambio (HL7 FHIR, CDA/CCD), codificación clínica (CIE-10, CPMS, SNOMED-CT, LOINC), y los niveles de interoperabilidad propuestos por HIMSS. Bossenko et al. (2024) demuestran que la transformación de CDA a FHIR mediante herramientas visuales permite a expertos del dominio con mínimas habilidades técnicas especificar y validar reglas de transformación de datos.

**Dimensión de evaluación de calidad:** Define los indicadores de desempeño (completitud, codificación, duplicidad, trazabilidad, continuidad) que permiten medir el impacto de la intervención. Liu et al. (2023) demostraron que la sustitución de gateways por servidores FHIR reduce efectivamente el tiempo y costo de conversión, mientras que Adelusi et al. (2025) validaron métricas de latencia, integridad y escalabilidad en frameworks federados.

## Definición de términos básicos

- **API RESTful:** Interfaz de programación de aplicaciones que sigue los principios de la arquitectura REST (Representational State Transfer), permitiendo la comunicación entre sistemas mediante operaciones HTTP estándar (GET, POST, PUT, DELETE). En el contexto de FHIR, las APIs RESTful constituyen el mecanismo principal para crear, leer, actualizar y eliminar recursos clínicos de forma interoperable (Pimenta et al., 2023).

- **CDA (Clinical Document Architecture):** Estándar de HL7 que define la estructura y semántica de documentos clínicos para su intercambio electrónico. CDA utiliza XML para representar documentos como resúmenes de alta, notas de evolución y reportes de laboratorio, proporcionando interoperabilidad documental entre sistemas de información en salud (Bossenko et al., 2024).

- **CIE-10 (Clasificación Internacional de Enfermedades, 10.ª revisión):** Sistema de codificación desarrollado por la Organización Mundial de la Salud para clasificar diagnósticos y causas de mortalidad. En el contexto del MINSA, su uso correcto es obligatorio para la codificación de diagnósticos en historias clínicas electrónicas y constituye un indicador clave de calidad de datos (Vorisek et al., 2022).

- **CPMS (Catálogo de Procedimientos Médicos y Sanitarios):** Catálogo normativo utilizado en el sistema de salud peruano para la codificación estandarizada de procedimientos médicos y sanitarios realizados en los establecimientos del MINSA. Su correcta aplicación facilita la validación de prestaciones por parte del SIS.

- **e-Qhali:** Sistema de información de historia clínica electrónica propuesto por el MINSA como estándar para el primer y segundo nivel de atención de las IPRESS en Perú, basado en la arquitectura de interoperabilidad HL7 (Bayona Castañeda, 2019).

- **EHR (Electronic Health Record):** Registro electrónico de salud; repositorio digital longitudinal de la información de salud de un paciente, que puede ser compartido entre diferentes establecimientos y proveedores de atención. A diferencia del EMR (Electronic Medical Record), que es propio de una institución, el EHR está diseñado para ser interoperable (Mauricio et al., 2024).

- **FHIR (Fast Healthcare Interoperability Resources):** Estándar desarrollado por HL7 International para el intercambio electrónico de información de salud. FHIR adopta un enfoque modular basado en recursos independientes — unidades mínimas de información clínica como Patient, Observation y Condition — que se combinan para representar datos clínicos complejos. Utiliza tecnologías web modernas (REST, JSON, XML, OAuth) para facilitar la implementación (Pimenta et al., 2023; Tabari et al., 2024).

- **Guía de Implementación (Implementation Guide - IG):** Documento que describe cómo utilizar FHIR para un caso de uso específico, incluyendo perfiles, extensiones y reglas de validación. Diferentes IGs pueden definir restricciones distintas sobre los mismos recursos FHIR, lo que puede generar desafíos de interoperabilidad entre sistemas que siguen guías diferentes (Kramer y Moesel, 2023).

- **HIE (Health Information Exchange):** Intercambio de información de salud; proceso mediante el cual se comparte electrónicamente información clínica entre organizaciones de salud. Las HIOs (Health Information Organizations) son entidades que facilitan y gobiernan este intercambio a nivel regional o nacional (Richwine et al., 2025).

- **HIS (Hospital Information System):** Sistema de información hospitalario que gestiona los datos administrativos y clínicos de un centro de salud, incluyendo finanzas, recursos humanos, citas, hospitalización y servicios complementarios. Arrué Pajares y Vargas Rioja (2022) desarrollaron un HIS interoperable basado en HL7 para centros de categoría II-1 o superior en Perú.

- **HL7 (Health Level Seven International):** Organización internacional que desarrolla estándares para el intercambio, integración, compartición y recuperación de información electrónica de salud. Su nombre se refiere al nivel 7 (aplicación) del modelo OSI, donde opera la comunicación de datos clínicos (Amar et al., 2024).

- **IEDS (Infraestructura de Estándares de Datos en Salud):** Marco normativo peruano establecido por la RM N° 1104-2018-MINSA que define los estándares técnicos para la representación, almacenamiento e intercambio de datos de salud entre los establecimientos del sistema público peruano.

- **Interoperabilidad en salud:** Capacidad de diferentes sistemas de tecnología de la información para comunicar e intercambiar datos con exactitud, efectividad y consistencia, y para usar la información que ha sido intercambiada. HIMSS distingue cuatro niveles: fundacional, estructural, semántico y organizacional (Amar et al., 2024; OPS, 2024).

- **Interoperabilidad semántica:** Nivel de interoperabilidad que asegura que los datos intercambiados entre sistemas sean interpretados con el mismo significado clínico por el sistema emisor y el receptor, mediante el uso de terminologías y codificaciones estandarizadas como SNOMED-CT, LOINC y CIE-10 (Torab-Miandoab et al., 2023). Porras Gamarra (2024) demostró la viabilidad de combinar interoperabilidad sintáctica (HL7 FHIR) con semántica (openEHR) en un contexto real de salud.

- **openEHR:** Estándar abierto de interoperabilidad semántica que utiliza arquetipos y plantillas para el modelado y persistencia de información clínica, permitiendo que los datos sean estructurados de forma independiente del software. Porras Gamarra (2024) lo complementó con HL7 FHIR en el proyecto M-Connecta.

- **RENHICE (Registro Nacional de Historias Clínicas Electrónicas):** Registro creado por la Ley N° 30024 del Perú que tiene como objetivo garantizar el acceso y disponibilidad de las historias clínicas electrónicas a nivel nacional, promoviendo la interoperabilidad entre las IPRESS públicas y privadas (Bayona Castañeda, 2019).

- **PIDESALUD (Plataforma de Interoperabilidad de Datos Estándares de Salud):** Plataforma normada por la RM N° 1193-2019-MINSA que establece los mecanismos técnicos para la interoperabilidad de datos de salud entre los establecimientos del MINSA y otras entidades del sector salud peruano.

- **Recurso FHIR:** Unidad modular básica de información en el estándar FHIR, descrita metafóricamente como un "ladrillo Lego®" de información sanitaria. Cada recurso representa un concepto clínico o administrativo discreto (Patient, Encounter, Observation, Condition, Procedure, entre otros) y puede utilizarse de forma independiente o combinada (Pimenta et al., 2023).

- **RNIEDS (Red Nacional de Interoperabilidad en Datos de Salud):** Red normada por la RM N° 464-2019-MINSA que define la arquitectura de conectividad e intercambio de datos estandarizados entre los sistemas de información de los establecimientos de salud del MINSA a nivel nacional.

- **SIS (Seguro Integral de Salud):** Organismo público del sector salud peruano que administra el aseguramiento en salud de la población en situación de vulnerabilidad, financiando prestaciones en los establecimientos del MINSA. La validación oportuna de atenciones por el SIS requiere registros clínicos completos y correctamente codificados.

# Capítulo III: Hipótesis y variables

## Hipótesis

### Hipótesis general

La implementación de un modelo de interoperabilidad basado en HL7 FHIR mejora significativamente la gestión de historias clínicas de pacientes SIS en centros de salud del MINSA en Perú, evidenciado por la mejora de los indicadores de completitud, codificación, duplicidad, tiempo de validación, continuidad de atención y trazabilidad.

### Hipótesis específicas

- **HE1:** El diagnóstico sistemático del cumplimiento de estándares de interoperabilidad (RNIEDS, PIDESALUD, HL7, CIE-10, CPMS) permite identificar brechas críticas cuantificables en la gestión de historias clínicas de los centros de salud MINSA del ámbito SIS.

- **HE2:** La implementación de una capa piloto de integración basada en HL7 FHIR produce una mejora estadísticamente significativa en los indicadores de calidad de gestión de historias clínicas (completitud, codificación CIE-10/CPMS, duplicidad de pacientes/exámenes, tiempo de validación SIS) respecto a la línea base.

- **HE3:** El modelo de interoperabilidad implementado mejora la continuidad de la atención y la trazabilidad de accesos en las historias clínicas electrónicas entre establecimientos de salud.

- **HE4:** Los lineamientos técnicos y operativos derivados de la experiencia piloto son replicables para la escalabilidad del modelo en otros establecimientos de salud del MINSA.

## Operacionalización de variables

### Variable independiente: Modelo de interoperabilidad basado en HL7 FHIR

Se define como el conjunto integrado de componentes técnicos, normativos y operativos que, organizados en tres fases secuenciales (diagnóstico, implementación piloto y evaluación de impacto), buscan habilitar el intercambio estandarizado de datos clínicos entre sistemas de información en salud. En la **Fase 1 (Diagnóstico)**, se evalúa el nivel de cumplimiento de la arquitectura RNIEDS-PIDESALUD, el grado de adopción de estándares de intercambio (HL7/FHIR), el cumplimiento de codificación clínica (CIE-10, CPMS, catálogos IEDS), el estado de seguridad y trazabilidad, y la capacidad de infraestructura y conectividad. En la **Fase 2 (Implementación piloto)**, se desarrolla la capa de integración FHIR (recursos, perfiles, terminologías), el mapeo y transformación de datos locales al modelo FHIR, la implementación del servicio de intercambio piloto y la capacitación del personal operativo. En la **Fase 3 (Evaluación)**, se comparan los indicadores de calidad de gestión de HCE antes y después de la intervención.

### Variable dependiente: Calidad de gestión de historias clínicas de pacientes SIS

Se operacionaliza mediante ocho indicadores medidos antes y después de la implementación del modelo: (1) **completitud de HCE**, definida como el porcentaje de campos obligatorios completos en la historia clínica electrónica; (2) **codificación CIE-10**, porcentaje de diagnósticos correctamente codificados; (3) **codificación CPMS**, porcentaje de procedimientos correctamente codificados; (4) **duplicidad de pacientes**, tasa de registros duplicados por cada 1 000 atenciones; (5) **duplicidad de exámenes**, tasa de exámenes y procedimientos duplicados por cada 1 000 atenciones; (6) **tiempo de validación SIS**, tiempo promedio en horas desde la atención hasta la validación por el Seguro Integral de Salud; (7) **continuidad de atención**, porcentaje de HCE con trazabilidad verificable entre establecimientos; y (8) **trazabilidad de accesos**, porcentaje de registros con log completo de acceso y modificación. Los indicadores se obtienen por auditoría de registros, muestras de atenciones, bases de datos HIS, registros SIS, cruce de registros entre establecimientos y logs del sistema.

## Matriz de operacionalización de variables

| Variable | Definición conceptual | Definición operacional | Dimensiones | Indicadores | Escala de valoración | Instrumentos |
|---|---|---|---|---|---|---|
| Variable independiente: Modelo de interoperabilidad basado en HL7 FHIR | Conjunto integrado de componentes técnicos, normativos y operativos que habilitan el intercambio estandarizado de datos clínicos. | Implementación de tres fases: diagnóstico de brechas, capa de integración FHIR piloto y evaluación pre/post. | Diagnóstico | Nivel de cumplimiento RNIEDS-PIDESALUD; adopción de HL7/FHIR; codificación CIE-10/CPMS. | Nominal (cumple/no cumple) y de razón (% de cumplimiento). | Lista de chequeo normativo-técnico; auditoría de registros; pruebas de integración. |
| Variable independiente: Modelo de interoperabilidad basado en HL7 FHIR | Conjunto integrado de componentes técnicos, normativos y operativos que habilitan el intercambio estandarizado de datos clínicos. | Implementación de tres fases: diagnóstico de brechas, capa de integración FHIR piloto y evaluación pre/post. | Implementación piloto | Recursos FHIR mapeados; tasa de éxito de intercambio; perfiles y terminologías aplicados. | Nominal (cumple/no cumple) y de razón (% de cumplimiento). | Lista de chequeo normativo-técnico; auditoría de registros; pruebas de integración. |
| Variable independiente: Modelo de interoperabilidad basado en HL7 FHIR | Conjunto integrado de componentes técnicos, normativos y operativos que habilitan el intercambio estandarizado de datos clínicos. | Implementación de tres fases: diagnóstico de brechas, capa de integración FHIR piloto y evaluación pre/post. | Evaluación de impacto | Comparación pre/post de los 8 indicadores de calidad de HCE. | Nominal (cumple/no cumple) y de razón (% de cumplimiento). | Lista de chequeo normativo-técnico; auditoría de registros; pruebas de integración. |
| Variable dependiente: Calidad de gestión de historias clínicas de pacientes SIS | Grado de integridad, codificación, trazabilidad y continuidad de las HCE en establecimientos MINSA. | Medición pre y post intervención de 8 indicadores cuantitativos de calidad de HCE. | Integridad de datos | Completitud de HCE (% campos obligatorios); codificación CIE-10 (%); codificación CPMS (%). | De razón (%, tasa, horas). | Auditoría de registros; base de datos HIS; registros SIS; logs del sistema. |
| Variable dependiente: Calidad de gestión de historias clínicas de pacientes SIS | Grado de integridad, codificación, trazabilidad y continuidad de las HCE en establecimientos MINSA. | Medición pre y post intervención de 8 indicadores cuantitativos de calidad de HCE. | Duplicidad | Duplicidad de pacientes (tasa/1000); duplicidad de exámenes (tasa/1000). | De razón (%, tasa, horas). | Auditoría de registros; base de datos HIS; registros SIS; logs del sistema. |
| Variable dependiente: Calidad de gestión de historias clínicas de pacientes SIS | Grado de integridad, codificación, trazabilidad y continuidad de las HCE en establecimientos MINSA. | Medición pre y post intervención de 8 indicadores cuantitativos de calidad de HCE. | Eficiencia administrativa | Tiempo de validación SIS (horas promedio). | De razón (%, tasa, horas). | Auditoría de registros; base de datos HIS; registros SIS; logs del sistema. |
| Variable dependiente: Calidad de gestión de historias clínicas de pacientes SIS | Grado de integridad, codificación, trazabilidad y continuidad de las HCE en establecimientos MINSA. | Medición pre y post intervención de 8 indicadores cuantitativos de calidad de HCE. | Continuidad y trazabilidad | Continuidad de atención (% HCE con trazabilidad); trazabilidad de accesos (% registros con log completo). | De razón (%, tasa, horas). | Auditoría de registros; base de datos HIS; registros SIS; logs del sistema. |

: Tabla 1. Matriz de operacionalización de variables



# Capítulo IV: Metodología del estudio

## Enfoque, tipo y alcance de investigación

### Enfoque

La presente investigación adopta un enfoque mixto con predominancia cuantitativa y apoyo cualitativo. Según Hernández-Sampieri y Mendoza (2018), los métodos mixtos representan un conjunto de procesos sistemáticos que implican la recolección y el análisis de datos tanto cuantitativos como cualitativos, así como su integración y discusión conjunta, lo que permite lograr un mayor entendimiento del fenómeno bajo estudio. El componente cuantitativo predominante se justifica porque el estudio busca medir objetivamente los indicadores de calidad de gestión de historias clínicas antes y después de la intervención, mientras que el componente cualitativo complementario permite capturar las barreras organizacionales y de implementación que los datos numéricos no reflejan. Este enfoque es consistente con los estudios de referencia: Adelusi et al. (2025) utilizaron métricas cuantitativas de rendimiento y Liu et al. (2023) emplearon pruebas de rendimiento con Apache JMeter, complementados con análisis cualitativos de la experiencia de implementación.

### Tipo y alcance

La investigación es de tipo aplicada, pues busca resolver un problema práctico específico — la deficiente interoperabilidad de historias clínicas en centros de salud del MINSA — mediante la implementación de un modelo basado en HL7 FHIR. Según Hernández-Sampieri y Mendoza (2018), la investigación aplicada se orienta a resolver problemas de la práctica a través de la aplicación del conocimiento. El alcance es explicativo-propositivo: explicativo porque busca establecer relaciones causales entre la implementación del modelo FHIR (variable independiente) y la mejora en la calidad de gestión de historias clínicas (variable dependiente), y propositivo porque genera lineamientos de escalabilidad para otros establecimientos. Este alcance se alinea con estudios como el de Bossenko et al. (2024), que no solo implementaron sino que evaluaron el impacto de su herramienta de transformación CDA-FHIR.

## Diseño de la investigación

El diseño es pre-experimental del tipo pre-test/post-test con un solo grupo, representado esquemáticamente como: O₁ → X → O₂, donde O₁ es la medición de línea base (pre-test), X es la intervención (implementación de la capa de integración FHIR) y O₂ es la medición posterior (post-test). Este diseño fue seleccionado considerando las restricciones operativas del contexto MINSA, donde la asignación aleatoria de establecimientos a grupos de control no es viable. Según Hernández-Sampieri y Mendoza (2018), los diseños pre-experimentales son útiles como un primer acercamiento al problema de investigación en contextos donde no es posible aplicar diseños experimentales puros. El diseño contempla tres fases: (1) diagnóstico de brechas de interoperabilidad y levantamiento de línea base; (2) implementación piloto de la capa de integración basada en HL7 FHIR; y (3) evaluación de impacto mediante comparación de indicadores pre y post intervención. Este diseño por fases es coherente con las implementaciones graduales recomendadas por Heryawan et al. (2025) y Jayathissa y Hewapathrana (2024).

## Población y muestra

### Población

La población está constituida por los establecimientos de salud del MINSA del ámbito SIS en Perú, así como el conjunto de historias clínicas electrónicas y registros clínico-administrativos generados en dichos establecimientos. Según Hernández-Sampieri y Mendoza (2018), la población es el conjunto de todos los casos que concuerdan con determinadas especificaciones. En este caso, los criterios de inclusión son: (a) establecimientos del MINSA en Lima que atienden pacientes SIS, (b) que cuenten con algún sistema de registro electrónico de salud, y (c) que operen en al menos dos niveles de complejidad diferentes.

### Muestra

La muestra se definirá mediante muestreo no probabilístico por conveniencia, considerando al menos 2 o 3 establecimientos de diferentes niveles de complejidad en Lima, según disponibilidad de acceso institucional y calidad de datos. Hernández-Sampieri y Mendoza (2018) señalan que en las muestras no probabilísticas, la elección de los elementos no depende de la probabilidad sino de las características de la investigación, lo cual es apropiado cuando las restricciones operativas limitan la aleatorización. Para la auditoría de registros clínicos, se seleccionará una muestra representativa de historias clínicas por establecimiento, cuyo tamaño se determinará mediante cálculo estadístico con un nivel de confianza del 95% y un margen de error del 5%.

## Técnicas e instrumentos de recolección de datos

### Técnicas e instrumentos

Se emplearán las siguientes técnicas e instrumentos, seleccionados en función de los objetivos y las fases del diseño de investigación:

- **Revisión documental normativa y técnica:** Análisis sistemático del marco regulatorio (RM N° 1104-2018-MINSA, RM N° 464-2019-MINSA, RM N° 1193-2019-MINSA) y de la documentación técnica de los sistemas de información en los establecimientos seleccionados. Según Hernández-Sampieri y Mendoza (2018), la revisión documental permite obtener datos secundarios de fuentes institucionales que complementan la información primaria.
- **Lista de chequeo de cumplimiento normativo-técnico:** Instrumento estructurado con ítems dicotómicos (cumple/no cumple) que evalúa el grado de adopción de los estándares de interoperabilidad (RNIEDS, PIDESALUD, HL7, CIE-10, CPMS) en cada establecimiento.
- **Ficha de auditoría de registros clínico-administrativos:** Instrumento que permite medir los ocho indicadores de calidad de gestión de HCE (completitud, codificación CIE-10, codificación CPMS, duplicidad de pacientes, duplicidad de exámenes, tiempo de validación SIS, continuidad de atención y trazabilidad de accesos) en las mediciones pre y post intervención.
- **Entrevistas semiestructuradas:** Dirigidas a responsables de TI y áreas asistenciales de los establecimientos, con el objetivo de identificar barreras organizacionales, culturales y técnicas no capturables mediante los instrumentos cuantitativos.
- **Pruebas de integración técnica:** Conjunto de pruebas automatizadas para validar la interoperabilidad FHIR (envío/recepción de recursos, validación de perfiles, tiempos de respuesta), siguiendo el enfoque de pruebas de rendimiento empleado por Liu et al. (2023) y las métricas de Adelusi et al. (2025).

### Validez y confiabilidad

La **validez de contenido** de los instrumentos (lista de chequeo de cumplimiento normativo-técnico y ficha de auditoría de registros clínicos) se asegurará mediante juicio de expertos: al menos tres especialistas en informática en salud, interoperabilidad o gestión de HCE evaluarán la pertinencia, claridad y suficiencia de cada ítem utilizando el coeficiente de concordancia V de Aiken, requiriendo un valor ≥ 0.80 para su aceptación. La **validez de constructo** se sustenta en que los indicadores derivan de estándares reconocidos internacionalmente (HL7 FHIR, CIE-10, CPMS) y del marco normativo nacional (RM N° 1104-2018-MINSA, RM N° 464-2019-MINSA), lo cual garantiza la correspondencia entre los indicadores medidos y los conceptos teóricos de interoperabilidad y calidad de gestión de HCE. La **confiabilidad** de los indicadores cuantitativos se evaluará mediante consistencia interna: para los ítems dicotómicos de la lista de chequeo se utilizará el coeficiente KR-20, y para las escalas de los ítems de auditoría se empleará el coeficiente alfa de Cronbach, esperando valores ≥ 0.70 en ambos casos. Adicionalmente, se realizará una prueba piloto en un establecimiento no incluido en la muestra final para calibrar los instrumentos.

### Procedimiento de recolección de datos

La recolección de datos se ejecutará en tres etapas alineadas con las fases del diseño de investigación:

**Etapa 1 — Diagnóstico (pre-test).** Se aplicará la lista de chequeo de cumplimiento normativo-técnico en cada establecimiento seleccionado, complementada con revisión documental de normativas institucionales. Simultáneamente, se levantará la línea base de los ocho indicadores de calidad de gestión de HCE mediante auditoría de una muestra representativa de registros clínico-administrativos (historias clínicas, atenciones SIS, logs de sistema). Se realizarán entrevistas semiestructuradas a responsables de TI y áreas asistenciales para identificar barreras organizacionales. Los datos cuantitativos se extraerán de las bases de datos HIS y registros SIS con autorización institucional.

**Etapa 2 — Implementación piloto.** Se registrarán los parámetros de configuración de la capa de integración FHIR (recursos mapeados, perfiles utilizados, terminologías aplicadas) y los resultados de las pruebas de integración técnica (tasa de éxito en envío/recepción de recursos, errores de validación, tiempos de respuesta). Se documentarán las actividades de capacitación y las incidencias detectadas durante la operación piloto.

**Etapa 3 — Evaluación (post-test).** Transcurrido un período de operación suficiente (mínimo cuatro semanas), se repetirá la medición de los ocho indicadores sobre una muestra equivalente de registros, utilizando los mismos instrumentos y criterios de la línea base. Las mediciones pre y post se compilarán en una base de datos anonimizada para su análisis estadístico.

## Técnicas de análisis de datos

El análisis de datos se realizará en dos vertientes, de acuerdo con el enfoque mixto de la investigación:

**Análisis cuantitativo.** Los datos de los ocho indicadores de calidad de gestión de HCE se procesarán con estadística descriptiva (media, mediana, desviación estándar, porcentajes) e inferencial. Para la comparación pre-post intervención, se verificará la normalidad de las distribuciones mediante la prueba de Shapiro-Wilk. En caso de distribuciones normales, se aplicará la prueba t de Student para muestras relacionadas; en caso contrario, se utilizará la prueba no paramétrica de rangos con signo de Wilcoxon (Hernández-Sampieri y Mendoza, 2018). El nivel de significancia se fijará en α = 0.05. Se construirá un índice compuesto de cumplimiento de interoperabilidad que integre los resultados de la lista de chequeo normativo-técnico. Los datos se procesarán con software estadístico SPSS o R.

**Análisis cualitativo.** La información obtenida de las entrevistas semiestructuradas se analizará mediante categorización temática, identificando patrones recurrentes sobre barreras organizacionales, técnicas y culturales para la implementación de interoperabilidad FHIR. Los hallazgos cualitativos se triangularán con los resultados cuantitativos para fortalecer la validez de las conclusiones.

# Capítulo V: Aspectos administrativos

## Presupuesto

A continuación se detalla el presupuesto estimado para la ejecución de la investigación, organizado por categorías de gasto:

| N° | Descripción | Cantidad | Costo unitario (S/) | Costo total (S/) |
|---|---|---:|---:|---:|
|  | **Recursos humanos** |  |  |  |
| 1 | Asesor estadístico | 1 | 1500.00 | 1500.00 |
| 2 | Apoyo técnico en implementación FHIR | 1 | 2000.00 | 2000.00 |
| 3 | Juicio de expertos (validación de instrumentos) | 3 | 300.00 | 900.00 |
|  | **Recursos tecnológicos** |  |  |  |
| 4 | Servidor HAPI-FHIR en nube (6 meses) | 6 | 150.00 | 900.00 |
| 5 | Licencia de software estadístico (SPSS/R) | 1 | 500.00 | 500.00 |
| 6 | Herramientas de prueba de integración (JMeter, Postman) | 1 | 0.00 | 0.00 |
|  | **Recursos logísticos** |  |  |  |
| 7 | Movilidad y viáticos para visitas a establecimientos | 12 | 80.00 | 960.00 |
| 8 | Material de impresión y papelería | 1 | 200.00 | 200.00 |
| 9 | Empastado y encuadernación de tesis | 5 | 50.00 | 250.00 |
|  | **Otros gastos** |  |  |  |
| 10 | Imprevistos (10% del total) | 1 | 721.00 | 721.00 |
|  | **TOTAL** |  |  | **7931.00** |

: Tabla 2. Presupuesto estimado de la investigación

**Fuente de financiamiento:** Autofinanciado por el investigador.

## Cronograma de actividades

El siguiente cronograma presenta la distribución temporal de las actividades de la investigación a lo largo de seis meses:

| N° | Actividad | Mes 1 | Mes 2 | Mes 3 | Mes 4 | Mes 5 | Mes 6 |
|---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | Revisión y aprobación del proyecto de tesis | X |  |  |  |  |  |
| 2 | Gestión de permisos institucionales (MINSA) | X | X |  |  |  |  |
| 3 | Validación de instrumentos (juicio de expertos) | X |  |  |  |  |  |
| 4 | Fase 1: Diagnóstico de brechas y línea base (pre-test) |  | X | X |  |  |  |
| 5 | Fase 2: Diseño e implementación de capa FHIR piloto |  |  | X | X |  |  |
| 6 | Capacitación del personal operativo |  |  |  | X |  |  |
| 7 | Operación piloto (mínimo 4 semanas) |  |  |  | X | X |  |
| 8 | Fase 3: Evaluación de impacto (post-test) |  |  |  |  | X |  |
| 9 | Análisis estadístico e interpretación de resultados |  |  |  |  | X | X |
| 10 | Redacción del informe final de tesis |  |  |  |  |  | X |
| 11 | Sustentación de tesis |  |  |  |  |  | X |

: Tabla 3. Cronograma de actividades

\newpage

# Referencias

- Pimenta, N., Chaves, A., Sousa, R., Abelha, A., & Peixoto, H. (2023). Interoperability of Clinical Data through FHIR: A review. *Procedia Computer Science, 220*, 856-861. https://doi.org/10.1016/j.procs.2023.03.115
- Raab, R., Kuderle, A., Zakreuskaya, A., Stern, A. D., Klucken, J., Kaissis, G., Rueckert, D., Boll, S., Eils, R., Wagener, H., & Eskofier, B. M. (2023). Federated electronic health records for the European Health Data Space. *The Lancet Digital Health, 5*(11), e840-e847. https://doi.org/10.1016/S2589-7500(23)00156-5
- Holmgren, A. J., Esdar, M., Husers, J., & Coutinho-Almeida, J. (2023). Health Information Exchange: Understanding the Policy Landscape and Future of Data Interoperability. *Yearbook of Medical Informatics, 32*(01), 184-194. https://doi.org/10.1055/s-0043-1768719
- Richwine, C., Strawley, C., Chang, W., & Everson, J. (2025). Assessing the value of health information exchange organizations to hospital interoperability. *Health Affairs Scholar, 3*(7). https://doi.org/10.1093/haschl/qxaf133
- Monsen, K. A., Heermann, L., & Dunn-Lopez, K. (2023). FHIR-up! Advancing knowledge from clinical data through application of standardized nursing terminologies within HL7 FHIR. *Journal of the American Medical Informatics Association, 30*(11), 1858-1864. https://doi.org/10.1093/jamia/ocad131
- Kramer, M. A., & Moesel, C. (2023). Interoperability with multiple Fast Healthcare Interoperability Resources (FHIR) profiles and versions. *JAMIA Open, 6*(1). https://doi.org/10.1093/jamiaopen/ooad001
- Torab-Miandoab, A., Samad-Soltani, T., Jodati, A., & Rezaei-Hachesu, P. (2023). Interoperability of heterogeneous health information systems: A systematic literature review. *BMC Medical Informatics and Decision Making, 23*(1). https://doi.org/10.1186/s12911-023-02115-5
- Surisetty, L. S. (2026). End-to-End Clinical Data Interoperability: A Practical Implementation Blueprint Using HL7, FHIR, CCD, and EHR Integration Standards. *International Journal of Multidisciplinary and Scientific Emerging ResearcH, 14*(1). https://doi.org/10.15662/ijmserh.2026.1401004
- Vorisek, C. N., Lehne, M., Klopfenstein, S. A. I., Mayer, P. J., Bartschke, A., Haese, T., & Thun, S. (2022). Fast Healthcare Interoperability Resources (FHIR) for Interoperability in Health Research: Systematic Review. *JMIR Medical Informatics, 10*(7), e35724. https://doi.org/10.2196/35724
- Amar, F., April, A., & Abran, A. (2024). Electronic Health Record and Semantic Issues Using Fast Healthcare Interoperability Resources: Systematic Mapping Review. *Journal of Medical Internet Research, 26*, e45209. https://doi.org/10.2196/45209
- Heryawan, L., Mori, Y., Yamamoto, G., Kume, N., Lazuardi, L., Fuad, A., & Kuroda, T. (2025). Fast Healthcare Interoperability Resources (FHIR)-Based Interoperability Design in Indonesia: Content Analysis of Developer Hub's Social Networking Service. *JMIR Formative Research, 9*, e51270-e51270. https://doi.org/10.2196/51270
- Tabari, P., Costagliola, G., De Rosa, M., & Boeker, M. (2024). State-of-the-Art Fast Healthcare Interoperability Resources (FHIR)-Based Data Model and Structure Implementations: Systematic Scoping Review. *JMIR Medical Informatics, 12*, e58445. https://doi.org/10.2196/58445
- Bossenko, I., Randmaa, R., Piho, G., & Ross, P. (2024). Interoperability of health data using FHIR Mapping Language: Transforming HL7 CDA to FHIR with reusable visual components. *Frontiers in Digital Health, 6*. https://doi.org/10.3389/fdgth.2024.1480600
- Liu, T., Lee, H., & Wu, F. (2023). Building an Electronic Medical Record System Exchanged in FHIR Format and Its Visual Presentation. *Healthcare, 11*(17), 2410. https://doi.org/10.3390/healthcare11172410
- Mauricio, D., Llanos-Colchado, P. C., Cutipa-Salazar, L. S., Castañeda, P., Chuquimbalqui-Maslucan, R., Rojas-Mezarina, L., & Castillo-Sequera, J. L. (2024). Electronic Health Record Interoperability System in Peru Using Blockchain. *International Journal of Online and Biomedical Engineering (iJOE), 20*(03), 136-153. https://doi.org/10.3991/ijoe.v20i03.44507
- Anand, G., & Sadhna, D. (2023). Electronic health record interoperability using FHIR and blockchain: A bibliometric analysis and future perspective. *Perspectives in Clinical Research, 14*(4), 161-166. https://doi.org/10.4103/picr.picr_272_22
- Adelusi, B. S., Osamika, D., Chinyeaka Kelvin-Agwu, M., Mustapha, A. Y., Forkuo, A. Y., & Ikhalea, N. (2025). A Federated Interoperability Framework for Seamless Health Data Exchange Using FHIR Standards Across Multi-Hospital Systems. *Engineering and Technology Journal, 10*(05). https://doi.org/10.47191/etj/v10i05.03
- Jayathissa, P., & Hewapathrana, R. (2024). HAPI-FHIR Server Implementation to Enhancing Interoperability among Primary Care Health Information Systems in Sri Lanka: Review of the Technical Use Case. *European Modern Studies Journal, 7*(6), 225-241. https://doi.org/10.59573/emsj.7(6).2023.23
- Hernández-Sampieri, R., & Mendoza, C. P. (2018). *Metodología de la investigación: las rutas cuantitativa, cualitativa y mixta*. McGraw-Hill Education.
- Organización Panamericana de la Salud (OPS). (2024). *Guía de implementación de interoperabilidad de sistemas de información en salud*. OPS.
- Arrué Pajares, S. D., & Vargas Rioja, C. A. (2022). *Implementación de un Sistema de Información Hospitalario (HIS) interoperable basado en HL7 para un Centro Médico de categoría II-1 o superior* [Tesis de pregrado, Pontificia Universidad Católica del Perú]. Repositorio PUCP.
- Bayona Castañeda, L. (2019). *Radiografía de la Historia Clínica en Perú* [Trabajo de fin de máster, Universitat Politècnica de València]. RiuNet UPV.
- Porras Gamarra, H. J. (2024). *Implementación de un sistema de interoperabilidad de información clínica basado en los estándares internacionales HL7 FHIR y openEHR* [Trabajo de suficiencia profesional, Universidad Nacional Federico Villarreal]. Repositorio UNFV.

\newpage

# Anexos
