import pytest
from src.prisma import prisma

@pytest.fixture
@pytest.mark.asyncio
async def init_prisma():
  await prisma.connect();
  yield
  await prisma.disconnect();