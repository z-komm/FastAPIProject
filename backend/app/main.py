# backend/app/main.py

from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from app.websocket import chat_endpoint
from app.session_manager import get_sessions, load_session
from app.document_loader import refresh_documents

app = FastAPI()

# CORS freischalten (für Frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# WebSocket Endpoint
app.websocket("/ws/chat")(chat_endpoint)


# REST Endpoints
@app.get("/api/sessions")
def list_sessions():
    return get_sessions()


@app.get("/api/sessions/{session_id}")
def load(session_id: int):
    return load_session(session_id)


@app.post("/api/documents/refresh")
def reload_documents():
    return refresh_documents()





















