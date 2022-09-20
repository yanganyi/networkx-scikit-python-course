import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy
from collections import namedtuple
from typing import Optional
import numpy as np
import random

Vertex = namedtuple("Vertex", ["x", "y"])
Edge = namedtuple("Edge", ["origin", "dest", "weight"])

def make_square_graph(n: int, edge_weight: int = 1) -> tuple[list[Vertex], list[Edge]]:
    """
    Generates vertices and edges for a square graph.
    Used for `make_nx_square_graph`
    """
    vertices = []
    edges = []
    for i in range(n):
        for j in range(n):
            vertices.append(Vertex(x=i, y=j))
    for vertex in vertices:
        if vertex.x + 1 < n:
            edges.append(
                Edge(
                    origin=vertex,
                    dest=Vertex(x=vertex.x + 1, y=vertex.y),
                    weight=edge_weight,
                )
            )
        if vertex.y + 1 < n:
            edges.append(
                Edge(
                    origin=vertex,
                    dest=Vertex(x=vertex.x, y=vertex.y + 1),
                    weight=edge_weight,
                )
            )

    return vertices, edges


def create_superhighway(src: Vertex, dst: Vertex) -> Edge:
    """Helper to make an edge with weight 0"""
    return Edge(origin=src, dest=dst, weight=0)


def get_diameter(graph: nx.Graph) -> int:
    """
    Returns the longest of all pairs shortest path lengths.
    This is basically the most inefficient way to do it.
    """
    apsp = dict(nx.all_pairs_dijkstra_path_length(graph))  # O(V) * O(V + E)
    res = []
    for src in apsp.keys():  # O(V)
        res.append(max(apsp[src].values()))  # O(V)
    return max(res)  # O(V)


def make_nx_square_graph(n: int, shw: Optional[Edge] = None) -> nx.Graph:
    graph = nx.Graph()
    vertices, edges = make_square_graph(n)
    graph.add_nodes_from(vertices)
    graph.add_weighted_edges_from(edges)
    if shw:
        graph.add_edge(shw.origin, shw.dest, weight=0, color="r")
    return graph


def draw_nx_graph(g: nx.Graph):
    """Helper utility to visualize the output"""
    plt.figure(figsize=(11, 11))
    _pos = nx.spring_layout(g, pos=nx.random_layout(g, seed=1))
    nx.draw_networkx_edge_labels(
        g, _pos, edge_labels=nx.get_edge_attributes(g, "weight"), font_color="r"
    )
    nx.draw(g, with_labels=True, pos=_pos)
    plt.show()


def make_possible_superhighway_positions(
    vertices: list[Vertex], starting_position: Optional[Vertex] = None
) -> list[Edge]:
    """
    Generates a list of possible superhighway positions,
    given the vertices, and optionally a starting position.

    Time complexity:
        O(V) if `starting_position` is given, else O(V^2)
    """
    result = []
    if starting_position:
        for dst in vertices:
            if starting_position == dst:
                continue
            result.append(create_superhighway(starting_position, dst))
    else:
        for src in vertices:
            for dst in vertices:
                if src == dst:
                    continue
                result.append(create_superhighway(src, dst))
    return result


def argmin(ls: list) -> int:
    return ls.index(min(ls))


def add_shw(g: nx.Graph, shw: Edge) -> nx.Graph:
    """
    Adds a superhighway to a graph.
    This does a deepcopy
    """
    c_g = deepcopy(g)
    c_g.add_edge(shw.origin, shw.dest, weight=0, color="r")
    return c_g


def optim_shw_pos_helper(g: nx.Graph, possible_shw_positions: list[Edge]) -> list[Edge]:
    edges = []
    diameters = []
    for possible_pos in possible_shw_positions:
        c_g = add_shw(g, possible_pos)
        diameter = get_diameter(c_g)
        diameters.append(diameter)
        edges.append(possible_pos)
    result = []
    min_d = min(diameters)
    print("Min diameter:", min_d)
    for e, d in zip(edges, diameters):
        if d == min_d:
            result.append(e)
    return result


def get_optim_shw_pos(n: int, start_pos: Vertex) -> list[Edge]:
    vertices, _ = make_square_graph(n)
    sqg = make_nx_square_graph(n)
    possible_pos = make_possible_superhighway_positions(vertices, start_pos)
    return optim_shw_pos_helper(sqg, possible_pos)


def sub_vert(v1: Vertex, v2: Vertex):
    return v1.x - v2.x, v1.y - v2.y


