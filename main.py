"""
Mastodon Game
-------------

This module serves as the entry point to the Mastodon Game. It initializes the game,
runs the primary game logic, and handles any keyboard interrupts.

Imports:
    - time: For potential delay or sleep functionality.
    - game_logic: Module containing the main logic for the game.
    - utils: Package containing utility modules like alerting, error handling, logging, etc.

Functions:
    - main: The main function responsible for initializing and starting the game.
"""

import time
from app.services import game_logic

# Importing utility modules
from app.utils import alerting
from app.utils import constants
from app.utils import errorhandler
from app.utils import exceptions
from app.utils import helpers
from app.utils import logging

def main():
    """
    Main function to initialize and run the Mastodon game.

    This function first prints an initialization message and then hands over control
    to the game logic from the `game_logic` module. Utility modules from the `utils`
    package can be used to enhance functionality, handle errors, log events, etc.
    """
    # Initialization or setup code
    logging.info("Mastodon Game Initializing...")

    # Potential use of utility functions (e.g., logging initialization)
    logging.initialize()

    # Hand over to the primary game logic
    game_logic.run()

if __name__ == "__main__":
    try:
        main()
    except exceptions.CustomGameException as e:
        # Handle custom game exceptions using the error handler utility
        errorhandler.handle(e)
    except KeyboardInterrupt:
        # Gracefully handle keyboard interrupts (e.g., Ctrl+C) using the logging utility
        logging.info("Mastodon Game Stopped by User.")
