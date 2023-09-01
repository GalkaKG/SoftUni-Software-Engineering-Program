# 1-st solution
def dfs(node, graph, visited, node_salary):
    if visited[node]:
        return node_salary[node]

    visited[node] = True

    if not graph[node]:
        node_salary[node] = 1
        return node_salary[node]

    if node not in node_salary:
        node_salary[node] = 0

    for child in graph[node]:
        node_salary[node] += dfs(child, graph, visited, node_salary)

    return node_salary[node]


count_nodes = int(input())
graph = {}

for key in range(count_nodes):
    graph[key] = [node for node, child in enumerate(list(input())) if child == 'Y']

sum_salaries = 0
node_salary = {}
visited = [False] * len(graph)

for node in graph:
    sum_salaries += dfs(node, graph, visited, node_salary)

print(sum_salaries)


# 2-nd solution
def dfs(node, graph, salaries):
    if salaries[node] is not None:
        return salaries[node]
    if len(graph[node]) == 0:
        salaries[node] = 1
        return 1
    salary = 0
    for child in graph[node]:
        salary += dfs(child, graph, salaries)

    salaries[node] = salary
    return salary


nodes = int(input())
graph = []

for _ in range(nodes):
    line = input()
    children = []
    for idx, state in enumerate(line):
        if state == 'Y':
            children.append(idx)
    graph.append(children)

salaries = [None] * nodes

result = 0
for node in range(nodes):
    salary = dfs(node, graph, salaries)
    result += salary

print(result)
