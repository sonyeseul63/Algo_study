# 만들 수 있는 모든 경우의 수 (중복됨)
n, m = map(int, input().split())
perm = []

def dfs(depth):
    if depth == m:
        print(" ".join(map(str, perm)))
        return
    
    for num in range(1, n+1):
        perm.append(num) # 현재 depth 처리
        dfs(depth+1) # 다음으로 넘기기
        perm.pop()

dfs(0)