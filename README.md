# Problema do caminho mais curto em um grafo

## Como executar

1. Crie o ambiente virtual digitando o seguinte comando no terminal: ```python -m venv venv```.
2. Ative o ambiente virtual digitando o seguinte comando no terminal: ```source venv/bin/activate```.
3. Instale as dependências digitando o seguinte comando no terminal: ```pip install -r requirements.txt```.
4. Para executar digite ```python src/main.py```.

## Fluxo de execução

1. É dado ao usuário a possibilidade de escolher o número de nós que ele quer e também a probabilidade de gerar uma aresta entre um nó e outro.

2. É criado o grafo com a função abaixo:

```python
def create_random_graph(num_nodes, prob_edge, min_weight=1, max_weight=10):
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() < prob_edge:
                weight = random.randint(min_weight, max_weight)
                G.add_edge(i, j, weight=weight)
    return G
```

3. Após criar o grafo, o programa entra em um loop que dá ao usuário a possibilidade de escolher o nó de começo e o nó de chegada, para posteriormente executar o caminhamento.

4. Escolhendo o nó de chegada e o nó de chegada, deve ser escolhido o algoritmo para executar o caminhamento no grafo, sendo eles: 
    - **Busca em largura (BFS)** 
    - **Busca em profundidade (DFS)**
    - **A-estrela com eurística Euclidiana**
    - **A-estrela com eurística Manhattan**

5. Caso as opções de **A-estrela** sejam escolhidas, as heurísticas são definidas com bases nas funções abaixo:

```python
def heuristic_manhattan(node, goal):
        return abs(node - goal)

def heuristic_euclidean(node, goal):
        return (node - goal) ** 2
```

6. A função que executa o algoritmo A* é a seguinte abaixo:

```python
def a_star_search(G, start, goal, heuristic):
    open_set = [(0, start)] # Fila de prioridade contendo o custo estimado (f_score) e o nó
    came_from = {} # Dicionário para armazenar o caminho
    g_score = {node: float('inf') for node in G.nodes()} # Custo acumulado para chegar a cada nó
    g_score[start] = 0 # Custo para chegar ao nó inicial é zero
    f_score = {node: float('inf') for node in G.nodes()} # Custo estimado total para chegar ao objetivo
    f_score[start] = heuristic(start, goal) # Estima o custo inicial (heurística) do nó inicial ao objetivo

    while open_set: # Enquanto houver nós para explorar
        _, current = heapq.heappop(open_set) # Retira o nó com o menor f_score da fila de prioridade
        
        if current == goal: # Se o nó atual é o objetivo, retorna o caminho encontrado
            return reconstruct_path(came_from, current)

        for neighbor in G.neighbors(current): # Para cada vizinho do nó atual
            tentative_g_score = g_score[current] + G[current][neighbor]['weight'] # Calcula o g_score temporário

            if tentative_g_score < g_score[neighbor]: # Se o custo acumulado atual for menor
                came_from[neighbor] = current # Atualiza o caminho
                g_score[neighbor] = tentative_g_score # Atualiza o g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal) # Atualiza o f_score (g_score + heurística)
                heapq.heappush(open_set, (f_score[neighbor], neighbor)) # Adiciona o vizinho na fila de prioridade

    return None # Retorna None se não encontrar um caminho
```

7. A função que executa o algoritmo BFS é a seguinte abaixo:

```python
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
```

8. A função que executa o algoritmo DFS é a seguinte abaixo:

```python
def dfs_search(G, start, goal):
    stack = [start]  # Inicializa a pilha com o nó inicial
    came_from = {}  # Dicionário para registrar de onde veio cada nó
    visited = set() # Conjunto de nós já visitados

    while stack:  # Enquanto houver nós na pilha para serem explorados
        current = stack.pop() # Remove o nó do topo da pilha para ser o nó atual
        if current == goal:  # Verifica se o nó atual é o objetivo
            return reconstruct_path(came_from, current) # Reconstrói o caminho até o objetivo
        
        if current not in visited: # Se o nó ainda não foi visitado
            visited.add(current) # Marca o nó como visitado
            for neighbor in G.neighbors(current): # Explora todos os vizinhos do nó atual
                if neighbor not in visited: # Se o vizinho ainda não foi visitado
                    came_from[neighbor] = current # Marca que chegamos no vizinho a partir do nó atual
                    stack.append(neighbor) # Adiciona o vizinho na pilha para ser explorado
                    
    return None # Se não encontrou o objetivo, retorna None
```

9. Encontrando nó de destino, é feita a reconstrução do grafo para poder ser visualizado o caminho percorrido. Isso é feito com o código abaixo:

```python
def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.insert(0, current)
    return total_path
```

10. Após reconstruir o grafo, o grafo finalmente pode ser visualizado com a função abaixo:

```python
def visualize_graph(G, path=None):
    edges = G.edges(data=True)

    edge_colors = ['black'] * len(G.edges())

    if path:
        edge_list = list(zip(path, path[1:]))
        edge_colors = ['red' if (u, v) in edge_list or (v, u) in edge_list else 'black' for u, v in G.edges()]

    nx.draw(G, nx.spring_layout(G, seed=42), with_labels=True, node_size=200, font_size=10)
    nx.draw_networkx_edge_labels(G, nx.spring_layout(G, seed=42), edge_labels={(u, v): f'{d["weight"]}' for u, v, d in edges})
    nx.draw(G, nx.spring_layout(G, seed=42), edgelist=G.edges(), edge_color=edge_colors, width=1)
    
    plt.show()
```