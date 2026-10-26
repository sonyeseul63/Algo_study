N, M = map(int, input().split())

graph = [ [] for _ in range(N) ]
visited = [0] * N #사람 수 만큼
flag = False

for _ in range(M): # 관계 수
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, visitCount):
    global flag
    # 종료조건이 2개..? 
    if flag: 
        return

    if visitCount == 5: 
        flag = True
        return
    
    visited[x] = 1
        
    for next in graph[x]:
        if not visited[next]:
            dfs(next, visitCount+1)
    visited[x] = 0

for n in range(N): # 사람 수
    dfs(n, 1)
    if flag:
        break

print (1 if flag else 0)