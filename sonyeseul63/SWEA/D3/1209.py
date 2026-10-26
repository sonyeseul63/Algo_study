T = 10
for test_case in range(1, T+1):
    # 배열 입력 받기
    _ = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_num = 0
    # 가로
    for row in range(100):
        cur_sum = sum(arr[row])
    #     for col in range(100):
    #         sum += arr[row][col]
        if max_num < cur_sum:
            max_num = cur_sum
    
    # 세로
    for col in range(100):
        cur_sum = sum(arr[row][col] for row in range(100)) 
    #     for row in range(100):
    #         sum += arr[row][col]
        if max_num < cur_sum:
            max_num = cur_sum

    # 대각선 (인덱스간의 규칙을 보면..)
    cur_sum = sum(arr[i][i] for i in range(100))
    if max_num < cur_sum:
        max_num = cur_sum
    
    cur_sum = sum(arr[i][99-i] for i in range(100))
    if max_num < cur_sum:
        max_num = cur_sum

    # 출력
    print(f"#{test_case} {max_num}")