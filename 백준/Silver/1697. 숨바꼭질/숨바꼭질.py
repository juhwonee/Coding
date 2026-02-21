from collections import deque

N, K = map(int, input().split())

time = [0] * 100001
visited = [0] * 100001
queue = deque()
queue.append(N)
visited[N] = True

while queue:
    current = queue.popleft()

    if current == K:
        print(time[current])
        break

    next = [current-1, current+1, current*2]
    for i in next:
        if 0 <= i <= 100000 and not visited[i]:
            visited[i] = True
            time[i] = time[current] + 1
            queue.append(i)