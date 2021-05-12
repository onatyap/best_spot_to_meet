

class Queue:
    def __init__(self):
        self.container = []
        self.size = 0

    def push(self, element):
        self.container[self.size] = element
        self.size += 1

    def pop(self):
        if self.size == 0:
            return

        self.size -= 1
        self.container.pop(self.size)

    def top(self):
        return self.container[self.size - 1]

    def is_empty(self):
        return self.size == 0
