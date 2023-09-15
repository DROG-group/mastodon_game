"""
Custom Exceptions for Mastodon Game
-----------------------------------

This module defines custom exception classes to handle specific error scenarios 
encountered throughout the Mastodon Game application. These custom exceptions allow 
for precise error identification, facilitating standardized error handling and 
response throughout the application.

Classes:
    - MastodonGameError: Base exception for the game.
    - UserNotFoundError: Exception for when a user is not found in the system.
    - InvalidInputError: Exception for invalid user inputs.
    - ScoreNotFoundError: Exception when a player's score is unavailable.
    - ConnectionError: Exception for connectivity issues, including problems connecting to game servers.
    - ChallengeFailedError: Exception when a player fails a game challenge.
    - DiskSpaceError: Exception for when the application encounters insufficient disk space.
    - MemoryOverflowError: Exception for when the application exhausts available memory.
    - OpenAIAPIThrottleError: Exception for when rate limits of the OpenAI API are reached.
    - MastodonAPIThrottleError: Exception for when rate limits of the Mastodon Game's API or related services are exceeded.
"""

class MastodonGameError(Exception):
    """Base exception class for all game-related errors."""

class UserNotFoundError(MastodonGameError):
    """Exception raised when a specific user is not found within the system."""

class InvalidInputError(MastodonGameError):
    """Exception raised for any invalid user inputs, such as incorrect data formats."""

class ScoreNotFoundError(MastodonGameError):
    """Exception raised when attempting to fetch a player's score, but it's unavailable."""

class ConnectionError(MastodonGameError):
    """Exception raised for any connectivity issues, especially when connecting to the game server or related services."""

class ChallengeFailedError(MastodonGameError):
    """Exception raised when a player fails to meet the criteria of a specific game challenge."""

class DiskSpaceError(MastodonGameError):
    """Exception raised when the application runs out of available disk space, affecting operations like saving or caching."""

class MemoryOverflowError(MastodonGameError):
    """Exception raised when the application exhausts its available memory resources during operations."""

class OpenAIAPIThrottleError(MastodonGameError):
    """Exception raised when the application hits the rate or quota limits for the OpenAI API."""

class MastodonAPIThrottleError(MastodonGameError):
    """Exception raised when the application exceeds the rate or quota limits for the Mastodon Game's API or affiliated services."""

# Potential space for more custom exceptions as the game evolves.
