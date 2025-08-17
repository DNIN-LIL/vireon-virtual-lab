$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

# repo root
Set-Location "$PSScriptRoot\.."

# ensure venv
$venv = Join-Path (Get-Location) 'venv'
if (-not (Test-Path $venv)) {
  Write-Host "Creating venv at $venv ..."
  if (Get-Command py -ErrorAction SilentlyContinue) { py -3 -m venv $venv }
  else { python -m venv $venv }
}

# activate (Windows)
& "$venv\Scripts\Activate.ps1"

# deps
if (Test-Path .\requirements.txt) {
  python -m pip install --upgrade pip
  pip install -r requirements.txt
}

# pass all args straight through to main.py
python .\main.py @args
