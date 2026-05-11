T = 10
for test_case in range(1, T+1):
    num = int(input())
    buildings = list(map(int, input().split()))
    res = 0
    for n in range(2, num-2):
        high = max(buildings[n-2], buildings[n-1], buildings[n+1], buildings[n+2])
        if buildings[n] > high:
            res += (buildings[n] - high)
    print(f"#{test_case} {res}")