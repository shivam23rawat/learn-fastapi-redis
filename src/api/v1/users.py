"""
Users router file, this module defines the APIs for user-related
endpoints.
"""

from typing import List
from fastapi import APIRouter, status

from src.services.users import UserService

router = APIRouter(prefix="/user", tags=["user"])


@router.get(
    "/list",
    response_model=List[str],
    status_code=status.HTTP_200_OK,
    tags=["user"],
    summary="Get User List",
    description="API to fetch a list of all users of the app.",
)
async def get_user_list() -> List[str]:
    """
    API to get a list of all users.

    Returns
    -------
    List[str]
        A list of usernames.
    """
    user_service = UserService()
    return user_service.get_all_users()
