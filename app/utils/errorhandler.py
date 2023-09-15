"""
Error Handling Utilities for Mastodon Game
------------------------------------------

This module provides functions to handle errors in a graceful manner. Instead 
of allowing the application to crash, errors are logged, and appropriate 
responses or notifications can be dispatched to the user or system administrators.

Imports:
    - setup_logging: A function from the logging module to configure the logger.
    - MastodonGameError: The base exception class for game-specific errors.

Functions:
    - handle_error: The primary error handling function that logs and handles both game-specific and unexpected errors.
    - send_alert: A function to send alerts or notifications for critical errors.
"""

from .logging import setup_logging
from .exceptions import MastodonGameError, UserNotFoundError, ConnectionError

logger = setup_logging()

def send_alert(message):
    """Send an alert or notification about a critical error."""
    # This could send an email, push notification, SMS, etc.
    # For simplicity, it's just a placeholder here.
    pass

def handle_error(e):
    """Handle and log errors."""
    if isinstance(e, MastodonGameError):
        if isinstance(e, UserNotFoundError):
            logger.warning(f"User not found: {e}")
            # Perhaps return a user-friendly message about the user not being found

        elif isinstance(e, ConnectionError):
            logger.error(f"Connectivity issue: {e}")
            # Maybe attempt a reconnect or inform the user to check their connection

        else:
            logger.error(f"Game-specific error: {e}")
            # Handle other game-specific errors, maybe return a specific message or code

    else:
        logger.critical(f"Unexpected error: {e}", exc_info=True)
        # For unexpected critical errors, we might want to send an alert
        send_alert(f"Critical error encountered: {e}")