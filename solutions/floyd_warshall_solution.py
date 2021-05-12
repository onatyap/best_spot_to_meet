from .best_spot_to_meet_abstract_solution import BestSpotToMeetAbstractSolution
from utils.problem_constraint_utils import CONSTRAINT_MAX


class FloydWarshallSolution(BestSpotToMeetAbstractSolution):

    def graph_construction(self):
        self.graph.adj_list_to_matrix(self.adj_list)

    def cost_calculation(self):
        cost_matrix = self.graph.container.copy()
        n = len(cost_matrix)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    cost_matrix[j][k] = min(cost_matrix[j][k], cost_matrix[j][i] + cost_matrix[i][k])
        self.graph.cost_container = cost_matrix

    def solve(self, day):
        class GlobalMin:  # [max_pair_distance, total_distance, vertex, cost_list]
            def __init__(self):
                self.max_pair_distance = CONSTRAINT_MAX
                self.total_distance = CONSTRAINT_MAX
                self.vertex = -1
                self.cost_list = []

        global_min = GlobalMin()
        temp_cost_list = [self.graph.cost_container[index] for index in self.friend_locations[day]]
        for i in range(len(temp_cost_list)):
            temp_max_pair_distance = max(temp_cost_list[0][i], temp_cost_list[1][i], temp_cost_list[2][i])
            if temp_max_pair_distance <= global_min.max_pair_distance:
                temp_total_distance = temp_cost_list[0][i] + temp_cost_list[1][i] + temp_cost_list[2][i]
                if temp_total_distance < global_min.total_distance:
                    global_min.total_distance = temp_total_distance
                    global_min.max_pair_distance = temp_max_pair_distance
                    global_min.vertex = i + 1
                    global_min.cost_list = [row[i] for row in temp_cost_list]

        return global_min.vertex, global_min.cost_list
