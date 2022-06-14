from unittest import TestCase
from utils import get_factorial_num

class ServerCorrectReturn(TestCase):

    def test_result(self):
        self.assertEqual(get_factorial_num(0), 1)
        self.assertEqual(get_factorial_num(1), 1)
        self.assertEqual(get_factorial_num(2), 2)
        self.assertEqual(get_factorial_num(3), 6)
        self.assertEqual(get_factorial_num(4), 24)
        self.assertEqual(get_factorial_num(5), 120)
        self.assertEqual(get_factorial_num(6), 720)
        self.assertEqual(get_factorial_num(10), 3628800)

