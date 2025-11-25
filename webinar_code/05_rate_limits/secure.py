from fastapi import FastAPI, Request, HTTPException
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# FIX: Initialize Rate Limiter
limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

def check_password(creds: dict) -> bool:
    """
    Simple placeholder password check. Replace with real secure verification
    (e.g. hash compare against database) in production.
    """
    if not isinstance(creds, dict):
        return False
    username = creds.get("username")
    password = creds.get("password")
    if not username or not password:
        return False
    # Placeholder logic: accept a known test password; change for real usage.
    return password == "secret"

@app.post("/login")
@limiter.limit("5/minute") # FIX: Limit to 5 attempts per minute per IP
def login(creds: dict, request: Request):
    if check_password(creds):
        return {"token": "..."}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/heavy_report")
@limiter.limit("10/hour") # FIX: Strict limit on heavy resources
def heavy_report(request: Request):
    # Ideally also use background tasks or caching
    return {"report": "data"}
