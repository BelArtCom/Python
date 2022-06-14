from unittest import TestCase
from utils import get_fibonacci_num

class ServerCorrectReturn(TestCase):

    def test_result(self):
        self.assertEqual(get_fibonacci_num(2), 1)
        self.assertEqual(get_fibonacci_num(3), 2)
        self.assertEqual(get_fibonacci_num(4), 3)
        self.assertEqual(get_fibonacci_num(5), 5)
        self.assertEqual(get_fibonacci_num(6), 8)

