import heapq
from graph.Graph import Graph
from collections import defaultdict as dd


class Edge:

    def __init__(self, s, d, w):
        self.s = s
        self.d = d
        self.w = w

    def __lt__(self, other):
        return self.w < other.w

    def __gt__(self, other):
        return self.w > other.w


def prims(g: Graph):
    start = list(g.nodes.keys())[0]
    visits = set()
    visits.add(start)
    pq = []
    edge_map = dict()
    temp = start
    final = dd(lambda: dd(lambda: 0))
    dist = 0
    while len(visits) != g.n:
        neighbours = g.nodes[temp].neighbours
        for k, v in neighbours.items():
            edge_map.setdefault(k, Edge(temp, k, v))
            edge = edge_map[k]
            heapq.heappush(pq, edge)

        edge = heapq.heappop(pq)
        while edge.d in visits:
            edge = heapq.heappop(pq)
        visits.add(edge.d)
        temp = edge.d
        final[edge.s][edge.d] = edge.w
        dist += edge.w

    return final, dist








