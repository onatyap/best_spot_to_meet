from data_structures.graph import Graph


class BestSpotToMeetAbstractSolution:
    def __init__(self, n: int, q: int, node_connection_list: list, friend_locations: list):  # input parameters and initialization

        self.n = n
        self.q = q
        self.node_connection_list = node_connection_list
        self.friend_locations = friend_locations

        self.graph = Graph()

    def graph_construction(self):  # adj_list -> graph construction
        pass

    def cost_calculation(self):  # cost calculation
        pass

    def solve(self, day):  # solution
        pass

    def run(self):
        self.graph_construction()
        self.cost_calculation()
        for day in range(self.q):
            yield self.solve(day)
