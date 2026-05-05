# 인접 노드(연결리스트) 구하기 -> dfs
T = int(input())

# 인접 노드 처리
def dfs(node):
    visited[node] = 1
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)

for test_case in range(1, T+1):
    n, m = map(int, input().split())

    # n개의 인접 리스트 생성
    graph = [ [] for _ in range(1+n)]
    visited = [0] * (n+1)

    # m개의 쌍 처리
    arr = list(map(int, input().split()))
    for idx in range(m):
        # 인덱스와 값 매핑
        u, v = arr[2*idx], arr[2*idx + 1]
        graph[u].append(v)
        graph[v].append(u)
    
    # 인접노드 개수 구하기
    result = 0
    for stu in range(1, n+1):
        if not visited[stu]:
            dfs(stu)
            result += 1
    
    # 결과 출력
    print(f"#{test_case} {result}")