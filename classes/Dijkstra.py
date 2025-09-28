# Direto do ED 1
from heapq import heappush, heappop

def dijkstra(graph, start):
    # Initialize the distance of all vertices to infinity
    dist = {vertex: float("inf") for vertex in graph}
    predecessor = {vertex: None for vertex in graph}
    dist[start] = 0  # Distance from start to start is 0
    
    # Initialize the priority queue with the start vertex
    pq = [(0, start)]  # (distance, vertex)
    
    while pq:
        current_dist, current_vertex = heappop(pq)
        
        if current_dist > dist[current_vertex]:
            continue
            
        if current_vertex not in graph:
            continue

        for edge in graph[current_vertex]:
            neighbor = edge.v
            weight = edge.w
            distance = current_dist + weight
            
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                predecessor[neighbor] = current_vertex
                heappush(pq, (distance, neighbor))
    
    return dist, predecessor

# Adicione esta função para uso no teste
def dijkstra_path(graph, start):
    return dijkstra(graph, start)

def reconstruct_path(predecessor, start, end):
    """Reconstrói o caminho do vértice start até end."""
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessor[current]
    path.reverse()  # Inverte para obter na ordem correta
    return path if path[0] == start else []  # Retorna caminho válido ou vazio