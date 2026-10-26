# N장의 카드, 1 ~ N 순대로
# 반복 행동: 위에있는 거 버리기 + 그 다음거 젤 밑으로
# 출력: 제일 마지막에 남는 카드

from collections import deque

N = int(input())
dq = deque()
for n in range(N):  
    dq.append(n+1)

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())
    
print(dq[0])
