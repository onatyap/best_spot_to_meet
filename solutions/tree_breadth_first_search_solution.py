from .best_spot_to_meet_abstract_solution import BestSpotToMeetAbstractSolution
from utils.problem_constraint_utils import CONSTRAINT_MAX
from data_structures.queue import Queue
from data_structures.treegraph import TreeGraph
import math


class TreeBreadthFirstSearchSolution(BestSpotToMeetAbstractSolution):

    def __init__(self, n: int, q: int, node_connection_list: list, friend_locations: list):
        super().__init__(n, q, node_connection_list, friend_locations)
        self.graph.node_connection_list_to_adj_list(self.node_connection_list)
        root = self.graph.find_root()
        self.tree = TreeGraph(root, self.node_connection_list, n)

    def solve(self, day):
        friend_location = self.friend_locations[day]

        friend_a_location, friend_b_location, friend_c_location = friend_location

        friend_pairs = [[friend_a_location, friend_b_location], [friend_b_location, friend_c_location],
                        [friend_c_location, friend_a_location]]

        distance = []
        path = [[]] * 3

        for index, (friend_source, friend_destination) in enumerate(friend_pairs):
            temp_distance = [CONSTRAINT_MAX] * self.n
            temp_distance[friend_source - 1] = 0
            path[index] = []

            source_subtree_index = self.tree.node_container[friend_source - 1].subtree_index
            destination_subtree_index = self.tree.node_container[friend_destination - 1].subtree_index

            temp_node = self.tree.node_container[friend_source - 1]
            intersection_subtree_index = []
            for a, b in zip(source_subtree_index, destination_subtree_index):
                if a == b:
                    intersection_subtree_index.append(a)
                else:
                    break

            while temp_node.subtree_index != intersection_subtree_index:
                path[index].append(temp_node)
                temp_distance[temp_node.parent.vertex - 1] = temp_distance[temp_node.vertex - 1] + 1
                temp_node = temp_node.parent

            for child in destination_subtree_index[len(intersection_subtree_index):]:
                #print(temp_node, child, destination_subtree_index)
                temp_distance[temp_node.children[child].vertex - 1] = temp_distance[temp_node.vertex - 1] + 1
                path[index].append(temp_node)
                temp_node = temp_node.children[child]
            path[index].append(temp_node)
            distance.append(temp_distance)

            #print("Path from", friend_source, "to", friend_destination, "=", [n.vertex for n in path[index]])
            #print("Distance from", friend_source, "to", friend_destination, "=", temp_distance)
            # print("Distance from", friend_source, "to", friend_destination, "=", [a for a in distance[index] if a != CONSTRAINT_MAX])

        if all([len(x) == 1 for x in path]):
            return path[0][0].vertex, (0, 0, 0)

        max_path_length = -CONSTRAINT_MAX
        max_path_index = -1
        for index, _path in enumerate(path):
            path_length = len(_path)
            if max_path_length < path_length:
                max_path_length = path_length
                max_path_index = index

        friend_pair_index = [[0, 1], [1, 2], [2, 0]]

        if max_path_length % 2 == 0:  # if path length is even, two possible centers
            center_a = path[max_path_index][int(max_path_length / 2)]
            center_b = path[max_path_index][int(max_path_length / 2) - 1]

            distance_to_center_a = [0] * 3
            distance_to_center_a[max_path_index] = distance[max_path_index][center_a.vertex - 1]
            remaining_index = [0, 1, 2]
            remaining_index.remove(max_path_index)
            for index in remaining_index:  # in the remaining indices
                if center_a in path[index]:  # if the center is visited in the path
                    distance_to_center_a[index] = distance[index][center_a.vertex - 1]
                else:  # if not visited, run guided bfs
                    # if the current remaining index corresponds to the destination vertex in max path
                    if friend_pair_index[max_path_index][1] == index:
                        distance_to_center_a[index] = max_path_length - distance[max_path_index][center_a.vertex - 1] - 1

                    # if the current remaining index corresponds to the destination vertex in the path
                    # whose source is the destination vertex in the max path
                    elif friend_pair_index[friend_pair_index[max_path_index][1]][1] == index:
                        distance_to_center_a[index] = len(path[friend_pair_index[max_path_index][1]]) - \
                                                    distance[friend_pair_index[max_path_index][1]][center_a.vertex - 1] - 1

            distance_to_center_b = [0] * 3
            distance_to_center_b[max_path_index] = distance[max_path_index][center_b.vertex - 1]
            remaining_index = [0, 1, 2]
            remaining_index.remove(max_path_index)
            for index in remaining_index:  # in the remaining indices
                if center_b in path[index]:  # if the center is visited in the path
                    distance_to_center_b[index] = distance[index][center_b.vertex - 1]
                else:  # if not visited, run guided bfs
                    # if the current remaining index corresponds to the destination vertex in max path
                    if friend_pair_index[max_path_index][1] == index:
                        distance_to_center_b[index] = max_path_length - distance[max_path_index][center_b.vertex - 1] - 1

                    # if the current remaining index corresponds to the destination vertex in the path
                    # whose source is the destination vertex in the max path
                    elif friend_pair_index[friend_pair_index[max_path_index][1]][1] == index:
                        distance_to_center_b[index] = len(path[friend_pair_index[max_path_index][1]]) - \
                                                      distance[friend_pair_index[max_path_index][1]][center_b.vertex - 1] - 1
            min_a = min(distance_to_center_a)
            min_b = min(distance_to_center_b)
            if min_a < min_b:
                return center_a.vertex, distance_to_center_a
            elif min_a == min_b:
                if sum(distance_to_center_a) < sum(distance_to_center_b):
                    return center_a.vertex, distance_to_center_a
                else:
                    return center_b.vertex, distance_to_center_b
            else:
                return center_b.vertex, distance_to_center_b

        else:
            distance_to_center = [0] * 3
            center = path[max_path_index][math.ceil(max_path_length / 2) - 1]
            distance_to_center[max_path_index] = distance[max_path_index][center.vertex - 1]
            remaining_index = [0, 1, 2]
            remaining_index.remove(max_path_index)
            for index in remaining_index:  # in the remaining indices
                if center in path[index]:  # if the center is visited in the path
                    distance_to_center[index] = distance[index][center.vertex - 1]
                else:  # if not visited, run guided bfs
                    # if the current remaining index corresponds to the destination vertex in max path
                    if friend_pair_index[max_path_index][1] == index:
                        distance_to_center[index] = max_path_length - distance[max_path_index][center.vertex - 1] - 1

                    # if the current remaining index corresponds to the destination vertex in the path
                    # whose source is the destination vertex in the max path
                    elif friend_pair_index[friend_pair_index[max_path_index][1]][1] == index:
                        distance_to_center[index] = len(path[friend_pair_index[max_path_index][1]]) -\
                                                    distance[friend_pair_index[max_path_index][1]][center.vertex - 1] - 1
            return center.vertex, distance_to_center

    def run(self):  # O(q * logV) ~ O(q logV)
        for day in range(self.q):  # O(q)
            yield self.solve(day)
