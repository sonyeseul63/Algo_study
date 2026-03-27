# <연산>
# bfs, 큐
from collections import deque
T = int(input())

def bfs(start, target):
    dq = deque()
    dq.append(start)
    visited = [0] * 1000001
    visited[start]=1
    while dq:
        cn = dq.popleft()
        if cn==target:
            return (visited[cn]-1)
        for nn in [cn+1, cn-1, cn*2, cn-10]:
            if 1<=nn<=1000000 and not visited[nn]:
                dq.append(nn)
                visited[nn]=visited[cn]+1

for test_case in range(1, T + 1):
    start, target = map(int, input().split())
    result = bfs(start, target)
    print(f"#{test_case} {result}")