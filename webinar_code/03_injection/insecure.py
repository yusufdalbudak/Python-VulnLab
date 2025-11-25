import os
import sqlite3
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_user(username: str):
    # VULNERABLE: SQL Injection via string concatenation
    # Exploit: username = "' OR '1'='1" -> dumps all users
    query = f"SELECT * FROM users WHERE username = '{username}'"
    conn = sqlite3.connect("db.sqlite")
    return conn.execute(query).fetchall()

@app.post("/ping")
def ping_host(hostname: str):
    # VULNERABLE: OS Command Injection
    # Exploit: hostname = "google.com; cat /etc/passwd"
    os.system(f"ping -c 1 {hostname}")
    return {"status": "ok"}
