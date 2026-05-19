# 오름차순 수열, 중복 안됨
n, m = map(int, input().split())
perm = []

# 현재 재귀 호출 = 현재 depth 자리에 들어갈 후보 탐색 + 다음 자리 재귀
def dfs(start, depth):
    # 종료
    if depth == m:
        print(' '.join(map(str, perm)))
        return

    # 현재 depth 처리, 다음으로 넘김
    for num in range(start+1, n+1):
        perm.append(num)
        dfs(num, depth+1)
        perm.pop()
dfs(0, 0)