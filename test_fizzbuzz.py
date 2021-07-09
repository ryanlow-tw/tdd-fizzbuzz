import unittest
from fizzbuzz import FizzBuzz


class FizzBuzzTest(unittest.TestCase):

    def test_should_return_same_number_if_not_multiple_of_3_and_5_if_num_is_0(self):
        result = FizzBuzz().fizzbuzz(0)
        self.assertEqual("Fizz", result)

    def test_should_return_same_number_if_not_multiple_of_3_and_5_if_num_is_4(self):
        result = FizzBuzz().fizzbuzz(4)
        self.assertEqual(4, result)

    def test_should_return_fizz_if_num_is_multiple_of_3(self):
        result = FizzBuzz().fizzbuzz(3)
        self.assertEqual("Fizz", result)