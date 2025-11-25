from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# VULNERABLE: Docs exposed in production (/docs, /redoc)
app = FastAPI(debug=True) # VULNERABLE: Debug mode enabled

# VULNERABLE: CORS allows ALL origins with credentials
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True, # This combination is dangerous!
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/admin_info")
def admin_info():
    return {"key": "secret_key"}
