def dfs(node, graph, visited):
    if visited[node]:
        return
    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)


nodes_count = int(input())
edges_count = int(input())

graph = []
[graph.append([]) for _ in range(nodes_count)]

edges = []

for _ in range(edges_count):
    first, second = [int(x) for x in input().split(' - ')]
    graph[first].append(second)
    graph[second].append(first)
    edges.append((min(first, second), max(first, second)))

print(f'Important streets:')

for first, second in edges:
    graph[first].remove(second)
    graph[second].remove(first)

    visited = [False] * nodes_count
    dfs(0, graph, visited)

    if not all(visited):
        print(first, second)

    graph[first].append(second)
    graph[second].append(first)
