# This module contains miscellaneous helper functions 
# that can be used in various parts of the application. 
# These functions can range from data processing to formatting and more.

def format_username(username):
    """Format the username to meet certain criteria."""
    return username.lower().replace(" ", "_")

def calculate_score(points, bonuses):
    """Calculate the final score based on points and bonuses."""
    return points + sum(bonuses)

