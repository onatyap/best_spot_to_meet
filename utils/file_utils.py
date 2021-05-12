import sys


def read_input(f_name):

    try:
        input_file = open(f_name, 'r')
    except OSError:
        print("Could not find file:", f_name)
        sys.exit()

    n, q = [int(x) for x in input_file.readline().split()]
    node_connection_list = [int(x) for x in input_file.readline().split()]
    nearest_nodes = [[int(x) for x in input_file.readline().split()] for _ in range(q)]

    try:
        input_file.close()
    except OSError:
        pass

    return n, q, node_connection_list, nearest_nodes
