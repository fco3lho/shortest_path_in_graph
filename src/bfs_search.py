from reconstruct_path import reconstruct_path
from collections import deque

def bfs_search(G, start, goal):
    queue = deque([start])
    came_from = {start: None}
    
    while queue:
        current_node = queue.popleft()
        
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            return path[::-1]
        
        for neighbor in G.neighbors(current_node):
            if neighbor not in came_from:
                queue.append(neighbor)
                came_from[neighbor] = current_node
    
    return None