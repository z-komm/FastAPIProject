# backend/Dockerfile

FROM python:3.11-slim

# System-Updates und Grundpakete
RUN apt-get update && \
    apt-get install -y build-essential sqlite3 && \
    rm -rf /var/lib/apt/lists/*

# Arbeitsverzeichnis definieren
WORKDIR /app

# Anforderungen installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Projektdateien kopieren
COPY app ./app
COPY data ./data

# SQLite-vec Extension vorbereiten (falls extern erforderlich)
# Hier ggf. sqlite-vec setup ergänzen, falls manuell erforderlich

# Port öffnen
EXPOSE 8000

# Startbefehl
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
