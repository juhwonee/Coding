N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

cnt = []
def divide(x, y, n):
    color = matrix[x][y]
    same = True

    for i in range(x, x+n):
        for j in range(y, y+n):
            if matrix[i][j] != color:
                same = False

    if same:
        if color == -1:
            cnt.append(-1)
        elif color == 1:
            cnt.append(1)
        else:
            cnt.append(0)

    else:
        new = n // 3
        for dx in range(3):
            for dy in range(3):
                divide(x + dx * new, y + dy * new, new)

divide(0, 0, N)
print(cnt.count(-1))
print(cnt.count(0))
print(cnt.count(1))