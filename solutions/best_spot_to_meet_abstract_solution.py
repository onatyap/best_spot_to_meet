from data_structures.graph import Graph


class BestSpotToMeetAbstractSolution:
    def __init__(self, n, q, adj_list, friend_locations):   # input parameters and initialization

        self.n = n
        self.q = q
        self.adj_list = adj_list
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
