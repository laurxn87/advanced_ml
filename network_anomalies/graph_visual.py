import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import graphviz

# import the graph data from sniff.py
packets_data_graph = nx.read_gexf("packets_graph.gexf")

# visualise the directed graph using matplotlib
plt.figure(figsize=(12, 8))
# Use a spring layout for better visualization - needs to be very spread out to avoid overlapping nodes
pos = nx.spring_layout(packets_data_graph, k=0.5, iterations=50)

# highlight the nodes with the highest degree centrality
degree_centrality = nx.degree_centrality(packets_data_graph)
# get the top node with the highest degree centrality
top_node = max(degree_centrality, key=degree_centrality.get)

print(f"Top node with highest degree centrality: {top_node} (Centrality: {degree_centrality[top_node]:.4f})")
# highlight the top node in red
node_colors = ['red' if node == top_node else 'lightblue' for node in packets_data_graph.nodes()]
nx.draw(packets_data_graph, pos, with_labels=True, node_size=500, node_color=node_colors, font_size=10, font_weight='bold', arrowsize=20)
edge_labels = nx.get_edge_attributes(packets_data_graph, 'weight')
nx.draw_networkx_edge_labels(packets_data_graph, pos, edge_labels=edge_labels, font_size=8)
plt.title(f"Directed Graph of Packet Flows (Top Node: {top_node})")
plt.axis('off')
plt.show()

# Draw edge labels (weights)
edge_labels = nx.get_edge_attributes(packets_data_graph, 'weight')
nx.draw_networkx_edge_labels(packets_data_graph, pos, edge_labels=edge_labels, font_size=8)

plt.title("Directed Graph of Packet Flows")
plt.axis('off')
plt.show()
