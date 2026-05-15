# stack으로 같은 숫자 나오면 pop
# stack[0]: 바닥, stack[-1]: 꼭대기
T = 10
for test_case in range(1, T+1):
    # 입력받을때 타입 주의
    n, st = input().split()
    n = int(n)
    pw = []
    for ch in st:
        if pw and pw[-1] == ch:
            pw.pop()
        else:
            pw.append(ch)
    res = "".join(map(str,pw))
    print(f"#{test_case} {res}")