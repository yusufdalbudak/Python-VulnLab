import jwt

SECRET = "weak_secret" # VULNERABLE: Hardcoded and weak secret

def verify_token_insecure(token):
    # VULNERABLE: Allows 'none' algorithm
    # Exploit: Attacker sends header {"alg": "none"} and removes signature
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256", "none"])
        return payload
    except:
        return None

def create_token_insecure(user_data):
    # VULNERABLE: Storing sensitive PII in payload
    # Base64 is NOT encryption; anyone can read this
    payload = {"sub": "123", "credit_card": "4111-2222-3333-4444"} 
    return jwt.encode(payload, SECRET, algorithm="HS256")
