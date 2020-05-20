
class Node:
    def __init__(self, data):
        self.data = data
        self.rank = 0
        self.parent = None


class Disjoint:

    def __init__(self, G):
        self.g = G
        self.d = dict()
        self.make_sets()

    def make_sets(self):
        for ver in self.g:
            self.d.setdefault(ver, Node(ver))

    def union(self, a, b):
        r1 = self.d[a]
        r2 = self.d[b]

        while r1.parent != None:
            r1 = r1.parent

        while r2.parent != None:
            r2 = r2.parent

        if r1 == r2:
            return False

        if r1.rank > r2.rank:
            r2.parent = r1
            r1.rank += 1
        else:
            r1.parent = r2
            r2.rank += 1

        return True

    def findset(self, a):
        r = a
        while self.d[r].parent != None:
            r = self.d[r].parent

        self.d[a].parent = self.d[r]

        return r