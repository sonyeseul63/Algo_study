for _ in range(10):
    test_case = int(input())
    board = []
    for i in range(100):
        arr = list(map(int, input().split()))
        for j, v in enumerate(arr):
            if v == 2:
                start = j
        board.append(arr)
    
    # board[99][99]에서 시작해서 역추적해서 row = 0일때의 col
    def dfs(r, c):
        if r == 0:
            return c

        # 다음 것 중 좌우만 따로 한꺼번에 처리
        if 0<=c-1 and board[r][c-1] == 1:
            while c-1>=0 and board[r][c-1]==1:
                c-=1
        elif c+1 < 100 and board[r][c+1] == 1:
            while c+1 <100 and board[r][c+1]==1:
                c+=1 
        # 좌우 없으면 위로, 
        return dfs(r-1, c)
    
    target = dfs(99, start)
    print(f"#{test_case} {target}")