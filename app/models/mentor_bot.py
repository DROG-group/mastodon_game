class MentorBot:
    def __init__(self):
        # Define a dictionary of commands and their corresponding methods
        self.commands = {
            "/start": self.start,
            "/help": self.help,
            "/challenges": self.challenges,
            "/rewards": self.rewards,
            "/leaderboard": self.leaderboard,
            "/hints": self.hints,
            "/profile": self.profile,
            "/feedback": self.feedback
        }

    def handle_command(self, command, user_id):
        # Check if the command exists in the dictionary
        if command in self.commands:
            # Call the corresponding method and return its response
            return self.commands[command](user_id)
        else:
            return "Unknown command. Type /help for a list of available commands."

    def start(self, user_id):
        return f"Welcome, {user_id}! This is the Mastodon Game. Your objective is to..."

    def help(self, user_id):
        help_text = """
        Here are the available commands:
        /start - Start the game and get an introduction.
        /challenges - View available challenges.
        /rewards - Check out the rewards you can earn.
        /leaderboard - See the top players.
        /hints - Get hints for challenges.
        /profile - View your game profile.
        /feedback - Provide feedback or report issues.
        """
        return help_text

    def challenges(self, user_id):
        # Logic to fetch and display challenges
        return "Here are the challenges..."

    def rewards(self, user_id):
        # Logic to fetch and display rewards
        return "Here are the rewards you can earn..."

    def leaderboard(self, user_id):
        # Logic to fetch and display the leaderboard
        return "Top players: ..."

    def hints(self, user_id):
        # Logic to provide hints for challenges
        return "Here's a hint for your current challenge..."

    def profile(self, user_id):
        # Logic to fetch and display the user's profile
        return f"{user_id}'s profile: ..."

    def feedback(self, user_id):
        # Logic to handle feedback
        return "Thank you for your feedback! We'll look into it."
