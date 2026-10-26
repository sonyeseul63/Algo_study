# 한줄정리:목표거리까지 1초당 접근할 수 있는 이동 3가지로 최단시간 -> BFS,time/dist 리스트로 중복방지
# 입력: 위치 N, K
# 출력: N에서 K까지의 가장 빠른 시간,
# 최단 시간 -> BFS -> 그래프, visited, 큐, 인접노드로 이동, 다음 노드의 범위
# 한 노드당 세가지 루트 (1초당) -> x-1, x+1, 2*x
# 목표: x == K
# 방문한 숫자는 다시 안가게 해야함

from collections import deque

N, K = map(int, input().split())
q = deque()
q.append(N)
time = [-1] * 100001
time[N] = 0

while(q):
    cur = q.popleft()
    if cur == K:
        print(time[K])
        break
    for n in (cur-1, cur+1, cur*2):
        if 0<=n<=100000 and time[n] == -1:
            q.append(n)
            time[n] = time[cur] + 1
        