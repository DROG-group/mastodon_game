# This service acts as an intermediary between the MentorBot model and the rest of the application. 
# It contains methods that handle the business logic related to the mentor bot, such as processing 
# user input, interacting with the database, and invoking the appropriate commands.

from app.models import MentorBot, Command
from app.models.database import SessionLocal

class MentorBotService:
    
    @staticmethod
    def process_command(user_id, command_text):
        """
        Process a command from a user and return the response.
        """
        # Create a new session
        session = SessionLocal()

        # Check if the user has a mentor bot instance
        mentor_bot = session.query(MentorBot).filter_by(user_id=user_id).first()

        # If not, create one
        if not mentor_bot:
            mentor_bot = MentorBot(user_id=user_id)
            session.add(mentor_bot)
            session.commit()

        # Handle the command using the Command class
        response = Command.handle_command(command_text, user_id)

        # Update the last_command and timestamp for the mentor bot
        mentor_bot.last_command = command_text
        session.commit()

        # Close the session
        session.close()

        return response

    # Additional methods related to the mentor bot can be added here, such as:
    # - Retrieving user statistics
    # - Managing challenges and rewards
    # - Handling feedback and hints
