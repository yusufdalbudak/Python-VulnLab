import pickle
import yaml
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/cart")
async def load_cart(request: Request):
    # VULNERABLE: Pickle allows arbitrary code execution during unpickling
    # Exploit: Attacker sends a pickled object that runs os.system('rm -rf /')
    data = await request.body()
    cart = pickle.loads(data) 
    return {"cart": cart}

@app.post("/config")
async def load_config(request: Request):
    # VULNERABLE: yaml.load is unsafe by default in older versions or if Loader is not specified
    # Exploit: YAML payload !!python/object/apply:os.system ["cat /etc/passwd"]
    content = await request.body()
    config = yaml.load(content, Loader=yaml.Loader)
    return config
