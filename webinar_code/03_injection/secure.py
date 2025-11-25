import subprocess
import sqlite3
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_user(username: str):
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()
    # FIX: Use parameterized queries (binding)
    # The DB driver handles escaping automatically
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchall()

@app.post("/ping")
def ping_host(hostname: str):
    # FIX: Use subprocess.run with a list of arguments
    # Shell=False (default) prevents command chaining
    try:
        # Validate hostname format first (e.g. regex)
        subprocess.run(["ping", "-c", "1", hostname], check=True)
        return {"status": "ok"}
    except subprocess.CalledProcessError:
        return {"status": "error"}
