from collections import deque

# def bfs():
#     queue = deque()
#     queue.append(start)
#     father = {tuple(sorted(start[0])) + (start[1],): None}

#     while queue:
#         current = queue.popleft()
#         if current == goal:
#             # Reconstrói caminho
#             path = []
#             cur = current
#             while father[tuple(sorted(cur[0])) + (cur[1],)] is not None:
#                 cur, movers, c = father[tuple(sorted(cur[0])) + (cur[1],)]
#                 path.append((cur, movers, c))
#             path.reverse()
#             return path

#         for novo, movers, c in successors(current):
#             key = tuple(sorted(novo[0])) + (novo[1],)
#             if key not in father:
#                 father[key] = (current, movers, c)
#                 queue.append(novo)
#     return None

def bfs(graph, start):
    """Realiza a busca em largura (BFS) no grafo a partir de start."""
    dist = {vertex: float("inf") for vertex in graph.graph}  # Inicializa as distâncias como infinito
    predecessor = {vertex: None for vertex in graph.graph}  # Predecessor para reconstrução do caminho
    dist[start] = 0  # Distância do nó inicial é 0

    queue = deque([start])  # Fila para a busca em largura

    while queue:
        current_vertex = queue.popleft()
        
        for edge in graph.graph[current_vertex]:
            neighbor = edge.v
            if dist[neighbor] == float("inf"):
                dist[neighbor] = dist[current_vertex] + 1
                predecessor[neighbor] = current_vertex
                queue.append(neighbor)
    
    return dist, predecessor

def reconstruct_path(predecessor, start, end):
    """Reconstrói o caminho do vértice start até end usando o dicionário predecessor."""
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessor[current]
    path.reverse()  # Inverte para obter na ordem correta
    return path if path[0] == start else []  # Retorna caminho válido ou vazio