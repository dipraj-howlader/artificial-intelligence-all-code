#Done

graph = {
    'A': ['E', 'B'],
    'E': ['D'],
    'B': ['G', 'C'],
    'D': ['G'],
    'C': [],  # Add 'C' with an empty list as its neighbors
    'G': []   # Add 'G' with an empty list as its neighbors
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        current_node = queue.pop(0)
        print(current_node, end=" ")

        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Following is the Breadth-First Search:")
bfs(visited, graph, 'A')
