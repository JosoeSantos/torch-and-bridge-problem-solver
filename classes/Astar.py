
def reconstruct_path(came_from, start, goal):
    """Reconstrói o caminho do vértice start até goal."""
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from.get(current)
        if current is None:
            return []  # Retorna caminho vazio se não houver caminho
    path.append(start)
    path.reverse()  # Inverte para obter na ordem correta
    return path

def a_star(graph, start, goal, heuristic):
    from heapq import heappop, heappush

    open_set = []
    heappush(open_set, (0 + heuristic(start), 0, start))  # (f_score, g_score, vertex)
    
    came_from = {}
    g_score = {vertex: float("inf") for vertex in graph}
    g_score[start] = 0
    
    f_score = {vertex: float("inf") for vertex in graph}
    f_score[start] = heuristic(start)
    
    while open_set:
        current_f, current_g, current = heappop(open_set)
        
        if current == goal:
            return reconstruct_path(came_from, start, goal)
        
        if current not in graph:
            continue
        
        for edge in graph[current]:
            neighbor = edge.v
            weight = edge.w
            tentative_g_score = current_g + weight
            
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                heappush(open_set, (f_score[neighbor], tentative_g_score, neighbor))
    
    return []  # Retorna caminho vazio se não houver caminho


def path_cost(graph, path):
    """Calcula o custo total do caminho dado."""
    total_cost = 0
    for u, v in zip(path, path[1:]):
        for edge in graph[u]:
            if edge.v == v:
                total_cost += edge.w
                break
    return total_cost