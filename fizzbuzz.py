class FizzBuzz:

    def fizzbuzz(self, number):
        if type(number) is not int:
            raise TypeError
        elif number < 0:
            raise ValueError("Please input a positive integer!")
        elif number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        return number

    def fizzbuzz_loop(self, number):
        result = ""
        for i in range(1, number + 1):
            fizzbuzz = self.fizzbuzz(i)

            result += (str(fizzbuzz) + " ")

        return result.strip()