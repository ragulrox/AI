from collections import deque

class State:
    def __init__(self, missionaries_left, cannibals_left, boat_position):
        self.missionaries_left = missionaries_left
        self.cannibals_left = cannibals_left
        self.boat_position = boat_position  # 0 for left, 1 for right

    def is_valid(self):
        # Check if the state is valid
        if self.missionaries_left < 0 or self.cannibals_left < 0:
            return False
        if self.missionaries_left < self.cannibals_left and self.missionaries_left > 0:
            return False
        return True

    def is_goal(self):
        # Check if the goal state is reached
        return self.missionaries_left == 0 and self.cannibals_left == 0

    def __hash__(self):
        return hash((self.missionaries_left, self.cannibals_left, self.boat_position))

    def __eq__(self, other):
        return (self.missionaries_left, self.cannibals_left, self.boat_position) == (other.missionaries_left, other.cannibals_left, other.boat_position)

def get_next_states(state):
    next_states = []
    if state.boat_position == 0:  # Boat is on the left side
        # Move 1 missionary
        next_states.append(State(state.missionaries_left - 1, state.cannibals_left, 1))
        # Move 2 missionaries
        next_states.append(State(state.missionaries_left - 2, state.cannibals_left, 1))
        # Move 1 cannibal
        next_states.append(State(state.missionaries_left, state.cannibals_left - 1, 1))
        # Move 2 cannibals
        next_states.append(State(state.missionaries_left, state.cannibals_left - 2, 1))
        # Move 1 missionary and 1 cannibal
        next_states.append(State(state.missionaries_left - 1, state.cannibals_left - 1, 1))
    else:  # Boat is on the right side
        # Move 1 missionary
        next_states.append(State(state.missionaries_left + 1, state.cannibals_left, 0))
        # Move 2 missionaries
        next_states.append(State(state.missionaries_left + 2, state.cannibals_left, 0))
        # Move 1 cannibal
        next_states.append(State(state.missionaries_left, state.cannibals_left + 1, 0))
        # Move 2 cannibals
        next_states.append(State(state.missionaries_left, state.cannibals_left + 2, 0))
        # Move 1 missionary and 1 cannibal
        next_states.append(State(state.missionaries_left + 1, state.cannibals_left + 1, 0))

    return [s for s in next_states if s.is_valid()]

def bfs():
    initial_state = State(3, 3, 0)  # 3 missionaries, 3 cannibals, boat on the left
    queue = deque([initial_state])
    visited = set()
    parent_map = {initial_state: None}

    while queue:
        current_state = queue.popleft()

        if current_state.is_goal():
            return reconstruct_path(parent_map, current_state)

        for next_state in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                parent_map[next_state] = current_state
                queue.append(next_state)

    return None

def reconstruct_path(parent_map, goal_state):
    path = []
    while goal_state is not None:
        path.append(goal_state)
        goal_state = parent_map[goal_state]
    return path[::-1]  # Reverse the path

def print_solution(solution):
    for state in solution:
        print(f"Left: {state.missionaries_left}M, {state.cannibals_left}C | Boat: {'Left' if state.boat_position == 0 else 'Right'}")

if __name__ == "__main__":
    solution = bfs()
    if solution:
        print("Solution found:")
       
