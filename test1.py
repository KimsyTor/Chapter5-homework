import unittest
from exercise1 import duplicate_odds

class TestDuplicateOdds(unittest.TestCase):
    
    def test_duplicate_odds(self):

        # list with odd numbers and zero
        self.assertEqual(duplicate_odds([1, 3, 9, 0]), [1, 1, 3, 3, 9, 9, 0])
        
        # list with negative odd numbers
        self.assertEqual(duplicate_odds([-1, -2, -3, -4]), [-1, -1, -2, -3, -3, -4])
        
        # list with odd decimals
        self.assertEqual(duplicate_odds([1.5, 3.9, 2.2, 8.4]), [1.5, 1.5, 3.9, 3.9, 2.2, 8.4])

if __name__ == '__main__':
    unittest.main()
