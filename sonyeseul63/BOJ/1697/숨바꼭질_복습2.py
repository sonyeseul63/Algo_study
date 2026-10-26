from collections import deque
N, K = map(int, input().split())
time = [-1] * 100001 # 아에 방문안한것 : -1

#가장 빠른 시간 -> 최단 거리 -> BFS로 탐색
def bfs(start):
    dq = deque()
    dq.append(start)
    time[start] = 0
    
    while dq:
        cur = dq.popleft()
        if cur == K:
            print(time[cur])
            return
        # 한 이동에 필요한 가짓수 3개
        for next in [cur-1, cur+1, 2*cur]: 
            if 0<=next<=100000 and time[next]==-1: # 중복가능?
                dq.append(next)
                # 현재위치 기준, 다음 칸의 시간은 + 1, 고유의 값
                time[next] = time[cur] + 1
     
bfs(N)
