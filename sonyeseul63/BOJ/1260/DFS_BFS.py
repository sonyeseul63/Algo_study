from collections import deque
N, M, V = map(int, input().split())

graph = [ [] for _ in range(N+1) ]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, N + 1):
    graph[i].sort()

visited_dfs = [0] * (N+1)
arr_dfs = []

def dfs(x): 
    visited_dfs[x] = 1
    arr_dfs.append(x)
    
    for next in graph[x]:
        if not visited_dfs[next]:
            dfs(next)

visited_bfs= [0] * (N+1)
arr_bfs = []

def bfs(x): 
    queue = deque([x])
    visited_bfs[x] = 1
    while queue: # 큐 방문
        curr = queue.popleft() # 2. 큐에서 빼기 + 할 일 하기
        arr_bfs.append(curr) 
    
        for next in graph[curr]: # 1. 새끼들 방문 & 큐에 넣기
            if not visited_bfs[next]:
                visited_bfs[next] = 1 #(재귀가 아님)중복체크, 두번 큐에 안넣도록
                queue.append(next)

dfs(V)
bfs(V)
print(*arr_dfs)
print(*arr_bfs)