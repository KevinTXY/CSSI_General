import sys
import unittest
from cards import *

class TestBueller(unittest.TestCase):

    def setUp(self):
        self.names = ["See-Mong Tan", "Stephen Pratt", "Matthew Levine", "Eric Breck", "Riccardo Crepaldi"]
        self.function_defined()

    def function_defined(self):
        try:
            self.assert_(everyone_sign is not None)
        except NameError as e:
            self.fail("Define a function called everyone_sign")
            self.skipTest(TestBueller)

    def test_return(self):
        result = everyone_sign(["test", "test2"])
        self.assertIsInstance(result,dict,"everyone_sign should return a dictionary")

    def test_count(self):
        result = everyone_sign(self.names)
        self.assertEqual(len(result), len(self.names), "everyone_sign should have the same number of entries as the list passed in")

    def test_types(self):
        result = everyone_sign(self.names)
        self.assertIsInstance(list(result.keys())[0],str, "keys of returned dictionary ought to be strings")
        self.assertIsInstance(list(result.values())[0],str, "values of the returned dictionary ought to be strings")

    def test_signatures(self):
        result = everyone_sign(self.names)
        for key in list(result.keys()):
            for name in self.names:
                if name == key:
                    self.assertNotIn(name,result[key], "No one should sign their own name!")
                else:
                    self.assertIn(name,result[key], "Not all the friends have signed everyone's card")

if __name__ == '__main__':
    unittest.main()
