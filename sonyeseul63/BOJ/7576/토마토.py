from collections import deque

M, N = map(int, input().split())

zeros = 0
grid = []
q = deque()
for i in range(N):
    row = list(map(int, input().split()))
    for j, value in enumerate(row):
        if value == 0:
            zeros += 1
        if value == 1:
            q.append((i,j)) #좌표를 집어넣음
    grid.append(row)
dr = [-1,1,0,0]
dc = [0,0,-1,1]

if zeros == 0:
    print(0)
    exit()

day = 0
while q:
    r, c = q.popleft() # (r,c) 인접토마토를 다 익힐 거임
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0<=nr<N and 0<=nc<M and grid[nr][nc]==0:
            grid[nr][nc] = grid[r][c] + 1
            zeros -= 1
            if grid[nr][nc]>day: day = grid[nr][nc]
            q.append((nr, nc))

if zeros > 0:
    print(-1)
else:
    print(day-1)