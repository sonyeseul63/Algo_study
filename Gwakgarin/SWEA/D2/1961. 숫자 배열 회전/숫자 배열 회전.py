T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    for k in range(N):
        arr.append(list(map(int, input().split())))

    print(f"#{tc}")
    for i in range(N):
        a = ""
        b = ""
        c = ""
        for j in range(N):
            a += str(arr[N - 1 - j][i])
            b += str(arr[N - 1 - i][N - 1 - j])
            c += str(arr[j][N - 1 - i])
        print(a, b, c)