"""
This is a Test Module for testing Functions in translator.py
The Following functions are imported english_to_french and
french_to_english and tested for expected output.
"""
import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """
    This is a TestClass for translator.py module
    """
    def test_english_to_french(self):
        """
        This is Test function for english_to_french function
        2 test case inputs are defined here 'Null' and 'Hello'
        """
        self.assertEqual(english_to_french('Null'),'Null')
        self.assertEqual(english_to_french('Hello'),'Bonjour')

    def test_french_to_english(self):
        """
        This is Test function for french_to_english function
        2 test case inputs are defined here 'Null' and 'Hello'
        """
        self.assertEqual(french_to_english('Null'),'Null')
        self.assertEqual(french_to_english('Bonjour'),'Hello')

if __name__ == '__main__':
    unittest.main()
