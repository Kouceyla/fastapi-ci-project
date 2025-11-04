# test_main.py
from fastapi.testclient import TestClient
from main import app

# Crée un client de test basé sur notre application FastAPI
client = TestClient(app)

def test_read_root():
    """Teste le point de terminaison racine (/)."""
    response = client.get("/")
    # Vérifie que le code de statut est 200 (OK)
    assert response.status_code == 200
    # Vérifie que la réponse JSON est correcte
    assert response.json() == {"message": "Bonjour, la pipeline CI fonctionne !"}

def test_read_item():
    """Teste le point de terminaison /items/{item_id}."""
    response = client.get("/items/5?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "q": "test"}