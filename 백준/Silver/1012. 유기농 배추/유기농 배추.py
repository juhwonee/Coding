T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())

    matrix = []
    for _ in range(M):
        row = [0] * N
        matrix.append(row)
    cnt = 0

    for _ in range(K):
        x, y = map(int, input().split())
        matrix[x][y] = 1

    def BFS(x,y):
        queue = []
        start_matrix = (x, y)
        queue.append(start_matrix)

        matrix[x][y] = 0

        while queue:
            x, y = queue.pop(0)

            if x - 1 >= 0 and matrix[x - 1][y] == 1:
                matrix[x - 1][y] = 0
                queue.append((x - 1, y))

            if x + 1 < M and matrix[x + 1][y] == 1:
                matrix[x + 1][y] = 0
                queue.append((x + 1, y))

            if y - 1 >= 0 and matrix[x][y - 1] == 1:
                matrix[x][y - 1] = 0
                queue.append((x, y - 1))

            if y + 1 < N and matrix[x][y + 1] == 1:
                matrix[x][y + 1] = 0
                queue.append((x, y + 1))

    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 1:
                BFS(i, j)
                cnt += 1
    print(cnt)