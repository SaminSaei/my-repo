import unittest
from multiply import multiply_numbers

class TestMultiply(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply_numbers(2, 3), 6)
        self.assertEqual(multiply_numbers(5, 10), 50)
        self.assertEqual(multiply_numbers(0, 5), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply_numbers(-2, 3), -6)
        self.assertEqual(multiply_numbers(-5, -10), 50)
        self.assertEqual(multiply_numbers(-2, -4), 8)

if __name__ == '__main__':
    unittest.main()
