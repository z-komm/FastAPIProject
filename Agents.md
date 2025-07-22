# Agents.md – Aktuelles Backend-Setup KI-Chat-System

## Ziel

Das Backend stellt ein mehrbenutzerfähiges KI-Chat-Interface zur Verfügung. Es basiert auf FastAPI, Ollama (lokaler LLM-Server) und einem RAG-Modul über sqlite-vec für den Zugriff auf Dokumentenwissen.

Das System kann lokal oder via Docker Compose betrieben werden.

## Architektur

### Module

* **main.py**
  Initialisiert FastAPI, CORS, WebSocket- und REST-Endpoints.

* **websocket.py**
  WebSocket-Handler für Echtzeit-Streaming-Chats.
  Verbindet User-Sessions, integriert RAG, sendet Ollama-Streaming-Antworten.

* **ollama\_api.py**
  Proxy-Modul:

  * Übergibt Prompts an Ollama.
  * Streamt Token-Antworten zurück via WebSocket.

* **rag\_engine.py**
  RAG-Logik (sqlite-vec):

  * Verbindet sich zur SQLite-Datenbank.
  * Führt Vektor-Suche nach relevanten Dokument-Abschnitten aus.
  * Gibt Top-K Chunks + Quellen zurück.

* **config.py**
  Verbindet System- und Masterprompt aus Konfigurationsdateien.

* **session\_manager.py**
  Aktuell Dummy-Implementierung für Sessions.
  Ziel: Speicherung und Wiederabruf aller Chatverläufe.

* **document\_loader.py**
  Bereitet Dokumenten-Neuladen über REST-API vor (aktuell Dummy).

* **database.py**
  Öffnet SQLite-Datenbank. Lädt sqlite-vec Extension ("vector0").

### API-Schnittstellen

| Endpunkt               | Methode   | Beschreibung                    |
| ---------------------- | --------- | ------------------------------- |
| /ws/chat               | WebSocket | Chat mit Ollama + RAG-Streaming |
| /api/sessions          | GET       | Sessions abrufen (Dummy)        |
| /api/sessions/{id}     | GET       | Session laden (Dummy)           |
| /api/documents/refresh | POST      | Dokumente neu laden (Dummy)     |

## Technologiestack

* **FastAPI** für REST-API & WebSockets
* **httpx** für Kommunikation mit Ollama
* **sqlite-vec** zur Dokumenten-Vektorisierung
* **Ollama** (lokaler LLM-Server, Modell: mistral)
* **Docker / Docker Compose** für Deployment

## Erweiterungsschritte (Next Milestones)

1. **Session-Management ausbauen**

   * Sessions persistent in SQLite speichern.
   * Messages mit Rollen (user/assistant) sichern.
   * Zusammenfassungen generieren und abspeichern.

2. **Dokumenten-Loader implementieren**

   * Dokumente chunken und vektorisieren.
   * Upload-/Refresh-Mechanik über REST vervollständigen.

3. **Quellenformatierung verbessern**

   * Quellenangaben als klickbare Links.
   * Abschnitte klar mit Quellen verknüpfen.

4. **Authentifizierung (optional)**

   * Multiuser-System absichern (Token oder Basis-Auth).

5. **Frontend-Anbindung vorbereiten**

   * WebSocket-Client auf Frontend-Seite.
   * Session-Übersicht und Zusammenfassungen im UI anzeigen.

## Start/Deployment

* Lokal:

  ```bash
  uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
  ```

* Docker Compose:

  ```bash
  docker-compose up --build -d
  ```

## Hinweis

Ollama muss intern auf Port 11434 erreichbar sein.
Datenbank liegt in `/backend/data/database/knowledge.db`.
Dokumente befinden sich in `/backend/data/documents/`.

System- und Masterprompt werden aus Textdateien in `/app/config/` geladen.
