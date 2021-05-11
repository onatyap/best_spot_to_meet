import unittest
import os
from utils.file_utils import read_input as ri
from utils import adj_list_to_matrix


def read_input(example):
    return ri(os.path.join('../examples', example))


class UtilsTests(unittest.TestCase):
    reason = False

    def test_input(self):
        n, q, adj_list, friend_locations = read_input('example1.txt')

        self.assertEqual(3, n)
        self.assertEqual(2, q)
        self.assertListEqual([0, 0], adj_list)
        self.assertListEqual([0, 1, 2], friend_locations[0])
        self.assertListEqual([1, 2, 2], friend_locations[1])


if __name__ == '__main__':
    unittest.main()
