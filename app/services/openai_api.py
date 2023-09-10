# This is a wrapper around the OpenAI API. It contains functions to interact with OpenAI's GPT models, 
# generating content based on prompts, etc. Like the Mastodon API wrapper, it abstracts the API calls 
# and provides a more Pythonic interface.

import openai
from mastodon_game.config import current_config

# Set the OpenAI API key
openai.api_key = current_config.OPENAI_API_KEY

def generate_content(prompt):
    response = openai.Completion.create(
      model="gpt-3.5-turbo",
      prompt=prompt,
      max_tokens=150
    )
    return response.choices[0].text.strip()