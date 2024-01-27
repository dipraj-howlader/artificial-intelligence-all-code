def depth_limited_search(graph, start, goal, depth_limit, visited=None):
    if visited is None:
        visited = set()

    return dls_recursive(graph, start, goal, depth_limit, visited, 0)

def dls_recursive(graph, current, goal, depth_limit, visited, current_depth):
    if current_depth > depth_limit:
        return None

    visited.add(current)
    print(current, end=' ')

    if current == goal:
        return [current]

    for neighbor in graph[current]:
        if neighbor not in visited:
            path = dls_recursive(graph, neighbor, goal, depth_limit, visited, current_depth + 1)
            if path is not None:
                return [current] + path

    return None

# Take input for the graph
graph = {}
num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    edge = input("Enter edge (format: node1 node2): ").split()
    node1, node2 = edge

    # Add edges to the graph
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []

    graph[node1].append(node2)
    graph[node2].append(node1)

# Take input for the start and goal nodes
start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

# Take input for the depth limit
depth_limit = int(input("Enter the depth limit: "))

if start_node not in graph or goal_node not in graph:
    print("Invalid start or goal node.")
else:
    print(f"Depth-Limited Search from {start_node} to {goal_node} with depth limit {depth_limit}:")
    path = depth_limited_search(graph, start_node, goal_node, depth_limit)
    
    if path:
        print("Path found:", path)
    else:
        print(f"No path from {start_node} to {goal_node} within the depth limit.")


# Enter the number of edges: 6
# Enter edge (format: node1 node2): A B
# Enter edge (format: node1 node2): B C
# Enter edge (format: node1 node2): C D
# Enter edge (format: node1 node2): D E
# Enter edge (format: node1 node2): B F
# Enter edge (format: node1 node2): F G
# Enter the start node: A
# Enter the goal node: G
# Enter the depth limit: 3
# Depth-Limited Search from A to G with depth limit 3:
# A B C D E F G
# Path found: ['A', 'B', 'F', 'G']
