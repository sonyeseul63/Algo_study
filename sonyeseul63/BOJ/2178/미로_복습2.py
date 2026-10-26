from collections import deque

N, M = map(int, input().split())
arr = [ list(map(int, input())) for _ in range(N) ]

def bfs(start):
    dq = deque()
    dq.append(start)
    while dq:
        cur_r, cur_c = dq.popleft()
        if (cur_r, cur_c) == (N-1, M-1):
            return arr[cur_r][cur_c]
        dr = (-1,1,0,0)
        dc = (0,0,-1,1)
        for i in range(4):
            nr = dr[i]+cur_r
            nc = dc[i]+cur_c
            if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 1:
                arr[nr][nc] = arr[cur_r][cur_c] + 1
                dq.append((nr,nc))

print(bfs((0,0)))