"""Context variables for request-scoped data.

This module contains all setters and getters for context variables used in the
application.
"""

import contextvars

request_id_ctx_var = contextvars.ContextVar("request_id", default="-")
correlation_id_ctx_var = contextvars.ContextVar("correlation_id", default="-")
process_time_ctx_var = contextvars.ContextVar("process_time", default="-")


def set_request_id(request_id: str) -> None:
    """Set the request ID in the context variable."""
    request_id_ctx_var.set(request_id)


def get_request_id() -> str:
    """Get the request ID from the context variable."""
    return request_id_ctx_var.get()


def set_correlation_id(correlation_id: str) -> None:
    """Set the correlation ID in the context variable."""
    correlation_id_ctx_var.set(correlation_id)


def get_correlation_id() -> str:
    """Get the correlation ID from the context variable."""
    return correlation_id_ctx_var.get()


def set_process_time(process_time: str) -> None:
    """Set the process time in the context variable."""
    process_time_ctx_var.set(process_time)


def get_process_time() -> str:
    """Get the process time from the context variable."""
    return process_time_ctx_var.get()
