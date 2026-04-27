<#
Plantilla agnostica para descarga catalogada de fuentes.

Copiar como download_<lote>.ps1 en un fork si se requiere descarga masiva.
No guardar URLs, DOIs, nombres de autores ni titulos de una tesis concreta en
`platform/` despues de completar el lote; mover esos insumos a `content/`.
#>

param(
    [string]$OutputDir = "content/sources/international"
)

$ErrorActionPreference = "Stop"

$sources = @(
    # @{ Name = "NN_Autor_Ano_TituloCorto.pdf"; Url = "<URL_DE_DESCARGA>" }
)

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

foreach ($source in $sources) {
    $target = Join-Path $OutputDir $source.Name
    Write-Host "Descargando $($source.Name)"
    Invoke-WebRequest -Uri $source.Url -OutFile $target
}