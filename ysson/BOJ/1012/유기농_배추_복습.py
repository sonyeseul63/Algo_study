from collections import deque
# 입력이 grid가 아니라 의미있는 칸의 위치
test_case = int(input())

def bfs(row, col, M, N):
    dq = deque()
    dq.append((row,col))
    board[row][col] = -1

    dr = (-1,1,0,0)
    dc = (0,0,-1,1)

    while dq:
        r, c = dq.popleft()
        for idx in range(4):
            nr = dr[idx] + r
            nc = dc[idx] + c
            if 0<=nr<N and 0<=nc<M and board[nr][nc] == 1:
                board[nr][nc] = -1
                dq.append((nr,nc))


for case in range(1, test_case+1):
    M, N, K = map(int, input().split())
    board = [([0] * M) for _ in range(N)]
    for _ in range(K):
        i, j = map(int, input().split())
        board[j][i] = 1 # 인덱스 주의

    cnt = 0
    for i in range(M):
        for j in range(N):
            if board[j][i] == 1:
                bfs(j, i, M, N)
                cnt += 1

    print(cnt)