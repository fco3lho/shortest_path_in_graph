import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(G, path=None):
    pos = nx.spring_layout(G)
    edges = G.edges(data=True)

    node_colors = ['lightblue' if node not in path else 'lightgreen' for node in G.nodes()]
    edge_colors = ['black'] * len(G.edges())

    if path:
        edge_list = list(zip(path, path[1:]))
        edge_colors = ['red' if (u, v) in edge_list or (v, u) in edge_list else 'black' for u, v in G.edges()]

    nx.draw(G, nx.spring_layout(G, seed=42), with_labels=True, node_color=node_colors, node_size=100, font_size=10)
    nx.draw_networkx_edge_labels(G, nx.spring_layout(G, seed=42), edge_labels={(u, v): f'{d["weight"]}' for u, v, d in edges})
    nx.draw(G, nx.spring_layout(G, seed=42), edgelist=G.edges(), edge_color=edge_colors, width=1)
    
    plt.show()