"""Provide a singleton Redis client for interacting with a Redis database.

Includes methods to set and get values from the Redis database.
"""

import redis


class RedisClient:
    """A singleton Redis client for interacting with a Redis database.

    Parameters
    ----------
    host : str, optional
        The hostname of the Redis server (default is "localhost").
    port : int, optional
        The port number of the Redis server (default is 6379).
    db : int, optional
        The database number to connect to (default is 0).

    Attributes
    ----------
    client : redis.StrictRedis
        The Redis client instance.

    Methods
    -------
    set(key, value)
        Set a value in the Redis database.
    get(key)
        Get a value from the Redis database.

    """

    def __new__(cls) -> object:
        """Ensure that only one instance of RedisClient is created.

        Returns
        -------
        RedisClient
            The singleton instance of RedisClient.

        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(
        self,
        host: str = "localhost",
        port: int = 6379,
        db: int = 0,
    ) -> None:
        """Initialize the Redis client.

        Parameters
        ----------
        host : str, optional
            The hostname of the Redis server (default is "localhost").
        port : int, optional
            The port number of the Redis server (default is 6379).
        db : int, optional
            The database number to connect to (default is 0).

        """
        if not hasattr(self, "client"):
            self.client = redis.StrictRedis(host=host, port=port, db=db)

    def set(self, key: str, value: str) -> bool:
        """Set a value in the Redis database.

        Parameters
        ----------
        key : str
            The key under which the value is stored.
        value : str
            The value to store.

        Returns
        -------
        bool
            True if the operation was successful, False otherwise.

        """
        return self.client.set(key, value)

    def get(self, key: str) -> bytes:
        """Get a value from the Redis database.

        Parameters
        ----------
        key : str
            The key of the value to retrieve.

        Returns
        -------
        bytes
            The value stored in the Redis database, or None if the key does
            not exist.

        """
        return self.client.get(key)


# Use like a singleton so initialization is done only once and in the module.
redis_client = RedisClient()
