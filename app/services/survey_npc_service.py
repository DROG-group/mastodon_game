# This service manages the survey bot's functionalities. It can send survey questions to users, 
# collect and store their responses, analyze survey data, and more. It might also contain logic 
# to decide when to send surveys, how to handle incomplete surveys, etc.

from app.models.survey_question import SurveyQuestion
from app.models.survey_user_responses import SurveyUserResponse
from app.models.database import SessionLocal

class SurveyBot:
    def __init__(self):
        self.session = SessionLocal()

    def get_next_question(self, user_id):
        """
        Fetch the next survey question for the user.
        This is a simple implementation that fetches the first unanswered question for the user.
        """
        answered_question_ids = self.session.query(SurveyUserResponse.question_id).filter_by(user_id=user_id).all()
        next_question = self.session.query(SurveyQuestion).filter(~SurveyQuestion.id.in_(answered_question_ids)).first()
        return next_question

    def save_response(self, user_id, question_id, response):
        """
        Save the user's response to a survey question.
        """
        user_response = SurveyUserResponse(user_id=user_id, question_id=question_id, response=response)
        self.session.add(user_response)
        self.session.commit()

    def send_question(self, user_id):
        """
        Send the next survey question to the user.
        This is a placeholder function. In a real-world scenario, you'd integrate with Mastodon API or another messaging service.
        """
        question = self.get_next_question(user_id)
        if question:
            # Send the question to the user via Mastodon API or another messaging service
            # For now, we'll just print it
            print(f"Sending question to user {user_id}: {question.question_text}")
        else:
            print(f"No more questions for user {user_id}")

    def close(self):
        """
        Close the database session.
        """
        self.session.close()

# Example usage:
# bot = SurveyBot()
# bot.send_question(1)
# bot.save_response(1, 1, "My response")
# bot.close()
