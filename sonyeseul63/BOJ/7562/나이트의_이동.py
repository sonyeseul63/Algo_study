from collections import deque
T = int(input())

# 최소 이동 -> bfs 이용한 순회
def bfs(start_r, start_c, target_r, target_c,l):
    dq = deque()
    dq.append((start_r, start_c))
    board[start_r][start_c] = 0

    dr = (-2,-1, 1,2,2,1,-1,-2)
    dc = (1,2,2,1,-1,-2,-2,-1)

    while dq:
        cur_r, cur_c = dq.popleft()
        if (cur_r, cur_c) == (target_r, target_c): # 문법주의: 튜플로 묶어주기
            return board[cur_r][cur_c]
    
        for idx in range(8):
            nr = dr[idx] + cur_r
            nc = dc[idx] + cur_c
            if 0<=nr<l and 0<=nc<l and board[nr][nc] < 0:
                dq.append((nr,nc))
                board[nr][nc] = board[cur_r][cur_c]+1


for test_case in range(1, T+1):
    l = int(input())
    board = [[-1] * l for _ in range(l)]
    start_r, start_c = map(int, input().split())
    target_r, target_c = map(int, input().split())
    print(bfs(start_r, start_c, target_r, target_c,l))