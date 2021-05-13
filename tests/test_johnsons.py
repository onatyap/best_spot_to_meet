import unittest
from tests import read_input
from solutions.johnsons_solution import JohnsonsSolution as Johnsons
from utils.debug_utils import debug_test_start, debug_test_end, debug_test_output

problem_name = "Johnson's"


class JohnsonsTests(unittest.TestCase):

    def test_johnsons_example1(self):
        debug_test_start(problem_name, 1)
        test_true = ['1 0 1 1',
                     '1 1 1 1']
        n, q, adj_list, friend_locations = read_input('example1.txt')
        solution = Johnsons(n, q, adj_list, friend_locations)
        for index, (vertex, distances) in enumerate(solution.run()):
            debug_test_output(vertex, distances)
            v, d0, d1, d2 = [int(x) for x in test_true[index].split()]
            self.assertEqual(vertex, v)
            self.assertEqual(distances[0], d0)
            self.assertEqual(distances[1], d1)
            self.assertEqual(distances[2], d2)
        debug_test_end()

    def test_johnsons_example2(self):
        debug_test_start(problem_name, 2)
        test_true = ['3 2 1 1',
                     '3 1 1 1']
        n, q, adj_list, friend_locations = read_input('example2.txt')
        solution = Johnsons(n, q, adj_list, friend_locations)
        for index, (vertex, distances) in enumerate(solution.run()):
            debug_test_output(vertex, distances)
            v, d0, d1, d2 = [int(x) for x in test_true[index].split()]
            self.assertEqual(vertex, v)
            self.assertEqual(distances[0], d0)
            self.assertEqual(distances[1], d1)
            self.assertEqual(distances[2], d2)
        debug_test_end()

    def test_johnsons_example3(self):
        debug_test_start(problem_name, 3)
        test_true = ['1 0 0 0',
                     '2 0 0 0']
        n, q, adj_list, friend_locations = read_input('example3.txt')
        solution = Johnsons(n, q, adj_list, friend_locations)
        for index, (vertex, distances) in enumerate(solution.run()):
            debug_test_output(vertex, distances)
            v, d0, d1, d2 = [int(x) for x in test_true[index].split()]
            self.assertEqual(vertex, v)
            self.assertEqual(distances[0], d0)
            self.assertEqual(distances[1], d1)
            self.assertEqual(distances[2], d2)
        debug_test_end()

    def test_johnsons_example4(self):
        debug_test_start(problem_name, 4)
        test_true = ['8 0 3 4',
                     '3 1 1 1',
                     '3 0 2 3',
                     '8 4 1 3']
        n, q, adj_list, friend_locations = read_input('example4.txt')
        solution = Johnsons(n, q, adj_list, friend_locations)
        for index, (vertex, distances) in enumerate(solution.run()):
            debug_test_output(vertex, distances)
            v, d0, d1, d2 = [int(x) for x in test_true[index].split()]
            self.assertEqual(vertex, v)
            self.assertEqual(distances[0], d0)
            self.assertEqual(distances[1], d1)
            self.assertEqual(distances[2], d2)
        debug_test_end()

    def test_johnsons_example5(self):
        debug_test_start(problem_name, 5)
        test_true = ['3 2 3 4',
                     '15 2 1 2',
                     '3 3 2 2',
                     '3 2 2 2']
        n, q, adj_list, friend_locations = read_input('example5.txt')
        solution = Johnsons(n, q, adj_list, friend_locations)
        for index, (vertex, distances) in enumerate(solution.run()):
            debug_test_output(vertex, distances)
            v, d0, d1, d2 = [int(x) for x in test_true[index].split()]
            self.assertEqual(vertex, v)
            self.assertEqual(distances[0], d0)
            self.assertEqual(distances[1], d1)
            self.assertEqual(distances[2], d2)
        debug_test_end()


if __name__ == '__main__':
    unittest.main()
