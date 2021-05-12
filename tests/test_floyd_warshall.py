import unittest
from tests import read_input
from solutions.floyd_warshall_solution import FloydWarshallSolution as FloydWarshall


class FloydWarshallTests(unittest.TestCase):

    @staticmethod
    def createFloydWarshall(n, q, adj_list, friend_locations):
        return FloydWarshall(n, q, adj_list, friend_locations)

    def test_floyd_warshall_example1(self):
        test_true = ['1 0 1 1',
                     '1 1 1 1']
        n, q, node_connection_list, friend_locations = read_input('example1.txt')
        solution = self.createFloydWarshall(n, q, node_connection_list, friend_locations)
        for index, (vertex, distances) in enumerate(solution.run()):
            v, d0, d1, d2 = [int(x) for x in test_true[index].split()]
            self.assertEqual(vertex, v)
            self.assertEqual(distances[0], d0, msg='Wrong vertex')
            self.assertEqual(distances[1], d1)
            self.assertEqual(distances[2], d2)


    def test_floyd_warshall_example2(self):
        test_true = ['3 2 1 1',
                     '3 1 1 1']
        n, q, node_connection_list, friend_locations = read_input('example2.txt')
        solution = self.createFloydWarshall(n, q, node_connection_list, friend_locations)
        for index, (vertex, distances) in enumerate(solution.run()):
            v, d0, d1, d2 = [int(x) for x in test_true[index].split()]
            self.assertEqual(vertex, v, msg='Wrong vertex')
            self.assertEqual(distances[0], d0)
            self.assertEqual(distances[1], d1)
            self.assertEqual(distances[2], d2)

    def test_floyd_warshall_example3(self):
        test_true = ['1 0 0 0',
                     '2 0 0 0']
        n, q, node_connection_list, friend_locations = read_input('example3.txt')
        solution = self.createFloydWarshall(n, q, node_connection_list, friend_locations)
        for index, (vertex, distances) in enumerate(solution.run()):
            v, d0, d1, d2 = [int(x) for x in test_true[index].split()]
            self.assertEqual(vertex, v, msg='Wrong vertex')
            self.assertEqual(distances[0], d0, msg='Wrong dist1')
            self.assertEqual(distances[1], d1, msg='Wrong dist2')
            self.assertEqual(distances[2], d2, msg='Wrong dist3')

if __name__ == '__main__':
    unittest.main()
