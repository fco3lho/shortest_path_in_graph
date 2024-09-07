from reconstruct_path import reconstruct_path
import heapq
import math

def heuristic_manhattan(pos, node, goal):
    x1, y1 = pos[node]
    x2, y2 = pos[goal]
    return abs(x1 - x2) + abs(y1 - y2)

def heuristic_euclidean(pos, node, goal):
    x1, y1 = pos[node]
    x2, y2 = pos[goal]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def a_star_search(G, start, goal, pos, heuristic):
    open_set = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in G.nodes()}
    g_score[start] = 0
    f_score = {node: float('inf') for node in G.nodes()}
    print(f"Start: {pos[start]}")
    f_score[start] = heuristic(pos, start, goal)

    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            return reconstruct_path(came_from, current), g_score[current]

        for neighbor in G.neighbors(current):
            tentative_g_score = g_score[current] + G[current][neighbor]['weight']

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(pos, neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None