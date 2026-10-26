# 각 경로에 대해 최단 거리 (노드 수) -> bfs or 백트래킹(최소 갱신)
T = int(input())

# bt의 의미: 현재 idx에 있고 cnt만큼 교환했다. arr[idx]만큼 갈 수 있다.
def bt(idx, cnt):
    global min_cnt

    # 되돌아가기: 현재까지의 cnt가 최소보다 크거나 같다
    if cnt >= min_cnt:
        return
    
    # 현재 위치에서 용량만큼 가면 도착인지
    if idx + arr[idx] >= end_point:
        min_cnt = cnt
        return
        
    # 다음 단계
    for n in range(arr[idx], 0, -1):
        bt(idx + n, cnt + 1)
   

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    end_point = arr[0]
    min_cnt = end_point
    bt(1, 0)
    print(f"#{test_case} {min_cnt}")