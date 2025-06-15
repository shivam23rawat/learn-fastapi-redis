"""Test module for PostService."""

import pytest

from src.services.posts import PostService


@pytest.mark.anyio
async def test_post_service_get_all_posts() -> None:
    """Test getting all posts from PostService."""

    class DummyRedis:
        async def get(self, _key: str) -> str | None:
            return None

        async def set(
            self,
            _key: str,
            _value: str,
            ex: int | None = None,
        ) -> bool:
            _ = ex  # Mark as intentionally unused
            return True

    class DummyClient:
        async def get(self, _endpoint: str) -> list[dict]:
            return [{"userId": 1, "id": 1, "title": "Test", "body": "Body"}]

    service = PostService(redis=DummyRedis(), client=DummyClient())
    posts = await service.get_all_posts()
    if len(posts) != 1:
        pytest.fail(f"Expected 1 post, got {len(posts)}")
    if posts[0].title != "Test":
        pytest.fail(f"Expected post title 'Test', got '{posts[0].title}'")


@pytest.mark.anyio
async def test_post_service_cache_hit() -> None:
    """Test getting posts from cache (cache hit)."""

    class DummyRedis:
        async def get(self, _key: str) -> list[dict]:
            return [{"userId": 2, "id": 2, "title": "Cached", "body": "Body"}]

        async def set(
            self,
            _key: str,
            _value: str,
            ex: int | None = None,
        ) -> bool:
            _ = ex  # Mark as intentionally unused
            return True

    class DummyClient:
        async def get(self, _endpoint: str) -> list[dict]:
            pytest.fail("Should not call external API on cache hit")

    service = PostService(redis=DummyRedis(), client=DummyClient())
    posts = await service.get_all_posts()
    if len(posts) != 1:
        pytest.fail(f"Expected 1 post from cache, got {len(posts)}")
    expected = posts[0].title
    if expected != "Cached":
        pytest.fail(
            f"Expected cached post title 'Cached', got '{expected}'",
        )


@pytest.mark.anyio
async def test_post_service_external_api_error() -> None:
    """Test error handling when external API fails."""

    class DummyRedis:
        async def get(self, _key: str) -> None:
            return None

        async def set(
            self,
            _key: str,
            _value: str,
            ex: int | None = None,
        ) -> bool:
            _ = ex  # Mark as intentionally unused
            return True

    class DummyClient:
        async def get(self, _endpoint: str) -> list[dict]:
            msg = "External API failure"
            raise RuntimeError(msg)

    service = PostService(redis=DummyRedis(), client=DummyClient())
    try:
        await service.get_all_posts()
        pytest.fail("Expected exception from external API")
    except RuntimeError as exc:
        if "External API failure" not in str(exc):
            pytest.fail(f"Unexpected error: {exc}")
