# bfs ? dfs? max갱신, 다음 수에 대한 제약..
# 인접노드 영역과 비슷
# 탐색 순서 (0,0)? 1? -> dfs 밖에서 제어
# 3->4->5에서 4->5는 안봐도됨: visited로 관리
# 안봐도 되는게 아니라 4->5를 이용한다
# 정보: 시작점, 몇번갔는지 -> 변수로 관리, 몇번갔는지는 visited로 dfs에서 계산
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*(n) for _ in range(n)] # 숫자별로 관리? 좌표별로 관리?->숫자는 직접 꺼내야하잖아

    # dfs : (r, c)에서 출발해 그 깊이 구하기
    def dfs(r, c):
        # 현재거 처리
        # 이미 방문한 값
        if visited[r][c] > 0:
            return visited[r][c]
        
        # 처음 방문: 1로 초기화 후 
        visited[r][c] = 1
        # 다음 탐색
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 조건에 들어오는지: 범위 안
            if 0<=nr<n and 0<=nc<n:
                # 조건에 들어오는지: 1보다 큰 수
                if room[nr][nc] == room[r][c] + 1:
                    visited[r][c] += dfs(nr, nc)
                    # 타겟 발견, 더이상 탐색할 필요 없음
                    break
        # (r, c)의 깊이 반환        
        return visited[r][c]
    
    md = 0 # depth
    mn = 0 # room[i][j]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                depth = dfs(i,j)
                # depth 가 최대인지
                if depth > md:
                    mn = room[i][j]
                    md = depth
                # 최대인 것이 또 있는지 -> mn 비교
                elif depth == md:
                    mn = min(mn, room[i][j])

    print(f"#{test_case} {mn} {md}")    