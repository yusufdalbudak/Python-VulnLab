import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# FIX: Disable docs and debug in production
ENVIRONMENT = os.getenv("ENV", "production")
SHOW_DOCS = ENVIRONMENT == "development"

app = FastAPI(
    docs_url="/docs" if SHOW_DOCS else None,
    redoc_url=None,
    openapi_url="/openapi.json" if SHOW_DOCS else None,
    debug=False # FIX: Never run debug=True in prod
)

# FIX: Whitelist specific trusted domains
origins = [
    "https://frontend.example.com",
    "https://mobile.example.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # FIX: Strict origin list
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)
