# <그룹 나누기>
# dfs, 연결요소(연결리스트)
T = int(input())

def dfs(node): # 해당 노드의 연결 요소 방문처리
    visited[node] = 1
    for next in graph[node]:
        if not visited[next]:
            dfs(next)

for test_case in range(1, T + 1):
    n, ap = map(int, input().split())

    #전역으로 관리
    graph = [[] for _ in range(n+1)] 
    visited = [0] * (n+1) 

    arr = list(map(int, input().split()))
    for i in range(0, len(arr), 2):
        u, v = arr[i], arr[i+1]
        graph[u].append(v)
        graph[v].append(u)

    cnt = 0
    for i in range(1, len(graph)):
        if not visited[i]:
            dfs(i)
            cnt+=1
    
    print(f"#{test_case} {cnt}")
