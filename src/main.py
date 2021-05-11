import numpy as np
import sys


def floyd_warshall_algo(n, adj_matrix):  # all pairs shortest path
    adj_matrix_temp = adj_matrix.copy()
    for i in range(n):
        for j in range(n):
            for k in range(n):
                adj_matrix_temp[j][k] = min(adj_matrix_temp[j][k],
                                            adj_matrix_temp[j][i] + adj_matrix_temp[i][k])
    return adj_matrix_temp


def adj_list_to_matrix(adj_list):
    n = len(adj_list) + 1  # len(adj_list) = n - 1
    adj_matrix = np.inf * np.ones((n, n))
    np.fill_diagonal(adj_matrix, 0)
    for i, qi in enumerate(adj_list, start=1):
        adj_matrix[i, qi] = 1
        adj_matrix[qi, i] = 1

    return adj_matrix


def read_input(f_name):
    with open(f_name) as data:
        n, q = [int(x) for x in data.readline().split()]
        adj_list = [int(x) - 1 for x in data.readline().split()]
        nearest_nodes = [[int(x) - 1 for x in data.readline().split()] for _ in range(q)]
    return n, q, adj_list, nearest_nodes


def find_min_via_floyd_warshall(cost_matrix, friend_locations):
    relevant_costs = cost_matrix[friend_locations, :]
    max_dists = np.min(np.max(relevant_costs, axis=0))
    min_max_dist = relevant_costs + 1e5*(np.max(relevant_costs, axis=0) != max_dists)

    best_node = np.argmin(np.sum(min_max_dist, axis=0))
    return best_node, cost_matrix[best_node, friend_locations]


def main(argv):
    n, q, adj_list, friend_locations = read_input(argv)
    # print(n, q, adj_list, friend_locations)
    adj_matrix = adj_list_to_matrix(adj_list)
    cost_matrix = floyd_warshall_algo(n, adj_matrix)
    # print(cost_matrix)

    for i in range(q):
        vertex, cost_list = find_min_via_floyd_warshall(cost_matrix, friend_locations[i])
        print(vertex+1, " ".join([str(int(x)) for x in cost_list]))


if __name__ == "__main__":
    if len(sys.argv) == 1:  # no arguments supplied
        print("Please provide an input file")

    main(sys.argv[1])  # python main.py examples/example1.txt
