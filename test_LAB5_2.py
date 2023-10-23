import unittest
from LAB5_2 import A

class TestH(unittest.TestCase):
    def test_A(self):
        self.assertEqual(A(-1, 1, -1), 0.0)  # add assertion here


if __name__ == '__main__':
    unittest.main()
