import numpy as np


def floyd_warshall_algo(n, adj_matrix):  # all pairs shortest path
    adj_matrix_temp = adj_matrix.copy()
    for i in range(n):
        for j in range(n):
            for k in range(n):
                adj_matrix_temp[j][k] = min(adj_matrix_temp[j][k],
                                            adj_matrix_temp[j][i] + adj_matrix_temp[i][k])
    return adj_matrix_temp


def find_min_via_floyd_warshall(cost_matrix, friend_locations):
    relevant_costs = cost_matrix[friend_locations, :]
    max_dists = np.min(np.max(relevant_costs, axis=0))
    min_max_dist = relevant_costs + 1e5 * (np.max(relevant_costs, axis=0) != max_dists)

    best_node = np.argmin(np.sum(min_max_dist, axis=0))
    return best_node + 1, cost_matrix[best_node, friend_locations]
