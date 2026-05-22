T = int(input())
for test_case in range(1, T+1):
    n = int(input())

    # 농장 입력
    farm = [list(map(int,input())) for _ in range(n)]
    answer = 0
    mid = n//2
    for i in range(n): #행 
        if i <= mid: 
            start = mid - i 
            end = mid + 1 + i
        else:
            start +=1
            end -=1

        for j in range(start, end):
            answer += farm[i][j]
    print(f"#{test_case} {answer}")