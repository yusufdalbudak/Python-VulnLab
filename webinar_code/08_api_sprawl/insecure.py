from fastapi import FastAPI

app = FastAPI()

# VULNERABLE: Deprecated version still active and unmaintained
@app.get("/v1/users")
def get_users_v1():
    # Old logic with known vulnerabilities (e.g., no auth)
    return [{"id": 1, "name": "admin"}] 

@app.get("/v2/users")
def get_users_v2():
    # Secure logic
    return [{"id": 1, "name": "admin"}]

# VULNERABLE: Shadow API endpoint (undocumented, for testing)
@app.get("/test_debug_endpoint")
def debug_test():
    return {"system_env": "production"}
