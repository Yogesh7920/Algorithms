from collections import deque


def topological_sort(g):
    stack = deque([])
    visits = set()
    vertices = g.nodes
    for ver in vertices:
        if ver not in visits:
            loop(vertices, ver, visits, stack)

    stack.reverse()
    return stack


def loop(vertices, ver, visits, stack):
    if ver not in visits:
        visits.add(ver)

    nbrs = vertices[ver].neighbours
    for nbr in nbrs:
        if nbr not in visits:
            loop(vertices, nbr, visits, stack)

    stack.append(ver)
