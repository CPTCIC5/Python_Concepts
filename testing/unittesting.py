import unittest
from prime import is_prime

class Tests(unittest.TestCase):
    def test1(self):
        """Checks that 1 is not prime"""
        self.assertFalse(is_prime(1))

    def test2(self):
        """Checks that 2 is prime"""
        self.assertTrue(is_prime(2))

    def test8(self):
        """checks that 8 is not prime"""
        self.assertTrue(is_prime(8))

if __name__ == '__main__':
    unittest.main()