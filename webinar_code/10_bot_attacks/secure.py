from fastapi import FastAPI, Request, HTTPException

app = FastAPI()
inventory = {"item_1": 100}

@app.post("/reserve_item")
def reserve_item(item_id: str, request: Request):
    # FIX: Implement Business Logic Limits
    user_reservations = get_user_reservation_count(request.client.host)
    if user_reservations >= 2:
        raise HTTPException(status_code=400, detail="Max 2 items per user")
        
    # FIX: Bot Detection Integration (Conceptual)
    # if is_bot(request.headers):
    #     raise HTTPException(status_code=403, detail="Bot detected")

    if inventory[item_id] > 0:
        inventory[item_id] -= 1
        return {"status": "reserved"}
    return {"error": "out of stock"}
