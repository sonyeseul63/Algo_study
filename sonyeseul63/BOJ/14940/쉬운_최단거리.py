from collections import deque
n, m = map(int, input().split())
grid = []
dist = [[-1]*m for _ in range(n)]
for i in range(n):
    row = list(map(int, input().split()))
    for j, v in enumerate(row):
        if v == 2:
            (target_r, target_c) = (i, j)
        # 0인부분은 0으로 출력 유지해야함. (-1로 초기화 했을때 방문할때 0으로 바꾸면 방문안할떈.?)
        if v == 0:
            dist[i][j] = 0
    grid.append(row)
dr = (-1,1,0,0)
dc = (0,0,-1,1)

def bfs(target_r, target_c): # 인자로 2의 좌표를 받음
    dist[target_r][target_c] = 0
    dq = deque()
    dq.append((target_r, target_c))
    while dq:
        cur_r, cur_c = dq.popleft()
        for i in range(4):
            next_r = dr[i]+cur_r
            next_c = dc[i]+cur_c

            if 0<=next_r<n and 0<=next_c<m:
                if grid[next_r][next_c] == 0:
                    dist[next_r][next_c]=0
                    continue
                if dist[next_r][next_c]==-1:
                    dist[next_r][next_c] = dist[cur_r][cur_c]+1
                    dq.append((next_r, next_c))

bfs(target_r, target_c)
for i in range(n):
    print(" ".join(map(str, dist[i])))