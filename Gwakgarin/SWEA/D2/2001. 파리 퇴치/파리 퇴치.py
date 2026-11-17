T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    arr = []
    for j in range(N):
        arr.append(list(map(int, input().split())))

    mx = 0
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            total = 0
            for a in range(M):
                for b in range(M):
                    total += arr[r + a][c + b]
            if total > mx:
                mx = total

    print(f"#{i + 1} {mx}")