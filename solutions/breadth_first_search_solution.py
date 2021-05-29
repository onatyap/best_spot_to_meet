from .best_spot_to_meet_abstract_solution import BestSpotToMeetAbstractSolution
from utils.problem_constraint_utils import CONSTRAINT_MAX
from data_structures.queue import Queue
from utils.debug_utils import debug_cost_matrix


class BFSSolution(BestSpotToMeetAbstractSolution):

    def graph_construction(self):
        self.graph.node_connection_list_to_adj_list(self.node_connection_list)

    def cost_calculation_for_day(self, day):  # O(V + E)
        friend_location = self.friend_locations[day]
        for source in friend_location:
            visited = set()
            visited.add(source)
            queue = Queue()
            queue.push(source)
            distance = [CONSTRAINT_MAX] * self.n
            distance[source - 1] = 0
            while not queue.is_empty():  # O(V + E)
                visited_node = queue.pop()
                for neighbor in self.graph.container[visited_node]:
                    if neighbor not in visited:
                        queue.push(neighbor)
                        visited.add(neighbor)
                    distance[neighbor - 1] = min(distance[visited_node - 1] + 1, distance[neighbor - 1])
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

    def run(self):  # O(q * (V + E)) ~ O(qV)
        self.graph_construction()
        for day in range(self.q):  # O(q)
            self.cost_calculation_for_day(day)  # O(V + E)
            yield self.solve(day)  # O(V)
            self.graph.cost_container.clear()
