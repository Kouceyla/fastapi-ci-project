from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    """Teste le point de terminaison racine (/)."""
    response = client.get("/")
    
    assert response.status_code == 200
    assert response.json() == {"message": "Bonjour, la pipeline CI fonctionne !"}

def test_read_item():
    """Teste le point de terminaison /items/{item_id}."""
    response = client.get("/items/5?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "q": "test"}