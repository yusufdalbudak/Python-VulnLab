import json
import yaml
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel

app = FastAPI()

class CartItem(BaseModel):
    item_id: str
    quantity: int

@app.post("/cart")
async def load_cart(cart_items: list[CartItem]):
    # FIX: Use JSON instead of pickle. JSON is data-only, no code execution.
    # Pydantic validates the schema automatically.
    return {"cart": cart_items}

@app.post("/config")
async def load_config(request: Request):
    content = await request.body()
    try:
        # FIX: Use safe_load which restricts to standard YAML tags only
        config = yaml.safe_load(content)
        return config
    except yaml.YAMLError:
        raise HTTPException(status_code=400, detail="Invalid YAML")
