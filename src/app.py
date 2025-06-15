r"""Create the FastAPI app instance using Factory Method.

Usage
-----
Run the app.py file from the root of the repository using
`fastapi run .\src\app.py`
"""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src._client.post import PostServiceClient
from src._database.redis import redis_client
from src.api.v1.router import router as v1_router
from src.logger import get_logger
from src.middleware.rate_limit import RateLimitMiddleware
from src.middleware.request import RequestLoggingMiddleware


def create_app() -> FastAPI:
    """Create and configure an instance of the FastAPI application."""
    logger = get_logger("app")
    logger.info("Creating FastAPI application instance.")

    @asynccontextmanager
    async def lifespan(_app: FastAPI) -> AsyncGenerator[None]:
        logger.info("Application startup: lifespan context entered.")
        yield
        logger.info("Application shutdown: closing HTTP and Redis clients.")
        await PostServiceClient().close()
        await redis_client.client.aclose()

    application = FastAPI(
        title="FastAPI Redis Integration Demo",
        description=(
            "This app demonstrates the integration of FastAPI with Redis"
        ),
        version="0.1.0",
        lifespan=lifespan,
    )
    logger.info("FastAPI app created. Adding middleware and routers.")
    application.add_middleware(RequestLoggingMiddleware)
    application.add_middleware(RateLimitMiddleware)
    application.include_router(v1_router)
    return application


app = create_app()
