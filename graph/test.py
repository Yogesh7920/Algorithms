from graph.Graph import Graph
from graph.flow import Flow


g = Graph()
with open("graph/flow_23.txt", "r") as f:
    a = f.readlines()

for info in a:
    v1, v2, w = info.split()
    g.add_edge(v1, v2, int(w))

flow = Flow(g, '0', '5')
val = flow.max_flow()

print(val)






