from utils.problem_constraint_utils import CONSTRAINT_MAX
from data_structures.queue import Queue
import math


class Graph:
    def __init__(self, n):
        self.container = []  # adjacency list or matrix
        self.cost_container = []  # for dynamic programming such as floyd warshall and johnson's solutions
        self.n = n

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

    def find_root(self):
        furthest_vertex_from_first = self.find_furthest_vertex(1)
        furthest_vertex_from_second = self.find_furthest_vertex(furthest_vertex_from_first)
        return self.find_middle(furthest_vertex_from_first, furthest_vertex_from_second)

    def find_furthest_vertex(self, source):
        distance = self.bfs(source)
        return distance.index(max(distance)) + 1  # due to 0 based indexing

    def find_middle(self, source, destination):
        path = self.bfs(source, destination)
        return path[math.ceil(len(path)/2) - 1]

    def bfs(self, source, destination=-1):
        visited = set()
        visited.add(source)
        queue = Queue()
        queue.push((source, [source]))
        distance = [CONSTRAINT_MAX] * self.n
        distance[source - 1] = 0
        while not queue.is_empty():  # O(V + E)
            visited_node, path = queue.pop()
            for neighbor in self.container[visited_node]:
                if neighbor == destination:
                    return path + [destination]
                else:
                    if neighbor not in visited:
                        queue.push((neighbor, path + [neighbor]))
                        visited.add(neighbor)
                    distance[neighbor - 1] = min(distance[visited_node - 1] + 1, distance[neighbor - 1])
        return distance
