# 1-st solution
def dfs(node, destination, all_edges, graph, visited):
    if node in visited:
        return

    visited.append(node)

    if node == destination:
        return

    for child in graph[node]:
        dfs(child, destination, all_edges, graph, visited)


count_nodes = int(input())
graph = {}
all_edges = []

for _ in range(count_nodes):
    node, values = input().split(' -> ')
    children = values.split()
    graph[node] = children

    for child in children:
        all_edges.append((node, child))

removed_edges = []

for source, destination in sorted(all_edges, key=lambda x: (x[0], x[1])):
    if source not in graph[destination] and destination not in graph[source]:
        continue

    graph[source].remove(destination)
    graph[destination].remove(source)

    visited = []
    dfs(source, destination, all_edges, graph, visited)

    if destination in visited:
        removed_edges.append((source, destination))
    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f'Edges to remove: {len(removed_edges)}')
for source, destination in removed_edges:
    print(f'{source} - {destination}')



# 2-nd solution
def dfs(node, destination, graph, visited):
    if node in visited:
        return
    visited.add(node)
    if node == destination:
        return
    for child in graph[node]:
        dfs(child, destination, graph, visited)


def path_exist(source, destination, graph):
    visited = set()

    dfs(source, destination, graph, visited)

    return destination in visited


nodes = int(input())

graph = {}
edges = []   # Всички ребра, които имаме
for _ in range(nodes):
    node, children_str = input().split(' -> ')
    children = children_str.split()
    graph[node] = children
    for child in children:
        edges.append((node, child))

removed_edges = []
for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if destination not in graph[source] and source not in graph[destination]:
        continue
    graph[source].remove(destination)
    graph[destination].remove(source)

    if path_exist(source, destination, graph):
        removed_edges.append((source, destination))
    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f'Edges to remove: {len(removed_edges)}')
for first, second in removed_edges:
    print(f'{first} - {second}')
