class FizzBuzz:

    def fizzbuzz(self, number):
        if number < 0:
            raise ValueError("Please input a positive integer!")

        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        if number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        return number
