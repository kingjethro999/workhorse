# =============================================================================
# Workhorse Windows PowerShell Universal Setup Script
# =============================================================================
$InstallDir = if ($MyInvocation.MyCommand.Path) { Split-Path -Parent $MyInvocation.MyCommand.Path } else { $null }
if (-not $InstallDir -or -not (Test-Path (Join-Path $InstallDir "workhorse.py"))) {
    $InstallDir = Join-Path $env:USERPROFILE "workhorse"
    if (-not (Test-Path $InstallDir)) {
        Write-Host "[*] Cloning Workhorse repository to $InstallDir..." -ForegroundColor Cyan
        git clone https://github.com/kingjethro999/workhorse.git $InstallDir
    }
}
$VenvPython = Join-Path $InstallDir ".venv\Scripts\python.exe"
$MainScript = Join-Path $InstallDir "workhorse.py"

if (-not (Test-Path $VenvPython)) {
    Write-Host "[*] Creating Python virtual environment in .venv..." -ForegroundColor Cyan
    python -m venv (Join-Path $InstallDir ".venv")
    & $VenvPython -m pip install --upgrade pip
    & $VenvPython -m pip install -r (Join-Path $InstallDir "requirements.txt")
}

$UserBin = Join-Path $env:USERPROFILE "bin"
if (-not (Test-Path $UserBin)) {
    New-Item -ItemType Directory -Path $UserBin | Out-Null
}

$CmdContent = @"
@echo off
set "WORKHORSE_INVOCATION_CWD=%CD%"
set "WORKHORSE_INSTALL_DIR=$InstallDir"
"$VenvPython" "$MainScript" %*
"@

Set-Content -Path (Join-Path $UserBin "workhorse.cmd") -Value $CmdContent
Set-Content -Path (Join-Path $UserBin "workhouse.cmd") -Value $CmdContent
Set-Content -Path (Join-Path $UserBin "wh.cmd") -Value $CmdContent

Write-Host "[SUCCESS] Workhorse installed as 'workhorse', 'workhouse', and 'wh' in $UserBin" -ForegroundColor Green
