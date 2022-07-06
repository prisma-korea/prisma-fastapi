import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


@pytest.mark.usefixtures("init_prisma")
class BaseTest:
    pass


class TestUser(BaseTest):
    def test_read_users(self):
        response = client.get("/apis/users")
        assert response.status_code == 200
