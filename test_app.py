# Assignment: Unit test file for app.py
# https://flask.palletsprojects.com/en/1.1.x/quickstart/
# Date: 09/29/2022
# Author: derekYankie

from app import returnBackwardsString
from app import hello_world
import unittest

class TestApp(unittest.TestCase):
    # Unit tests defined for app.py
    def test_hello():
        response = app.test_client().get('/')
        assert response.status_code == 200
        assert response.data == b'Hello, World!'

    def test_return_backwards_string(self):
    # Test return backwards simple string
        random_string = "This is my test string"
        random_string_reversed = "gnirts tset ym si sihT"
        self.assertEqual(random_string_reversed, returnBackwardsString(random_string))

if __name__ == "__main__":
    unittest.main()