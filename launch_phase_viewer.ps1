param (
    # Optional port override (default: 8000)
    [int]$Port = 8000,

    # Suppress automatic browser launch (headless / remote use)
    [switch]$NoBrowser
)

# ☄️ Polyrifringence Engine — Phase Trace Viewer
# Localhost Launcher
# --------------------------------------------------------
# Spins up a lightweight Python HTTP server and opens
# the Phase Trace Viewer in your default browser.
#
# This viewer is a passive inspection and visualization
# tool. It does not execute engine logic, modify state,
# or perform computation.
#
# Designed to remain valid across engine versions (v8.x+)
# and align with future launch_engine.ps1 and benchmark
# launcher scripts.
# --------------------------------------------------------

Write-Host ""

# Semantic anchor for future shared launcher logic
$LauncherMode = "viewer"

# Resolve script root safely
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$ExamplesPath = Join-Path $Root "examples"

if (-not (Test-Path $ExamplesPath)) {
    Write-Host "❌ examples/ directory not found." -ForegroundColor Red
    exit 1
}

Set-Location $ExamplesPath

# Viewer file
$ViewerFile = "phase_trace_viewer.html"

if (-not (Test-Path $ViewerFile)) {
    Write-Host "❌ Viewer file not found: $ViewerFile" -ForegroundColor Red
    exit 1
}

# Pre-flight: check port availability
if (Test-NetConnection -ComputerName "localhost" -Port $Port -InformationLevel Quiet) {
    Write-Host "❌ Port $Port is already in use." -ForegroundColor Red
    Write-Host "   Try: ./launch_phase_viewer.ps1 -Port 8081" -ForegroundColor DarkGray
    exit 1
}

# Detect Python executable
$PythonCmd = $null
if (Get-Command python -ErrorAction SilentlyContinue) {
    $PythonCmd = "python"
} elseif (Get-Command python3 -ErrorAction SilentlyContinue) {
    $PythonCmd = "python3"
} else {
    Write-Host "❌ Python not found. Install Python 3.x to continue." -ForegroundColor Red
    exit 1
}

Write-Host "------------------------------------------------------------" -ForegroundColor DarkGray
Write-Host "🧠 Polyrifringence Engine — Phase Trace Viewer" -ForegroundColor Cyan
Write-Host "📂 Directory : $ExamplesPath" -ForegroundColor DarkGray
Write-Host "🐍 Python    : $PythonCmd" -ForegroundColor DarkGray
Write-Host "🌐 Server    : http://localhost:$Port" -ForegroundColor Yellow
Write-Host "📄 Viewer    : $ViewerFile" -ForegroundColor Green
Write-Host "------------------------------------------------------------" -ForegroundColor DarkGray
Write-Host ""

# Launch browser (unless suppressed)
if (-not $NoBrowser) {
    Start-Process "http://localhost:$Port/$ViewerFile"
}

# Start HTTP server with graceful shutdown notice
try {
    & $PythonCmd -m http.server $Port
}
finally {
    Write-Host ""
    Write-Host "🛑 Phase Trace Viewer server stopped." -ForegroundColor DarkYellow
}

# Future: shared launcher utilities (env checks, logging, cleanup)
# . "$Root\_common_launcher.ps1"
