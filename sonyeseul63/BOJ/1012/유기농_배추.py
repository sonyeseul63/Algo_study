# 입력: T(test case)/ M x N (table)/ K(num of 배추)/ X, Y (위치 좌표)
# 출력: 입력받은 좌표 기반으로 인접요소 구하기

from collections import deque

# 좌표탐색 도우미
dx = (-1,1,0,0)
dy = (0,0,1,-1)

# bfs 이유: 입력 값 크기는 널널하지만 안정성을 위해
# board를 인자로 받아서 조작한다
def bfs(board, x,y, M, N):
    q = deque()
    q.append((x,y))
    board[y][x] = 0

    while(q):
        cx, cy = q.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < M and 0 <= ny < N and board[ny][nx] == 1:
                board[ny][nx] = 0
                q.append((nx, ny))


T = int(input().strip())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = [ [0]*M for _ in range(N)]
    for _ in range(K):
        X, Y  = map(int, input().split())
        board[Y][X] = 1
    count = 0
    for y in range(N):
        for x in range(M):
            if board[y][x] == 1:
                bfs(board, x, y,M,N)
                count+=1
    print(count)

# 오답 주의: board의 격자 board[y][x]