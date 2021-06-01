import time

DEBUG = False
SEPARATOR_LENGTH = 20

time_passed = 0
problem_count = 0


def debug_test_start(p_name: str, p_count: int):
    if not DEBUG:
        return

    global time_passed, problem_count
    time_passed = time.time()
    problem_count = p_count

    print("="*SEPARATOR_LENGTH)
    print(p_name, "example:", str(p_count))


def debug_test_end():
    if not DEBUG:
        return

    global time_passed
    time_passed = time.time() - time_passed
    print(f'Problem {problem_count} took {time_passed * 1e3} ms')

    print("="*SEPARATOR_LENGTH)
    print()


def debug_test_output(vertex, distances):
    if not DEBUG:
        return

    print("Minimum cost:", vertex, distances)


def debug_cost_matrix(cost_matrix, day):
    if not DEBUG:
        return

    print("\nCost lists for day:", day)
    for cost_list in cost_matrix:
        print(cost_list)
    print()
