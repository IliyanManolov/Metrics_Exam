import math
import unittest

class TestAbsoluteValueFunction(unittest.TestCase):
    
    def test_positive_number(self):
        result = absolute_value(5)
        self.assertEqual(result, 5)

    def test_negative_number(self):
        result = absolute_value(-3.14)
        self.assertEqual(result, 3.14)

    def test_large_positive(self):
        result = absolute_value(5000000000)
        self.assertEqual(result, 5000000000)

    def test_large_negative(self):
        result = absolute_value(-5000000000)
        self.assertEqual(result, 5000000000)

    def test_zero(self):
        result = absolute_value(0)
        self.assertEqual(result, 0)

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            absolute_value("invalid")

    def test_invalid_input_list(self):
        with self.assertRaises(TypeError):
            absolute_value([1, 2, 3])

    def test_no_input(self):
        with self.assertRaises(TypeError):
            absolute_value()

if __name__ == '__main__':
    unittest.main()
