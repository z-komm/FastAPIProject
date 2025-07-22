# backend/app/session_manager.py

def get_sessions():
    # Dummy implementation
    return [{"id": 1, "title": "Test-Session"}]


def load_session(session_id: int):
    return {"id": session_id, "messages": []}


def save_message(session_id, role, content):
    pass