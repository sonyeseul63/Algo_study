n, m = map(int, input().split())

permutation = []
visited = [0] * (n+1)

# 순열이 완성되기까지 재귀하는 함수
def bt(cur, depth): # cur: 크기 비교해야함
    if depth == m:
        print(*permutation)
        return
    for next in range(1, n+1):
        if cur < next and visited[next] == 0:
            visited[next] = 1
            permutation.append(next)
            bt(next, depth+1)
            visited[next] = 0
            permutation.pop()

bt(0, 0)