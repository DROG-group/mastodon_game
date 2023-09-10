# This file initializes the `tests` directory as a Python package. 
# It can also be used to set up any common test fixtures or configurations.

import unittest

# This is a common setup that will be executed before any test in this package
def setUpModule():
    print("Setting up the test module...")

# This is a common teardown that will be executed after all tests in this package are done
def tearDownModule():
    print("Tearing down the test module...")


# Mock data that can be used across multiple tests
MOCK_USER_DATA = {
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "securepassword"
}