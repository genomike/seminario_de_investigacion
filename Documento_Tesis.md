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
**"MODELO DE INTEROPERABILIDAD BASADO EN HL7 FHIR PARA MEJORAR EL INTERCAMBIO DE INFORMACIÓN CLÍNICA EN CENTROS DE SALUD DEL MINSA - PERÚ"**
:::

::: {custom-style="Portada-Centrado"}
&nbsp;
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
&nbsp;
:::

::: {custom-style="Portada-Centrado"}
PARA OPTAR EL GRADO ACADÉMICO DE:
:::

::: {custom-style="Portada-Centrado"}
**MAESTRO(A) EN INGENIERÍA DE SOFTWARE**
:::

::: {custom-style="Portada-Centrado"}
&nbsp;
:::

::: {custom-style="Portada-Centrado"}
**LIMA**

**2026**
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

La presente investigación propone un modelo de interoperabilidad basado en HL7 FHIR para mejorar el intercambio de información clínica de pacientes atendidos en centros de salud del MINSA en Perú. El estudio se estructura en tres fases: diagnóstico de brechas de interoperabilidad, implementación piloto de una capa de integración FHIR y evaluación del impacto mediante comparación pre y post intervención. En la fase diagnóstica se analiza el cumplimiento de estándares y componentes clave (RNIEDS, PIDESALUD, HL7, CIE-10 y CPMS), así como la calidad de los registros clínicos. En la fase de implementación se plantea el diseño y despliegue de servicios de integración orientados a mejorar completitud, codificación, trazabilidad y continuidad de atención. En la fase de evaluación se utilizan indicadores de desempeño para medir cambios en la calidad del intercambio de información clínica. Los resultados esperados incluyen reducción de duplicidad de registros, mejora en codificación clínica, disminución de tiempos de validación y fortalecimiento de la continuidad asistencial, aportando lineamientos de escalabilidad para otros establecimientos del MINSA.

**Palabras claves:** Interoperabilidad en salud, Historia clínica electrónica, HL7 FHIR, MINSA, gestión pública de salud

\newpage

# Abstract

This research proposes an interoperability model based on HL7 FHIR to improve clinical information exchange for patients treated in MINSA health centers in Peru. The study is structured into three phases: interoperability gap diagnosis, pilot implementation of an FHIR integration layer, and impact evaluation through pre- and post-intervention comparison. The diagnostic phase assesses compliance with key standards and components (RNIEDS, PIDESALUD, HL7, ICD-10, and CPMS), as well as clinical data quality. The implementation phase focuses on the design and deployment of integration services aimed at improving record completeness, coding quality, traceability, and continuity of care. The evaluation phase uses performance indicators to measure changes in clinical information exchange quality. Expected outcomes include reduced record duplication, improved clinical coding, shorter administrative validation times, and stronger care continuity, providing scalability guidelines for other MINSA facilities.

**Keywords:** Health interoperability, Electronic health records, HL7 FHIR, MINSA, public health governance

\newpage

# Introducción

La interoperabilidad en salud constituye un factor crítico para garantizar la continuidad asistencial, la seguridad del paciente y la eficiencia administrativa en los sistemas públicos de atención. A nivel global, la fragmentación de los sistemas de información sanitarios ha sido identificada como un obstáculo persistente para el intercambio efectivo de datos clínicos (Torab-Miandoab et al., 2023; Holmgren et al., 2023). Según Vorisek et al. (2022), HL7 FHIR se ha consolidado como el estándar de referencia para habilitar la interoperabilidad, con un crecimiento sostenido en su adopción para investigación clínica y gestión de datos de salud.

En el contexto peruano, el Ministerio de Salud (MINSA) ha emitido un marco normativo específico —la Infraestructura de Estándares de Datos en Salud (IEDS), la Red Nacional de Interoperabilidad en Datos de Salud (RNIEDS) y la Plataforma de Interoperabilidad de Datos Estándares de Salud (PIDESALUD)— orientado a estandarizar el intercambio de información entre establecimientos del MINSA, articulando procesos asistenciales y administrativos financiados por el SIS cuando corresponde. Sin embargo, la implementación operativa de estas normativas permanece incompleta y heterogénea, como documentan Mauricio et al. (2024) al señalar que en Perú no existe actualmente un sistema integrado de historias clínicas electrónicas que permita compartir información automáticamente entre establecimientos.

Frente a este escenario, la presente investigación propone un modelo de interoperabilidad basado en HL7 FHIR que integra tres fases secuenciales: diagnóstico de brechas, implementación piloto de una capa de integración y evaluación de impacto mediante indicadores de calidad del intercambio de información clínica. El estudio se sustenta en evidencia científica reciente —incluyendo revisiones sistemáticas de Amar et al. (2024), Tabari et al. (2024) y Pimenta et al. (2023)— y en experiencias internacionales de implementación en Estonia (Bossenko et al., 2024), Indonesia (Heryawan et al., 2025) y Sri Lanka (Jayathissa y Hewapathrana, 2024).

El documento se estructura en cinco capítulos. El Capítulo I presenta el planteamiento del problema, los objetivos, la justificación y las limitaciones. El Capítulo II desarrolla el marco teórico, incluyendo antecedentes internacionales y nacionales, bases teóricas y la definición de términos. El Capítulo III formula las hipótesis y operacionaliza las variables. El Capítulo IV describe la metodología del estudio. El Capítulo V presenta los aspectos administrativos, incluyendo el presupuesto y el cronograma de actividades.

\newpage

# Capítulo I: Planteamiento del estudio

## 1.1. -> Planteamiento y formulación del problema

### 1.1.1.- Planteamiento del problema

Actualmente, en los centros de salud del Ministerio de Salud (MINSA) del Perú, los sistemas de gestión de historias clínicas operan con una interoperabilidad limitada debido a la ausencia de implementación sistemática de estándares internacionales como HL7 FHIR (Fast Healthcare Interoperability Resources). Esta condición genera fragmentación de la información clínica del paciente, afectando su integridad, calidad y continuidad en la atención.

En el ámbito global, la ausencia de una integración fluida de datos se reconoce como un obstáculo crítico para la digitalización de la salud. Pimenta et al. (2023) señalan que, sin una regulación uniforme, los establecimientos adoptan sistemas heterogéneos según criterios propios, produciendo registros segregados y fragmentación informacional. Por su parte, Torab-Miandoab et al. (2023) subrayan que esta desarticulación no solo reduce la calidad de la atención y desperdicia recursos financieros, sino que hace imperativa la adopción de estándares como HL7 FHIR, CDA y SNOMED-CT para lograr una integración efectiva.

El panorama peruano refleja esta problemática de manera crítica. Bayona Castañeda (2019) documenta que un paciente puede tener tantas historias clínicas como establecimientos visita, como resultado de un sistema segmentado y fragmentado. Arrué Pajares y Vargas Rioja (2022) señalan la ausencia de sistemas interoperables que optimicen la gestión de citas, camas y referencias. Mauricio et al. (2024) advierten que actualmente no existe un sistema integrado de historias clínicas electrónicas compartible entre establecimientos, lo que incrementa costos por exámenes duplicados y tiempos adicionales de gestión clínica. Porras Gamarra (2024), con experiencia directa en interoperabilidad europea, contrasta que, durante la pandemia, mientras Europa debatía sobre estándares de mensajería, en Perú se construían sistemas aislados sin planificación ni estándares.

Si bien el MINSA ha establecido un marco normativo para la interoperabilidad mediante la Infraestructura de Estándares de Datos en Salud (IEDS), la Red Nacional de Interoperabilidad en Datos de Salud (RNIEDS) y la Plataforma de Interoperabilidad de Datos Estándares de Salud (PIDESALUD), reguladas por la RM N° 1104-2018-MINSA, RM N° 464-2019-MINSA y RM N° 1193-2019-MINSA, su implementación no es uniforme. Como resultado, persisten brechas operativas concretas en los centros de salud del MINSA:

- **Completitud de registros clínicos:** Información incompleta en historias clínicas que impide una visión integral del paciente.
- **Inconsistencias en codificación clínica:** Uso heterogéneo de CIE-10 y CPMS, afectando el registro y la trazabilidad diagnóstica.
- **Duplicidad de información:** Múltiples registros de un mismo paciente y exámenes repetidos entre establecimientos.
- **Limitaciones en trazabilidad y continuidad:** Dificultad para dar seguimiento a la atención entre distintos niveles y redes de salud.

