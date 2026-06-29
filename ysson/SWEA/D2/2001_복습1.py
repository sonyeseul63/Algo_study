T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    # 파리잡기 반복문
    answer = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            #파리채 영역
            res = 0
            for x in range(i, i+m):
                for y in range(j,j+m):
                    res += board[x][y]
            answer = max(answer, res)

    print(f"#{test_case} {answer}")