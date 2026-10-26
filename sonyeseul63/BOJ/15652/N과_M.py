N, M = map(int, input().split())
result = []
def bt(num, dept):
    if dept == M:
        print(" ".join(map(str,result)))
        return
    for i in range(1, N+1):
        if num <= i:
            result.append(i)
            bt(i, dept+1)
            result.pop()
bt(1, 0)