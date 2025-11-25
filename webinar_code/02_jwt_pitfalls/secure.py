import jwt
import os

# FIX: Load strong secret from environment
SECRET = os.environ.get("JWT_SECRET_KEY") 

def verify_token_secure(token):
    # FIX: Explicitly whitelist ONLY strong algorithms (RS256 preferred)
    # 'none' is excluded.
    try:
        payload = jwt.decode(token, SECRET, algorithms=["RS256"])
        return payload
    except jwt.InvalidTokenError:
        raise Exception("Invalid Token")

def create_token_secure(user_id):
    # FIX: Minimal payload, no PII. Use 'sub' for ID.
    # Short expiration time (exp) should be added.
    payload = {"sub": user_id, "role": "user"} 
    return jwt.encode(payload, SECRET, algorithm="RS256")
