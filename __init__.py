# This file initializes the `mastodon_game` directory as a Python package.
# It can also be used to set up global configurations, initialize resources, or set up logging.

# Import necessary modules or packages
import os
from dotenv import load_dotenv

# Load the .env file for environment variables
load_dotenv()

# Global configurations or initializations can go here
# For example, setting up a logger for the entire application:
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Any other global setup can be done here
