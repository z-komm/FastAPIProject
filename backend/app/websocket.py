# backend/app/websocket.py

from fastapi import WebSocket
from app.ollama_api import stream_ollama_response
from app.rag_engine import fetch_relevant_chunks
from app.session_manager import save_message
from app.config import get_combined_prompt


async def chat_endpoint(websocket: WebSocket):
    await websocket.accept()
    session_id = None
    while True:
        message = await websocket.receive_text()
        if message.startswith("__SESSION__"):
            session_id = int(message.replace("__SESSION__", ""))
            continue

        system_prompt = get_combined_prompt()
        chunks, sources = fetch_relevant_chunks(message)
        prompt = f"{system_prompt}\n\nQuellen:\n{sources}\n\n{chunks}\n\nUser: {message}"

        await stream_ollama_response(websocket, prompt)
        if session_id:
            save_message(session_id, "user", message)
            save_message(session_id, "assistant", "[Antwort gestreamt]")