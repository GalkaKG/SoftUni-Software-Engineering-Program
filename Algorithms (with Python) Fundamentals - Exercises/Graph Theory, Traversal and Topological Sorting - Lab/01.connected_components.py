# 1-st decision
def dfs(node, visited, graph, connected):
    if visited[node]:
        return

    visited[node] = True

    for child in graph[node]:
        dfs(child, visited, graph, connected)

    connected.append(node)


n = int(input())
graph = {}

for i in range(n):
    graph[i] = [int(x) for x in input().split()]

visited = [False] * n

for node in graph:
    if visited[node]:
        continue
    connected = []
    dfs(node, visited, graph, connected)
    print(f'Connected component: {" ".join(str(x) for x in connected)}')


# 2-nd decision
def dfs(node, graph, visited, component):
    if visited[node]:
        return
    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited, component)

    component.append(node)


nodes = int(input())
graph = []

for node in range(nodes):
    line = input()
    children = [] if line == "" else [int(x) for x in line.split()]
    graph.append(children)

visited = [False] * nodes
for node in range(nodes):
    if visited[node]:
        continue
    component = []
    dfs(node, graph, visited, component)
    print(f'Connected component: {" ".join([str(x) for x in component])}')
