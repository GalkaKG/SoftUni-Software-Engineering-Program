# 1-st solution
from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


count_edges = int(input())
graph = {}

for _ in range(count_edges):
    start, end, weight = [int(x) for x in input().split(', ')]
    if start not in graph:
        graph[start] = []
    if end not in graph:
        graph[end] = []
    graph[start].append(Edge(start, end, weight))

start_node = int(input())
end_node = int(input())

max_node = max(graph.keys()) + 1
parent = [None] * max_node
distance = [float('inf')] * max_node

distance[start_node] = 0
pq = PriorityQueue()
pq.put((0, start_node))

while not pq.empty():
    weight, node = pq.get()
    if node == end_node:
        break
    for child in graph[node]:
        new_distance = weight + child.weight
        if new_distance < distance[child.end]:
            distance[child.end] = new_distance
            parent[child.end] = node
            pq.put((new_distance, child.end))


if distance[end_node] == float('inf'):
    print('There is no such path.')
else:
    print(distance[end_node])

    path = deque()
    end_idx = end_node
    path.appendleft(end_idx)

    while start_node != end_idx:
        path.appendleft(parent[end_idx])
        end_idx = parent[end_idx]

    print(*path)


# 2-nd solution
from queue import PriorityQueue
from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


edges = int(input())
graph = {}

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(', ')]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(Edge(source, destination, weight))

start = int(input())
target = int(input())

max_node = max(graph.keys())

distance = [float('inf')] * (max_node + 1)
parent = [None] * (max_node + 1)

distance[start] = 0

pq = PriorityQueue()
pq.put((0, start))

while not pq.empty():
    min_distance, node = pq.get()
    if node == target:
        break
    for edge in graph[node]:
        new_distance = min_distance + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = node
            pq.put((new_distance, edge.destination))

if distance[target] == float('inf'):
    print('There is no such path.')
else:
    print(distance[target])

    path = deque()
    node = target
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    print(*path, sep=' ')
    
