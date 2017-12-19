#s is a collection of test cases that you can use to verify your code
# before submitting. Feel free to add more tests following this template.

import sys
import unittest
from anon_notes import anon_note_checker

class TestBueller(unittest.TestCase):

    def setUp(self):
        pass

    def test_strict_inclusion(self):
        note = "This is the message for you"
        magazine = ("This magazine contains everything you need "
                    "you should find that the article is enough "
                    "for composing the message")
        self.assertTrue(anon_note_checker(magazine, note))

    def test_same_message(self):
        note = "This is the message for you"
        magazine = "This is the message for you"
        self.assertTrue(anon_note_checker(magazine, note))

    def test_inclusion(self):
        note = "This is the message for you"
        magazine = "for you This message is the"
        self.assertTrue(anon_note_checker(magazine, note))

    def test_inclusion_case_insensitive(self):
        note = "This is the message for you"
        magazine = "FOR YOU THIS MESSAGE IS THE"
        self.assertTrue(anon_note_checker(magazine, note))

    def test_failure(self):
        note = "This is the message I want to send you"
        magazine = ("send a message to you is the scope of this printed "
                    "article but it will not be enough because it does not "
                    "contain two of the needed words")
        self.assertFalse(anon_note_checker(magazine, note))

    def test_duplicate_words(self):
        note = "This message is the message that I want to send to you"
        magazine = ("This article is not enough because it contains the words "
                    "that I want to send you in a message but does not contain "
                    "two words twice")
        self.assertFalse(anon_note_checker(magazine, note))


if __name__ == '__main__':
    unittest.main()
anon_notes_test.py
