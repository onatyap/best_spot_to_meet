from data_structures.priority_queue_node import PriorityQueueNode
from utils.data_types_utils import PriorityQueueNodeList


class PriorityQueue:  # Array based Min Priority Queue
    def __init__(self):
        self.container: PriorityQueueNodeList = []

    def push(self, element: PriorityQueueNode):
        self.container.append(element)

    def pop(self) -> PriorityQueueNode:
        return self.container.pop(self.container.index(min(self.container, key=lambda x: x.distance)))

    def top(self) -> PriorityQueueNode:
        return min(self.container, key=lambda x: x.distance)

    def update(self, updated_element: PriorityQueueNode):
        self.container[self.container.index(updated_element.vertex)] = updated_element

    def print(self):
        output = [str(node) for node in self.container]
        print(output)

    def is_empty(self) -> bool:
        return len(self.container) < 1
