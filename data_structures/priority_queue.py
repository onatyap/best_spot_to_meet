# Min Priority Queue

class PriorityQueue:
    def __init__(self):
        self.container = []

    def push(self, element):
        self.container.append(element)

    def pop(self):
        return self.container.pop(self.container.index(min(self.container, key=lambda x: x.distance)))

    def top(self):
        return min(self.container, key=lambda x: x.distance)

    def is_empty(self):
        return len(self.container) < 1
