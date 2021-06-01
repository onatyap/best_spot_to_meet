from utils.problem_constraint_utils import CONSTRAINT_MAX
from data_structures.node import Node


class Tree:
    def __init__(self, root_value, node_connection_list):
        self.root_value = root_value
        self.node_connection_list = node_connection_list
        self.root = self.construct_tree(Node(root_value))

    def construct_tree(self, source):
        if source.vertex == self.root_value:
            source.parent = None
        children = [Node(index + 2, source) for index, value in enumerate(self.node_connection_list) if value == source.vertex]
        source.children = children
        for child in children:
            self.construct_tree(child)
        return source

    def assign_data(self):
        pass

    def pre_order_traversal(self, source):
        print(source)
        for child in source.children:
            self.pre_order_traversal(child)

    def pre_order(self):
        self.pre_order_traversal(self.root)

    def __str__(self):
        return "".join(self.pre_order_traversal(self.root))



