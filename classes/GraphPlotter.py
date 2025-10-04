"""
Plots a graph using plotly.
"""

from TAD import Graph
import plotly.graph_objects as go
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import plotly.express as px
from matplotlib import animation



class GraphPlotter:
    """
    Plots a graph using matplotlib and nx.
    Supports 2D and 3D plotting.
    Steps to use:
    1. Create an instance of GraphPlotter with a Graph object.
    2. Call create_2d_layout() or create_3d_layout() to setup the layout.
    3. Call plot_2d() or plot_3d()
    4. Optionally, call color_path(path) to highlight a specific path.
    5. Call show() to display the plot.
    """
    def __init__(self, graph: Graph, dim=2, pretty=True):
        self.graph = graph
        self.G = nx.DiGraph()  # Directed graph
        self.pos = None
        self.pretty = pretty
        self.fig = plt.figure()


    def create_nx_layout(self, dim=2):
        edges = self.graph.get_edges()

        nodes = self.graph.graph.keys()
        for node in nodes:
            self.G.add_node(node, label=self.pretty_vertex(node))

        for edge in edges:
            self.G.add_edge(
                edge.u,
                edge.v,
                weight=edge.w,
            )
        self.pos = nx.spring_layout(self.G, seed=42, dim=dim)
        
    def color_path(self, path, color="r"):
        edge_list = [(u, v) for u, v in zip(path, path[1:])]
        nx.draw_networkx_edges(
            self.G,
            edgelist=edge_list,
            edge_color=color,
            width=2.5,
            pos=self.pos,
        )

    def pretty_vertex(self, v):
        """Converts vertex from format '[010|1]' to integer 2."""
        if self.pretty is False:
            return v
        code, torch = v.strip("[]").split("|")
        vertex_code = str(int(code, 2)) + '/' + torch
        return vertex_code

    def plot_2d(self):
        nx.draw(
            self.G,
            with_labels=True,
            node_color="lightblue",
            arrows=False,
            pos=self.pos,
            labels={node: self.pretty_vertex(node) for node in self.G.nodes()}   
        )

    def show(self):
        plt.draw()
        plt.show()


    def plot_3d(self):
        pos = nx.spring_layout(self.G, seed=42, dim=3)

        for node, data in self.G.nodes(data=True):
            data["label"] = str(node)
            data['color'] = 'lightblue'

        edge_x = []
        edge_y = []
        edge_z = []
        for edge in self.G.edges():
            x0, y0, z0 = pos[edge[0]]
            x1, y1, z1 = pos[edge[1]]
            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)
            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)
            edge_z.append(z0)
            edge_z.append(z1)
            edge_z.append(None)

        pos = nx.spectral_layout(self.G, dim=3)
        nodes = np.array([pos[v] for v in self.G])
        edges = np.array([(pos[u], pos[v]) for u, v in self.G.edges()])

        ax = self.fig.add_subplot(111, projection="3d")
        self.fig.tight_layout()

        def init():
            ax.clear()
            ax.scatter(*nodes.T, alpha=0.2, s=100, color="blue")
            for vizedge in edges:
                ax.plot(*vizedge.T, color="gray")
            ax.grid(False)
            ax.set_axis_off()


        # ani = animation.FuncAnimation(
        #     fig,
        #     _frame_update,
        #     init_func=init,
        #     interval=50,
        #     cache_frame_data=False,
        #     frames=100,
        # )

        init()

