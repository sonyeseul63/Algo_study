# 한번에 입력값들 입력 받고
# 끝에서부터 pop (그거보다 큰 값이 나오기 전까지 or 숫자 없을 떄까지)
# 스택


T = int(input())
for test_case in range(1, T+1):

    n = int(input())
    st = list(map(int, input().split()))
    max = st.pop()
    res = 0
    while(st):
        x = st.pop()
        if max > x:
            res += (max - x)
            continue
        elif max < x:
            max = x
            continue
    print(f'#{test_case} {res}')