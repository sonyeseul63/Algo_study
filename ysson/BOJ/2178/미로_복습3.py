from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
# start ~ end칸까지 최소 이동 칸 수 반환
def bfs(start, end):
    dq = deque()
    dq.append(start)
    dr = (-1,1,0,0)
    dc = (0,0,-1,1)
    while dq:
        r,c = dq.pop()
        # 종료조건
        if (r,c) == end:
            return
        #return 다음
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            # 후보
            if 0<=nr<n and 0<=nc<m and board[nr][nc] == 1:
                    board[nr][nc] = board[r][c] + 1
                    dq.append((nr,nc))
bfs((0, 0), (n-1, m-1))
print(board[n-1][m-1])