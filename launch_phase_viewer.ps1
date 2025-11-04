# ☄️ Polyrifringence Engine v6.8
# Phase Trace Viewer – Localhost Launcher
# --------------------------------------------------------
# Spins up a lightweight Python HTTP server and opens
# the Phase Trace Viewer automatically in your browser.
# --------------------------------------------------------

# Move to examples directory
Set-Location "$PSScriptRoot\examples"

# Port can be changed if 8000 is in use
$Port = 8000
$ViewerFile = "phase_trace_viewer.html"

Write-Host ""
Write-Host "🧠 Polyrifringence Engine v6.8 — Phase Trace Viewer" -ForegroundColor Cyan
Write-Host "🌐 Starting local server on http://localhost:$Port" -ForegroundColor Yellow
Write-Host "📄 Opening $ViewerFile ..." -ForegroundColor Green
Write-Host ""

# Launch browser
Start-Process "http://localhost:$Port/$ViewerFile"

# Start simple HTTP server
python -m http.server $Port
