from fastapi.testclient import TestClient
import pytest
from prisma import Prisma

from main import app

client = TestClient(app)
prisma = Prisma()


def test_root():
    response = client.get("/")
    assert response.status_code == 200
