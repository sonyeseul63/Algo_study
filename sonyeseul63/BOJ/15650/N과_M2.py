N, M = map(int, input().split())

arr = []
visited = [0] * (N+1)

def dfs(x, depth):
    if(depth == M): 
        print(*arr)
        return

    for next in range(x+1, N+1):
        if not visited[next]:
            visited[next] = 1
            arr.append(next)
            dfs(next, depth+1)
            arr.pop()
            visited[next] = 0

dfs(0, 0)
