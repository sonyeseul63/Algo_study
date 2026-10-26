#햄버거 다이어트, 선택지 2가지 재귀
T = int(input())
for test_case in range(1, T+1):
    N, L = map(int, input().split())
    hams = []
    for _ in range(N):
        x, y = map(int, input().split())
        hams.append((x,y))

    # 햄버거 조합 -> 최고 경우 반환
    def dfs(i, total_fav, total_cal):
        if total_cal > L: # 무효
            return 0
        if i >= len(hams): # 현재 값을 최종 인정
            return total_fav
        
        
        pick = dfs(i+1, total_fav+hams[i][0], total_cal+hams[i][1])
        skip = dfs(i+1, total_fav, total_cal)
      

        return max(pick,skip)

    res = dfs(0,0,0)
    print(f"#{test_case} {res}")

