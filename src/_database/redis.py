"""Provide an asynchronous interface for interacting with a Redis database.

Using the AsyncRedisClient class, you can perform basic get/set operations
asynchronously.

Classes:
    AsyncRedisClient: Asynchronous Redis client for basic get/set operations.
"""

import json
from datetime import timedelta

from redis.asyncio import Redis

from src.logger import get_logger


class AsyncRedisClient:
    """Async interface for interacting with a Redis database."""

    def __init__(
        self,
        host: str = "localhost",
        port: int = 6379,
        db: int = 0,
    ) -> None:
        self.logger = get_logger("AsyncRedisClient")
        self.logger.debug(
            "Connecting to Redis at %s:%d, db=%d",
            host,
            port,
            db,
        )
        self.client = Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=True,
        )

    async def set(
        self,
        key: str,
        value: str | list | dict,
        ex: timedelta = timedelta(minutes=5),
    ) -> bool:
        self.logger.debug(
            "Setting key '%s' in Redis with expiry %s.",
            key,
            ex,
        )
        serialized_value = json.dumps(value)
        return await self.client.set(
            name=key,
            value=serialized_value,
            ex=ex,
        )

    async def get(self, key: str) -> str | None:
        self.logger.debug("Getting key '%s' from Redis.", key)
        serialized_value = await self.client.get(key)
        if serialized_value is not None:
            self.logger.debug("Cache hit for key '%s'.", key)
            return json.loads(serialized_value)
        self.logger.debug("Cache miss for key '%s'.", key)
        return None


# Singleton instance for use throughout the app
redis_client = AsyncRedisClient(host="localhost", port=6379, db=0)
