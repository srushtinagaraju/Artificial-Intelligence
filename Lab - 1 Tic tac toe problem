def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
       
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
        except ValueError:
            print("Please enter valid integers for row and column.")
            continue
       
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Row and column must be 0, 1, or 2.")
            continue
       
        if board[row][col] != ' ':
            print("Cell already taken. Choose another.")
            continue
       
        board[row][col] = current_player
       
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
       
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
       
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()



OUTPUT:

  |   |  
---------
  |   |  
---------
  |   |  
---------
Player X's turn.
Enter row (0, 1, or 2): 0
Enter column (0, 1, or 2): 0


X |   |  
---------
  |   |  
---------
  |   |  
---------
Player O's turn.
Enter row (0, 1, or 2): 1
Enter column (0, 1, or 2): 0


X |   |  
---------
O |   |  
---------
  |   |  
---------
Player X's turn.
Enter row (0, 1, or 2): 1
Enter column (0, 1, or 2): 1


X |   |  
---------
O | X |  
---------
  |   |  
---------
Player O's turn.
Enter row (0, 1, or 2): 1
Enter column (0, 1, or 2): 2


X |   |  
---------
O | X | O
---------
  |   |  
---------
Player X's turn.
Enter row (0, 1, or 2): 2
Enter column (0, 1, or 2): 2


X |   |  
---------
O | X | O
---------
  |   | X
---------
Player X wins!
