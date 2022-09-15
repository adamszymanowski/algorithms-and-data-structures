import unittest
from book.Roughgarden.four_examples import *

class TestsForSearchingOneArray(unittest.TestCase):
    def test_true(self):
        self.assertTrue(searching_one_array([1,2,3], 3))
        self.assertTrue(searching_one_array([-3,-2,11,0,1,1,2,35], 0))

    def test_false(self):
        self.assertFalse(searching_one_array([], 7))
        self.assertFalse(searching_one_array([1,2,3], 4))


class TestCasesForSearchingTwoArrays(unittest.TestCase):
    def test_true(self):
        self.assertTrue(searching_two_arrays([3,0,0], [1,2,1], 3))
        self.assertTrue(searching_two_arrays([-1,0,1], [0,-1,-2], 0))
        self.assertTrue(searching_two_arrays([-17, 17], [17, 27], -17))

    def test_false(self):
        self.assertFalse(searching_two_arrays([], [], 127))
        self.assertFalse(searching_two_arrays([10, 24, 55], [67, 81, 18], 11))
        self.assertFalse(searching_two_arrays([-1,-2,-3], [0, 1, 2], 7))


class TestCasesForCheckCommonElement(unittest.TestCase):
    def test_true(self):
        self.assertTrue(check_for_common_element([0,1,2], [-2,-1,0]))
        self.assertTrue(check_for_common_element([-3,-5,-7], [3, 1, -3]))

    def test_false(self):
        self.assertFalse(check_for_common_element([], []))
        self.assertFalse(check_for_common_element([1,1], [0,0]))


class TestCasesForCheckDuplicates(unittest.TestCase):
    def test_true(self):
        self.assertTrue(check_for_duplicates([1,1,1]))
        self.assertTrue(check_for_duplicates([-2,-1,-1,0,0]))

    def test_false(self):
        self.assertFalse([])
        self.assertFalse(check_for_duplicates([1,2,3]))
        self.assertFalse(check_for_duplicates([-3,-2,-1,0,1,2,3]))
        self.assertFalse(check_for_duplicates([17, 23, 59, 107]))