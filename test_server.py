from unittest import TestCase
from utils import get_fibonacci_num, get_factorial_num

class ServerCorrectReturn(TestCase):

    def test_fibonacci(self):
        self.assertEqual(get_fibonacci_num(0), 0)
        self.assertEqual(get_fibonacci_num(1), 1)
        self.assertEqual(get_fibonacci_num(2), 1)
        self.assertEqual(get_fibonacci_num(3), 2)
        self.assertEqual(get_fibonacci_num(4), 3)
        self.assertEqual(get_fibonacci_num(5), 5)
        self.assertEqual(get_fibonacci_num(6), 8)
        self.assertEqual(get_fibonacci_num(10), 55)

    def test_factorial(self):
        self.assertEqual(get_factorial_num(0), 1)
        self.assertEqual(get_factorial_num(1), 1)
        self.assertEqual(get_factorial_num(2), 2)
        self.assertEqual(get_factorial_num(3), 6)
        self.assertEqual(get_factorial_num(4), 24)
        self.assertEqual(get_factorial_num(5), 120)
        self.assertEqual(get_factorial_num(6), 720)
        self.assertEqual(get_factorial_num(10), 3628800)
