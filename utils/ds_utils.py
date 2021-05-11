import numpy as np


def adj_list_to_matrix(adj_list):
    n = len(adj_list) + 1  # len(adj_list) = n - 1
    adj_matrix = np.inf * np.ones((n, n))
    np.fill_diagonal(adj_matrix, 0)
    for i, qi in enumerate(adj_list, start=1):
        adj_matrix[i, qi] = 1
        adj_matrix[qi, i] = 1

    return adj_matrix
