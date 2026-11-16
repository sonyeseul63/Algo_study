T = int(input())
for i in range(T):
    test_case = int(input())
    arr = list(map(int, input().split()))

    cnt = [0] * 101
    for x in arr:
        cnt[x] += 1

    mx = 0
    ans = 0
    for j in range(101):
        if cnt[j] >= mx:
            mx = cnt[j]
            ans = j

    print(f"#{test_case} {ans}")