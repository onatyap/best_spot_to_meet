import unittest
from tests import read_input
from solutions.breadth_first_search_solution import BFSSolution as BreadthFirstSearch
from utils.debug_utils import debug_test_start, debug_test_end, debug_test_output

problem_name = "BreadthFirstSearch"


class BreadthFirstSearchTests(unittest.TestCase):

    def test_bfs_example1(self):
        debug_test_start(problem_name, 1)
        test_true = ['1 0 1 1',
                     '1 1 1 1']
        n, q, adj_list, friend_locations = read_input('example1.txt')
        solution = BreadthFirstSearch(n, q, adj_list, friend_locations)
        for index, (vertex, distances) in enumerate(solution.run()):
            debug_test_output(vertex, distances)
            v, d0, d1, d2 = [int(x) for x in test_true[index].split()]
            self.assertEqual(vertex, v)
            self.assertEqual(distances[0], d0)
            self.assertEqual(distances[1], d1)
            self.assertEqual(distances[2], d2)
        debug_test_end()

    def test_bfs_example2(self):
        debug_test_start(problem_name, 2)
        test_true = ['3 2 1 1',
                     '3 1 1 1']
        n, q, adj_list, friend_locations = read_input('example2.txt')
        solution = BreadthFirstSearch(n, q, adj_list, friend_locations)
        for index, (vertex, distances) in enumerate(solution.run()):
            debug_test_output(vertex, distances)
            v, d0, d1, d2 = [int(x) for x in test_true[index].split()]
            self.assertEqual(vertex, v)
            self.assertEqual(distances[0], d0)
            self.assertEqual(distances[1], d1)
            self.assertEqual(distances[2], d2)
        debug_test_end()

    def test_bfs_example3(self):
        debug_test_start(problem_name, 3)
        test_true = ['1 0 0 0',
                     '2 0 0 0']
        n, q, adj_list, friend_locations = read_input('example3.txt')
        solution = BreadthFirstSearch(n, q, adj_list, friend_locations)
        for index, (vertex, distances) in enumerate(solution.run()):
            debug_test_output(vertex, distances)
            v, d0, d1, d2 = [int(x) for x in test_true[index].split()]
            self.assertEqual(vertex, v)
            self.assertEqual(distances[0], d0)
            self.assertEqual(distances[1], d1)
            self.assertEqual(distances[2], d2)
        debug_test_end()

    def test_bfs_example4(self):
        debug_test_start(problem_name, 4)
        test_true = ['8 0 3 4',
                     '3 1 1 1',
                     '3 0 2 3',
                     '8 4 1 3']
        n, q, node_connection_list, friend_locations = read_input('example4.txt')
        solution = BreadthFirstSearch(n, q, node_connection_list, friend_locations)

        for index, (vertex, distances) in enumerate(solution.run()):
            debug_test_output(vertex, distances)
            v, d0, d1, d2 = [int(x) for x in test_true[index].split()]
            self.assertEqual(vertex, v, msg='Wrong vertex')
            self.assertEqual(distances[0], d0, msg='Wrong dist1')
            self.assertEqual(distances[1], d1, msg='Wrong dist2')
            self.assertEqual(distances[2], d2, msg='Wrong dist3')
        debug_test_end()

    def test_bfs_example5(self):
        debug_test_start(problem_name, 5)
        test_true = ['3 2 3 4',
                     '15 2 1 2',
                     '3 3 2 2',
                     '3 2 2 2']
        n, q, node_connection_list, friend_locations = read_input('example5.txt')
        solution = BreadthFirstSearch(n, q, node_connection_list, friend_locations)

        for index, (vertex, distances) in enumerate(solution.run()):
            debug_test_output(vertex, distances)
            v, d0, d1, d2 = [int(x) for x in test_true[index].split()]
            self.assertEqual(vertex, v, msg='Wrong vertex')
            self.assertEqual(distances[0], d0, msg='Wrong dist1')
            self.assertEqual(distances[1], d1, msg='Wrong dist2')
            self.assertEqual(distances[2], d2, msg='Wrong dist3')
        debug_test_end()

    def test_bfs_example6(self):
        debug_test_start(problem_name, 6)
        test_true = ['1 1 1 1',
                     '2 1 1 1',
                     '6 1 1 1',
                     '1 4 4 4',
                     '2 1 0 1',
                     '20 1 0 1',
                     '6 2 1 3',
                     '2 4 1 3',
                     '3 3 3 3',
                     '1 3 4 4',
                     '2 3 2 2',
                     '10 2 2 2',
                     '1 4 4 4',
                     '4 4 3 3',
                     '24 1 0 0',
                     '4 0 0 0',
                     '2 1 3 3',
                     '2 3 3 3',
                     '4 1 3 2',
                     '2 2 1 2',
                     '1 4 4 4',
                     '2 2 2 2',
                     '1 4 3 0']
        n, q, node_connection_list, friend_locations = read_input('example6.txt')
        solution = BreadthFirstSearch(n, q, node_connection_list, friend_locations)

        for index, (vertex, distances) in enumerate(solution.run()):
            debug_test_output(vertex, distances)
            v, d0, d1, d2 = [int(x) for x in test_true[index].split()]
            self.assertEqual(vertex, v, msg='Wrong vertex')
            self.assertEqual(distances[0], d0, msg='Wrong dist1')
            self.assertEqual(distances[1], d1, msg='Wrong dist2')
            self.assertEqual(distances[2], d2, msg='Wrong dist3')
        debug_test_end()


if __name__ == '__main__':
    unittest.main()
