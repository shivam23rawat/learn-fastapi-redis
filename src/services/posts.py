"""Service module for post-related operations."""

from typing import Any


class PostService:
    """Service class for user-related operations.

    Methods
    -------
    get_all_posts() -> List[Dict[str, Any]]
        Returns a list of all posts.

    """

    def get_all_posts(self) -> list[dict[str, Any]]:
        """Return a list of all posts.

        Returns
        -------
        List[Dict[str, Any]]
            A list containing all posts.

        """
        return [
            {
                "userId": 1,
                "id": 1,
                "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
            },
            {
                "userId": 1,
                "id": 2,
                "title": "qui est esse",
                "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla",
            },
        ]
