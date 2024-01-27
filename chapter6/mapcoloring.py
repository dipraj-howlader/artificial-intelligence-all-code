import networkx as nx
import matplotlib.pyplot as plt

# Modified dataset where each node has relationships with at most two other nodes
dataset = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'F'],
    'F': ['E', 'G'],
    'G': ['F'],
}

# Create a graph from the modified dataset
G = nx.Graph(dataset)

# Perform graph coloring with constraints
color_map = {}

# Sort nodes by degree in descending order
nodes_sorted = sorted(G.nodes, key=lambda x: G.degree(x), reverse=True)

# Color nodes while respecting constraints
for node in nodes_sorted:
    used_colors = set(color_map[neighbor] for neighbor in G.neighbors(node) if neighbor in color_map)
    available_colors = set(range(len(nodes_sorted))) - used_colors
    color_map[node] = min(available_colors)

# Plot the graph with assigned colors
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color=list(color_map.values()), cmap=plt.cm.rainbow)
plt.show()
