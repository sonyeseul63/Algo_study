# 한 줄 정리: 3차원 격자 멀티적으로 전파
# M(가로), N(세로), H(높이) 
#      -> box[z][x][y]
# 토마토 상태 : 1(익음), 0(익지 않음), -1(없음) 
#      ->(상태변화) 0에서 1로, -1은 무시
# 1 주위 인접한 곳: 6개 
#      -> 이동 방향 6 방향
# 하루 지나면 1 주위 인접한 토마토 1됨 
#      -> bfs 레벨 달라질때마다 +1, 시작점 여러개
# 출력: 며칠인지, 0(이미 모두 익음), -1(어차피 다 못익음)
#      -> 날짜 세기-> 값 덮어쓰기
#      -> 다 돌았는데 0이 있음-> -1
#      -> 처음에 0이 없음 -> 0
# 출력에 max_day 갱신방법이 있음
from collections import deque

M, N, H = map(int, input().split())

box = []
cnt_0 = 0
q = deque()

for z in range(H): #높이
    layer = []
    for y in range(N): #행
        row = list(map(int, input().split()))
        layer.append(row)

        for x, n in enumerate(row):
            if n == 0: cnt_0 += 1
            if n == 1: q.append((z,y,x))

    box.append(layer)

dz = (-1,1,0,0,0,0)
dy = (0,0,-1,1,0,0)
dx = (0,0,0,0,-1,1)

day = 0
if cnt_0 == 0: print(0)
else:
    while q:
        cz, cy, cx = q.popleft()
        for d in range(6):
            nz, ny, nx = cz+dz[d], cy+dy[d], cx+dx[d]
            if 0<=nz<H and 0<=nx<M and 0<=ny<N:
                if box[nz][ny][nx] == 0:
                    q.append((nz,ny,nx))
                    box[nz][ny][nx] = box[cz][cy][cx] + 1
                    if day < box[nz][ny][nx]:
                        day = box[nz][ny][nx]
                    cnt_0 -= 1

    if cnt_0 > 0: print(-1)
    else:
        print(day-1)
