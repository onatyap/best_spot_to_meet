import unittest
from tests import read_input


class FloydWarshallTests(unittest.TestCase):

    def test_floyd_warshall_example1(self):
        test_true = ['1 0 1 1',
                     '1 1 1 1']
        for index, case in enumerate(read_input('example1.txt')):
            self.assertEqual(test_true[index], case)

    def test_floyd_warshall_example2(self):
        test_true = ['3 2 1 1',
                     '3 1 1 1']
        for index, case in enumerate(read_input('example2.txt')):
            self.assertEqual(test_true[index], case)


if __name__ == '__main__':
    unittest.main()
