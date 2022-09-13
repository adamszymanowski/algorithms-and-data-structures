import unittest
from book.Roughgarden.multiplication import *

# helpers
class TestsForNumberOfDigits(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(number_of_digits(0), 1)
        self.assertEqual(number_of_digits(20), 2)
        self.assertEqual(number_of_digits(321), 3)
        self.assertEqual(number_of_digits(4321), 4)
        self.assertEqual(number_of_digits(54321), 5)


class TestsForIsPowerOf2(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_power_of_2(1))
        self.assertTrue(is_power_of_2(2))
        self.assertTrue(is_power_of_2(4))
        self.assertTrue(is_power_of_2(8))
        self.assertTrue(is_power_of_2(16))
        
    def test_false(self):
        self.assertFalse(is_power_of_2(3))
        self.assertFalse(is_power_of_2(5))


class TestsForHalves(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(halves(78), (7, 8))
        self.assertEqual(halves(1122), (11, 22))
        self.assertEqual(halves(10012002), (1001, 2002))
        self.assertEqual(halves(1234_1234_5678_5678), (1234_1234, 5678_5678))


class TestsForErrorCheckAndGetNumberOfDigits(unittest.TestCase):
    def test_input_error(self):
        self.assertRaises(InputError, error_check_and_get_number_of_digits, 321, 21)
        self.assertRaises(InputError, error_check_and_get_number_of_digits, -321, 321)
        self.assertRaises(InputError, error_check_and_get_number_of_digits, 107, -767)
        self.assertRaises(InputError, error_check_and_get_number_of_digits, -555, -767)
        
    def test_assumption_error(self):
        self.assertRaises(AssumptionError, error_check_and_get_number_of_digits, 787, 101)
        
# algorithms
class TestsForRecursiveIntegerMultiplication(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(recursive_integer_multiplication(5,5), 5*5)
        self.assertEqual(recursive_integer_multiplication(20, 20), 20*20)
        self.assertEqual(recursive_integer_multiplication(3418, 1024), 3418*1024)

        
class TestsForKaratsuba(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(karatsuba(20, 20), 20*20)
        self.assertEqual(karatsuba(2048, 4096), 2048*4096)
        self.assertEqual(karatsuba(8765_4321, 1234_5678), 8765_4321*1234_5678)