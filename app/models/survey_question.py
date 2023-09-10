# This module defines the SurveyQuestion model, 
# representing questions that are posed to users as part of surveys or quizzes.

from .database import Base
from sqlalchemy import Column, Integer, String, Text

class SurveyQuestion(Base):
    __tablename__ = 'survey_questions'

    id = Column(Integer, primary_key=True)
    question_text = Column(Text, nullable=False)
    question_type = Column(String(50), nullable=False)  # e.g. 'multiple_choice', 'open_ended'
    options = Column(Text)  # For multiple choice questions, store options as a JSON string
