import copy

def print_puzzle(state):
    for row in state:
        print(" ".join(map(str, row)))
    print()

def h(state, goal):
    """Heuristic function - counts the number of misplaced tiles"""
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j]:
                count += 1
    return count

def generate_neighbors(state):
    """Generate neighboring states by swapping the blank space with adjacent tiles"""
    neighbors = []
    blank_i, blank_j = find_blank(state)
    
    # Possible moves: left, right, up, down
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for move_i, move_j in moves:
        new_i, new_j = blank_i + move_i, blank_j + move_j
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = copy.deepcopy(state)
            new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
            neighbors.append(new_state)

    return neighbors

def find_blank(state):
    """Find the coordinates of the blank space in the puzzle"""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def hill_climbing(initial_state, goal_state):
    current_state = copy.deepcopy(initial_state)
    steps = 0

    while True:
        print(f"Step {steps}:")
        print_puzzle(current_state)
        steps += 1

        # Check if the current state is the goal state
        if current_state == goal_state:
            print("Goal State Reached!")
            break

        neighbors = generate_neighbors(current_state)
        best_neighbor = min(neighbors, key=lambda x: h(x, goal_state))

        # If no neighbor has a lower heuristic value, we have reached a local minimum
        if h(best_neighbor, goal_state) >= h(current_state, goal_state):
            print("Local Minimum Reached!")
            break

        current_state = best_neighbor

if __name__ == "__main__":
    # Example initial and goal states
    initial_state = [
        [3, 8, 5],
        [0 , 7, 1],
        [2, 6, 4]
    ]

    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    print("Initial State:")
    print_puzzle(initial_state)

    hill_climbing(initial_state, goal_state)
