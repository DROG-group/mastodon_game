from mastodon import Mastodon
from mastodon_game.config import current_config

# Create a Mastodon API client instance
mastodon = Mastodon(
    access_token=current_config.MASTODON_ACCESS_TOKEN,
    api_base_url=current_config.MASTODON_API_BASE_URL
)

def post_toot(content):
    """Post a toot on Mastodon."""
    return mastodon.toot(content)