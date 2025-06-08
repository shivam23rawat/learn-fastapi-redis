"""Provide a generic asynchronous HTTP client using httpx.

This module defines an asynchronous HTTP client for GET and POST requests.
"""

from typing import Any

import httpx

from src.logger import get_logger


class HttpClient:
    """A generic HTTP client for async GET and POST requests."""

    def __init__(self, base_url: str) -> None:
        self.logger = get_logger("HttpClient")
        self.logger.debug(
            "Initializing HttpClient with base_url: %s",
            base_url,
        )
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
        self.logger.debug(
            "Sending GET request to %s with params: %s",
            endpoint,
            params,
        )
        response = await self.client.get(endpoint, params=params)
        response.raise_for_status()
        self.logger.info(
            "Received response for GET %s with status %d",
            endpoint,
            response.status_code,
        )
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
        self.logger.debug(
            "Sending POST request to %s with data: %s",
            endpoint,
            data,
        )
        response = await self.client.post(endpoint, json=data)
        response.raise_for_status()
        self.logger.info(
            "Received response for POST %s with status %d",
            endpoint,
            response.status_code,
        )
        return response.json()

    async def close(self) -> None:
        """Close the AsyncClient session."""
        self.logger.debug("Closing HttpClient session.")
        await self.client.aclose()
