# N x M 격좌와 0, 1
# (1,1) -> (N, M) 최소 칸 개수
# 같은 거리끼리 병렬적으로 실행 -> 먼저 (N, M)에 도착한 거의 칸 개수
from collections import deque

N, M = map(int, input().split())
board = [ list(map(int, input().strip())) for _ in range(N)]

dx = (-1,1,0,0)
dy = (0,0,1,-1)

def bfs(x, y): # x은 행, y은 열
    q = deque()
    q.append((x, y))

    while q:
        cx, cy = q.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0<= nx < N and 0 <= ny < M:
                if board[nx][ny] == 1:
                    q.append((nx, ny))
                    board[nx][ny] = board[cx][cy] + 1
                    if nx == (N-1) and ny == (M-1):
                        return board[nx][ny]

print(bfs(0, 0))