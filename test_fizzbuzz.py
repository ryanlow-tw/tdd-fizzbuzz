import unittest
from fizzbuzz import FizzBuzz


class FizzBuzzTest(unittest.TestCase):

    def test_should_return_fizzbuzz_if_number_is_0(self):
        result = FizzBuzz().fizzbuzz(0)
        self.assertEqual("FizzBuzz", result)

    def test_should_return_same_number_if_not_multiple_of_3_and_5_if_num_is_4(self):
        result = FizzBuzz().fizzbuzz(4)
        self.assertEqual(4, result)

    def test_should_return_fizz_if_num_is_multiple_of_3(self):
        result = FizzBuzz().fizzbuzz(3)
        self.assertEqual("Fizz", result)

    def test_should_return_buzz_if_num_is_multiple_of_5(self):
        result = FizzBuzz().fizzbuzz(5)
        self.assertEqual("Buzz", result)

    def test_should_return_fizzbuzz_if_num_is_multiple_of_3_and_5(self):
        result = FizzBuzz().fizzbuzz(15)
        self.assertEqual("FizzBuzz", result)

    def test_should_raise_value_error_if_input_is_not_positive_integer(self):

        with self.assertRaises(ValueError) as cm:
            FizzBuzz().fizzbuzz(-4)
        the_exception = cm.exception
        self.assertEqual(f"{the_exception}", "Please input a positive integer!")

    def test_should_raise_type_error_if_input_is_string(self):
        with self.assertRaises(TypeError):
            FizzBuzz().fizzbuzz("asd")

    def test_should_raise_type_error_if_input_is_float(self):
        with self.assertRaises(TypeError):
            FizzBuzz().fizzbuzz(3.14)

    def test_should_return_all_values_from_1_to_input_in_a_concatenated_string(self):
        result = FizzBuzz().fizzbuzz_loop(5)
        self.assertEqual("1 2 Fizz 4 Buzz", result)

    def test_fizzbuzz_loop_should_raise_type_error_if_input_is_float(self):
        with self.assertRaises(TypeError):
            FizzBuzz().fizzbuzz(3.14)

    def test_fizzbuzz_loop_should_raise_type_error_if_input_is_negative_int(self):
        with self.assertRaises(ValueError):
            FizzBuzz().fizzbuzz(-4)
