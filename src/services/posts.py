"""Service module for post-related operations."""

from src._client.post import PostServiceClient
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

    async def get_all_posts(self) -> list[Post]:
        """Return a list of all posts.

        Returns
        -------
        list[Post]
            A list containing all posts.

        """
        posts = await self._client.get("/posts")
        return [Post(**post) for post in posts]
