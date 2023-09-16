# npc.py
# This module defines the NPC model, representing automated users in the game, 
# including their attributes and basic behaviors.

class NPC:
    def __init__(self, username, avatar, bio):
        self.username = username
        self.avatar = avatar
        self.bio = bio
        self.followers = []  # List of users or bots following this bot
        self.following = []  # List of users or bots this bot is following
        self.score = 0  # Score or points associated with the bot's performance or actions

    def toot(self, message):
        """Basic behavior to post a message or status update."""
        # This might just update an internal state or log the action
        pass

    def follow(self, user):
        """Basic behavior to follow another user or bot."""
        if user not in self.following:
            self.following.append(user)

    def unfollow(self, user):
        """Basic behavior to unfollow a user or bot."""
        if user in self.following:
            self.following.remove(user)

    def receive_follow(self, user):
        """Add a user or bot to the followers list."""
        if user not in self.followers:
            self.followers.append(user)

    def update_score(self, points):
        """Update the bot's score based on actions or interactions."""
        self.score += points

    def display_profile(self):
        """Display the bot's profile information."""
        return {
            "username": self.username,
            "avatar": self.avatar,
            "bio": self.bio,
            "score": self.score,
            "followers": len(self.followers),
            "following": len(self.following)
        }
