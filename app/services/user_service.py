# Provides services and operations related to the User model.
# Includes CRUD operations, authentication, preferences, scoring, and more.

from app.models import User
from app.database import SessionLocal as Session  # Renaming for clarity in the service

def create_user(username):
    """Add a new user to the database."""
    session = Session()
    user = User(username=username)
    session.add(user)
    session.commit()
    return user

def get_user_by_id(user_id):
    """Retrieve user details by ID."""
    session = Session()
    return session.query(User).filter(User.id == user_id).first()

def update_username(user_id, new_username):
    """Update a user's username."""
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        user.username = new_username
        session.commit()
    return user

def delete_user(user_id):
    """Remove a user from the database."""
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()

def get_user_by_username(username):
    """Retrieve user details by username."""
    session = Session()
    return session.query(User).filter(User.username == username).first()

def authenticate_user(username, password):
    """Authenticate a user based on username and password.
    Note: This is a placeholder. In a real-world scenario, you'd use password hashing and verification.
    """
    session = Session()
    user = session.query(User).filter(User.username == username).first()
    if user and user.password == password:  # This is a simplistic check. Always hash and salt passwords!
        return True
    return False

def set_user_preference(user_id, preference_key, preference_value):
    """Set a user's preference."""
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        # Assuming the User model has a 'preferences' column that stores data in a dictionary format
        user.preferences[preference_key] = preference_value
        session.commit()

def get_user_preference(user_id, preference_key):
    """Get a user's preference."""
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    if user and preference_key in user.preferences:
        return user.preferences[preference_key]
    return None

def update_user_score(user_id, score_increment):
    """Update a user's score."""
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        # Assuming the User model has a 'score' column
        user.score += score_increment
        session.commit()

def get_leaderboard(limit=10):
    """Get the top users based on score."""
    session = Session()
    return session.query(User).order_by(User.score.desc()).limit(limit).all()

