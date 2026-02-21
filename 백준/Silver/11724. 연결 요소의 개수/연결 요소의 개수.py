from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N+1)
cnt = 0
queue = deque()

for i in range(1, N+1):
    if not visited[i]:
        queue.append(i)
        visited[i] = 1

        while queue:
            current = queue.popleft()
            for next in graph[current]: # graph[1] = [2, 5]
                if not visited[next]:
                    visited[next] = 1
                    queue.append(next)

        cnt += 1

print(cnt)