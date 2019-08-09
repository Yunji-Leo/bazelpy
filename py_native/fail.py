"""A tiny example binary for the native Python rules of Bazel."""
import unittest
import lib

class TestGetNumber(unittest.TestCase):
    def test_fail(self):
        self.assertEqual(lib.GetNumber(),0)

if __name__ == '__main__':
    unittest.main()