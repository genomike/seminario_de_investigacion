# Pendientes de descarga manual (3 de 12)

Guarda cada PDF con el nombre exacto indicado.

## 1) Gazzarata 2024 (internacional)
- Nombre destino:
  - `fuentes/nuevos_12_2026/internacionales/01_Gazzarata_2024_10.1016-j.ijmedinf.2024.105507.pdf`
- DOI:
  - https://doi.org/10.1016/j.ijmedinf.2024.105507
- ScienceDirect (PII):
  - https://www.sciencedirect.com/science/article/pii/S1386505624001709
- Enlace de intento directo PDF (si tu sesión lo permite):
  - https://www.sciencedirect.com/science/article/pii/S1386505624001709/pdfft?isDTMRedir=true&download=true

## 2) Chatterjee 2022 (internacional)
- Nombre destino:
  - `fuentes/nuevos_12_2026/internacionales/03_Chatterjee_2022_10.3390-s22103756.pdf`
- DOI:
  - https://doi.org/10.3390/s22103756
- Landing del artículo:
  - https://www.mdpi.com/1424-8220/22/10/3756
- Enlace PDF MDPI:
  - https://www.mdpi.com/1424-8220/22/10/3756/pdf
- Alternativa PMC (si abre en tu navegador):
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC9147872/

## 3) Morales-Camargo 2023 (nacional)
- Nombre destino:
  - `fuentes/nuevos_12_2026/nacionales/12_MoralesCamargo_2023_10.56294-sctconf2023455.pdf`
- DOI:
  - https://doi.org/10.56294/sctconf2023455
- Landing editorial actual:
  - https://conferencias.ageditor.ar/index.php/sctconf/article/view/373
- Galley/PDF (puede requerir resolver protección web):
  - https://conferencias.ageditor.ar/index.php/sctconf/article/view/373/497

## Verificación rápida después de descargar
En PowerShell, ejecuta:

```powershell
$files = @(
  'E:/Maestria/Seminario_De_Investigacion/Investigación/fuentes/nuevos_12_2026/internacionales/01_Gazzarata_2024_10.1016-j.ijmedinf.2024.105507.pdf',
  'E:/Maestria/Seminario_De_Investigacion/Investigación/fuentes/nuevos_12_2026/internacionales/03_Chatterjee_2022_10.3390-s22103756.pdf',
  'E:/Maestria/Seminario_De_Investigacion/Investigación/fuentes/nuevos_12_2026/nacionales/12_MoralesCamargo_2023_10.56294-sctconf2023455.pdf'
)
foreach ($f in $files) {
  $b = [System.IO.File]::ReadAllBytes($f)
  $isPdf = ($b.Length -ge 5 -and $b[0]-eq 37 -and $b[1]-eq 80 -and $b[2]-eq 68 -and $b[3]-eq 70 -and $b[4]-eq 45)
  Write-Host "$f -> isPdf=$isPdf size=$($b.Length)"
}
```
