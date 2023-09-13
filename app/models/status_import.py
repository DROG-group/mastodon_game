# Defines the Status model for storing imported status updates from CSV files.
# Represents individual status updates with attributes like timestamp, username, text, and interaction type.

from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class Status(Base):
    __tablename__ = "statuses"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, index=True)  # Timestamp when the status was created
    updated_at = Column(DateTime, index=True)  # Timestamp when the status was last updated
    account_username = Column(String, index=True)  # Username of the account that posted the status
    text = Column(String)  # Content of the status
    interaction_type = Column(String)  # Type of interaction (e.g., post, reply, reblog)
    in_reply_to_id = Column(Integer)  # ID of the status this status is replying to, if any
    reblog_of_id = Column(Integer)  # ID of the status this status is reblogging, if any
    media_attachment_ids = Column(String)  # Comma-separated list of media attachment IDs, if any
    visibility = Column(String)  # Visibility setting of the status (e.g., public, private, unlisted)
