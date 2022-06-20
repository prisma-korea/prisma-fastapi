# from fastapi.testclient import TestClient
# import pytest
# from prisma import Prisma

# from main import app

# client = TestClient(app)
# prisma = Prisma()


# # @pytest.fixture(scope="function", autouse=True)
# # async def test_init(request):
# #     await prisma.connect()
# #     yield
# #     await prisma.disconnect()


# async def test_read_users():
#     await prisma.connect()
#     response = client.get("/apis/users")
#     assert response.status_code == 200
