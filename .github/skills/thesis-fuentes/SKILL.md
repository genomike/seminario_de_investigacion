---
name: thesis-fuentes
description: Buscar, validar, descargar y catalogar fuentes académicas (artículos Q1/Q2, tesis, normativa). Usar cuando el usuario pide "buscar fuentes", "descargar el PDF de…", "agregar una referencia con DOI…", o cuando hay que ampliar antecedentes/bases teóricas.
---

# Búsqueda y descarga de fuentes

## Pipeline de búsqueda

1. **Refinar palabras clave** en español + inglés. Combinar con `AND` / `OR`.
   Guardar el set de keywords en `tesis/problema-unificado.md` (o equivalente)
   para reproducibilidad.
2. **Bases recomendadas** (en este orden de confiabilidad):
   - Crossref (`api.crossref.org/works?query=...`) → metadata + DOI.
   - OpenAlex (`api.openalex.org/works?search=...`) → metadata + URL al PDF
     en `open_access.oa_url` o `best_oa_location.pdf_url`.
   - JMIR / Frontiers / BMC / MDPI / Oxford Academic / Lancet → directo del DOI.
   - Repositorios institucionales para tesis nacionales (UNFV, PUCP, USIL, UPCH, ESAN).
3. **Criterios de inclusión** acordados:
   - Ventana 2022-2026 (recientes; aceptar ≥2019 solo para clásicos).
   - Tipo: `journal-article` o tesis con DOI/handle verificable.
   - Idioma: inglés o español.
   - Q1/Q2 indicativo (verificar en SCImago/JCR antes de defensa).
4. **Clasificar el cuartil** explícitamente en tres grupos: *núcleo
   recomendado*, *soporte complementario*, *uso con cautela* (ver
   `tesis/Elaboración_Tesis.md` para ejemplo).

## Descarga (PowerShell)

Plantilla idempotente con validación de firma `%PDF`:

```powershell
$base = 'fuentes/<grupo>'
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

Ver ejemplo real en [platform/scripts/downloads/download_12_docs.ps1](../../../platform/scripts/downloads/download_12_docs.ps1).

## Cuando la descarga falla (Cloudflare / JS challenge)

Síntomas: archivo bajado pero los primeros bytes no son `%PDF` (suele ser HTML).
Acciones:

1. Probar URL alternativa de OpenAlex (`content.openalex.org/works/Wxxx.pdf`).
2. Probar URL del editor (Elsevier/SAGE) usando el DOI directo.
3. Si el portal requiere navegador, **no insistir con curl/Invoke-WebRequest**:
   añadir el ítem a `fuentes/<grupo>/PENDIENTES_DESCARGA_MANUAL.md` con:
   - Cita APA completa
   - DOI / handle
   - URL editor
   - Estado: `pendiente — requiere navegador / acceso institucional`
4. Editores conocidos como bloqueadores: ScienceDirect, MDPI (a veces), AGEDITOR.

## Convención de nombres

```
NN_<ApellidoPrimerAutor>_<Año>_<doi-slug>.pdf
NN_<ApellidoPrimerAutor>_<Año>_hdl_<handle-slug>.pdf   # tesis con handle
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
2. Registrar la fuente en la tabla del paso 3 de `tesis/Elaboración_Tesis.md`
   con: año, autor, título, revista, DOI, disponibilidad.
3. Si va a aparecer en el cuerpo, agregar entrada APA a `# Referencias` en
   `content/manuscript/Documento_Tesis.md` (ver `thesis-citas-apa7`).

## Reglas para tesis nacionales

- Usar handle como identificador (`hdl.handle.net/20.500.xxxxx/yyyy`) cuando
  no haya DOI.
- Tipo entre corchetes: `[Tesis de maestría, Universidad X]` o
  `[Trabajo de suficiencia profesional, Universidad X]`.
- Repositorio al final: `Repositorio UNFV`, `Repositorio PUCP`, etc.

## Anti-patrones

- Aceptar como "descargado" un archivo cuyos primeros bytes no son `%PDF`.
- Mezclar internacionales con nacionales en el mismo subfolder.
- Citar en el cuerpo una fuente que no existe físicamente en `content/sources/`.
- Renombrar PDFs ya catalogados (rompe los enlaces de `PENDIENTES_*.md`).
