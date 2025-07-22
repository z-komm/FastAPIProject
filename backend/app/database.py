# backend/app/database.py

def get_vector_connection():
    import sqlite3
    conn = sqlite3.connect("data/database/knowledge.db")
    conn.enable_load_extension(True)
    conn.execute("SELECT load_extension('vector0')")
    return conn