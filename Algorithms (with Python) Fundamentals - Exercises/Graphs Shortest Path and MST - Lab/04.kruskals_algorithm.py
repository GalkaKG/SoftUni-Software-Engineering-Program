class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


edges = int(input())
graph = []

max_node = float('-inf')
for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(', ')]
    graph.append(Edge(first, second, weight))
    max_node = max(first, second, max_node)

parent = [num for num in range(max_node + 1)]
forest = []
for edge in sorted(graph, key=lambda e: e.weight):
    first_node_root = find_root(parent, edge.first)
    second_node_root = find_root(parent, edge.second)
    if first_node_root != second_node_root:
        parent[first_node_root] = second_node_root
        forest.append(edge)

for edge in forest:
    print(f'{edge.first} - {edge.second}')
