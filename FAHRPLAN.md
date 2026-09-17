# Bad Wolf - unser Fahrplan

Stand: **17.09.2026, nach Zielkorrektur durch Tudor**. Für Tudor und die weitere Projektbegleitung. Diese Datei ist die zentrale Arbeitsgrundlage; das PDF ist nur die daraus erzeugte Kurzfassung. Sie fasst Entscheidungen und belegte Ergebnisse dieses Gesprächs zusammen, nicht jede Gesprächsformulierung. Das Ziel einer Multi-Agent-Produktionsplattform ersetzt ausdrücklich die vorherige Einordnung als zuerst zu bauender persönlicher Sprachassistent.

<!-- ONEPAGE_START -->
## Bad Wolf auf einem Blatt

**Ziel:** Bad Wolf wird eine **Multi-Agent-Produktionsplattform**, mit der Tudor Inhalte und digitale Produkte herstellen und Geld verdienen kann. YouTube, TikTok und 3D-Generierung sind ausdrücklich gewünschte Einsatzfelder. Eigene Stimme, Modellanbieter und Rechenleistung unterstützen dieses Produktionsziel.

**Drei Betriebsarten:** ein bis zwei persönlich geführte eigene Kanäle, zusätzliche vollautomatische eigene Kanäle und Kundenaufträge. Sie sollen dieselben Produktionsfähigkeiten nutzen. Eigene Produktion und Kundenarbeit dürfen gleichzeitig möglich sein.

**Research-Team:** Ein kleines Team aus Agenten soll regelmäßig Trends untersuchen und neue Themen, Formate und Kanalideen vorschlagen. Google-Daten sind dafür vorgesehen; das konkret gemeinte Werkzeug, der Rhythmus und Datenzugriff sind noch offen.

**Automatik je Kanal:** Jeder Kanal erhält eigene Regeln für Selbstständigkeit. Bestätigtes Beispiel: Ein AI-News-Kanal greift Trends auf und produziert selbstständig Videos dazu. Vorgeschlagene vollständige Kette: Themenpool -> Recherche -> Konzept -> Medienproduktion -> automatische Qualitätsprüfung -> Veröffentlichung -> Auswertung. Veröffentlichung und Ausnahmen sind noch zu klären.

### Was bereits steht

- **Technische Basis:** OmniRoute 3.8.51 und Schaltwerk im Hauptrepo; Qwen3.5 Heretic 9B mit Vision auf der VM. Die Multi-Agent-Produktion ist noch nicht integriert.
- **Audio:** Qwen3-TTS und Chatterbox auf Windows technisch geprüft. Zielstimme offen; VoiceStudio/OmniVoice als dritter Vergleichskandidat vereinbart. Kein laufender Testserver.
- **Produktionsrezepte:** OpenMontage und MoneyPrinterTurbo recherchiert. Sie sind Kandidaten für den ersten Medienablauf; noch nicht installiert oder im eigenen Pilot geprüft.

### Der neue Hauptfahrplan

| Schritt | Ergebnis | Voraussetzung |
| --- | --- | --- |
| 1. Grill-me / Zielbild (Q0/P1) | Kanalprofile und erster exemplarischer Produktionsauftrag | Drei Betriebsarten stehen fest |
| 2. Produktion erproben (P2) | Ein tatsächlich nutzbares Ergebnis mit vorhandenem Rezept | Auftrag und Qualitätsmaßstab geklärt |
| 3. Agenten koordinieren (P3) | Wiederholbarer Ablauf mit Zuständigkeiten, Übergaben und Prüfung | Funktionierender Pilot |
| 4. Automatik betreiben (P4) | Wiederkehrende Produktion, Verwertung und Auswertung; weitere Formate | Wiederholbare Produktion |

### Wo die bisherigen Themen hingehören

**Stimme/Cloning:** gewünschte Identität und Audio-Produktion. **LiveKit:** möglicher Sprachzugang zur Plattform. **OmniRoute/Schaltwerk:** Modell- und Verbindungsinfrastruktur. **3D:** gewünschter Produktionsbereich; Werkzeuge und erstes Produkt noch offen. Der erste Pilot begrenzt den Einstieg, nicht das spätere Plattformziel. Große Colibri-Modelle bleiben wegen der 12-GB-Modellgrenze zurückgestellt.

### Eigener Arbeitsstrang: Mail-Auswertung

**Konto B:** Letzter geprüfter Stand vom 17.09., 11:29 MESZ: Lauf beendet, 4.194/4.201 klassifiziert, sieben Fehlerfälle, 520 unbestätigte Prüfkandidaten. Bild-/Anhangsinhalte ungeprüft. Fehlerdiagnose und Kandidatenprüfung bleiben ein eigener Auftrag.

### Feste Leitplanken

Erst gemeinsam den Fahrplan fassen, dann implementieren. Bestehende Community-Rezepte bevorzugen. Eigene VM und lokale Verarbeitung als Standard, externe Anbieter bewusst wählbar. Kontext je Modell. Qualität, Produktionskosten und verwertbare Ergebnisse beurteilen. Dieses Gespräch klärt das Konzept; es startet keine neue Produktion.
<!-- ONEPAGE_END -->

## So verwenden wir diesen Plan

Die Zerlegung wurde in diesem Dokument mit **Fable Plan (`fable-plan`)** vorgenommen: kleine Arbeitspakete mit Abhängigkeiten, Zuständigkeit, Abnahme und Rückweg. **Fable Discover** diente dem Abgleich mit den vorhandenen Dateien; **Fable Artifact** der Dokumentstruktur. Dies ist ein dokumentierter Arbeitsplan, keine automatisch laufende Aufgabenwarteschlange und keine Überwachungsautomation.

