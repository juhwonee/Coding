N = int(input())

matrix = []
for _ in range(N):
    row = list(input().strip())
    matrix.append(row)

def BFS(x, y):
    queue = []
    queue.append((x, y))
    matrix[x][y] = '0'
    cnt = 1

    while queue:
        x, y = queue.pop(0)

        if x-1 >= 0 and matrix[x-1][y] == '1':
            matrix[x-1][y] = '0'
            queue.append((x-1, y))
            cnt += 1

        if x+1 < N and matrix[x+1][y] == '1':
            matrix[x+1][y] = '0'
            queue.append((x+1, y))
            cnt += 1

        if y-1 >= 0 and matrix[x][y-1] == '1':
            matrix[x][y-1] = '0'
            queue.append((x, y-1))
            cnt += 1

        if y+1 < N and matrix[x][y+1] == '1':
            matrix[x][y+1] = '0'
            queue.append((x, y+1))
            cnt += 1

    return cnt

result = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == '1':
            danji = BFS(i, j)
            result.append(danji)

result.sort()
print(len(result))
for i in result:
    print(i)