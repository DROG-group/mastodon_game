# This file contains unit tests for utility functions and helpers used throughout the application.
# It ensures that these utility functions behave as expected in various scenarios.

import unittest
from app.utils.helpers import format_username

class TestUtils(unittest.TestCase):
    def test_format_username(self):
        result = format_username("Example User")
        self.assertEqual(result, "example_user")
