from collections import deque
from TAD import Graph, Edge
from Bfs import bfs, reconstruct_path
from Dijkstra import dijkstra, dijkstra_path
from itertools import combinations 
# gera todas as combinações possiveis de um conjunto de elementos

'''
EX do combinations

pessoas = ["A", "B", "C"]

# combinações de 2 pessoas
for par in combinations(pessoas, 2):
    print(par)
    
Output:
('A', 'B')
('A', 'C')
('B', 'C')
'''

# Defines
TIMES = {"A": 1, "B": 2, "C": 5, "D": 10}
ALL = ["A", "B", "C", "D"]

# Estado inicial e objetivo
start = (["A", "B", "C", "D"], "init")
goal = ([], "final")

def cost(movers):
    """Custo da ação = tempo da pessoa mais lenta"""
    bigger = None
    for p in movers:
        if bigger is None or TIMES[p] > bigger:
            bigger = TIMES[p]
    return bigger
    #return max(TIMES[p] for p in movers)
    
def key_state(state): # funcao pra transformar o estado do problema em um vertice do grafo
    left, torch = state
    left_sorted = ",".join(sorted(left)) if left else "∅"
    return f"[{left_sorted}|{torch}]"
    
def successors(state):
    "Gera todos os próximos estados possíveis a partir de um estado"
    left, torch = state
    left = list(left)
    
    if torch == "init":
        # Escolher 1 ou 2 pessoas do lado esquerdo para ir
        for k in (1, 2):
            for movers in combinations(left, k):
                new_left = [p for p in left if p not in movers]
                yield (new_left, "final"), movers, cost(movers) # yeld retorna o valor mas mantem o valor de onde parou

    else:  # tocha está no final
        right = [p for p in ALL if p not in left]
        for k in (1, 2):
            for movers in combinations(right, k):
                new_left = left + list(movers)
                yield (new_left, "init"), movers, cost(movers)

def init_graph():
    G = Graph()
    queue = deque([start])
    visited = {key_state(start): start}
    
    while queue:
        state = queue.popleft()
        u = key_state(state)
        
        for new_state, movers, c in successors(state):
            v = key_state(new_state)
            #print(movers)
            G.add_edge(u, v, c) # adiciona aresta dirigida u -> v com peso "c"
            
            if v not in visited:
                visited[v] = new_state
                queue.append(new_state)
    return G, visited


G, states = init_graph()
#print(G)  # lista as arestas u -> v (custo)
start_v = key_state(start) 
goal_v  = key_state(goal) 

dist, predecessor = bfs(G, start_v)

# Exibir as distâncias mínimas
print("Menores distâncias (número de arestas):", dist)

# Exibir os caminhos para cada nó
path = reconstruct_path(predecessor, start_v, goal_v)

print("Caminho (menor nº de passos):")
print(path if path else "goal não alcançado") # como o bfs n leva em consideração os pesos
# o output n necessariamente sera o caminho otimo


distances = dijkstra(G.graph, start_v)
best_path = dijkstra_path(G.graph, start_v)

print(best_path)