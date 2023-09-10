class MastodonGameError(Exception):
    """Base exception for the game."""

class UserNotFoundError(MastodonGameError):
    """Raised when a user is not found."""

# ... add more custom exceptions as needed
