# 햄버거 다이어트, 조합
T = int(input())
for test_case in range(1, T+1):
    N, L = map(int, input().split())
    hams = []
    for _ in range(N):
        x, y = map(int, input().split())
        hams.append((x,y))

    # 끝이아니면 끝일때 까지 재귀를 거치며 총 best를 반환
    def dfs(start, total_fav, total_cal):
        if total_cal > L:
            return 0
        # best: 현재에서의 최선
        best = total_fav
        for i in range(start, N):
            best = max(
                best,
                dfs(i + 1, total_fav + hams[i][0], total_cal + hams[i][1])
            )
        return best
    
    res = dfs(0,0,0)
    print(f"#{test_case} {res}")