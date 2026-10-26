from collections import deque
n = int(input())
board = [ (list(map(int, input()))) for _ in range(n) ]

# 인접한 칸도 1인지 확인하는 함수
def bfs(r, c):
    cnt = 1
    dq = deque()
    dq.append((r,c))
    board[r][c] = -1

    dr = (-1,1,0,0)
    dc=(0,0,1,-1)

    while dq:
        r, c = dq.popleft()
        for i in range(4):
            nr = dr[i]+r
            nc = dc[i]+c
            if 0<=nr<n and 0<=nc<n and board[nr][nc] == 1:
                cnt+=1
                dq.append((nr,nc))
                board[nr][nc] = -1
    
    return cnt

result = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            result.append(bfs(i, j))

print(len(result))
print("\n".join(map(str,sorted(result))))