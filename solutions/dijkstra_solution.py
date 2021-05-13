from .best_spot_to_meet_abstract_solution import BestSpotToMeetAbstractSolution
from utils.problem_constraint_utils import CONSTRAINT_MAX
from data_structures.min_heap import MinHeap
from data_structures.priority_queue import PriorityQueue
from data_structures.priority_queue_node import PriorityQueueNode
from utils.debug_utils import debug_cost_matrix


class DijkstraSolution(BestSpotToMeetAbstractSolution):

    def graph_construction(self):
        self.graph.node_connection_list_to_adj_list(self.node_connection_list)

    def cost_calculation_for_day(self, day):
        friend_location = self.friend_locations[day]
        for source in friend_location:
            distance = [CONSTRAINT_MAX] * self.n
            distance[source - 1] = 0
            #min_heap = MinHeap()
            min_heap = PriorityQueue()

            vertex_set = set(self.graph.container)

            for vertex in vertex_set:
                min_heap.push(PriorityQueueNode(vertex, distance[vertex - 1]))

            #min_heap.position_container[source - 1] = source - 1
            #distance[source - 1] = 0
            #min_heap.update(PriorityQueueNode(source, distance[source - 1]))

            while not min_heap.is_empty():
                min_distance_node = min_heap.pop()
                for neighbor in self.graph.container[min_distance_node.vertex]:
                    temp_min = distance[min_distance_node.vertex - 1] + 1  # edge weight
                    if temp_min < distance[neighbor - 1]:
                        distance[neighbor - 1] = temp_min
                        min_heap.update(PriorityQueueNode(neighbor, temp_min))

            self.graph.cost_container.append(distance)

    def solve(self, day):
        class GlobalMin:  # [max_pair_distance, total_distance, vertex, cost_list]
            def __init__(self):
                self.max_pair_distance = CONSTRAINT_MAX
                self.total_distance = CONSTRAINT_MAX
                self.vertex = -1
                self.cost_list = []

        global_min = GlobalMin()
        temp_cost_list = self.graph.cost_container
        debug_cost_matrix(temp_cost_list, day)
        for i in range(len(temp_cost_list[0])):
            temp_max_pair_distance = max(temp_cost_list[0][i], temp_cost_list[1][i], temp_cost_list[2][i])
            if temp_max_pair_distance < global_min.max_pair_distance:
                temp_total_distance = temp_cost_list[0][i] + temp_cost_list[1][i] + temp_cost_list[2][i]
                global_min.total_distance = temp_total_distance
                global_min.max_pair_distance = temp_max_pair_distance
                global_min.vertex = i + 1
                global_min.cost_list = [row[i] for row in temp_cost_list]
            elif temp_max_pair_distance == global_min.max_pair_distance:
                temp_total_distance = temp_cost_list[0][i] + temp_cost_list[1][i] + temp_cost_list[2][i]
                if temp_total_distance < global_min.total_distance:
                    global_min.total_distance = temp_total_distance
                    global_min.max_pair_distance = temp_max_pair_distance
                    global_min.vertex = i + 1
                    global_min.cost_list = [row[i] for row in temp_cost_list]

        return global_min.vertex, global_min.cost_list

    def run(self):
        self.graph_construction()
        for day in range(self.q):
            self.cost_calculation_for_day(day)
            yield self.solve(day)
            self.graph.cost_container.clear()
