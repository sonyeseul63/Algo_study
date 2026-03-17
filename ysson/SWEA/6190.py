T = int(input())

# 단조 증가하는 수인지 체크하는 함수
def is_increased(num):
    num = str(num)
    for idx in range(len(num)-1):
        if num[idx] > num[idx+1]:
            return 0
    return 1


# 메인 : 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    max_num = -1

    # 숫자들의 조합 구하기
    for i in range(n-1):
        for j in range(i+1, n):
            cur = arr[i] * arr[j]
            if is_increased(cur):
                max_num = max(cur, max_num)

    print(f"#{test_case} {max_num}")