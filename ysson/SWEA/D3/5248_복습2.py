T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    for i in range(0,len(arr),2):
        a, b = arr[i], arr[i+1]
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (n+1)
    # 인접한거 순회해서 한 덩이로 처리(공용 visited)
    def bfs(start):
        visited[start] = 1

        for next in graph[start]:
            if not visited[next]:
                bfs(next)

        return 1

    # 순회해야하는 대상: not visited
    # 적힌것이 있을경우만
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            cnt += bfs(i)

    print(f"#{test_case} {cnt}")