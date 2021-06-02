import sys
import time
import itertools
import solutions.tree_breadth_first_search_solution
from utils.file_utils import read_input
from solutions.floyd_warshall_solution import FloydWarshallSolution as FloydWarshall
from solutions.johnsons_solution import JohnsonsSolution as Johnsons
from solutions.dijkstra_solution import DijkstraSolution as Dijkstra
from solutions.breadth_first_search_solution import BreadthFirstSearchSolution as BreadthFirstSearch
from solutions.multi_breadth_first_search_solution import MultiBreadthFirstSearchSolution as MultiBreadthFirstSearch
from solutions.tree_breadth_first_search_solution import TreeBreadthFirstSearchSolution as TreeBreadthFirstSearch
from utils.problem_constraint_utils import solution_list
from utils.graph_generator_util import generate_graph


def main(argv):
    #for a,b,c in itertools.product(range(1,51), repeat=3):
    #    print(a,b,c)
    #return
    #generate_graph(f"test{time.time()}.txt", 1000, 0, 3, 5)
    #return
    grand_total = 0
    if argv is None:
        for solution in solution_list:
            solution_total = 0
            for i in range(1, 11):
                n, q, node_connection_list, friend_locations = read_input(f"examples/example{i}.txt")
                optimal_solution = eval(solution + '(n, q, node_connection_list, friend_locations)')

                print("Program started with", solution, "for", f"examples/example{i}.txt")
                start = time.time()  # start
                total = 0
                for vertex, distances in optimal_solution.run():
                    # stop
                    end = time.time()
                    total += (end - start)
                    # print(vertex, distances[0], distances[1], distances[2])
                    # start
                    start = time.time()
                print(f'{solution} for examples/example{i}.txt took {total * 1e3} ms')
                solution_total += total
            print(f'{solution} took {solution_total * 1e3} ms')
            grand_total += solution_total
        print(f'Grand Total run took {grand_total * 1e3} ms')
    else:
        if argv[0] == "all-examples":
            solution_total = 0
            for i in range(1, 11):
                n, q, node_connection_list, friend_locations = read_input(f"examples/example{i}.txt")
                optimal_solution = eval(argv[1] + '(n, q, node_connection_list, friend_locations)')

                print("Program started with", argv[1], "for", f"examples/example{i}.txt")
                start = time.time()  # start
                total = 0
                for vertex, distances in optimal_solution.run():
                    # stop
                    end = time.time()
                    total += (end - start)
                    # print(vertex, distances[0], distances[1], distances[2])
                    # start
                    start = time.time()
                print(f'{argv[1]} for examples/example{i}.txt took {total * 1e3} ms')
                solution_total += total
            print(f'{argv[1]} took {solution_total * 1e3} ms')
        elif "test" in argv[0] and len(argv) < 2:  # test provided but no solution specified
            for solution in solution_list:
                try:
                    n, q, node_connection_list, friend_locations = read_input(argv[0])
                    optimal_solution = eval(solution + '(n, q, node_connection_list, friend_locations)')

                    print("Program started with", solution, "for", argv[0])
                    start = time.time()  # start
                    total = 0
                    for vertex, distances in optimal_solution.run():
                        # stop
                        end = time.time()
                        total += (end - start)
                        # print(vertex, distances[0], distances[1], distances[2])
                        # start
                        start = time.time()
                    print(f'{solution} for {argv[0]} took {total * 1e3} ms')
                    grand_total += total
                except:
                    print("Error in", solution, "skipping...")
            print(f'Grand Total run took {grand_total * 1e3} ms')
        else: # 110925.79817771912 ms
            n, q, node_connection_list, friend_locations = read_input(argv[0])
            # print(n, q, node_connection_list, friend_locations)
            if len(argv) == 1:  # if solution type was not specified, solve with optimal
                optimal_solution = TreeBreadthFirstSearch(n, q, node_connection_list, friend_locations)
            elif len(argv) == 2:  # if solution was specified, solve with that
                solution_input = argv[1]
                if solution_input in solution_list:
                    optimal_solution = eval(solution_input + '(n, q, node_connection_list, friend_locations)')
                else:
                    print("Please specify a correct algorithm")
                    sys.exit(1)
            else:
                print("Too many parameters, please only specify an input file and a correct algorithm!")
                sys.exit(1)

            print("Program started with", argv[1], "for", argv[0])
            start = time.time()  # start
            total = 0
            for vertex, distances in optimal_solution.run():
                # stop
                end = time.time()
                total += (end - start)
                # print(vertex, distances[0], distances[1], distances[2])
                # start
                start = time.time()
            print(f'Total run took {total * 1e3} ms')


if __name__ == "__main__":
    if len(sys.argv) == 1:  # no arguments supplied
        print('Test Mode')
        main(None)
    else:
        main(sys.argv[1:])  # python main.py examples/example1.txt FloydWarshall
