---
name: thesis-fuentes
description: Buscar, validar, descargar y catalogar fuentes académicas (artículos Q1/Q2, tesis, normativa). Usar cuando el usuario pide "buscar fuentes", "descargar el PDF de…", "agregar una referencia con DOI…", o cuando hay que ampliar antecedentes/bases teóricas.
---

# Búsqueda y descarga de fuentes

## Pipeline de búsqueda

1. **Refinar palabras clave** en español + inglés. Combinar con `AND` / `OR`.
   Guardar el set de keywords en `content/drafts/` para reproducibilidad.
2. **Bases recomendadas** (en este orden de confiabilidad):
   - Crossref (`api.crossref.org/works?query=...`) → metadata + DOI.
   - OpenAlex (`api.openalex.org/works?search=...`) → metadata + URL al PDF
     en `open_access.oa_url` o `best_oa_location.pdf_url`.
   - Scielo / Redalyc / DOAJ → cobertura regional y acceso abierto.
   - Repositorios institucionales → tesis nacionales o locales.
   - Bases especializadas del dominio → definirlas en
     `thesis-fuentes-<dominio>` si el tema lo requiere.
3. **Criterios de inclusión** a completar por tema:
   - Ventana temporal: `<años>` (justificar excepciones para clásicos).
   - Tipo: artículos revisados por pares, tesis, normas, reportes técnicos o
     datasets, según el diseño.
   - Idioma: `<idiomas aceptados>`.
   - Calidad: cuartil, indexación, fuente oficial, revisión por pares,
     pertinencia metodológica o vigencia normativa.
4. **Clasificar el cuartil** explícitamente en tres grupos: *núcleo
   recomendado*, *soporte complementario*, *uso con cautela*.

## Descarga (PowerShell)

Plantilla idempotente con validación de firma `%PDF`:

```powershell
$base = 'content/sources/<grupo>'
New-Item -ItemType Directory -Force -Path $base | Out-Null

$items = @(
    [pscustomobject]@{ File='NN_Apellido_Year_doi.pdf'; Url='https://...' }
    # ...
)

foreach ($item in $items) {
    $out = Join-Path $base $item.File
    if (Test-Path $out) { continue }   # idempotente
    try {
        Invoke-WebRequest -Uri $item.Url -OutFile $out -MaximumRedirection 10 -TimeoutSec 120
        $b = [System.IO.File]::ReadAllBytes($out)[0..3]
        $isPdf = $b[0] -eq 37 -and $b[1] -eq 80 -and $b[2] -eq 68 -and $b[3] -eq 70
        if (-not $isPdf -or (Get-Item $out).Length -lt 10240) {
            Remove-Item $out
            Write-Host "INVALID: $($item.File)" -ForegroundColor Yellow
        }
    } catch { Write-Host "FAIL: $($item.Url)" -ForegroundColor Red }
}
```

Para lotes masivos, copiar
[platform/scripts/downloads/template_download_sources.ps1](../../../platform/scripts/downloads/template_download_sources.ps1)
y completarlo dentro del fork.

## Cuando la descarga falla (Cloudflare / JS challenge)

Síntomas: archivo bajado pero los primeros bytes no son `%PDF` (suele ser HTML).
Acciones:

1. Probar URL alternativa de OpenAlex o repositorio institucional.
2. Probar URL del editor usando el DOI directo.
3. Si el portal requiere navegador, **no insistir con curl/Invoke-WebRequest**:
   añadir el ítem a `content/sources/<grupo>/PENDIENTES_DESCARGA_MANUAL.md` con:
   - Cita APA completa
   - DOI / handle
   - URL editor
   - Estado: `pendiente — requiere navegador / acceso institucional`
4. Si el bloqueo persiste, registrar la fuente como pendiente en vez de
   guardar HTML renombrado como PDF.

## Convención de nombres

```
NN_<ApellidoPrimerAutor>_<Año>_<slug-identificador>.pdf
NN_<ApellidoPrimerAutor>_<Año>_<slug-identificador>.txt
```

donde `NN` es un número ordinal por grupo, y `doi-slug` reemplaza `/` por `-`.

## Catalogación obligatoria post-descarga

Para cada PDF nuevo:

1. Generar **gemelo `.txt`** con el texto extraído (usado por grep para
   recuperar citas y datos sin abrir el PDF):

   ```powershell
   pdftotext -layout "ruta.pdf" "ruta.txt"
   ```

   (alternativa: `pypdf` si pdftotext no está instalado).
2. Registrar la fuente en una matriz de `content/drafts/` con: año, autor,
   título, tipo de fuente, DOI/URL/handle, disponibilidad y aporte.
3. Si va a aparecer en el cuerpo, agregar entrada APA a `# Referencias` en
   `content/manuscript/Documento_Tesis.md` (ver `thesis-citas-apa7`).

## Reglas para tesis o trabajos académicos

- Usar handle como identificador (`hdl.handle.net/20.500.xxxxx/yyyy`) cuando
  no haya DOI.
- Tipo entre corchetes: `[Tesis de maestría, Universidad X]` o
  `[Trabajo de suficiencia profesional, Universidad X]`.
- Repositorio al final: `Repositorio <Institución>`.

## Anti-patrones

- Aceptar como "descargado" un archivo cuyos primeros bytes no son `%PDF`.
- Mezclar internacionales con nacionales en el mismo subfolder.
- Citar en el cuerpo una fuente que no existe físicamente en `content/sources/`.
- Renombrar PDFs ya catalogados (rompe los enlaces de `PENDIENTES_*.md`).
