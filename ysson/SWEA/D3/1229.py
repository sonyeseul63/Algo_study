# 명령어
# arr 중간 삭제 -> del, pop()
T = 10
for test_case in range(1, T+1):
    _ = input()
    origin = list(map(int, input().split()))
    n = int(input())
    exp = list(input().split())
    # 명령어 덩어리
    idx = 0
    for _ in range(n):
        command = exp[idx]
        if command == 'I':
            idx += 1
            pos = int(exp[idx])
            idx += 1
            cnt = int(exp[idx])
            idx += 1
            add = exp[idx:idx+cnt]
            origin[pos:pos] = add
            idx += cnt

        if command == 'D':
            idx += 1
            pos = int(exp[idx])
            idx += 1
            cnt = int(exp[idx])
            idx += 1
            del origin[pos:pos+cnt]

    res = " ".join(map(str, origin[:10]))
    print(f"#{test_case} {res}")