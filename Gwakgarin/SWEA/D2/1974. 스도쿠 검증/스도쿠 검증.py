T = int(input())
for test_case in range(1, T+1):
    arr = []
    for j in range(9):
        arr.append(list(map(int, input().split())))

    ans = 1

    for r in range(9):
        if len(set(arr[r])) != 9:
            ans = 0

    for c in range(9):
        col = []
        for r in range(9):
            col.append(arr[r][c])
        if len(set(col)) != 9:
            ans = 0

    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            box = []
            for a in range(3):
                for b in range(3):
                    box.append(arr[r + a][c + b])
            if len(set(box)) != 9:
                ans = 0

    print(f"#{test_case} {ans}")