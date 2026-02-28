import random
from collections import deque

def create_grid(n):
    # More free cells (1), fewer obstacles (0)
    return [[random.choice([1,1,1,0]) for _ in range(n)] for _ in range(n)]

def print_grid(grid):
    print("\nGenerated N x N Matrix:")
    for row in grid:
        print(row)

def bfs_with_moves(grid, start, goal):
    n = len(grid)
    queue = deque([start])
    visited = set([start])

    directions = [(-1,0,"Up"),
                  (1,0,"Down"),
                  (0,-1,"Left"),
                  (0,1,"Right")]

    while queue:
        x, y = queue.popleft()

        if (x,y) == goal:
            print("\nGoal Reached!")
            return

        for dx, dy, move in directions:
            nx, ny = x+dx, y+dy

            if 0<=nx<n and 0<=ny<n:
                # Now check FREE cell (1)
                if grid[nx][ny] == 1 and (nx,ny) not in visited:
                    print(f"Moving {move} -> ({nx}, {ny})")
                    queue.append((nx,ny))
                    visited.add((nx,ny))

    print("No Path Found")


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

bfs_with_moves(grid, start, goal)