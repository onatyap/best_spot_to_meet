def floyd_warshall_algo(n, adj_matrix):  # all pairs shortest path
    adj_matrix_temp = adj_matrix.copy()
    for i in range(n):
        for j in range(n):
            for k in range(n):
                adj_matrix_temp[j][k] = min(adj_matrix_temp[j][k],
                                            adj_matrix_temp[j][i] + adj_matrix_temp[i][k])
    return adj_matrix_temp


def find_min_via_floyd_warshall(cost_matrix, friend_locations):
    class GlobalMin:  # [max_pair_distance, total_distance, vertex, cost_list]
        def __init__(self, max_pair_distance, total_distance, vertex, cost_list):
            self.max_pair_distance = max_pair_distance
            self.total_distance = total_distance
            self.vertex = vertex
            self.cost_list = cost_list

    global_min = GlobalMin(1e5, 1e5, -1, [])
    temp_cost_list = cost_matrix[friend_locations, :]
    for i in range(len(temp_cost_list)):
        temp_max_pair_distance = max(temp_cost_list[0][i], temp_cost_list[1][i], temp_cost_list[2][i])
        if temp_max_pair_distance <= global_min.max_pair_distance:
            temp_total_distance = temp_cost_list[0][i] + temp_cost_list[1][i] + temp_cost_list[2][i]
            if temp_total_distance < global_min.total_distance:
                global_min.total_distance = temp_total_distance
                global_min.max_pair_distance = temp_max_pair_distance
                global_min.vertex = i + 1
                global_min.cost_list = temp_cost_list[:, i]

    return global_min.vertex, global_min.cost_list
