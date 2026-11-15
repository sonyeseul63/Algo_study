
for test_case in range(1, 11):
    N = int(input())
    h = list(map(int, input().split()))
    answer = 0
    for i in range(2, N - 2):
        side_max = max(h[i - 2], h[i - 1], h[i + 1], h[i + 2])
        if h[i] > side_max:
            answer += h[i] - side_max
    print(f"#{test_case} {answer}")