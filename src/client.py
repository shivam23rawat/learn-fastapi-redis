"""HTTP client module using httpx.AsyncClient with singleton pattern."""

from typing import Any, Optional

import httpx


class HttpClient:
    """A singleton HTTP client for async GET and POST requests.

    Implements the singleton pattern for shared usage.
    """

    _instance: Optional["HttpClient"] = None

    def __new__(cls) -> "HttpClient":
        """Create or return the singleton instance."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = httpx.AsyncClient()
        return cls._instance

    def __init__(self) -> None:
        """Initialize the AsyncClient instance."""
        self.client = httpx.AsyncClient()

    async def get(
        self,
        endpoint: str,
        params: dict[str, object] | None = None,
    ) -> dict[str, object]:
        """Send an asynchronous GET request.

        Args:
            endpoint (str): The URL endpoint.
            params (Optional[Dict[str, object]]): Query parameters.

        Returns:
            dict[str, object]: The JSON response.

        """
        response = await self.client.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()

    async def post(
        self,
        endpoint: str,
        data: dict[str, Any] | None = None,
    ) -> dict[str, object]:
        """Send an asynchronous POST request.

        Args:
            endpoint (str): The URL endpoint.
            data (Optional[Dict[str, Any]]): Data to send as JSON.

        Returns:
            dict[str, object]: The JSON response.

        """
        response = await self.client.post(endpoint, json=data)
        response.raise_for_status()
        return response.json()

    async def close(self) -> None:
        """Close the AsyncClient session."""
        await self.client.aclose()
