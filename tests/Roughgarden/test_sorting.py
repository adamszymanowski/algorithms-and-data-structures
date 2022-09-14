import unittest
from book.Roughgarden.sorting import *

class TestsForMerge(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(merge([1,2], [3,4]), [1,2,3,4])
        self.assertEqual(merge([1], [4]), [1,4])

class TestsForMergeSort(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort([5]), [5])
        self.assertEqual(merge_sort([8, 6]), [6, 8])
        self.assertEqual(merge_sort([9, 1, 1, 8, 7]), [1, 1, 7, 8, 9])
        self.assertEqual(merge_sort([0, 0, -1, -2, 1]), [-2, -1, 0, 0, 1])