La Organización Panamericana de la Salud (OPS, 2024) define la interoperabilidad como la capacidad de diferentes sistemas para intercambiar datos con exactitud, efectividad y consistencia, distinguiendo entre interoperabilidad técnica (transferencia fiable) e interoperabilidad semántica (comprensión mutua de la información). HL7 FHIR emerge como el estándar internacional más prometedor para abordar ambas dimensiones, tal como evidencian Vorisek et al. (2022) en su revisión sobre usos de FHIR en investigación, y Holmgren et al. (2023) en el análisis de marcos de políticas de interoperabilidad en países con mayor madurez.

Esta evidencia se complementa con hallazgos recientes sobre gobernanza e implementación: Richwine et al. (2025) muestran que la participación institucional en organizaciones de intercambio (HIO) incrementa de forma significativa el intercambio clínico efectivo; Raab et al. (2023) plantean arquitecturas federadas orientadas al control ciudadano de datos en el EHDS; Pedrera-Jiménez et al. (2023) demuestran la viabilidad de enfoques agnósticos donde OpenEHR, ISO 13606 y FHIR coexisten por capas; y Chatterjee et al. (2022) validan, en prueba de concepto, que la combinación FHIR + SNOMED-CT reduce pérdidas semánticas en intercambio bidireccional.

A pesar de la existencia de la normativa y avances en estándares de interoperabilidad, no se evidencian propuestas aplicadas y evaluadas en el contexto de los centros de salud del MINSA que integren un modelo basado en HL7 FHIR alineado a la normativa nacional y que demuestren empíricamente mejoras en la calidad del intercambio de información clínica. Esta ausencia constituye una brecha tanto práctica como científica que limita la toma de decisiones basada en evidencia en procesos de transformación digital en salud.

Frente a este panorama, se requiere una propuesta de intervención fundamentada en la evidencia que permita:

1.- Diagnosticar las brechas de interoperabilidad con instrumentos validados.

2.- Implementar una capa de integración basada en HL7 FHIR alineada con los estándares internacionales y el marco normativo nacional.

3.- Evaluar sus efectos medibles en la calidad del intercambio de información clínica del paciente.

La presente investigación responde a esta necesidad integrando las tres fases en un modelo coherente y replicable.

### 1.1.2.- Formulación del problema

1.- *Problema general*

¿De qué manera un modelo de interoperabilidad basado en HL7 FHIR contribuye a mejorar el intercambio de información clínica en los centros de salud del MINSA del Perú, considerando las brechas de interoperabilidad existentes, los requerimientos técnicos y normativos, y los efectos medibles en la calidad del intercambio?

2.- *Problemas específicos*

- ¿Cuáles son las brechas de interoperabilidad actuales en los centros de salud del MINSA del Perú en cuanto a completitud, codificación, duplicidad y trazabilidad de la información clínica?
- ¿Cuáles son los requerimientos técnicos, funcionales y normativos que debe satisfacer un modelo de interoperabilidad basado en HL7 FHIR para ser compatible con la infraestructura existente y el marco regulatorio nacional (IEDS, RNIEDS, PIDESALUD)?
- ¿Cómo debe diseñarse e implementarse una capa de interoperabilidad basada en HL7 FHIR que integre sistemas heterogéneos en centros de salud del MINSA?
- ¿Cuál es el efecto de la implementación del modelo propuesto en indicadores de calidad del intercambio de información clínica (integridad, consistencia, disponibilidad y continuidad)?

## 1.2. -> Determinación de objetivos

### 1.2.1.- Objetivo general

Proponer un modelo de interoperabilidad basado en HL7 FHIR para mejorar el intercambio de información clínica en centros de salud del MINSA del Perú, mediante un proceso estructurado de diagnóstico de brechas, diseño e implementación de una capa de integración piloto, y evaluación de sus efectos en indicadores de calidad de la información.

### 1.2.2.- Objetivos específicos

- Diagnosticar las brechas de interoperabilidad en los centros de salud del MINSA del Perú, particularmente en las dimensiones de completitud de registros, consistencia en la codificación clínica (CIE-10, CPMS), duplicidad de información y trazabilidad de la atención.
- Diseñar e implementar una capa de integración piloto basada en HL7 FHIR que atienda las brechas de interoperabilidad identificadas en la fase diagnóstica, considerando los requerimientos técnicos y el marco normativo vigente (IEDS, RNIEDS, PIDESALUD).
- Evaluar el efecto del modelo de interoperabilidad implementado mediante un diseño pre-post intervención, a través de indicadores cuantitativos de integridad, consistencia, disponibilidad y continuidad de la información clínica intercambiada.
- Formular lineamientos técnicos y operativos para la escalabilidad del modelo de interoperabilidad propuesto, basados en los resultados de la implementación piloto y alineados con la infraestructura de estándares de datos en salud del MINSA.

## 1.3. -> Justificación e importancia del estudio

### 1.3.1.- Justificación teórica

Esta investigación aporta al campo de la interoperabilidad en el sector salud al incluir, en un marco analítico conjunto, los elementos estructurales, semánticos, tecnológicos y el análisis de impacto en la gestión de registros clínicos digitales. A través de un análisis minucioso de más de 70 estudios sobre FHIR y la interoperabilidad semántica, Amar et al. (2024) identificaron seis tipos de estrategias: mapeo (24,6%), servicios terminológicos (14,3%), enfoques con RDF/OWL (19%), mecanismos de anotación (14,3%), técnicas de aprendizaje automático y procesamiento del lenguaje natural (15,9%), y ontologías (11,9%). Sin embargo, subrayan la falta de estructuras que integren estas estrategias con la evaluación de impactos en contextos de operación específicos.

Por otro lado, Tabari et al. (2024), a través de una revisión comprensiva sobre modelos de datos en FHIR, sostienen que, aunque este estándar tiene un gran potencial para transformar, aún se necesitan ajustes para superar sus limitaciones y alcanzar implementaciones efectivas. El presente análisis aborda esta falta al conectar estándares internacionales (HL7 FHIR, HL7 CDA, DICOM) con el marco regulatorio local (RM N.° 1104-2018-MINSA, RM N.° 464-2019-MINSA, RM N.° 1193-2019-MINSA), generando perspectivas sobre su implementación práctica en sistemas públicos gestionados por el MINSA y financiados por el SIS.

Asimismo, Gaudet-Blavignac et al. (2021) proponen una estrategia semántica de tres pilares para uso secundario de datos en redes nacionales, mientras que Monsen et al. (2023) muestran que el uso de terminologías estandarizadas en FHIR incrementa la reutilización de datos clínicos para analítica y toma de decisiones. Estos aportes refuerzan la pertinencia de un modelo que no solo integre sistemas, sino que preserve significado clínico y habilite valor posterior del dato.

### 1.3.2.- Justificación metodológica

El enfoque metodológico está alineado a un proceso de trabajo organizado y dividido en tres fases fundamentales: detección de problemas, implementación experimental y evaluación de resultados. Este diseño está alineado con los métodos más comunes en estudios actuales del sector. Adelusi et al. (2025), evaluaron una arquitectura de interoperabilidad basada en FHIR, analizando aspectos como la velocidad de respuesta, la precisión de los datos y la escalabilidad, lo que resultó en más del 95% de exactitud en la captura de información y una reducción del 38% en los retrasos en comparación con las estructuras centralizadas tradicionales. Asimismo Liu et al. (2023), validaron un sistema de registros médicos electrónicos utilizando FHIR mediante pruebas de carga con Apache JMeter, demostrando que reemplazar gateways con servidores FHIR reduce significativamente los tiempos y costos asociados con la transformación de los datos.

La metodología que proponemos es un diseño pre-experimental con comparación pre-post intervención, el cual garantiza su aplicabilidad en otros entornos de atención médica, ya que especifica herramientas, parámetros, indicadores y métricas de rendimiento con total claridad. La comparación de datos antes y después de la intervención proporciona información empírica y sólida sobre la efectividad del modelo.

Adicionalmente, Mukhiya et al. (2021) evidencian que capas de interoperabilidad basadas en FHIR con interfaces flexibles (GraphQL) reducen acoplamiento entre sistemas heterogéneos, y Richwine et al. (2025) reportan que los mayores beneficios aparecen cuando la integración técnica se acompaña de mecanismos de gobernanza de intercambio. Esto respalda el enfoque metodológico del estudio, que combina diseño técnico de integración y evaluación operacional de resultados.

![Fases del enfoque metodológico](media/fases_metodologicas.png)

### 1.3.3.- Justificación social

La mejora de la interoperabilidad impacta directamente en la rapidez y eficiencia del servicio brindado a los usuarios de los establecimientos del MINSA, especialmente en poblaciones vulnerables con cobertura financiera del SIS. De acuerdo con Holmgren et al. (2023), una interoperabilidad eficiente puede frenar el aumento de los gastos en salud al disminuir el uso innecesario de servicios, además de aliviar la carga administrativa para los pacientes al permitir que sus datos los acompañen de manera clara a lo largo de su atención. De igual manera, Pimenta et al. (2023), argumentan que el tratamiento adecuado de un paciente solo se logra cuando los profesionales de la salud tienen acceso a la información más reciente y completa sobre datos personales y clínicos, siendo la interoperabilidad esencial para lograr una atención de calidad.

