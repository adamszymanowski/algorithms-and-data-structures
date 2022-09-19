import unittest
from book.Roughgarden.inversions import *

class TestsForBruteForceCountInversions(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(brute_force_count_inversions([]), 0)
        self.assertEqual(brute_force_count_inversions([1,2,3]), 0)
        self.assertEqual(brute_force_count_inversions([6,5,4,3,2,1]), 15)
        self.assertEqual(brute_force_count_inversions([17,5,12,4,1,9,3,8]), 19)
        self.assertEqual(brute_force_count_inversions([1,3,5,2,4,6]), 3) # book says there's should be two, but it's 3!
