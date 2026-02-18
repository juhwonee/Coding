N, M, V = map(int, input(). split())

matrix = []
for _ in range(N+1):
    matrix.append([])

for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

for i in range(1, N+1):
    matrix[i].sort()

visit_dfs = [0] * (N+1)
def DFS(v):
    visit_dfs[v] = 1
    print(v, end=' ')

    for i in matrix[v]:
        if visit_dfs[i] == 0:
            DFS(i)

visit_bfs = [0] * (N+1)
def BFS(start):
    queue = []
    queue.append(start)
    visit_bfs[start] = 1

    while queue:
        v = queue.pop(0)
        print(v, end= ' ')

        for i in matrix[v]:
            if visit_bfs[i] == 0:
                visit_bfs[i] = 1
                queue.append(i)

DFS(V)
print()
BFS(V)