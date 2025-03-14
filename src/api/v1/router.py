"""
This module defines the API router for version 1 of the application.
It imports the necessary modules and includes the sample router with a specified prefix and tags.
Attributes
----------
router : fastapi.APIRouter
    The main router for version 1 of the API.
Modules
-------
fastapi
    The FastAPI framework used to create the API router.
src.api.v1.users
    The module containing the user router to be included in the main router.
"""

from fastapi import APIRouter

from src.api.v1.users import router as user_router

router = APIRouter()

# NOTE: duplicate APIs may show up in swagger but atleast the APIs get clubbed
# under the same version
router.include_router(user_router, prefix="/v1", tags=["v1"])
