T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = []

    for x in range(1, N + 1):
        num = [0] * x
        arr.append(num)

    for r in range(N):
        for c in range(r + 1):
            if c == 0 or c == r:
                arr[r][c] = 1
            else:
                arr[r][c] = arr[r - 1][c - 1] + arr[r - 1][c]

    print(f"#{test_case}")
    for r in range(N):
        print(*arr[r])