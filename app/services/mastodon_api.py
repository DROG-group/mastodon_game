# This is a wrapper around the Mastodon API. It contains functions to interact with Mastodon, 
# such as posting toots, reading timelines, following users, etc. It abstracts the API calls 
# and provides a more Pythonic interface for the rest of the application.

from mastodon import Mastodon
from config import current_config

# Create a Mastodon API client instance
mastodon = Mastodon(
    access_token=config.MASTODON_ACCESS_TOKEN,
    api_base_url=config.MASTODON_API_BASE_URL
)

def post_toot(content):
    """Post a toot on Mastodon."""
    return mastodon.toot(content)