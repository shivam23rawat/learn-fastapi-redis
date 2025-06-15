"""Service module for post-related operations."""

from datetime import timedelta

from src._client.post import PostServiceClient
from src._database.redis import redis_client
from src._schemas.posts import Post
from src.logger import get_logger


class PostService:
    """Service class for user-related operations.

    Methods
    -------
    get_all_posts() -> list[Post]
        Returns a list of all posts.

    """

    def __init__(
        self,
        client: object = None,
        redis: object = None,
    ) -> None:
        """Init PostService with optional client and redis for tests."""
        self._logger = get_logger("PostService")
        self._logger.debug("Initializing PostService.")
        self._client = client if client is not None else PostServiceClient()
        self._redis = redis if redis is not None else redis_client
        self._post_cache_expiry_time = timedelta(minutes=5)

    async def get_all_posts(self) -> list[Post]:
        """Return a list of all posts.

        Returns
        -------
        list[Post]
            A list containing all posts.

        """
        self._logger.info("Fetching all posts (with cache).")
        posts = await self._redis.get("all_posts")
        if not posts:
            self._logger.debug(
                "Cache miss for all_posts. Fetching from PostServiceClient.",
            )
            posts = await self._client.get("/posts")
            await self._redis.set(
                "all_posts",
                posts,
                ex=self._post_cache_expiry_time,
            )
            self._logger.debug("Posts cached in Redis.")
        else:
            self._logger.debug("Cache hit for all_posts.")
        return [Post(**post) for post in posts]
