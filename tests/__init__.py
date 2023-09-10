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