T = int(input())
# dfs: (r,c)에서 시작했을 때 갈 수 있는 방 개수(깊이 구하기)
def dfs(r, c):
    # dp: 이미 그 값을 알고 있음
    if dp[r][c] != 0:
        return dp[r][c]
    # 아니면 기본값
    else: 
        dp[r][c] = 1
    
    dr = (-1,1,0,0)
    dc = (0,0,-1,1)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # 다음 방문 노드 조건: 범위, 값
        if 0<=nr<n and 0<=nc<n:
            if rooms[nr][nc] == rooms[r][c] + 1:
                # 깊이 기본값에서 갱신
                dp[r][c] = 1 + dfs(nr,nc)
                break # 어차피 해당 위치에서 한번만 갈 수 있으니까
    return dp[r][c]
    
for test_case in range(1, T+1):
    n = int(input())
    rooms = [ list(map(int, input().split())) for _ in range(n)]
    # 해당 좌표를 시작점으로 갖는 깊이, 값이 있다는 것은 깊이 측정 완료
    dp = [ [0]*n for _ in range(n)]
    
    max_depth = 0
    for i in range(n):
        for j in range(n):
            # dp: 깊이 측정 안 한 것들 대상으로 탐색
            if not dp[i][j]:
                depth = dfs(i, j)
                if max_depth < depth:
                    max_depth = depth
                    res_num = rooms[i][j]
                elif max_depth == depth:
                    res_num = min(res_num, rooms[i][j]) # 뒤에 더 작은 숫자
    print(f"#{test_case} {res_num} {max_depth}")