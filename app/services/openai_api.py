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