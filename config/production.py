# This file contains configurations specific to the production environment.
# It includes settings like database connection details, API keys, 
# and other production-specific configurations.

import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Database configuration
DATABASE_CONFIG = {
    'dbname': os.environ.get('DB_NAME'),
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'host': os.environ.get('DB_HOST')
}

# Configuration for Mastodon API interactions
MASTODON_API_URL = "https://mastodon.example.com/api/v1/"

# OpenAI API Key
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')