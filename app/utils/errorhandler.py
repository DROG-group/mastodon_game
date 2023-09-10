# This module provides functions to handle errors gracefully. 
# Instead of crashing the application, errors can be logged, 
# and appropriate responses can be returned to the user or system.

from .logging import setup_logging
from .exceptions import MastodonGameError

logger = setup_logging()

def handle_error(e):
    if isinstance(e, MastodonGameError):
        logger.error(f"Game-specific error: {e}")
        # Handle game-specific errors, maybe return a specific message or code
    else:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        # Handle unexpected errors, maybe send an alert or email
