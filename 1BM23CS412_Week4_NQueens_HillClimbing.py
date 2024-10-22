import random

# Function to generate a random initial board configuration
def generate_initial_board(n):
    return [random.randint(0, n - 1) for _ in range(n)]

# Function to calculate the number of attacking pairs (heuristic)
def calculate_heuristic(board):
    heuristic = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                heuristic += 1
    return heuristic

# Function to generate neighboring boards
def generate_neighbors(board):
    neighbors = []
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i] != j:
                neighbor = board[:]
                neighbor[i] = j
                neighbors.append(neighbor)
    return neighbors

# Hill Climbing with Random Restart algorithm
# Allows passing a fixed initial state, or defaults to random initialization.
def hill_climbing_with_random_restart(n, max_restarts=100, initial_state=None):
    for restart in range(max_restarts):
        if initial_state is not None and restart == 0:
            # Use provided initial state on the first restart
            current_state = initial_state
        else:
            # Generate a random initial state for subsequent restarts
            current_state = generate_initial_board(n)
        
        current_heuristic = calculate_heuristic(current_state)

        print(f"Restart {restart + 1}: Initial State {current_state} with cost: {current_heuristic}")

        while True:
            neighbors = generate_neighbors(current_state)
            next_state = None
            next_heuristic = current_heuristic

            neighbor_costs = []

            for neighbor in neighbors:
                neighbor_heuristic = calculate_heuristic(neighbor)
                neighbor_costs.append((neighbor, neighbor_heuristic))

                if neighbor_heuristic < next_heuristic:
                    next_state = neighbor
                    next_heuristic = neighbor_heuristic

            print("\nNeighbor States and Costs:")
            for neighbor, cost in neighbor_costs:
                print(f"State: {neighbor} | Cost: {cost}")

            if next_heuristic >= current_heuristic:
                print(f"\nFinal State: {current_state} with cost: {current_heuristic}")
                if current_heuristic == 0:
                    return current_state
                else:
                    break  

            current_state = next_state
            current_heuristic = next_heuristic
            print(f"\nMove to state: {current_state} with cost: {current_heuristic}")

    print("No solution found after maximum restarts.")
    return None

# Function to print the board in a readable format
def print_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

# Main program
if __name__ == "__main__":
    n = 4  # Number of queens (4-Queens problem)
    max_restarts = 10  # Maximum number of restarts

    # Set a fixed initial state, e.g., [3, 1, 2, 0]
    fixed_initial_state = [3, 2, 1, 0]  

    # Run the algorithm with the fixed initial state
    solution = hill_climbing_with_random_restart(n, max_restarts, initial_state=fixed_initial_state)

    if solution:
        print("\nSolution found:")
        print_board(solution)
    else:
        print("\nNo solution found.")
