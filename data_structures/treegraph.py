from utils.problem_constraint_utils import CONSTRAINT_MAX
from data_structures.node import Node


class TreeGraph:
    def __init__(self, root_value, node_connection_list, n):
        self.root_value = root_value
        self.node_connection_list = node_connection_list
        self.node_adjacency_list = []
        self.create_node_adjacency_list(node_connection_list)  # sets node_adjacency_list
        self.node_container = [Node(index) for index in range(1, n + 1)]
        self.visited = set()
        self.construct_tree(self.node_container[root_value - 1].vertex)
        self.root = self.node_container[root_value - 1]

    def construct_tree(self, source):
        for neighbor in self.node_adjacency_list[source]:
            if neighbor in self.visited:
                continue
            if neighbor != self.root_value:
                self.node_container[neighbor - 1].parent = self.node_container[source - 1]
                self.node_container[source - 1].add_child(self.node_container[neighbor - 1])
                self.visited.add(neighbor)
                children_size = len(self.node_container[source - 1].children) - 1
                self.node_container[neighbor - 1].subtree_index = self.node_container[source - 1].subtree_index + [children_size]
            self.construct_tree(self.node_container[neighbor - 1].vertex)

    # def construct_treev1(self):
    #     print(self.node_connection_list)
    #     for child, parent in enumerate(self.node_connection_list, start=2):
    #         #print(child+1, parent)
    #         if child + 1 != self.root_value:
    #             self.node_container[child - 1].parent = self.node_container[parent - 1]
    #             children_size = len(self.node_container[parent - 1].children)
    #             self.node_container[child - 1].subtree_index = self.node_container[parent - 1].subtree_index + \
    #                                                            [children_size]
    #             self.node_container[parent - 1].add_child(self.node_container[child - 1])
    #             print("Not root, child:", child, "parent:", parent)
    #         else:
    #             print("root", child + 1, parent)
    #             self.node_container[parent - 1].add_child(self.node_container[child - 1])

    def assign_data(self):
        pass

    def pre_order_traversal(self, source):
        # print(source)
        for child in source.children:
            self.pre_order_traversal(child)

    def pre_order(self):
        # print("Root", self.root_value)
        for node in self.node_container:
            print(str(node))
        #self.pre_order_traversal(self.root)

    def __str__(self):
        return "".join(self.pre_order_traversal(self.root))

    def create_node_adjacency_list(self, node_connection_list):
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

        self.node_adjacency_list = adj_list


