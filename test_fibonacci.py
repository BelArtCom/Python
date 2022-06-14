from unittest import TestCase
from utils import get_factorial_num

class ServerCorrectReturn(TestCase):

    def test_result(self):
        self.assertEqual(get_factorial_num(0), 0)
        self.assertEqual(get_factorial_num(1), 1)
        self.assertEqual(get_factorial_num(2), 1)
        self.assertEqual(get_factorial_num(3), 2)
        self.assertEqual(get_factorial_num(4), 3)
        self.assertEqual(get_factorial_num(5), 5)
        self.assertEqual(get_factorial_num(6), 8)
        self.assertEqual(get_factorial_num(10), 55)

