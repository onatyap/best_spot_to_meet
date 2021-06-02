import sys
import random
import itertools


def generate_graph(f_name, n, q, b_min, b_max=-1):  # n = number of nodes, q = number of days, b = branching factor
    if b_max == -1:
        b_max = b_min
    try:
        input_file = open(f"outputs/{f_name}", mode='a')
    except OSError:
        print("Could not open file:", f"outputs/{f_name}")
        sys.exit()

    line = ""
    node_count = 1  # root node 1
    for node in range(1, n + 1):
        branching_factor = random.randint(b_min, b_max)
        line += f"{node} " * branching_factor
        node_count += branching_factor
    if q == 0:
        q = node_count * 2
    input_file.write(f"{node_count} {q}\n")
    print(node_count, q)

    print(line)
    input_file.write(f"{line}\n")

    picked_values = set()
    for _ in range(1, q + 1):
        random_value_a = random.randint(1, node_count)
        random_value_b = random.randint(1, node_count)
        random_value_c = random.randint(1, node_count)
        picked_tuple = (random_value_a, random_value_b, random_value_c)
        if picked_tuple not in picked_values:
            print(random_value_a, random_value_b, random_value_c)
            input_file.write(f"{random_value_a} {random_value_b} {random_value_c}\n")
            picked_values.add(picked_tuple)

    try:
        input_file.close()
    except OSError:
        pass