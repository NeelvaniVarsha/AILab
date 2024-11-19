import random
import math

N = 8

def fitness(state):
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def neighbor(state):
    neighbor_state = state[:]
    col = random.randint(0, N - 1)  
    row = random.randint(0, N - 1)  
    while row == neighbor_state[col]:  
        row = random.randint(0, N - 1)
    neighbor_state[col] = row
    return neighbor_state

def simulated_annealing_8_queens(initial_state, initial_temperature, decrease_factor, min_temperature):
    current = initial_state
    T = initial_temperature

    while T > min_temperature:
        next_state = neighbor(current)
        delta_E = fitness(current) - fitness(next_state)
        if delta_E > 0:
            current = next_state  
        else:
            p = math.exp(delta_E / T)
            if random.random() < p:
                current = next_state
        T *= decrease_factor
        if fitness(current) == 0:
            return current
    return current  

initial_state = [random.randint(0, N - 1) for _ in range(N)]  
initial_temperature = 500  
decrease_factor = 0.98  
min_temperature = 1e-4  

solution_found = False
while not solution_found:
    result = simulated_annealing_8_queens(initial_state, initial_temperature, decrease_factor, min_temperature)
    if fitness(result) == 0:
        solution_found = True

print("Final configuration:", result)
print("Number of conflicts:", fitness(result))

def print_board(state):
    board = [["."] * N for _ in range(N)]
    for col, row in enumerate(state):
        board[row][col] = "Q"
    for row in board:
        print(" ".join(row))

print_board(result)
