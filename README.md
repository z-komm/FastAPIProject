# 🛠️ KI-Inhouse-Chat-System (RAG + Ollama)

## Projektbeschreibung

Dieses System stellt ein webbasiertes, mehrbenutzerfähiges Chatinterface bereit, das mit einem lokalen Ollama-Modell arbeitet und per RAG (Retrieval-Augmented Generation) unternehmensinterne Dokumente durchsucht. Sessions werden gespeichert, inklusive KI-generierter Zusammenfassungen. Quellenangaben sind in jeder Antwort enthalten.

---

## Features

- ✅ Ollama-Integration (lokal)
- ✅ Dokumentenpool (RAG, sqlite-vec)
- ✅ System- & Master-Prompt (zentral steuerbar)
- ✅ Multiuser-Chat via WebSocket
- ✅ Streaming-Antworten (wie ChatGPT)
- ✅ Session-Management inkl. Zusammenfassungen
- ✅ Quellenangabe + Verlinkung
- ✅ Intranet-fähiges Deployment (Docker)

---

## Verzeichnisstruktur

```plaintext
backend/           # FastAPI + RAG Backend
frontend/          # React Frontend (geplant)
data/              # Dokumente und SQLite-Datenbank
docker-compose.yml
README.md
