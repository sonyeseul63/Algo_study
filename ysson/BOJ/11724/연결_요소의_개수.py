N, M = map(int, input().split())

graph = [ [] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)
count = 0
def dfs(x):
    visited[x] = 1

    for next in graph[x]:
        if not visited[next]:
            dfs(next)

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)