import unittest
from exercise2 import filter_non_primes

class TestFilterNonPrimes(unittest.TestCase):
    
    def test_filter_non_primes(self):
        
        # prime and non-prime numbers
        self.assertEqual(filter_non_primes([1, 2, 3, 4, 6]), [1, 4, 6])

        # only prime numbers
        self.assertEqual(filter_non_primes([2, 3, 5, 7]), [])

        # non-prime numbers and zero
        self.assertEqual(filter_non_primes([0, 1, 4, 6, 8]), [0, 1, 4, 6, 8])

        # list contains negative numbers
        self.assertEqual(filter_non_primes([-1, -2, -3, -4, -5]), [-1, -2, -3, -4, -5])

if __name__ == '__main__':
    unittest.main()
