import os

import time

import networkx as nx
from create_graph import create_random_graph
from a_star import a_star_search
from a_star import heuristic_euclidean
from a_star import heuristic_manhattan
from bfs_search import bfs_search
from dfs_search import dfs_search
from visualize_graph import visualize_graph

# Configurações do grafo
num_nodes = int(input("Insira o número de nós do grafo: "))
prob_edge = float(input("Insira a probabilidade de gerar arestas, sendo medida de 0 a 1: "))

# Criação do grafo
G = create_random_graph(num_nodes, prob_edge)
pos = nx.spring_layout(G)

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
        3. Digite 3 para executar o algoritmo A* com eurística Manhattan adaptada no grafo criado.
        4. Digite 4 para executar o algoritmo A* com eurística Euclidiana adaptada no grafo criado.

    ''')

    opt = int(input("Digite sua opção: "))

    if opt == 1:
        # Inicia contagem de tempo
        start_time = time.time()

        ##### Executa BFS
        path = bfs_search(G, start_node, goal_node)

        # Termina contagem de tempo
        end_time = time.time()
        elapsed_time = end_time - start_time

        print("\nTempo de execução em segundos:", elapsed_time)
    
    if opt == 2:
        # Inicia contagem de tempo
        start_time = time.time()

        ##### Executa DFS
        path = dfs_search(G, start_node, goal_node)

        # Termina contagem de tempo
        end_time = time.time()
        elapsed_time = end_time - start_time

        print("\nTempo de execução em segundos:", elapsed_time)

    if opt == 3:
        # Inicia contagem de tempo
        start_time = time.time()

        ##### Executa A* Manhattan
        path = a_star_search(G, start_node, goal_node, pos, heuristic_manhattan)

        # Termina contagem de tempo
        end_time = time.time()
        elapsed_time = end_time - start_time

        print("\nTempo de execução em segundos:", elapsed_time)

    if opt == 4:
        # Inicia contagem de tempo
        start_time = time.time()

        ##### Executa A* Euclidean
        path = a_star_search(G, start_node, goal_node, pos,heuristic_euclidean)

        # Termina contagem de tempo
        end_time = time.time()
        elapsed_time = end_time - start_time

        print("\nTempo de execução em segundos:", elapsed_time)

    # Visualizando o grafo e o caminho encontrado
    if path:
        print("Número de nós explorados:", len(path[0]))
        print("Distância percorrida: ", path[1])
        print("Caminho encontrado:", path[0])
        visualize_graph(G, path[0])
    else:
        print("Caminho não encontrado.")
