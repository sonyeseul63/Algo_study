from collections import deque
T = 10
for _ in range(1,T+1):
    test_case = int(input())
    q = deque(map(int, input().split()))
    minus = 0
    while True:
        minus = (minus % 5) + 1
        x = q.popleft() - minus
        if x <= 0:
            q.append(0)
            break
        else:
            q.append(x)

    print(f"#{test_case} ", *q)