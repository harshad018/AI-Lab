def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Player {current}, enter row (0-2): "))
            col = int(input(f"Player {current}, enter col (0-2): "))
            if row not in range(3) or col not in range(3):
                print("Invalid input! Please enter values between 0 and 2.")
                continue
            if board[row][col] != " ":
                print("Cell already taken! Try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        board[row][col] = current

        if check_win(board, current):
            print_board(board)
            print(f"Player {current} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current = "O" if current == "X" else "X"

# Run the game
tic_tac_toe()
