# 입력받은 자료 -> 그래프 표현: 인접리스트 (가변)
# 큰 for로 전체 노드 순회
# 방문 안된 거에 DFS 시작
# BFS 에서 방문체크
# visited 전역 관리

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)] # 한 행씩 생성
visited = [0]*(N+1)

# 그래프 표현
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 재귀적 탐방
def dfs(x):
    visited[x] = 1

    for next in graph[x]:
        if not visited[next]:
            dfs(next)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)