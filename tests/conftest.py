"""Conftest file for pytest configuration and fixtures."""

from collections.abc import AsyncGenerator

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
