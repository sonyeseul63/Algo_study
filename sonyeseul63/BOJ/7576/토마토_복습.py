from collections import deque

M, N = map(int, input().split())
arr = []
zeros = 0
dq = deque()
for i in range(N):
    row = list(map(int, input().split()))
    # row list 하나씩 순회 -> 0갯수, 1위치 수집
    for j, value in enumerate(row):
        if value == 0:
            zeros+=1
        if value == 1:
            dq.append((i,j))
    #row lsit 를 arr에 추가
    arr.append(row)

if zeros == 0:
    print(0)
    exit()

days = 0
dr = (-1,1,0,0)
dc = (0,0,-1,1)
while dq:
    cur_r, cur_c = dq.popleft()
    for i in range(4):
        nr = cur_r+dr[i]
        nc = cur_c+dc[i]
        if 0<=nr<N and 0<=nc<M and arr[nr][nc]==0:
            arr[nr][nc]=arr[cur_r][cur_c]+1
            zeros-=1
            dq.append((nr,nc))
            if days < arr[nr][nc]:
                days = arr[nr][nc]
if zeros > 0:
    print(-1)
else:
    print(days-1)