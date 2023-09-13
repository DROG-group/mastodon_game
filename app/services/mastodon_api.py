# This is a wrapper around the Mastodon API. It abstracts the API calls 
# and provides a more Pythonic interface for the rest of the application, 
# while also allowing direct access to any methods not explicitly defined in this wrapper.

from mastodon import Mastodon
from config import current_config

class MastodonServiceWrapper:
    def __init__(self):
        self.mastodon = Mastodon(
            access_token=current_config.MASTODON_ACCESS_TOKEN,
            api_base_url=current_config.MASTODON_API_BASE_URL
        )

    def post_toot(self, content):
        """Custom method to post a toot on Mastodon."""
        return self.mastodon.toot(content)

    # ... any other custom methods ...

    def __getattr__(self, attr):
        """If the method isn't defined in this wrapper, try to call it on the underlying Mastodon object."""
        return getattr(self.mastodon, attr)

# Create an instance of the wrapper for use throughout the application
mastodon_api = MastodonServiceWrapper()

