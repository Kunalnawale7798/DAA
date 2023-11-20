def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens(board, row, n):
    if row == n:
        # All queens are placed, print the board
        print_board(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            # Place queen and move to the next row
            board[row][col] = 'Q'
            solve_n_queens(board, row + 1, n)
            # Backtrack
            board[row][col] = '.'

# Example usage
n = 5  # Change the value of n for different board sizes
board = [['.' for _ in range(n)] for _ in range(n)]

# Initialize the board with the first queen placed (for simplicity)
board[0][0] = 'Q'

print(f"Solutions for {n}-Queens:")
solve_n_queens(board, 1, n)
