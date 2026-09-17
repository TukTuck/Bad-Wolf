#!/usr/bin/env bash
# Bad Wolf — Gesamtstart (OmniRoute + Schaltwerk), Linux-/Dev-Variante.
# Windows: START-ALLES.bat nehmen.
set -euo pipefail
cd "$(dirname "$0")"

echo "=========================================================="
echo "  Bad Wolf — Gesamtstart"
echo "  1. OmniRoute  (Node.js)   -> http://127.0.0.1:20128"
echo "  2. Schaltwerk (Python)    -> http://127.0.0.1:8765"
echo "=========================================================="

command -v node >/dev/null || { echo "[!] Node.js fehlt (>=22.22.2): https://nodejs.org/"; exit 1; }

# ── OmniRoute ────────────────────────────────────────────────────────
if [ ! -d omniroute/node_modules ]; then
  echo "[1/2] OmniRoute: node_modules fehlt — npm ci (einmalig, dauert Minuten) …"
  (cd omniroute && npm ci --no-audit --no-fund)
fi
echo "[1/2] OmniRoute: optionale Pakete prüfen/beheben …"
(cd omniroute && node scripts/setup/fix-optional-deps.mjs)
echo "[1/2] OmniRoute starten …"
(cd omniroute && npm run dev) &
OMNI_PID=$!

# ── Schaltwerk ───────────────────────────────────────────────────────
PY=""
for c in python3 python; do
  command -v "$c" >/dev/null && { PY="$c"; break; }
done
[ -n "$PY" ] || { echo "[!] Python 3.11+ fehlt."; kill $OMNI_PID 2>/dev/null || true; exit 1; }

SWENV="schaltwerk/.venv"
if [ ! -d "$SWENV" ]; then
  echo "[2/2] Schaltwerk: Virtualenv anlegen (einmalig) …"
  "$PY" -m venv "$SWENV"
  "$SWENV/bin/pip" install -q -r schaltwerk/requirements.txt
fi
echo "[2/2] Schaltwerk starten …"
(cd schaltwerk && HOST=127.0.0.1 PORT=8765 "../$SWENV/bin/python" server.py) &
SW_PID=$!

trap 'kill $OMNI_PID $SW_PID 2>/dev/null || true' EXIT INT TERM
echo
echo "  Beide laufen. OmniRoute-Dashboard: http://127.0.0.1:20128"
echo "  Schaltwerk:                http://127.0.0.1:8765"
echo "  Beenden: Strg+C"
wait
