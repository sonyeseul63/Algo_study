T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    # 그래프 입력
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    # 인접노드로 이동해서 start로부터 최장 루트(정점 개수
    visited = [0] * (N+1) # 방향을 잡기위해서, 이전에 쓴 값 선택 못하게
    def dfs(start):
        best = 1 # 경로에서 정점이 start 하나여도 길이는 1
        for j in graph[start]:
            if not visited[j]:
                visited[j] = 1
                best = max(best, 1 + dfs(j)) # 1+dfs(j) : 지금부터 끝까지 경로 수
                visited[j] = 0
        return best
    
    # 시작점에 따른 길이 중 최장 구하기
    res = 0
    for i in range(1, N+1):
        visited[i] = 1
        res = max(res, dfs(i))
        visited[i] = 0
            

    
    print(f"#{test_case} {res}")