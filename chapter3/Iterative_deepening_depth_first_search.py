def iterative_deepening_dfs(graph, start, goal):
    depth_limit = 0

    while True:
        result = depth_limited_search(graph, start, goal, depth_limit)
        if result is not None:
            return result
        depth_limit += 1

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

if start_node not in graph or goal_node not in graph:
    print("Invalid start or goal node.")
else:
    print(f"Iterative Deepening Depth-First Search from {start_node} to {goal_node}:")
    path = iterative_deepening_dfs(graph, start_node, goal_node)
    
    if path:
        print("Path found:", path)
    else:
        print(f"No path from {start_node} to {goal_node} exists.")



# Enter the number of edges: 9
# Enter edge (format: node1 node2): A B
# Enter edge (format: node1 node2): A D
# Enter edge (format: node1 node2): B A
# Enter edge (format: node1 node2): B C
# Enter edge (format: node1 node2): B E
# Enter edge (format: node1 node2): C F
# Enter edge (format: node1 node2): D E
# Enter edge (format: node1 node2): E G
# Enter edge (format: node1 node2): E H
# Enter the start node: A
# Enter the goal node: F
# Iterative Deepening Depth-First Search from A to F:
# A A B D A B C E D A B C F Path found: ['A', 'B', 'C', 'F']