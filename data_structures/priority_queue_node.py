class PriorityQueueNode:
    def __init__(self, vertex, distance):
        self.vertex = vertex
        self.distance = distance

    def __str__(self):
        return str(self.vertex) + ", " + str(self.distance)

    def __eq__(self, other):  # other: Vertex
        return self.vertex == other
