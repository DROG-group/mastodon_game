# This module defines the SurveyUserResponses model, 
# capturing the answers or responses given by users to survey questions.


from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from .survey_question import SurveyQuestion

class SurveyUserResponse(Base):
    __tablename__ = 'survey_user_responses'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)  # Assuming user ID is an integer. Adjust as needed.
    question_id = Column(Integer, ForeignKey('survey_questions.id'), nullable=False)
    response = Column(Text, nullable=False)

    # Relationship to get the corresponding question for a response
    question = relationship("SurveyQuestion", back_populates="responses")

# Back-reference in the SurveyQuestion model
SurveyQuestion.responses = relationship("SurveyUserResponse", order_by=SurveyUserResponse.id, back_populates="question")
