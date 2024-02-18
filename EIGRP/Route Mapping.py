import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_node("R1")
G.add_node("R2")
G.add_node("R3")
G.add_node("R4")

# Add direct routes as edges
G.add_edge("R1", "R2")
G.add_edge("R1", "R3")
G.add_edge("R1", "R4")
G.add_edge("R2", "R1")
G.add_edge("R2", "R3")
G.add_edge("R2", "R4")
G.add_edge("R3", "R1")
G.add_edge("R3", "R2")
G.add_edge("R4", "R1")
G.add_edge("R4", "R2")

# Add routes via intermediate nodes as paths (not directly as edges to avoid cluttering the graph with too many edges)
# For example, "R1 to R2 via R3" is represented by the path R1 -> R3 -> R2, which is implicitly represented by the edges R1 -> R3 and R3 -> R2.

# Draw the graph
plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_size=2000, node_color="skyblue", font_size=20, font_weight="bold")
plt.title("Link Map of Possible Routes", size=15)
plt.show()
