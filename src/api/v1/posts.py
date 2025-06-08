"""Defines APIs for managing posts related operations."""

from typing import Annotated

from fastapi import APIRouter, Depends, status

from src._schemas.posts import Post
from src.logger import get_logger
from src.services.posts import PostService

router = APIRouter(prefix="/post", tags=["posts"])
logger = get_logger("api.v1.posts")


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    summary="Get list of all posts",
    description="API to fetch a list of all posts.",
)
async def get_post_list(
    post_service: Annotated[PostService, Depends(PostService)],
) -> list[Post]:
    """Get a list of all posts.

    Returns
    -------
    List[Post]
        A list of posts.

    """
    logger.info("Handling GET /post request.")
    posts = await post_service.get_all_posts()
    logger.debug("Returning %d posts.", len(posts))
    return posts
