@echo off
setlocal EnableExtensions
chcp 65001 >nul
title Bad Wolf — Gesamtstart (OmniRoute + Schaltwerk)
cd /d "%~dp0"

echo ==========================================================
echo   Bad Wolf — Gesamtstart
echo   1. OmniRoute  (Node.js)   -> http://127.0.0.1:20128
echo   2. Schaltwerk (Python)    -> http://127.0.0.1:8765
echo ==========================================================
echo.

where node >nul 2>&1
if errorlevel 1 (
  echo  [!] Node.js fehlt. Benoetigt: Version 22.22.2 oder neuer.
  echo      https://nodejs.org/  ^(LTS installieren, "Add to PATH" anhaeken^)
  pause
  exit /b 1
)

echo [1/2] OmniRoute vorbereiten ...
cd /d "%~dp0omniroute"
if not exist node_modules (
  echo   node_modules fehlt - installiere Pakete ^(einmalig, dauert Minuten^) ...
  call npm ci --no-audit --no-fund
  if errorlevel 1 (
    echo   [!] npm ci fehlgeschlagen. Internet an?
    pause
    exit /b 1
  )
)
echo   Optionale Pakete pruefen/beheben ...
call node scripts\setup\fix-optional-deps.mjs
start "OmniRoute (20128)" cmd /c "cd /d %~dp0omniroute && npm run dev"

cd /d "%~dp0"
echo [2/2] Schaltwerk starten ...
start "Schaltwerk (8765)" cmd /c "cd /d %~dp0schaltwerk && call STARTEN.bat"

echo.
echo   Beide Fenster offen lassen. Erster Start von OmniRoute braucht
echo   1-2 Minuten Kompilierzeit - danach Dashboard-Login:
echo     http://127.0.0.1:20128   (Passwort: INITIAL_PASSWORD oder CHANGEME)
echo   Schaltwerk:  http://127.0.0.1:8765
echo   Key mit manage-Scope im OmniRoute-Dashboard anlegen und einmal
echo   in Schaltwerk eintragen - danach verbindet Schaltwerk automatisch.
echo.
echo   Beenden: beide Konsolenfenster schliessen ^(Strg+C^).
pause
