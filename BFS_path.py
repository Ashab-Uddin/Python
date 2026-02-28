from collections import deque
import random

# Generate grid with random obstacles
def generate_grid(N, obstacle_prob=0.3):
    grid = []
    for i in range(N):
        row = []
        for j in range(N):
            if random.random() < obstacle_prob:
                row.append(0)   # 0 = obstacle
            else:
                row.append(1)   # 1 = free cell
        grid.append(row)
    return grid

# Print grid
def print_grid(grid):
    print("\nGenerated Grid (1 = Free, 0 = Obstacle):")
    for row in grid:
        print(row)

# Recursive function to print path
def print_path(parent, start, current):
    if current == start:
        print(current)
        return
    print_path(parent, start, parent[current])
    print(current)

# BFS function
def bfs_path(grid, start, goal):
    N = len(grid)
    visited = [[False]*N for _ in range(N)]
    parent = {}   # Dictionary to store parent of each node
    
    # Movement directions
    x_move = [1, -1, 0, 0]
    y_move = [0, 0, 1, -1]
    
    Q = deque()
    Q.append(start)
    visited[start[0]][start[1]] = True
    parent[start] = None
    
    while Q:
        x, y = Q.popleft()
        
        if (x, y) == goal:
            print("\nGoal Found!\n")
            print("Path from Start to Goal:")
            print_path(parent, start, goal)
            return
        
        # Explore neighbors
        for i in range(4):
            nx = x + x_move[i]
            ny = y + y_move[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and grid[nx][ny] == 1:
                    visited[nx][ny] = True
                    parent[(nx, ny)] = (x, y)
                    Q.append((nx, ny))
    
    print("\nGoal Cannot Be Reached.")

# ================= MAIN =================

N = int(input("Enter Grid Size N: "))
grid = generate_grid(N)
print_grid(grid)

sx, sy = map(int, input("\nEnter Start (x y): ").split())
gx, gy = map(int, input("Enter Goal (x y): ").split())

if grid[sx][sy] == 0 or grid[gx][gy] == 0:
    print("Start or Goal is blocked by obstacle!")
else:
    bfs_path(grid, (sx, sy), (gx, gy))