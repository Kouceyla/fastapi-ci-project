from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """Point de terminaison racine qui retourne un message de bienvenue."""
    return {"message": "Bonjour, la pipeline CI fonctionne !"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    """Point de terminaison pour récupérer un item."""
    return {"item_id": item_id, "q": q}