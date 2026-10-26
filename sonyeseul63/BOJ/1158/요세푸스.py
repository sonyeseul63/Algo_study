from collections import deque
N, K = map(int, input().split())
q = deque()
yose = []
for num in range(1, N+1):
    q.append(num)
while q: #순열에 하나씩 추가하고 q에서 하나씩 빼기
    for _ in range(K-1):
        q.append(q.popleft())
    yose.append(q.popleft()) # pop한 순자가 중복일 수 있나? -> no
print("<" + ", ".join(map(str, yose)) + ">")