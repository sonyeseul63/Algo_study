from collections import deque

N, L = map(int, input().split())
nums = list(map(int, input().split()))
dq = deque()
answer = []

for idx in range(N):
    while dq and nums[dq[-1]] > nums[idx] : dq.pop()
    dq.append(idx)

    if(dq[0] <= idx - L) : dq.popleft()

    # 이때의 덱 상태 점검!

    answer.append(str(nums[dq[0]]))

print(" ".join(answer))