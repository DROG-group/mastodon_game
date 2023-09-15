"""
Logging Utility for Mastodon Game
---------------------------------

This module sets up and configures logging for the Mastodon Game application.
It ensures that logs are consistently formatted and can be written to various 
outputs such as files, databases, or external services.

The primary functionality provided by this module is encapsulated in the 
`setup_logging` function, which configures the logging settings and returns 
a logger instance for the calling module.

Modules:
    - logging: The standard Python logging module.

Functions:
    - setup_logging: Configures the logging settings and returns a logger instance.
"""

import logging

def setup_logging(level=logging.INFO):
    """
    Set up and configure logging for the Mastodon Game application.

    This function configures the logging settings using the `basicConfig` method
    from Python's built-in logging module. The resultant logs will include the 
    timestamp, module name, log level, and the actual log message.

    Parameters:
        - level (int, optional): The logging level. Defaults to logging.INFO.

    Returns:
        logging.Logger: A logger instance for the calling module.
    """
    logging.basicConfig(level=level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)
