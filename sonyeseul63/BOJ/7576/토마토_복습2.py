# 0 -> 1로 만들어야함, 
# 만드는 법: 1이 한번에 한칸씩 0을 1로 만듬
from collections import deque
n, m = map(int, input().split())
cnt = 0 # 안익은 토마토 개수
box = [] # 날짜 저장
tomatos = deque()

for i in range(m):
    l = list(map(int, input().split()))
    for j, v in enumerate(l):
        if v == 0:
            cnt += 1
        if v == 1:
            tomatos.append((i, j))
    box.append(l)

day = 0
if cnt > 0:
    # 토마토 확산 방향(4방향)
    dr = (-1, 1, 0, 0)
    dc = (0,0,-1,1)

    # 토마토 다 익는데 걸린 시간
    while tomatos:
        r, c = tomatos.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<m and 0<=nc<n and box[nr][nc] == 0:
                box[nr][nc] = box[r][c] + 1
                tomatos.append((nr,nc))
                day = max(day, box[nr][nc])
                cnt -= 1
    # 다 익음
    if cnt == 0:
        print(day-1)
    # 다 안익음
    else:
        print(-1)
else:
    print(day)