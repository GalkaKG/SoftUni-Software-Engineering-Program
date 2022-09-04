from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


def prim(node, graph, forest, forest_edges):
    forest.add(node)

    pq = PriorityQueue()
    for edge in graph[node]:
        pq.put(edge)

    while not pq.empty():
        min_edge = pq.get()
        non_tree_node = -1

        if min_edge.first in forest and min_edge.second not in forest:
            non_tree_node = min_edge.second
        elif min_edge.second in forest and min_edge.first not in forest:
            non_tree_node = min_edge.first

        if non_tree_node == -1:
            continue

        forest.add(non_tree_node)
        forest_edges.append(min_edge)

        for edge in graph[non_tree_node]:
            pq.put(edge)

edges = int(input())

graph = {}

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(', ')]
    if first not in graph:
        graph[first] = []
    if second not in graph:
        graph[second] = []
    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

forest = set()
forest_edges = []

for node in graph:
    if node in forest:
        continue
    prim(node, graph, forest, forest_edges)

for edge in forest_edges:
    print(f'{edge.first} - {edge.second}')
