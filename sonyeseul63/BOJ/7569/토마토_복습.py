from collections import deque

M, N, H = map(int, input().split())
box = []
zeros = 0 # 안익은 토마토 개수
dq = deque() # 익은 토마토 좌표(탐색 후보)
days = 0 # 익는데 걸린 시간

for h in range(H): # 높이
    layer = []
    for n in range(N): # 세로, 한 줄씩 체크
        row = list(map(int, input().split()))
        layer.append(row)

        for m, v in enumerate(row):
            if v==0: zeros+=1
            if v==1: dq.append((h,n,m))
    box.append(layer)

if zeros==0: #안익은 토마토 없으면 0 출력 후 종료
    print(0)
    exit()

dh = (-1,1,0,0,0,0)
dr = (0,0,-1,1,0,0)
dc = (0,0,0,0,-1,1)

while dq:
    cur_h, cur_r, cur_c = dq.popleft()
    for i in range(6):
        nh = cur_h + dh[i]
        nr = cur_r + dr[i]
        nc = cur_c + dc[i]
        if 0<=nh<H and 0<=nr<N and 0<=nc<M:
            if box[nh][nr][nc]==0:
                dq.append((nh, nr, nc))
                box[nh][nr][nc]=box[cur_h][cur_r][cur_c]+1
                days = box[nh][nr][nc]
                zeros-=1

if zeros > 0: 
    print(-1)

else:
    print(days-1)