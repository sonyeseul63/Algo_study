N, M = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()

answer = []
visited = [0] * N

def dfs(depth):
    if depth == M:
        print(*answer)
        return

    x = 0
    for i, n in enumerate(arr):
        if not visited[i]:
            if n == x:
                continue
            visited[i] = 1
            answer.append(n)
            dfs(depth + 1)
            answer.pop()
            visited[i] = 0
            x = n

dfs(0)