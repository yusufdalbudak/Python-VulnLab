from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
# FIX: Import rate limiter (conceptual) and auth dependencies

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_db = {
    "1": {"id": "1", "owner": "user_a", "data": "Sensitive A"},
    "2": {"id": "2", "owner": "user_b", "data": "Sensitive B"}
}

def get_current_user(token: str = Depends(oauth2_scheme)):
    # FIX: Validate token and identify user
    if token == "valid_token_user_a":
        return "user_a"
    raise HTTPException(status_code=401)

@app.post("/login")
# FIX: Apply rate limiting decorator (e.g., 5 req/min)
def login(creds: dict):
    # FIX: Use strong password hashing (bcrypt) and account lockout policies
    # verify_password(creds["password"], stored_hash)
    return {"token": "valid_token_user_a"}

@app.get("/invoice/{invoice_id}")
def get_invoice(invoice_id: str, user: str = Depends(get_current_user)):
    if invoice_id not in fake_db:
        raise HTTPException(status_code=404)
    
    invoice = fake_db[invoice_id]
    
    # FIX: Authorization check - Ensure requester owns the object
    if invoice["owner"] != user:
        raise HTTPException(status_code=403, detail="Not authorized")
        
    return invoice
