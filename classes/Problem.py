import time
from array import array
from collections import deque
from itertools import combinations

from Astar import a_star, path_cost
from Bfs import bfs, reconstruct_path
from Dfs import dfs, dfs_path_reconstruct_path
from Dijkstra import dijkstra_path, reconstruct_path
from GraphPlotter import GraphPlotter
from TAD import Graph

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

pred = dfs(G.graph, start_v)
path_dfs = dfs_path_reconstruct_path(pred, start_v, goal_v)

# print(f"Caminho DFS: {path}")

def astar_heuristic(v):
    state = states[v]
    
    people_on_left = [i for i, pos in enumerate(state[:-1]) if pos == 0]
    people_on_right = [i for i, pos in enumerate(state[:-1]) if pos == 1]
    
    # A tocha está no lado esquerdo, então pessoas precisam ir para o lado direito
    if state[-1] == 0:
        # A estimativa é o custo das 2 pessoas mais lentas
        # ou, se apenas uma pessoa resta, o tempo dela.
        # Essa é uma heurística otimista e admissível.
        sorted_times_left = sorted([TIMES[p] for p in people_on_left], reverse=True)
        
        if len(sorted_times_left) == 0:
            return 0
        elif len(sorted_times_left) == 1:
            return sorted_times_left[0]
        else:
            return sorted_times_left[0] + sorted_times_left[1]
    
    # A tocha está no lado direito e precisa voltar para o lado esquerdo
    else:
        # O custo é o tempo da pessoa mais rápida para trazer a tocha
        # de volta.
        if not people_on_right:
            return 0
        
        sorted_times_right = sorted([TIMES[p] for p in people_on_right])
        
        return sorted_times_right[0]

path_a = a_star(G.graph, start_v, goal_v, astar_heuristic)


print(f"Caminho A*: {path}")
print(f"Custo total: {path_cost(G.graph, path)}")

print("-------------------")
print(f"Némero de pessoas: {N}")
# Execução do Dijkstra
start_time_dijkstra = time.time()
distances_dijkstra, pred_dijkstra = dijkstra_path(G.graph, start_v)
end_time_dijkstra = time.time()
dijkstra_duration = end_time_dijkstra - start_time_dijkstra

# Exibir os resultados do Dijkstra
cost_dijkstra = distances_dijkstra[goal_v]
path_dijkstra = reconstruct_path(pred_dijkstra, start_v, goal_v)
print(f"Dijkstra: Caminho encontrado em {dijkstra_duration:.4f} segundos.")
print(f"Custo total (Dijkstra): {cost_dijkstra}")

# Execução do A*
start_time_astar = time.time()
path_a_star = a_star(G.graph, start_v, goal_v, astar_heuristic)
end_time_astar = time.time()
astar_duration = end_time_astar - start_time_astar

# Exibir os resultados do A*
cost_astar = path_cost(G.graph, path_a_star)
print(f"A*: Caminho encontrado em {astar_duration:.4f} segundos.")
print(f"Custo total (A*): {cost_astar}")

plotter = GraphPlotter(G, pretty=False)
plotter.create_nx_layout()
plotter.plot_2d()
# dijkstra é azul
plotter.color_path(path_dijkstra, color="b", width=4.5)
# astar é laranja   
plotter.color_path(path_a_star, color="orange", width=2.5)
# dfs é verde
plotter.color_path(path_dfs, color="g", width=1.5)
# bfs é vermelho
plotter.color_path(path, color="r", width=1.0)
# plotar o grafo
plotter.show()