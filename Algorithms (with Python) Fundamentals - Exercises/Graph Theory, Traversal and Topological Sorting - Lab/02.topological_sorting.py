# 1-st decision
def sorted_nodes(graph, predecessors, output):
    while predecessors:
        nodes_to_remove = [k for k in predecessors if predecessors[k] == 0]
        if not nodes_to_remove:
            return False
        node_to_remove = nodes_to_remove[0]
        del predecessors[node_to_remove]
        output.append(node_to_remove)
        for child in graph[node_to_remove]:
            predecessors[child] -= 1

    return True


n = int(input())

graph = {}
for _ in range(n):
    key, value = input().split(' ->')
    graph[key] = list(value.strip().split(', ')) if value and value != ' ' else []

predecessors = {}

for node, children in graph.items():
    if node not in predecessors:
        predecessors[node] = 0
    for child in children:
        if child not in predecessors:
            predecessors[child] = 1
        else:
            predecessors[child] += 1

output = []

is_sortable = sorted_nodes(graph, predecessors, output)
if is_sortable:
    print(f'Topological sorting: {", ".join(str(x) for x in output)}')
else:
    print('Invalid topological sorting')



# 2-nd decision
def find_dependencies(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0
        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1
    return result


def find_node_without_dependencies(dependencies_by_node):
    for node, dependencies in dependencies_by_node.items():
        if dependencies == 0:
            return node
    return None


nodes = int(input())

graph = {}

for _ in range(nodes):
    line_parts = input().split('->')
    node = line_parts[0].strip()
    children = line_parts[1].strip().split(', ') if line_parts[1] else []
    graph[node] = children


dependencies_by_node = find_dependencies(graph)
has_cycles = False
sorted_nodes = []

while dependencies_by_node:
    node_to_remove = find_node_without_dependencies(dependencies_by_node)
    if node_to_remove is None:
        has_cycles = True
        break
    dependencies_by_node.pop(node_to_remove)
    sorted_nodes.append(node_to_remove)
    for child in graph[node_to_remove]:
        dependencies_by_node[child] -= 1

if has_cycles:
    print("Invalid topological sorting")
else:
    print(f"Topological sorting: {', '.join(sorted_nodes)}")
