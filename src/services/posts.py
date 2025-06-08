"""Service module for post-related operations."""

from datetime import timedelta

from src._client.post import PostServiceClient
from src._database.redis import redis_client
from src._schemas.posts import Post


class PostService:
    """Service class for user-related operations.

    Methods
    -------
    get_all_posts() -> list[Post]
        Returns a list of all posts.

    """

    def __init__(self) -> None:
        """Initialize the PostService."""
        self._client = PostServiceClient()
        self._redis = redis_client
        self._post_cache_expiry_time = timedelta(minutes=5)

    async def get_all_posts(self) -> list[Post]:
        """Return a list of all posts.

        Returns
        -------
        list[Post]
            A list containing all posts.

        """
        posts = await self._redis.get("all_posts")
        if not posts:
            posts = await self._client.get("/posts")
            await self._redis.set(
                "all_posts",
                posts,
                ex=self._post_cache_expiry_time,
            )
        return [Post(**post) for post in posts]