La OPS (2024) resalta que en el ámbito de la salud, la interoperabilidad posibilita que los sistemas de información crucen los límites organizacionales y fomenten la prestación de servicios eficaces, al proporcionar la información pertinente a los proveedores de atención para que puedan entender y atender la salud de los individuos y las comunidades. Contar con información clínica más completa, accesible y rastreable mejora la seguridad del paciente, disminuye la posibilidad de errores debido a información incompleta y promueve una atención más justa dentro del sistema público de salud en Perú, especialmente para las poblaciones más vulnerables.

En el plano nacional, la evidencia reciente también vincula madurez de historia clínica electrónica con resultados de gestión y atención: Esparza Morgan (2025) identifica asociación positiva entre uso de HCE única y mejora de la gestión de calidad hospitalaria, Arias Geronimo (2025) reporta relación significativa entre confiabilidad del registro electrónico y desempeño en servicios preventivos, y Morales-Camargo y Meneses-Claudio (2023) destacan efectos favorables de EMR en eficiencia y soporte a decisión clínica cuando existen condiciones de estandarización y capacitación.

## 1.4. -> Limitaciones de la presente investigación

### 1.4.1.- Disponibilidad y calidad de los datos

Los datasets clínicos administrativos del MINSA muestran carencias estructurales, inconsistencias en el significado y falta de estándares, lo que deteriora la exactitud del diagnóstico inicial de brechas entre un 15 y un 20% según las tasas de error en los analizadores preliminares. De acuerdo con lo expuesto por Torab-Miandoab et al. (2023), exploran este problema en su estudio de 45 sistemas EHR heredados.

- **Dominio de la propiedad (82% de los casos):** Los esquemas cerrados (por ejemplo, SQL personalizado en Oracle frente a PostgreSQL por cada hospital) obstaculizan un ETL uniforme, obligando a realizar mapeos manuales que dan como resultado una pérdida de precisión de hasta un 28% en los datos categóricos.
- **Diferencias entre instituciones:** La variabilidad en las convenciones de nombres (por ejemplo, "fiebre" frente a "fieb" en síntomas) aumenta la complejidad de la normalización, generando un sobrecosto de 3 a 5 veces más en el tiempo de preprocesamiento en comparación con conjuntos de datos nativos de FHIR.
- **Impacto medido:** La extracción uniforme no tiene éxito en el 62% de las consultas interinstitucionales sin ontologías puente, lo que coincide con las observaciones en los datos del MINSA (muestra piloto: 31% de registros con más del 10% de nulos).

**Estrategia de mitigación:** Se implementarán criterios de exclusión para registros que estén incompletos y se documentará el porcentaje de datos eliminados para clarificar el alcance real de la muestra estudiada.

### 1.4.2.- Acceso a fuentes de información

La obtención de autorizaciones para dumps o APIs de los sistemas del MINSA enfrenta retrasos regulatorios que suelen oscilar entre los 3 y 6 meses debido a revisiones de los comités de ética (IRB) y el cumplimiento con la Ley 29733 sobre Protección de Datos. Esto se ve agravado por limitaciones específicas como el control de velocidades (por ejemplo, 100 consultas por hora) o los permisos de solo lectura en los puntos finales de FHIR. Esta situación obstaculiza el proceso de incorporación de datos, especialmente en contextos con divisiones verticales entre aseguramiento (SIS) y prestación (MINSA/HIS).

Mauricio et al. (2024), describen de la siguiente manera la situación en el Perú en su encuesta realizada a 120 proveedores:

- **Cobertura de EHR insatisfactoria:** Apenas el 42% de las instalaciones en áreas urbanas y el 18% de las rurales cuentan con sistemas EHR operativos. En regiones como la sierra y la amazonía, un 65% aún depende de registros en papel o Excel, sin APIs disponibles.
- **Desigualdad entre zonas rurales y urbanas:** Las áreas rurales informan que el 72% de las interrupciones afectan la continuidad de la atención (por ejemplo, traslados entre hospitales sin un historial digital), con tiempos de espera de 48 a 72 horas para la conciliación manual de información.
- **Obstáculos técnicos:** La falta de estándares (solo el 22% tiene integraciones HL7/FHIR) obliga a utilizar soluciones alternativas como documentos PDF escaneados, lo que incrementa la tasa de errores en la entrada de datos al 35%.
- **Efectos medibles:** El 55% de los pacientes crónicos (como los de diabetes y tuberculosis) experimentan pérdida de datos durante las transiciones de atención, lo que se relaciona con un 28% de probabilidad adicional de readmisión debido a información incompleta.

Todo lo indicado anteriormente trae como consecuencia el retraso en la etapa de diagnóstico y las pruebas de integración. En la fase piloto, simular “inicios en frío” utilizando datos de reemplazo, pero subestima las latencias reales en conexiones de bajo ancho de banda.

**Estrategia de mitigación:** Se gestionarán los permisos institucionales desde la fase inicial del proyecto y se establecerán acuerdos de confidencialidad. En caso de restricciones, se utilizarán datos anonimizados o sintéticos para las pruebas técnicas con datasets sintéticos HHIMS (Jayathissa y Hewapathrana, 2024).

### 1.4.3.- Alcance geográfico

El análisis se concentra únicamente en los centros de salud del MINSA en Lima, lo que complica la posibilidad de extender los hallazgos a otras zonas del país, como la sierra o la selva. Esto ocurre debido a que cada área tiene sus propias metodologías y desafíos particulares. Según lo señalado por Holmgren et al. (2023), realizaron una evaluación de sistemas de salud en diferentes locaciones y observaron que las grandes ciudades (como Lima) disfrutan de un acceso adecuado a internet, cuentan con electricidad confiable y tienen equipos modernos. En cambio, las áreas rurales o remotas enfrentan cortes de energía frecuentes, conexiones lentas y utilizan tecnologías obsoletas o incluso papel.

Por esta razón, una solución que funcione bien en Lima podría no ser efectiva en Arequipa o Pucallpa. También ofrecen ejemplos en los que las iniciativas urbanas no tienen éxito en un 60% fuera de las ciudades, ya que no toman en cuenta estas variaciones.

En conclusión, cada región requiere adaptaciones, y lo que se evalúa en una sola ubicación no puede ser replicado fácilmente en otros lugares.

**Estrategia de mitigación:** Se elegirá a establecimientos que cuenten con al menos 2 o 3 niveles de complejidad para captar una variabilidad representativa y se establecerán directrices para facilitar la escalabilidad en futuras implementaciones en otras localidades.

### 1.4.4.- Limitaciones del modelo de interoperabilidad implementado

Kramer y Moesel (2023), muestran que las aplicaciones que se ajustan a distintas Guías de Implementación FHIR pueden no ser compatibles entre sí, y que la verificación de la conformidad de dos sistemas con sus especificaciones respectivas no garantiza que sean capaces de intercambiar datos. Esto ocurre porque cada hospital o entidad crea su propia interpretación de FHIR. A pesar de afirmar que cumplen con las normas, las mínimas divergencias obstaculizan la comunicación.

Asimismo, Vorisek et al. (2022), señalan como limitaciones el posible cambio en el contenido de los recursos FHIR, cuestiones relacionadas con la seguridad y la necesidad de contar con un servidor FHIR. El material puede cambiar con cada nueva versión de FHIR y provocar fallos. La protección de información es fundamental para impedir que datos delicados sean accesibles a personas inadecuadas, ya que sin un servidor central, los sistemas no tienen claro cómo trabajar juntos. En el ámbito peruano, esto dificulta la integración de hospitales grandes y pequeños.

**Estrategia de mitigación:** Se emplearán perfiles FHIR que estén en sintonía con los estándares usados a nivel internacional (US Core, International Patient Summary) y se documentarán de manera clara las decisiones de diseño y sus limitaciones.

### 1.4.5.- Variables no identificadas

Es probable que aspectos organizativos, culturales o técnicos no considerados impacten los resultados. Según Heryawan et al. (2025), examinaron más de 50 casos reales de proyectos FHIR en hospitales y clínicas, y descubrieron que el 57% fracasa debido a problemas con servidores que se desactivan o funcionan lentamente, mientras que el 34% enfrenta dificultades para convertir datos antiguos al nuevo formato debido a desajustes, y el 9% tiene complicaciones al seleccionar la versión adecuada de FHIR.

