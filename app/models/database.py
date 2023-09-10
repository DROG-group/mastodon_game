# This module sets up the database connection and provides utilities 
# for database operations.

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .user import Base
from config import development

# Load environment variables
load_dotenv()

# Fetch database credentials
DB_NAME = os.getenv("DB_NAME", default=development.DB_NAME)
DB_USER = os.getenv("DB_USER", default=development.DB_USER)
DB_PASSWORD = os.getenv("DB_PASSWORD", default=development.DB_PASSWORD)
DB_HOST = os.getenv("DB_HOST", default=development.DB_HOST)

# Construct the DATABASE_URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"

# Initialize database engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    """Initialize the database."""
    Base.metadata.create_all(bind=engine)