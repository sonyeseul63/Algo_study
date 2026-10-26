from collections import deque
# 입력
row, col = map(int, input().split())
board = []
for _ in range(row):
    l = list(map(int, input()))
    board.append(l)

# dist 생성(3차원 배열, dist[x][y] = [_, _])
dist = [[[-1]*2 for _ in range(col)] for _ in range(row)]

# bfs 함수(가장 먼저 도착한게 최단 거리)
def bfs(r, c, state):
    dq = deque()

    # 초기값 처리
    dist[r][c][state] = 1
    dq.append((r, c, state))

    while dq:
        cr, cc, state = dq.popleft()
        # 현재 노드가 도착지인지
        if (cr, cc) == (row-1, col-1):
            return dist[cr][cc][state]

        # 아니면: 현재 노드 기준 다음 노드 탐색
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1,1]
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0<=nr<row and 0<=nc<col: # 다음 노드 범위 유효성

                # 벽 부시기(부신 상태 갱신)
                if board[nr][nc] == 1 and state == 0:
                    if dist[nr][nc][1] < 0: # 다음 노드 방문 여부
                        dist[nr][nc][1] = dist[cr][cc][state] + 1 # 다음 노드 탐색 처리
                        dq.append((nr, nc, 1)) # 다음 노드 후보에 추가

                # 벽 안 부시기(부신 상태 상속)
                if board[nr][nc] == 0:
                    if dist[nr][nc][state] < 0: # 다음 노드 방문 여부
                        dist[nr][nc][state] = dist[cr][cc][state] + 1 # 다음 노드 탐색 처리
                        dq.append((nr, nc, state)) # 다음 노드 방문 여부

    # 못갔을 때 -1 출력
    return -1

print(bfs(0, 0, 0))