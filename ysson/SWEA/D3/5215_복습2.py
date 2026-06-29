# 조건있는 조합하기
# 조합? -> 선택/미선택으로 경로 선택
T = int(input())
for test_case in range(1, T+1):
    N, L = map(int,input().split())
    hams = {}
    for _ in range(N):
        a, b = map(int, input().split())
        hams.append((a,b))

    # 가능한 햄버거 조합 만들고 그 중 total_fav가 높은거 반환한다 
    def dfs(depth, total_fat, total_fav):
        if total_fat > L:
            # L보다 초과한 루트 : 무효의 경우, 돌아가
            return 0
        
        if depth == len(hams):
            # 루트 끝의 경우, 유효인 채 돌아가, 잘만들어진 경우는 total_fav를 반환한다
            return total_fav
        
        # 현재까지의 total_fat, total_fav를 다음 거에 보낸다.
        yes = dfs(depth+1, total_fat + hams[depth][1], total_fav + hams[depth][0])
        no = dfs(depth+1, total_fat, total_fav)
        best = max(yes, no)
        return best
    
    res = 0
    res = dfs(0, 0, 0)
    print(f"#{test_case} {res}")