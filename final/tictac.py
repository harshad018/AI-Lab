

def print_board(board):

    for row in board:

        print( " | ".join(row))
        print("*" * 5)


def check_win(board, player):

    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
            return True

    return False


def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():

    board = [[" " for _ in range(3)] for _ in range(3)]

    current = "X"

    while True:
        print_board(board)

        try:
            row = int(input(f"For player {current} , Enter row: "))
            col = int(input(f"For player {current} , Enter col: "))

            if row not in range(3) or col not in range(3):
                print("Invalid input , please enter the value between 0 to 2")
                continue

            if board[row][col] != " ":
                print("The cell is already taken , please choose other one.")
                continue
        except ValueError:
            print("Please enter numerical value")
            continue


        board[row][col] = current

        if check_win(board,current):
            print_board(board)
            print(f"Player {current} has won!")
            break

        if check_draw(board):
            print_board(board)
            print("There is a draw!")
            break

        if current == "X":
            current = "O"
        else:
            current = "X"


tic_tac_toe()
