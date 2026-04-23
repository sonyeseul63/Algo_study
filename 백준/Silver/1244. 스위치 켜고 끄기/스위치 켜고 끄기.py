# 입력
n = int(input())
arr = [0] + list(map(int, input().split())) # 인덱스 조정

# 전구 스위치 변경 함수
def change_s(s_n):
    return 1 - s_n

# 전구 일치 검사 함수
def check_s(s_n1, s_n2):
    if s_n1 == s_n2:
        return 1
    else:
        return 0

stu = int(input())
for _ in range(stu):
    g, s_i = map(int, input().split())

    # man
    if g == 1:
        for i in range(s_i, n+1, s_i):
            arr[i] = change_s(arr[i])
        # i = s_i
        # while i <= n:
        #     arr[i] = change_s(arr[i])
        #     i += s_i
        
    # woman
    if g == 2:
        l, r = s_i, s_i
        while True:
            if l-1 >= 1 and r+1 <= n:
                if check_s(arr[l-1], arr[r+1]):
                    l -= 1
                    r +=1
                else:
                    break
            else:
                break

        for i in range(l, r+1):
            arr[i] = change_s(arr[i])

for i in range(1, len(arr), 20):
    print(*arr[i:i+20])