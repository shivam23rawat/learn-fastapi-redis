"""Post service HTTP Client."""

from typing import Optional

from src._client.http import HttpClient
from src.config import settings


class PostServiceClient(HttpClient):
    """A service-specific HTTP client with a predefined base URL."""

    _instance: Optional["PostServiceClient"] = None
    _base_url: str = settings.post_service_url

    def __new__(cls) -> "PostServiceClient":
        """Create or return the singleton instance."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            super(PostServiceClient, cls._instance).__init__(cls._base_url)
        return cls._instance

    def __init__(self) -> None:
        """Prevent reinitialization of the singleton instance."""
