# This is a wrapper around the OpenAI API. It abstracts the API calls for generating content with GPT models,
# while also allowing direct access to any methods not explicitly defined in this wrapper.

import openai
from config import current_config

class OpenAIServiceWrapper:
    def __init__(self):
        # Set the OpenAI API key
        openai.api_key = current_config.OPENAI_API_KEY

    def generate_content(self, prompt, model="gpt-3.5-turbo", max_tokens=150, temperature=0.7):
        """Generate content based on a given prompt using the specified model."""
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response.choices[0].text.strip()

    def generate_avatar_with_dalle(self, entity_name, extra_prompt_text="", model="DALL-E_MODEL_NAME"):
        """
        Generate an avatar image using DALL·E via the OpenAI API.
        
        :param entity_name: The name of the entity (user/bot) for which the avatar is being generated.
        :param extra_prompt_text: Additional descriptive text to guide the avatar generation.
        :param model: The DALL·E model name.
        :return: URL of the generated avatar image.
        """
        # Construct the prompt for DALL·E
        prompt = f"Create a unique avatar for {entity_name}. {extra_prompt_text}".strip()

        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            n=1,  # Generate only one image
            size="200x200"  # Image size of 200x200px
        )
        
        # Assuming the API returns a URL to the generated image
        return response.choices[0].image_url
    def __getattr__(self, attr):
        """If the method isn't defined in this wrapper, try to call it on the underlying openai object."""
        return getattr(openai, attr)

# Create an instance of the wrapper for use throughout the application
openai_api = OpenAIServiceWrapper()
