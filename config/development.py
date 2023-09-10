# This file contains configurations specific to the development environment.
# It includes settings like database connection details, 
# API keys, and other development-specific configurations.

import os
from dotenv import load_dotenv
from config import development

# Load the .env file
load_dotenv()

# Fetch database credentials
DB_NAME = os.getenv("DB_NAME", default=development.DB_NAME)
DB_USER = os.getenv("DB_USER", default=development.DB_USER)
DB_PASSWORD = os.getenv("DB_PASSWORD", default=development.DB_PASSWORD)
DB_HOST = os.getenv("DB_HOST", default=development.DB_HOST)

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