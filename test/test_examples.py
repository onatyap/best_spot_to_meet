import unittest
import os
from utils.file_utils import read_input as ri
from utils import adj_list_to_matrix
from algorithms.floyd_warshall import floyd_warshall_algo, find_min_via_floyd_warshall


def read_input(example):
    return ri(os.path.join('../examples', example))


def prep(example):
    n, q, adj_list, friend_locations = read_input(example)
    adj_matrix = adj_list_to_matrix(adj_list)
    cost_matrix = floyd_warshall_algo(n, adj_matrix)

    for i in range(q):
        vertex, cost_list = find_min_via_floyd_warshall(cost_matrix, friend_locations[i])
        yield str(vertex) + ' ' + ' '.join([str(int(x)) for x in cost_list])


class ExamplesTest(unittest.TestCase):

    def test_example1(self):
        test_true = ['1 0 1 1',
                     '1 1 1 1']
        for index, case in enumerate(prep('example1.txt')):
            self.assertEqual(test_true[index], case)

    def test_example2(self):
        test_true = ['3 2 1 1',
                     '3 1 1 1']
        for index, case in enumerate(prep('example2.txt')):
            self.assertEqual(test_true[index], case)


if __name__ == '__main__':
    unittest.main()
