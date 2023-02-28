from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


async def test_read_users():
    with client:
        response = client.get("/apis/users")
        assert response.status_code == 200
