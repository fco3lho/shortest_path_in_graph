from reconstruct_path import reconstruct_path
from collections import deque

def bfs_search(G, start, goal):
    queue = deque([start])
    came_from = {}
    visited = set()

    while queue:
        current = queue.popleft()
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor in G.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)
                
    return None