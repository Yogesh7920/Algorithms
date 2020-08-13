from collections import deque
import pprint
from graph.Graph import Graph

inf = float('inf')


class Node:
    def __init__(self, id, parent):
        self.id = id
        self.parent = parent


def back_track(end: Node):
    temp = end
    final = []
    while temp.parent is not None:
        final.append(temp.id)
        temp = temp.parent

    final.append(temp.id)
    final.reverse()
    return final


def aug_path(nodes, source, sink):
    temp = source

    visits = deque([])
    visits.append(source)

    storage = deque([])
    storage.append(source)

    node_map = dict()
    node_map[source] = Node(source, None)

    while temp not in sink:
        neighbours = nodes[temp].neighbours
        for neighbour in neighbours:
            if neighbour not in visits:
                visits.append(neighbour)
                storage.append(neighbour)
                node_map[neighbour] = Node(neighbour, node_map[temp])

        if len(storage):
            temp = storage.popleft()
        else:
            return False

    path = back_track(node_map[temp])
    return path


def find_critical(nodes, path):
    val = inf
    for i in range(len(path)-1):
        val = min(nodes[path[i]].neighbours[path[i+1]], val)

    return val


def mod_nodes(nodes, path, val):
    for i in range(len(path)-1):
        node1 = path[i]
        node2 = path[i+1]

        if nodes[node1].neighbours[node2] == val:
            nodes[node1].neighbours.pop(node2)
        else:
            nodes[node1].neighbours[node2] -= val

        nodes[node2].neighbours[node1] += val

    return nodes


def flow(g: Graph, source, sink):
    nodes = g.nodes.copy()
    total = 0
    while True:
        aug = aug_path(nodes, source, sink)
        if aug:
            critical = find_critical(nodes, aug)
            nodes = mod_nodes(nodes, aug, critical)
            total += critical
        else:
            break

    return nodes, total



