import os

import time

from create_graph import create_random_graph
from a_star import a_star_search
from a_star import heuristic_euclidean
from a_star import heuristic_manhattan
from bfs_search import bfs_search
from dfs_search import dfs_search
from visualize_graph import visualize_graph

# Configurações do grafo
# num_nodes = int(input("Insira o número de nós do grafo: "))
# prob_edge = float(input("Insira a probabilidade de gerar arestas, sendo medida de 0 a 1: "))
num_nodes = 100
prob_edge = 0.4

# Criação do grafo
# G = create_random_graph(num_nodes, prob_edge)

i = 0;

average_time_execution = 0
average_distance = 0
average_nodes_exploreds = 0

while (i < 50):
    os.system('clear')

    G = create_random_graph(num_nodes, prob_edge)

    # Definindo os nós de início e fim
    # start_node = int(input(f"Insira o nó de começo (De 0 à {num_nodes - 1}): "))
    # goal_node = int(input(f"Insira o nó de chegada (De 0 à {num_nodes - 1}): "))
    start_node = 0
    goal_node = 99

    os.system('clear')

    print('''
        Menu

        1. Digite 1 para executar o algoritmo BFS no grafo criado.
        2. Digite 2 para executar o algoritmo DFS no grafo criado.
        3. Digite 3 para executar o algoritmo A* com eurística Euclidiana no grafo criado.
        4. Digite 4 para executar o algoritmo A* com eurística Manhattan no grafo criado.

    ''')

    # opt = int(input("Digite sua opção: "))
    opt = 4

    if opt == 1: # BFS
        # Inicia contagem de tempo
        start_time = time.time()

        ##### Executa BFS
        path = bfs_search(G, start_node, goal_node)

        # Termina contagem de tempo
        end_time = time.time()
        elapsed_time = end_time - start_time

        # print("\nTempo de execução em segundos:", elapsed_time)
        average_time_execution += elapsed_time
    
    if opt == 2: # DFS
        # Inicia contagem de tempo
        start_time = time.time()

        ##### Executa DFS
        path = dfs_search(G, start_node, goal_node)

        # Termina contagem de tempo
        end_time = time.time()
        elapsed_time = end_time - start_time

        # print("\nTempo de execução em segundos:", elapsed_time)
        average_time_execution += elapsed_time

    if opt == 3: # A* Manhattan
        # Inicia contagem de tempo
        start_time = time.time()

        ##### Executa A* Manhattan
        path = a_star_search(G, start_node, goal_node, heuristic_manhattan)

        # Termina contagem de tempo
        end_time = time.time()
        elapsed_time = end_time - start_time

        # print("\nTempo de execução em segundos:", elapsed_time)
        average_time_execution += elapsed_time

    if opt == 4: # A* Euclidean
        # Inicia contagem de tempo
        start_time = time.time()

        ##### Executa A* Euclidean
        path = a_star_search(G, start_node, goal_node, heuristic_euclidean)

        # Termina contagem de tempo
        end_time = time.time()
        elapsed_time = end_time - start_time

        # print("\nTempo de execução em segundos:", elapsed_time)
        average_time_execution += elapsed_time

    # Visualizando o grafo e o caminho encontrado
    if path:
        # print("Número de nós explorados:", len(path[0]))
        # print("Distância percorrida: ", path[1])
        # print("Caminho encontrado:", path[0])
        # visualize_graph(G, path[0])
        average_nodes_exploreds += len(path[0])
        average_distance += path[1]
    else:
        print("Caminho não encontrado.")

    i+=1

print(f"Média de nós explorados para 50 execuções: {average_nodes_exploreds/50}")
print(f"Média de distância percorrida para 50 execuções: {average_distance/50}")
print(f"Média de tempo de execução 50 execuções: {average_time_execution/50}")