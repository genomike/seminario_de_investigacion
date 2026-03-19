# Checklist de cumplimiento normativo y brechas

## Contexto normativo

- RM N° 1104-2018-MINSA: infraestructura de interoperabilidad (RNIEDS y PIDESALUD).
- RM N° 464-2019-MINSA: directiva de interoperabilidad asistencial (DA N° 266-MINSA/2019/OGTI).
- RM N° 1193-2019-MINSA: catálogo IEDS para estandarización de datos.

## Uso sugerido

Marcar cada ítem con evidencia verificable (documento, captura, log, acta técnica).

- Estado: `Cumple` | `Parcial` | `No cumple`
- Prioridad: `Alta` | `Media` | `Baja`

## Matriz de verificación

| Dominio | Requisito verificable | Evidencia esperada | Estado | Prioridad | Riesgo si no cumple |
|---|---|---|---|---|---|
| Gobernanza | Existe responsable formal de interoperabilidad (OGTI/red regional/establecimiento) | Resolución interna, MOF/ROF, designación |  | Alta | Implementación descoordinada |
| Arquitectura | El sistema local está registrado para integrarse a PIDESALUD | Acta técnica, endpoint habilitado, credenciales |  | Alta | Aislamiento de datos |
| Arquitectura | Se consulta/publica catálogos desde RNIEDS o réplica oficial | Bitácora de sincronización, script de actualización |  | Alta | Inconsistencia semántica |
| Estándares | Mensajería clínica implementada con HL7 en procesos definidos | Especificaciones, mensajes de prueba, logs |  | Alta | Intercambio no interoperable |
| Estándares | Imágenes diagnósticas interoperan con DICOM cuando aplica | Integración RIS/PACS, pruebas de intercambio |  | Media | Pérdida de continuidad diagnóstica |
| Codificación | Diagnósticos codificados con CIE-10 | Registros clínicos auditados |  | Alta | Errores clínico-estadísticos |
| Codificación | Procedimientos codificados con CPMS | Historias clínicas, reportes SIS |  | Alta | Observaciones y rechazo de pagos |
| IEDS | Identificación de paciente usa DNI/CE con validación de fuente oficial | Integración RENIEC/Migraciones, reglas de validación |  | Alta | Duplicidad/colisión de identidad |
| IEDS | Identificación de establecimiento usa código RENAES vigente | Catálogo local y validación vigente |  | Alta | Trazabilidad institucional deficiente |
| IEDS | Catálogo de medicamentos alineado con DIGEMID | Maestro de medicamentos y mapeo de códigos |  | Alta | Riesgo de medicación |
| Seguridad | Tratamiento de datos cumple Ley 29733 y medidas de seguridad | Políticas, controles de acceso, cifrado |  | Alta | Riesgo legal y de privacidad |
| Trazabilidad | Auditoría de accesos y transacciones habilitada | Logs, tablero SIEM, reportes de auditoría |  | Alta | Imposibilidad de control y sanción |
| Operación SIS | Validación administrativa SIS integrada al flujo clínico | Tiempos de validación, tasa de rechazo |  | Alta | Demoras y no cobertura |
| Calidad de dato | Existe proceso de calidad para detectar incompletitud y duplicidad | Indicadores, reportes mensuales, planes de mejora |  | Media | Decisiones clínicas y de gestión sesgadas |
| Continuidad de atención | Se recupera historia básica del paciente entre establecimientos | Pruebas de caso interinstitucional |  | Alta | Repetición de exámenes y retrasos |

## Matriz rápida de brechas priorizadas

| Brecha crítica | Impacto principal | Priorización | Acción mínima recomendada |
|---|---|---|---|
| No conexión funcional a PIDESALUD | Historia fragmentada y duplicación de exámenes | Alta | Habilitar integración y pruebas de punta a punta |
| Catálogos IEDS desactualizados | Incompatibilidad semántica y errores de codificación | Alta | Sincronizar catálogos y bloquear códigos no vigentes |
| Bajo cumplimiento HL7/CIE-10/CPMS | Rechazos SIS e información no comparable | Alta | Plan de adecuación técnica y capacitación por servicio |
| Falta de auditoría y trazabilidad | Riesgo legal y baja gobernanza de datos | Alta | Implementar logs auditables y revisión periódica |
| Déficit de conectividad/equipamiento | Captura tardía y datos incompletos en punto de atención | Media | Priorizar inversión en sedes críticas SIS |

## Indicadores mínimos para seguimiento

- Porcentaje de establecimientos conectados y operativos en PIDESALUD.
- Porcentaje de transacciones clínicas válidas por estándar HL7.
- Porcentaje de diagnósticos codificados correctamente en CIE-10.
- Porcentaje de procedimientos codificados correctamente en CPMS.
- Tasa de duplicidad de pacientes y de exámenes por cada 1000 atenciones.
- Tiempo promedio de validación administrativa SIS.
- Porcentaje de eventos con trazabilidad completa de acceso al dato.
