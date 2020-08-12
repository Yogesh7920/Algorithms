from graph.Graph import Graph
from graph.MST.prim import prims
import os

input_file = "graph_input/complete.txt"
g = Graph(directed=False)
if os.path.exists(input_file):

    with open(input_file, "r") as f:
        a = f.readlines()

    for line in a:
        s, t, w = line.split()
        g.add_edge(s, t, w)

    print(prims(g))
else:
    print(os.getcwd())
    print('Not Available')



