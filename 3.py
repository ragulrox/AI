from collections import deque

class State:
    def __init__(self, jug1, jug2, capacity1, capacity2):
        self.jug1 = jug1  # Current amount in jug 1
        self.jug2 = jug2  # Current amount in jug 2
        self.capacity1 = capacity1  # Capacity of jug 1
        self.capacity2 = capacity2  # Capacity of jug 2

    def is_goal(self, target):
        return self.jug1 == target or self.jug2 == target

    def get_neighbors(self):
        neighbors = []
        # Fill jug 1
        neighbors.append(State(self.capacity1, self.jug2, self.capacity1, self.capacity2))
        # Fill jug 2
        neighbors.append(State(self.jug1, self.capacity2, self.capacity1, self.capacity2))
        # Empty jug 1
        neighbors.append(State(0, self.jug2, self.capacity1, self.capacity2))
        # Empty jug 2
        neighbors.append(State(self.jug1, 0, self.capacity1, self.capacity2))
        # Pour jug 1 into jug 2
        pour = min(self.jug1, self.capacity2 - self.jug2)
        neighbors.append(State(self.jug1 - pour, self.jug2 + pour, self.capacity1, self.capacity2))
        # Pour jug 2 into jug 1
        pour = min(self.jug2, self.capacity1 - self.jug1)
        neighbors.append(State(self.jug1 + pour, self.jug2 - pour, self.capacity1, self.capacity2))
        return neighbors

def bfs(capacity1, capacity2, target):
    initial_state = State(0, 0, capacity1, capacity2)
    queue = deque([initial_state])
    visited = set()

    while queue:
        current_state = queue.popleft()

        if current_state.is_goal(target):
            return current_state

        visited.add((current_state.jug1, current_state.jug2))

        for neighbor in current_state.get_neighbors():
            if (neighbor.jug1, neighbor.jug2) not in visited:
                queue.append(neighbor)

    return None

def print_solution(solution):
    path = []
    while solution:
        path.append((solution.jug1, solution.jug2))
        # Create a new state to explore its previous states
        solution = solution.previous if hasattr(solution, 'previous') else None
    for state in reversed(path):
        print(f"Jug 1: {state[0]}, Jug 2: {state[1]}")

if __name__ == "__main__":
    capacity1 = 4  # Capacity of jug 1
    capacity2 = 3  # Capacity of jug 2
    target = 2     # Target amount of water to measure

    solution = bfs(capacity1, capacity2, target)
    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution exists.")
