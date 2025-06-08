"""Test module for Redis set/get functionality using a dummy client."""

import pytest


@pytest.mark.anyio
async def test_redis_set_get() -> None:
    """Test setting and getting a value in DummyRedis."""

    class DummyRedis:
        def __init__(self) -> None:
            self.store = {}

        async def set(self, name: str, value: str) -> bool:
            self.store[name] = value
            return True

        async def get(self, name: str) -> str | None:
            return self.store.get(name)

    client = DummyRedis()
    await client.set("foo", "bar")
    result = await client.get("foo")
    if result != "bar":
        msg = f'Expected "bar", got {result}'
        raise AssertionError(msg)
