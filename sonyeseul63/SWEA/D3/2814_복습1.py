T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0] * (N+1) # 한 경로 탐색할 때 방향잡기 위해 (되돌아가기 x)
    # dfs: 해당 시작점에서 가장 긴 경로 반환
    def dfs(start, depth):
        best = depth
        for next in graph[start]:
            if not visited[next]:
                visited[next] = 1
                best = max(best, dfs(next, depth+1)) # 현재까지의 경로와, 더 있는 경우 비교
                visited[next] = 0
        return best

    res = 0
    # 정점마다 시작점으로 하여 dfs 호출, 반환값중 최대값
    for i in range(1, N+1):
        visited[i] = 1
        res = max(res, dfs(i, 1))
        visited[i] = 0
    
    print(f"#{test_case} {res}")