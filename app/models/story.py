from sqlalchemy import Column, Integer, String
from .database import Base

class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    plot = Column(String, index=True)
    # Add other attributes and methods for the story