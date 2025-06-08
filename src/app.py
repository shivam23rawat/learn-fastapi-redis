r"""Create the FastAPI app instance using Factory Method.

Usage
-----
Run the app.py file from the root of the repository using
`fastapi run .\src\app.py`
"""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src._client.http import HttpClient
from src._database.redis import redis_client
from src.api.v1.router import router as v1_router


def create_app() -> FastAPI:
    """Create and configure an instance of the FastAPI application.

    Returns
    -------
    application
        An instance of the FastAPI application with the specified title,
        description, and version.

    """

    @asynccontextmanager
    async def lifespan(_app: FastAPI) -> AsyncGenerator[None]:
        yield
        await HttpClient().close()
        await redis_client.client.aclose()

    application = FastAPI(
        title="FastAPI Redis Integration Demo",
        description=(
            "This app demonstrates the integration of FastAPI with Redis"
        ),
        version="0.1.0",
        lifespan=lifespan,
    )
    application.include_router(v1_router)
    return application


app = create_app()