**Ergänzung auf Nutzerwunsch: `grill-me`.** Der originale Skill von Matt Pocock und seine notwendige Anleitung `grilling` sind unter `C:/Users/Tudor/.codex/skills/` installiert. Gepinnte Quellrevision: `959a8e9f1edc3adbe2f7e3054bb6fbefa6696260` aus [mattpocock/skills](https://github.com/mattpocock/skills/tree/959a8e9f1edc3adbe2f7e3054bb6fbefa6696260/skills/productivity/grill-me). Die automatische Skill-Erkennung ist ab dem nächsten Gesprächsbeitrag verfügbar; die gelesene Interviewmethode wird bereits in diesem Gespräch angewandt. Frühere Entscheidungen werden nicht erneut grundlos abgefragt.

**Q0 - Grundgedanke geklärt; erster Beispielablauf in Klärung:** Bestätigt sind Multi-Agent-Produktion für Einnahmen, eigene und Kundenproduktion nebeneinander, persönlich geführte und vollautomatische Kanäle, regelmäßige Trendforschung durch ein Research-Team sowie Vorschläge für neue Kanäle. Tudor legt fest: Selbstständigkeit hängt vom jeweiligen Kanal ab. Ein AI-News-Kanal soll beispielsweise selbst Trends aufgreifen und Videos dazu produzieren. Der allgemeine Ansatz, größere Neuausrichtungen zunächst vorzuschlagen, passt grundsätzlich, wird aber nicht als starre Regel für jeden Kanal festgeschrieben. Aktuelle Frage: Soll AI-News der erste vollständige Beispielablauf für den Fahrplan werden? Empfehlung ja; noch nicht entschieden. Danach folgen Format, Themen-/Datenquellen, Rhythmus, Kostenrahmen, Qualitäts-/Fehlerregeln, Veröffentlichung und Extras. Das Ziel dieses Gesprächs bleibt ein verständlicher Grundgedanke und Fahrplan; neue Produktumsetzung oder Veröffentlichung ist in diesem Schritt nicht beauftragt.

### Das gemeinsame Produktionsbild

**Bestätigt:** Eine Plattform soll sowohl eigene Inhalte als auch Kundenaufträge ermöglichen. Persönlich betreute und automatische Kanäle sind unterschiedliche Betriebsarten, keine getrennten Produkte. Vollautomatische, vollständig KI-generierte Produktion ist ein Kernziel und wird nicht pauschal auf einen Ablauf mit manueller Prüfung jedes Clips reduziert.

**Vorgeschlagener gemeinsamer Unterbau:** Projekte beziehungsweise Kanalprofile beschreiben Zweck und gewünschten Stil. Ein Themenbestand hält Ideen und Recherchebezüge. Eine Koordination verteilt Arbeit auf passende Agenten und Werkzeuge; die Ergebnisse und Zwischenstände bleiben einem Auftrag zugeordnet. Dieselben Audio-, Video- und später 3D-Fähigkeiten sind für eigene Kanäle und Kundenarbeit nutzbar. Diese Bauteile beschreiben das Konzept, noch keine implementierte Architektur.

**Automatik-Ablauf:** Thema auswählen -> Quellen recherchieren -> Konzept/Skript -> Bild/Video/Audio/gegebenenfalls 3D erzeugen -> zusammenstellen -> automatisch prüfen -> nach den festgelegten Kanalregeln veröffentlichen -> Aufwand und Wirkung auswerten. Themenauswahl, Recherche und KI-Generierung sind ausdrücklich bestätigt; Veröffentlichung, Auswertung und die genaue Ausnahmesteuerung sind zur Klärung vorgeschlagene Folgeschritte. Ein einmal festgelegtes Profil soll wiederkehrende Nachfragen vermeiden. Ob fehlerhafte Inhalte neu generiert, verworfen oder Tudor vorgelegt werden, ist noch offen.

**Faktenlücke:** „Unsere Datenbank“ ist als gemeinsamer Themenbestand gemeint. Eine tatsächlich vorhandene thematische Datenbank samt Schema, Inhalt und Zugriff wurde noch nicht verifiziert. Der Obsidian-Brain und OmniRoutes Betriebsdatenbank werden nicht ohne Prüfung damit gleichgesetzt. Die technische Bestandsaufnahme ist Aufgabe von Codex. Die „Extras“ sind ein geäußerter Wunsch, aber noch keine spezifizierte Funktion.

**Selbstständigkeit pro Kanal - bestätigt:** Keine einheitliche Freigabeschleife für alle Produktionen festlegen. Das Kanalprofil bestimmt, welche Entscheidungen automatisch getroffen werden. Für das genannte AI-News-Beispiel sind Trendaufnahme, Themenwahl und Videoerstellung ohne einzelne Themenfreigabe gewünscht. Für persönlich geführte Kanäle und Kundenprojekte können andere Regeln gelten. Die genaue Veröffentlichungs- und Fehlerbehandlung ist noch offen. AI-News ist bisher ein Beispiel; die nächste Frage klärt, ob wir damit den ersten vollständigen Ablauf durchplanen.

### Research-Team und Rückkopplung

**Bestätigter Auftrag an die künftige Plattform:** Ein kleines Research-Team untersucht in regelmäßigen Abständen Trends. Es darf neue Ideen für Kanäle entwickeln und vorschlagen. Das Team speist damit die Produktionsplanung; es ist keine einmalige Vorrecherche vor der Installation.

**Datenquellen unterscheiden:** Tudor nannte das „Google-Analytics-Tool“. [Google Trends](https://trends.google.com/trends/) liefert Suchinteresse; [YouTube Analytics](https://developers.google.com/youtube/analytics) liefert Daten zu eigenen YouTube-Kanälen; [Google Analytics](https://developers.google.com/analytics) misst vor allem eigene Websites und Apps. Welches Werkzeug ursprünglich gemeint war und welche Zugänge vorhanden sind, ist nicht bestätigt. Vorgeschlagen ist eine spätere Kombination aus Marktsignalen und eigener Kanalperformance; nicht behaupten, dass diese Anbindung schon existiert oder alle Daten ohne Zugang verfügbar seien.

**Vorgeschlagene Ergebnisse eines Research-Laufs:** Quellen mit Datum, Themen-/Formatvorschläge, Begründung der Nachfrage, Konkurrenz, voraussichtlicher Produktionsaufwand und mögliche Verwertung. Von Views oder Suchvolumen allein lässt sich kein Gewinn ableiten. Die Bewertungskriterien und Gewichte werden noch vereinbart. Einen Quellenbefund von der Interpretation der Agenten unterscheiden.

**Geplanter Kreislauf:** Trends -> Vorschläge im Themenbestand -> passende Produktion -> tatsächliche Ergebnisse -> nächster Research-Lauf. Eigene Ergebnisse zurückzuführen ist eine Empfehlung, noch keine implementierte oder abschließend beschlossene Datenverarbeitung. Die Aufgaben für P1 umfassen damit auch die konkreten Datenquellen; P3 umfasst den belegbaren Themenbestand; P4 umfasst wiederkehrende Research-Läufe. Teamgröße, Rollen, Zeitplan und Budget sind offen. „Regelmäßig“ ist hier eine Produktanforderung an Bad Wolf; dafür wurde keine Codex-Automation und kein laufender Research-Dienst eingerichtet.

**Statusbegriffe:** `erledigt/geprüft` bezeichnet belegte Arbeit; `bereit` heißt, dass die Voraussetzungen für den nächsten Schritt bestehen; `wartet` nennt eine fehlende Voraussetzung; `Entwurf` wird erst nach dem vorangehenden Meilenstein konkretisiert. Ein akzeptierter Plan bedeutet nicht, dass seine Aufgaben schon ausgeführt wurden.

**Verantwortung:** Tudor bestimmt Produktionsziele, Zielgruppe, Verwertung und die Qualitätsabnahme. Codex klärt technische Fakten, dokumentiert Entscheidungen und setzt anschließend das jeweils beauftragte Paket um. Die künftigen Agentenrollen innerhalb Bad Wolfs werden aus dem Produktionsablauf abgeleitet; eine feststehende Agentenzahl gibt es noch nicht. Die Erwähnung von Multi-Agenten ist keine Anweisung, für dieses Gespräch ungefragt Subagenten zu starten. Codex prüft auch das Zusammenspiel der Komponenten; einzelne erfolgreiche Modelltests genügen nicht für eine fertige Produktionsplattform.

**Pflege:** Nach jedem Paket Status, Ergebnisdatei und nächsten Schritt hier aktualisieren. Das Übersichtsblatt mit `tools/render_fahrplan.py` neu erzeugen. Keine zweite, unabhängig gepflegte Roadmap anlegen. Die Upstream-Roadmap in OmniRoute bleibt die Roadmap dieses Teilprojekts.

## Entscheidungen, die bereits getroffen sind

| Thema | Vereinbarung |
| --- | --- |
| Zweck | Multi-Agent-Produktionsplattform zur Herstellung und Verwertung von Inhalten und digitalen Produkten. Diese ausdrückliche Zielkorrektur ersetzt die alte Reihenfolge „persönlicher Assistent zuerst“. |
| Produktionsfelder | YouTube, TikTok und 3D-Generierung wurden ausdrücklich genannt. Das Ziel bleibt breit; ein erster Pilot und dessen Einnahmeweg sind noch festzulegen. |
| Betriebsarten | Eigene Produktion und Kundenaufträge gleichzeitig ermöglichen. Ein bis zwei persönlich geführte eigene Kanäle plus zusätzliche vollautomatische Kanäle sind gewünscht. |
| Automatikkanäle | Selbstständige Themenauswahl aus dem gemeinsamen Themenbestand, Recherche und vollständig KI-generierte Produktion. Automatik gehört zum Kernziel; Kanalprofile, Veröffentlichung und konkrete Extras sind noch zu klären. |
| Research-Team | Kleines Team aus Agenten für regelmäßige Trendforschung mit Google-Daten. Es darf neue Themen/Formate/Kanalideen vorschlagen. Datenquelle, Rhythmus und Entscheidungsbefugnisse bleiben zu konkretisieren. |
| Selbstständigkeit | Kanalabhängig festlegen. AI-News als genanntes Beispiel darf Trends selbst aufgreifen und daraus Videos produzieren. Keine pauschale manuelle Themenfreigabe für alle Kanäle einbauen. |
| Ergebnis dieses Gesprächs | Einen verständlichen Grundgedanken und Fahrplan zurückgewinnen. Weitere Installation oder Produktion ist dafür nicht nötig. |
| Arbeitsweise | Schrittweise; vorhandene Community-Projekte und Rezepte prüfen, bevor wir Infrastruktur selbst bauen. |
| Stimme | Voice Cloning ist ein Kernbestandteil. Inspiration: Rose Tyler als Bad Wolf in bestimmten Doctor-Who-Szenen, mit ihrer besonderen Sprechweise. |
| Noch zu klären | Konkrete Szene, englisches Original oder deutsche Synchronfassung. Das wurde noch nicht entschieden. |
| Betriebsort | Eigene VM als bevorzugtes Ziel; lokale Verarbeitung als Standard. Die bestehende Stimmvorbereitung liegt tatsächlich auf Windows. |
| Cloud | Azure, Google Cloud, Alibaba Cloud, Colab und Kaggle stehen nach Nutzerangabe zur Verfügung. Konkrete GPU-Verfügbarkeit, Guthaben und Limits sind nicht geprüft. Optionale API-Anbieter sollen später wählbar sein. |
| Kontext | Jede Modellvariante erhält ihre passende Konfiguration. Kein global erzwungener Kontextwert. 40k allein genügte dem gewünschten Einsatz nicht. |
| Downloadgröße | Für die besprochene LLM-Auswahl gilt maximal **12 GB inklusive Bildmodul**. Die vorherigen 2 GB waren ein Diktatfehler. Dies ist kein belegtes Gesamtbudget für sämtliche Software und Audiomodelle. |
| Modell-Merges | Gemeint war ein Merge mehrerer Sprachmodelle. Kein bestimmter Merge wurde zum Einsatz beschlossen; Vision, Werkzeuge und Kontext müssten erneut geprüft werden. |
| Vergleich | Qwen, Chatterbox und VoiceStudio/OmniVoice mit derselben Referenz und vergleichbaren Testsätzen. Dieser Vorschlag wurde akzeptiert. |
| Plan schärfen | `grill-me` auf Nutzerwunsch ergänzt; Geschäfts-/Produktionsausrichtung und erster Produktionsauftrag werden vor der davon abhängigen Umsetzung gemeinsam geklärt. |
| Projektsammlung | Chrome-Lesezeichen ausgewertet; Firefox entfällt auf dem frisch eingerichteten Windows. Neue Videolinks wurden separat recherchiert. |

## Tatsächlicher technischer Stand

### Hauptrepo: die vorhandene Grundlage

Das Arbeitsrepo liegt unter [Bad-Wolf](<C:/Users/Tudor/Documents/Bad Wolf/Bad-Wolf>). Es bündelt zwei Teile:

- **OmniRoute 3.8.51:** Gateway, das Modellanbieter, Weiterleitung, Fallbacks und Verwaltung bündelt; Next.js/TypeScript. Vorhandene Audio-/API-Funktionen allein belegen noch keinen vollständigen Bad-Wolf-Gesprächsablauf.
- **Schaltwerk:** FastAPI/Python-Anwendung, die Proxy-Kandidaten holt, prüft und über die Management-API als manuelle Proxies nach OmniRoute schreibt. Der importierte Stand enthält laut Repo den 403-Authentifizierungsfix und zugehörigen Regressionstest. Die Tests wurden bei dieser Dokumentation nicht neu ausgeführt.

Die Verbindung wird zur Laufzeit gesetzt. **Dokumentationswiderspruch:** Das Haupt-README nennt für OmniRoute `24615`, das Schaltwerk-README `20128`. Der tatsächliche Endpunkt muss bei der Integrationsaufnahme festgestellt werden; keinen der Werte ungeprüft zum Soll erklären. Der Schaltwerk-Management-Key wird laut Haupt-README nicht dauerhaft gespeichert.

**Vorgemerkt am 17.09.2026: [MCP Client for Ollama / ollmcp](https://github.com/jonigl/mcp-client-for-ollama) als Ergänzung zu OmniRoute.** Auf ausdrücklichen Nutzerwunsch in die Planung aufgenommen. Anschließend hat Tudor die unmittelbare Verwendung freigegeben, wenn sie bei der Arbeit konkret nützt; die allgemeine Pause ist dadurch nicht pauschal aufgehoben. Das Python-Terminalprogramm verbindet ein Modell mit MCP-Werkzeugen, Prompts und Ressourcen. Es unterstützt mehrere MCP-Server, wiederholte Werkzeugaufrufe, Modellwechsel, Streaming, Bild-Ressourcen und einstellbare Ausführungsfreigaben. MIT-Lizenz; geprüfter Upstream-Stand `7322a9e425cb45cc6563ea108d07b345cac2b69e` vom 11.09.2026.

Zwei mögliche Anbindungen passen zur vorhandenen Infrastruktur: (1) Modellanfragen aus ollmcp über OmniRoutes OpenAI-kompatible `/v1`-API weiterleiten; der geprüfte ollmcp-Code verwendet eine konfigurierbare Provider-, Basis-URL- und API-Key-Anbindung über AnyLLM. (2) OmniRoute selbst als MCP-Werkzeugserver in ollmcp einbinden; OmniRoutes README dokumentiert unter anderem `/api/mcp/stream` für Streamable HTTP und `omniroute --mcp` für stdio. Die erste Verbindung betrifft Modellantworten, die zweite Gateway-Werkzeuge. Zusammenführen ist ein Integrationskandidat, noch kein bestandener gemeinsamer Laufzeittest und keine fertige Multi-Agent-Produktionskoordination.

Für einen begrenzten Test bei Wiederaufnahme der passenden Integrationsarbeit: tatsächliche OmniRoute-Adresse und passende Schlüssel feststellen, ein Modell auflisten und aufrufen, ein lesendes MCP-Werkzeug ausführen, Streaming und gegebenenfalls ein Bild prüfen. Modellkontext beibehalten: ollmcp setzt `num_ctx` in seiner Standardkonfiguration auf `None`; gespeicherte Profile und die Weiterleitung über OmniRoute müssen trotzdem auf Anfrage-Overrides geprüft werden. Modell-API-Key und MCP-Server-Header getrennt betrachten. Der native Ollama-Remotezugang und sein aktueller HTTP-400-Fehler werden durch diesen zusätzlichen Client allein nicht behoben. Daher aktuell kein unmittelbarer Nutzen für diese Verbindungsdiagnose und noch keine Installation. Die bedingte Freigabe zur Verwendung ist vorhanden; für den ersten passenden MCP-Werkzeugtest nicht erneut allein wegen der Toolwahl nachfragen.

Der gemeinsame Start, ein durchgängiger Sprachablauf und die spätere Mobilintegration sind **nicht abgenommen**. Während dieser Gesprächsarbeit wurde keine solche Produktintegration implementiert. Für spätere Änderungen innerhalb OmniRoute gelten dessen lokale Entwicklungsregeln einschließlich der dort geforderten Arbeitsisolation.

### VM und Sprachmodell

| Merkmal | Belegter Stand |
| --- | --- |
| Maschine | `nucc`, NVIDIA L4, 23.034 MiB VRAM, ungefähr 50,5 GB RAM dezimal; die anfängliche RAM-Schätzung wurde damit präzisiert. |
| Ollama | Version 0.34.0 beim Setup. |
| Modell | `qwen35-heretic:9b-q8-256k`, Qwen3.5-9B-Heretic, Q8, mit Bildmodul. |
| Download | 10.449.206.240 Bytes insgesamt, ungefähr 10,45 GB; Dateien und Hashes im Installationsbeleg. |
| Kontext | `num_ctx=262144` in der Modellkonfiguration; keine globale Kontextüberschreibung. Clients können Werte je Anfrage überschreiben. |
| Funktionstests | Text, Bildverständnis, Werkzeugaufruf und gezielter Informationsabruf bei 91.043 Eingabetoken bestanden. |
| Grenzen der Prüfung | Kein vollständiger 262k-Qualitätstest, keine kontrollierte deutsche Gesamtevaluation und keine eigene belastbare Ablehnungsquote. |
| Speicher | Beim großen Kontext ungefähr 17,7 GB VRAM für den Modellprozess beobachtet. Das ist ein einzelner Messzustand, kein garantiertes Maximum für alle Anfragen. |

**Ressourcenfolge:** Mailmodell, großer LLM-Kontext, Spracherkennung und TTS müssen gemeinsam geplant werden. Große Modelle passen nicht automatisch gleichzeitig in 24 GB VRAM. Je Modell sinnvollen Kontext, Laden/Entladen und gegebenenfalls sequentielle Ausführung messen; keinen globalen Kontext reduzieren, um einen Engpass zu verstecken.

**Remote-Zugang, 17.09.2026, 12:16 MESZ:** Zielgeräte sind Windows und Handy. Ollama 0.34.0 ist auf Windows installiert. Ein nativer Remote-Alias `bad-wolf-vm:9b` wurde über einen befristeten, authentifizierten SSH-Tunnel erfolgreich getestet: Streaming und OpenAI-kompatible API, tatsächlicher VM-Kontext 262.144 Tokens, keine Modellgewichte auf Windows. Der normale Chat der offiziellen App sendet laut geprüftem Quellcode keinen eigenen `num_ctx`; andere Clients können Modellparameter je Anfrage überschreiben. Handy-App/Betriebssystem noch offen. Die automatische Entdeckung aller VM-Modelle allein über denselben Ollama-Account ist nicht nachgewiesen. Die dauerhafte Tailscale-Freigabe wurde vor Ausführung durch die automatische Sicherheitsprüfung abgelehnt, weil der angefragte API-Key-Schutz beziehungsweise passende Zugriffsbeschränkungen nicht belegt waren. Dauerzugang bleibt offen. [Einrichtung und Quellen](<C:/Users/Tudor/Documents/Bad Wolf/vm-model-setup-20260917/REMOTE-ZUGRIFF.md>) · [Laufzeitnachweis](<C:/Users/Tudor/Documents/Bad Wolf/vm-model-setup-20260917/native-remote-test.json>).

Quantisierung, Modell-Merge und Auslagerung sind verschiedene Verfahren. Quantisierung kann Qualität kosten; ein Merge ist nicht automatisch besser. Colibris Verschieben vorhandener Gewichte zwischen SSD/RAM/VRAM reduziert die nötige schnelle Speicherkapazität, nicht automatisch die Dateigröße. Benchmarks aus verschiedenen Projekten oder unterschiedlichen Aufgaben sind kein direkter Leistungsvergleich.

### Stimmvorbereitung auf Windows

Die getrennte Installation liegt unter [voice-vorbereitung](<C:/Users/Tudor/Documents/Bad Wolf/voice-vorbereitung>). Sie nutzt ComfyUI 0.36.0 und TTS Audio Suite in einer eigenen Python-Umgebung. Hardware: **RTX 2070 SUPER mit 8 GB VRAM**, ungefähr 16 GB RAM. Torch 2.8.0 mit CUDA 12.8 ist installiert. Modellrevisionen, Quellen und Prüfsummen sind gespeichert.

| Kandidat | Zustand und Ergebnis |
| --- | --- |
| Qwen3-TTS-12Hz-0.6B-Base | Ungefähr 2,52 GB ausgewählte Modelldateien inklusive Codec. Technischer Test: 3,83 s Audio; erster Aufruf inklusive Laden 20,28 s. Referenz war synthetisch. |
| Chatterbox Multilingual V3 | Ungefähr 3,21 GB ausgewählte Komponenten. Technischer Test: 3,64 s Audio; erster Aufruf inklusive Laden 30,19 s. |
| VoiceStudio mit OmniVoice | Recherchiert und als dritter Vergleichskandidat vereinbart; **nicht installiert und nicht gemessen**. |
| Qwen 1.7B / andere Suite-Engines | Optionale spätere Vergleiche; nicht Teil der geprüften Installation. Sichtbarkeit im Menü bedeutet keine Einsatzbereitschaft. |

Beide erzeugten Testdateien waren endlich und nicht stumm. **Hörverständlichkeit und Ähnlichkeit zur Zielstimme wurden noch nicht bewertet.** Die gemessenen Zeiten sind keine Streaming-Latenzen. `pip check` war erfolgreich. Qwen scheiterte auf dieser GPU mit `float16`; der vorbereitete Ablauf verwendet deshalb **float32**. Das ist eine lokale Einstellung, keine Aussage über andere GPUs.

Die GPU wurde tatsächlich verwendet. Geringe sichtbare Auslastung und stille Lüfter widersprechen kurzen Inferenzphasen nicht; Downloads und Installation machten viel Wartezeit aus. Der Testserver wurde beendet und seitdem in dieser Arbeit nicht erneut gestartet. Launcher: [Start-Stimmvergleich.ps1](<C:/Users/Tudor/Documents/Bad Wolf/voice-vorbereitung/Start-Stimmvergleich.ps1>), lokale Oberfläche `127.0.0.1:8189`.

### Referenz und Qualitätsvergleich

Tudor sucht einen **30-60 Sekunden langen Szenenausschnitt**. Daraus wählen wir passend zur Engine eine klare Passage mit genau einer Stimme, möglichst wenig Musik und Hall. Etwa **10-20 Sekunden** sind für den Vergleich praktisch; für OmniVoice kann eine kürzere Teilpassage sinnvoll sein. Kein ganzes Serienkapitel nötig. Original unverändert aufbewahren; Zuschnitt, Transkript und etwaige Reinigung als Ableitungen dokumentieren.

Entscheidend sind zwei getrennte Dinge: die **Stimmidentität** und die **besondere Darbietung** in der Szene. Hall, Doppelung oder andere hörbare Effekte erst nach dem trockenen Vergleich separat untersuchen; noch ist nicht belegt, welche Effekte die ausgewählte Szene enthält.

Vergleichsvorschlag: dieselben kurzen Sätze, eine längere Passage, Namen/Zahlen sowie ruhige, bestimmte und geflüsterte Darbietung, soweit die jeweilige Engine sie unterstützt. Verfügbare Stilsteuerung dokumentieren, keine gemeinsamen Fähigkeiten voraussetzen. Seed/Parameter innerhalb einer Engine festhalten; gleiche Seed-Zahlen machen verschiedene Modelle nicht identisch reproduzierbar.

Für jeden Kandidaten festhalten: verständliche Aussprache, Wiedererkennbarkeit, Ausdruck, Aussetzer, Referenztreue, erster Aufruf mit Laden, weitere Aufrufe ohne Laden, Zeit bis zum ersten Audio nur bei echtem Streaming, Audiodauer und maximal beobachteter VRAM/RAM. **Keine erfundene Prozentnote.** Tudor hört möglichst ohne Modellnamen mit; falls kein Kandidat überzeugt, erst Referenz verbessern und dann gezielt einen weiteren Kandidaten prüfen.

## Kleine Arbeitspakete mit Abnahme

**Der Hauptweg ist jetzt P1 -> P2 -> P3 -> P4.** Er beschreibt die Produktionsplattform. Die bisher ausgearbeiteten V-/G-Pakete bleiben als vorbereitete Audio- und Bedienmodule erhalten; sie sind keine Voraussetzung für jede Produktion und legen die Produktreihenfolge nicht mehr fest. S bleibt ein unabhängiger Mail-Arbeitsstrang. Die folgenden Zukunftspakete sind Entwürfe: konkrete Werkzeuge, Schnittstellen und Abnahmeschwellen werden erst nach der Zielklärung festgelegt. Daraus entsteht keine Freigabe für beliebige Deployments oder Provideränderungen.

### Hauptweg P: Von der Grundidee zur wiederholbaren Produktion

| ID / Status | Ergebnis und Umfang | Abhängigkeit / Zuständigkeit | Fertig, wenn ... | Rückweg / Übergabe |
| --- | --- | --- | --- | --- |
| **P1 - in Klärung** | Die drei bestätigten Betriebsarten konkretisieren und einen exemplarischen Produktionsauftrag wählen: Kanalprofil, Zielgruppe, Ergebnis, gewünschte Verwertung und Qualitätsmaßstab. Themenbestand technisch verifizieren. | Q0; Tudor entscheidet, Codex klärt Fakten und fasst zusammen. | Tudor das Zielbild wiedererkennt und ein Ablauf konkret genug für einen Pilot ist; parallele eigene/Kundenproduktion bleibt im Konzept erhalten. | Unpassende Empfehlungen verwerfen; Plattformziel breit halten. Klarer Auftrag an P2. |
| **P2 - Entwurf nach P1** | Einen vorhandenen Community-Ablauf für den gewählten Auftrag prüfen und damit ein fertiges Ergebnis erstellen. Bei Video OpenMontage/MoneyPrinterTurbo vergleichen; bei 3D zuerst geeignete Quellen und Werkzeuge recherchieren. | P1; Codex klärt Fakten vor Umsetzung, Tudor beurteilt das Ergebnis. | Ein verwendbares Artefakt samt dokumentiertem Ablauf, Aufwand, Kosten und verbleibenden manuellen Schritten vorliegt. | Rezept isoliert testen; vorhandene Umgebung erhalten. Ausgewerteter Pilot an P3. |
| **P3 - Entwurf nach P2** | Den bewährten Ablauf als wiederholbare Multi-Agent-Produktion organisieren: gemeinsame Projekt-/Kanalprofile, Themenbestand, Rollen, Status, Ergebnisse, Übergaben, Wiederaufnahme und automatische Qualitätsprüfung. Eigene/Kundenaufträge eindeutig zuordnen. | P2 + technische Bestandsaufnahme inklusive tatsächlicher Ports/API-Verträge. | Ein zweiter Auftrag denselben Ablauf durchläuft; fehlerhafte Schritte gezielt fortsetzbar sind; Tudor Fortschritt und Ergebnis erkennt. Automatik- und betreute Aufträge nutzen dieselbe Produktion mit passenden Regeln. | Einzelne Schritte austauschbar lassen; Artefakte und erfolgreichen Zustand bewahren. Ablauf an P4. |
| **P4 - Entwurf nach P3** | Automatikbetrieb vom Themenbestand bis zum freigegebenen Veröffentlichungsweg und dessen Auswertung konkretisieren; mehrere Kanäle und Kundenaufträge koordinieren. Weitere Formate wie 3D aus dem Bedarf ableiten. | P3 + konkrete Kanal-/Zeit-/Kosten-/Fehlerregeln und erlaubte Veröffentlichungsziele. | Wiederkehrende Aufträge innerhalb der vereinbarten Regeln ohne Eingriff produziert werden; Fehlerfälle nachvollziehbar behandelt und Aufwand sowie reale Nutzung/Verwertung ausgewertet werden. Umsatz bleibt Ziel, kein bereits nachgewiesenes Ergebnis. | Kanalspezifische Automatik pausierbar halten; vorhandene Inhalte/Jobs erhalten; unwirksame Erweiterungen zurückstellen. |

**Noch keine Architekturentscheidung:** Als Gesprächsbild sind Planung, Recherche, Erstellung und Qualitätsprüfung sinnvolle Verantwortlichkeiten. Ob dafür vier Agenten, weniger oder weitere nötig sind, muss der Pilot zeigen. Projektgedächtnis, gemeinsame Ablage, Freigabepunkte, Kostenkontrolle und Bedienung werden aus diesem Ablauf abgeleitet, nicht vorab als vollständiges Framework festgelegt.

### Unterstützendes Modul V: Eine passende Stimme auswählen

| ID / Status | Ergebnis und Umfang | Abhängigkeit / Zuständigkeit | Fertig, wenn ... | Rückweg / Übergabe |
| --- | --- | --- | --- | --- |
| **V1 - wartet auf Szene** | Referenzpaket: Quelle, Sprachfassung, Original, Zuschnitt, genaues Transkript. Nur Audioaufbereitung. | Tudor liefert Szene und Fassung; Codex bereitet vor. | Passage ist verständlich, enthält eine Stimme; Transkript stimmt mit dem Zuschnitt überein. | Original erhalten; Reinigung bei Artefakten verwerfen. Referenz an V3. |
| **V2 - bereit** | VoiceStudio/OmniVoice isoliert ergänzen; Versionen, Modellbedarf, Gerät und Modellbedingungen festhalten. Bestehende Qwen-/Chatterbox-Umgebung bleibt verfügbar. | Keine Szene nötig für synthetischen Funktionstest; Codex. | Eine lokale Testausgabe funktioniert; API und tatsächlich verwendetes Gerät sind dokumentiert; Server kann sauber beendet werden. | Neue Umgebung abschalten; vorhandene Tests bleiben nutzbar. Ergebnis an V3. |
| **V3 - wartet auf V1+V2** | Drei Kandidaten mit gemeinsamer Referenz und Testsätzen vergleichen. Die ersten zwei Kandidaten sind technisch vorbereitet. | V1 + V2; Codex erzeugt und misst, Tudor hört. | Zugeordnete Audiodateien, Einstellungen und Messblatt vorhanden; Qualität und Laufzeit getrennt bewertet. | Wiederholbare Parameter erhalten; misslungene Varianten nicht als Erfolg zählen. Ergebnis an V4. |
| **V4 - wartet auf V3** | Stimme und Darbietung wählen; eine bevorzugte Einstellung dokumentieren. Noch keine Produktintegration. | V3; Tudor entscheidet, Codex dokumentiert. | Tudor bestätigt eine Variante oder benennt konkret, was fehlt. Nur falls nötig V1/V3 gezielt wiederholen. | Vergleichsausgaben behalten; keine voreilige endgültige Modellbindung. Gewählte Variante an G1. |

### Unterstützendes Modul G: Sprachzugang auf der VM

| ID / Status | Ergebnis und Umfang | Abhängigkeit / Zuständigkeit | Fertig, wenn ... | Rückweg / Übergabe |
| --- | --- | --- | --- | --- |
| **G1 - Entwurf nach V4** | Betriebsaufnahme und Speicherplan für LLM, STT und gewählte TTS: aktiver VM-Zustand, freie Ressourcen, passende Modellkontexte, Transport und Start/Stop. | V4; Codex. Vor jedem Lasttest vorhandene Jobs prüfen. | Gerät, Speicherbudgets und ein konkreter API-Vertrag stehen fest; keine offene Architekturfrage wird in die Installation verschoben. | Bei Engpass sequentiellen Betrieb planen. Keine fremden Jobs stoppen. Vertrag an G2. |
| **G2 - Entwurf nach G1** | Gewählte TTS als getrennten Dienst mit wiederverwendbarem Stimmprofil auf der VM bereitstellen. | G1; Codex. | Derselbe Testtext über die API korrekt ausgegeben wird, Neustart das Profil erhält und Speicher/Laufzeit protokolliert sind. | Nur neuen Dienst stoppen/zurücksetzen; Modell- und Quelldaten erhalten. Endpunkt an G3. |
| **G3 - Entwurf nach G2** | Bestehenden LiveKit-Starter zu einer lokalen Kette aus Mikrofon, STT, Ollama und TTS verbinden. | G2 + konkrete STT-/Clientwahl; Codex klärt den Adapter vor Umsetzung. | Mehrere aufeinanderfolgende Sprachwechsel funktionieren; Unterbrechung beendet alte Ausgabe, nach Stille ist die nächste Eingabe möglich. | Starter separat betreiben und abschalten können; Gateway bleibt unverändert. Demonstration an G4. |
| **G4 - Entwurf nach G3** | Sprachzugang unter realer Last beurteilen und Betriebsprofil wählen. | G3; Codex misst, Tudor beurteilt Gesprächsgefühl. | Kurzes Mehrturn-Gespräch, Unterbrechungen und Wiederverbindung geprüft; Ladezeit, Antwortbeginn, Aussetzer und Speicher dokumentiert; akzeptables Tempo gemeinsam festgelegt. | Langsames Profil nicht zum Standard erklären; Engpass gezielt beheben. Optionaler Sprachzugang für P3. |

**Abhängigkeiten innerhalb der Audiomodule:** V1 und V2 können unabhängig vorbereitet werden; V3 braucht beide. Danach V4 -> G1 -> G2 -> G3 -> G4. Audioerstellung über G2 kann schon für einen Produktionsauftrag nützlich sein, ohne G3/G4 als Gesprächsoberfläche abzuwarten. Der Produktionspilot P2 braucht nur die für sein Ergebnis nötigen Module. GPU-lastige Tests nacheinander. Mobilzugriff bleibt eine spätere Bedienoption; Zeitpunkt und konkrete Umsetzung hängen vom Produktionsbedarf ab.

### Meilenstein S: Mail-Auswertung separat fertig auswerten

Der private Mail-Arbeitsstrang gehört zum SecOps-Bestand und ist keine Voraussetzung, um VoiceStudio vorzubereiten. Seine Ergebnisse werden nur bereinigt in diesen Fahrplan übernommen. Diese Dokumentation startet keinen neuen Mail-Lauf und versendet keine Nachrichten.

| ID / Status | Ergebnis und Umfang | Abhängigkeit / Zuständigkeit | Fertig, wenn ... | Rückweg / Übergabe |
| --- | --- | --- | --- | --- |
| **S1 - bereit zur Diagnose** | Ursachen der sieben fehlgeschlagenen Abschnitte auf der VM untersuchen; gegebenenfalls gezielter Wiederholungsplan. | B-Lauf beendet; Codex. | Fehlerursachen und betroffene Anzahl geklärt; erfolgreiche Ergebnisse bleiben erhalten; bereinigter Status nach begrenzter Wiederholung oder begründete Restlücke dokumentiert. | Private Sicherung und vorhandene Sperre nutzen; keine zweite Instanz, keine Rohmails in externe Werkzeuge. Ergebnis an S2. |
| **S2 - Entwurf nach S1** | 520 unbestätigte Kandidaten lokal gruppieren und eine kleine Reihenfolge konkreter Kontenprüfungen ableiten. | S1; Codex bereinigt, Tudor ordnet eigene Aktivitäten zu. | Konkrete Prüfaufgaben mit Quelle und Unsicherheit vorliegen; Mailbehauptung und bestätigtes Ereignis getrennt bleiben. | Originalbelege erhalten; keine automatische Kontenänderung und keine pauschale Entwarnung. |
| **S3 - Umfang noch festzulegen** | Vier Nachrichten ohne sichtbaren Text und relevante Anhänge als Abdeckungslücken behandeln. | Separater Analyseumfang; kein automatisches Nachladen externer Bilder. | Für ausgewählte Fälle eine lokale Prüfung oder eine ausdrücklich dokumentierte Restlücke vorliegt. | Anhänge nicht ausführen; Originale erhalten. Abdeckung in S2 ergänzen. |
| **S4 - wartet auf Export** | Konto A getrennt importieren und mit eigener Abdeckung auswerten. | Tudor stellt eindeutig zugeordneten Export bereit. | Integrität und Konto-Zuordnung geprüft; eigener Status und abschließende Lückenliste vorhanden. | Konto B unverändert lassen; kein Vermischen von Identitäten/Ergebnissen. |

## Recherche-Ergebnisse und zurückgestellte Optionen

Dies sind Quellenbewertungen vom 17.09.2026, keine eigenen Laufzeitnachweise, sofern nicht ausdrücklich als gemessen bezeichnet. Verfügbare Features, Lizenzen und Modelle können sich ändern.

| Projekt | Wofür es uns nützt | Einordnung / Entscheidung |
| --- | --- | --- |
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) + [TTS Audio Suite](https://github.com/diodiogod/TTS-Audio-Suite) | Vorhandene Community-Abläufe für reproduzierbaren Stimmvergleich. | Bereits getrennt vorbereitet; kein Grund, sofort eigene Cloning-Infrastruktur zu bauen. |
| [Qwen3-TTS Base 0.6B](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-Base) / [Chatterbox](https://huggingface.co/ResembleAI/chatterbox) | Lokales Cloning, bestehende Vergleichskandidaten. | Technische Tests bestanden; Zielstimmenvergleich offen. |
| [VoiceStudio](https://github.com/debpalash/VoiceStudio) | Lokale Stimmprofile, Cloning, Dubbing, Transkription, API und entferntes Backend. | Dritter Kandidat mit Standard-Engine OmniVoice. Aktive Beta; Fähigkeiten hängen von Engine ab. App AGPL-3.0, Modell-/Tokenizerbedingungen separat. Keine pauschale Lizenzfreigabe aus dem App-Namen ableiten. |
| [LiveKit Agents](https://github.com/livekit/agents) | Echtzeitgespräche, WebRTC, Unterbrechungen, STT/LLM/TTS und spätere Mobilclients. | Kandidat für den Sprachzugang zur Produktionsplattform, kein Ersatz für Produktionskoordination. Eigener Serverbetrieb möglich. Cloning bleibt ein eigener TTS-Baustein. Framework Apache-2.0; einzelne Modelle separat lizenziert. Noch nicht integriert. |
| [MCP Client for Ollama / ollmcp](https://github.com/jonigl/mcp-client-for-ollama) | Terminalclient für Modellgespräche mit MCP-Werkzeugen, Prompts und Ressourcen; möglicher Client für OmniRoute und dessen MCP-Schnittstelle. | Vorgemerkt und bei konkretem Nutzen zur Verwendung freigegeben. MIT, konfigurierbare Provider-Anbindung im geprüften Quellcode. `num_ctx` standardmäßig ungesetzt. Konkrete Verbindung, Authentifizierung, Werkzeugaufrufe und Kontextweitergabe noch gemeinsam testen; nicht installiert. Details bei der technischen Bestandsaufnahme. |
| [Kokoro Inno Clone Tuner](https://huggingface.co/remsky/kokoro-inno-clone-tuner) | Sehr kleine, schnelle Stimm-Anpassung für Kokoro. | Aktuell Englisch. 0,1-0,3 s beziehen sich laut Entwickler auf Profilerstellung nach Laden. Dessen normalisierte Identitätswertung: Inno 0,32, F5-TTS 0,94, auf einem englischen Testdatensatz. Keine Prozent-Genauigkeit und kein eigener Vergleich. Für starke Wiedererkennbarkeit vorerst nachrangig. |
| [Fish Audio](https://fish.audio/) | Optionale komfortable Cloud-Stimme. | Das Video nennt 15 s Referenzaufnahme. Begrenzter Gratistarif; genaue aktuelle Konditionen nicht verifiziert. Gezeigter Onlinedienst erfüllt nicht unseren lokalen Standard. |
| [OpenMontage](https://github.com/calesthio/OpenMontage) | Breitere Videoproduktion mit Analyse, Skripten, Szenen, Assets, Narration und Komposition. | Nach Zielkorrektur ein direkter Kandidat für einen Video-Produktionspilot. AGPL-3.0; nicht installiert oder im eigenen Ablauf geprüft. |
| [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | Vorgegebener Ablauf vom Thema über Skript, Clips, Stimme und Untertitel zum Kurzvideo. | Direkter Kandidat für einen Kurzvideo-Pilot. MIT; Ollama und selbst gehostetes Chatterbox vorgesehen. Standard-Edge-TTS benötigt Internet, auch ohne Key. Nicht installiert; keine Veröffentlichung beauftragt. |
| 3D-Generierung | Gewünschter Bereich für digitale Produkte und Produktionsassets. | Ziel ausdrücklich genannt; noch kein konkretes Modell, Tool, Ausgabeformat oder Absatzweg gewählt. Erst am passenden Pilotauftrag recherchieren. |
| [Colibri](https://github.com/JustVugg/colibri) | Große MoE-Modelle durch Expert-Auslagerung auf SSD/RAM/VRAM betreiben. | Große Gewichte bleiben groß: ungefähr 167 GB DeepSeek V4 Flash, 372 GB GLM-5.2 laut Projekt. Langsame Datenträger können unter 1 Token/s bedeuten. Große Varianten zurückgestellt: 12-GB-Grenze und flüssige Gespräche haben Vorrang. |
| [MiniCPM5-2B](https://huggingface.co/openbmb/MiniCPM5-2B) | Kleiner Coding-Kandidat. | Tatsächlich 2,52B Gesamtparameter, 131.072 Kontext laut Modellkarte. Autorenwerte: LiveCodeBench v6 69,1; SWE-bench Verified 46,4. Nicht installiert, genaue Videovariante unbestätigt. |
| [NeoHorse-1-4B](https://huggingface.co/TokenRhythm/NeoHorse-1-4B) | Kleiner Coding-/Agent-Kandidat. | Text-only; keine Vision-Gewichte. Beworbene 96,95 beziehen sich auf HumanEval; LiveCodeBench v6 59,43 laut Autor. Kein Nachweis allgemeiner Coding-Zuverlässigkeit, nicht installiert. |

**Offener Modellvergleich:** Ablehnungsquote, korrekte statt bloß bereitwillige Antworten, deutscher Chat, Coding, Vision, Werkzeuge und lange Kontexte sind getrennt zu messen. Die zuvor diskutierten Prozentwerte ersetzen diesen Vergleich nicht. Für einen späteren Test zuerst einen kleinen reproduzierbaren Aufgabensatz und identische Bedingungen festlegen; dafür den gewählten VM-Stand zunächst beibehalten.

## Mail-Stand mit Zeitbezug und Grenzen

Bereinigter Status auf `nucc` am **17.09.2026, 11:29 MESZ** direkt gelesen. Letzte Jobaktualisierung **09:20:28 MESZ**. `phase=finished_with_gaps`, Dienst `inactive/dead`, `Result=success`, `ExecMainStatus=0`.

| Zähler | Stand |
| --- | ---: |
| Nachrichten gesamt / klassifiziert | 4.201 / 4.194 |
| Nachrichten mit fehlgeschlagenen Abschnitten | 7 |
| Abschnitte gesamt / erfolgreich / fehlgeschlagen / wartend | 4.547 / 4.540 / 7 / 0 |
| Wegen Größe ausgelassen / Text gekürzt / Parser vollständig fehlgeschlagen | 0 / 0 / 0 |
| Nachrichten ohne sichtbaren Textkörper | 4 |
| Unbestätigte sicherheitsrelevante Kandidaten | 520 |
| Gezählt, nicht inhaltlich ausgewertet: Anhänge | 403 |

Die vier textlosen Nachrichten sind eine Abdeckungslücke innerhalb des Bestands und nicht vier zusätzliche Exportdateien. 99,8 % klassifizierte Nachrichten bedeuten **nicht** 99,8 % inhaltliche Genauigkeit oder vollständige Prüfung von Bildern/Anhängen. Klassifizierte Mailbehauptungen sind keine bestätigten Kontoereignisse. Konto A war nach der letzten vorliegenden Information noch ohne bereitgestellten Export.

Die Originalarchive, private SQLite-Datenbank, Agentenlogs und Rohmails bleiben außerhalb dieses Repos. Die bestehenden SecOps-Regeln gelten für die Weiterarbeit. Keine Provider-/Modellkonfiguration aus einer bloßen Statusabfrage heraus ändern.

## Ablagen und Nachweise

| Ablage / Datei | Zweck |
| --- | --- |
| [Haupt-README](<C:/Users/Tudor/Documents/Bad Wolf/Bad-Wolf/README.md>) | Herkunft und Inhalt des konsolidierten Repos. |
| [Schaltwerk-README](<C:/Users/Tudor/Documents/Bad Wolf/Bad-Wolf/schaltwerk/README.md>) | Proxy-Ablauf; Portangabe muss mit tatsächlichem Betrieb abgeglichen werden. |
| [VM-Installationsbeleg](<C:/Users/Tudor/Documents/Bad Wolf/vm-model-setup-20260917/deployment-receipt.json>) | Modell, Hashes, Kontext, Funktionstests, damalige Speicherbeobachtung. |
| [Stimmvergleich: START](<C:/Users/Tudor/Documents/Bad Wolf/voice-vorbereitung/START.txt>) | Aktueller Startweg und Hinweise zur vorbereiteten Umgebung. |
| [Stimmprüfung](<C:/Users/Tudor/Documents/Bad Wolf/voice-vorbereitung/verification.json>) / [Modellbestand](<C:/Users/Tudor/Documents/Bad Wolf/voice-vorbereitung/models.json>) | Tatsächliche Testergebnisse, Revisionen und Prüfsummen. |
| [Testsätze](<C:/Users/Tudor/Documents/Bad Wolf/voice-vorbereitung/testsätze.txt>) | Wiederverwendbare Sprachproben. |
| [Chrome-Lesezeichen](<C:/Users/Tudor/Documents/Bad Wolf/lesezeichen-20260917/lesezeichen.html>) | 428 Originaleinträge, 313 zusammengefasste Ziele; Sortierung aus Titel/URL, damals ohne Seitenprüfung. |
| [Private Mail-Übergabe](<C:/Users/Tudor/Documents/SecOps/05-Fortsetzung-20260917/B-AUSWERTUNG.md>) | Verfahren und Regeln; frühere Fortschrittszahlen dort werden durch den datierten Status oben ergänzt. |

Die lokalen Links beziehen sich auf diesen Windows-Arbeitsplatz und sind auf einem anderen Rechner anzupassen. Details zur Mail-Auswertung bleiben in SecOps. Die in einer anderen Aufgabe eingerichtete Obsidian-Ablage **Brain** kann später einen Verweis auf diesen Fahrplan erhalten; eine automatische Synchronisierung oder VM-/KI-Anbindung ist hier nicht eingerichtet.

### Die besprochenen Videoquellen

- [Lokaler Sprachassistent / Codacus](https://www.youtube.com/watch?v=xbedfuqYQYA): als vorhandene Referenz gesammelt; im aktuellen Quellenabgleich kein vollständiger eigener Videotest.
- [MiniCPM5](https://www.youtube.com/watch?v=Wik_JQ-enUA) und [NeoHorse](https://www.youtube.com/watch?v=3JRrNpozzpE): Modellkarten ausgewertet; Videoabruf damals fehlgeschlagen.
- [MoneyPrinterTurbo](https://www.youtube.com/watch?v=MY2zQ-9VEGY): beide gesendeten Links führten zum selben Video; Bewertung aus dem zugeordneten Repository, Videoabruf fehlgeschlagen.
- [VoiceStudio](https://www.youtube.com/watch?v=R0mq0IqiVUQ): Projekt-/Engine-Dokumentation geprüft; Videoabruf fehlgeschlagen.
- [Kokoro-Cloning](https://www.youtube.com/watch?v=K8NsnLNlRpA): Videobeschreibung führt zu [RayCodes_KokoroVoiceCloner](https://github.com/47thtechcorner/RayCodes_KokoroVoiceCloner), das den Inno-Tuner nutzt; Originalmodellkarte geprüft.
- [Cloning in 15 Sekunden](https://www.youtube.com/watch?v=X-1avE2MKP8): Videobeschreibung und automatisch erzeugtes englisches Transkript gelesen; Hauptbeispiel Fish Audio, Referenzlänge ab etwa 3:54.
- [Colibri](https://www.youtube.com/watch?v=kadY7AxpHYQ): Einschätzung aus offizieller Projektbeschreibung und Dokumentation; kein eigener Inferenztest und kein vollständiger Videoabruf.

### Weiterarbeiten ohne den ganzen Chat

**Aktuelle Pause am 17.09.2026:** Tudor lässt VM und Dienste weiterlaufen. Die angefragte Backup-/Shutdown-Vorbereitung wurde nach der lesenden Bestandsaufnahme pausiert: kein neuer Snapshot, keine Dienste gestoppt und keine Startabhängigkeiten geändert. GitHub-/Git-Abgleich ist für die Wiederaufnahme offen. Lokale Planungs- und Einrichtungsdateien sind vorhanden, aber damit nicht automatisch auf GitHub gesichert. [Exakter Pausenstand](<C:/Users/Tudor/Documents/Bad Wolf/vm-backup-20260917/PAUSE.md>).

Zuerst diesen Fahrplan und den Nachweis des jeweiligen Pakets lesen. **Aktuell laufen Q0/P1: Grundgedanke und Produktionsausrichtung klären.** Nicht zur verworfenen Reihenfolge „erst persönlicher Sprachassistent, irgendwann Produktion“ zurückkehren. V2 bleibt technisch vorbereitet, ist aber nicht automatisch der nächste Produktschritt. S1 ist ein eigener Diagnoseauftrag. Vor Änderungen den aktuellen Zustand erneut prüfen. Keine neuen Modelle oder Tools aus der Merkliste installieren, nur weil sie hier genannt sind. Nach einer Antwort zunächst Zielbild und Entscheidungen hier aktualisieren; erst daraus das nächste konkrete Umsetzungspaket ableiten.
