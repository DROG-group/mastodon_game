class Event:
    def __init__(self, title, description, reward):
        self.title = title
        self.description = description
        self.reward = reward

    def trigger(self):
        # Logic to trigger the event
        pass