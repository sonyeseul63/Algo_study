T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))

    ans = 0
    mx = 0

    for x in reversed(price):
        if x > mx:
            mx = x
        else:
            ans += (mx - x)

    print(f'#{test_case} {ans}')