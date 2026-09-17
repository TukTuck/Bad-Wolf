# Bad Wolf

Konsolidiertes Arbeitsrepo für **OmniRoute** und **Schaltwerk** — beide bisher an
getrennten Orten und in unterschiedlichen Versionsständen.

## Inhalt

| Pfad | Was | Technik |
| --- | --- | --- |
| `omniroute/` | OmniRoute Gateway (Provider-Routing, Proxy-Verwaltung, Dashboard) | Next.js / TypeScript / Bun, Version **3.8.51** |
| `schaltwerk/` | Schaltwerk — Proxy-Austausch für OmniRoute | FastAPI / Python 3.11+ |

## Herkunft dieses Stands

Importiert am **12.09.2026**. Die Quellorte wurden **nicht verändert** — dieser
Stand ist eine Kopie, jederzeit rückholbar.

| Komponente | Quelle | Git-Referenz |
| --- | --- | --- |
| `omniroute/` | `BWO/OmniRoute` | Branch `release/v3.8.51`, Commit `b345c7f6cd4e1590d1177540813302375a75e332` |
| `schaltwerk/` | `BWO/Arena-Wrap/schaltwerk/omni-proxy-exchange` | Commit `0b32e348795d24cd4f231c6089bf8db3a926286a` |

`schaltwerk/server.py` hat in diesem Stand **sha256 `23067de939682a58…`**
(Präfix, 1507 Zeilen).

### Historie

Dieses Repo startet mit **frischer Historie**. Die Upstream-Historie von
OmniRoute (`diegosouzapw/OmniRoute`) sowie deren Remotes wurden bewusst **nicht**
übernommen: kein `.git`, keine Remote-Konfiguration. Ein versehentlicher Push in
den Upstream ist damit ausgeschlossen.

### Warum genau *dieser* Schaltwerk-Stand

Von Schaltwerk existierten drei verschiedene Code-Stände, die **alle** im
CHANGELOG dieselbe Version `1.1.0` meldeten — die Versionsnummer unterschied sie
also nicht, nur der Dateihash:

| Stand | `server.py` | Zeilen | Übernommen? |
| --- | --- | --- | --- |
| 1.0.0 (Worktree `tuktuck-reimagined-memory`) | `c0692de592` | 1057 | nein — zu alt, ohne Scheduler-Feature |
| 1.1.0 alt (`Desktop/Omniwerke/Schaltwerk`, `schaltwerk-main-b6e2c72`, Backup-Zip) | `5ac42af0c7` | 1505 | nein — **ohne 403-Fix** |
| 1.1.0 neu (`BWO/Arena-Wrap`) | `23067de939` | **1507** | **ja** |

Der Unterschied zwischen den beiden 1.1.0-Ständen sind zwei Zeilen in
`server.py`, und sie sind verhaltensrelevant:

```python
-        auth_ok = resp.status_code != 401
+        auth_ok = resp.status_code < 400
```

OmniRoute antwortet auf ein ungültiges Management-Token mit **403**, nicht mit
401. Die alte Variante hat „Invalid management token" deshalb fälschlich als
erfolgreiche Verbindung gemeldet. Dieses Repo enthält den korrigierten Stand
inklusive Regressionstest `test_connect_erkenn_403_als_auth_fehler`.

## Starten

### Schaltwerk

```bat
cd schaltwerk
STARTEN.bat
```

`STARTEN.bat` prüft Python, installiert `requirements.txt` und startet den Server
auf **http://127.0.0.1:8765** (`HOST=127.0.0.1`, `PORT=8765`).

Tests:

```bat
python -m pip install -r schaltwerk\requirements-dev.txt
python -m pytest schaltwerk\tests
```

### OmniRoute

Node-Anforderung laut `package.json`: `>=22.22.2 <23 || >=24.0.0 <27`.

```bat
cd omniroute
npm install
npm run dev
```

Weitere Skripte in `omniroute/package.json` (u. a. `build`,
`build:backend`, `build:secure`). Docker-Betrieb über `omniroute/docker-compose.yml`.

## Verbindung der beiden Teile

Schaltwerk schreibt geprüfte Proxies über die Management-API nach OmniRoute.
Der Endpunkt wird zur Laufzeit in der Oberfläche gesetzt
(`http://127.0.0.1:20128`). URL und API-Key werden **im Benutzerverzeichnis
gespeichert** (Windows: `%APPDATA%\Schaltwerk\config.json`, Linux:
`~/.config/schaltwerk/config.json`) — nach dem Start verbindet Schaltwerk
automatisch; ein fehlgeschlagener Connect überschreibt den gespeicherten Key
nicht. Zum Zurücksetzen die Datei löschen.

**3-Provider-Regel:** Jeder Provider-Key wird (vom Nutzer) mehrfach — üblich:
3× — als Connection angelegt. „Proxies zuordnen" gibt jeder aktiven Connection
ihren eigenen Proxy (Connection-Ebene, `scope=account`), Connections desselben
Providers bekommen round-robin die besten Proxies → jeder Key-Instanz eine
eigene Exit-IP. Die Zuordnung läuft nach jedem Austausch automatisch.
