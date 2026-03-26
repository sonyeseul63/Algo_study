# 상태를 체크해야할 경우
from collections import deque
N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
dist = [[[-1]*2 for _ in range(M)] for _ in range(N)]
dr = (-1,1,0,0)
dc = (0,0,-1,1)
def bfs(r,c,state):
    dq = deque()
    dq.append((r,c,state))
    dist[r][c][state] = 1
    while dq:
        cur_r, cur_c, state = dq.popleft()
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0<=nr<N and 0<=nc<M: # 범위 체크
                if board[nr][nc]==1 and state==0: # 벽 부순 상태
                    if dist[nr][nc][1]<0: # 방문 체크
                        dist[nr][nc][1] = dist[cur_r][cur_c][state]+1
                        dq.append((nr,nc,1))
                elif board[nr][nc]==0:
                    if dist[nr][nc][state]<0:
                        dist[nr][nc][state] = dist[cur_r][cur_c][state]+1
                        dq.append((nr,nc,state))
bfs(0,0,0)
a, b = dist[N-1][M-1]

if a == -1 and b == -1:
    print(-1)
elif a == -1:
    print(b)
elif b == -1:
    print(a)
else:
    print(min(a, b))