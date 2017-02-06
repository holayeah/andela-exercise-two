import unittest
from primes import prime_numbers

class PrimeTestCase(unittest.TestCase):

    def test_input_zero(self):
        self.assertRaises(Exception):
            prime_numbers(0)

    def test_input_one(self):
        self.assertRaises(Exception):
            prime_numbers(1) # The function can not output between range 0, 1

    def test_is_not_negative(self):
        self.assertRaises(ValueError):
            prime_numbers(-2)

    def test_is_an_instance_of_int(self):
        self.assertRaises(TypeError):
            prime_numbers("string")



if __name__ == '__main__'
    unittest.main()
