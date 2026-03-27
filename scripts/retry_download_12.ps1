$ErrorActionPreference = 'Stop'

$base = 'E:\Maestria\Seminario_De_Investigacion\Investigación\fuentes\nuevos_12_2026'
$intDir = Join-Path $base 'internacionales'
$natDir = Join-Path $base 'nacionales'

$targets = @(
    [pscustomobject]@{
        Group='internacionales'; File='01_Gazzarata_2024_10.1016-j.ijmedinf.2024.105507.pdf';
        Urls=@(
            'https://www.sciencedirect.com/science/article/pii/S1386505624001709/pdfft?isDTMRedir=true&download=true',
            'https://www.sciencedirect.com/science/article/pii/S1386505624001709/pdfft',
            'https://www.sciencedirect.com/science/article/pii/S1386505624001709'
        )
    },
    [pscustomobject]@{
        Group='internacionales'; File='02_PedreraJimenez_2023_10.2196-48702.pdf';
        Urls=@('https://www.jmir.org/2023/1/e48702/PDF')
    },
    [pscustomobject]@{
        Group='internacionales'; File='03_Chatterjee_2022_10.3390-s22103756.pdf';
        Urls=@('https://www.mdpi.com/1424-8220/22/10/3756/pdf?version=1653025877')
    },
    [pscustomobject]@{
        Group='internacionales'; File='04_GaudetBlavignac_2021_10.2196-27591.pdf';
        Urls=@('https://medinform.jmir.org/2021/6/e27591/PDF')
    },
    [pscustomobject]@{
        Group='internacionales'; File='05_MukhiyaLamo_2021_10.1177-14604582211043920.pdf';
        Urls=@(
            'https://journals.sagepub.com/doi/epdf/10.1177/14604582211043920',
            'https://journals.sagepub.com/doi/pdf/10.1177/14604582211043920'
        )
    },
    [pscustomobject]@{
        Group='internacionales'; File='06_Fernandez_2025_10.3389-fdgth.2025.1622302.pdf';
        Urls=@('https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2025.1622302/pdf')
    },
    [pscustomobject]@{
        Group='nacionales'; File='08_AriasGeronimo_2025_hdl_20.500.14005-16817.pdf';
        Urls=@(
            'https://repositorio.usil.edu.pe/server/api/core/bitstreams/f7340267-0ba2-4413-b5f9-93e6b3fd3914/content',
            'https://repositorio.usil.edu.pe/bitstreams/f7340267-0ba2-4413-b5f9-93e6b3fd3914/download'
        )
    },
    [pscustomobject]@{
        Group='nacionales'; File='10_FernandezInfanzon_Huarac_2021_hdl_20.500.12640-2139.pdf';
        Urls=@(
            'https://repositorio.esan.edu.pe/server/api/core/bitstreams/f639f09f-537c-4889-ab60-3721b9b47d78/content',
            'https://repositorio.esan.edu.pe/bitstreams/f639f09f-537c-4889-ab60-3721b9b47d78/download'
        )
    },
    [pscustomobject]@{
        Group='nacionales'; File='11_Bran_2024_10.3991-ijoe.v20i15.51515.pdf';
        Urls=@(
            'https://online-journals.org/index.php/i-joe/article/download/51515/15631',
            'https://ebuah.uah.es/dspace/bitstream/10017/63704/3/Interoperability_Bran_iJOE_2024.pdf'
        )
    },
    [pscustomobject]@{
        Group='nacionales'; File='12_MoralesCamargo_2023_10.56294-sctconf2023455.pdf';
        Urls=@('https://conferencias.saludcyt.ar/index.php/sctconf/article/download/455/398')
    }
)

function Test-IsValidPdf {
    param([string]$Path)
    if (!(Test-Path $Path)) { return $false }
    $fi = Get-Item $Path
    if ($fi.Length -le 10240) { return $false }
    $bytes = [System.IO.File]::ReadAllBytes($Path)
    if ($bytes.Length -lt 4) { return $false }
    return ($bytes[0] -eq 37 -and $bytes[1] -eq 80 -and $bytes[2] -eq 68 -and $bytes[3] -eq 70)
}

$retryResults = @()

foreach ($t in $targets) {
    $dir = if ($t.Group -eq 'internacionales') { $intDir } else { $natDir }
    $out = Join-Path $dir $t.File
    $tmp = "$out.tmp"

    $downloaded = $false
    $detail = 'No success URL'

    foreach ($url in $t.Urls) {
        try {
            if (Test-Path $tmp) { Remove-Item $tmp -Force }
            & curl.exe -L -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' -H 'Accept: application/pdf,*/*;q=0.8' --connect-timeout 20 --max-time 180 -o $tmp $url | Out-Null

            if (Test-IsValidPdf -Path $tmp) {
                Move-Item -Force $tmp $out
                $downloaded = $true
                $sizeKb = [math]::Round((Get-Item $out).Length / 1KB, 1)
                $detail = "OK from $url ($sizeKb KB)"
                break
            }
            else {
                if (Test-Path $tmp) { Remove-Item $tmp -Force }
                $detail = "Invalid PDF from $url"
            }
        }
        catch {
            if (Test-Path $tmp) { Remove-Item $tmp -Force }
            $detail = "Error with $url :: $($_.Exception.Message)"
        }
    }

    $retryResults += [pscustomobject]@{
        group = $t.Group
        file = $t.File
        status = if ($downloaded) { 'downloaded' } else { 'failed' }
        detail = $detail
    }
}

$retryReport = Join-Path $base 'download_retry_report_12.csv'
$retryResults | Export-Csv -NoTypeInformation -Encoding UTF8 -Path $retryReport
$retryResults | Sort-Object group, file | Format-Table -AutoSize
Write-Host "\nReporte retry guardado en: $retryReport"
