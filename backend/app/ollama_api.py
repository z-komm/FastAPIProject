# backend/app/ollama_api.py

import httpx
import asyncio

OLLAMA_URL = "http://localhost:11434/api/generate"


async def stream_ollama_response(websocket, prompt):
    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream("POST", OLLAMA_URL,
                                 json={"prompt": prompt, "stream": True, "model": "mistral"}) as resp:
            async for line in resp.aiter_lines():
                if line.strip():
                    await websocket.send_text(line)
                    await asyncio.sleep(0.01)