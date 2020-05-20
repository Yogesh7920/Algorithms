from disjoint_sets import Disjoint as Djs
from queue import PriorityQueue as PQ


class Kruskel:

    def __init__(self, G):
        self.G = G

    def K_MST(self):
        G = self.G.adj_list()
        pq = PQ()
        for node in G:
            for nbr in G[node]:
                l = [G[node][nbr], node, nbr]
                pq.put(l)

        g = dict()
        dj = Djs(G)
        for ver in G:
            g.setdefault(ver, dict())

        wt = 0

        for _ in range(len(G)):
            edge = pq.get()
            w, f, t = edge
            if dj.union(f, t):
                g[f].setdefault(t, 0)
                g[f][t] = w
                wt += w

        return g, wt





