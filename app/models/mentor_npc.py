# This module defines the MentorBot model, 
# a specialized type of bot that guides and assists users throughout the game.

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from .database import Base
from .command import Command

#

class MentorBot(Base):
    __tablename__ = "mentor_bots"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    last_command = Column(String, index=True)
    timestamp = Column(DateTime(timezone=True), default=func.now())

    def handle_command(self, command, user_id):
        return Command.handle_command(command, user_id)
