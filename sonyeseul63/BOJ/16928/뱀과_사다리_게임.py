from collections import deque
N, M = map(int, input().split())
jumps = {}
for _ in range(N+M):
    start, end = map(int, input().split())
    jumps[start] = end
visited = [0] * 101
def bfs(start):
    dq = deque()
    dq.append(start)
    # visited[start] = 1
    while(dq):
        cur = dq.popleft()
        if cur == 100:
            return visited[cur]
        for i in range(1, 7):
            next = cur + i
            if next > 100:
                continue
            if next in jumps:
                next = jumps[next]
            if not visited[next]:
                dq.append(next)
                visited[next] = visited[cur] + 1
print(bfs(1))