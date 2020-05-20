from collections import defaultdict as dd


class Node:
    def __init__(self, node, depth=0, parent=None):
        self.id = node
        self.neighbours = dd(lambda: 0)
        self.depth = depth
        self.parent = parent

    def add_neighbours(self, v2, w):
        self.neighbours[v2] = w


class Graph:

    def __init__(self, directed=True):

        self.nodes = dd(lambda: Node(-1))
        self.n = 0
        self.directed = directed

    def add_vertex(self, node):
        self.n += 1
        self.nodes[node] = Node(node)

    def add_edge(self, f, t, w):
        if f not in self.nodes:
            self.add_vertex(f)

        if t not in self.nodes:
            self.add_vertex(t)

        if w:
            self.nodes[f].add_neighbours(t, w)
            if not self.directed:
                self.nodes[t].add_neighbours(f, w)

    def adjacency_list(self):
        d = dd(lambda: dd(lambda: None))
        for ver in self.nodes:
            v = self.nodes[ver].neighbours
            d[ver] = v

        return d

    def adjacency_matrix(self):
        am = dict()
        for ver in self.nodes:
            am.setdefault(ver, dict())
            nbrs = self.nodes[ver].neighbours
            for v2 in self.nodes:
                if ver != v2:
                    am[ver].setdefault(v2, float('inf'))
                    if v2 in nbrs:
                        am[ver][v2] = self.nodes[ver].neighbours[v2]
                else:
                    am[ver].setdefault(v2, 0)

        return am



