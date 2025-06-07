"""Defines APIs for managing posts related operations."""

from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.services.posts import PostService

router = APIRouter(prefix="/post", tags=["posts"])


@router.get(
    "/list",
    status_code=status.HTTP_200_OK,
    summary="Get list of all posts",
    description="API to fetch a list of all posts.",
)
async def get_post_list(
    post_service: Annotated[PostService, Depends(PostService)],
) -> list[str]:
    """Get a list of all posts.

    Returns
    -------
    List[str]
        A list of posts.

    """
    return post_service.get_all_posts()
