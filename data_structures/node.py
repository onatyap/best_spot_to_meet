class Node:
    def __init__(self, vertex, parent=None):
        self.vertex = vertex
        self.parent = parent
        self.subtree_index = []
        self.children = []

    def has_parent(self):
        return self.parent is not None

    def has_children(self):
        return len(self.children) > 0

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return f'Node:{self.vertex}' \
               f'Parent: {self.parent.vertex if self.parent is not None else None} ' \
               f'Children: {[child.vertex for child in self.children]} Subtree index: {self.subtree_index} '
