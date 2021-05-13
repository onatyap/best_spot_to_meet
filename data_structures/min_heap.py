import math

from data_structures.priority_queue_node import PriorityQueueNode
from utils.data_types_utils import PriorityQueueNodeList


class MinHeap:
    def __init__(self):
        self.container: PriorityQueueNodeList = []
        self.size = 0
        self.position_container = []

    def push(self, element: PriorityQueueNode):
        self.container.append(element)
        self.position_container.append(self.size)
        self.size += 1

    def pop(self) -> PriorityQueueNode:
        if self.is_empty():
            return None

        first_node = self.container[0]  # first element (root node)
        last_node = self.container[-1]  # last element
        self.container[0] = last_node  # put last in first

        self.position_container[last_node.vertex - 1] = 0
        self.position_container[first_node.vertex - 1] = self.size - 1

        self.size -= 1
        self.heap_update(0)

        return first_node

    def heap_update(self, index):
        smallest_index = index
        right_child_index = 2 * index + 2
        left_child_index = 2 * index + 1

        if right_child_index < self.size and self.container[right_child_index].distance < self.container[smallest_index].distance:
            smallest_index = right_child_index

        if left_child_index < self.size and self.container[left_child_index].distance < self.container[smallest_index].distance:
            smallest_index = left_child_index

        if index != smallest_index:  # a smaller element is found in the children
            self.position_container[self.container[smallest_index].vertex - 1] = index
            self.position_container[self.container[index].vertex - 1] = smallest_index

            temp_priority_queue_node = self.container[index]
            self.container[index] = self.container[smallest_index]
            self.container[smallest_index] = temp_priority_queue_node

            self.heap_update(smallest_index)

    def update(self, updated_element: PriorityQueueNode):
        index = self.position_container[updated_element.vertex - 1]

        self.container[index].distance = updated_element.distance

        up_index = math.floor((index - 1) / 2)

        while index > 0 and self.container[index].distance < self.container[up_index].distance:
            self.position_container[self.container[up_index].vertex - 1] = index
            self.position_container[self.container[index].vertex - 1] = up_index

            temp_priority_queue_node = self.container[index]
            self.container[index] = self.container[up_index]
            self.container[up_index] = temp_priority_queue_node

            index = up_index
            up_index = math.floor((index - 1) / 2)

    def is_in_min_heap(self, vertex):
        return self.position_container[vertex - 1] < self.size

    def is_empty(self):
        return self.size == 0
