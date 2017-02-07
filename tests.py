import unittest
from primes import prime_numbers, is_prime

class PrimeTestCase(unittest.TestCase):

    def test_input_zero(self):
        with self.assertRaises(Exception):
            prime_numbers(0)

    def test_input_one(self):
        with self.assertRaises(Exception):
            prime_numbers(1) # The function can not output between range 0, 1

    def test_is_not_negative(self):
        with self.assertRaises(ValueError):
            prime_numbers(-2)

    def test_is_an_instance_of_int(self):
        with self.assertRaises(TypeError):
            prime_numbers("string")

    def test_getting_primes_list(self):
        list_returned = prime_numbers(10)
        self.assertEqual(list_returned, [2, 3, 5, 7])

    def test_list_is_not_greater_than_n(self):
        list_returned = prime_numbers(100)
        self.assertTrue(len(list_returned) < 100)

    
    def test_each_element_is_prime(self):
        list_returned = prime_numbers(100)
        for number in list_returned:
            self.assertTrue(is_prime(number))

    def test_for_larger_numbers(self):
        list_returned = prime_numbers(1000)
        self.assertEqual(len(list_returned), 168)

    def test_prime_numbers_in_range(self):
        list_returned = prime_numbers(start=10, end=15)
        self.assertEqual(list_returned, [11, 13])

    def test_invalid_range(self):
        with self.assertRaises(ValueError):
            prime_numbers(start=15, end=4)

    def test_start_equal_end(self):
        with self.assertRaises(ValueError):
            prime_numbers(start=2, end=2)

if __name__ == '__main__':
    unittest.main()
