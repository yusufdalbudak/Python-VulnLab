from fastapi import FastAPI, HTTPException

app = FastAPI()

MAX_N = 1000

@app.get("/hash_files")
def hash_files(n: int):
    # FIX: Input Validation & Resource Limits
    if n > MAX_N:
        raise HTTPException(status_code=400, detail=f"Max n is {MAX_N}")
        
    # FIX: Caching (Conceptual)
    # if cache.get(n): return cache.get(n)
    
    result = ""
    for i in range(n):
        result += hashlib.sha256(str(i).encode()).hexdigest()
    return {"hash": result}
