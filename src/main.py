import sys
import time
import solutions.tree_breadth_first_search_solution
from utils.file_utils import read_input
from solutions.floyd_warshall_solution import FloydWarshallSolution as FloydWarshall
from solutions.johnsons_solution import JohnsonsSolution as Johnsons
from solutions.dijkstra_solution import DijkstraSolution as Dijkstra
from solutions.breadth_first_search_solution import BreadthFirstSearchSolution
from solutions.multi_breadth_first_search_solution import MultiBreadthFirstSearchSolution as MultiBreadthFirstSearch
from solutions.tree_breadth_first_search_solution import TreeBreadthFirstSearchSolution as TreeBreadthFirstSearch
from utils.problem_constraint_utils import solution_list


def main(argv):
    n, q, node_connection_list, friend_locations = read_input(argv[0])
    print(n, q, node_connection_list, friend_locations)
    if len(argv) == 1:  # if solution type was not specified, solve with optimal
        optimal_solution = TreeBreadthFirstSearch(n, q, node_connection_list, friend_locations)
    elif len(argv) == 2:  # if solution was specified, solve with that
        solution_input = argv[1]
        if solution_input in solution_list:
            optimal_solution = eval(solution_input+'(n, q, node_connection_list, friend_locations)')
        else:
            print("Please specify a correct algorithm")
            sys.exit(1)
    else:
        print("Too many parameters, please only specify an input file and a correct algorithm!")
        sys.exit(1)

    start = time.time()  # start
    total = 0
    for vertex, distances in optimal_solution.run():
        print(vertex, distances[0], distances[1], distances[2])
        #start
        start = time.time()
    print(f'Total run took {total * 1e3} ms')


if __name__ == "__main__":
    if len(sys.argv) == 1:  # no arguments supplied
        print("Please specify an input file")
        sys.exit(1)
    # print(' '.join(sys.argv))
    main(sys.argv[1:])  # python main.py examples/example1.txt FloydWarshall
