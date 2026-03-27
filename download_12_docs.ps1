$ErrorActionPreference = 'Stop'

$base = 'E:\Maestria\Seminario_De_Investigacion\Investigación\fuentes\nuevos_12_2026'
$intDir = Join-Path $base 'internacionales'
$natDir = Join-Path $base 'nacionales'

New-Item -ItemType Directory -Force -Path $intDir | Out-Null
New-Item -ItemType Directory -Force -Path $natDir | Out-Null

$items = @(
    [pscustomobject]@{ Group='internacionales'; File='01_Gazzarata_2024_10.1016-j.ijmedinf.2024.105507.pdf'; Url='https://content.openalex.org/works/W4399360943.pdf' },
    [pscustomobject]@{ Group='internacionales'; File='02_PedreraJimenez_2023_10.2196-48702.pdf'; Url='https://content.openalex.org/works/W4389062494.pdf' },
    [pscustomobject]@{ Group='internacionales'; File='03_Chatterjee_2022_10.3390-s22103756.pdf'; Url='https://content.openalex.org/works/W4280498943.pdf' },
    [pscustomobject]@{ Group='internacionales'; File='04_GaudetBlavignac_2021_10.2196-27591.pdf'; Url='https://content.openalex.org/works/W3163217846.pdf' },
    [pscustomobject]@{ Group='internacionales'; File='05_MukhiyaLamo_2021_10.1177-14604582211043920.pdf'; Url='https://journals.sagepub.com/doi/pdf/10.1177/14604582211043920' },
    [pscustomobject]@{ Group='internacionales'; File='06_Fernandez_2025_10.3389-fdgth.2025.1622302.pdf'; Url='https://content.openalex.org/works/W4413297856.pdf' },

    [pscustomobject]@{ Group='nacionales'; File='07_EsparzaMorgan_2025_hdl_20.500.14005-16177.pdf'; Url='https://repositorio.usil.edu.pe/bitstreams/2b35d727-6c70-4d91-9146-fd68e1d2570a/download' },
    [pscustomobject]@{ Group='nacionales'; File='08_AriasGeronimo_2025_hdl_20.500.14005-16817.pdf'; Url='https://repositorio.usil.edu.pe/bitstreams/f7340267-0ba2-4413-b5f9-93e6b3fd3914/download' },
    [pscustomobject]@{ Group='nacionales'; File='09_SanchezCalle_2024_hdl_20.500.12866-17191.pdf'; Url='https://repositorio.upch.edu.pe/bitstream/handle/20.500.12866/17191/Arquitectura_SanchezCalle_David.pdf?sequence=1&isAllowed=y' },
    [pscustomobject]@{ Group='nacionales'; File='10_FernandezInfanzon_Huarac_2021_hdl_20.500.12640-2139.pdf'; Url='https://repositorio.esan.edu.pe/bitstreams/f639f09f-537c-4889-ab60-3721b9b47d78/download' },
    [pscustomobject]@{ Group='nacionales'; File='11_Bran_2024_10.3991-ijoe.v20i15.51515.pdf'; Url='https://content.openalex.org/works/W4405070420.pdf' },
    [pscustomobject]@{ Group='nacionales'; File='12_MoralesCamargo_2023_10.56294-sctconf2023455.pdf'; Url='https://content.openalex.org/works/W4392830469.pdf' }
)

$results = @()

foreach ($item in $items) {
    $targetDir = if ($item.Group -eq 'internacionales') { $intDir } else { $natDir }
    $outputPath = Join-Path $targetDir $item.File
    $status = 'failed'
    $detail = ''

    try {
        Invoke-WebRequest -Uri $item.Url -OutFile $outputPath -MaximumRedirection 10 -TimeoutSec 120

        $fileInfo = Get-Item $outputPath
        $bytes = [System.IO.File]::ReadAllBytes($outputPath)
        $isPdf = $bytes.Length -ge 4 -and $bytes[0] -eq 37 -and $bytes[1] -eq 80 -and $bytes[2] -eq 68 -and $bytes[3] -eq 70

        if ($isPdf -and $fileInfo.Length -gt 10240) {
            $status = 'downloaded'
            $detail = "OK $([math]::Round($fileInfo.Length / 1KB, 1))KB"
        } else {
            $detail = "INVALID $([math]::Round($fileInfo.Length / 1KB, 1))KB"
        }
    }
    catch {
        $detail = $_.Exception.Message
    }

    $results += [pscustomobject]@{
        group = $item.Group
        file = $item.File
        status = $status
        detail = $detail
        url = $item.Url
    }
}

$reportPath = Join-Path $base 'download_report_12.csv'
$results | Export-Csv -NoTypeInformation -Encoding UTF8 -Path $reportPath

$results | Sort-Object group, file | Format-Table -AutoSize
Write-Host "\nReporte guardado en: $reportPath"
