from .best_spot_to_meet_abstract_solution import BestSpotToMeetAbstractSolution
from utils.problem_constraint_utils import CONSTRAINT_MAX
from data_structures.priority_queue import PriorityQueue
from data_structures.priority_queue_node import PriorityQueueNode


class DijkstraSolution(BestSpotToMeetAbstractSolution):

    def graph_construction(self):
        self.graph.node_connection_list_to_adj_list(self.node_connection_list)

    def cost_calculation(self):
        sorted_vertices = sorted(self.graph.container.keys())
        for source in sorted_vertices:

            distance = [CONSTRAINT_MAX] * self.n
            distance[source - 1] = 0
            for adjacent_vertex in self.graph.container[source]:
                distance[adjacent_vertex - 1] = 1

            priority_queue = PriorityQueue()

            vertex_set = set(self.graph.container)

            for vertex in vertex_set:
                priority_queue.push(PriorityQueueNode(vertex, distance[vertex - 1]))

            while not priority_queue.is_empty():
                min_distance_node = priority_queue.pop()
                for neighbor in self.graph.container[min_distance_node.vertex]:
                    temp_min = distance[min_distance_node.vertex - 1] + 1  # edge weight
                    if temp_min < distance[neighbor - 1]:
                        distance[neighbor - 1] = temp_min

            self.graph.cost_container.append(distance)


    def solve(self, day):
        class GlobalMin:  # [max_pair_distance, total_distance, vertex, cost_list]
            def __init__(self):
                self.max_pair_distance = CONSTRAINT_MAX
                self.total_distance = CONSTRAINT_MAX
                self.vertex = -1
                self.cost_list = []

        global_min = GlobalMin()
        temp_cost_list = [self.graph.cost_container[index-1] for index in self.friend_locations[day]]
        for i, _ in enumerate(temp_cost_list):
            temp_max_pair_distance = max(temp_cost_list[0][i], temp_cost_list[1][i], temp_cost_list[2][i])
            if temp_max_pair_distance <= global_min.max_pair_distance:
                temp_total_distance = temp_cost_list[0][i] + temp_cost_list[1][i] + temp_cost_list[2][i]
                if temp_total_distance < global_min.total_distance:
                    global_min.total_distance = temp_total_distance
                    global_min.max_pair_distance = temp_max_pair_distance
                    global_min.vertex = i + 1
                    global_min.cost_list = [row[i] for row in temp_cost_list]

        return global_min.vertex, global_min.cost_list
