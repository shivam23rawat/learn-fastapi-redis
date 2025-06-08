"""Test suite for post-related API endpoints."""

from http import HTTPStatus

import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_get_posts(async_client: AsyncClient) -> None:
    """Test retrieving posts from the /v1/post endpoint."""
    response = await async_client.get("/v1/post")
    expected_status = HTTPStatus.OK
    if response.status_code != expected_status:
        msg = (
            (
                f"Expected status code {expected_status}, "
                f"got {response.status_code}"
            ),
        )
        raise AssertionError(msg)
    if not isinstance(response.json(), list):
        msg = "Response JSON is not a list"
        raise TypeError(msg)


# Add more tests for error cases, cache, etc. as needed
