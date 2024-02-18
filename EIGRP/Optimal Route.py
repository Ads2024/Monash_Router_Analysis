import networkx as nx
import matplotlib.pyplot as plt

# Recreate the directed graph
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

# Define the routes to highlight without adding them as edges to avoid clutter
highlight_routes = {
    ("R1", "R2"): {"color": "red", "style": "solid"},
    ("R1", "R3"): {"color": "green", "style": "dashed", "via": "R2"},
    ("R1", "R4"): {"color": "green", "style": "dashed", "via": "R2"},
    ("R2", "R1"): {"color": "red", "style": "solid"},
    ("R2", "R4"): {"color": "red", "style": "solid"},
    ("R2", "R3"): {"color": "red", "style": "solid"},
    ("R3", "R2"): {"color": "red", "style": "solid"},
    ("R3", "R1"): {"color": "green", "style": "dashed", "via": "R2"},
    ("R3", "R4"): {"color": "green", "style": "dashed", "via": "R2"},
    ("R4", "R2"): {"color": "red", "style": "solid"},
    ("R4", "R1"): {"color": "green", "style": "dashed", "via": "R2"},
    ("R4", "R3"): {"color": "green", "style": "dashed", "via": "R2"}
}

# Generate positions for each node
pos = nx.circular_layout(G)

# Draw the graph
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=20, font_weight="bold", alpha=0.5)

# Highlight the specified routes
for route, properties in highlight_routes.items():
    if 'via' in properties:
        intermediate = properties['via']
        # Draw the path to the intermediate node
        nx.draw_networkx_edges(G, pos, edgelist=[(route[0], intermediate)], edge_color=properties['color'], style=properties['style'])
        # Draw the path from the intermediate node to the target
        nx.draw_networkx_edges(G, pos, edgelist=[(intermediate, route[1])], edge_color=properties['color'], style=properties['style'])
    else:
        # Draw the direct route
        nx.draw_networkx_edges(G, pos, edgelist=[route], edge_color=properties['color'], width=2)

# Title and show
plt.title("Highlighted Routes Map", size=15)
plt.show()