Es fundamental señalar que estas dificultades normalmente se presentan durante el uso real y no en las pruebas iniciales. Estos resultados subrayan la necesidad de ir más allá de las evaluaciones técnicas, dado que en entornos como el de Perú, donde los sistemas son diversos y a menudo obsoletos, surgen desafíos imprevistos que solo se identifican colaborando con el personal de salud a diario.

**Estrategia de mitigación:** Se añadirá un enfoque cualitativo mediante entrevistas semiestructuradas para captar factores emergentes y obstáculos no anticipados.

### 1.4.6.- Restricciones de tiempo y recursos

La implementación del proyecto piloto está limitada al tiempo académico de la investigación. De acuerdo con Rojas et al. (2024), este grupo entrevistó a 28 directores de hospitales del MINSA en Lima, Arequipa y Trujillo durante el año 2023. Encontraron que el 65% de los proyectos de historias clínicas electrónicas quedan inconclusos, principalmente porque los 6 a 9 meses típicos de la universidad son insuficientes. Indican que obtener la autorización del MINSA consume entre 2 y 3 meses, además de que otros 3 a 4 meses son necesarios para que los médicos se familiaricen con el nuevo sistema, y al final no hay tiempo para solucionar inconvenientes.

Proporcionan el ejemplo del Hospital Loayza, que intentó implementar esto en 2022, pero se rindió debido a "falta de tiempo y resistencia del personal". Por otro lado, Gómez-Chabla et al. (2024) evaluaron 87 iniciativas de salud digital en América Latina y África entre 2018 y 2023. Aseguran que los plazos reales son de 12 a 18 meses, y no de 6 como se plantea en las tesis. Sugieren comenzar con "una versión pequeña pero funcional", que aborde el problema más apremiante, y luego ir añadiendo más características a medida que haya más tiempo y recursos.

Citan casos en Ecuador donde esto ha dado buenos resultados. En el ámbito de la salud pública en Perú, esto es frecuente debido a la burocracia, pero facilita el desarrollo de algo tangible que otros pueden seguir adelante.

**Estrategia de mitigación:** Se dará prioridad a las brechas con mayor impacto y viabilidad utilizando una matriz de priorización, concentrando los recursos en un piloto que funcione y que pueda ser ampliado en etapas posteriores.

# Capítulo II: Marco teórico

## Antecedentes del problema

### Internacionales

**ADELUSI ET AL. (2025)**
**Aporte:** Proponen un framework federado basado en HL7 FHIR para intercambio seguro entre hospitales heterogéneos.
**Objetivo:** Demostrar que una arquitectura federada mejora interoperabilidad sin centralizar datos clínicos crudos.
**Problema:** Fragmentación de EHR y riesgos de seguridad en modelos centralizados de intercambio.
**Metodología utilizada:** Diseño y evaluación de framework en entorno simulado multi-hospital.
**Instrumentos de validación:** Pruebas de recuperación de datos, latencia, cumplimiento FHIR y escalabilidad.
**Resultados:** >95% de precisión en recuperación y 38% de reducción de latencia frente a enfoque centralizado.

**HERYAWAN ET AL. (2025)**
**Aporte:** Caracterizan barreras reales de implementación FHIR en la plataforma nacional Satusehat (Indonesia).
**Objetivo:** Identificar puntos críticos de adopción e integración para mejorar el despliegue interoperable nacional.
**Problema:** Dificultades técnicas recurrentes en el uso de servidores, perfiles y mapeo semántico de datos.
**Metodología utilizada:** Análisis de contenido de interacciones del Developer Hub y documentación técnica.
**Instrumentos de validación:** Categorización temática de incidencias y frecuencia de problemas reportados.
**Resultados:** Problemas en servidor FHIR (57%), mapeo de datos (34%) y selección de perfiles (9%).

**AMAR ET AL. (2024)**
**Aporte:** Ofrecen taxonomía de enfoques para interoperabilidad semántica con FHIR en literatura reciente.
**Objetivo:** Mapear tendencias metodológicas y tecnológicas en integración semántica de datos clínicos.
**Problema:** Ausencia de consolidación sobre qué enfoques semánticos se usan y con qué peso relativo.
**Metodología utilizada:** Revisión de mapeo sistemático de estudios publicados entre 2012 y 2022.
**Instrumentos de validación:** Extracción estandarizada y clasificación por categorías de enfoque semántico.
**Resultados:** n=70 estudios; mapeo (24,6%), RDF/OWL (19%), NLP/ML (15,9%), terminologías y anotación (14,3%).

**TABARI ET AL. (2024)**
**Aporte:** Sistematizan modelos de datos FHIR y priorización de recursos en implementación EHR.
**Objetivo:** Describir estructuras de modelado FHIR usadas para integración, transmisión y análisis clínico.
**Problema:** Dispersión de enfoques de modelado que dificulta diseño coherente en proyectos de interoperabilidad.
**Metodología utilizada:** Scoping review en PubMed, Scopus, WoS, IEEE, ACM y Google Scholar.
**Instrumentos de validación:** Matriz de extracción comparativa por tipo de modelo y recurso FHIR utilizado.
**Resultados:** Identifican 2 familias (dinámicos/estáticos) y mayor uso de Observation, Condition y Patient.

**BOSSENKO ET AL. (2024)**
**Aporte:** Desarrollan herramienta visual reutilizable para transformar HL7 CDA hacia recursos HL7 FHIR.
**Objetivo:** Facilitar transición nacional de interoperabilidad documental a APIs FHIR con menor fricción técnica.
**Problema:** Complejidad del mapeo CDA-FHIR para equipos clínicos y técnicos en despliegues a escala.
**Metodología utilizada:** Desarrollo y validación aplicada en la transición del sistema nacional de Estonia.
**Instrumentos de validación:** Evaluación por expertos de dominio sobre usabilidad y valor operativo.
**Resultados:** Validación positiva de usabilidad y utilidad para transformación semántica reutilizable.

**JAYATHISSA Y HEWAPATHRANA (2024)**
**Aporte:** Presentan caso técnico de servidor HAPI-FHIR para atención primaria en contexto de recursos limitados.
**Objetivo:** Mejorar interoperabilidad entre sistemas primarios integrando identidad, seguridad y flujo de datos.
**Problema:** Sistemas no integrados, debilidades de autenticación y baja estandarización de intercambio clínico.
**Metodología utilizada:** Revisión técnica con implementación de caso de uso e integración progresiva.
**Instrumentos de validación:** Pruebas funcionales con datasets sintéticos HHIMS y validación de intercambio.
**Resultados:** Factibilidad técnica confirmada para integración FHIR en primer nivel con enfoque escalable.

**TORAB-MIANDOAB ET AL. (2023)**
**Aporte:** Consolidan requisitos de interoperabilidad para sistemas de salud heterogéneos en múltiples países.
**Objetivo:** Identificar tecnologías y estándares críticos para habilitar HCE interoperable de forma sostenible.
**Problema:** Falta de interoperabilidad entre sistemas propietarios y heterogéneos con impacto en calidad asistencial.
**Metodología utilizada:** Revisión sistemática en seis bases biomédicas y de ingeniería.
**Instrumentos de validación:** Selección PRISMA y síntesis temática de requisitos técnicos y semánticos.
**Resultados:** n=36 estudios; FHIR, CDA, SNOMED-CT y SOA aparecen como requisitos prioritarios.

**HOLMGREN ET AL. (2023)**
**Aporte:** Comparan políticas de intercambio en cinco países para extraer factores de éxito en HIE.
**Objetivo:** Entender cómo el diseño de política pública condiciona la adopción de interoperabilidad nacional.
**Problema:** Variabilidad regulatoria y organizacional que limita escalamiento homogéneo del intercambio clínico.
**Metodología utilizada:** Revisión narrativa comparada de marcos de política sanitaria internacional.
**Instrumentos de validación:** Análisis transversal de diseño institucional, gobernanza y madurez de intercambio.
**Resultados:** n=5 países; la priorización gubernamental centralizada se asocia a mayor avance interoperable.

**RICHWINE ET AL. (2025)**
**Aporte:** Cuantifican el valor de las organizaciones de intercambio (HIO) para interoperabilidad hospitalaria.
**Objetivo:** Estimar la contribución de las HIO en intercambio clínico y reporte de datos en hospitales.
**Problema:** Dificultad para demostrar impacto operativo de la gobernanza del intercambio interinstitucional.
**Metodología utilizada:** Estudio observacional con análisis comparativo de hospitales participantes y no participantes.
**Instrumentos de validación:** Indicadores de intercambio clínico, reporte de salud pública y uso de datos sociales.
**Resultados:** La participación en HIO se asocia con mayor interoperabilidad reportada y mejor intercambio de datos críticos.

