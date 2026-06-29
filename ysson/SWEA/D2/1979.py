# 유효한 카운트 판단 시점: 연속이 끝났을 때 연속된 횟수 -> 검정 등장 혹은 끝났을 때
T = int(input())
for test_case in range(1, T+1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]

    # 가로 세기
    res = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0:
                if cnt == k:
                    res += 1
                cnt = 0
        if cnt == k:
            res += 1

    # 세로 세기
    for j in range(n):
        cnt = 0
        for i in range(n):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0:
                if cnt == k:
                    res += 1
                cnt = 0
        if cnt == k:
            res += 1
    print(f"#{test_case} {res}")