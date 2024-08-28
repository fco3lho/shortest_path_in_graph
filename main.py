from create_graph import create_random_graph
from a_star import a_star_search
from bfs_search import bfs_search
from dfs_search import dfs_search
from visualize_graph import visualize_graph

# Configurações do grafo
num_nodes = int(input("Insira o número de nós do grafo: "))
prob_edge = 0.5

# Criação do grafo
G = create_random_graph(num_nodes, prob_edge)

while True:
  # Definindo os nós de início e fim
  start_node = int(input(f"Insira o nó de começo (De 0 à {num_nodes - 1}): "))
  goal_node = int(input(f"Insira o nó de chegada (De 0 à {num_nodes - 1}): "))

  # Realizando a busca A*
  path = dfs_search(G, start_node, goal_node)

  # Visualizando o grafo e o caminho encontrado
  if path:
      print("Caminho encontrado:", path)
      visualize_graph(G, path)
  else:
      print("Caminho não encontrado.")
