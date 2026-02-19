from collections import deque

M, N = map(int, input().split())

matrix = []
queue = deque()

for i in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()

    if x-1 >= 0 and matrix[x-1][y] == 0:
        matrix[x-1][y] = matrix[x][y] + 1
        queue.append((x-1, y))

    if x+1 < N and matrix[x+1][y] == 0:
        matrix[x+1][y] = matrix[x][y] + 1
        queue.append((x+1, y))

    if y-1 >= 0 and matrix[x][y-1] == 0:
        matrix[x][y-1] = matrix[x][y] + 1
        queue.append((x, y-1))

    if y+1 < M and matrix[x][y+1] == 0:
        matrix[x][y+1] = matrix[x][y] + 1
        queue.append((x, y+1))

ans = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            print(-1)
            exit()
        ans = max(ans, matrix[i][j])
print(ans - 1)