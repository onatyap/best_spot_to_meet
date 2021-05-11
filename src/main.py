import sys
from algorithms.floyd_warshall import *
from utils import *
from utils.file_utils import read_input


def main(argv):
    n, q, adj_list, friend_locations = read_input(argv)
    # print(n, q, adj_list, friend_locations)
    adj_matrix = adj_list_to_matrix(adj_list)
    cost_matrix = floyd_warshall_algo(n, adj_matrix)
    # print(cost_matrix)

    for i in range(q):
        vertex, cost_list = find_min_via_floyd_warshall(cost_matrix, friend_locations[i])
        print(vertex, " ".join([str(int(x)) for x in cost_list]))


if __name__ == "__main__":
    if len(sys.argv) == 1:  # no arguments supplied
        print("Please provide an input file")

    main(sys.argv[1])  # python main.py examples/example1.txt
