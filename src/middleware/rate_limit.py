"""Rate Limit Middleware for Starlette Applications."""

from collections.abc import Awaitable, Callable

from fastapi.responses import JSONResponse
from starlette import status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp

from src._database.redis import redis_client
from src.logger import get_logger

logger = get_logger("rate_limit")


class RateLimitMiddleware(BaseHTTPMiddleware):
    """Middleware to limit the number of requests from a single IP address."""

    def __init__(
        self,
        app: ASGIApp,
        max_requests: int = 10,
        window_seconds: int = 60,
    ) -> None:
        """Initialize the RateLimitMiddleware."""
        super().__init__(app)
        self._max_requests = max_requests
        self._window_seconds = window_seconds
        self._redis = redis_client

    async def dispatch(
        self,
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ) -> Response:
        """Check the request rate limit and process the request."""
        client_ip = request.client.host
        key = f"rate_limit:{client_ip}"
        current = await self._redis.get(key)
        if current is None:
            await self._redis.set(key, 1, ex=self._window_seconds)
        elif int(current) < self._max_requests:
            await self._redis.incr(key)
        else:
            logger.warning(
                "Rate limit exceeded for IP %s.",
                client_ip,
            )
            return JSONResponse(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                content={
                    "detail": (
                        "Too Many Requests. You have to wait "
                        f"{self._window_seconds} seconds before making "
                        "another request now."
                    ),
                },
            )
        return await call_next(request)
