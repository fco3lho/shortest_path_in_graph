from reconstruct_path import reconstruct_path
import heapq

def heuristic_manhattan(node, goal):
    return abs(node - goal)

def heuristic_euclidean(node, goal):
    return (node - goal) ** 2

def a_star_search(G, start, goal, heuristic):
    open_set = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in G.nodes()}
    g_score[start] = 0
    f_score = {node: float('inf') for node in G.nodes()}
    f_score[start] = heuristic(start, goal)

    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            return reconstruct_path(came_from, current), g_score[current]

        for neighbor in G.neighbors(current):
            tentative_g_score = g_score[current] + G[current][neighbor]['weight']

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None