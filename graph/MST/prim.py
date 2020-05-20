from queue import PriorityQueue as PQ


class Prim:

    def __init__(self, G):
        self.g = G

    def prims(self):
        x = list()
        final = dict()
        am = self.g.adj_matrix()
        vertices = self.g.get_vertices()
        ver = list(vertices)[0]

        weight = 0
        x.append(ver)
        pq = PQ()
        inf = float('inf')
        while self.g.n != len(x):

            for nbr in am[ver]:
                if nbr not in x:
                    t = [am[ver][nbr], ver, nbr]
                    pq.put(t)

            a = pq.get()
            if a[0] == inf:
                print("not spanning tree")
                break
            ver = a[2]
            final.setdefault(a[1], dict())
            final[a[1]].setdefault(ver, inf)
            final[a[1]][ver] = a[0]
            weight += a[0]
            x.append(ver)

        return final, weight







