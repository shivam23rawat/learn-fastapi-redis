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
        pytest.fail(
            f"Expected status code {expected_status}, "
            f"got {response.status_code}",
        )
    if not isinstance(response.json(), list):
        pytest.fail("Response JSON is not a list")


@pytest.mark.anyio
async def test_get_posts_cache(
    async_client: AsyncClient,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test retrieving posts with cache hit."""
    from src.services.posts import PostService

    async def fake_get_all_posts(_self: object) -> list[dict]:
        return [{"user_id": 1, "id": 1, "title": "Cached", "body": "Body"}]

    monkeypatch.setattr(PostService, "get_all_posts", fake_get_all_posts)
    response = await async_client.get("/v1/post")
    if response.status_code != HTTPStatus.OK:
        pytest.fail(
            f"Expected status code {HTTPStatus.OK}, "
            f"got {response.status_code}",
        )
    if response.json()[0]["title"] != "Cached":
        pytest.fail("Expected cached post title 'Cached'")


@pytest.mark.anyio
async def test_get_posts_external_api_failure(
    async_client: AsyncClient,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test error handling when external API fails."""
    from fastapi import HTTPException

    from src.services.posts import PostService

    async def fake_get_all_posts(_self: object) -> list[dict]:
        msg = "External API failure"
        raise HTTPException(status_code=500, detail=msg)

    monkeypatch.setattr(PostService, "get_all_posts", fake_get_all_posts)
    response = await async_client.get("/v1/post")
    if response.status_code not in {
        HTTPStatus.INTERNAL_SERVER_ERROR,
        HTTPStatus.UNPROCESSABLE_ENTITY,
    }:
        pytest.fail(
            f"Expected 500 or 422, got {response.status_code}",
        )


# Add more tests for error cases, cache, etc. as needed
