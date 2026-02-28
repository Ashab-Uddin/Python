import random
from collections import deque

# Question 1 & 2

# Create grid with random obstacles


def create_grid(n):
    grid = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.choice([0, 0, 0, 1]))  # More free cells
        grid.append(row)
    return grid

# Print grid


def print_grid(grid):
    print("\nGenerated Grid:")
    for row in grid:
        print(row)

# BFS Traversal


def bfs(grid, start, goal):
    n = len(grid)
    queue = deque()
    visited = set()
    parent = {}

    queue.append(start)
    visited.add(start)

    directions = [(-1, 0, "Up"), (1, 0, "Down"),
                  (0, -1, "Left"), (0, 1, "Right")]

    while queue:
        x, y = queue.popleft()

        if (x, y) == goal:
            print("\nGoal Reached!")
            return parent

        for dx, dy, move in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == 0 and (nx, ny) not in visited:
                    print(f"Moving {move} -> ({nx}, {ny})")
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)

    return None


# Question 3

# Print path using parent
def print_path(parent, start, goal):
    if parent is None:
        print("No Path Found")
        return

    path = []
    current = goal

    while current != start:
        path.append(current)
        current = parent[current]

    path.append(start)
    path.reverse()

    print("\nFinal Shortest Path:")
    for node in path:
        print(node)


# MAIN
n = int(input("Enter grid size N: "))
grid = create_grid(n)
print_grid(grid)

sx = int(input("Enter start x: "))
sy = int(input("Enter start y: "))
gx = int(input("Enter goal x: "))
gy = int(input("Enter goal y: "))

start = (sx, sy)
goal = (gx, gy)

grid[sx][sy] = 0
grid[gx][gy] = 0

parent = bfs(grid, start, goal)
print_path(parent, start, goal)