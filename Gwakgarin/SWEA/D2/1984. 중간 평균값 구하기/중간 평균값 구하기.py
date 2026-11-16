T = int(input())
for i in range(T):
    arr = list(map(int, input().split()))

    mx = max(arr)
    mn = min(arr)
    total = sum(arr) - mx - mn

    ans = int(total / 8 + 0.5) #반올림

    print(f"#{i + 1} {ans}")