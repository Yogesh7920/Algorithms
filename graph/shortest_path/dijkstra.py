from queue import PriorityQueue as PQ


def dijkstra(g, s, e):
    pq = PQ()

    d = dict()
    final = dict()
    inf = float('inf')
    vertices = g.nodes
    for ver in vertices:
        d.setdefault(ver, inf)

    d[s] = 0.0

    for (k, v) in d.items():
        pq.put((v, k))

    while not pq.empty():

        dis, v = pq.get()
        if v == e:
            break
        ver = vertices[v]
        nbrs = ver.neighbour
        for (nbr, w) in nbrs.items():
            if d[nbr] > d[v] + w:
                d[nbr] = d[v] + w

        final[v] = d[v]
        del d[v]

        pq = PQ()
        for (k, v) in d.items():
            pq.put((v, k))

    return d[e]