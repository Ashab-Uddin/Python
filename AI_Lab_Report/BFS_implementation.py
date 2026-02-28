from collections import deque
import random

# Step 1: Take grid size N
N = int(input("Enter Grid Size N: "))

# Step 2: Generate graph[N][N] with random obstacles
graph = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(random.choice([0, 1]))   # 0 = obstacle, 1 = free
    graph.append(row)

# Print the matrix
print("\nGenerated Grid (1 = Free, 0 = Obstacle):")
for row in graph:
    print(row)

# Step 3: Initialize Start State S and Goal State G
sx, sy = map(int, input("\nEnter Start State (x y): ").split())
gx, gy = map(int, input("Enter Goal State (x y): ").split())

S = (sx, sy)
G = (gx, gy)

# If start or goal blocked
if graph[sx][sy] == 0 or graph[gx][gy] == 0:
    print("Start or Goal is blocked by obstacle!")
    exit()

# Step 4: level[S] = 0
level = [[-1]*N for _ in range(N)]
level[sx][sy] = 0

# Step 5: Q = empty
Q = deque()

# Step 6: ENQUEUE(Q, S)
Q.append(S)

goal_flag = False

# Step 7: while Q not empty
while Q:

    # Step 8: Node u = DEQUEUE(Q)
    u = Q.popleft()
    x, y = u

    # x_move and y_move arrays
    x_move = [1, -1, 0, 0]
    y_move = [0, 0, 1, -1]

    # Step 9: for each child node v ∈ adj[u]
    for i in range(4):

        v_x = x + x_move[i]
        v_y = y + y_move[i]

        # Step 10: valid move & free cell check
        if (0 <= v_x < N and 0 <= v_y < N) and graph[v_x][v_y] == 1:

            # Step 11: if v == G
            if (v_x, v_y) == G:
                goal_flag = True
                break

            # Step 15: mark visited
            graph[v_x][v_y] = -1   # visited mark

            # Step 16: level[v] = level[u] + 1
            level[v_x][v_y] = level[x][y] + 1

            # Step 17: ENQUEUE(Q, v)
            Q.append((v_x, v_y))

    if goal_flag:
        break

# Step 20-24: Print result
if goal_flag:
    print("\nGoal Found!")
else:
    print("\nGoal cannot be reached.")