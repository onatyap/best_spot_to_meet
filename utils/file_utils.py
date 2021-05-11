def read_input(f_name):
    with open(f_name, 'r') as data:
        n, q = [int(x) for x in data.readline().split()]
        adj_list = [int(x) - 1 for x in data.readline().split()]
        nearest_nodes = [[int(x) - 1 for x in data.readline().split()] for _ in range(q)]
    return n, q, adj_list, nearest_nodes
