import heapq

class PuzzleState:
    def __init__(self, board, zero_pos, moves=0, previous=None):
        self.board = board
        self.zero_pos = zero_pos
        self.moves = moves
        self.previous = previous
        self.goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    def is_goal(self):
        return tuple(self.board) == self.goal

    def get_neighbors(self):
        neighbors = []
        x, y = self.zero_pos
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_board = [row[:] for row in self.board]  # Create a copy of the board
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                neighbors.append(PuzzleState(new_board, (new_x, new_y), self.moves + 1, self))

        return neighbors

    def heuristic(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                value = self.board[i][j]
                if value != 0:
                    target_x = (value - 1) // 3
                    target_y = (value - 1) % 3
                    distance += abs(target_x - i) + abs(target_y - j)
        return distance

    def __lt__(self, other):
        return (self.moves + self.heuristic()) < (other.moves + other.heuristic())

def a_star(initial_board):
    initial_zero_pos = next((i, j) for i in range(3) for j in range(3) if initial_board[i][j] == 0)
    initial_state = PuzzleState(initial_board, initial_zero_pos)

    open_set = []
    heapq.heappush(open_set, initial_state)
    closed_set = set()

    while open_set:
        current_state = heapq.heappop(open_set)

        if current_state.is_goal():
            return current_state

        closed_set.add(tuple(tuple(row) for row in current_state.board))

        for neighbor in current_state.get_neighbors():
            if tuple(tuple(row) for row in neighbor.board) in closed_set:
                continue
            heapq.heappush(open_set, neighbor)

    return None

def print_solution(solution):
    path = []
    while solution:
        path.append(solution.board)
        solution = solution.previous
    for board in reversed(path):
        for row in board:
            print(row)
        print()  # Print a blank line between boards

if __name__ == "__main__":
    initial_board = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6]
    ]
    
    solution = a_star(initial_board)
    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution exists.")
