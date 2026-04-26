---
name: thesis-fuentes-derecho
description: |
  Carga este skill cuando se necesite buscar, evaluar o descargar
  fuentes para una tesis de Derecho. Complementa a `thesis-fuentes`
  (genérico) con bases especializadas, criterios de validez normativa
  y APIs/portales jurídicos peruanos.
---

# Skill: fuentes para tesis de Derecho

Este skill define **dónde**, **cómo** y **bajo qué criterios** buscar
fuentes jurídicas. No reemplaza a `thesis-citas-apa7`: una vez
descargada la fuente, la cita se construye con el formato del skill
`thesis-dominio-derecho` § 4.

## 1. Bases de búsqueda — orden recomendado

### A. Legislación peruana
1. **SPIJ** (`spij.minjus.gob.pe`) — Sistema Peruano de Información
   Jurídica del MINJUS. Verifica vigencia y muestra historial de
   modificaciones. **Siempre validar aquí** la versión vigente de
   cualquier ley citada.
2. **Diario Oficial El Peruano** (`elperuano.pe`) — texto oficial
   publicado el día de promulgación. Útil para Decretos de Urgencia
   recientes.
3. **Plataforma Digital Única del Estado** (`gob.pe/normas`) — versión
   consolidada por entidad.

### B. Jurisprudencia
1. **TC**: `tc.gob.pe/jurisprudencia` — buscador por expediente, materia
   o precedente vinculante.
2. **Poder Judicial**: `consultasenlinea.pj.gob.pe` para casaciones y
   plenos casatorios.
3. **Corte IDH**: `corteidh.or.cr/casos-sentencias` — sentencias contra
   Perú son altamente citables.
4. **vLex Perú** (suscripción institucional) — agrega legislación +
   jurisprudencia + doctrina con buscador unificado.

### C. Doctrina nacional
1. **Repositorios universitarios**:
   - PUCP: `tesis.pucp.edu.pe`, `revistas.pucp.edu.pe`.
   - UNMSM: `cybertesis.unmsm.edu.pe`.
   - U. de Lima: `repositorio.ulima.edu.pe`.
   - UPC, USMP, UDEP, U. del Pacífico, ESAN.
2. **Revistas peruanas indexadas**:
   - Derecho PUCP (Latindex, Scielo).
   - Themis Revista de Derecho.
   - IUS ET VERITAS.
   - Foro Jurídico (PUCP).
   - Pensamiento Constitucional.
3. **Editoriales jurídicas**: Gaceta Jurídica, Palestra, Grijley, ARA,
   Idemsa.

### D. Doctrina internacional
1. **Dialnet** (`dialnet.unirioja.es`) — España + Hispanoamérica.
2. **SciELO** (filtrar por área "Ciencias Sociales > Derecho").
3. **SSRN Legal Scholarship Network** (`papers.ssrn.com`).
4. **HeinOnline** (suscripción) — derecho anglosajón histórico.
5. **JSTOR Law** y **Westlaw** (suscripción).
6. Revistas Q1 Scopus categoría Law: *American Journal of Comparative
   Law*, *Modern Law Review*, *Oxford Journal of Legal Studies*.

## 2. Criterios de validez para citar

Antes de incorporar una fuente al manuscrito, validar:

- [ ] **Autoridad**: autor con producción académica verificable
      (perfil ORCID, Scopus, repositorio institucional).
- [ ] **Vigencia normativa**: si es legislación, ¿está vigente o
      derogada? Si está modificada, ¿qué versión cito?
- [ ] **Recencia**: ¿últimos 10 años? Si es más antigua, ¿es clásica
      fundacional?
- [ ] **Pertinencia**: ¿la rama del Derecho coincide con la tesis?
- [ ] **Indexación** (para doctrina): Scopus / WoS / Scielo / Latindex.
- [ ] **Acceso**: descargué el PDF original (no captura ni resumen)
      y lo guardé en `content/sources/`.

## 3. Estructura recomendada en `content/sources/`

Para tesis de Derecho:

```
content/sources/
├── legislacion/
│   ├── nacional/        # Constitución, leyes, DL, DS peruanos
│   └── comparada/       # legislación extranjera relevante
├── jurisprudencia/
│   ├── tc/              # sentencias del Tribunal Constitucional
│   ├── corte-suprema/   # casaciones y plenos casatorios
│   └── corte-idh/       # sentencias de la Corte IDH
├── doctrina/
│   ├── nacional/        # autores peruanos
│   └── internacional/   # autores extranjeros
└── tratados/            # tratados internacionales ratificados
```

> Cuando hagas el fork, ajustar `content/sources/README.md` con esta
> estructura y borrar `international/` y `national/` heredadas.

## 4. Convenciones de naming de archivos

```
<año>_<entidad o autor>_<slug-del-titulo-corto>.<ext>

Ejemplos:
2001_Ley27444_procedimiento-administrativo-general.pdf
2017_CSJR_casacion-4442-2015-moquegua-v-pleno-civil.pdf
2004_TC_exp-0008-2003-AI-libertad-empresa.pdf
2023_RubioCorrea_interpretacion-constitucion.pdf
```

## 5. Búsquedas eficientes (queries reusables)

### En Google Scholar
```
"<institución jurídica>" "Perú" filetype:pdf  site:.edu.pe
"<doctrina>" autor:"<apellido>"  -site:scribd.com
```

### En SPIJ
- Filtrar por "Norma vigente" para evitar citar leyes derogadas.
- Cuando hay reformas, descargar **TUO** (Texto Único Ordenado) si existe.

### En vLex
- Usar booleanos: `("imputación objetiva" OR "criterio del riesgo") AND penal`.
- Filtrar por país: Perú.

## 6. Anti-patrones (NO hacer)

- ❌ Citar Wikipedia, blogs no académicos, redes sociales.
- ❌ Citar leyes sin verificar vigencia en SPIJ.
- ❌ Citar sentencias sin número de expediente y fecha.
- ❌ Citar "doctrina alemana" o "doctrina española" sin autor concreto.
- ❌ Confundir doctrina con jurisprudencia ("según la jurisprudencia
  de Roxin" — Roxin es doctrina, no jurisprudencia).
- ❌ Descargar resúmenes de e-Justice o blogs sin volver al texto
  original.

## 7. Flujo recomendado al iniciar la tesis

1. Definir las **palabras clave jurídicas** (3-5 conceptos centrales).
2. Por cada palabra clave, buscar:
   - **Norma matriz** (artículo constitucional + ley específica).
   - **Sentencia hito** (TC o Corte Suprema).
   - **Autor referente nacional + internacional**.
3. Construir tabla de fuentes en `content/observations/fuentes-base.md`
   con: tipo / cita / pertinencia / estado de lectura.
4. Avanzar el marco teórico solo después de tener ≥ 30 fuentes
   validadas.
