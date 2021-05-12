from utils.problem_constraint_utils import CONSTRAINT_MAX


class Graph:
    def __init__(self):
        self.container = []  # adjacency list or matrix
        self.cost_container = []  # for dynamic programming such as floyd warshall and johnson's solutions

    def node_connection_list_to_adj_matrix(self, node_connection_list):
        n = len(node_connection_list) + 1  # len(adj_list) = n - 1
        adj_matrix = [[CONSTRAINT_MAX for _ in range(n)] for _ in range(n)]
        adj_matrix[0][0] = 0
        for i, qi in enumerate(node_connection_list, start=1):
            adj_matrix[i][i] = 0
            adj_matrix[i][qi] = 1
            adj_matrix[qi][i] = 1

        self.container = adj_matrix

    def node_connection_list_to_adj_list(self, node_connection_list):
        n = len(node_connection_list) + 1  # len(adj_list) = n - 1
        adj_list = dict()

        for i, qi in enumerate(node_connection_list, start=1):
            if qi not in adj_list:
                adj_list[qi] = [i + 1]
            else:
                adj_list[qi] += [i + 1]

            if i + 1 not in adj_list:
                adj_list[i + 1] = [qi]
            else:
                adj_list[i + 1] += [qi]

        self.container = adj_list
