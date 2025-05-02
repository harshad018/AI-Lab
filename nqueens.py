import random

def print_board(state):
    n = len(state)
    for row in range(n):
        line = ""
        for col in range(n):
            if state[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def generate_initial_state(n):
    return [random.randint(0, n - 1) for _ in range(n)]

def compute_heuristic(state):
    h = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                h += 1
    return h

def get_best_neighbor(state):
    n = len(state)
    best_state = state[:]
    min_h = compute_heuristic(state)

    for col in range(n):
        original_row = state[col]
        for row in range(n):
            if row != original_row:
                state[col] = row
                h = compute_heuristic(state)
                if h < min_h:
                    min_h = h
                    best_state = state[:]
        state[col] = original_row

    return best_state, min_h

def hill_climbing(n):
    current = generate_initial_state(n)
    current_h = compute_heuristic(current)

    while True:
        neighbor, neighbor_h = get_best_neighbor(current)

        if neighbor_h >= current_h:  # No better neighbor
            break
        current = neighbor
        current_h = neighbor_h

    return current, current_h

# Example usage:
n = 8
solution, h = hill_climbing(n)
print("Final Board:")
print_board(solution)
if h == 0:
    print("Solution Found!")
else:
    print("Local Optimum Reached (no solution). Heuristic:", h)
