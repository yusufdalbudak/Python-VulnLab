from fastapi import FastAPI
import hashlib

app = FastAPI()

@app.get("/hash_files")
def hash_files(n: int):
    # VULNERABLE: Resource Exhaustion (L7 DDoS target)
    # Attacker sends n=1000000. Server CPU spikes to 100%.
    result = ""
    for i in range(n):
        result += hashlib.sha256(str(i).encode()).hexdigest()
    return {"hash": result}
