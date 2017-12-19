import sys
import unittest
from up_and_down_array import find_max_idx

class TestUpAndDownArray(unittest.TestCase):

    def setUp(self):
        pass

    def test_case_one_element(self):
        self.assertEqual(find_max_idx([1]), 0)

    def test_case_two_elements_increasing(self):
        self.assertEqual(find_max_idx([1, 2]), 1)

    def test_case_two_elements_decreasing(self):
        self.assertEqual(find_max_idx([3, 2]), 0)

    def test_case_three_elements_middle(self):
        self.assertEqual(find_max_idx([3, 5, 2]), 1)

    def test_case_general_case(self):
        self.assertEqual(find_max_idx([3, 7, 19, 25, 20, 17, 5, 4, 2, 1]), 3)

    def test_case_general_case_all_negative(self):
        self.assertEqual(find_max_idx([-20, -17, -5, -4, -2, -1, -3, -7, -19, -25]), 5)

    def test_case_sorted_increasing(self):
        self.assertEqual(find_max_idx([-20, -17, -5, -4, -2, -1]), 5)

    def test_case_sorted_decreasing(self):
        self.assertEqual(find_max_idx([-1, -2, -5, -8, -27, -134]), 0)

if __name__ == '__main__':
    unittest.main()
