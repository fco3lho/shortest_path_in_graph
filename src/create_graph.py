import networkx as nx
import random

def create_random_graph(num_nodes, prob_edge, min_weight=1, max_weight=10):
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() < prob_edge:
                weight = random.randint(min_weight, max_weight)
                G.add_edge(i, j, weight=weight)
    return G