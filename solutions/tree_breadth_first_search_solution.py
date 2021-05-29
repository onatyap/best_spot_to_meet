from .best_spot_to_meet_abstract_solution import BestSpotToMeetAbstractSolution
from utils.problem_constraint_utils import CONSTRAINT_MAX
from data_structures.queue import Queue


class TreeBFSSolution(BestSpotToMeetAbstractSolution):

    def graph_construction(self):
        self.graph.node_connection_list_to_adj_list(self.node_connection_list)

    def solve(self, day):
        friend_location = self.friend_locations[day]

        friend_a_location, friend_b_location, friend_c_location = friend_location

        class Friend:
            def __init__(self, location, n):
                self.location = location
                self.visited_set = set()

                self.queue = Queue()
                self.queue.push(location)

                self.distance = [CONSTRAINT_MAX] * n
                self.distance[location - 1] = 0

        friend_a = Friend(friend_a_location, self.n)
        friend_b = Friend(friend_b_location, self.n)
        friend_c = Friend(friend_c_location, self.n)

        friends = [friend_a, friend_b, friend_c]

        visited_count = [0] * self.n
        solution_nodes = []

        class GlobalMin:
            def __init__(self):
                self.total_distance = CONSTRAINT_MAX
                self.vertex = -1

        while any([not friend.queue.is_empty() for friend in friends]):
            for friend in friends:
                if friend.queue.is_empty():
                    continue
                visited_nodes = []
                while not friend.queue.is_empty():
                    visited_node = friend.queue.pop()
                    visited_nodes.append(visited_node)
                    friend.visited_set.add(visited_node)
                    visited_count[visited_node - 1] += 1
                    if visited_count[visited_node - 1] == len(friends):
                        solution_nodes.append(visited_node)
                for visited_node in visited_nodes:
                    for neighbor in self.graph.container[visited_node]:
                        if neighbor not in friend.visited_set:
                            friend.queue.push(neighbor)
                            friend.distance[neighbor - 1] = min(friend.distance[visited_node - 1] + 1,
                                                                friend.distance[neighbor - 1])

            if len(solution_nodes) > 0:
                global_min = GlobalMin()
                for solution_node in solution_nodes:
                    temp_distance = sum(friend.distance[solution_node - 1] for friend in friends)
                    if temp_distance < global_min.total_distance:
                        global_min.total_distance = temp_distance
                        global_min.vertex = solution_node

                return global_min.vertex, [friend.distance[global_min.vertex - 1] for friend in friends]

        # visited_set_map = {x: {x} for x in friend_location}
        # friend_queue_map = {x: Queue() for x in friend_location}
        # distance_map = {x: [CONSTRAINT_MAX] * self.n for x in friend_location}
        # visited_count = [0] * self.n
        # for source in friend_location:  # initialization
        #     friend_queue_map.get(source).push(source)
        #     distance_map.get(source)[source - 1] = 0

        # while not (friend_queue_map.get(friend_location[0]).is_empty() and friend_queue_map.get(friend_location[1]).is_empty() and friend_queue_map.get(friend_location[2]).is_empty()):

        # while any([not queue.is_empty() for queue in friend_queue_map.values()]):
        #     for source in friend_location:
        #         if friend_queue_map.get(source).is_empty():
        #             continue
        #         visited_nodes = []
        #         while not friend_queue_map.get(source).is_empty():
        #             visited_node = friend_queue_map.get(source).pop()
        #             visited_nodes.append(visited_node)
        #             visited_set_map.get(source).add(visited_node)
        #             visited_count[visited_node - 1] += 1
        #             if visited_count[visited_node - 1] == len(friend_queue_map.keys()):
        #                 return visited_node, [distance_map.get(friend)[visited_node - 1] for friend in friend_location]
        #         for visited_node in visited_nodes:
        #             for neighbor in self.graph.container[visited_node]:
        #                 if neighbor not in visited_set_map.get(source):
        #                     friend_queue_map.get(source).push(neighbor)
        #                     distance_map.get(source)[neighbor - 1] = min(distance_map.get(source)[visited_node - 1] + 1,
        #                                                                  distance_map.get(source)[neighbor - 1])

        return "Not possible", (0, 0, 0)

    def run(self):  # O(q * (V + E)) ~ O(qV)
        self.graph_construction()
        for day in range(self.q):  # O(q)
            yield self.solve(day)
