import random

def print_board(state):

    n = len(state)


    for row in range(n):

        line = " "

        for col in range(n):

            if state[col] == row:
                line += "Q"
            else:
                line += "."
        print(line)
    print()


def get_initial_states(n):
    return [random.randint(0,n-1) for _ in range(n) ]


def compute_heurestic(state):
    n = len(state)
    h = 0


    for i in range(n):
        for j in range(i+1, n):

            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):

                h += 1

    return h


def get_best_neighbour(state):

    n = len(state)
    best_state = state[:]
    min_h = compute_heurestic(state)

    for col in range(n):
        original_row = state[col]

        for row in range(n):
            if row != original_row:
                state[col] = row
                h = compute_heurestic(state)

                if h < min_h:
                    min_h = h
                    best_state = state[:]

        state[col] = original_row

    return best_state, min_h

def hill_climbing(n):
    current = get_initial_states(n)
    current_h = compute_heurestic(current)

    while True:
        neighbour, neighbour_h = get_best_neighbour(current)

        if neighbour_h >= current_h:
            break

        current = neighbour
        current_h = neighbour_h

    return current, current_h


n = 8

solution , h = hill_climbing(n)
print_board(solution)

if h == 0:
    print("Solution Found")
else:
    print("Local optimum reached, no solution")
