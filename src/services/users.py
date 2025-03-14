"""
Service file for user-related operations
"""

from typing import List


class UserService:
    """
    Service class for user-related operations.

    Methods
    -------
    get_all_users() -> List[str]
        Returns a list of all user names.
    """

    def get_all_users(self) -> List[str]:
        """
        Returns a list of all user names.

        Returns
        -------
        List[str]
            A list containing the names of all users.

        Example
        -------
        >>> service = UserService()
        >>> service.get_all_users()
        ['user1', 'user2', 'user3']
        """
        return ["user1", "user2", "user3"]
