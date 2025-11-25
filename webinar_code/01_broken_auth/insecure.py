from fastapi import FastAPI, HTTPException
# VULNERABLE: No rate limiting, weak auth logic
app = FastAPI()

fake_db = {
    "1": {"id": "1", "owner": "user_a", "data": "Sensitive A"},
    "2": {"id": "2", "owner": "user_b", "data": "Sensitive B"}
}

@app.post("/login")
def login(creds: dict):
    # VULNERABLE: Susceptible to credential stuffing & brute force
    # No account lockout or rate limit mechanism
    if creds["username"] == "admin" and creds["password"] == "123456":
        return {"token": "admin_token"}
    return {"error": "Invalid"}, 401

@app.get("/invoice/{invoice_id}")
def get_invoice(invoice_id: str):
    # VULNERABLE: Broken Object Level Authorization (BOLA)
    # No check if the current user actually owns this invoice
    if invoice_id in fake_db:
        return fake_db[invoice_id] # Exploit: curl /invoice/2 (even if I am user_a)
    raise HTTPException(status_code=404)
