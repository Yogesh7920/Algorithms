from collections import deque
import pprint


class Flow:

    def __init__(self, g, source, sink):
        self.g = g
        self.source = source
        self.sink = sink

    def dfs(self):
        visits = deque([])
        storage = deque([])
        mn = float('inf')
        start, end = self.source, self.sink
        visits.append(start)
        storage.append(start)

        while len(storage) != 0:
            e = storage.pop()
            if e == end:
                break
            neighbours = self.g.nodes[e].neighbours
            for neighbour in neighbours:
                if neighbour not in visits:
                    c = neighbours[neighbour]
                    if c:
                        self.g.nodes[neighbour].parent = self.g.nodes[e]
                        visits.append(neighbour)
                        storage.append(neighbour)

                        if end == neighbour:
                            return

    def update(self, a, val):
        from_ = a[0]
        a.popleft()
        for temp in a:
            from_.neighbours[temp.id] -= val
            temp.neighbours[from_.id] += val
            from_ = temp

    def show_steps(self):
        for node in self.g.nodes:
            c = self.g.nodes[node]
            print('id = ', c.id)
            pprint.pprint(c.neighbours, indent=4)
            print()

    def find_val(self):
        if self.g.nodes[self.sink].parent is None:
            return True, [], 0
        else:
            a = deque([])
            mn = float('inf')
            temp = self.g.nodes[self.sink]
            while not (temp.parent is None):
                a.appendleft(temp)
                nxt = temp.parent
                c = nxt.neighbours[temp.id]
                mn = min(mn, c)
                temp = nxt

            self.g.nodes[self.sink].parent = None

            return False, a, mn

    def max_flow(self):
        max_val = 0
        while True:
            self.dfs()
            done, a, bottleneck = self.find_val()
            if done:
                break
            self.update(a, bottleneck)
            max_val += bottleneck

        return max_val
