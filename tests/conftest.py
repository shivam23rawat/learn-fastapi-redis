"""Conftest file for pytest configuration and fixtures."""

from collections.abc import AsyncGenerator
from unittest.mock import AsyncMock

import pytest
from httpx import ASGITransport, AsyncClient

from src.app import app


@pytest.fixture(scope="module")
def anyio_backend() -> str:
    """Fixture to specify the anyio backend as asyncio."""
    return "asyncio"


@pytest.fixture(scope="module")
async def async_client() -> AsyncGenerator[AsyncClient]:
    """Asynchronous fixture that provides an HTTPX AsyncClient for testing."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.fixture(autouse=True)
def mock_redis_client(monkeypatch: pytest.MonkeyPatch) -> None:
    """Patch redis_client with a dummy async mock for all tests."""
    from src._database import redis as redis_module

    dummy = AsyncMock()
    dummy.get.return_value = None
    dummy.set.return_value = True
    dummy.incr.return_value = 1
    monkeypatch.setattr(redis_module, "redis_client", dummy)
