from utils.problem_constraint_utils import CONSTRAINT_MAX


class Graph:
    def __init__(self):
        self.container = []
        self.cost_container = []

    def adj_list_to_matrix(self, adj_list):
        n = len(adj_list) + 1  # len(adj_list) = n - 1
        adj_matrix = [[CONSTRAINT_MAX for _ in range(n)] for _ in range(n)]
        adj_matrix[0][0] = 0
        for i, qi in enumerate(adj_list, start=1):
            adj_matrix[i][i] = 0
            adj_matrix[i][qi] = 1
            adj_matrix[qi][i] = 1

        self.container = adj_matrix
