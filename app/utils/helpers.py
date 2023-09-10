def format_username(username):
    """Format the username to meet certain criteria."""
    return username.lower().replace(" ", "_")

def calculate_score(points, bonuses):
    """Calculate the final score based on points and bonuses."""
    return points + sum(bonuses)