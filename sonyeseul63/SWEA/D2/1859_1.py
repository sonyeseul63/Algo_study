# 규칙
# append -> pop : 끝에서부터 
# 판단지점: 전 것이 현재거보다 클떄 차이 계산, 큰 것이 나오면 갱신

T = int(input())
for test_case in range(1, T+1):
    _ = input()
    stack = list(map(int, input().split()))
    target = stack.pop() # 현재까지의 큰 수
    money = 0
    while stack:
        cur = stack.pop()
        # 차익 실현
        if target > cur:
            money += target - cur
        # 더 큰 값 발견
        if target < cur:
            target = cur
    print(f"#{test_case} {money}")