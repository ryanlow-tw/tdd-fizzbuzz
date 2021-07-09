import unittest
from fizzbuzz import FizzBuzz


class FizzBuzzTest(unittest.TestCase):

    def test_should_return_same_number_if_not_multiple_of_3_and_5(self):
        result = FizzBuzz().fizzbuzz(0)
        self.assertEqual(0, result)
