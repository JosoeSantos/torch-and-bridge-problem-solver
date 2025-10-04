'''
Plots a graph using plotly.
'''

from TAD import Graph
import plotly.graph_objects as go
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class GraphPlotter:
    def __init__(self, graph: Graph):
        self.graph = graph

    def plot(self):
        edges = self.graph.get_edges()
        G_nx = nx.DiGraph()  # Directed graph

        for edge in edges:
            print("adding edge", edge)
            G_nx.add_edge(edge.u, edge.v, weight=edge.w)

        nx.draw(G_nx, with_labels=True, node_color='lightblue', arrows=False, pos=nx.spring_layout(G_nx, method="energy"))
        plt.draw()
        plt.show()
        