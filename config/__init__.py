import os

# Determine the environment (default to development if not specified)
env = os.environ.get('MASTODON_GAME_ENV', 'development').capitalize()

# Dynamically import the configuration based on the environment
current_config_module = __import__(f"mastodon_game.config.{env.lower()}", fromlist=[env])

# Set the current configuration
current_config = getattr(current_config_module, env)

# If you want to directly access the DATABASE_CONFIG from here, you can do:
DATABASE_CONFIG = current_config.DATABASE_CONFIG