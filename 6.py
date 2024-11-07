class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid  # The environment grid
        self.position = (0, 0)  # Starting position of the vacuum cleaner
        self.cleaned_cells = []  # List to keep track of cleaned cells

    def is_dirty(self, position):
        """Check if the current position is dirty."""
        x, y = position
        return self.grid[x][y] == 1  # 1 represents dirty

    def clean(self, position):
        """Clean the current position."""
        x, y = position
        if self.is_dirty(position):
            self.grid[x][y] = 0  # Clean the cell
            self.cleaned_cells.append(position)
            print(f"Cleaned cell at {position}")

    def move(self, direction):
        """Move the vacuum cleaner in the specified direction."""
        x, y = self.position
        if direction == 'up' and x > 0:
            self.position = (x - 1, y)
        elif direction == 'down' and x < len(self.grid) - 1:
            self.position = (x + 1, y)
        elif direction == 'left' and y > 0:
            self.position = (x, y - 1)
        elif direction == 'right' and y < len(self.grid[0]) - 1:
            self.position = (x, y + 1)

    def clean_environment(self):
        """Clean the entire environment."""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.position = (i, j)  # Move to the next cell
                self.clean(self.position)

    def display_grid(self):
        """Display the current state of the grid."""
        for row in self.grid:
            print(' '.join(['D' if cell == 1 else 'C' for cell in row]))
        print()

if __name__ == "__main__":
    # 1 represents dirty, 0 represents clean
    environment = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 1, 1]
    ]

    vacuum = VacuumCleaner(environment)
    print("Initial environment:")
    vacuum.display_grid()

    vacuum.clean_environment()

    print("Final environment after cleaning:")
    vacuum.display_grid()
    print("Cleaned cells:", vacuum.cleaned_cells)
