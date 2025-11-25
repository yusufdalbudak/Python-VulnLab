from fastapi import FastAPI

app = FastAPI()

inventory = {"item_1": 100}

@app.post("/reserve_item")
def reserve_item(item_id: str):
    # VULNERABLE: Business Logic Abuse
    # No CAPTCHA, no limit on reservations per user.
    # A bot can reserve ALL items instantly, denying real users.
    if inventory[item_id] > 0:
        inventory[item_id] -= 1
        return {"status": "reserved"}
    return {"error": "out of stock"}
