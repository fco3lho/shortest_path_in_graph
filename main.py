import os

from create_graph import create_random_graph
from a_star import a_star_search, heuristic_euclidean, heuristic_manhattan
from bfs_search import bfs_search
from dfs_search import dfs_search
from visualize_graph import visualize_graph

# Configurações do grafo
num_nodes = int(input("Insira o número de nós do grafo: "))
prob_edge = 0.5

# Criação do grafo
G = create_random_graph(num_nodes, prob_edge)

while True:
    os.system('clear')

    # Definindo os nós de início e fim
    start_node = int(input(f"Insira o nó de começo (De 0 à {num_nodes - 1}): "))
    goal_node = int(input(f"Insira o nó de chegada (De 0 à {num_nodes - 1}): "))

    os.system('clear')

    print('''
        Menu

        1. Digite 1 para executar o algoritmo BFS no grafo criado.
        2. Digite 2 para executar o algoritmo DFS no grafo criado.
        3. Digite 3 para executar o algoritmo A* com eurística Euclidiana no grafo criado.
        4. Digite 4 para executar o algoritmo A* com eurística Manhattan no grafo criado.

    ''')

    opt = int(input("Digite sua opção: "))

    if opt == 1:
        path = bfs_search(G, start_node, goal_node)
    
    if opt == 2:
        path = dfs_search(G, start_node, goal_node)

    if opt == 3:
        path = a_star_search(G, start_node, goal_node, heuristic_manhattan)

    if opt == 4:
        path = a_star_search(G, start_node, goal_node, heuristic_euclidean)

    # Visualizando o grafo e o caminho encontrado
    if path:
        print("Caminho encontrado:", path)
        visualize_graph(G, path)
    else:
        print("Caminho não encontrado.")
