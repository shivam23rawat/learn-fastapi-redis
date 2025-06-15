"""Centralized logger configuration for the FastAPI application."""

import logging
import sys
from logging import Logger

from src.config import settings
from src.context import get_correlation_id, get_process_time, get_request_id

LOG_FORMAT = (
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s | "
    "process_time_ms=%(process_time_ms)s | "
    "request_id=%(request_id)s | "
    "correlation_id=%(correlation_id)s"
)


class RequestContextFilter(logging.Filter):
    """Inject request_id, correlation_id, and process_time into log records."""

    def filter(self, record: logging.LogRecord) -> bool:
        """Inject request, correlation IDs, and process_time if not present."""
        record.request_id = getattr(record, "request_id", get_request_id())
        record.correlation_id = getattr(
            record,
            "correlation_id",
            get_correlation_id(),
        )
        record.process_time_ms = getattr(
            record,
            "process_time_ms",
            get_process_time(),
        )
        return True


def get_logger(name: str = "app") -> Logger:
    """Get a configured logger instance with context filter."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(LOG_FORMAT)
        handler.setFormatter(formatter)
        handler.addFilter(RequestContextFilter())
        logger.addHandler(handler)
        # Set log level from environment/config
        log_level = settings.log_level.upper()
        logger.setLevel(getattr(logging, log_level, logging.INFO))
    return logger
