from graph.Graph import Graph
import os

from graph.flow import flow

input_file = "graph_input/flow_23.txt"
g = Graph()
if os.path.exists(input_file):

    with open(input_file, "r") as f:
        a = f.readlines()

    for line in a:
        s, t, w = line.split()
        g.add_edge(s, t, w)

    print(flow(g, '0', '5'))

else:
    print(os.getcwd())
    print('Not Available')



