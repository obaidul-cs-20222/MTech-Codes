import networkx as nx
import matplotlib.pyplot as plt
import math
import random

# Number of nodes in the graph
n = 4

# Generating random points
points = {i: (random.uniform(0, 10), random.uniform(0, 10)) for i in range(n)}

#graph creation
G = nx.Graph()


G.add_nodes_from(points.keys())

# Add weighted edges using Euclidean distance
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        weight = math.dist((x1, y1), (x2, y2))
        G.add_edge(i, j, weight=round(weight, 2))

mst = nx.minimum_spanning_tree(G)

pos = points
nx.draw(G, pos, with_labels=True, node_color="lightblue",
        node_size=500, edge_color="gray")


edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Complete Weighted Graph (Triangle Inequality Satisfied)")
plt.show()

# Draw MST
nx.draw(mst, pos, with_labels=True, node_color="lightgreen",
        node_size=500, edge_color="red", width=2)


mst_labels = nx.get_edge_attributes(mst, "weight")
mst_labels = {k: round(v, 2) for k, v in mst_labels.items()}
nx.draw_networkx_edge_labels(mst, pos, edge_labels=mst_labels)

plt.title("Minimum Spanning Tree (MST)")
plt.show()

multi = nx.MultiGraph()
multi.add_nodes_from(mst.nodes())
for u, v, data in mst.edges(data=True):
    multi.add_edge(u, v, weight=data["weight"])
    multi.add_edge(u, v, weight=data["weight"])

# Euler tour
euler_tour = list(nx.eulerian_circuit(multi))

# Shortcut tour
visited = set()
tsp_path = []

for u, v in euler_tour:
    if u not in visited:
        tsp_path.append(u)
        visited.add(u)

# return to start
tsp_path.append(tsp_path[0])

tsp_length = sum(
    G[tsp_path[i]][tsp_path[i+1]]["weight"]
    for i in range(len(tsp_path) - 1)
)

#Visualization pf final TSP tour
plt.figure(figsize=(8, 6))
pos = points


nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=500)


tsp_edges = [(tsp_path[i], tsp_path[i+1]) for i in range(len(tsp_path)-1)]
nx.draw_networkx_edges(G, pos, edgelist=tsp_edges,
                       edge_color="red", width=2)


nx.draw_networkx_labels(G, pos)

plt.title(f"Twice-Around-the-Tree TSP Tour\nTotal length = {tsp_length:.2f}")
plt.axis("off")
plt.show()

# Output tour
print("TSP Tour:", tsp_path)
print("Tour Length:", round(tsp_length, 2))