class Travel:

    def __init__(self, G):
        self.g = G

    def TSP(self, start):
        self.am = self.g.adj_list()
        return self.dist(start, start, set(self.g.nodes).difference({start}))

    def dist(self,start, i, s):
        if s == set():
            return self.am[i][start]
        else:
            return min([(self.am[i][j] + self.dist(start, j, s.difference({j}))) for j in s])