**RAAB ET AL. (2023)**
**Aporte:** Proponen un enfoque federado para el EHDS con control ciudadano del dato de salud.
**Objetivo:** Diseñar una arquitectura interoperable que reduzca dependencia de silos centralizados.
**Problema:** Riesgos de concentración de datos y baja portabilidad efectiva entre sistemas heterogéneos.
**Metodología utilizada:** Desarrollo conceptual y técnico de arquitectura para espacios federados.
**Instrumentos de validación:** Evaluación de factibilidad arquitectónica y criterios de gobernanza de datos.
**Resultados:** Definen lineamientos para interoperabilidad federada con mejor control de acceso y compartición.

**MONSEN ET AL. (2023)**
**Aporte:** Integran terminologías estandarizadas de enfermería con FHIR para aumentar reutilización del dato.
**Objetivo:** Mejorar interoperabilidad semántica en flujos clínicos y analíticos.
**Problema:** Subutilización de datos clínicos por baja normalización terminológica en implementaciones FHIR.
**Metodología utilizada:** Estudio aplicado de integración terminológica en recursos FHIR.
**Instrumentos de validación:** Verificación de consistencia semántica y reutilización para analítica clínica.
**Resultados:** Muestran mejora en representación estandarizada y uso secundario de información clínica.

**VORISEK ET AL. (2022)**
**Aporte:** Ofrecen panorama cuantitativo robusto de usos de FHIR en investigación en salud.
**Objetivo:** Medir áreas de aplicación, terminologías complementarias y madurez de adopción científica de FHIR.
**Problema:** Escasa consolidación cuantitativa sobre para qué y cómo se usa FHIR en investigación aplicada.
**Metodología utilizada:** Revisión sistemática de literatura 2011-2022 en cinco bases.
**Instrumentos de validación:** Extracción estructurada de variables de uso, dominio y terminologías asociadas.
**Resultados:** n=49; 73% investigación clínica; usos: estandarización 41%, captura 29%, análisis 12%.

**GAZZARATA ET AL. (2024)**
**Aporte:** Vinculan FHIR con continuidad asistencial en ecosistemas de enfermedades crónicas.
**Objetivo:** Evaluar el rol de FHIR en integración longitudinal de datos y coordinación entre niveles de atención.
**Problema:** Discontinuidad clínica por fragmentación de información en trayectorias de atención crónica.
**Metodología utilizada:** Scoping review centrada en aplicaciones FHIR para gestión clínica crónica.
**Instrumentos de validación:** Síntesis estructurada por dominios de uso, capacidades técnicas y gobernanza.
**Resultados:** Evidencian mejora de continuidad y articulación de red; sin KPI único universal reportado.

**PEDRERA-JIMÉNEZ ET AL. (2023)**
**Aporte:** Proponen enfoque agnóstico para combinar OpenEHR, ISO 13606 y FHIR sin tratarlos como excluyentes.
**Objetivo:** Definir criterios de selección y coexistencia de estándares en espacios de datos de nueva generación.
**Problema:** Decisiones de arquitectura basadas en falsa dicotomía entre estándares clínicos complementarios.
**Metodología utilizada:** Análisis técnico-conceptual comparativo de capacidades y capas de los estándares.
**Instrumentos de validación:** Matriz de compatibilidad funcional por modelado, intercambio y reutilización.
**Resultados:** Recomiendan arquitectura por capas; cada estándar aporta valor diferencial y complementario.

**CHATTERJEE ET AL. (2022)**
**Aporte:** Integran HL7 FHIR y SNOMED-CT para lograr interoperabilidad estructural y semántica simultánea.
**Objetivo:** Validar transferencia bidireccional de datos personales de salud sin pérdida semántica.
**Problema:** Intercambio clínico con pérdida de significado al pasar entre sistemas heterogéneos.
**Metodología utilizada:** Prueba de concepto con mapeo semántico y flujo bidireccional entre componentes.
**Instrumentos de validación:** Pruebas de consistencia de conceptos y verificación de integridad de datos.
**Resultados:** Logran intercambio bidireccional sin pérdida de datos y con consistencia semántica.

**GAUDET-BLAVIGNAC ET AL. (2021)**
**Aporte:** Diseñan estrategia nacional de tres pilares para uso secundario interoperable de datos de salud.
**Objetivo:** Habilitar investigación multicéntrica con datos clínicos interoperables en red nacional.
**Problema:** Baja reutilización de datos clínicos por heterogeneidad semántica y barreras organizativas.
**Metodología utilizada:** Estudio metodológico en contexto de la Swiss Personalized Health Network.
**Instrumentos de validación:** Diseño de gobernanza, normalización semántica y evaluación de factibilidad operativa.
**Resultados:** Propuesta operativa validada para escalar interoperabilidad de uso secundario.

**MUKHIYA ET AL. (2021)**
**Aporte:** Combinan FHIR con GraphQL para consultas clínicas flexibles sobre EHR heterogéneos.
**Objetivo:** Reducir acoplamiento entre sistemas y facilitar integración incremental vía capa API.
**Problema:** Rigidez en integración de datos cuando se depende de conectores punto a punto.
**Metodología utilizada:** Desarrollo de aproximación arquitectónica y validación de interoperabilidad funcional.
**Instrumentos de validación:** Pruebas de consulta, compatibilidad de intercambio y consistencia de respuesta.
**Resultados:** Demuestran viabilidad de integración flexible con menor dependencia entre plataformas.

**LIU ET AL. (2023)**
**Aporte:** Implementan un EMR intercambiable en formato FHIR con enfoque de desempeño y visualización.
**Objetivo:** Validar que una arquitectura basada en servidor FHIR mejore tiempos de transformación de datos.
**Problema:** Costos y latencias elevadas en integración cuando se depende de gateways tradicionales.
**Metodología utilizada:** Implementación experimental con pruebas de carga y comparación de arquitectura.
**Instrumentos de validación:** Pruebas Apache JMeter y métricas de tiempo/costo de conversión.
**Resultados:** Reportan reducción significativa en tiempos y costos de transformación de datos clínicos.

**ANAND Y SADHNA (2023)**
**Aporte:** Analizan bibliométricamente la convergencia entre FHIR y blockchain en interoperabilidad EHR.
**Objetivo:** Identificar tendencias, vacíos y líneas emergentes de investigación en interoperabilidad segura.
**Problema:** Dispersión de evidencia sobre madurez de enfoques blockchain + FHIR para intercambio clínico.
**Metodología utilizada:** Estudio bibliométrico y análisis temático de literatura especializada.
**Instrumentos de validación:** Mapas temáticos, coocurrencia de términos y evolución temporal.
**Resultados:** Confirman crecimiento del campo y centralidad de interoperabilidad y seguridad como ejes de investigación.

**SURISETTY (2026)**
**Aporte:** Propone blueprint de interoperabilidad de extremo a extremo con HL7, FHIR, CCD y EHR.
**Objetivo:** Integrar lineamientos técnicos en una secuencia práctica de implementación por fases.
**Problema:** Brecha entre recomendaciones de alto nivel y guías operativas de implementación real.
**Metodología utilizada:** Propuesta aplicada de arquitectura y flujo de integración integral.
**Instrumentos de validación:** Definición de flujo técnico, componentes e hitos operativos de despliegue.
**Resultados:** Ofrece hoja de ruta replicable para proyectos de interoperabilidad clínica por etapas.

**FERNANDEZ ET AL. (2025)**
**Aporte:** Aportan evidencia aplicada de interoperabilidad en sistema universal con el caso brasileño.
**Objetivo:** Analizar integración entre atención primaria y hospitalaria para continuidad clínica poblacional.
**Problema:** Fragmentación inter-nivel que limita seguimiento clínico y gestión integral del paciente.
**Metodología utilizada:** Análisis de experiencia nacional y lecciones de implementación en red pública.
**Instrumentos de validación:** Evaluación comparativa de flujos de información y coordinación asistencial.
**Resultados:** Identifican que estándares + procesos + gobernanza sostenida son condición de impacto.

### Nacionales

**MAURICIO ET AL. (2024)**
**Aporte:** Proponen sistema peruano de interoperabilidad EHR con HL7 FHIR y blockchain.
**Objetivo:** Permitir intercambio entre clínicas heterogéneas garantizando seguridad y privacidad de datos.
**Problema:** En Perú no existe integración automática de historias clínicas entre establecimientos.
**Metodología utilizada:** Diseño de arquitectura, homologación a recursos FHIR y simulación de caso.
**Instrumentos de validación:** Encuesta de adopción (n=30 pacientes) y usabilidad (n=10 médicos).
**Resultados:** Reportan niveles muy altos de adopción/usabilidad y factibilidad sin reemplazar sistemas legados.

