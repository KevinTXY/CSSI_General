# This is an empty testfile. Use this template to add your tests.

import sys
import unittest
from balance_checker import is_string_balanced

class TestParentheses(unittest.TestCase):

    def setUp(self):
        pass

    # This test fails, ("False" is obviously not "True")
    # To add your testcases, define new functions
    # like this one (function name should start with "test_").
    #
    # In each test, call your function like you would normally do,
    # using "is_string_balanced()", and use self.assertTrue() and
    # self.assertFalse() to verify that the returned value of your
    # function matches your expectations.
    def test_case_1(self):
        message = "(())"
        self.assertTrue(is_string_balanced(message))

    def test_case_2(self):
        message = "()(()())"
        self.assertTrue(is_string_balanced(message))

    def test_case_3(self):
        message = "())"
        self.assertFalse(is_string_balanced(message))

    def test_case_4(self):
        message = "))"
        self.assertFalse(is_string_balanced(message))


if __name__ == '__main__':
    unittest.main()
balance_checker_test_template.py
