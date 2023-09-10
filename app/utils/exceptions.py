# This module defines custom exception classes that can be raised 
# throughout the application. These exceptions can be caught and handled 
# in a standardized way.

class MastodonGameError(Exception):
    """Base exception for the game."""

class UserNotFoundError(MastodonGameError):
    """Raised when a user is not found."""

# ... add more custom exceptions as needed
