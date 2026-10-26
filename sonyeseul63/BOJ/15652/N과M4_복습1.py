# 중복허용, 순열이 증가하거나 같게
n, m = map(int, input().split())
perm = []

def bfs(start, depth):
    if depth == m:
        print(" ".join(map(str, perm)))
        return
    
    for num in range(start, n+1):
        perm.append(num)
        bfs(num, depth+1)
        perm.pop()

bfs(1, 0)