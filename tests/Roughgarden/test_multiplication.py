import unittest
from book.Roughgarden.multiplication import *

class TestsForNumberOfDigits(unittest.TestCase):

    def test_2_digits(self):
        self.assertEqual(number_of_digits(21), 2)

    def test_3_digits(self):
        self.assertEqual(number_of_digits(321), 3)

    def test_4_digits(self):
        self.assertEqual(number_of_digits(4321), 4)

    def test_5_digits(self):
        self.assertEqual(number_of_digits(54321), 5)


class TestsForIsPowerOf2(unittest.TestCase):

    def test1(self):
        self.assertTrue(is_power_of_2(1))
    
    def test2(self):
        self.assertTrue(is_power_of_2(2))

    def test3(self):
        self.assertFalse(is_power_of_2(3))

    def test4(self):
        self.assertTrue(is_power_of_2(4))

    def test5(self):
        self.assertFalse(is_power_of_2(5))

    def test8(self):
        self.assertTrue(is_power_of_2(8))

    def test16(self):
        self.assertTrue(is_power_of_2(16))


class TestsForHalves(unittest.TestCase):

    def test2(self):
        self.assertEqual(halves(78), (7, 8))

    def test4(self):
        self.assertEqual(halves(1122), (11, 22))