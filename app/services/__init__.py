"""
app/services/__init__.py

This module initializes the services package, providing direct access to various services used throughout the application.
These services handle distinct functionalities, from game mechanics to external API integrations, ensuring a modular and maintainable codebase.

By importing specific service classes here, they can be directly accessed from other modules in the application without referring to their specific files.

Available Services:
    - GameLogicService: Manages core game logic and mechanics.
    - MastodonAPIService: Handles interactions with the Mastodon API.
    - MentorBotService: Manages functionalities and behaviors of the mentor bot.
    - MentorService: Manages mentor-related operations, such as assigning and retrieving mentors.
    - OpenAIApiService: A wrapper around the OpenAI API, streamlining interactions.
    - SurveyBotService: Manages functionalities and behaviors of the survey bot.
    - BotService: Manages the general bot functionalities in the application.
    - EventService: Manages and processes various in-game events.
    - StatusImportService: Handles the importation of status updates from CSV files.
    - UserService: Provides services and operations related to the User model.
    - WorldService: Manages the game world, including its generation and properties.
"""

from .game_logic import GameLogicService
from .mastodon_api import MastodonAPIService
from .mentor_npc_service import MentorBotService
from .mentor_service import MentorService
from .openai_api import OpenAIApiService
from .survey_npc_service import SurveyBotService
from .npc_service import BotService
from .event_service import EventService
from .status_import_service import StatusImportService
from .user_service import UserService
from .world_service import WorldService
