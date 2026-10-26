from collections import deque

N, L = map(int, input().split())
arr = list(map(int, input().split()))

dq = deque() # heap?
ans = []

for i, v in enumerate(arr):
    # 큐에 비교해서 넣는 경우, 그냥 넣는 경우
    while dq and arr[dq[-1]] >= v:
        dq.pop()

    dq.append(i) # append를 if 전? 후? 후 할 때 주의점
    
    if dq[0] <= (i - L):
        dq.popleft() # while이 아니라 if인 이유?

    ans.append(arr[dq[0]])

print(*ans)