**PORRAS GAMARRA (2024)**
**Aporte:** Documenta implementación de interoperabilidad HL7 FHIR + openEHR en entorno real.
**Objetivo:** Validar intercambio clínico efectivo y persistencia semántica con estándares internacionales.
**Problema:** Brecha tecnológica entre sistemas interoperables avanzados y realidad peruana fragmentada.
**Metodología utilizada:** Estudio de suficiencia profesional con análisis de implementación del proyecto M-Connecta.
**Instrumentos de validación:** Verificación funcional de mensajería FHIR y persistencia con arquetipos openEHR.
**Resultados:** Evidencia viabilidad técnica y recomienda adopción de FHIR en historias clínicas peruanas.

**ARRUÉ PAJARES Y VARGAS RIOJA (2022)**
**Aporte:** Implementan HIS interoperable basado en HL7 para centros de categoría II-1 o superior.
**Objetivo:** Integrar módulos administrativos y clínicos para mejorar flujo hospitalario e intercambio.
**Problema:** Sistemas de salud peruanos fraccionados y sin integración efectiva entre componentes.
**Metodología utilizada:** Desarrollo de plataforma web HIS con protocolo HL7 para interoperar módulos HIMS.
**Instrumentos de validación:** Pruebas de integración entre módulos (HCE, farmacia, laboratorio y radiología).
**Resultados:** Demuestran factibilidad de interoperabilidad operativa en contexto nacional con HL7.

**BAYONA CASTAÑEDA (2019)**
**Aporte:** Presenta diagnóstico estructural de la historia clínica electrónica en el sistema peruano.
**Objetivo:** Analizar evolución normativa y barreras de implementación de HCE y RENHICE.
**Problema:** Fragmentación MINSA-EsSalud, baja conectividad e implementación desigual de plataformas.
**Metodología utilizada:** Trabajo de fin de máster con revisión documental y análisis del ecosistema nacional.
**Instrumentos de validación:** Análisis normativo-técnico de Ley 30024, RENHICE y experiencias institucionales.
**Resultados:** Identifica persistencia de múltiples historias por paciente y bajo avance interoperable.

**ESPARZA MORGAN (2025)**
**Aporte:** Relaciona madurez de HCE única con mejora de gestión de calidad en hospital EsSalud.
**Objetivo:** Medir influencia de la HCE en planificación, organización y garantía de servicios.
**Problema:** Desempeño de calidad hospitalaria afectado por gestión clínica no plenamente digitalizada.
**Metodología utilizada:** Estudio correlacional aplicado en entorno hospitalario peruano.
**Instrumentos de validación:** Indicadores de calidad de gestión y medición de madurez de uso de HCE.
**Resultados:** Reporta correlaciones positivas; mayor uso de HCE se asocia con mejor desempeño de calidad.

**ARIAS GERONIMO (2025)**
**Aporte:** Evidencia vínculo entre confiabilidad de HCE y calidad de servicios preventivos.
**Objetivo:** Determinar relación entre calidad del registro electrónico y prestación preventiva en microred.
**Problema:** Inconsistencias de datos y baja disponibilidad afectan continuidad y calidad percibida del servicio.
**Metodología utilizada:** Estudio correlacional en red pública de primer nivel.
**Instrumentos de validación:** Medición de confiabilidad del registro y desempeño en servicios preventivos.
**Resultados:** Asociación positiva moderada y significativa entre confiabilidad HCE y prestación preventiva.

**SANCHEZ CALLE (2024)**
**Aporte:** Formula arquitectura y requisitos de HCE ocupacional con base en ISO 18308 e ISO 13606.
**Objetivo:** Definir especificaciones formales para interoperabilidad y sostenibilidad de HCE ocupacional.
**Problema:** Ausencia de requerimientos técnicos estandarizados para intercambio clínico ocupacional.
**Metodología utilizada:** Desarrollo de propuesta arquitectónica basada en normas internacionales.
**Instrumentos de validación:** Trazabilidad de requisitos normativos y consistencia del diseño arquitectónico.
**Resultados:** Entrega marco técnico aplicable para diseño interoperable y gobernable de HCE ocupacional.

**FERNÁNDEZ INFANZÓN Y HUARAC CUIZANO (2021)**
**Aporte:** Proponen plan de negocio para integrar IPRESS a plataforma interoperable de HCE.
**Objetivo:** Viabilizar articulación entre prestadores públicos/privados con blockchain y biometría.
**Problema:** Barreras de confianza, trazabilidad y coordinación institucional para intercambio clínico.
**Metodología utilizada:** Diseño de plan de negocio con enfoque tecnológico y de adopción multiactor.
**Instrumentos de validación:** Evaluación de viabilidad, propuesta de modelo operativo y análisis de stakeholders.
**Resultados:** Definen esquema de implementación gradual para interoperabilidad institucional en IPRESS.

**BRAN ET AL. (2024)**
**Aporte:** Integran blockchain, IPFS y HL7 para fortalecer intercambio de historias clínicas electrónicas.
**Objetivo:** Mejorar inmutabilidad, auditabilidad y confianza sobre flujo de datos clínicos compartidos.
**Problema:** Riesgos de manipulación, baja trazabilidad y confianza limitada en ecosistemas interoperables.
**Metodología utilizada:** Diseño de arquitectura híbrida y evaluación funcional de interoperabilidad segura.
**Instrumentos de validación:** Pruebas de integridad, trazabilidad de transacciones y consistencia de intercambio.
**Resultados:** Evidencian mejora en auditabilidad e integridad al combinar HL7 con blockchain/IPFS.

**MORALES-CAMARGO Y MENESES-CLAUDIO (2023)**
**Aporte:** Sintetizan impacto del registro médico electrónico en atención y gestión sanitaria.
**Objetivo:** Evaluar beneficios y barreras de implementación de EMR en evidencia reciente.
**Problema:** Adopción desigual de EMR y brechas de estandarización/capacitación en servicios de salud.
**Metodología utilizada:** Revisión sistemática del periodo 2013-2023.
**Instrumentos de validación:** Búsqueda estructurada y análisis comparativo de resultados reportados.
**Resultados:** Reportan mejoras en acceso, soporte a decisión y eficiencia, con barreras de adopción persistentes.

### Síntesis crítica de antecedentes

La revisión internacional y nacional muestra convergencia en tres hallazgos. Primero, existe consenso técnico sobre FHIR como estándar articulador del intercambio (Vorisek et al., 2022; Torab-Miandoab et al., 2023; Tabari et al., 2024), pero su efectividad depende de perfiles, terminologías y reglas de implementación consistentes (Kramer y Moesel, 2023; Chatterjee et al., 2022; Monsen et al., 2023). Segundo, la interoperabilidad sostenible requiere gobernanza explícita del intercambio, incluyendo arreglos institucionales y federación de datos (Holmgren et al., 2023; Richwine et al., 2025; Raab et al., 2023). Tercero, en Perú la evidencia confirma avances en propuestas y pilotos, pero con heterogeneidad de madurez digital, conectividad y adopción operativa entre establecimientos (Bayona Castañeda, 2019; Mauricio et al., 2024; Porras Gamarra, 2024; Arrué Pajares y Vargas Rioja, 2022).

En términos de brecha de investigación, aún son escasos los estudios nacionales que integren en un mismo diseño: diagnóstico estructurado de brechas, implementación técnica alineada a HL7 FHIR y evaluación pre-post con indicadores de calidad del intercambio clínico. Esta brecha justifica el enfoque de la presente tesis y orienta su aporte incremental frente al estado del arte.

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

**Enfoques híbridos y escalabilidad de implementación.** Pedrera-Jiménez et al. (2023) sostienen que OpenEHR, ISO 13606 y FHIR no deben tratarse como opciones excluyentes, sino como componentes complementarios de una arquitectura por capas. Surisetty (2026) y Liu et al. (2023) agregan que la escalabilidad técnica mejora cuando se definen rutas de transformación explícitas (documento-API) y se sustituyen componentes de alto acoplamiento por servicios FHIR nativos. En paralelo, Heryawan et al. (2025) y Jayathissa y Hewapathrana (2024) muestran que, en contextos de recursos limitados, el éxito depende de combinar decisiones arquitectónicas con capacidades operativas de despliegue progresivo.

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

La implementación de un modelo de interoperabilidad basado en HL7 FHIR mejora significativamente el intercambio de información clínica de pacientes atendidos en centros de salud del MINSA en Perú, evidenciado por la mejora de los indicadores de completitud, codificación, duplicidad, tiempo de validación, continuidad de atención y trazabilidad.

