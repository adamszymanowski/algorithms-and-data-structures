import unittest
from book.Roughgarden.multiplication import *

class TestsForMultiplication(unittest.TestCase):

    def test_output_two(self):
        self.assertEqual(output_two(), 2)