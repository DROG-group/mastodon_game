# This module defines the Slash Command model, 
# representing the various slash commands that bots 
# and users can execute within the game.

class Command:
    # Dictionary of commands and their corresponding methods
    commands = {
        "/start": "start",
        "/help": "help",
        "/leaderboard": "leaderboard",
        "/hints": "hints",
        "/profile": "profile",
        "/feedback": "feedback"
    }

    @classmethod
    def handle_command(cls, command, user_id):
        # Check if the command exists in the dictionary
        if command in cls.commands:
            # Call the corresponding method and return its response
            method_name = cls.commands[command]
            method = getattr(cls, method_name)
            return method(user_id)
        else:
            return "Unknown command. Type /help for a list of available commands."

    @staticmethod
    def start(user_id):
        return f"Welcome, {user_id}! This is the Mastodon Game. Your objective is..."

    @staticmethod
    def help(user_id):
        help_text = """
        Here are the available commands:
        /start - Start the game and get an introduction.
        /leaderboard - See the top players.
        /hints - Get hints for challenges.
        /profile - View your game profile.
        /feedback - Provide feedback or report issues.
        """
        return help_text

    @staticmethod
    def leaderboard(user_id):
        return "Top players: ..."

    @staticmethod
    def hints(user_id):
        return "Here's a hint for your current challenge..."

    @staticmethod
    def profile(user_id):
        return f"{user_id}'s profile: ..."

    @staticmethod
    def feedback(user_id):
        return "Thank you for your feedback! We'll look into it."