### Hipótesis específicas

- **HE1:** El diagnóstico sistemático del cumplimiento de estándares de interoperabilidad (RNIEDS, PIDESALUD, HL7, CIE-10, CPMS) permite identificar brechas críticas cuantificables en el intercambio de información clínica de los centros de salud del ámbito MINSA.

- **HE2:** La implementación de una capa piloto de integración basada en HL7 FHIR produce una mejora estadísticamente significativa en los indicadores de calidad del intercambio de información clínica (completitud, codificación CIE-10/CPMS, duplicidad de pacientes/exámenes, tiempo de validación administrativa de prestaciones) respecto a la línea base.

- **HE3:** El modelo de interoperabilidad implementado mejora la continuidad de la atención y la trazabilidad de accesos en las historias clínicas electrónicas entre establecimientos de salud.

- **HE4:** Los lineamientos técnicos y operativos derivados de la experiencia piloto son replicables para la escalabilidad del modelo en otros establecimientos de salud del MINSA.

## Operacionalización de variables

### Variable independiente: Modelo de interoperabilidad basado en HL7 FHIR

Se define como el conjunto integrado de componentes técnicos, normativos y operativos que, organizados en tres fases secuenciales (diagnóstico, implementación piloto y evaluación de impacto), buscan habilitar el intercambio estandarizado de datos clínicos entre sistemas de información en salud. En la **Fase 1 (Diagnóstico)**, se evalúa el nivel de cumplimiento de la arquitectura RNIEDS-PIDESALUD, el grado de adopción de estándares de intercambio (HL7/FHIR), el cumplimiento de codificación clínica (CIE-10, CPMS, catálogos IEDS), el estado de seguridad y trazabilidad, y la capacidad de infraestructura y conectividad. En la **Fase 2 (Implementación piloto)**, se desarrolla la capa de integración FHIR (recursos, perfiles, terminologías), el mapeo y transformación de datos locales al modelo FHIR, la implementación del servicio de intercambio piloto y la capacitación del personal operativo. En la **Fase 3 (Evaluación)**, se comparan los indicadores de calidad del intercambio de información clínica antes y después de la intervención.

### Variable dependiente: Calidad del intercambio de información clínica en establecimientos del MINSA

Se operacionaliza mediante ocho indicadores medidos antes y después de la implementación del modelo: (1) **completitud de HCE**, definida como el porcentaje de campos obligatorios completos en la historia clínica electrónica; (2) **codificación CIE-10**, porcentaje de diagnósticos correctamente codificados; (3) **codificación CPMS**, porcentaje de procedimientos correctamente codificados; (4) **duplicidad de pacientes**, tasa de registros duplicados por cada 1 000 atenciones; (5) **duplicidad de exámenes**, tasa de exámenes y procedimientos duplicados por cada 1 000 atenciones; (6) **tiempo de validación administrativa de prestaciones**, tiempo promedio en horas desde la atención hasta la validación administrativa de prestaciones financiadas por el SIS; (7) **continuidad de atención**, porcentaje de HCE con trazabilidad verificable entre establecimientos; y (8) **trazabilidad de accesos**, porcentaje de registros con log completo de acceso y modificación. Los indicadores se obtienen por auditoría de registros, muestras de atenciones, bases de datos HIS, registros administrativos de validación de prestaciones (SIS), cruce de registros entre establecimientos y logs del sistema.

## Matriz de operacionalización de variables

| Variable | Definición conceptual | Definición operacional | Dimensiones | Indicadores | Escala de valoración | Instrumentos |
|---|---|---|---|---|---|---|
| Variable independiente: Modelo de interoperabilidad basado en HL7 FHIR | Conjunto integrado de componentes técnicos, normativos y operativos que habilitan el intercambio estandarizado de datos clínicos. | Implementación de tres fases: diagnóstico de brechas, capa de integración FHIR piloto y evaluación pre/post. | Diagnóstico | Nivel de cumplimiento RNIEDS-PIDESALUD; adopción de HL7/FHIR; codificación CIE-10/CPMS. | Nominal (cumple/no cumple) y de razón (% de cumplimiento). | Lista de chequeo normativo-técnico; auditoría de registros; pruebas de integración. |
| Variable independiente: Modelo de interoperabilidad basado en HL7 FHIR | Conjunto integrado de componentes técnicos, normativos y operativos que habilitan el intercambio estandarizado de datos clínicos. | Implementación de tres fases: diagnóstico de brechas, capa de integración FHIR piloto y evaluación pre/post. | Implementación piloto | Recursos FHIR mapeados; tasa de éxito de intercambio; perfiles y terminologías aplicados. | Nominal (cumple/no cumple) y de razón (% de cumplimiento). | Lista de chequeo normativo-técnico; auditoría de registros; pruebas de integración. |
| Variable independiente: Modelo de interoperabilidad basado en HL7 FHIR | Conjunto integrado de componentes técnicos, normativos y operativos que habilitan el intercambio estandarizado de datos clínicos. | Implementación de tres fases: diagnóstico de brechas, capa de integración FHIR piloto y evaluación pre/post. | Evaluación de impacto | Comparación pre/post de los 8 indicadores de calidad de HCE. | Nominal (cumple/no cumple) y de razón (% de cumplimiento). | Lista de chequeo normativo-técnico; auditoría de registros; pruebas de integración. |
| Variable dependiente: Calidad del intercambio de información clínica en establecimientos del MINSA | Grado de integridad, codificación, trazabilidad y continuidad del intercambio de información clínica en establecimientos MINSA. | Medición pre y post intervención de 8 indicadores cuantitativos de calidad de HCE. | Integridad de datos | Completitud de HCE (% campos obligatorios); codificación CIE-10 (%); codificación CPMS (%). | De razón (%, tasa, horas). | Auditoría de registros; base de datos HIS; registros administrativos de validación (SIS); logs del sistema. |
| Variable dependiente: Calidad del intercambio de información clínica en establecimientos del MINSA | Grado de integridad, codificación, trazabilidad y continuidad del intercambio de información clínica en establecimientos MINSA. | Medición pre y post intervención de 8 indicadores cuantitativos de calidad de HCE. | Duplicidad | Duplicidad de pacientes (tasa/1000); duplicidad de exámenes (tasa/1000). | De razón (%, tasa, horas). | Auditoría de registros; base de datos HIS; registros administrativos de validación (SIS); logs del sistema. |
| Variable dependiente: Calidad del intercambio de información clínica en establecimientos del MINSA | Grado de integridad, codificación, trazabilidad y continuidad del intercambio de información clínica en establecimientos MINSA. | Medición pre y post intervención de 8 indicadores cuantitativos de calidad de HCE. | Eficiencia administrativa | Tiempo de validación administrativa de prestaciones (horas promedio). | De razón (%, tasa, horas). | Auditoría de registros; base de datos HIS; registros administrativos de validación (SIS); logs del sistema. |
| Variable dependiente: Calidad del intercambio de información clínica en establecimientos del MINSA | Grado de integridad, codificación, trazabilidad y continuidad del intercambio de información clínica en establecimientos MINSA. | Medición pre y post intervención de 8 indicadores cuantitativos de calidad de HCE. | Continuidad y trazabilidad | Continuidad de atención (% HCE con trazabilidad); trazabilidad de accesos (% registros con log completo). | De razón (%, tasa, horas). | Auditoría de registros; base de datos HIS; registros administrativos de validación (SIS); logs del sistema. |

: Tabla 1. Matriz de operacionalización de variables



# Capítulo IV: Metodología del estudio

## Enfoque, tipo y alcance de investigación

### Enfoque

La presente investigación adopta un enfoque mixto con predominancia cuantitativa y apoyo cualitativo. Según Hernández-Sampieri y Mendoza (2018), los métodos mixtos representan un conjunto de procesos sistemáticos que implican la recolección y el análisis de datos tanto cuantitativos como cualitativos, así como su integración y discusión conjunta, lo que permite lograr un mayor entendimiento del fenómeno bajo estudio. El componente cuantitativo predominante se justifica porque el estudio busca medir objetivamente los indicadores de calidad del intercambio de información clínica antes y después de la intervención, mientras que el componente cualitativo complementario permite capturar las barreras organizacionales y de implementación que los datos numéricos no reflejan. Este enfoque es consistente con los estudios de referencia: Adelusi et al. (2025) utilizaron métricas cuantitativas de rendimiento y Liu et al. (2023) emplearon pruebas de rendimiento con Apache JMeter, complementados con análisis cualitativos de la experiencia de implementación.

### Tipo y alcance

