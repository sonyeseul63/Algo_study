# 입력: N개의 격좌와 1, 0
# 출력: 인접요소 + 각 요소의 개수
from collections import deque

N = int(input().strip())
board = [ list(map(int, input().strip())) for _ in range(N)]
num = []

dx = (-1,1,0,0)
dy = (0,0,1,-1)

def bfs(x, y):
    q = deque()
    q.append((x, y))
    board[x][y] = 0
    num_cnt = 1
    while q:
        x, y = q.popleft()
        for n in range(4):
            nx = x + dx[n]
            ny = y + dy[n]
            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny] == 1:
                    q.append((nx,ny))
                    board[nx][ny] = 0
                    num_cnt+=1
    return num_cnt


for i in range(N): # 행
    for j in range(N): # 열
        if board[i][j] == 1:
            num.append(bfs(i, j))

num.sort()
print(len(num))
print("\n".join(map(str, num)))