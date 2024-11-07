def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")
def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if j < 0:
            break
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if j >= len(board):
            break
        if board[i][j] == 1:
            return False
    return True
def solve_n_queens_util(board, row):
    if row >= len(board):
        print_solution(board)
        return True
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1)
            board[row][col] = 0
    return False
def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_n_queens_util(board, 0)

if __name__ == "__main__":
    n = 8 
    solve_n_queens(n)
