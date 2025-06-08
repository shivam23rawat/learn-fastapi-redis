"""Conftest file for pytest configuration and fixtures."""

from collections.abc import AsyncGenerator

import pytest
from httpx import AsyncClient

from src.app import app


@pytest.fixture(scope="module")
def anyio_backend() -> str:
    """Fixture to specify the anyio backend as asyncio."""
    return "asyncio"


@pytest.fixture(scope="module")
async def async_client() -> AsyncGenerator[AsyncClient]:
    """Asynchronous fixture that provides an HTTPX AsyncClient for testing."""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


def test_health(async_client: AsyncClient) -> None:
    """Test the health endpoint (currently a placeholder)."""
    # Health endpoint not implemented, placeholder
