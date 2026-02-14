from collections import deque

N = int(input())

dq = deque()

# deque을 만든다
for i in range(1, N+1):
    dq.append(i)

# 사이클을 만든다
while(len(dq) > 1):
    dq.popleft()
    dq.append(dq.popleft())

# 출력
print(dq[0])