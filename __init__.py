"""
Initialization for the `mastodon_game` Package
----------------------------------------------

The `mastodon_game` package serves as the main entry point for the Mastodon Game application. 
This initialization file ensures that the directory is treated as a Python package and also 
handles global configurations, resource initializations, and logging setups to maintain 
consistency and ease of use throughout the application.

Modules:
    - os: Standard Python module for OS-related functionalities.
    - dotenv: Utility to load environment variables from a .env file.
    - logging: Provides mechanisms to configure and use logging within the application.

Configurations:
    - Environment Variable Loading: Extracts and loads environment variables from a .env file.
    - Logging: Sets up a global logging configuration for the application.
"""

# Standard library imports
import os
import logging

# Third-party imports
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging for the entire application
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Placeholder for any other global setups or initializations
# Examples could include database connections, cache initializations, 
# or other resources that need to be set up globally.
