T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    board = [[0] * n for _ in range(n)]
    
    # 좌표 이동(우, 하, 좌, 상)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # 달팽이 숫자 만들기 (방향 전환의 트리거? 0이 아니거나 범위 오버)
    cr, cc= 0, 0
    i = 0 #i는 방향
    for now in range(1, (n*n)+1):
        # 현재 값 넣기
        board[cr][cc] = now
        # 같은 방향에서의 다음 자리
        nr = cr + dr[i]
        nc = cc + dc[i]
        # 유효성 검사
        if nr<0 or nr>=n or nc<0 or nc>=n or board[nr][nc] != 0:
            # 방향(i) 바꾸고 다음 자리
            i = (i + 1) % 4
            nr = cr + dr[i]
            nc = cc + dc[i]
        # 다음 자리를 현재로
        cr = nr
        cc = nc

    # 출력
    print(f"#{test_case}")
    for i in range(n):
        print(*board[i])