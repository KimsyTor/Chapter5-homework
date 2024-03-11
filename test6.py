import unittest
from exercise6 import detect_pattern

class TestDetectPattern(unittest.TestCase):
    def test_detect_pattern(self):

        # Test detection function for greatest common factor in a variety of cases
        self.assertEqual(detect_pattern([1, 2, 3]), 1)
        self.assertEqual(detect_pattern([10, 20, 30]), 10)

        # Test special cases
        self.assertEqual(detect_pattern([1, 2, 4]), 0)  # No greatest common factor
        self.assertEqual(detect_pattern([-2, -4, -6]), 2)  # Negative numbers

if __name__ == '__main__':
    unittest.main()
