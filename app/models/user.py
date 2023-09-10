# This module defines the User model, representing human players or participants in the game, 
# including their attributes, scores, and statuses. 

from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    # Add other attributes and methods for the user