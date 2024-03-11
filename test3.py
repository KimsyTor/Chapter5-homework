import unittest
from exercise3 import calculate_product

class TestCalculateProduct(unittest.TestCase):
    
    def test_calculate_product(self):
     
      # list of numbers
      self.assertEqual(calculate_product([1, 2, 3, 4, 5, 6]), 720)

      # list of zeros
      self.assertEqual(calculate_product([0, 0, 0, 0]), 0)

      # list with one number
      self.assertEqual(calculate_product([7]), 'invalid input')

      # empty list
      self.assertEqual(calculate_product([]), 'invalid input')

      # negative numbers
      self.assertEqual(calculate_product([-1, -2, -3, -4]), 24)
     
if __name__ == '__main__':
    unittest.main()
