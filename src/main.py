import numpy as np
import sys
import os

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
        adj_list = [int(x)-1 for x in data.readline().split()]
        nearest_nodes = [[int(x)-1 for x in data.readline().split()] for _ in range(q)]
    return n, q, adj_list, nearest_nodes


def find_min_via_floyd_warshall(cost_matrix, friend_locations):
    class GlobalMin:  # [max_pair_distance, total_distance, vertex, cost_list]
        def __init__(self, max_pair_distance, total_distance, vertex, cost_list):
            self.max_pair_distance = max_pair_distance
            self.total_distance = total_distance
            self.vertex = vertex
            self.cost_list = cost_list

    global_min = GlobalMin(1e5, 1e5, -1, [])
    temp_cost_list = cost_matrix[friend_locations, :]
    for i in range(len(temp_cost_list)):
        temp_max_pair_distance = max(temp_cost_list[0][i], temp_cost_list[1][i], temp_cost_list[2][i])
        if temp_max_pair_distance <= global_min.max_pair_distance:
            temp_total_distance = temp_cost_list[0][i] + temp_cost_list[1][i] + temp_cost_list[2][i]
            if temp_total_distance < global_min.total_distance:
                global_min.total_distance = temp_total_distance
                global_min.max_pair_distance = temp_max_pair_distance
                global_min.vertex = i + 1
                global_min.cost_list = temp_cost_list[:, i]

    return global_min.vertex, global_min.cost_list


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
