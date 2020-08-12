import heapq
from graph.Graph import Graph

inf = float('inf')


class Node:

    def __init__(self, id, dis, parent):
        self.id = id
        self.dis = dis
        self.parent = parent

    def __lt__(self, other):
        return self.dis < other.dis

    def __gt__(self, other):
        return self.dis > other.dis


def route_find(end):
    route = []
    temp = end
    while temp.parent is not None:
        route.append(temp.id)
        temp = temp.parent
    route.append(temp.id)
    route.reverse()
    return route


def dijkstra(g: Graph, start, end):
    start_node = Node(start, 0, None)
    pq = []
    node_map = dict()
    node_map[start] = start_node
    temp = start
    while temp != end:
        neighbours = g.nodes[temp].neighbours
        temp_node = node_map[temp]
        for k, v in neighbours.items():
            node = node_map.get(k, Node(k, inf, None))
            node_map[k] = node
            if node.dis > temp_node.dis + v:
                node.dis = temp_node.dis + v
                node.parent = node_map[temp]
                heapq.heappush(pq, node)

        temp = heapq.heappop(pq).id

    route = route_find(node_map[temp])
    return route, node_map[temp].dis
