# 인덱스 쓰임
# 1. 시작점으로 가능한 범위
# 2. 길이 
T = 1
for _ in range(1):
    test_case = int(input())
    target = input()
    n = len(target)
    st = input()
    cnt = 0
    for i in range(len(st)-n+1):
        if target[i:i+n] == target:
            cnt+=1
    print(f"#{test_case} {cnt}")