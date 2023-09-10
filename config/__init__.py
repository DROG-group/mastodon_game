# This file initializes the `config` directory as a Python package. 
# It also dynamically loads the appropriate configuration based on the environment setting.

import os
from dotenv import load_dotenv
import config  # Import the config module

# Load the .env file
load_dotenv()

# Determine the environment (default to development if not specified)
env = os.environ.get('MASTODON_GAME_ENV', 'development')

# Dynamically get the configuration based on the environment
current_config = getattr(config, env)

# Fetch database credentials
DB_NAME = os.getenv("DB_NAME", default=current_config.DB_NAME)
DB_USER = os.getenv("DB_USER", default=current_config.DB_USER)
DB_PASSWORD = os.getenv("DB_PASSWORD", default=current_config.DB_PASSWORD)
DB_HOST = os.getenv("DB_HOST", default=current_config.DB_HOST)

# Construct the DATABASE_URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"

# Database configuration
DATABASE_CONFIG = {
    'dbname': DB_NAME,
    'user': DB_USER,
    'password': DB_PASSWORD,
    'host': DB_HOST
}

# Fetch OpenAI API Key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')