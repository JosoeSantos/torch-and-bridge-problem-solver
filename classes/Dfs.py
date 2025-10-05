# Implementação do DFS para encontrar o caminho em um grafo
def dfs(graph, start):
    visited = set()
    stack = [start]
    predecessor = {start: None}

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for edge in graph.get(vertex, []):
                neighbor = edge.v
                if neighbor not in visited:
                    stack.append(neighbor)
                    predecessor[neighbor] = vertex
    return predecessor


# Reconstrói o caminho do vértice start até end.
def dfs_path_reconstruct_path(predecessor, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessor.get(current)
    path.reverse()
    return path if path[0] == start else []