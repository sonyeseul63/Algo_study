from collections import deque
com = int(input())
n = int(input())
graph = [[] for _ in range(com+1)]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (com+1)
cnt = 0

def bfs(start):
    global cnt
    visited[start] = 1
    dq = deque()
    dq.append(start)
    while dq:
        cur = dq.popleft()
        for next in graph[cur]:
            if visited[next] == 0:
                visited[next] = 1
                dq.append(next)
                cnt+=1

bfs(1)
print(cnt)