import random

# Create grid with random obstacles
def create_grid(n):
    grid = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.choice([1, 1, 1, 0]))  # More free cells (1)
        grid.append(row)
    return grid


# Print grid
def print_grid(grid):
    print("\nGenerated Grid:")
    for row in grid:
        print(row)


# DFS traversal
def dfs(grid, current, goal, visited):
    n = len(grid)
    x, y = current

    if current == goal:
        print("Goal Reached!")
        return True

    visited.add(current)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < n:
            # Check FREE cell (1) instead of 0
            if grid[nx][ny] == 1 and (nx, ny) not in visited:
                if dfs(grid, (nx, ny), goal, visited):
                    return True

    return False


# MAIN
n = int(input("Enter Grid Size N: "))
grid = create_grid(n)
print_grid(grid)

sx = int(input("Enter Start X: "))
sy = int(input("Enter Start Y: "))
gx = int(input("Enter Goal X: "))
gy = int(input("Enter Goal Y: "))

start = (sx, sy)
goal = (gx, gy)

# Ensure start and goal are free (1)
grid[sx][sy] = 1
grid[gx][gy] = 1

visited = set()

if not dfs(grid, start, goal, visited):
    print("No Path Found")