import sys

def is_safe(board, row, col):
    # Check if a queen can be placed at the given position (row, col)
    # without attacking any other queen on the board
    
    # Check row
    for c in range(col):
        if board[row][c] == 'Q':
            return False
    
    # Check upper diagonal
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 'Q':
            return False
        r -= 1
        c -= 1
    
    # Check lower diagonal
    r, c = row, col
    while r < len(board) and c >= 0:
        if board[r][c] == 'Q':
            return False
        r += 1
        c -= 1
    
    return True

def solve_n_queens(n):
    # Recursive function to solve the N-Queens problem
    
    def backtrack(board, col):
        # Base case: All queens are placed on the board
        if col >= len(board):
            print_solution(board)
            return
        
        for row in range(len(board)):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(board, col + 1)
                board[row][col] = '.'
    
    def print_solution(board):
        # Print the current solution
        for row in board:
            print(' '.join(row))
        print()
    
    # Check if N is a valid integer
    try:
        n = int(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Initialize the board
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    # Solve the N-Queens problem
    backtrack(board, 0)

# Check if the program is called with the correct number of arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Get the value of N from command line argument
n = sys.argv[1]

# Solve the N-Queens problem
solve_n_queens(n)
