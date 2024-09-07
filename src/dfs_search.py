from reconstruct_path import reconstruct_path

def dfs_search(G, start, goal):
    stack = [start]
    came_from = {}
    visited = set()
    distance = {start: 0}

    while stack:
        current = stack.pop()
        if current == goal:
            return reconstruct_path(came_from, current), distance[goal]
        
        if current not in visited:
            visited.add(current)
            for neighbor in G.neighbors(current):
                if neighbor not in visited:
                    came_from[neighbor] = current
                    stack.append(neighbor)
                    edge_weight = G[current][neighbor]['weight']
                    distance[neighbor] = distance[current] + edge_weight
                    
    return None