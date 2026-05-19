# 중복없이, 순서 구하기
# visited 배열, 자릿수 -> depth
n, m = map(int, input().split())
visited = [False] * (n+1)
perm = []

# perm 만들기
def dfs(depth):
    if depth == m:
        print(' '.join(map(str,perm)))
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            perm.append(i)
            visited[i] = True
            dfs(depth+1)
            visited[i] = False
            perm.pop()

dfs(0)