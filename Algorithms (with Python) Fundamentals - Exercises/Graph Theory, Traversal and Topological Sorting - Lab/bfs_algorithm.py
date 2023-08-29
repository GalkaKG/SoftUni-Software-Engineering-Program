from collections import deque


def bfs(node, graph, visited):
    if node in visited:
        return
    queue = deque([node])
    visited.add(node)

    while queue:
        current_node = queue.popleft()
        print(current_node, end=' ')

        for child in graph[current_node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)


graph = {
    7: [19, 21, 14],
    19: [1, 12, 31, 21],
    1: [7],
    12: [],
    31: [21],
    21: [14],
    14: [23, 6],
    6: [],
    23: [21]
}

visited = set()

for node in graph:
    bfs(node, graph, visited)
