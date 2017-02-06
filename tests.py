import unittest
from primes import prime_numbers, is_prime

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

    def test_list_is_not_greater_than_n(self):
        list_returned = prime_numbers(100)
        self.assertTrue(len(list_returned) < 100)

    
    def test_each_element_is_prime(self):
        list_returned = prime_numbers(100)
        for number in list_returned:
            self.assertTrue(is_prime(number))

if __name__ == '__main__'
    unittest.main()
