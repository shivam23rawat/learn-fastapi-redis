"""Provide a generic asynchronous HTTP client using httpx.

This module defines an asynchronous HTTP client for GET and POST requests.
"""

from typing import Any

import httpx


class HttpClient:
    """A generic HTTP client for async GET and POST requests."""

    def __init__(self, base_url: str) -> None:
        """Initialize the AsyncClient instance."""
        self.client = httpx.AsyncClient(base_url=base_url)

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
