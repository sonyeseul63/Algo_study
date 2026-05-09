# 완전탐색+구간합
T=int(input())
for test_case in range(1, T+1):
    # 입력값 처리
    n, m = map(int, input().split())
    arr = [ list(map(int, input().split())) for _ in range(n) ]
    # 구간합 구하기
    answer = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            total = 0
            for c in range(m):
                for r in range(m):
                    total += arr[i+r][j+c]
            answer = max(answer, total)
    #출력
    print(f"#{test_case} {answer}")