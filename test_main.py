from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_item():
    response = client.get("/")
    assert response.status_code == 200

