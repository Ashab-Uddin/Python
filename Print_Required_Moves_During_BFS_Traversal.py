from collections import deque
import random

# Generate grid with random obstacles
def generate_grid(N, obstacle_prob=0.3):
    grid = []
    for i in range(N):
        row = []
        for j in range(N):
            if random.random() < obstacle_prob:
                row.append(0)  # obstacle
            else:
                row.append(1)  # free cell
        grid.append(row)
    return grid

# Print grid
def print_grid(grid):
    print("\nGenerated Grid (1 = Free, 0 = Obstacle):")
    for row in grid:
        print(row)

# BFS with Move Printing
def bfs_with_moves(grid, start, goal):
    N = len(grid)
    visited = [[False]*N for _ in range(N)]
    
    # Direction arrays
    x_move = [1, -1, 0, 0]
    y_move = [0, 0, 1, -1]
    move_name = ["Moving Down", "Moving Up", 
                 "Moving Right", "Moving Left"]
    
    Q = deque()
    Q.append(start)
    visited[start[0]][start[1]] = True
    
    while Q:
        x, y = Q.popleft()
        
        if (x, y) == goal:
            print("\nGoal Found!")
            return
        
        # Explore all 4 directions
        for i in range(4):
            nx = x + x_move[i]
            ny = y + y_move[i]
            
            # Check boundary and free cell
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and grid[nx][ny] == 1:
                    visited[nx][ny] = True
                    
                    # Print required move
                    print(f"{move_name[i]} -> ({nx}, {ny})")
                    
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
    bfs_with_moves(grid, (sx, sy), (gx, gy))