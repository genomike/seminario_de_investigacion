---
name: thesis-dominio-interoperabilidad
description: Conocimiento de dominio específico de la tesis actual (interoperabilidad clínica, HL7 FHIR, MINSA-Perú). Cargar SOLO si la tesis sigue siendo sobre este tema. En forks de otro tema, reemplazar este skill por `thesis-dominio-<nuevo-tema>`.
---

# Dominio: interoperabilidad clínica con HL7 FHIR (MINSA-Perú)

> ⚠ Este skill es **específico al tema de la tesis original**.
> En un fork, eliminar y crear un equivalente para el nuevo dominio.

## Vocabulario obligatorio

| Sigla | Forma completa | Primera mención |
|---|---|---|
| HL7 | Health Level Seven | Health Level Seven (HL7) |
| FHIR | Fast Healthcare Interoperability Resources | Fast Healthcare Interoperability Resources (FHIR) |
| EHR | Electronic Health Record | Historia clínica electrónica (EHR) |
| HIE | Health Information Exchange | intercambio de información en salud (HIE) |
| MINSA | Ministerio de Salud del Perú | Ministerio de Salud del Perú (MINSA) |
| OPS | Organización Panamericana de la Salud | Organización Panamericana de la Salud (OPS) |
| HIMSS | Healthcare Information and Management Systems Society | Healthcare Information and Management Systems Society (HIMSS) |
| CDA | Clinical Document Architecture | Clinical Document Architecture (CDA) |
| LOINC | Logical Observation Identifiers Names and Codes | LOINC |
| SNOMED CT | Systematized Nomenclature of Medicine — Clinical Terms | SNOMED CT |

## Niveles de interoperabilidad (HIMSS)

1. Fundacional
2. Estructural
3. Semántica
4. Organizacional

Citar siempre como modelo de referencia para clasificar las dimensiones
de la variable dependiente.

## Recursos FHIR clave para este dominio

`Patient`, `Practitioner`, `Encounter`, `Observation`, `Condition`,
`MedicationRequest`, `DiagnosticReport`, `Bundle`, `Composition`,
`Consent`. Mantener consistencia: nombres de recursos siempre en inglés
y en monoespaciado (` `Patient` `).

## Marco normativo peruano (referencia obligada)

- Ley General de Salud (Ley 26842)
- Ley de protección de datos personales (Ley 29733)
- RM 297-2014/MINSA — Norma técnica de historia clínica electrónica
- RM 1104-2024/MINSA — Lineamientos de interoperabilidad
- RM 464-2024/MINSA — Estándar HL7 FHIR para intercambio
- RM 1193-2024/MINSA — Mesa de partes electrónica / interoperabilidad

Cualquier antecedente nacional debe poder mapearse al menos a una de
estas resoluciones.

## Bases académicas privilegiadas

- JMIR (incluye `Medical Informatics`, `Formative Research`).
- Frontiers in Digital Health.
- BMC Medical Informatics and Decision Making.
- npj Digital Medicine.
- Journal of the American Medical Informatics Association (JAMIA).
- Sensors (MDPI) — solo cuando es de implementación clínica.
- Repositorios institucionales: PUCP, UPCH, USIL, UNFV, ESAN, UNI.

## Métricas usadas como indicadores

- Latencia de respuesta (ms).
- Tasa de adherencia al protocolo (% de mensajes válidos).
- Precisión de recuperación (% de registros íntegros).
- Cobertura semántica (% de campos mapeados a LOINC/SNOMED).
- Tasa de éxito de intercambio (% transacciones completadas).
- Tiempo de despliegue (días).

Cuando un antecedente reporta otra métrica, traducirla al equivalente
más cercano en la tabla síntesis (`thesis-tablas-apa`).

## Ejemplos de antecedentes ya escritos

Ver bloques en `content/manuscript/Documento_Tesis.md` para: ADELUSI ET AL. (2025),
HERYAWAN ET AL. (2025), AMAR ET AL. (2024), TABARI ET AL. (2024),
BOSSENKO ET AL. (2024), MAURICIO ET AL. (2024). Reusar esos como
referencia de estilo, no copiar contenido.

## Diagramas de referencia

- `media/diagrama-niveles-interoperabilidad.png` — niveles HIMSS.
- `media/diagrama-recursos-fhir.png` — relaciones entre recursos.
- `media/diagrama-arquitecturas-hie.png` — modelos federado / centralizado / híbrido.
- `media/diagrama-marco-normativo-peru.png` — pirámide normativa.
- `media/diagrama-fragmentacion-sistema-salud-peru.png` — diagnóstico.

## Anti-patrones de dominio

- Confundir HL7 v2 (mensajería) con HL7 FHIR (REST + recursos).
- Llamar "API FHIR" a un endpoint que no implementa los recursos
  estándar.
- Usar "interoperabilidad" como sinónimo de "integración".
- Citar Indonesia / Estonia / EE.UU. como si fueran replicables al
  Perú sin discutir el contexto regulatorio.
- Olvidar que el **MINSA no es la única red**: existen también
  EsSalud, sanidad militar/policial y privados. Cuando se hable del
  ecosistema peruano completo, mencionarlo.
