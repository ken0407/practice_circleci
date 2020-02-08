import unittest
import os, sys

from practice_circleci.core import int_num

#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestCore(unittest.TestCase):
    def test_add(self):
        base_num = 5
        num = int_num(base_num)
        y = 3
        num.add(y)
        assert num.value == 8

    def test_diff(self):
        base_num = 5
        num = int_num(base_num)
        y = 3
        num.diff(y)
        assert num.value == 2



if __name__ == '__main__':
    unittest.main()
