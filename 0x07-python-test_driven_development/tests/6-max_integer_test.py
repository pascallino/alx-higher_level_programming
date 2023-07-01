#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_module_docstring(self):
        """Tests for module docsting"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """Tests for funstion docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    """Unittest for max_integer([2, 7, 1, 100]))
    """
    def test_max_interge_exact(self):
        result = max_integer([2, 7, 1, 100])
        self.assertEqual(result, 100)
    def test_empty_list(self):
        """Unittest for max_integer([..])
        """
        result = max_integer([])
        self.assertEqual(result, None)
    def test_no_arg(self):
        """Unittest for no arguement"""
        self.assertIsNone(max_integer())


if __name__ == '__main__':
    unittest.main()
