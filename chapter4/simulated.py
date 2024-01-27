import copy
import math
import random

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

def anneal(initial_state, goal_state, temperature, cooling_rate):
    current_state = copy.deepcopy(initial_state)
    current_energy = h(current_state, goal_state)
    
    while temperature > 0.1:
        new_state = random.choice(generate_neighbors(current_state))
        new_energy = h(new_state, goal_state)
        
        # Calculate the change in energy
        delta_energy = new_energy - current_energy
        
        # If the new state is better or with a certain probability, accept the worse solution
        if delta_energy < 0 or random.uniform(0, 1) < math.exp(-delta_energy / temperature):
            current_state = new_state
            current_energy = new_energy
        
        print(f"Temperature: {temperature:.2f}, Energy: {current_energy}")
        
        temperature *= cooling_rate

    print("Final State:")
    print_puzzle(current_state)

if __name__ == "__main__":
    # Example initial and goal states
    initial_state = [
        [3, 8, 5],
        [0, 7, 1],
        [2, 6, 4]
    ]

    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    print("Initial State:")
    print_puzzle(initial_state)

    initial_temperature = 1.0
    cooling_rate = 0.995

    anneal(initial_state, goal_state, initial_temperature, cooling_rate)
