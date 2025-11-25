from fastapi import FastAPI, HTTPException, Request

app = FastAPI()

# FIX: Explicitly deprecate and sunset old versions
@app.get("/v1/users", deprecated=True)
def get_users_v1():
    # FIX: Return 410 Gone or redirect to v2
    raise HTTPException(status_code=410, detail="API v1 is deprecated. Use v2.")

@app.get("/v2/users")
def get_users_v2():
    # Secure logic
    return [{"id": 1, "name": "admin"}]

# FIX: Remove Shadow APIs entirely in production
# If needed for dev, use conditional inclusion
# if settings.DEBUG:
#    @app.get("/test_debug_endpoint")...
