# M x N 지도, 칸에 정수가 적힘
# 주사위 놓인 좌표 (x, y), 0이 적힘 -> 1차원 리스트
# (x, y)에 적힌 수 : 0 -> board(x, y) = 주사위의 바닥면의 수
#                 0이 아니면 -> 주사위의 바닥면 수 = board(x,y), 칸의수 = 0
# 명령: 좌표 이동
# 출력: 주사위가 이동했을 때마다 상단에 쓰인 수
# 범위내에서만 이동, 범위 벗어나면 출력도 x
# 변수명으로 map 주의

N, M, r, c, K = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N) ]
orders = list(map(int, input().split()))
dice = [0,0,0,0,0,0] # 0:위, 1:아래, 2:앞, 3:뒤, 4:오른, 5:왼
dr = (0,0,0,-1,1)
dc = (0,1,-1,0,0)

# 주어진 방향에 따라
for n in orders:
    # 지도의 좌표 이동
    nr, nc = r + dr[n], c + dc[n] # nr, nc 후보
    if 0 <= nr < N and 0<=nc < M:
        # nr, nc (후보) -> 값
        r, c = nr, nc
        # 주사위 굴리기
        if n==1: # 동
            dice[0],dice[4],dice[1],dice[5]=dice[5],dice[0],dice[4],dice[1]
        if n==2: # 서
            dice[0],dice[4],dice[1],dice[5]=dice[4],dice[1],dice[5],dice[0]
        if n==3: # 북
            dice[0],dice[2],dice[1],dice[3]=dice[3],dice[0],dice[2],dice[1]
        if n==4: # 남
            dice[0],dice[2],dice[1],dice[3]=dice[2],dice[1],dice[3],dice[0]
    
        # 규칙
        if not board[r][c]:
            board[r][c] = dice[1]
        else:
            dice[1] = board[r][c]
            board[r][c] = 0
        print(dice[0])