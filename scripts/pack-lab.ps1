$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

# run from repo root
Set-Location "$PSScriptRoot\.."

$paths = @(
  'core',
  'experiments',           # <- packs ALL experiments
  'main.py',
  'config.default.yaml',
  'requirements.txt'
) | Where-Object { Test-Path $_ }

New-Item -ItemType Directory -Force -Path dist | Out-Null
$zip = 'dist\vireon-lab.zip'
if (Test-Path $zip) { Remove-Item $zip -Force }

Compress-Archive -Path $paths -DestinationPath $zip -Force

# checksum
$sha = (Get-FileHash -Algorithm SHA256 $zip).Hash
"$sha  vireon-lab.zip" | Set-Content 'dist\vireon-lab.zip.sha256'

Write-Host "Packed $zip"
Write-Host "SHA256 $sha"