La investigación es de tipo aplicada, pues busca resolver un problema práctico específico — la deficiente interoperabilidad de historias clínicas en centros de salud del MINSA — mediante la implementación de un modelo basado en HL7 FHIR. Según Hernández-Sampieri y Mendoza (2018), la investigación aplicada se orienta a resolver problemas de la práctica a través de la aplicación del conocimiento. El alcance es explicativo-propositivo: explicativo porque busca establecer relaciones causales entre la implementación del modelo FHIR (variable independiente) y la mejora en la calidad del intercambio de información clínica (variable dependiente), y propositivo porque genera lineamientos de escalabilidad para otros establecimientos. Este alcance se alinea con estudios como el de Bossenko et al. (2024), que no solo implementaron sino que evaluaron el impacto de su herramienta de transformación CDA-FHIR.

## Diseño de la investigación

El diseño es pre-experimental del tipo pre-test/post-test con un solo grupo, representado esquemáticamente como: O₁ → X → O₂, donde O₁ es la medición de línea base (pre-test), X es la intervención (implementación de la capa de integración FHIR) y O₂ es la medición posterior (post-test). Este diseño fue seleccionado considerando las restricciones operativas del contexto MINSA, donde la asignación aleatoria de establecimientos a grupos de control no es viable. Según Hernández-Sampieri y Mendoza (2018), los diseños pre-experimentales son útiles como un primer acercamiento al problema de investigación en contextos donde no es posible aplicar diseños experimentales puros. El diseño contempla tres fases: (1) diagnóstico de brechas de interoperabilidad y levantamiento de línea base; (2) implementación piloto de la capa de integración basada en HL7 FHIR; y (3) evaluación de impacto mediante comparación de indicadores pre y post intervención. Este diseño por fases es coherente con las implementaciones graduales recomendadas por Heryawan et al. (2025) y Jayathissa y Hewapathrana (2024).

## Población y muestra

### Población

La población está constituida por los establecimientos de salud del MINSA en Perú, así como el conjunto de historias clínicas electrónicas y registros clínico-administrativos generados en dichos establecimientos. Según Hernández-Sampieri y Mendoza (2018), la población es el conjunto de todos los casos que concuerdan con determinadas especificaciones. En este caso, los criterios de inclusión son: (a) establecimientos del MINSA en Lima que atienden población usuaria del sistema público (incluida la cobertura SIS), (b) que cuenten con algún sistema de registro electrónico de salud, y (c) que operen en al menos dos niveles de complejidad diferentes.

### Muestra

La muestra se definirá mediante muestreo no probabilístico por conveniencia, considerando al menos 2 o 3 establecimientos de diferentes niveles de complejidad en Lima, según disponibilidad de acceso institucional y calidad de datos. Hernández-Sampieri y Mendoza (2018) señalan que en las muestras no probabilísticas, la elección de los elementos no depende de la probabilidad sino de las características de la investigación, lo cual es apropiado cuando las restricciones operativas limitan la aleatorización. Para la auditoría de registros clínicos, se seleccionará una muestra representativa de historias clínicas por establecimiento, cuyo tamaño se determinará mediante cálculo estadístico con un nivel de confianza del 95% y un margen de error del 5%.

## Técnicas e instrumentos de recolección de datos

### Técnicas e instrumentos

Se emplearán las siguientes técnicas e instrumentos, seleccionados en función de los objetivos y las fases del diseño de investigación:

- **Revisión documental normativa y técnica:** Análisis sistemático del marco regulatorio (RM N° 1104-2018-MINSA, RM N° 464-2019-MINSA, RM N° 1193-2019-MINSA) y de la documentación técnica de los sistemas de información en los establecimientos seleccionados. Según Hernández-Sampieri y Mendoza (2018), la revisión documental permite obtener datos secundarios de fuentes institucionales que complementan la información primaria.
- **Lista de chequeo de cumplimiento normativo-técnico:** Instrumento estructurado con ítems dicotómicos (cumple/no cumple) que evalúa el grado de adopción de los estándares de interoperabilidad (RNIEDS, PIDESALUD, HL7, CIE-10, CPMS) en cada establecimiento.
- **Ficha de auditoría de registros clínico-administrativos:** Instrumento que permite medir los ocho indicadores de calidad del intercambio de información clínica (completitud, codificación CIE-10, codificación CPMS, duplicidad de pacientes, duplicidad de exámenes, tiempo de validación administrativa de prestaciones, continuidad de atención y trazabilidad de accesos) en las mediciones pre y post intervención.
- **Entrevistas semiestructuradas:** Dirigidas a responsables de TI y áreas asistenciales de los establecimientos, con el objetivo de identificar barreras organizacionales, culturales y técnicas no capturables mediante los instrumentos cuantitativos.
- **Pruebas de integración técnica:** Conjunto de pruebas automatizadas para validar la interoperabilidad FHIR (envío/recepción de recursos, validación de perfiles, tiempos de respuesta), siguiendo el enfoque de pruebas de rendimiento empleado por Liu et al. (2023) y las métricas de Adelusi et al. (2025).

### Validez y confiabilidad

La **validez de contenido** de los instrumentos (lista de chequeo de cumplimiento normativo-técnico y ficha de auditoría de registros clínicos) se asegurará mediante juicio de expertos: al menos tres especialistas en informática en salud, interoperabilidad o gestión de HCE evaluarán la pertinencia, claridad y suficiencia de cada ítem utilizando el coeficiente de concordancia V de Aiken, requiriendo un valor ≥ 0.80 para su aceptación. La **validez de constructo** se sustenta en que los indicadores derivan de estándares reconocidos internacionalmente (HL7 FHIR, CIE-10, CPMS) y del marco normativo nacional (RM N° 1104-2018-MINSA, RM N° 464-2019-MINSA), lo cual garantiza la correspondencia entre los indicadores medidos y los conceptos teóricos de interoperabilidad y calidad del intercambio de información clínica. La **confiabilidad** de los indicadores cuantitativos se evaluará mediante consistencia interna: para los ítems dicotómicos de la lista de chequeo se utilizará el coeficiente KR-20, y para las escalas de los ítems de auditoría se empleará el coeficiente alfa de Cronbach, esperando valores ≥ 0.70 en ambos casos. Adicionalmente, se realizará una prueba piloto en un establecimiento no incluido en la muestra final para calibrar los instrumentos.

### Procedimiento de recolección de datos

La recolección de datos se ejecutará en tres etapas alineadas con las fases del diseño de investigación:

**Etapa 1 — Diagnóstico (pre-test).** Se aplicará la lista de chequeo de cumplimiento normativo-técnico en cada establecimiento seleccionado, complementada con revisión documental de normativas institucionales. Simultáneamente, se levantará la línea base de los ocho indicadores de calidad del intercambio de información clínica mediante auditoría de una muestra representativa de registros clínico-administrativos (historias clínicas, atenciones financiadas por SIS, logs de sistema). Se realizarán entrevistas semiestructuradas a responsables de TI y áreas asistenciales para identificar barreras organizacionales. Los datos cuantitativos se extraerán de las bases de datos HIS y registros administrativos de validación de prestaciones (SIS) con autorización institucional.

**Etapa 2 — Implementación piloto.** Se registrarán los parámetros de configuración de la capa de integración FHIR (recursos mapeados, perfiles utilizados, terminologías aplicadas) y los resultados de las pruebas de integración técnica (tasa de éxito en envío/recepción de recursos, errores de validación, tiempos de respuesta). Se documentarán las actividades de capacitación y las incidencias detectadas durante la operación piloto.

**Etapa 3 — Evaluación (post-test).** Transcurrido un período de operación suficiente (mínimo cuatro semanas), se repetirá la medición de los ocho indicadores sobre una muestra equivalente de registros, utilizando los mismos instrumentos y criterios de la línea base. Las mediciones pre y post se compilarán en una base de datos anonimizada para su análisis estadístico.

## Técnicas de análisis de datos

El análisis de datos se realizará en dos vertientes, de acuerdo con el enfoque mixto de la investigación:

**Análisis cuantitativo.** Los datos de los ocho indicadores de calidad del intercambio de información clínica se procesarán con estadística descriptiva (media, mediana, desviación estándar, porcentajes) e inferencial. Para la comparación pre-post intervención, se verificará la normalidad de las distribuciones mediante la prueba de Shapiro-Wilk. En caso de distribuciones normales, se aplicará la prueba t de Student para muestras relacionadas; en caso contrario, se utilizará la prueba no paramétrica de rangos con signo de Wilcoxon (Hernández-Sampieri y Mendoza, 2018). El nivel de significancia se fijará en α = 0.05. Se construirá un índice compuesto de cumplimiento de interoperabilidad que integre los resultados de la lista de chequeo normativo-técnico. Los datos se procesarán con software estadístico SPSS o R.

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








