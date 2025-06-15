"""Test module for Redis set/get functionality using a dummy client."""

import pytest

REDIS_EXPECTED_COUNTER = 2


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

        async def incr(self, name: str) -> int:
            self.store[name] = int(self.store.get(name, 0)) + 1
            return self.store[name]

    client = DummyRedis()
    await client.set("foo", "bar")
    result = await client.get("foo")
    if result != "bar":
        pytest.fail(f"Expected 'bar', got {result}")
    await client.set("counter", "1")
    incr_result = await client.incr("counter")
    if incr_result != REDIS_EXPECTED_COUNTER:
        pytest.fail(
            f"Expected counter to be {REDIS_EXPECTED_COUNTER}, "
            f"got {incr_result}",
        )


@pytest.mark.anyio
async def test_redis_expiry_simulation() -> None:
    """Test simulating expiry logic in DummyRedis."""

    class DummyRedis:
        def __init__(self) -> None:
            self.store = {}
            self.expired = set()

        async def set(
            self,
            name: str,
            value: str,
            ex: int | None = None,
        ) -> bool:
            self.store[name] = value
            if ex:
                self.expired.add(name)
            return True

        async def get(self, name: str) -> str | None:
            if name in self.expired:
                return None
            return self.store.get(name)

    client = DummyRedis()
    await client.set("foo", "bar", ex=1)
    result = await client.get("foo")
    if result is not None:
        pytest.fail(f"Expected None due to expiry, got {result}")
