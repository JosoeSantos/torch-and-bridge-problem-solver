from collections import deque
from TAD import Graph, Edge
from Bfs import bfs, reconstruct_path
from Dijkstra import dijkstra, dijkstra_path, reconstruct_path
from itertools import combinations
from array import array
from Dfs import dfs, dfs_path_reconstruct_path
from GraphPlotter import GraphPlotter
from Astar import a_star, path_cost 
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

N = 4  # número de pessoas

def fib_n(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_n(n-1) + fib_n(n-2)

# Defines
TIMES = [1, 2, 5, 10] + [fib_n(i)*10 for i in range(4, N)]  # tempos das pessoas
ALL = ["A", "B", "C", "D"]

# Estado inicial e objetivo
# Essa é a forma mais rápida de representar o estado
# 0 = lado esquerdo, 1 = lado direito
state_start = array("B", [0]) * (N + 1)  # A, B, C, D, tocha
weights = [1, 2, 5, 10, 0] # pesos das arestas

state_goal = array("B", [1]) * (N + 1)  # A, B, C, D, tocha

def cost(movers): #AJ OK
    """Custo da ação = tempo da pessoa mais lenta"""
    bigger = None
    for p, idx in enumerate(movers):
        if bigger is None or TIMES[idx] > bigger:
            bigger = TIMES[idx]
    return bigger
    #return max(TIMES[p] for p in movers)
    
def key_state(state): # AJ: Talvez não use # funcao pra transformar o estado do problema em um vertice do grafo
    people = state[:-1]
    torch = state[-1]

    left_sorted = "".join(str(i) for i in people) if people else "∅"
    return f"[{left_sorted}|{torch}]"
    
def successors(state): # AJ OK
    "Gera todos os próximos estados possíveis a partir de um estado"
    left = [i for i, pos in enumerate(state[:-1]) if pos == 0]
    right = [i for i, pos in enumerate(state[:-1]) if pos == 1]

    if state[-1] == 0:
        # Escolher 1 ou 2 pessoas do lado esquerdo para ir
        for k in (1, 2):
            for movers in combinations(left, k):
                new_state = state[:]
                for m in movers:
                    new_state[m] = 1  # mover para o lado direito
                new_state[-1] = 1  # mover a tocha para o lado direito
                yield new_state, movers, cost(movers) # yeld retorna o valor mas mantem o valor de onde parou

    else:  # tocha está no final
        for k in (1, 2):
            for movers in combinations(right, k):
                new_state = state[:]
                for m in movers:
                    new_state[m] = 0  # mover para o lado esquerdo
                new_state[-1] = 0  # mover a tocha para o lado esquerdo
                yield new_state, movers, cost(movers)

def init_graph():
    G = Graph()
    queue = deque([state_start])
    visited = {key_state(state_start): state_start}

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
start_v = key_state(state_start) 
goal_v  = key_state(state_goal) 

dist, predecessor = bfs(G, start_v)

# Exibir as distâncias mínimas
#print("Menores distâncias (número de arestas):", dist)

# Exibir os caminhos para cada nó
path = reconstruct_path(predecessor, start_v, goal_v)

#print("Caminho (menor nº de passos):")
#print(path if path else "goal não alcançado") # como o bfs n leva em consideração os pesos
# o output n necessariamente sera o caminho otimo


#distances = dijkstra(G.graph, start_v)
distances, pred  = dijkstra_path(G.graph, start_v)
path = reconstruct_path(pred, start_v, goal_v)


cost = distances[goal_v]

print(f"Caminho dijkstra: {path}")
print(f"Custo total: {cost}")

pred = dfs(G.graph, start_v)
path_dfs = dfs_path_reconstruct_path(pred, start_v, goal_v)

print(f"Caminho DFS: {path}")

def astar_heuristic(v):
    state = states[v]
    left = sum(1 for pos in state[:-1] if pos == 0)
    return (left + 1) // 2 * 10  # estimativa otimista

path_a = a_star(G.graph, start_v, goal_v, astar_heuristic)


print(f"Caminho A*: {path}")
print(f"Custo total: {path_cost(G.graph, path)}")

plotter = GraphPlotter(G)
plotter.create_nx_layout()
plotter.plot_2d()
# dijkstra é azul
plotter.color_path(path, color="b")
# astar é verde
plotter.color_path(path_a, color="g")
# dfs é vermelho
plotter.color_path(path_dfs, color="r")
# plotar o grafo
plotter.show()