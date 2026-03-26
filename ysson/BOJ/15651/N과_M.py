N, M = map(int, input().split())
result=[]
def bt(dept):
    if dept == M:
        print(" ".join(map(str, result)))
        return
    for i in range(1, N+1): # 재귀적으로 result에 숫자 넣기
        result.append(i)
        bt(dept+1)
        result.pop()
bt(0)
