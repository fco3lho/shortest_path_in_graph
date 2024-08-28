from reconstruct_path import reconstruct_path
from collections import deque

def bfs_search(G, start, goal):
    # Fila para armazenar os nós a serem explorados (FIFO)
    queue = deque([start])
    # Dicionário para armazenar o caminho de volta de cada nó até o início
    came_from = {start: None}
    
    while queue:
        # Extrair o nó atual da fila
        current_node = queue.popleft()
        
        # Se o nó atual for o objetivo, reconstruir o caminho e retorná-lo
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            return path[::-1]  # Retorna o caminho na ordem correta (do início ao objetivo)
        
        # Expandir os nós vizinhos do nó atual
        for neighbor in G.neighbors(current_node):
            if neighbor not in came_from:  # Se o vizinho ainda não foi visitado
                queue.append(neighbor)  # Adicionar o vizinho à fila
                came_from[neighbor] = current_node  # Registrar o caminho de volta
    
    return None  # Se a fila esvaziar e o objetivo não for encontrado, retorna None