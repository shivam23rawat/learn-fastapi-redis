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
            _ex: int | None = None,
        ) -> bool:
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
