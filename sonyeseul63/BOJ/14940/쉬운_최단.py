from collections import deque
# 입력
n, m = map(int, input().split())
# 2로부터의 거리, 도달못하면(초기) -1, 0은 그대로
dist = [[-1] * m for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    for j, v in enumerate(row):
        if v == 0:
            dist[i][j] = 0
        if v == 2:
            start = (i, j)

def bfs(start):
    dq = deque()
    # 시작점
    dq.append(start)
    dist[start[0]][start[1]] = 0
    
    # 이동 방향
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    while dq:
        r, c = dq.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<m and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                dq.append((nr,nc))

bfs(start)
for i in range(n):
    print(' '.join(map(str, dist[i])))