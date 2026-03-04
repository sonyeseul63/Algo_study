# 한 줄 정리: dfs처럼 보였지만 그냥 좌표기반 구현, 방향회전 구현
# N, M : 방의 크기 (0,0) ~ (N-1, M-1)
# (r, c): 시작점, d-> 0,1,2,3:북쪽부터 시계방향
# 0: 청소x, 1:벽
# 출력: 청소횟수
# 멈추는 경우: 후진했더니 벽

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# d = 0:북, 1:동, 2:남, 3:서
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

clean = 0

# 아 로직이 정리가 잘안됨.ㅠ
while(True):
    # 1. 현재 칸 청소
    if room[r][c] == 0:
        room[r][c] = 2
        clean+=1

    go = 0

    # 왼쪽부터 주위 탐색 
    for _ in range(4): 
        # 방향을 바꿈 (d를 수정)
        d = (d+4-1)%4
        nr = r+ dr[d]
        nc = c+ dc[d]
        if 0<= nr < N and 0<= nc<M:
            if room[nr][nc] == 0:
                go = 1
                r, c = nr, nc
                break

    # 후진
    if go == 0:
        #방향은 그대로 후진 (d는 그대로)
        nd = (d+2)%4
        nr = r + dr[nd]
        nc = c + dc[nd]
        # 벽이 있으면 종료
        if room[nr][nc] == 1:
            break
        else:
            r, c = nr, nc

print(clean)     
                    
