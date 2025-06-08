"""Request logging middleware for FastAPI."""

import time
import uuid
from collections.abc import Callable

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from src.context import set_correlation_id, set_process_time, set_request_id
from src.logger import get_logger

logger = get_logger("request")


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Log requests with response time, request ID, and correlation ID."""

    async def dispatch(
        self,
        request: Request,
        call_next: Callable,
    ) -> Response:
        """Log request and response details including timing and IDs."""
        request_id = str(uuid.uuid4())
        correlation_id = request.headers.get(
            "x-correlation-id",
            str(uuid.uuid4()),
        )
        set_request_id(request_id)
        set_correlation_id(correlation_id)
        start_time = time.perf_counter()
        logger.debug(
            "Incoming request: %s %s | correlation_id=%s",
            request.method,
            request.url.path,
            correlation_id,
        )
        response: Response = await call_next(request)
        process_time = round((time.perf_counter() - start_time) * 1000, 2)
        set_process_time(process_time)
        http_error_status = 400
        if response.status_code >= http_error_status:
            logger.warning(
                "Request %s %s failed with status %d.",
                request.method,
                request.url.path,
                response.status_code,
            )
        else:
            logger.info(
                "%s %s - %d",
                request.method,
                request.url.path,
                response.status_code,
                extra={
                    "request_id": request_id,
                    "correlation_id": correlation_id,
                    "process_time_ms": process_time,
                },
            )
        response.headers["x-request-id"] = request_id
        response.headers["x-correlation-id"] = correlation_id
        response.headers["x-response-time-ms"] = str(process_time)
        return response
