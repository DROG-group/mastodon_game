# This module defines the Event model, representing significant occurrences 
# or actions within the game that can affect users or bots.

class Event:
    def __init__(self, title, description, reward):
        self.title = title
        self.description = description
        self.reward = reward

    def trigger(self):
        # Logic to trigger the event
        pass