"""
Sample router file
"""

from fastapi import APIRouter

from src.services.sample import SampleService

router = APIRouter(prefix="/sample", tags=["sample"])


@router.get("/")
async def sample_api():
    """
    Handles the sample API endpoint.

    Returns
    -------
    dict
        The result from the sample_method of SampleService.
    """
    sample_service = SampleService()
    return sample_service.sample_method()
