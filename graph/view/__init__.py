from collections import deque
from graph.view.topo_sort import topological_sort


def bfs(g, start):

    visits = deque([])
    storage = deque([])

    visits.append(start)
    storage.append(start)

    while len(storage) != 0:
        e = storage.popleft()
        neighbours = g.nodes[e].neighbours
        for neighbour in neighbours:
            if neighbour not in visits:
                visits.append(neighbour)
                storage.append(neighbour)

    return visits


def dfs(g, start):
    visits = deque([])
    storage = deque([])

    visits.append(start)
    storage.append(start)

    while len(storage) != 0:
        e = storage.pop()
        neighbours = g.nodes[e].neighbours
        for neighbour in neighbours:
            if neighbour not in visits:
                visits.append(neighbour)
                storage.append(neighbour)

    return visits

