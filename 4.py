from itertools import permutations

def is_valid_solution(mapping):
    # Extract the numbers based on the current mapping
    cross = mapping['C'] * 10000 + mapping['R'] * 1000 + mapping['O'] * 100 + mapping['S'] * 10 + mapping['S']
    roads = mapping['R'] * 10000 + mapping['O'] * 1000 + mapping['A'] * 100 + mapping['D'] * 10 + mapping['S']
    danger = mapping['D'] * 100000 + mapping['A'] * 10000 + mapping['N'] * 1000 + mapping['G'] * 100 + mapping['E']

    # Check if the equation holds
    return cross + roads == danger

def solve_cryptarithmetic():
    letters = 'CROSSROADEN'  # Unique letters in the equation
    unique_letters = set(letters)

    # Generate all permutations of digits for the unique letters
    for perm in permutations(range(10), len(unique_letters)):
        mapping = dict(zip(unique_letters, perm))

        # Check for leading zeros
        if mapping['C'] == 0 or mapping['R'] == 0 or mapping['D'] == 0:
            continue

        if is_valid_solution(mapping):
            return mapping
    return None

if __name__ == "__main__":
    solution = solve_cryptarithmetic()
    
    if solution:
        print("Solution found:")
        for letter, digit in sorted(solution.items()):
            print(f"{letter}: {digit}")
    else:
        print("No solution exists.")
