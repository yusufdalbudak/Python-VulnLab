from fastapi import FastAPI
import time

app = FastAPI()

@app.post("/login")
def login(creds: dict):
    # VULNERABLE: No rate limit. Attacker can try 10,000 passwords/sec.
    # Also susceptible to resource exhaustion if logic is heavy.
    if check_password(creds):
        return {"token": "..."}
    return {"error": "Invalid"}, 401

@app.get("/heavy_report")
def heavy_report():
    # VULNERABLE: No resource limit. 
    # Attacker can trigger this 100 times to spike CPU/RAM.
    time.sleep(5) # Simulating heavy work
    return {"report": "data"}
