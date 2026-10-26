# 이미 주어진 격자와 아이템(NxN, 3<N<1001)
# 아이템을 빈칸에 추가하면 그 추가된 아이템의 점수 + 인접한 아이템의 점수가 바뀜

# 입력
N = int(input())
grid = []
for _ in range(N):
    grid.append(list(map(int,input().split())))
target = int(input())

# 변수
origin_total = 0
max_delta = 0
delta = 0

# 격자 이동 탐색 (상하좌우/대각선)
dr = (1, -1, 0, 0, -1, -1, 1, 1)
dc = (0, 0, -1, 1, -1, 1, -1, 1)

# 격자 순환 (+:2, x:1, *:3)
for r in range(N):
    for c in range(N):
        if grid[r][c] == 2: #십자기
            for i in range(0, 4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<N and 0<=nc<N:
                    if grid[nr][nc] > 0:
                        origin_total += 1
        elif grid[r][c] == 1: #곱하기
            for i in range(4, 8):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<N and 0<=nc<N:
                    if grid[nr][nc] > 0:
                        origin_total += 1
        elif grid[r][c] == 3: #star
            for i in range(0, 8):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<N and 0<=nc<N:
                    if grid[nr][nc] > 0:
                        origin_total += 1

        else: # 0
            delta = 0
            # 새로운 아이템
            if target == 1: # 곱하기
                for i in range(4, 8):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0<=nr<N and 0<=nc<N:
                        if grid[nr][nc] > 0:
                            delta += 1
            elif target == 2: # 십자가
                for i in range(0, 4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0<=nr<N and 0<=nc<N:
                        if grid[nr][nc] > 0:
                            delta += 1
            elif target == 3: # 스타
                for i in range(0, 8):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0<=nr<N and 0<=nc<N:
                        if grid[nr][nc] > 0:
                            delta += 1
            
            # 인접한 기존 아이템
            for i in range(0,8):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<N and 0<=nc<N:
                    if grid[nr][nc] == 2 and i in range(0,4):
                        delta +=1
                    if grid[nr][nc] == 1 and i in range(4,8):
                        delta += 1
                    if grid[nr][nc] == 3:
                        delta += 1

            if delta > max_delta:
                max_delta = delta
print(max_delta + origin_total)