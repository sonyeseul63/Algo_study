from collections import deque

N, K = map(int, input().split())
q = deque()
q.append(N)
visited = [-1] * 100001
visited[N] = 0

while(q): 
    x = q.popleft()
    if x == K:
        print(visited[x])
        break
    for n in [x-1, x+1, 2*x]:
        if 0<=n<=100000 and visited[n] != -1:
            q.append(n)
            visited[n] = visited[x] + 1